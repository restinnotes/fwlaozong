"""证据—文献归属核对（11-14 S5La 绝对验收发现 PMID:42185340 的证据其实是 PMID:42183045 的内容）。
每条证据的 发现+对象+条件 与本文献 题目+摘要 比字符二元组覆盖率；再和本版本所有有摘要的文献比，别篇明显更像就列出。"""
import re, sqlite3, sys, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
run = sys.argv[1] if len(sys.argv) > 1 else "S4R"
c = sqlite3.connect(ROOT / "kb" / "kb.sqlite3"); c.row_factory = sqlite3.Row
def g(s):
    s = re.sub(r"\s+", "", (s or "").lower()); return {s[i:i + 2] for i in range(len(s) - 1)}
def gw(s):  # 英文词（摘要多为英文、证据多为中文，用英文术语和数字对齐）
    return set(re.findall(r"[a-z][a-z0-9\-]{2,}|\d+(?:\.\d+)?", (s or "").lower()))
papers = {r["pid"]: r for r in c.execute("SELECT pid,title,abstract FROM papers WHERE pid IN (SELECT pid FROM screening WHERE run_id=? AND decision='include')", (run,))}
pw = {p: gw((r["title"] or "") + " " + (r["abstract"] or "")) for p, r in papers.items()}
out = []
for e in c.execute("SELECT eid,pid,finding,population,condition,measure,n,basis FROM evidence WHERE run_id=?", (run,)):
    ew = gw(" ".join(e[k] or "" for k in ("finding", "population", "condition", "measure", "n")))
    if len(ew) < 4: continue
    sc = lambda p: len(ew & pw.get(p, set())) / len(ew)
    own = sc(e["pid"])
    best = max(((sc(p), p) for p in papers if p != e["pid"]), default=(0, None))
    if best[0] >= max(0.35, 2 * own) and best[0] - own >= 0.2:
        out.append({"eid": e["eid"], "pid": e["pid"], "own": round(own, 2), "better": best[1], "better_score": round(best[0], 2), "basis": e["basis"], "finding": (e["finding"] or "")[:120]})
out.sort(key=lambda x: x["own"] - x["better_score"])
(ROOT / "out" / run).mkdir(exist_ok=True)
(ROOT / "out" / run / "attribution_suspects.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{run}：证据中疑似挂错文献 {len(out)} 条（涉及 {len({o['pid'] for o in out})} 篇）")
for o in out[:15]: print(f"  {o['eid']} 本篇 {o['own']} vs {o['better']} {o['better_score']} [{o['basis']}] {o['finding'][:70]}")
