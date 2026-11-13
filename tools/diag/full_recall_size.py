"""S4R 规划：22 条检索式全量取编号（不取摘要，不调模型），看去重后的规模，以及对 43 篇必读的召回。"""
import json, sys, urllib.parse
sys.stdout.reconfigure(encoding="utf-8"); sys.path.insert(0, "tools")
import lit
plan = json.load(open("out/S1/plan.json", encoding="utf-8"))
seeds = json.load(open("out/S1/search_seeds.json", encoding="utf-8"))
allids, per = set(), []
for q in plan["queries"]:
    ids, cursor = [], "*"
    while True:
        u = (f"{lit.EPMC}/search?query={urllib.parse.quote(q['q'])}&format=json&resultType=idlist&pageSize=1000&cursorMark={urllib.parse.quote(cursor)}")
        d = json.loads(lit._get(u, timeout=120))
        rs = d.get("resultList", {}).get("result", [])
        ids += [f"PMID:{r['pmid']}" if r.get("pmid") else f"{r.get('source')}:{r.get('id')}" for r in rs]
        nxt = d.get("nextCursorMark")
        if not rs or not nxt or nxt == cursor: break
        cursor = nxt
    per.append((len(ids), q["q"][:60])); allids |= set(ids)
    print(f"{len(ids):>6}  {q['q'][:80]}", flush=True)
seed_pids = {s["pid"] for s in seeds if s["exists"]}
print("全量去重", len(allids), "篇；必读召回", len(seed_pids & allids), "/", len(seed_pids))
json.dump(sorted(allids), open("out/S1/full_ids.json", "w", encoding="utf-8"))
