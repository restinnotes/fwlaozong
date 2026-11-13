"""流程入口。用法见 README.md。

  python tools/run.py check                      两个账号就绪检查（不发模型请求）
  python tools/run.py oneshot --tag B0           基线：gpt3、gpt4 各 One-shot 一份 → out/B0_gpt3、out/B0_gpt4
  python tools/run.py system --tag S1            系统流水线：plan → search → screen → fetch → extract → synthesize → report
  python tools/run.py <单步> --tag S1            plan / search / screen / fetch / extract / synthesize / report 单独跑
  python tools/run.py refcheck --tag B0_gpt3     引用机械核验（PubMed / Europe PMC）
  python tools/run.py review --tag B0_gpt3       开放评审（GPT-6 + GPT-5.6）+ 绝对验收
  python tools/run.py blind --a B0_gpt3 --b S1   盲比，两种先后顺序 × 两位评委
  python tools/run.py stats                      知识库和调用统计
"""
import argparse, json, re, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch as F, kb, lit, llm
from llm import G6, G56

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"; OUT.mkdir(exist_ok=True)
P = lambda name: (ROOT / "prompts" / f"{name}.txt").read_text(encoding="utf-8")
WORKERS = 4
INLINE_MAX = 60000   # 提示词超过这个字数就改用附件（通道上限 65536）


def rd(p): return Path(p).read_text(encoding="utf-8-sig")
def wr(p, x):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(x if isinstance(x, str) else json.dumps(x, ensure_ascii=False, indent=1), encoding="utf-8")


def standard():
    rows = [l for l in rd(ROOT / "标准.md").splitlines() if re.match(r"\|\s*\d+\s*\|", l)]
    return "\n".join(f"{c[1].strip()}. {c[2].strip()}" for c in (r.split("|") for r in rows))


def question(args):
    return rd(ROOT / "questions" / f"{args.q}.md").strip()


def fill(tpl, **kw):
    for k, v in kw.items(): tpl = tpl.replace("{" + k + "}", v)
    return tpl


# ---------------- 基线 B0 ----------------

def split_report(ans):
    """One-shot 回答 → 正文 + 附录 JSON。"""
    app = None
    m = list(re.finditer(r"```json\s*(.*?)```", ans, re.S))
    if m:
        try: app = json.loads(m[-1].group(1)); body = ans[:m[-1].start()].rstrip()
        except ValueError: body = ans
    else:
        body = ans
    return body, app


def cmd_oneshot(args):
    """A 组：同一提示词 + 分轮说明（通道单次上限约 1770 秒，见猜想台账 P2），gpt3、gpt4 各一份。
    用户只交代一次任务；之后每轮只回复"继续"，不给内容，等价于 One-shot。"""
    msg = fill(P("oneshot"), QUESTION=question(args), STANDARD=standard()) + P("turns_note")
    print(f"One-shot 提示词 {len(msg)} 字", flush=True)
    def one(acct):
        tag = f"{args.tag}_{acct}"
        ans = llm.session(f"{tag}_{args.q}_oneshot_{llm.pid(msg)}", msg, model=G6, acct=acct, stage="oneshot", max_turns=args.max_turns)
        if not ans: print(tag, "无回答"); return
        clean = [a.replace("【完成】", "").replace("【继续】", "").strip() for a in ans]
        body, app = split_report(clean[-1])
        # 模型可能把报告分轮续写（最后一轮以"第 N 部分/第 N 轮"开头），这时成品是各轮拼起来
        if len(clean) > 1 and re.match(r"^#+\s*第\s*[二三四五六七八九十\d]+\s*(部分|轮|部)", body.lstrip()):
            body = "\n\n".join([split_report(x)[0] for x in clean[:-1]] + [body])
            print(tag, "最后一轮是续写，成品按各轮拼接", flush=True)
        wr(OUT / tag / "report.md", body); wr(OUT / tag / "raw.md", "\n\n=====（下一轮）=====\n\n".join(ans))
        if app: wr(OUT / tag / "appendix.json", app)
        print(tag, f"完成，{len(ans)} 轮，", "最后一轮有【完成】" if "【完成】" in ans[-1][-200:] else "到轮数上限未见【完成】",
              len(body), "字", "附录", "有" if app else "无", flush=True)
    with ThreadPoolExecutor(2) as ex: list(ex.map(one, ["gpt3", "gpt4"]))


# ---------------- 系统流水线 ----------------

def cmd_plan(args):
    q = question(args); msg = fill(P("plan"), QUESTION=q)
    ans = llm.call(f"{args.tag}_{args.q}_plan_{llm.pid(msg)}", msg, model=G6, stage="plan")
    d = llm.parse_json(ans); wr(OUT / args.tag / "plan.json", d)
    print(f"子问题 {len(d['subquestions'])}，检索式 {len(d['queries'])}，必读 {len(d['must_read'])}", flush=True)


def cmd_search(args):
    plan = json.loads(rd(OUT / args.tag / "plan.json")); c = kb.connect(); q = args.q
    found = set()
    for x in plan["queries"]:
        try: total, rs = lit.epmc_search(x["q"], max_n=args.per_query)
        except Exception as e: print("检索失败", x["q"][:80], e); continue
        ids = [kb.upsert_paper(c, r, "epmc") for r in rs if r.get("pmid") or r.get("doi")]
        found |= {i for i in ids if i}
        c.execute("INSERT INTO queries(question,engine,text,hit_count,kept,run_id,at) VALUES(?,?,?,?,?,?,?)",
                  (q, "epmc", x["q"], total, len(ids), args.tag, kb.now()))
        print(f"  {total:>6} 命中 取 {len(ids):>3}  {x['q'][:90]}", flush=True)
    c.commit()
    # 模型自己点名的必读文献：查真假，进库；同时看本地检索有没有覆盖到（检索层覆盖率的一个测量）
    seeds = []
    for m in plan.get("must_read", []):
        ident = m.get("pmid") or m.get("doi")
        r = lit.lookup(str(ident)) if ident else None
        pid = kb.upsert_paper(c, r, "model_seed") if r else None
        seeds.append({"given": m, "exists": bool(r), "pid": pid, "in_search": pid in found if pid else False,
                      "title_found": (r or {}).get("title")})
    c.commit()
    wr(OUT / args.tag / "search_seeds.json", seeds)
    ex = [s for s in seeds if s["exists"]]
    print(f"检索去重后 {len(found)} 篇；模型点名必读 {len(seeds)} 篇，查得到 {len(ex)}，"
          f"其中本地检索已覆盖 {sum(s['in_search'] for s in ex)}", flush=True)
    wr(OUT / args.tag / "pool.json", sorted(found | {s["pid"] for s in ex}))


def paper_brief(p, abs_chars=1400):
    a = (p["abstract"] or "")[:abs_chars]
    return f"pid: {p['pid']}\n题目: {p['title']}\n年份: {p['year']}  类型: {p['pub_type'] or ''}\n摘要: {a or '（无摘要）'}"


def cmd_screen(args):
    c = kb.connect(); q = question(args); pool = json.loads(rd(OUT / args.tag / "pool.json"))
    done = {r["pid"] for r in c.execute("SELECT pid FROM screening WHERE question=? AND run_id=?", (args.q, args.tag))}
    todo = [p for p in pool if p not in done]
    papers = {r["pid"]: r for r in c.execute(f"SELECT * FROM papers WHERE pid IN ({','.join('?' * len(todo))})", todo)} if todo else {}
    batches = [todo[i:i + args.batch] for i in range(0, len(todo), args.batch)]
    print(f"待筛 {len(todo)} 篇，{len(batches)} 批", flush=True)
    def one(b):
        body = "\n\n---\n\n".join(paper_brief(papers[p]) for p in b if p in papers)
        msg = fill(P("screen"), QUESTION=q, PAPERS=body)
        ans = llm.call(f"{args.tag}_{args.q}_screen_{llm.pid(msg)}", msg, model=G6, stage="screen")
        try: return llm.parse_json(ans)["items"]
        except Exception as e: print("筛选结果解析失败", e); return []
    with ThreadPoolExecutor(WORKERS) as ex:
        for items in ex.map(one, batches):
            for it in items:
                if it.get("pid") in papers:
                    c.execute("INSERT OR REPLACE INTO screening VALUES(?,?,?,?,?,?)",
                              (args.q, it["pid"], it.get("decision"), it.get("reason"), args.tag, kb.now()))
            c.commit()
    cnt = dict(c.execute("SELECT decision, COUNT(*) FROM screening WHERE question=? AND run_id=? GROUP BY decision",
                         (args.q, args.tag)).fetchall())
    print("筛选结果", cnt, flush=True)


def selected(c, args, decisions=("include",)):
    return [r["pid"] for r in c.execute(
        f"SELECT pid FROM screening WHERE question=? AND run_id=? AND decision IN ({','.join('?' * len(decisions))})",
        (args.q, args.tag, *decisions))]


def cmd_fetch(args):
    c = kb.connect(); pids = selected(c, args)
    tiers = tiers_of(args)
    if tiers: pids = [p for p in pids if tiers.get(p) == "A"]; print(f"按分层只给 A 层取全文：{len(pids)} 篇", flush=True)
    n = F.fetch(c, pids, use_luna=not args.no_luna)
    print(f"纳入 {len(pids)} 篇，有全文 {n} 篇", flush=True)


def fulltext_of(p, limit=55000):
    f = p["fulltext_path"]
    if not f or not Path(f).exists(): return None, None
    if f.endswith(".txt"): return Path(f).read_text(encoding="utf-8")[:limit], None
    return None, f   # PDF / HTML：作为附件上传


