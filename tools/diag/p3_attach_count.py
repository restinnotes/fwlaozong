import json, glob, os, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
ok, bad = Counter(), Counter()
for acct in ('gpt3', 'gpt4'):
    for d in glob.glob(f'D:/musicclaude/gpt2agent-safechain/runs/{acct}/pro-bridge-*'):
        m = os.path.join(d, 'attachment-manifest.json'); r = os.path.join(d, 'result.json')
        if not os.path.exists(m) or not os.path.exists(r): continue
        try: n = len(json.load(open(m, encoding='utf-8'))); res = json.load(open(r, encoding='utf-8'))
        except Exception: continue
        (ok if str(res.get('ok')) == 'True' else bad)[(n, res.get('code'))] += 1
print('成功：附件数分布', sorted((k[0], v) for k, v in ok.items()))
print('失败：(附件数, 错误码)', sorted(bad.items())[-15:])
