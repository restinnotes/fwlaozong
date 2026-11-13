import json, sys
sys.stdout.reconfigure(encoding='utf-8'); sys.path.insert(0, 'tools')
import lit
plan = json.load(open('out/S1/plan.json', encoding='utf-8'))
seeds = json.load(open('out/S1/search_seeds.json', encoding='utf-8'))
miss = [x for x in seeds if x['exists'] and not x['in_search']]
res = []
for x in miss:
    pmid = x['pid'].split(':')[1]
    matched = []
    for i, q in enumerate(plan['queries']):
        n, _ = lit.epmc_search(f"({q['q']}) AND EXT_ID:{pmid} AND SRC:MED", max_n=1)
        if n: matched.append(i + 1)
    res.append({'pid': x['pid'], 'title': x['title_found'], 'matched_queries': matched})
    print(x['pid'], '被检索式匹配：', matched or '无', '|', (x['title_found'] or '')[:60], flush=True)
json.dump(res, open('out/S1/i02a_recall.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('匹配到但被前 100 截掉：', sum(bool(r['matched_queries']) for r in res), '/', len(res))