def cmd_extract(args):
    c = kb.connect(); q = question(args)
    inc = selected(c, args); mb = selected(c, args, ("maybe",))
    have = {r["pid"] for r in c.execute("SELECT DISTINCT pid FROM evidence WHERE question=? AND run_id=?", (args.q, args.tag))}
    rows = {r["pid"]: r for r in c.execute(f"SELECT * FROM papers WHERE pid IN ({','.join('?' * len(inc + mb))})", inc + mb)} if inc + mb else {}
    jobs = []
    abstract_only = []
    tiers = tiers_of(args)
    for pid in inc:
        if pid in have or pid not in rows: continue
        txt, att = fulltext_of(rows[pid])
        if (txt or att) and (not tiers or tiers.get(pid) == "A"): jobs.append(("full", [pid], txt, att))
        else: abstract_only.append(pid)
    if tiers: mb = []   # 有分层的版本没有"待定"（S4R 已终判），也不读待定文献
    abstract_only += [p for p in mb if p not in have and p in rows]
    for i in range(0, len(abstract_only), 20):
        jobs.append(("abs", abstract_only[i:i + 20], None, None))
    print(f"提取：全文 {sum(j[0] == 'full' for j in jobs)} 篇，摘要批 {sum(j[0] == 'abs' for j in jobs)} 批", flush=True)
    def one(job):
        kind, pids, txt, att = job
        if kind == "full":
            p = rows[pids[0]]
            body = f"pid: {p['pid']}\n题目: {p['title']}\n年份: {p['year']}\n" + (
                f"全文：\n{txt}" if txt else "全文见附件。")
        else:
            body = "\n\n---\n\n".join(paper_brief(rows[x], 3000) for x in pids)
        v2 = args.extract_prompt == "extract_v2"
        msg = fill(P(args.extract_prompt), QUESTION=q, PAPERS=body)
        if v2 and kind == "abs":   # 设定登记 #11：v2 提示词按单篇设计，摘要批次只做格式适配
            msg += ("\n\n【格式适配】本次给了多篇论文（都只有摘要，basis 一律写 abstract）。请对每篇分别按上面的格式输出，"
                    "publication.ref 照抄该篇的 pid，最外层写成 {\"papers\": [ {\"publication\": {...}, \"evidence\": [...]}, ... ]}。")
        ans = llm.call(f"{args.tag}_{args.q}_extract_{llm.pid(msg + (att or ''))}", msg, attach=[att] if att else (),
                       model=G6, stage="extract-" + kind)
        try:
            d = llm.parse_json(ans)
            if not v2: return [(p, None, e) for e in d["evidence"] for p in [e.get("pid") if e.get("pid") in pids else pids[0]]]
            items = d.get("papers") or [d]
            out = []
            for it in items:
                pub = it.get("publication") or {}
                pid = pub.get("ref") if pub.get("ref") in pids else (pids[0] if len(pids) == 1 else None)
                if pid is None: continue
                out += [(pid, pub, e) for e in it.get("evidence", [])]
            return out
        except Exception as e: print("提取解析失败", pids[:2], e); return []
    with ThreadPoolExecutor(WORKERS) as ex:
        for res in ex.map(one, jobs):
            for pid, pub, e in res:
                n = c.execute("SELECT COUNT(*) FROM evidence WHERE pid=? AND run_id=?", (pid, args.tag)).fetchone()[0]
                eid = f"E_{F.safe_key(pid)}_{n + 1}" if args.tag == "S1" else f"{args.tag}_E_{F.safe_key(pid)}_{n + 1}"
                if pub is None:
                    vals = (e.get("design"), e.get("population"), str(e.get("n") or ""), e.get("condition"), e.get("measure"),
                            e.get("finding"), e.get("effect"), e.get("limitations"), e.get("quote"), e.get("basis"), None)
                else:   # v2：分母、终点/阶段、条件拼进原有列（给旧代码和人看），完整字段存 extra
                    den = "; ".join(f"{k}={e[k]}" for k in ("n_enrolled", "n_analyzed", "n_patients_with_FOG", "n_patients_with_valid_neural_data",
                                                             "n_FOG_events", "n_trials", "n_electrodes_contacts") if e.get(k) not in (None, "", "unknown"))
                    cond = "; ".join(f"{k}:{e[k]}" for k in ("endpoint_class", "event_phase", "freezing_phenotype", "medication_phenotype",
                                                             "experimental_medication_state", "DBS_state_and_parameters", "task", "recording_location")
                                     if e.get(k) not in (None, "", "unknown"))
                    rob = (e.get("risk_of_bias") or {}).get("overall")
                    vals = (e.get("design"), e.get("population"), den, cond,
                            " | ".join(x for x in (e.get("measure"), e.get("frequency_and_analysis_window")) if x),
                            e.get("finding"), " | ".join(x for x in (e.get("effect_estimate"), e.get("statistical_unit_and_method")) if x),
                            (e.get("limitations") or "") + (f"（偏倚风险总体：{rob}）" if rob else ""), e.get("quote"), e.get("basis"),
                            json.dumps({"publication": pub, "evidence": e}, ensure_ascii=False))
                    if pub.get("publication_status"):
                        c.execute("UPDATE papers SET publication_status=? WHERE pid=?", (pub["publication_status"], pid))
                c.execute("INSERT OR REPLACE INTO evidence(eid,question,pid,design,population,n,condition,measure,finding,"
                          "effect,limitations,quote,basis,extra,run_id,at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                          (eid, args.q, pid, *vals, args.tag, kb.now()))
                kb.hist(c, "evidence", eid, "add", {"pid": pid}, args.tag)
            c.commit()
    print("证据条数", c.execute("SELECT COUNT(*) FROM evidence WHERE question=? AND run_id=?", (args.q, args.tag)).fetchone()[0])


def evidence_rows(c, args):
    return list(c.execute("SELECT e.*, p.title, p.year, p.version_of FROM evidence e JOIN papers p USING(pid) WHERE e.question=? AND e.run_id=? "
                          "ORDER BY p.year, e.pid", (args.q, args.tag)))


PREPRINT_DOI = ("10.1101/", "10.64898/", "10.21203/", "10.2139/", "10.20944/", "10.31234/", "10.48550/")


def is_preprint(p):
    return (p["doi"] or "").lower().startswith(PREPRINT_DOI) or (p["publication_status"] or "") == "preprint"


def cmd_versions(args):
    """S3c / P6：预印本与正式版关联。只在标题相似度 ≥0.9 时建立 version_of（不确定的不合并，顾问要求）。"""
    c = kb.connect()
    pids = [r["pid"] for r in c.execute("SELECT DISTINCT pid FROM screening WHERE run_id=? AND decision IN ('include','maybe')", (kbtag(args),))]
    rows = list(c.execute(f"SELECT * FROM papers WHERE pid IN ({','.join('?' * len(pids))})", pids))
    allp = list(c.execute("SELECT * FROM papers"))
    n = 0
    for p in rows:
        if not is_preprint(p): continue
        best, s = None, 0
        for q in allp:
            if q["pid"] == p["pid"] or is_preprint(q): continue
            v = title_sim(p["title"], q["title"]) or 0
            if v > s: best, s = q, v
        if best is not None and s >= 0.9:
            c.execute("UPDATE papers SET version_of=? WHERE pid=?", (best["pid"], p["pid"])); n += 1
            kb.hist(c, "papers", p["pid"], "version_of", {"published": best["pid"], "title_sim": round(s, 2)}, args.tag)
            print(f"  预印本 {p['pid']} → 正式版 {best['pid']}（标题相似 {s:.2f}）", flush=True)
    c.commit()
    print(f"纳入/待定文献 {len(rows)} 篇，其中预印本 {sum(is_preprint(p) for p in rows)} 篇，关联到正式版 {n} 篇", flush=True)


def evidence_line(r, k=400):
    f = lambda x: (x or "")[:k]
    s = (f"[{r['eid']}] {r['pid']} ({r['year']}) {f(r['title'])}\n  设计:{f(r['design'])} | 对象:{f(r['population'])} | n={r['n']} | "
         f"条件:{f(r['condition'])} | 测量:{f(r['measure'])}\n  发现:{f(r['finding'])} | 效应:{f(r['effect'])} | "
         f"局限:{f(r['limitations'])} | 依据:{r['basis']}")
    keys = r.keys()
    if "extra" in keys and r["extra"]:   # S3c：研究级账本字段
        x = json.loads(r["extra"]); pub, e = x.get("publication") or {}, x.get("evidence") or {}
        rob = e.get("risk_of_bias") or {}
        doms = "; ".join(f"{d.get('domain')}={d.get('judgement')}" for d in (rob.get("domains") or [])[:8])
        s += (f"\n  研究账本：发表状态={pub.get('publication_status')} | 来源类型={pub.get('source_type')} | 研究候选={pub.get('study_id_candidate')}"
              f" | 队列候选={pub.get('cohort_id_candidate')}（{f(pub.get('cohort_relation_basis'))}）"
              f"\n  偏倚风险（{rob.get('tool_or_framework')}）总体={rob.get('overall')}：{f(doms)}")
    if "version_of" in keys and r["version_of"]:
        s += f"\n  版本：这是 {r['version_of']} 的预印本版本，与之是同一研究，不能计为独立证据"
    return s


def evidence_text(c, args, limit=58000):
    """S1 用过的单次综合输入。11-13 起：放不下就报错，不再从尾部静默截断
    （S1 因此只把 544 条里最旧的 92 条送进综合，2023–2026 年的 351 条全丢，猜想台账 P4）。"""
    rows = evidence_rows(c, args)
    for k in (400, 250, 160, 100):
        t = "\n".join(evidence_line(r, k) for r in rows)
        if len(t) <= limit: return t, len(rows)
    raise RuntimeError(f"证据 {len(rows)} 条放不进一次综合（{len(t)} 字 > {limit}），请用分片综合")


def cmd_synthesize(args):
    c = kb.connect(); rows = evidence_rows(c, args)
    single = "\n".join(evidence_line(r) for r in rows)
    if len(single) <= 52000 and not args.map_reduce:
        msg = fill(P("synthesize"), QUESTION=question(args), STANDARD=standard(), EVIDENCE=single)
        print(f"综合（一次）：证据 {len(rows)} 条，提示词 {len(msg)} 字", flush=True)
        d = llm.parse_json(llm.call(f"{args.tag}_{args.q}_synth_{llm.pid(msg)}", msg, model=G6, stage="synthesize"))
    else:
        d = synth_map_reduce(c, args, rows)
    store_synthesis(c, args, d)


def synth_map_reduce(c, args, rows, chunk_chars=48000):
    """分片综合：全部证据按年份顺序切片（每片 ≤ chunk_chars），每片单独出局部结论，最后一次合并成最终结论和假说。
    保证每一条证据都进过某一次综合。"""
    chunks, cur, n = [], [], 0
    for r in rows:
        s = evidence_line(r)
        if n + len(s) > chunk_chars and cur: chunks.append(cur); cur, n = [], 0
        cur.append((r, s)); n += len(s) + 1
    if cur: chunks.append(cur)
    N = len(chunks); q = question(args)
    spans = [f"{ch[0][0]['year']}–{ch[-1][0]['year']}" for ch in chunks]
    print(f"分片综合：证据 {len(rows)} 条 → {N} 片（年份 {spans}）", flush=True)
    def one(i):
        ch = chunks[i]
        msg = fill(P("synth_map"), QUESTION=q, EVIDENCE="\n".join(s for _, s in ch)).replace("{I}", str(i + 1)).replace("{N}", str(N))
        ans = llm.call(f"{args.tag}_{args.q}_synthmap{i + 1}_{llm.pid(msg)}", msg, model=G6, stage="synth-map")
        try: return llm.parse_json(ans)["claims"]
        except Exception as e: print(f"第 {i + 1} 片解析失败", e); return None
    with ThreadPoolExecutor(WORKERS) as ex: parts = list(ex.map(one, range(N)))
    if any(p is None for p in parts): raise RuntimeError(f"有分片综合失败：{[i + 1 for i, p in enumerate(parts) if p is None]}")
    wr(OUT / args.tag / "synth_parts.json", parts)
    # 证据关联不交给模型抄：每条局部结论的证据由程序记住，合并时模型只写 from，程序按 from 把证据并上去（11-13：带证据列表的合并输入 11 万字放不下）
    year = {r["eid"]: r["year"] for r in rows}
    pool = {cl["cid"]: cl for p in parts for cl in p}
    def evid(cl):
        return cl.get("evidence", [])
    def line(cl, k):
        ys = sorted(year.get(e.get("eid")) or 0 for e in evid(cl)) or [0]
        return (f"[{cl['cid']}] [{cl.get('level')}/{cl.get('status')}] {(cl.get('text') or '')[:k]} ｜不确定性:{(cl.get('uncertainty') or '')[:k // 3]}"
                f" ｜证据 {len(evid(cl))} 条，{ys[0]}–{ys[-1]}")
    def resolve(new, old_pool, label):
        """按 from 把证据并上；没被任何新结论引用的旧结论原样保留（不丢）。"""
        used, out = set(), []
        for cl in new:
            ev, seen = [], set()
            for f in cl.get("from", []):
                if f in old_pool:
                    used.add(f)
                    for e in evid(old_pool[f]):
                        if e.get("eid") not in seen: seen.add(e.get("eid")); ev.append(e)
            cl["evidence"] = ev; out.append(cl)
        orphan = [old_pool[k] for k in old_pool if k not in used]
        if orphan: print(f"{label}：{len(orphan)} 条局部结论没被引用，原样保留", flush=True)
        return out + orphan
    def pack(cls, k, limit):
        groups, cur, n = [], [], 0
        for cl in cls:
            s = line(cl, k)
            if n + len(s) > limit and cur: groups.append(cur); cur, n = [], 0
            cur.append(cl); n += len(s) + 1
        if cur: groups.append(cur)
        return groups
    claims = list(pool.values()); level = 0
    while True:
        k = 500
        msg = fill(P("synth_reduce"), QUESTION=q, STANDARD=standard(), CLAIMS="\n".join(line(cl, k) for cl in claims)) \
            .replace("{NE}", str(len(rows))).replace("{NP}", str(len({r['pid'] for r in rows}))).replace("{N}", str(N))
        if len(msg) <= 60000: break
        level += 1
        groups = pack(claims, k, 45000)
        print(f"第 {level} 级分组合并：{len(claims)} 条 → {len(groups)} 组", flush=True)
        def merge(i):
            g = groups[i]
            m = fill(P("synth_merge"), QUESTION=q, CLAIMS="\n".join(line(cl, k) for cl in g)).replace("{G}", f"{level}_{i + 1}").replace("{NG}", str(len(groups)))
            try: return llm.parse_json(llm.call(f"{args.tag}_{args.q}_synthmerge{level}_{i + 1}_{llm.pid(m)}", m, model=G6, stage="synth-merge"))["claims"]
            except Exception as e: print(f"第 {level} 级第 {i + 1} 组合并失败", e); return None
        with ThreadPoolExecutor(WORKERS) as ex: merged = list(ex.map(merge, range(len(groups))))
        if any(m is None for m in merged): raise RuntimeError("分组合并有失败")
        old = {cl["cid"]: cl for cl in claims}
        claims = resolve([x for m in merged for x in m], old, f"第 {level} 级")
        wr(OUT / args.tag / f"synth_merge{level}.json", claims)
        if level >= 3: raise RuntimeError(f"三级合并后仍放不下（{len(claims)} 条）")
    print(f"最终合并：{len(claims)} 条结论，提示词 {len(msg)} 字", flush=True)
    d = llm.parse_json(llm.call(f"{args.tag}_{args.q}_synthreduce_{llm.pid(msg)}", msg, model=G6, stage="synth-reduce"))
    d["claims"] = resolve(d["claims"], {cl["cid"]: cl for cl in claims}, "最终合并")
    # 最终结论只保留 C 编号的；没被引用、原样保留的中间结论另放，免得混进报告
    d["unmerged"] = [cl for cl in d["claims"] if not re.match(r"^C\d+$", str(cl.get("cid")))]
    d["claims"] = [cl for cl in d["claims"] if re.match(r"^C\d+$", str(cl.get("cid")))]
    n_ev = len({e.get("eid") for cl in d["claims"] for e in cl["evidence"]})
    print(f"最终结论 {len(d['claims'])} 条，覆盖证据 {n_ev}/{len(rows)} 条；未被合并引用的中间结论 {len(d['unmerged'])} 条", flush=True)
    return d


def store_synthesis(c, args, d):
    wr(OUT / args.tag / "synthesis.json", d)
    valid = {r["eid"] for r in c.execute("SELECT eid FROM evidence WHERE run_id=?", (args.tag,))}
    bad = 0
    for cl in d.get("claims", []):
        cid = f"{args.tag}_{cl['cid']}"
        c.execute("INSERT OR REPLACE INTO claims(cid,question,text,level,status,uncertainty,superseded_by,run_id,at) VALUES(?,?,?,?,?,?,?,?,?)",
                  (cid, args.q, cl.get("text"), cl.get("level"), cl.get("status"), cl.get("uncertainty"), None, args.tag, kb.now()))
        for e in cl.get("evidence", []):
            if e.get("eid") not in valid: bad += 1; continue
            c.execute("INSERT OR REPLACE INTO claim_evidence VALUES(?,?,?,?)", (cid, e["eid"], e.get("relation"), e.get("note")))
    for h in d.get("hypotheses", []):
        hid = f"{args.tag}_{h['hid']}"
        c.execute("INSERT OR REPLACE INTO hypotheses(hid,question,name,text,predictions,falsifiers,status,superseded_by,run_id,at) VALUES(?,?,?,?,?,?,?,?,?,?)",
                  (hid, args.q, h.get("name"), h.get("text"), json.dumps(h.get("predictions"), ensure_ascii=False),
                   json.dumps(h.get("falsifiers"), ensure_ascii=False), "proposed", None, args.tag, kb.now()))
        for x in h.get("claims", []):
            c.execute("INSERT OR REPLACE INTO hypothesis_claims VALUES(?,?,?)", (hid, f"{args.tag}_{x['cid']}", x.get("relation")))
    c.commit()
    print(f"结论 {len(d.get('claims', []))}，假说 {len(d.get('hypotheses', []))}，缺口 {len(d.get('gaps', []))}，"
          f"引用了库里没有的证据编号 {bad} 处", flush=True)


def kb_text(c, args, limit=60000):
    syn = json.loads(rd(syn_path(args)))
    used = {e["eid"] for cl in syn["claims"] for e in cl.get("evidence", [])}
    ev = {r["eid"]: r for r in c.execute("SELECT e.*, p.title, p.year, p.authors FROM evidence e JOIN papers p USING(pid) WHERE e.run_id=?", (kbtag(args),))}
    parts = ["## 结论与假说\n" + json.dumps({"claims": syn["claims"], "hypotheses": syn["hypotheses"], "gaps": syn.get("gaps", [])}, ensure_ascii=False)]
    for n in (None, 300, 200, 120):
        f = (lambda x: x or "") if n is None else (lambda x, n=n: (x or "")[:n])
        lines = [f"[{k}] 文献 {r['pid']}（{(r['authors'] or '').split(',')[0]} {r['year']}，{f(r['title'])}）| 条件:{f(r['condition'])} | 测量:{f(r['measure'])} | 发现:{f(r['finding'])} | 局限:{f(r['limitations'])} | 依据:{r['basis']}"
                 for k, r in ev.items() if k in used]
        t = "\n".join(parts) + "\n\n## 结论引用的证据\n" + "\n".join(lines)
        if len(t) <= limit:
            if n: print(f"写报告输入：证据字段截到 {n} 字才放下", flush=True)
            return t
    raise RuntimeError(f"写报告输入超长 {len(t)} 字（结论 {len(syn['claims'])} 条、证据 {len(lines)} 条），不静默截断")


def kbtag(args):
    """证据和筛选从哪个版本取（--kb，只改写报告/审计等下游步骤的变体沿用上游版本的知识库）。"""
    return getattr(args, "kb", None) or args.tag


def syn_path(args):
    p = OUT / args.tag / "synthesis.json"
    return p if p.exists() else OUT / kbtag(args) / "synthesis.json"


def build_methods(c, args):
    """S3a（顾问 g56"检索账本入报告"、g6"Recall First"第四节）：检索与筛选过程全部由程序从运行记录生成，模型不填数字。"""
    src = kbtag(args)
    lineage = [src]
    while (OUT / lineage[-1] / "plan.json").exists() and lineage[-1] != "S1" and len(lineage) < 5:
        lineage.append("S1")   # 目前所有 S 版本的检索都在 S1 跑（fork 沿用）
    qrun = lineage[-1]
    qs = list(c.execute("SELECT text, hit_count, kept, at FROM queries WHERE run_id=? AND question=? ORDER BY qid", (qrun, args.q)))
    pool = json.loads(rd(OUT / src / "pool.json")) if (OUT / src / "pool.json").exists() else []
    seeds = json.loads(rd(OUT / src / "search_seeds.json")) if (OUT / src / "search_seeds.json").exists() else []
    scr = dict(c.execute("SELECT decision, COUNT(*) FROM screening WHERE run_id=? AND question=? GROUP BY decision", (src, args.q)).fetchall())
    inc = [r["pid"] for r in c.execute("SELECT pid FROM screening WHERE run_id=? AND question=? AND decision='include'", (src, args.q))]
    kinds = {}
    for r in c.execute(f"SELECT fulltext_kind FROM papers WHERE pid IN ({','.join('?' * len(inc))})", inc) if inc else []:
        kinds[r[0] or "无全文（只有摘要）"] = kinds.get(r[0] or "无全文（只有摘要）", 0) + 1
    nev = c.execute("SELECT COUNT(*), COUNT(DISTINCT pid) FROM evidence WHERE run_id=?", (src,)).fetchone()
    lp = ROOT / "runs" / "luna_calls.jsonl"
    luna = [json.loads(l) for l in lp.read_text(encoding="utf-8").splitlines()] if lp.exists() else []
    date = (qs[0]["at"] or "")[:10] if qs else "unknown"
    L = ["### 检索与筛选记录（程序根据运行日志生成，数字未经模型改写）", "",
         f"- 综述类型：结构化叙述性证据综合（structured narrative evidence synthesis）；未按 PRISMA 系统综述方案预注册和双人独立筛选，不是系统综述或 Meta 分析。",
         f"- 检索日期：{date}；数据库：Europe PMC REST API（收录 PubMed/MEDLINE、PMC、预印本）。没有检索 Embase、Scopus、Web of Science、Cochrane。",
         f"- 检索式：{len(qs)} 条，由模型根据研究问题拟定；每条按 Europe PMC 相关度排序取前 {max((q['kept'] for q in qs), default=0)} 条（命中数超过时被截断，见下表）。",
         f"- 模型联网点名的必读文献：{len(seeds)} 篇，查得到 {sum(s['exists'] for s in seeds)} 篇，其中本地检索已覆盖 {sum(s.get('in_search') for s in seeds if s['exists'])} 篇；两路合并去重后进入筛选 {len(pool)} 篇。",
         f"- 题目+摘要筛选（GPT-6，每批 30 篇）：纳入 {scr.get('include', 0)}，待定 {scr.get('maybe', 0)}，排除 {scr.get('exclude', 0)}。",
         f"- 纳入文献的全文获取：" + "；".join(f"{k} {v} 篇" for k, v in sorted(kinds.items())) + f"（下载辅助调用 {len(luna)} 次，只用合法开放来源）。",
         f"- 证据提取：{nev[1]} 篇文献提取出 {nev[0]} 条证据（纳入文献有全文的读全文，其余和待定文献读摘要）。",
         "", "| # | 检索式 | 命中数 | 取回 | 是否截断 |", "|---|---|---|---|---|"]
    for i, q in enumerate(qs, 1):
        L.append(f"| {i} | `{q['text'].replace('|', '/')}` | {q['hit_count']} | {q['kept']} | {'是' if q['hit_count'] > q['kept'] else '否'} |")
    return "\n".join(L)


def cmd_report(args):
    c = kb.connect(); att = []; src = kbtag(args)
    try:
        kbt = kb_text(c, args)
    except RuntimeError as e:
        # 放不下：结论/假说内联（证据只写编号），完整证据表作附件（不删减）
        print("写报告输入改为附件：", e, flush=True)
        syn = json.loads(rd(syn_path(args)))
        used = list(dict.fromkeys(e["eid"] for cl in syn["claims"] for e in cl.get("evidence", [])))
        ev = {r["eid"]: r for r in c.execute("SELECT e.*, p.title, p.year, p.authors FROM evidence e JOIN papers p USING(pid) WHERE e.run_id=?", (src,))}
        tbl = OUT / args.tag / "evidence_table.txt"
        wr(tbl, "\n".join(f"[{k}] 文献 {ev[k]['pid']}（{(ev[k]['authors'] or '').split(',')[0]} {ev[k]['year']}，{ev[k]['title']}）| 设计:{ev[k]['design']} | 对象:{ev[k]['population']} | n={ev[k]['n']} | 条件:{ev[k]['condition']} | 测量:{ev[k]['measure']} | 发现:{ev[k]['finding']} | 效应:{ev[k]['effect']} | 局限:{ev[k]['limitations']} | 依据:{ev[k]['basis']}"
                          for k in used if k in ev))
        compact = {"claims": [{**{x: cl.get(x) for x in ("cid", "text", "level", "status", "uncertainty")},
                               "evidence": [f"{e['eid']}:{(e.get('relation') or '')[:4]}" for e in cl.get("evidence", [])]} for cl in syn["claims"]],
                   "hypotheses": syn["hypotheses"], "gaps": syn.get("gaps", [])}
        kbt = ("## 结论与假说（每条结论的 evidence 是证据编号:关系；证据全文见附件 evidence_table.txt，"
               f"共 {len(used)} 条，按编号查）\n" + json.dumps(compact, ensure_ascii=False))
        att = [tbl]
    msg = fill(P("report"), QUESTION=question(args), STANDARD=standard(), KB=kbt)
    if len(msg) > INLINE_MAX - 3000:
        # 第三层（11-13 S3d2：整份作附件时正文把 13 个假说压成 7 个宽泛模型，综合盲比 0:4）：
        # 结论文字、假说、缺口内联；"结论→证据编号"映射和证据表作附件
        syn = json.loads(rd(syn_path(args)))
        cmap = OUT / args.tag / "claim_evidence_map.md"
        wr(cmap, "\n".join(f"{cl['cid']}: " + "; ".join(f"{e['eid']}:{(e.get('relation') or '')[:4]}" for e in cl.get("evidence", [])) for cl in syn["claims"]))
        inline = {"claims": [{k: cl.get(k) for k in ("cid", "text", "level", "status", "uncertainty", "applies_to")} for cl in syn["claims"]],
                  "hypotheses": syn["hypotheses"], "gaps": syn.get("gaps", [])}
        kbt3 = ("## 结论（文字和强度；每条结论的证据编号见附件 claim_evidence_map.md，证据内容见附件 evidence_table.txt）、假说、缺口\n"
                + json.dumps(inline, ensure_ascii=False))
        msg3 = fill(P("report"), QUESTION=question(args), STANDARD=standard(), KB=kbt3)
        if len(msg3) <= INLINE_MAX - 3000:
            msg, att = msg3, att + [cmap]
            print(f"写报告：结论文字/假说/缺口内联 {len(kbt3)} 字，证据映射和证据表作附件", flush=True)
    if len(msg) > INLINE_MAX - 3000:   # 第四层：结论/假说本身也放不下：整份结构化知识作附件（不删减）
        kbf = OUT / args.tag / "kb_for_report.md"; wr(kbf, kbt)
        att = att + [kbf]
        msg = fill(P("report"), QUESTION=question(args), STANDARD=standard(),
                   KB="（结构化知识——全部结论、假说、缺口及其证据编号——见附件 kb_for_report.md；每条证据的内容见附件 evidence_table.txt。请完整读完再写。）")
        print(f"写报告：结构化知识 {len(kbt)} 字改为附件", flush=True)
    methods = None
    if args.with_methods:
        methods = build_methods(c, args); wr(OUT / args.tag / "methods.md", methods)
        inline = methods
        if len(msg) + len(methods) + 400 > INLINE_MAX:   # 检索式表格放附件，要点内联
            inline = methods.split("\n| # |")[0] + "\n（各条检索式的命中数和截断情况见附件 methods.md 的表格）"
            att = att + [OUT / args.tag / "methods.md"]
        msg += ("\n\n【检索与筛选记录（程序根据运行日志生成，数字准确）】\n" + inline +
                "\n\n写报告时：开头写明本报告的类型和边界（结构化叙述性证据综合，不是 PRISMA 系统综述）；方法一节只能依据上面的记录写，"
                "不得添加没有使用的数据库、步骤或数字；记录里检索被截断的地方要如实说明对覆盖的影响。程序会把这份记录原样附在报告末尾。")
    if len(msg) > INLINE_MAX: raise RuntimeError(f"写报告提示词仍超长 {len(msg)}")
    ans = llm.call(f"{args.tag}_{args.q}_report_{llm.pid(msg)}", msg, attach=att, model=G6, stage="report")
    if methods: ans = ans.rstrip() + "\n\n" + methods + "\n"
    wr(OUT / args.tag / "report.md", ans)
    export_appendix(c, args)
    print(args.tag, "报告", len(ans), "字", flush=True)


def export_appendix(c, args):
    """和 B0 同一格式的结构化附录，从知识库导出（结论引用到的证据、文献）。"""
    syn = json.loads(rd(syn_path(args)))
    used = [e["eid"] for cl in syn["claims"] for e in cl.get("evidence", [])]
    ev = {r["eid"]: r for r in c.execute("SELECT * FROM evidence WHERE run_id=?", (kbtag(args),))}
    used = [x for x in dict.fromkeys(used) if x in ev]
    pids = list(dict.fromkeys(ev[x]["pid"] for x in used))
    papers = {r["pid"]: r for r in c.execute(f"SELECT * FROM papers WHERE pid IN ({','.join('?' * len(pids))})", pids)} if pids else {}
    app = {"references": [{"ref": p, "pmid": papers[p]["pmid"] or "", "doi": papers[p]["doi"] or "", "title": papers[p]["title"], "year": papers[p]["year"]} for p in pids if p in papers],
           "evidence": [{"eid": x, "ref": ev[x]["pid"], **{k: ev[x][k] for k in ("design", "population", "n", "condition", "measure", "finding", "limitations", "quote", "basis")}} for x in used],
           "claims": syn["claims"], "hypotheses": syn["hypotheses"], "gaps": syn.get("gaps", [])}
    wr(OUT / args.tag / "appendix.json", app)
    print(f"附录：文献 {len(app['references'])}，证据 {len(app['evidence'])}，结论 {len(app['claims'])}，假说 {len(app['hypotheses'])}", flush=True)


def cmd_system(args):
    for step in (cmd_plan, cmd_search, cmd_screen, cmd_fetch, cmd_extract, cmd_synthesize, cmd_report):
        print(f"===== {step.__name__[4:]} =====", flush=True)
        if step is cmd_plan and (OUT / args.tag / "plan.json").exists(): print("已有 plan.json，跳过"); continue
        if step is cmd_search and (OUT / args.tag / "pool.json").exists(): print("已有 pool.json，跳过"); continue
        step(args)


# ---------------- 测量 ----------------

def full_report(tag):
    """评审、盲比看的成品：正文 + 结构化附录（11-13：只给正文时评委把"附录缺失"判成头号大问题，测法错）。"""
    body = rd(OUT / tag / "report.md")
    app = OUT / tag / "appendix.json"
    if app.exists():
        body += "\n\n## 结构化附录（JSON）\n\n```json\n" + json.dumps(json.loads(rd(app)), ensure_ascii=False) + "\n```\n"
    wr(OUT / tag / "report_full.md", body)
    return body




def cited_ids(tag):
    """报告里引用的文献标识：附录 references，或正文里的 [PMID:x] / [DOI:x]。"""
    ids = []
    app = OUT / tag / "appendix.json"
    if app.exists():
        for r in json.loads(rd(app)).get("references", []):
            ids.append({"ref": r.get("ref"), "pmid": str(r.get("pmid") or "").strip(), "doi": (r.get("doi") or "").strip(),
                        "title": r.get("title")})
    else:
        t = rd(OUT / tag / "report.md")
        for m in sorted(set(re.findall(r"PMID:\s*(\d{5,9})", t))): ids.append({"ref": "PMID:" + m, "pmid": m, "doi": "", "title": None})
        for m in sorted(set(re.findall(r"DOI:\s*(10\.[^\s\]\),;]+)", t, re.I))): ids.append({"ref": "DOI:" + m, "pmid": "", "doi": m.rstrip("."), "title": None})
    return ids


def title_sim(a, b):
    w = lambda s: set(re.findall(r"[a-z0-9]+", (s or "").lower())) - {"the", "of", "and", "in", "a", "with", "for", "to", "on"}
    A, B = w(a), w(b)
    return len(A & B) / max(1, min(len(A), len(B))) if A and B else None


def cmd_bodycheck(args):
    """正文引用核验（11-13 S3a：正文把 PMID 40635563 当成胆碱能 PET 研究，实际是另一篇综述；refcheck 只查附录，没拦住）。
    正文里的每个 [PMID:x]/[DOI:x]：① 在不在本版本知识库的证据来源里；② 不在的话查真伪和题目。"""
    t = rd(OUT / args.tag / "report.md")
    t = t.split("### 检索与筛选记录")[0]
    pm = sorted(set(re.findall(r"PMID[:：]\s*(\d{5,9})", t)))
    do = sorted(set(x.rstrip(".)，。；") for x in re.findall(r"DOI[:：]\s*(10\.[^\s\]\)，。；,;]+)", t, re.I)))
    c = kb.connect(); src = kbtag(args)
    inkb = {r[0] for r in c.execute("SELECT DISTINCT pid FROM evidence WHERE run_id=?", (src,))}
    res = []
    for kind, v in [("PMID", x) for x in pm] + [("DOI", x.lower()) for x in do]:
        pid = f"{kind}:{v}"
        if pid in inkb: res.append({"cite": pid, "verdict": "in_kb"}); continue
        hit = None
        try: hit = lit.lookup(v)
        except Exception: pass
        res.append({"cite": pid, "verdict": "not_in_kb_exists" if hit else "not_in_kb_not_found", "real_title": hit and hit.get("title")})
    # 引文与内容一致性：每处引用前面那句话，和被引文献的证据比字符二元组相似度；别的文献明显更像就标出（可能挂错编号）
    def grams(s):
        s = re.sub(r"\s+", "", s or ""); return {s[i:i + 2] for i in range(len(s) - 1)}
    evtext = {}
    for r in c.execute("SELECT pid, finding, measure, condition, population FROM evidence WHERE run_id=?", (src,)):
        evtext.setdefault(r["pid"], []).append(" ".join(x or "" for x in (r["finding"], r["measure"], r["condition"], r["population"])))
    eg = {p: grams(" ".join(v)) for p, v in evtext.items()}
    sim = lambda a, b: len(a & b) / max(1, len(a))
    mism = []
    for m in re.finditer(r"(PMID|DOI)[:：]\s*([^\s\]\)，。；,;]+)", t, re.I):
        pid = f"{m.group(1).upper()}:{m.group(2).rstrip('.').lower() if m.group(1).upper() == 'DOI' else m.group(2)}"
        if pid not in eg: continue
        end = m.start()
        while end > 0 and t[end - 1] in "[ （(。；;，,]）)": end -= 1
        while end > 0 and re.match(r"(PMID|DOI)", t[max(0, end - 40):end].split("[")[-1] or "x", re.I):   # 连续多个引用
            end = t.rfind("[", 0, end)
            while end > 0 and t[end - 1] in "[ （(。；;，,]）)": end -= 1
        start = max(t.rfind("。", 0, end), t.rfind("\n", 0, end), end - 220) + 1
        ctx = re.sub(r"\[?(PMID|DOI)[:：][^\]]*\]?", "", t[start:end], flags=re.I)
        cg = grams(ctx)
        if len(cg) < 25: continue
        own = sim(cg, eg[pid]); best, bs = max(((p, sim(cg, g)) for p, g in eg.items()), key=lambda x: x[1])
        if best != pid and bs > own * 1.6 and own < 0.35:
            mism.append({"cite": pid, "context": ctx[-160:], "own_sim": round(own, 3), "better_match": best, "better_sim": round(bs, 3)})
    wr(OUT / args.tag / "bodycheck.json", {"citations": res, "possible_mismatch": mism})
    from collections import Counter
    print(args.tag, "正文引用", len(res), "个", dict(Counter(r["verdict"] for r in res)), "；疑似挂错编号", len(mism), "处", flush=True)
    for r in res:
        if r["verdict"] != "in_kb": print("  ", r["verdict"], r["cite"], "|", (r.get("real_title") or "")[:80])
    for x in mism:
        print(f"  疑似挂错：{x['cite']}（相似 {x['own_sim']}）更像 {x['better_match']}（{x['better_sim']}）| …{x['context'][-90:]}")


def cmd_refcheck(args):
    rows = []
    for r in cited_ids(args.tag):
        hit = None
        for ident in (r["pmid"], r["doi"]):
            if ident and not hit:
                try: hit = lit.lookup(ident)
                except Exception: hit = None
        sim = title_sim(r["title"], hit["title"]) if hit and r["title"] else None
        verdict = "not_found" if not hit else ("title_mismatch" if sim is not None and sim < 0.5 else "ok")
        rows.append({**r, "verdict": verdict, "found_title": hit and hit["title"], "title_sim": sim})
    wr(OUT / args.tag / "refcheck.json", rows)
    from collections import Counter
    cnt = Counter(x["verdict"] for x in rows)
    print(args.tag, "引用", len(rows), "条", dict(cnt), flush=True)
    for x in rows:
        if x["verdict"] != "ok": print("  ", x["verdict"], x["ref"], x["pmid"] or x["doi"], (x["title"] or "")[:60], "| 查到:", (x["found_title"] or "")[:60])


def cmd_review(args):
    rep = full_report(args.tag); q = question(args); st = standard()
    jobs = [("open_g6", "open_review", G6, "gpt3"), ("open_g56", "open_review", G56, "gpt4"), ("abs_g6", "abs_review", G6, None)]
    if args.only: jobs = [j for j in jobs if j[0] in args.only.split(",")] +                          ([("abs_g56", "abs_review", G56, "gpt4")] if "abs_g56" in args.only.split(",") else [])
    sfx = f"_r{args.rep}" if args.rep > 1 else ""   # 同一版本重复测（I07 补次数、测评委波动）
    def one(j):
        name, tpl, model, acct = j
        name = name + sfx
        p = OUT / args.tag / f"{name}.json"
        if p.exists(): return
        msg = fill(P(tpl), QUESTION=q, STANDARD=st, REPORT=rep); att = []
        if len(msg) > INLINE_MAX:   # 太长就把报告作为附件上传
            att = [OUT / args.tag / "report_full.md"]
            msg = fill(P(tpl), QUESTION=q, STANDARD=st, REPORT="（报告全文和结构化附录见附件 report_full.md，请完整读完再判断。）")
        ans = llm.call(f"{args.tag}_{args.q}_{name}_{llm.pid(msg + rep)}", msg, attach=att, model=model, acct=acct, stage=tpl)
        try: wr(p, llm.parse_json(ans))
        except Exception as e:
            wr(OUT / args.tag / f"{name}.raw.md", ans or "")
            key = "rank" if tpl == "open_review" else "n"
            items = llm.salvage_items(ans, key)
            if items:
                wr(p, {"problems" if key == "rank" else "standards": items, "salvaged": True})
                print(name, "整体解析失败，逐条救回", len(items), "条", flush=True)
            else:
                print(name, "解析失败", e)
    with ThreadPoolExecutor(3) as ex: list(ex.map(one, jobs))
    summarize_review(args.tag)


def summarize_review(tag):
    for n in ("open_g6", "open_g56"):
        p = OUT / tag / f"{n}.json"
        if p.exists():
            d = json.loads(rd(p)); ps = d.get("problems", [])
            print(f"{tag} {n}: major {sum(x.get('severity') == 'major' for x in ps)}，moderate {sum(x.get('severity') == 'moderate' for x in ps)}")
            for x in ps[:3]: print("   ", x.get("rank"), x.get("severity"), (x.get("what") or "")[:120])
    p = OUT / tag / "abs_g6.json"
    if p.exists():
        d = json.loads(rd(p)); sev = [i.get("severity") for s in d.get("standards", []) for i in s.get("issues", [])]
        print(f"{tag} 绝对验收: severe {sev.count('severe')}，moderate {sev.count('moderate')}，minor {sev.count('minor')}；",
              "逐条", [(s.get("n"), s.get("verdict")) for s in d.get("standards", [])])
        from collections import Counter
        print("   抽查", dict(Counter(x.get("verdict") for x in d.get("spot_checks", []))))


def cmd_blind(args):
    q = question(args); st = standard(); A = full_report(args.a); B = full_report(args.b)
    jobs = [(seat, j, m, acct) for seat in ("aX", "bX") for j, m, acct in (("g6", G6, "gpt3"), ("g56", G56, "gpt4"))]
    def one(job):
        seat, j, m, acct = job
        x, y = (A, B) if seat == "aX" else (B, A)
        msg = fill(P("blind"), QUESTION=q, STANDARD=st, X=x, Y=y); att = []
        if len(msg) > INLINE_MAX:   # 两份都作附件，文件名只叫 X、Y，不暴露版本
            dd = ROOT / "runs" / f"blind_files_{args.a}_vs_{args.b}_{seat}"; dd.mkdir(parents=True, exist_ok=True)
            wr(dd / "X.md", x); wr(dd / "Y.md", y); att = [dd / "X.md", dd / "Y.md"]
            msg = fill(P("blind"), QUESTION=q, STANDARD=st, X="（见附件 X.md，请完整读完）", Y="（见附件 Y.md，请完整读完）")
        ans = llm.call(f"blind_{args.a}_vs_{args.b}_{seat}_{j}_{llm.pid(msg + x + y)}", msg, attach=att, model=m, acct=acct, stage="blind")
        try:
            d = llm.parse_json(ans)
        except Exception as e: print("盲比解析失败", e); return None
        tr = lambda v: {"X": args.a if seat == "aX" else args.b, "Y": args.b if seat == "aX" else args.a}.get(v, "tie")
        return {"seat": seat, "judge": j, "better": tr(d.get("better")), "items": {k: tr(v.get("better")) for k, v in d.get("items", {}).items()}, "why": d.get("why")}
    with ThreadPoolExecutor(4) as ex: res = [r for r in ex.map(one, jobs) if r]
    wr(OUT / f"blind_{args.a}_vs_{args.b}.json", res)
    for r in res: print(r["judge"], r["seat"], "总体:", r["better"], "分项:", r["items"])


def _norm(s):
    return re.findall(r"[a-z0-9]+", (s or "").lower())


def quote_found(quote, source):
    """原句机械核对：quote 的连续 6 词片段有多少能在原文里找到。"""
    q, src = _norm(quote), " ".join(_norm(source))
    if len(q) < 6 or not src: return "no_source" if not src else ("found" if " ".join(q) in src else "not_found")
    grams = [" ".join(q[i:i + 6]) for i in range(len(q) - 5)]
    r = sum(g in src for g in grams) / len(grams)
    return "found" if r >= 0.8 else "partial" if r >= 0.3 else "not_found"


def cmd_quotecheck(args):
    """AROS 3.3：每个证据必须关联真实原文，不能以模型记忆代替来源。机械核对，不调模型。"""
    c = kb.connect(); from collections import Counter
    rows = list(c.execute("SELECT e.eid, e.quote, e.basis, p.abstract, p.fulltext_path FROM evidence e JOIN papers p USING(pid) "
                          "WHERE e.run_id=?", (args.tag,)))
    cnt = Counter()
    for r in rows:
        src = r["abstract"] or ""
        f = r["fulltext_path"]
        if f and Path(f).exists() and f.endswith((".txt", ".html")):
            src += "\n" + Path(f).read_text(encoding="utf-8", errors="ignore")
        v = quote_found(r["quote"], src) if not (f and f.endswith(".pdf")) or r["basis"] == "abstract" else (
            quote_found(r["quote"], src) if quote_found(r["quote"], src) == "found" else "pdf_unchecked")
        c.execute("UPDATE evidence SET quote_check=? WHERE eid=?", (v, r["eid"])); cnt[v] += 1
    c.commit()
    print(args.tag, "原句核对", len(rows), "条", dict(cnt), flush=True)


def bundle_fulltexts(rows, d, max_chars=400_000):
    """服务端单条消息附件数有上限（历史：≤11 个成功，24、41 个都 HTTP 422，猜想台账 P3）。
    文本全文按大小拼成几个合集，PDF/HTML 打进一个 zip；内容不删减。"""
    import zipfile
    texts, others = [], []
    for r in rows:
        f = r["fulltext_path"]
        if not f or not Path(f).exists(): continue
        (texts if f.endswith(".txt") else others).append((r, Path(f)))
    out, buf, n = [], [], 0
    def flush():
        if buf:
            p = d / f"fulltexts_{len(out) + 1}.txt"; p.write_text("\n\n".join(buf), encoding="utf-8"); out.append(p)
    for r, f in texts:
        s = f"===== {r['pid']} | {r['title']} ({r['year']}) =====\n" + f.read_text(encoding="utf-8")
        if n + len(s) > max_chars and buf: flush(); buf, n = [], 0
        buf.append(s); n += len(s)
    flush()
    if others:
        z = d / "fulltexts_pdf_html.zip"
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for r, f in others: zf.write(f, arcname=F.safe_key(r["pid"]) + f.suffix)
        out.append(z)
    print(f"全文打包：文本 {len(texts)} 篇 → {sum(1 for x in out if x.suffix == '.txt')} 个合集；PDF/HTML {len(others)} 篇 → {'1 个 zip' if others else '无'}", flush=True)
    return out


def cmd_material(args):
    """AROS 7.2 的 B 组：通用模型 + 和系统相同的检索材料，没有专用流程。
    材料 = 系统 --src 版本纳入的全部文献（摘要清单一个文件 + 拿到的全文作为附件），提示词和 B0 完全相同只多一句说明。"""
    c = kb.connect(); src = args.src or "S1"
    inc = [r["pid"] for r in c.execute("SELECT pid FROM screening WHERE question=? AND run_id=? AND decision='include'", (args.q, src))]
    rows = list(c.execute(f"SELECT * FROM papers WHERE pid IN ({','.join('?' * len(inc))})", inc))
    d = OUT / args.tag; d.mkdir(parents=True, exist_ok=True)
    lst = d / "materials_abstracts.txt"
    lst.write_text("\n\n---\n\n".join(paper_brief(r, 4000) for r in rows), encoding="utf-8")
    att = [lst] + bundle_fulltexts(rows, d)
    msg = fill(P("oneshot"), QUESTION=question(args), STANDARD=standard()) + (
        f"\n\n【附带材料】附件里有 {len(rows)} 篇检索得到的相关文献的题目和摘要（materials_abstracts.txt），"
        f"以及其中有全文的文献（fulltexts_*.txt 是开放获取全文的文本合集，每篇以 ===== 文献编号 开头；fulltexts_pdf_html.zip 里是其余的 PDF/HTML 全文）。这些材料可以用，也可以继续自己联网查。")
    print(f"B 组：纳入 {len(rows)} 篇，附件 {len(att)} 个", flush=True)
    msg += P("turns_note")   # 和 B0 一样分轮（通道上限，猜想台账 P2）
    ans = llm.session(f"{args.tag}_{args.q}_material_{llm.pid(msg + ''.join(map(str, att)))}", msg, model=G6, acct="gpt3",
                      stage="material", max_turns=args.max_turns, attach=att)
    if not ans: print("无回答"); return
    clean = [a.replace("【完成】", "").replace("【继续】", "").strip() for a in ans]
    body, app = split_report(clean[-1])
    if len(clean) > 1 and re.match(r"^#+\s*第\s*[二三四五六七八九十\d]+\s*(部分|轮|部)", body.lstrip()):
        body = "\n\n".join([split_report(x)[0] for x in clean[:-1]] + [body])
    wr(d / "report.md", body); wr(d / "raw.md", "\n\n=====（下一轮）=====\n\n".join(ans))
    if app: wr(d / "appendix.json", app)
    print(args.tag, "完成", len(body), "字", flush=True)


def cmd_fork(args):
    """新版本沿用 --src 版本的检索、筛选和证据（只差后面的步骤，便于"只差一处"的对照）。证据编号加新版本前缀。"""
    c = kb.connect(); src = args.src
    if c.execute("SELECT COUNT(*) FROM evidence WHERE run_id=?", (args.tag,)).fetchone()[0]:
        print(args.tag, "已有证据，不重复复制"); return
    for f in ("plan.json", "pool.json", "search_seeds.json"):
        if (OUT / src / f).exists(): wr(OUT / args.tag / f, rd(OUT / src / f))
    c.execute("INSERT OR REPLACE INTO screening SELECT question, pid, decision, reason, ?, at FROM screening WHERE run_id=?", (args.tag, src))
    if args.no_evidence:
        c.commit(); print(args.tag, "沿用", src, "的检索和筛选，不复制证据（要重新提取）"); return
    cols = [r[1] for r in c.execute("PRAGMA table_info(evidence)")]
    for r in c.execute("SELECT * FROM evidence WHERE run_id=?", (src,)).fetchall():
        d = dict(r); d["eid"] = f"{args.tag}_{r['eid']}"; d["run_id"] = args.tag
        c.execute(f"INSERT INTO evidence({','.join(cols)}) VALUES({','.join('?' * len(cols))})", [d[k] for k in cols])
    c.commit()
    print(args.tag, "沿用", src, "：筛选", c.execute("SELECT COUNT(*) FROM screening WHERE run_id=?", (args.tag,)).fetchone()[0],
          "条，证据", c.execute("SELECT COUNT(*) FROM evidence WHERE run_id=?", (args.tag,)).fetchone()[0], "条")


def cmd_advise(args):
    """I02/I03：把四项定位、台账、设定、全部测量原文交两位顾问（GPT-6 走 gpt3、GPT-5.6 走 gpt4），各自独立出诊断和候选方案。
    --tag 是被诊断的主线版本，--a 是用来对比的最强基线。输出 out/advise_<tag>/advisor_g6.json、advisor_g56.json。"""
    d = OUT / f"advise_{args.tag}"; d.mkdir(parents=True, exist_ok=True)
    wr(d / "current_pipeline.md", rd(ROOT / "主线.md"))
    wr(d / "current_prompts.txt", "\n\n".join(f"===== prompts/{n}.txt =====\n" + P(n) for n in
                                                ("plan", "screen", "extract", "synth_map", "synth_merge", "synth_reduce", "report")))
    wr(d / "ledger.md", rd(ROOT / "猜想台账.md") + "\n\n" + rd(ROOT / "试验记录.md"))
    wr(d / "settings.md", rd(ROOT / "设定登记.md"))
    ev = []
    for tag in (args.tag, args.a):
        for f in ("open_g6.json", "open_g56.json", "abs_g6.json", "refcheck.json"):
            p = OUT / tag / f
            if p.exists(): ev.append(f"===== {tag} / {f} =====\n" + rd(p))
    for f in sorted(OUT.glob(f"blind_*_vs_{args.tag}.json")):
        ev.append(f"===== {f.name}（better/items 已换成版本名）=====\n" + rd(f))
    wr(d / "evaluations.md", "\n\n".join(ev))
    att = [d / x for x in ("current_pipeline.md", "current_prompts.txt", "ledger.md", "settings.md", "evaluations.md")]
    msg = fill(P("i02_advisor"), QUESTION=question(args), STANDARD=standard())
    def one(j):
        name, model, acct = j
        p = d / f"advisor_{name}.json"
        if p.exists(): return
        ans = llm.call(f"advise_{args.tag}_{name}_{llm.pid(msg + ''.join(rd(a) for a in att))}", msg, attach=att, model=model, acct=acct, stage="advise")
        try: wr(p, llm.parse_json(ans))
        except Exception as e: print(name, "解析失败", e); wr(d / f"advisor_{name}.raw.md", ans or "")
    with ThreadPoolExecutor(2) as ex: list(ex.map(one, [("g6", G6, "gpt3"), ("g56", G56, "gpt4")]))
    for name in ("g6", "g56"):
        p = d / f"advisor_{name}.json"
        if not p.exists(): continue
        r = json.loads(rd(p))
        print(f"== 顾问 {name}：诊断 {len(r.get('diagnosis', []))} 条，方案 {len(r.get('candidates', []))} 套")
        for x in r.get("diagnosis", [])[:4]: print("   诊断", x.get("rank"), (x.get("problem") or "")[:100])
        for x in r.get("candidates", []): print("   方案", x.get("name"), "|", x.get("layer"), "|", (x.get("expected") or "")[:80])


def fulltext_plain(p, d):
    """知识库里一篇文献的全文转成纯文本文件（给裁定用）。PDF 用 pypdf，HTML 去标签。拿不到返回 None。"""
    f = p["fulltext_path"]
    if not f or not Path(f).exists(): return None
    out = d / f"{F.safe_key(p['pid'])}.txt"
    if out.exists(): return out
    if f.endswith(".txt"): txt = Path(f).read_text(encoding="utf-8")
    elif f.endswith(".html"):
        import html as H
        txt = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", Path(f).read_text(encoding="utf-8", errors="ignore"))))
    elif f.endswith(".pdf"):
        from pypdf import PdfReader
        txt = "\n".join((pg.extract_text() or "") for pg in PdfReader(f).pages)
    else: return None
    if len(txt) < 2000: return None
    wr(out, f"{p['pid']} | {p['title']} ({p['year']})\n\n" + txt)
    return out


def find_paper(c, acc):
    for k, pre in (("pmid", "PMID:"), ("doi", "DOI:")):
        v = str(acc.get(k) or "").strip().lower()
        if v:
            r = c.execute("SELECT * FROM papers WHERE pid=?", (pre + v,)).fetchone() or \
                c.execute(f"SELECT * FROM papers WHERE {k}=?", (v,)).fetchone()
            if r: return r
    words = [w for w in re.findall(r"[A-Za-z]{4,}", acc.get("paper") or "") if w.lower() not in ("study", "with", "from", "that")]
    yr = re.search(r"(19|20)\d\d", acc.get("paper") or "")
    best, score = None, 0
    for r in c.execute("SELECT * FROM papers WHERE fulltext_path IS NOT NULL" + (" AND year=?" if yr else ""), ((int(yr.group(0)),) if yr else ())):
        s = sum(w.lower() in ((r["title"] or "") + " " + (r["authors"] or "")).lower() for w in words)
        if s > score: best, score = r, s
    return best if score >= 2 else None


def cmd_factcheck(args):
    """P5 测法校准：评委的"误读/错引"指控，对照知识库全文裁定后才计入。--tag 是被评的报告版本。"""
    c = kb.connect(); d = OUT / args.tag / "factcheck"; d.mkdir(parents=True, exist_ok=True)
    sources = []
    for f in sorted(list((OUT / args.tag).glob("open_*.json")) + list((OUT / args.tag).glob("abs_*.json"))):
        sources.append((f.name, "这份报告", rd(f)))
    for rd_ in sorted((ROOT / "runs").glob(f"blind_*_vs_{args.tag}_*")):
        if not (rd_ / "output.txt").exists(): continue
        seat = "aX" if "_aX_" in rd_.name else "bX"
        target = "报告 Y" if seat == "aX" else "报告 X"   # aX：X 是对手，被评版本在 Y
        sources.append((rd_.name, target, rd(rd_ / "output.txt")))
    def extract(src):
        name, target, text = src
        msg = fill(P("fc_extract"), TARGET=target, TEXT=text[:55000])
        try: return [(name, a) for a in llm.parse_json(llm.call(f"fcx_{args.tag}_{llm.pid(msg)}", msg, model=G6, stage="factcheck"))["accusations"]]
        except Exception as e: print("抽指控失败", name, e); return []
    with ThreadPoolExecutor(WORKERS) as ex: accs = [x for r in ex.map(extract, sources) for x in r]
    print(f"指控来源 {len(sources)} 份，抽出指控 {len(accs)} 条", flush=True)
    def judge(item):
        name, a = item
        p = find_paper(kb.connect(), a)   # SQLite 连接不能跨线程
        if not p: return {**a, "source": name, "verdict": "paper_not_in_kb"}
        ft = fulltext_plain(p, d)
        if not ft: return {**a, "source": name, "pid": p["pid"], "verdict": "no_fulltext"}
        msg = fill(P("fc_judge"), PAPER=f"{p['pid']} {p['title']} ({p['year']})", REPORT_SAYS=a.get("report_says") or "", JUDGE_SAYS=a.get("judge_says") or "")
        try:
            r = llm.parse_json(llm.call(f"fcj_{args.tag}_{llm.pid(msg + p['pid'])}", msg, attach=[ft], model=G6, stage="factcheck"))
            return {**a, "source": name, "pid": p["pid"], **r}
        except Exception as e:
            return {**a, "source": name, "pid": p["pid"], "verdict": "error", "why": str(e)}
    with ThreadPoolExecutor(WORKERS) as ex: res = list(ex.map(judge, accs))
    for r in res:   # 只有报告说法无全文依据（no）或缺关键限定（partly）时指控才成立
        if "report_supported" in r:
            r["verdict"] = {"no": "accusation_holds", "partly": "accusation_partly", "yes": "accusation_rejected"}.get(r["report_supported"], "cannot_tell")
    wr(OUT / args.tag / "factcheck.json", res)
    from collections import Counter
    print(args.tag, "指控裁定", dict(Counter(r["verdict"] for r in res)), flush=True)
    for r in res:
        print(f"  [{r['verdict']}] 报告有依据:{r.get('report_supported')} 指控有依据:{r.get('judge_supported')} {r.get('pid') or r.get('paper')} | 指控：{(r.get('judge_says') or '')[:80]}")


def evidence_table_file(c, src, path):
    rows = evidence_rows(c, type("A", (), {"q": "Q1", "tag": src})())
    wr(path, "\n".join(evidence_line(r, 100000) for r in rows))
    return path, len(rows)


def cmd_audit(args):
    """S3d（顾问 g6"Claim Audit"）：对 --kb 版本的结论/假说/报告做独立审计（prompts/synth_audit.txt 原文），按审计修订，再写报告。"""
    c = kb.connect(); src = kbtag(args); d = OUT / args.tag; d.mkdir(parents=True, exist_ok=True)
    syn = json.loads(rd(OUT / src / "synthesis.json"))
    ev_file, n = evidence_table_file(c, src, d / "evidence_all.txt")
    draft = d / "report_draft.md"; wr(draft, rd(OUT / src / "report.md"))
    compact = [{**{x: cl.get(x) for x in ("cid", "text", "level", "status", "uncertainty")},
                "evidence": [f"{e['eid']}:{(e.get('relation') or '')[:4]}" for e in cl.get("evidence", [])]} for cl in syn["claims"]]
    msg = fill(P("synth_audit"), QUESTION=question(args), CLAIMS=json.dumps(compact, ensure_ascii=False),
               HYPOTHESES=json.dumps(syn["hypotheses"], ensure_ascii=False),
               EVIDENCE=f"（全部 {n} 条原始结构化证据见附件 evidence_all.txt，每条以 [证据编号] 开头）",
               REPORT_DRAFT="（报告正文草稿见附件 report_draft.md）",
               STUDY_MAP="（本版本知识库还没有研究/队列/版本映射。请根据证据里的作者、年份、样本和题目自行识别可能的同一研究不同版本或同一队列，写进 integrity_errors。）")
    print(f"审计：结论 {len(compact)}、假说 {len(syn['hypotheses'])}、证据 {n} 条（附件），提示词 {len(msg)} 字", flush=True)
    if len(msg) > INLINE_MAX: raise RuntimeError(f"审计提示词超长 {len(msg)}")
    aud = llm.parse_json(llm.call(f"{args.tag}_{args.q}_audit_{llm.pid(msg + rd(draft))}", msg, attach=[ev_file, draft], model=G6, stage="audit"))
    wr(d / "audit.json", aud)
    print("审计结果：", {k: len(v) if isinstance(v, list) else 1 for k, v in aud.items()}, flush=True)
    # 按审计修订
    audtxt = json.dumps(aud, ensure_ascii=False); att = []
    msg2 = fill(P("synth_revise"), QUESTION=question(args), STANDARD=standard(),
                SYNTHESIS=json.dumps({"claims": compact, "hypotheses": syn["hypotheses"], "gaps": syn.get("gaps", [])}, ensure_ascii=False), AUDIT=audtxt)
    if len(msg2) > INLINE_MAX:
        wr(d / "audit.json", aud); att = [d / "audit.json"]
        msg2 = fill(P("synth_revise"), QUESTION=question(args), STANDARD=standard(),
                    SYNTHESIS=json.dumps({"claims": compact, "hypotheses": syn["hypotheses"], "gaps": syn.get("gaps", [])}, ensure_ascii=False),
                    AUDIT="（审计结果 JSON 见附件 audit.json）")
    rev = llm.parse_json(llm.call(f"{args.tag}_{args.q}_revise_{llm.pid(msg2 + audtxt)}", msg2, attach=att, model=G6, stage="revise"))
    # 证据关系：沿用的结论取审计列表（无则取原结论），再并上修订时显式列出的
    ca = {x.get("cid"): x for x in aud.get("claim_audit", [])}
    orig = {cl["cid"]: cl for cl in syn["claims"]}
    valid = {r["eid"] for r in c.execute("SELECT eid FROM evidence WHERE run_id=?", (src,))}
    for cl in rev.get("claims", []):
        ev, seen = [], set()
        base = cl.get("base_cid")
        a = ca.get(base) if base else None
        if a:
            for rel, key in (("supports", "supporting_eids"), ("contradicts", "contradicting_eids"), ("qualifies", "qualifying_eids")):
                for e in a.get(key) or []:
                    if e in valid and e not in seen: seen.add(e); ev.append({"eid": e, "relation": rel})
        elif base in orig:
            for e in orig[base].get("evidence", []):
                if e["eid"] not in seen: seen.add(e["eid"]); ev.append(e)
        for e in cl.get("evidence") or []:
            if isinstance(e, dict) and e.get("eid") in valid and e["eid"] not in seen: seen.add(e["eid"]); ev.append(e)
        cl["evidence"] = ev
    wr(d / "synthesis.json", rev)
    print(f"修订后：结论 {len(rev.get('claims', []))}（新增 {sum(1 for x in rev.get('claims', []) if not x.get('base_cid'))}），"
          f"假说 {len(rev.get('hypotheses', []))}，拒绝的审计要求 {len(rev.get('rejected_requests', []))}，"
          f"结论覆盖证据 {len({e['eid'] for x in rev.get('claims', []) for e in x['evidence']})}/{n}", flush=True)


def cmd_handback(args):
    """I12：没过的候选交回提出者。--tag 是候选版本，--a 是对比的主线，--names 是顾问方案名（逗号分隔，在 out/advise_<主线>/ 里找），
    --why 是没过的原因（写进提示词）。每位提出者各自回答。"""
    d = OUT / args.tag / "handback"; d.mkdir(parents=True, exist_ok=True)
    adv = OUT / f"advise_{args.a}"
    parts = []
    for f in ("open_g6.json", "open_g56.json", "abs_g6.json", "factcheck.json", "bodycheck.json"):
        if (OUT / args.tag / f).exists(): parts.append(f"===== {f} =====\n" + rd(OUT / args.tag / f))
    for f in sorted(OUT.glob(f"blind_*_vs_{args.tag}.json")): parts.append(f"===== {f.name} =====\n" + rd(f))
    for rd_ in sorted((ROOT / "runs").glob(f"blind_*_vs_{args.tag}_*")):
        if (rd_ / "output.txt").exists(): parts.append(f"===== 盲比原文 {rd_.name}（X/Y 见文件名 aX=前者在 X 位）=====\n" + rd(rd_ / "output.txt"))
    wr(d / "results.md", "\n\n".join(parts))
    summary = rd(ROOT / "STATUS.md").split("## 待修的问题")[0][-6000:]
    impl = rd(ROOT / "试验记录.md").split(f"### {args.tag}")[-1].split("\n### ")[0][:4000]
    jobs = []
    for who, model, acct in (("g6", G6, "gpt3"), ("g56", G56, "gpt4")):
        p = adv / f"advisor_{who}.json"
        if not p.exists(): continue
        cands = [x for x in json.loads(rd(p)).get("candidates", []) if any(n in (x.get("name") or "") for n in args.names.split(","))]
        for cnd in cands: jobs.append((who, model, acct, cnd))
    def one(j):
        who, model, acct, cnd = j
        msg = fill(P("handback"), QUESTION=question(args), STANDARD=standard(), CANDIDATE=json.dumps(cnd, ensure_ascii=False)[:20000],
                   IMPLEMENTATION=impl, SUMMARY=summary, WHY_FAILED=args.why or "")
        ans = llm.call(f"handback_{args.tag}_{who}_{llm.pid(msg + rd(d / 'results.md'))}", msg, attach=[d / "results.md"], model=model, acct=acct, stage="handback")
        try: r = llm.parse_json(ans)
        except Exception as e: r = {"error": str(e), "raw": ans}
        wr(d / f"handback_{who}.json", r)
        print(f"== {who}（{cnd.get('name')}）：原因 {r.get('cause')}，能修 {r.get('fixable')}；{(r.get('why_not_fixable') or r.get('expected') or '')[:200]}", flush=True)
    with ThreadPoolExecutor(2) as ex: list(ex.map(one, jobs))


def cmd_recall(args):
    """S4R（S3a 交回后两位提出者的改后方案"检索—筛选—证据准入闭环"）：
    ① 每条检索式分页取全（不再截断）并入库；② 新文献先题目初筛（150 篇一批，从宽）→ 摘要筛选（沿用 screen 提示词）；
    ③ 已在 --src（S1）筛过的沿用原结论；④ 所有"待定"给最终结论（include/exclude）。只有 include 进入后续提取。"""
    c = kb.connect(); src = args.src or "S1"; q = question(args); tag = args.tag
    plan = json.loads(rd(OUT / src / "plan.json")); wr(OUT / tag / "plan.json", plan)
    for f in ("search_seeds.json",):
        if (OUT / src / f).exists(): wr(OUT / tag / f, rd(OUT / src / f))
    # ① 全量取回
    if not c.execute("SELECT COUNT(*) FROM queries WHERE run_id=?", (tag,)).fetchone()[0]:
        pool = set()
        for x in plan["queries"]:
            total, rs = lit.epmc_search(x["q"], max_n=100000, page=1000)
            ids = [kb.upsert_paper(c, r, "epmc_full") for r in rs if r.get("pmid") or r.get("doi")]
            pool |= {i for i in ids if i}
            c.execute("INSERT INTO queries(question,engine,text,hit_count,kept,run_id,at) VALUES(?,?,?,?,?,?,?)",
                      (args.q, "epmc", x["q"], total, len(ids), tag, kb.now()))
            c.commit(); print(f"  {total:>6} 命中 取回 {len(ids):>6}  {x['q'][:80]}", flush=True)
        seeds = json.loads(rd(OUT / src / "search_seeds.json"))
        pool |= {s["pid"] for s in seeds if s["exists"] and s["pid"]}
        wr(OUT / tag / "pool.json", sorted(pool))
    pool = json.loads(rd(OUT / tag / "pool.json"))
    old = {r["pid"]: r["decision"] for r in c.execute("SELECT pid, decision FROM screening WHERE run_id=? AND question=?", (src, args.q))}
    done = {r["pid"] for r in c.execute("SELECT pid FROM screening WHERE run_id=? AND question=?", (tag, args.q))}
    for pid, dec in old.items():   # ③ 沿用
        if pid not in done:
            c.execute("INSERT OR REPLACE INTO screening VALUES(?,?,?,?,?,?)", (args.q, pid, dec, f"沿用 {src} 筛选", tag, kb.now()))
    c.commit()
    papers = {r["pid"]: r for r in c.execute("SELECT * FROM papers")}
    new = [p for p in pool if p not in old and p not in done and p in papers]
    print(f"全量池 {len(pool)} 篇；沿用 {src} 筛选 {len(old)} 篇；新文献待题目初筛 {len(new)} 篇", flush=True)
    # ② 题目初筛
    def tbatch(b):
        body = "\n".join(f"{p} | {papers[p]['year']} | {(papers[p]['pub_type'] or '')[:40]} | {papers[p]['title']}" for p in b)
        msg = fill(P("screen_title"), QUESTION=q, PAPERS=body)
        try:
            ks = llm.parse_json(llm.call(f"{tag}_{args.q}_tscreen_{llm.pid(msg)}", msg, model=G6, stage="screen-title"))["keep"]
            # 11-13：模型常返回纯数字 PMID（"28691105"），要补成 "PMID:28691105" 才能和输入对上（否则全被当成排除）
            norm = lambda x: x if ":" in str(x) else (f"PMID:{x}" if str(x).isdigit() else f"DOI:{str(x).lower()}")
            got = {norm(str(k).strip()) for k in ks}
            if ks and not (got & set(b)): print("题目初筛返回的编号一个都对不上（这批全部保留）", list(ks)[:3]); return b, set(b)
            return b, got
        except Exception as e: print("题目初筛失败（这批全部保留）", e); return b, set(b)
    batches = [new[i:i + 150] for i in range(0, len(new), 150)]
    keep = []
    with ThreadPoolExecutor(WORKERS) as ex:
        for b, k in ex.map(tbatch, batches):
            for p in b:
                if p in k: keep.append(p)
                else: c.execute("INSERT OR REPLACE INTO screening VALUES(?,?,?,?,?,?)", (args.q, p, "title_drop", "题目初筛排除", tag, kb.now()))
            c.commit()
    print(f"题目初筛：{len(new)} 篇 → 保留 {len(keep)} 篇（{len(batches)} 批）", flush=True)
    # 摘要筛选
    def abatch(b):
        body = "\n\n---\n\n".join(paper_brief(papers[p]) for p in b)
        msg = fill(P("screen"), QUESTION=q, PAPERS=body)
        try: return llm.parse_json(llm.call(f"{tag}_{args.q}_screen_{llm.pid(msg)}", msg, model=G6, stage="screen"))["items"]
        except Exception as e: print("摘要筛选失败", e); return []
    with ThreadPoolExecutor(WORKERS) as ex:
        for items in ex.map(abatch, [keep[i:i + 30] for i in range(0, len(keep), 30)]):
            for it in items:
                if it.get("pid") in papers:
                    c.execute("INSERT OR REPLACE INTO screening VALUES(?,?,?,?,?,?)", (args.q, it["pid"], it.get("decision"), it.get("reason"), tag, kb.now()))
            c.commit()
    # ④ 待定终判
    mb = [r["pid"] for r in c.execute("SELECT pid FROM screening WHERE run_id=? AND question=? AND decision='maybe'", (tag, args.q))]
    def fbatch(b):
        body = "\n\n---\n\n".join(paper_brief(papers[p], 2500) for p in b)
        msg = fill(P("screen_final"), QUESTION=q, PAPERS=body)
        try: return llm.parse_json(llm.call(f"{tag}_{args.q}_fscreen_{llm.pid(msg)}", msg, model=G6, stage="screen-final"))["items"]
        except Exception as e: print("待定终判失败", e); return []
    with ThreadPoolExecutor(WORKERS) as ex:
        for items in ex.map(fbatch, [mb[i:i + 25] for i in range(0, len(mb), 25)]):
            for it in items:
                if it.get("pid") in papers and it.get("decision") in ("include", "exclude"):
                    c.execute("INSERT OR REPLACE INTO screening VALUES(?,?,?,?,?,?)", (args.q, it["pid"], it["decision"], "待定终判：" + (it.get("reason") or ""), tag, kb.now()))
            c.commit()
    cnt = dict(c.execute("SELECT decision, COUNT(*) FROM screening WHERE run_id=? AND question=? GROUP BY decision", (tag, args.q)).fetchall())
    seeds = json.loads(rd(OUT / tag / "search_seeds.json"))
    inc = {r[0] for r in c.execute("SELECT pid FROM screening WHERE run_id=? AND decision='include'", (tag,))}
    print("筛选结果", cnt, "；必读文献最终纳入", sum(1 for s in seeds if s["pid"] in inc), "/", sum(1 for s in seeds if s["exists"]), flush=True)


def cmd_rebase(args):
    """S3d2（S3d 交回 GPT-6 后的改后方案 Claim Audit v2 的最小实现）：证据库不可变，审计只能改关系、不能删证据。
    以 --kb（S2）的证据关联为底；--src（S3d）审计明确列出的 EID 按审计改关系类型；审计没提到的原关联保留。
    结论/假说文字沿用 --src 修订版（base_cid 指回 S2 结论）。不新增模型调用。"""
    base = json.loads(rd(OUT / kbtag(args) / "synthesis.json")); rev = json.loads(rd(OUT / args.src / "synthesis.json"))
    aud = json.loads(rd(OUT / args.src / "audit.json"))
    borig = {cl["cid"]: cl for cl in base["claims"]}; ca = {x.get("cid"): x for x in aud.get("claim_audit", [])}
    out_claims, changed, kept, added = [], 0, 0, 0
    for cl in rev["claims"]:
        b = cl.get("base_cid")
        rel = {}
        if b in borig:
            for e in borig[b].get("evidence", []): rel[e["eid"]] = dict(e); kept += 1
        a = ca.get(b) if b else None
        if a:
            for r, key in (("supports", "supporting_eids"), ("contradicts", "contradicting_eids"), ("qualifies", "qualifying_eids")):
                for e in a.get(key) or []:
                    if e in rel and rel[e].get("relation") != r: rel[e]["relation"] = r; rel[e]["note"] = "审计改关系类型"; changed += 1
                    elif e not in rel: rel[e] = {"eid": e, "relation": r, "note": "审计新增"}; added += 1
        for e in cl.get("evidence") or []:   # S3d 修订版里显式列出的（含新增结论）
            if e["eid"] not in rel: rel[e["eid"]] = e; added += 1
        cl = dict(cl); cl["evidence"] = list(rel.values()); out_claims.append(cl)
    d = {**rev, "claims": out_claims}
    n_base = len({e["eid"] for x in base["claims"] for e in x["evidence"]}); n_new = len({e["eid"] for x in out_claims for e in x["evidence"]})
    lost = {e["eid"] for x in base["claims"] for e in x["evidence"]} - {e["eid"] for x in out_claims for e in x["evidence"]}
    wr(OUT / args.tag / "synthesis.json", d)
    print(f"证据关联：底 {n_base} 条 EID → 新 {n_new} 条；改类型 {changed}、新增 {added}；丢失 {len(lost)}（应为 0：S2 结论都被 S3d 修订版沿用时）", flush=True)
    if lost: print("  丢失的 EID（所属 S2 结论没被修订版沿用）：", sorted(lost)[:10], flush=True)


def tiers_of(args):
    p = OUT / args.tag / "tiers.json"
    return json.loads(rd(p)) if p.exists() else None


def cmd_tier(args):
    """S4R：纳入文献按直接程度分 A/B/C（GPT-5.6 改后方案的"全文优先级"）。A 读全文，B/C 读摘要。"""
    c = kb.connect(); q = question(args)
    inc = selected(c, args); papers = {r["pid"]: r for r in c.execute(f"SELECT * FROM papers WHERE pid IN ({','.join('?' * len(inc))})", inc)}
    old = tiers_of(args) or {}
    todo = [p for p in inc if p not in old and p in papers]
    def one(b):
        body = "\n\n---\n\n".join(paper_brief(papers[p], 700) for p in b)
        msg = fill(P("tier"), QUESTION=q, PAPERS=body)
        try:
            items = llm.parse_json(llm.call(f"{args.tag}_{args.q}_tier_{llm.pid(msg)}", msg, model=G6, stage="tier"))["items"]
            norm = lambda x: x if ":" in str(x) else (f"PMID:{x}" if str(x).isdigit() else f"DOI:{str(x).lower()}")
            got = {norm(str(i.get("pid")).strip()): i.get("tier") for i in items}
            return {p: (got.get(p) if got.get(p) in ("A", "B", "C") else "B") for p in b}   # 漏判的按 B（读摘要）
        except Exception as e:
            print("分层失败（这批按 B）", e); return {p: "B" for p in b}
    out = dict(old)
    with ThreadPoolExecutor(WORKERS) as ex:
        for r in ex.map(one, [todo[i:i + 50] for i in range(0, len(todo), 50)]): out.update(r)
    wr(OUT / args.tag / "tiers.json", out)
    from collections import Counter
    print("分层", dict(Counter(out.values())), flush=True)


def cmd_inherit(args):
    """把 --src（S1）已经提取过、且本版本纳入的文献的证据复制过来（同一提取提示词，不重复花调用）。"""
    c = kb.connect(); inc = set(selected(c, args))
    if c.execute("SELECT COUNT(*) FROM evidence WHERE run_id=?", (args.tag,)).fetchone()[0]:
        print(args.tag, "已有证据，不重复沿用"); return
    cols = [r[1] for r in c.execute("PRAGMA table_info(evidence)")]
    n, pids = 0, set()
    for r in c.execute("SELECT * FROM evidence WHERE run_id=?", (args.src,)).fetchall():
        if r["pid"] not in inc: continue
        d = dict(r); d["eid"] = f"{args.tag}_{r['eid']}"; d["run_id"] = args.tag
        c.execute(f"INSERT INTO evidence({','.join(cols)}) VALUES({','.join('?' * len(cols))})", [d[k] for k in cols]); n += 1; pids.add(r["pid"])
    c.commit(); print(f"{args.tag} 沿用 {args.src} 证据 {n} 条（{len(pids)} 篇）", flush=True)


def cmd_appendix(args):
    export_appendix(kb.connect(), args)


def cmd_stats(args):
    c = kb.connect(); print("知识库", kb.stats(c))
    from collections import Counter, defaultdict
    secs, cnt, fail = defaultdict(int), Counter(), Counter()
    p = ROOT / "runs" / "calls.jsonl"
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            r = json.loads(l); s = r.get("stage") or "?"
            secs[s] += r.get("seconds", 0); cnt[s] += 1; fail[s] += (not r.get("completed"))
    for s in cnt: print(f"  {s:<18} 调用 {cnt[s]:>4}  失败 {fail[s]:>3}  合计 {secs[s] / 3600:.1f} 小时")
    lp = ROOT / "runs" / "luna_calls.jsonl"
    print("luna 调用", len(lp.read_text(encoding="utf-8").splitlines()) if lp.exists() else 0, "次")


def cmd_check(args):
    import subprocess
    for a, exe in llm.CLI.items():
        r = subprocess.run([exe, "check", "--json"], capture_output=True)
        try: j = json.loads(r.stdout.decode("utf-8")); print(a, "就绪" if j.get("ready") else "未就绪", "凭据到期", j.get("token_expiry_utc"))
        except Exception: print(a, "检查失败", r.stderr[-300:])
        print("  冷却中" if llm.cooling(a) else "  未冷却")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("--tag", default="S1"); ap.add_argument("--q", default="Q1")
    ap.add_argument("--a"); ap.add_argument("--b")
    ap.add_argument("--per-query", type=int, default=100); ap.add_argument("--batch", type=int, default=30)
    ap.add_argument("--no-luna", action="store_true"); ap.add_argument("--map-reduce", action="store_true"); ap.add_argument("--kb"); ap.add_argument("--with-methods", action="store_true"); ap.add_argument("--no-evidence", action="store_true"); ap.add_argument("--extract-prompt", default="extract"); ap.add_argument("--rep", type=int, default=1); ap.add_argument("--only"); ap.add_argument("--names", default=""); ap.add_argument("--why", default="")
    ap.add_argument("--src"); ap.add_argument("--max-turns", type=int, default=8); ap.add_argument("--max-attach", type=int, default=40)
    args = ap.parse_args()
    globals()["cmd_" + args.cmd](args)


if __name__ == "__main__":
    main()
