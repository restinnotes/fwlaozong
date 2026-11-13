"""全文获取层（L2）。

顺序：本地 Europe PMC 开放获取全文 XML → 转成纯文本（papers/epmc/<PMC>.txt）。
本地拿不到的，攒成一批，一次 codex exec（gpt-6-luna，max）去合法开放来源下载（papers/luna_<批>/）。
用户 11-13："如果他碰到下载问题 你可以使用codex exec 用gpt6 luna max来做一些辅助……但尽量不要使用太多这个luna"。
所以：每批最多一次 luna 调用，只做下载，不做分析；每次调用记 runs/luna_calls.jsonl。
下载的文件是不可信数据：只检查文件头和大小、作为附件上传给 gpt3，不执行其中任何东西。
"""
import json, os, shutil, subprocess, time
from pathlib import Path

import kb, lit

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
LUNA_MODEL = os.environ.get("LUNA_MODEL", "gpt-6-luna")
LUNA_EFFORT = os.environ.get("LUNA_EFFORT", "max")
LUNA_PER_BATCH = int(os.environ.get("LUNA_PER_BATCH", "40"))   # 一次 luna 调用最多交多少篇


def safe_key(pid):
    return pid.replace(":", "_").replace("/", "_").replace("\\", "_")


def local_fetch(c, pids):
    """本地拿开放全文，返回拿不到的 pid 列表。"""
    miss = []
    (PAPERS / "epmc").mkdir(parents=True, exist_ok=True)
    for pid in pids:
        p = c.execute("SELECT * FROM papers WHERE pid=?", (pid,)).fetchone()
        if not p: continue
        if p["fulltext_path"] and Path(p["fulltext_path"]).exists(): continue
        txt = None
        if p["pmcid"]:
            x = lit.epmc_fulltext_xml(p["pmcid"])
            if x:
                try: txt = lit.jats_to_text(x)
                except Exception: txt = None
        if txt and len(txt) > 3000:
            f = PAPERS / "epmc" / f"{safe_key(pid)}.txt"
            f.write_text(txt, encoding="utf-8")
            c.execute("UPDATE papers SET fulltext_path=?, fulltext_kind='epmc_xml' WHERE pid=?", (str(f), pid))
            kb.hist(c, "papers", pid, "fulltext", {"via": "epmc_xml", "chars": len(txt)})
            print(f"  本地全文 {pid} {len(txt)} 字", flush=True)
        else:
            miss.append(pid)
    c.commit()
    return miss


LUNA_PROMPT = """你只做一件事：把下面列出的论文全文下载到当前目录。不要阅读、总结或分析论文内容。

规则：
1. 只用合法的开放来源：Europe PMC、PubMed Central、出版社的开放获取页面、Unpaywall 指向的开放版本、作者或机构仓库、bioRxiv/medRxiv/arXiv 等预印本服务器。禁止使用 Sci-Hub、LibGen、Anna's Archive 之类来源，也不要尝试绕过付费墙或登录。
2. 每篇保存为 <key>.pdf（拿不到 PDF、只有完整 HTML 全文时保存为 <key>.html）。key 见列表。
3. 保存后自己检查：PDF 要以 %PDF 开头、大于 50KB；HTML 要包含正文（Methods/Results 等），不能是验证码页、登录页或只有摘要的页面。不合格的删掉，换来源再试；确实没有开放版本就记 not_open。
4. 可以用 curl、Python、浏览器自动化等任何你需要的手段；可以并行。
5. 最后写 manifest.json：一个 JSON 数组，每篇一项 {"key","status"(ok/not_open/failed),"file","source_url","note"}。
6. 最后一条消息只输出一行：完成 N 篇 / 共 M 篇。

论文列表（JSON）：
"""


def luna_fetch(c, pids, batch=None):
    """把本地拿不到的论文一次交给 codex luna 下载。返回成功的 pid 列表。"""
    pids = pids[:LUNA_PER_BATCH]
    if not pids: return []
    batch = batch or time.strftime("%m%d_%H%M%S")
    d = PAPERS / f"luna_{batch}"; d.mkdir(parents=True, exist_ok=True)
    items = []
    for pid in pids:
        p = c.execute("SELECT * FROM papers WHERE pid=?", (pid,)).fetchone()
        items.append({"key": safe_key(pid), "pmid": p["pmid"], "pmcid": p["pmcid"], "doi": p["doi"],
                      "title": p["title"], "year": p["year"], "journal": p["journal"]})
    prompt = LUNA_PROMPT + json.dumps(items, ensure_ascii=False, indent=1)
    (d / "_prompt.txt").write_text(prompt, encoding="utf-8")
    exe = shutil.which("codex.cmd") or shutil.which("codex") or "codex"
    # 不加引号：-c 的值不是合法 TOML 时按原样字符串处理，max 即 "max"
    cmd = [exe, "exec", "-m", LUNA_MODEL, "-c", f"model_reasoning_effort={LUNA_EFFORT}",
           "--skip-git-repo-check", "-C", str(d), "-o", str(d / "_last_message.txt"), "-"]
    t0 = time.time()
    print(f"  luna 下载 {len(items)} 篇 → {d}", flush=True)
    cp = subprocess.run(cmd, input=prompt.encode("utf-8"), capture_output=True)
    (d / "_stdout.txt").write_bytes(cp.stdout); (d / "_stderr.txt").write_bytes(cp.stderr)
    ok = verify_batch(c, d, pids)
    rec = {"batch": batch, "model": LUNA_MODEL, "effort": LUNA_EFFORT, "asked": len(items), "ok": len(ok),
           "seconds": round(time.time() - t0), "exit_code": cp.returncode, "at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    with (ROOT / "runs" / "luna_calls.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"  luna 完成：{len(ok)}/{len(items)} 篇可用，{rec['seconds']}s，退出码 {cp.returncode}", flush=True)
    return ok


def verify_batch(c, d, pids):
    """不信 luna 自报，逐个文件查头和大小。"""
    ok = []
    for pid in pids:
        k = safe_key(pid)
        for ext, kind in ((".pdf", "pdf"), (".html", "html")):
            f = d / (k + ext)
            if not f.exists(): continue
            b = f.read_bytes()[:2048]
            good = (kind == "pdf" and b.startswith(b"%PDF") and f.stat().st_size > 50_000) or \
                   (kind == "html" and f.stat().st_size > 30_000 and b"captcha" not in f.read_bytes()[:200_000].lower())
            if good:
                c.execute("UPDATE papers SET fulltext_path=?, fulltext_kind=? WHERE pid=?", (str(f), "luna_" + kind, pid))
                kb.hist(c, "papers", pid, "fulltext", {"via": "luna_" + kind, "bytes": f.stat().st_size})
                ok.append(pid); break
    c.commit()
    return ok


def fetch(c, pids, use_luna=True):
    miss = local_fetch(c, pids)
    print(f"  本地拿到 {len(pids) - len(miss)}/{len(pids)} 篇全文", flush=True)
    if miss and use_luna:
        luna_fetch(c, miss)
    return c.execute(f"SELECT COUNT(*) FROM papers WHERE fulltext_path IS NOT NULL AND pid IN ({','.join('?' * len(pids))})",
                     pids).fetchone()[0] if pids else 0
