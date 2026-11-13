"""gpt3 / gpt4 调用封装（照 musicclaude 的 evo.call 精简改写）。

- 两个账号：gpt3（默认账号）、gpt4（第二个账号）。两者都是 GPT-6 Thinking / max，可选 GPT-5.6。
- 按调用编号缓存：runs/<编号>/output.txt 存在就直接返回，不再发请求。改了提示词必须换编号。
- 按编号的 crc32 固定分流到两个账号；一个账号失败，这次改走另一个。
- 账号报异常活动（UPSTREAM_UNUSUAL_ACTIVITY）→ 标成冷却 50 分钟；两个都冷却就等。
- 每账号两次提交起始至少间隔 MIN_GAP 秒（musicclaude 同时在用同一账号）。
- 每次调用记一行 runs/calls.jsonl。
"""
import hashlib, json, os, re, subprocess, threading, time, zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"; RUNS.mkdir(exist_ok=True)
BIN = Path("D:/musicclaude/gpt2agent-safechain/bin")
CLI = {"gpt3": str(BIN / "gpt3.cmd"), "gpt4": str(BIN / "gpt4.cmd")}
G6, G56 = "gpt-6-thinking", "gpt-5-6-thinking"
MIN_GAP = float(os.environ.get("LLM_MIN_GAP", "7"))
COOL = 50 * 60
MAX_CHARS = 65000

_gap = {a: threading.Lock() for a in CLI}
_last = {a: 0.0 for a in CLI}
_logl = threading.Lock()


