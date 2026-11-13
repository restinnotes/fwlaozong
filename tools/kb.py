"""分层知识库（SQLite，kb/kb.sqlite3）。

层次（标准第 4 条）：文献 papers → 证据 evidence（单项研究的具体发现，带研究条件和出处）
→ 结论 claims（跨研究综合，带证据关系 claim_evidence）→ 假说 hypotheses（机制解释，带预测和反证条件，关联结论）。
每次写入都记一行 history，旧结论不删，用 superseded_by 指向新版本（标准第 5 条：可修订、可回溯）。
"""
import json, sqlite3, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "kb" / "kb.sqlite3"

SCHEMA = """
CREATE TABLE IF NOT EXISTS papers(
  pid TEXT PRIMARY KEY, pmid TEXT, pmcid TEXT, doi TEXT, title TEXT, authors TEXT, journal TEXT, year INTEGER,
  abstract TEXT, pub_type TEXT, is_oa TEXT, fulltext_path TEXT, fulltext_kind TEXT, sources TEXT, added_at TEXT);
CREATE TABLE IF NOT EXISTS queries(
  qid INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, engine TEXT, text TEXT, hit_count INTEGER, kept INTEGER,
  run_id TEXT, at TEXT);
CREATE TABLE IF NOT EXISTS screening(
  question TEXT, pid TEXT, decision TEXT, reason TEXT, run_id TEXT, at TEXT, PRIMARY KEY(question, pid, run_id));
CREATE TABLE IF NOT EXISTS evidence(
  eid TEXT PRIMARY KEY, question TEXT, pid TEXT, design TEXT, population TEXT, n TEXT, condition TEXT,
  measure TEXT, finding TEXT, effect TEXT, limitations TEXT, quote TEXT, basis TEXT, run_id TEXT, at TEXT);
CREATE TABLE IF NOT EXISTS claims(
  cid TEXT PRIMARY KEY, question TEXT, text TEXT, level TEXT, status TEXT, uncertainty TEXT,
  superseded_by TEXT, run_id TEXT, at TEXT);
CREATE TABLE IF NOT EXISTS claim_evidence(cid TEXT, eid TEXT, relation TEXT, note TEXT, PRIMARY KEY(cid, eid));
CREATE TABLE IF NOT EXISTS hypotheses(
  hid TEXT PRIMARY KEY, question TEXT, name TEXT, text TEXT, predictions TEXT, falsifiers TEXT, status TEXT,
  superseded_by TEXT, run_id TEXT, at TEXT);
CREATE TABLE IF NOT EXISTS hypothesis_claims(hid TEXT, cid TEXT, relation TEXT, PRIMARY KEY(hid, cid));
CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT, tbl TEXT, key TEXT, action TEXT,
  detail TEXT, run_id TEXT, at TEXT);
"""


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S")


MIGRATIONS = [
    # AROS 方案 3.3：pending / verified / rejected 分开，AI 不能自己设 verified（只有 tools/review_ui 的人工操作能设）
    ("evidence", "review_status", "TEXT DEFAULT 'pending'"),
    ("evidence", "quote_check", "TEXT"),          # 原句机械核对：found / partial / not_found / no_source
    ("evidence", "reviewer_note", "TEXT"),
    ("claims", "review_status", "TEXT DEFAULT 'pending'"),
    ("hypotheses", "review_status", "TEXT DEFAULT 'pending'"),
    # S3c（顾问"研究级证据账本"）：extract_v2 的完整字段（分母、终点类别、事件阶段、偏倚风险、版本/队列候选、来源定位）
    ("evidence", "extra", "TEXT"),
    ("papers", "version_of", "TEXT"),          # 预印本 → 正式版 pid（程序按标题相似度判定）
    ("papers", "publication_status", "TEXT"),
]


def connect():
    DB.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(DB, timeout=60)
    c.row_factory = sqlite3.Row
    c.executescript(SCHEMA)
    for t, col, decl in MIGRATIONS:
        if col not in {r[1] for r in c.execute(f"PRAGMA table_info({t})")}:
            c.execute(f"ALTER TABLE {t} ADD COLUMN {col} {decl}")
    c.commit()
    return c


def hist(c, tbl, key, action, detail="", run_id=""):
    c.execute("INSERT INTO history(tbl,key,action,detail,run_id,at) VALUES(?,?,?,?,?,?)",
              (tbl, key, action, detail if isinstance(detail, str) else json.dumps(detail, ensure_ascii=False), run_id, now()))


def paper_id(rec):
    if rec.get("pmid"): return f"PMID:{rec['pmid']}"
    if rec.get("doi"): return f"DOI:{rec['doi'].lower()}"
    if rec.get("pmcid"): return f"PMC:{rec['pmcid']}"
    return None


def upsert_paper(c, rec, source):
    pid = paper_id(rec)
    if not pid: return None
    old = c.execute("SELECT * FROM papers WHERE pid=?", (pid,)).fetchone()
    if old:
        srcs = set(json.loads(old["sources"] or "[]")) | {source}
        fields = {k: rec.get(k) for k in ("pmcid", "doi", "title", "authors", "journal", "year", "abstract", "pub_type", "is_oa")
                  if rec.get(k) and not old[k]}
        sets = ", ".join(f"{k}=?" for k in fields)
        c.execute(f"UPDATE papers SET sources=?{', ' + sets if sets else ''} WHERE pid=?",
                  (json.dumps(sorted(srcs)), *fields.values(), pid))
        return pid
    c.execute("INSERT INTO papers(pid,pmid,pmcid,doi,title,authors,journal,year,abstract,pub_type,is_oa,sources,added_at)"
              " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (pid, rec.get("pmid"), rec.get("pmcid"), (rec.get("doi") or "").lower() or None, rec.get("title"),
               rec.get("authors"), rec.get("journal"), rec.get("year"), rec.get("abstract"), rec.get("pub_type"),
               rec.get("is_oa"), json.dumps([source]), now()))
    hist(c, "papers", pid, "add", {"source": source})
    return pid


def stats(c):
    out = {}
    for t in ("papers", "queries", "screening", "evidence", "claims", "hypotheses"):
        out[t] = c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    out["fulltext"] = c.execute("SELECT COUNT(*) FROM papers WHERE fulltext_path IS NOT NULL").fetchone()[0]
    out["included"] = c.execute("SELECT COUNT(DISTINCT pid) FROM screening WHERE decision='include'").fetchone()[0]
    return out
