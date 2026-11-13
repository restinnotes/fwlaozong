import json, sys, glob, os
sys.stdout.reconfigure(encoding='utf-8')
ok, bad = [], []
for acct in ('gpt3', 'gpt4'):
    for d in glob.glob(f'D:/musicclaude/gpt2agent-safechain/runs/{acct}/pro-bridge-2026111*'):
        f = os.path.join(d, 'generation-network.json')
        if not os.path.exists(f): continue
        try: g = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        e = (g.get('elapsed_ms') or g.get('done_ms') or g.get('last_chunk_ms') or 0) / 1000
        (ok if g.get('done_seen') else bad).append((round(e), acct, g.get('error_type'), os.path.basename(d)))
ok.sort(reverse=True); bad.sort(reverse=True)
print('成功（收到 DONE）的最长 8 次：', ok[:8])
print('失败里超过 1500 秒的：', [b for b in bad if b[0] > 1500])
print('成功', len(ok), '失败', len(bad))