def _log(rec):
    with _logl, (RUNS / "calls.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _cool_file(acct):
    return RUNS / f"{acct}_protected.json"


def cooling(acct):
    try:
        return json.loads(_cool_file(acct).read_text(encoding="utf-8")).get("until", 0) > time.time()
    except (OSError, ValueError):
        return False


def _mark_cool(acct, run_id, why):
    _cool_file(acct).write_text(json.dumps({"until": time.time() + COOL, "run": run_id, "why": str(why)[:300],
                                            "at": time.strftime("%Y-%m-%d %H:%M:%S")}, ensure_ascii=False), encoding="utf-8")
    print(f"[{run_id}] {acct} 报异常活动，冷却 50 分钟，之后改走另一个账号", flush=True)


def other(acct):
    return "gpt4" if acct == "gpt3" else "gpt3"


def pick(run_id, acct=None):
    a = acct or ("gpt4" if zlib.crc32(run_id.encode()) % 2 else "gpt3")
    if cooling(a) and not cooling(other(a)):
        a = other(a)
    while cooling(a) and cooling(other(a)):
        ends = []
        for x in CLI:
            try: ends.append(json.loads(_cool_file(x).read_text(encoding="utf-8"))["until"])
            except Exception: ends.append(0)
        wait = max(0, min(ends) - time.time()) + 10
        print(f"[{run_id}] 两个账号都在冷却，等 {round(wait / 60)} 分钟", flush=True)
        time.sleep(wait)
    return a


def done(run_id):
    return (RUNS / run_id / "output.txt").exists()


def output(run_id):
    p = RUNS / run_id / "output.txt"
    return p.read_text(encoding="utf-8-sig") if p.exists() else None


def pid(text, n=8):
    """提示词哈希，拼进调用编号，改了提示词自动换编号。"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:n]


def _once(acct, run_id, d, message, attach, model, stage):
    inp = d / "input.txt"; inp.write_text(message, encoding="utf-8")
    with _gap[acct]:
        w = MIN_GAP - (time.time() - _last[acct])
        if w > 0: time.sleep(w)
        _last[acct] = time.time()
    cmd = [CLI[acct], "ask", "--file", str(inp), "--json", "--model", model]
    for a in attach:
        cmd += ["--attach", str(a)]
    t0 = time.time(); started = time.strftime("%Y-%m-%dT%H:%M:%S")
    cp = subprocess.run(cmd, capture_output=True)
    dt = time.time() - t0
    (d / f"stdout_{acct}.bin").write_bytes(cp.stdout); (d / f"stderr_{acct}.bin").write_bytes(cp.stderr)
    try: j = json.loads(cp.stdout.decode("utf-8"))
    except Exception: j = {}
    md = j.get("metadata") or {}
    err = {}
    for line in cp.stderr.decode("utf-8", "replace").splitlines():
        try:
            c = json.loads(line)
            if isinstance(c, dict) and c.get("error_code"): err = c
        except (ValueError, TypeError):
            pass
    if not err and isinstance(j, dict) and j.get("error_code"):
        err = j
    ok = cp.returncode == 0 and j.get("completed") is True and bool(j.get("response"))
    if ok and (md.get("model") != model or md.get("thinking_effort") != "max"):
        ok = False
    job = md.get("job_directory") or err.get("job_directory")
    resp = j.get("response") if ok else None
    if not ok and job:   # 校验器拒了但任务其实完整：从任务目录取回
        try:
            rj = json.loads((Path(job) / "result.json").read_text(encoding="utf-8"))
            rt = (Path(job) / "response.txt").read_text(encoding="utf-8-sig")
            if str(rj.get("ok")) == "True" and rj.get("model") == model and str(rj.get("thinkingEffort")) == "max" and rt.strip():
                ok, resp = True, rt
        except Exception:
            pass
    rec = {"run_id": run_id, "account": acct, "model": model, "stage": stage, "started": started, "seconds": round(dt),
           "exit_code": cp.returncode, "completed": ok, "job_directory": job, "session_handle": md.get("session_handle"),
           "message_chars": len(message), "attach": [str(a) for a in attach],
           "error_code": err.get("error_code"), "error": (err.get("message") or "")[:300] if err else None}
    if ok:
        rec["response_chars"] = len(resp)
        (d / "call.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / "output.txt").write_text(resp, encoding="utf-8")
    else:
        rec["stderr_tail"] = cp.stderr.decode("utf-8", "replace")[-600:]
        (d / f"fail_{acct}_{int(t0)}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    _log(rec)
    print(f"[{run_id}] {acct} {model} {'完成' if ok else '失败 ' + str(rec['error_code'])} {dt:.0f}s"
          + (f" {len(resp)} 字" if ok else ""), flush=True)
    return resp, rec


def call(run_id, message, attach=(), model=G6, acct=None, stage=""):
    """一次全新的 Temporary 会话提问。返回回答文本；两个账号都失败返回 None。"""
    if done(run_id):
        return output(run_id)
    assert len(message) <= MAX_CHARS, f"{run_id}: 提示词过长 {len(message)} 字"
    assert message.strip(), f"{run_id}: 提示词为空"
    for a in attach:
        assert Path(a).exists() and Path(a).stat().st_size > 0, f"{run_id}: 附件不存在或为空 {a}"
    d = RUNS / run_id; d.mkdir(parents=True, exist_ok=True)
    (d / "meta.json").write_text(json.dumps({"stage": stage, "model": model, "attach": [str(a) for a in attach]},
                                            ensure_ascii=False), encoding="utf-8")
    a = pick(run_id, acct)
    tried = []
    for _ in range(2):   # 本账号一次，失败换另一个账号一次；不在同一账号上自动重发
        resp, rec = _once(a, run_id, d, message, list(attach), model, stage)
        if resp is not None:
            return resp
        tried.append(a)
        if rec.get("error_code") == "UPSTREAM_UNUSUAL_ACTIVITY" or "limit" in (rec.get("error") or "").lower():
            _mark_cool(a, run_id, rec.get("error_code") or rec.get("error"))
        nxt = other(a)
        if nxt in tried or cooling(nxt):
            break
        a = nxt
    return None


def _resume_once(acct, run_id, d, handle, message, model, stage):
    """在同一 Temporary 会话里续一轮（gpt3/gpt4 resume）。只能用原账号，不换号。"""
    inp = d / "input.txt"; inp.write_text(message, encoding="utf-8")
    with _gap[acct]:
        w = MIN_GAP - (time.time() - _last[acct])
        if w > 0: time.sleep(w)
        _last[acct] = time.time()
    cmd = [CLI[acct], "resume", handle, "--file", str(inp), "--json", "--model", model]
    t0 = time.time(); started = time.strftime("%Y-%m-%dT%H:%M:%S")
    cp = subprocess.run(cmd, capture_output=True); dt = time.time() - t0
    (d / f"stdout_{acct}.bin").write_bytes(cp.stdout); (d / f"stderr_{acct}.bin").write_bytes(cp.stderr)
    try: j = json.loads(cp.stdout.decode("utf-8"))
    except Exception: j = {}
    md = j.get("metadata") or {}
    ok = cp.returncode == 0 and j.get("completed") is True and bool(j.get("response")) and md.get("model") == model
    rec = {"run_id": run_id, "account": acct, "model": model, "stage": stage, "started": started, "seconds": round(dt),
           "exit_code": cp.returncode, "completed": ok, "resume_of": handle, "session_handle": md.get("session_handle") or handle,
           "job_directory": md.get("job_directory"), "message_chars": len(message)}
    if not ok:
        for line in cp.stderr.decode("utf-8", "replace").splitlines():
            try:
                c = json.loads(line)
                if isinstance(c, dict) and c.get("error_code"): rec["error_code"] = c["error_code"]
            except (ValueError, TypeError): pass
        rec["stderr_tail"] = cp.stderr.decode("utf-8", "replace")[-600:]
    _log(rec)
    print(f"[{run_id}] {acct} 续接 {'完成' if ok else '失败 ' + str(rec.get('error_code'))} {dt:.0f}s", flush=True)
    if ok:
        (d / "call.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / "output.txt").write_text(j["response"], encoding="utf-8")
        return j["response"], rec
    return None, rec


def session(run_id, first, follow="继续", done_mark="【完成】", more_mark="【继续】", max_turns=8, model=G6, acct=None, stage="", attach=()):
    """多轮完成一个任务（通道单次回答上限约 1770 秒，见猜想台账 P2）。
    第一轮发 first；回答最后一行有 more_mark 就只回复 follow，直到出现 done_mark 或到 max_turns。
    每轮按 run_id_t<k> 缓存；某一轮失败，整个会话从头重来（续接失败的会话会被冻结，不能重发）。返回各轮回答列表。"""
    a = pick(run_id, acct)
    answers = []
    t0 = f"{run_id}_t0"
    if done(t0):
        answers.append(output(t0)); handle = json.loads((RUNS / t0 / "call.json").read_text(encoding="utf-8"))["session_handle"]
        a = json.loads((RUNS / t0 / "call.json").read_text(encoding="utf-8"))["account"]
    else:
        r = call(t0, first, attach=attach, model=model, acct=a, stage=stage)
        if r is None: return None
        answers.append(r); cj = json.loads((RUNS / t0 / "call.json").read_text(encoding="utf-8"))
        handle, a = cj["session_handle"], cj["account"]
    k = 0
    while more_mark in answers[-1][-200:] and done_mark not in answers[-1][-200:] and k + 1 < max_turns:
        k += 1; rid = f"{run_id}_t{k}"
        if done(rid):
            answers.append(output(rid)); handle = json.loads((RUNS / rid / "call.json").read_text(encoding="utf-8"))["session_handle"]; continue
        d = RUNS / rid; d.mkdir(parents=True, exist_ok=True)
        r, rec = _resume_once(a, rid, d, handle, follow, model, stage)
        if r is None: return None
        answers.append(r); handle = rec["session_handle"]
    return answers


def salvage_items(text, first_key):
    """整体 JSON 坏掉时（11-13：GPT-5.6 在条目之间插了 '"}]}' 之类的碎片），逐个解析以 {"first_key" 开头的条目。只取能完整解析的，不改内容。"""
    s = re.sub(r"</?escape>", "", text or "")
    out, dec = [], json.JSONDecoder()
    for m in re.finditer(r'\{\s*"' + re.escape(first_key) + '"', s):
        try:
            obj, _ = dec.raw_decode(s[m.start():])
            if isinstance(obj, dict): out.append(obj)
        except ValueError:
            pass
    return out


def parse_json(text):
    """从回答里取出第一个 JSON 对象（可在 ```json 代码块里）。"""
    if text is None: raise ValueError("无回答")
    s = re.sub(r"</?escape>", "", text)   # 11-13：GPT-5.6 回答里夹了 <escape> 标签，打断 JSON
    if "```" in s:
        for block in s.split("```")[1::2]:
            b = block[4:] if block.startswith("json") else block
            try: return json.loads(b.strip())
            except ValueError: pass
    i = min([k for k in (s.find("{"), s.find("[")) if k >= 0], default=-1)
    if i < 0: raise ValueError("回答里没有 JSON")
    try:
        return json.JSONDecoder().raw_decode(s[i:])[0]
    except ValueError:
        # 11-13：GPT-5.6 偶尔多写逗号（"},\n," 或结尾逗号）。只修逗号，不改内容。
        fixed = re.sub(r",(\s*,)+", ",", s[i:])
        fixed = re.sub(r",(\s*[\]}])", r"\1", fixed)
        return json.JSONDecoder().raw_decode(fixed)[0]
