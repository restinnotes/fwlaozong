"""研究者审核工作台（AROS M08）。启动：streamlit run tools/workbench.py

只有这里的人工操作能把证据、结论、假说设成 verified / rejected（AROS 3.3：AI 不能自动设 verified）。
每次审核写 history（actor=human），可回溯。
"""
import json, re, sys
from pathlib import Path

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
st.set_page_config(page_title="科研工作台", layout="wide")
c = kb.connect()

tags = sorted({r[0] for r in c.execute("SELECT DISTINCT run_id FROM screening UNION SELECT DISTINCT run_id FROM evidence")})
qs = sorted({r[0] for r in c.execute("SELECT DISTINCT question FROM screening")}) or ["Q1"]
with st.sidebar:
    st.title("科研工作台")
    q = st.selectbox("研究问题", qs)
    tag = st.selectbox("系统版本", tags or ["S1"])
    page = st.radio("页面", ["项目", "文献", "证据", "结论与假说", "评估", "导出"])
    qf = ROOT / "questions" / f"{q}.md"
    if qf.exists(): st.caption(qf.read_text(encoding="utf-8")[:400])


def review_buttons(table, key_col, key, cur, note_col=None):
    cols = st.columns([1, 1, 1, 3])
    note = cols[3].text_input("审核备注", key=f"note_{table}_{key}")
    for i, s in enumerate(["verified", "rejected", "pending"]):
        if cols[i].button({"verified": "✅ 确认", "rejected": "❌ 驳回", "pending": "↩ 待审"}[s], key=f"{s}_{table}_{key}", disabled=(cur == s)):
            c.execute(f"UPDATE {table} SET review_status=?{', reviewer_note=?' if note_col else ''} WHERE {key_col}=?",
                      (s, note, key) if note_col else (s, key))
            kb.hist(c, table, key, "review", {"actor": "human", "from": cur, "to": s, "note": note})
            c.commit(); st.rerun()


def context(src, quote, width=700):
    words = re.findall(r"[A-Za-z0-9]+", quote or "")
    for n in (8, 6, 4):
        for i in range(0, max(1, len(words) - n + 1)):
            pat = r"\W+".join(map(re.escape, words[i:i + n]))
            m = re.search(pat, src, re.I) if pat else None
            if m:
                a, b = max(0, m.start() - width), min(len(src), m.end() + width)
                return src[a:m.start()] + " **〔" + src[m.start():m.end()] + "〕** " + src[m.end():b]
    return None


if page == "项目":
    st.header("项目状态")
    st.json(kb.stats(c))
    s = ROOT / "STATUS.md"
    if s.exists(): st.markdown(s.read_text(encoding="utf-8"))

elif page == "文献":
    st.header("文献")
    df = pd.read_sql_query("SELECT p.pid, p.year, p.title, p.journal, s.decision, s.reason, p.fulltext_kind, p.sources "
                           "FROM papers p LEFT JOIN screening s ON s.pid=p.pid AND s.run_id=? AND s.question=? "
                           "ORDER BY s.decision, p.year DESC", c, params=(tag, q))
    kw = st.text_input("搜索题目")
    dec = st.multiselect("筛选结果", ["include", "maybe", "exclude"], default=["include"])
    v = df[df["decision"].isin(dec)] if dec else df
    if kw: v = v[v["title"].str.contains(kw, case=False, na=False)]
    st.caption(f"{len(v)} 篇")
    st.dataframe(v, width='stretch', height=600)

