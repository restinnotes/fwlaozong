"""整点检查：最近一小时调用完成/失败、零秒失败（calls.jsonl 字段 started/seconds/completed）。"""
import json, time, sys
from pathlib import Path
R = Path(__file__).resolve().parents[2] / "runs"
since = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() - 3600 * float(sys.argv[1] if len(sys.argv) > 1 else 1)))
ok = bad = zero = 0
for l in open(R / "calls.jsonl", encoding="utf-8"):
    try: d = json.loads(l)
    except Exception: continue
    if (d.get("started") or "") < since: continue
    if d.get("completed"): ok += 1
    else:
        bad += 1; zero += (d.get("seconds") or 0) < 5
print(f"最近一小时：完成 {ok}，失败 {bad}（其中零秒失败 {zero}）")