elif page == "证据":
    st.header("证据矩阵")
    df = pd.read_sql_query("SELECT e.eid, e.pid, p.year, e.design, e.population, e.n, e.condition, e.measure, e.finding, e.effect, "
                           "e.basis, e.quote_check, e.review_status FROM evidence e JOIN papers p USING(pid) "
                           "WHERE e.run_id=? AND e.question=? ORDER BY p.year", c, params=(tag, q))
    f1, f2 = st.columns(2)
    rs = f1.multiselect("审核状态", ["pending", "verified", "rejected"], default=["pending", "verified", "rejected"])
    qc = f2.multiselect("原句核对", sorted(df["quote_check"].dropna().unique()), default=[])
    v = df[df["review_status"].isin(rs)]
    if qc: v = v[v["quote_check"].isin(qc)]
    st.caption(f"{len(v)} 条；原句核对 not_found 的优先人工看")
    st.dataframe(v, width='stretch', height=320)
    eid = st.selectbox("选一条证据做原文对照", v["eid"].tolist())
    if eid:
        e = c.execute("SELECT e.*, p.title, p.abstract, p.fulltext_path FROM evidence e JOIN papers p USING(pid) WHERE eid=?", (eid,)).fetchone()
        L, R = st.columns(2)
        with L:
            st.subheader("提取记录（AI）")
            for k in ("design", "population", "n", "condition", "measure", "finding", "effect", "limitations", "basis", "quote_check"):
                st.markdown(f"**{k}**：{e[k] or ''}")
            st.markdown(f"**quote**：> {e['quote'] or ''}")
            st.markdown(f"**审核状态**：`{e['review_status']}`  {e['reviewer_note'] or ''}")
            review_buttons("evidence", "eid", eid, e["review_status"], note_col=True)
        with R:
            st.subheader(f"原文：{e['title']}")
            src = e["abstract"] or ""
            f = e["fulltext_path"]
            if f and Path(f).exists() and f.endswith((".txt", ".html")):
                src = Path(f).read_text(encoding="utf-8", errors="ignore")
            ctx = context(src, e["quote"])
            if ctx: st.markdown(ctx)
            else:
                st.warning("原文里没定位到这句。" + ("（全文是 PDF，请打开文件核对）" if f and f.endswith(".pdf") else ""))
                if f and f.endswith(".pdf"): st.code(f)
                st.text_area("摘要", e["abstract"] or "", height=300)

elif page == "结论与假说":
    st.header("结论")
    for cl in c.execute("SELECT * FROM claims WHERE run_id=? AND question=?", (tag, q)):
        with st.expander(f"[{cl['status']}] {cl['text'][:120]}  · {cl['review_status']}"):
            st.markdown(f"层级 **{cl['level']}**；不确定性：{cl['uncertainty']}")
            ev = pd.read_sql_query("SELECT ce.relation, ce.note, e.eid, e.finding, e.condition, e.quote_check, e.review_status "
                                   "FROM claim_evidence ce JOIN evidence e USING(eid) WHERE ce.cid=?", c, params=(cl["cid"],))
            st.dataframe(ev, width='stretch')
            review_buttons("claims", "cid", cl["cid"], cl["review_status"])
    st.header("竞争性假说")
    for h in c.execute("SELECT * FROM hypotheses WHERE run_id=? AND question=?", (tag, q)):
        with st.expander(f"{h['name']}  · {h['review_status']}"):
            st.markdown(h["text"] or "")
            st.markdown("**预测**"); [st.markdown(f"- {x}") for x in json.loads(h["predictions"] or "[]")]
            st.markdown("**反证条件**"); [st.markdown(f"- {x}") for x in json.loads(h["falsifiers"] or "[]")]
            rel = pd.read_sql_query("SELECT hc.relation, cl.text FROM hypothesis_claims hc JOIN claims cl USING(cid) WHERE hc.hid=?",
                                    c, params=(h["hid"],))
            st.dataframe(rel, width='stretch')
            review_buttons("hypotheses", "hid", h["hid"], h["review_status"])

elif page == "评估":
    st.header("评估")
    vers = sorted(p.name for p in OUT.iterdir() if p.is_dir())
    for vname in vers:
        d = OUT / vname
        with st.expander(vname):
            for f in ("refcheck.json", "open_g6.json", "open_g56.json", "abs_g6.json"):
                if (d / f).exists():
                    st.markdown(f"**{f}**"); st.json(json.loads((d / f).read_text(encoding="utf-8")), expanded=False)
    for f in sorted(OUT.glob("blind_*.json")):
        st.markdown(f"**{f.name}**"); st.dataframe(pd.DataFrame(json.loads(f.read_text(encoding="utf-8"))), width='stretch')

elif page == "导出":
    st.header("导出")
    rp = OUT / tag / "report.md"
    if rp.exists():
        st.download_button("报告 Markdown", rp.read_bytes(), file_name=f"{tag}_report.md")
        st.markdown(rp.read_text(encoding="utf-8"))
    for name, sql in {"evidence": "SELECT * FROM evidence WHERE run_id=?", "claims": "SELECT * FROM claims WHERE run_id=?",
                      "hypotheses": "SELECT * FROM hypotheses WHERE run_id=?"}.items():
        df = pd.read_sql_query(sql, c, params=(tag,))
        st.download_button(f"{name}.csv（{len(df)} 行）", df.to_csv(index=False).encode("utf-8-sig"), file_name=f"{tag}_{name}.csv")
    hist = pd.read_sql_query("SELECT * FROM history ORDER BY id DESC LIMIT 500", c)
    st.download_button("审核与修改历史.json", hist.to_json(orient="records", force_ascii=False).encode("utf-8"), file_name="history.json")
