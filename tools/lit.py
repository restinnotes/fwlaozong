"""本地文献检索层：Europe PMC（含 PubMed、PMC、预印本）和 PubMed E-utilities。

补 gpt3/gpt4 自带联网"查得不够全"的问题：检索式由模型出，检索由这里的脚本用公开 API 执行，
命中的全部元数据和摘要进知识库，再交给模型筛。只用公开免费接口，不需要账号。
"""
import json, re, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

UA = {"User-Agent": "research-kb/0.1 (literature search script)"}
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
_last = [0.0]


def _get(url, timeout=60, tries=3):
    for k in range(tries):
        w = 0.4 - (time.time() - _last[0])
        if w > 0: time.sleep(w)
        _last[0] = time.time()
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            if k == tries - 1: raise
            time.sleep(2 * (k + 1))


def _strip(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def epmc_search(query, max_n=200, page=100):
    """Europe PMC 检索，返回 (命中总数, [记录])。记录字段对齐 kb.upsert_paper。"""
    out, cursor, total = [], "*", 0
    while len(out) < max_n:
        size = min(page, max_n - len(out))
        u = (f"{EPMC}/search?query={urllib.parse.quote(query)}&format=json&resultType=core"
             f"&pageSize={size}&cursorMark={urllib.parse.quote(cursor)}")
        d = json.loads(_get(u))
        total = d.get("hitCount", 0)
        rs = d.get("resultList", {}).get("result", [])
        for r in rs:
            pts = (r.get("pubTypeList") or {}).get("pubType") or []
            out.append({"pmid": r.get("pmid"), "pmcid": r.get("pmcid"), "doi": r.get("doi"),
                        "title": _strip(r.get("title")), "authors": r.get("authorString"),
                        "journal": (r.get("journalInfo") or {}).get("journal", {}).get("title") or r.get("bookOrReportDetails", {}).get("publisher"),
                        "year": int(r["pubYear"]) if str(r.get("pubYear", "")).isdigit() else None,
                        "abstract": _strip(r.get("abstractText")), "pub_type": "; ".join(pts) if isinstance(pts, list) else str(pts),
                        "is_oa": r.get("isOpenAccess"), "source_db": r.get("source")})
        nxt = d.get("nextCursorMark")
        if not rs or not nxt or nxt == cursor: break
        cursor = nxt
    return total, out


def pubmed_search(query, max_n=200):
    """PubMed 检索，返回 (命中总数, [PMID])。"""
    u = f"{EUTILS}/esearch.fcgi?db=pubmed&retmode=json&retmax={max_n}&term={urllib.parse.quote(query)}"
    d = json.loads(_get(u))["esearchresult"]
    return int(d.get("count", 0)), d.get("idlist", [])


def pubmed_fetch(pmids):
    """按 PMID 取元数据和摘要。"""
    out = []
    for i in range(0, len(pmids), 150):
        ids = ",".join(pmids[i:i + 150])
        x = ET.fromstring(_get(f"{EUTILS}/efetch.fcgi?db=pubmed&retmode=xml&id={ids}", timeout=120))
        for a in x.findall(".//PubmedArticle"):
            m = a.find("MedlineCitation"); art = m.find("Article")
            pmid = m.findtext("PMID")
            doi = next((e.text for e in a.findall(".//ArticleIdList/ArticleId") if e.get("IdType") == "doi"), None)
            pmc = next((e.text for e in a.findall(".//ArticleIdList/ArticleId") if e.get("IdType") == "pmc"), None)
            abst = " ".join("".join(t.itertext()) for t in art.findall(".//Abstract/AbstractText"))
            au = ", ".join(f"{x.findtext('LastName') or ''} {x.findtext('Initials') or ''}".strip()
                           for x in art.findall(".//AuthorList/Author")[:8])
            yr = art.findtext(".//Journal/JournalIssue/PubDate/Year") or (art.findtext(".//Journal/JournalIssue/PubDate/MedlineDate") or "")[:4]
            out.append({"pmid": pmid, "pmcid": pmc, "doi": doi, "title": "".join(art.find("ArticleTitle").itertext()) if art.find("ArticleTitle") is not None else "",
                        "authors": au, "journal": art.findtext(".//Journal/Title"), "year": int(yr) if yr.isdigit() else None,
                        "abstract": abst, "pub_type": "; ".join(p.text for p in art.findall(".//PublicationTypeList/PublicationType"))})
    return out


def lookup(ident):
    """按 PMID 或 DOI 查一篇，查不到返回 None（引用核验用）。"""
    ident = ident.strip()
    if re.fullmatch(r"\d{4,9}", ident):
        q = f"EXT_ID:{ident} AND SRC:MED"
    elif ident.lower().startswith("10."):
        q = f'DOI:"{ident}"'
    else:
        return None
    _, rs = epmc_search(q, max_n=1)
    if rs: return rs[0]
    if q.startswith("EXT_ID"):
        r = pubmed_fetch([ident])
        return r[0] if r else None
    return crossref(ident)   # 11-13 校准：Europe PMC 不收的期刊（如 Basal Ganglia）DOI 查不到，不能判伪造


def crossref(doi):
    try:
        d = json.loads(_get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}", timeout=30, tries=2))["message"]
    except Exception:
        return None
    return {"doi": doi, "title": _strip((d.get("title") or [""])[0]), "year": (d.get("issued", {}).get("date-parts") or [[None]])[0][0],
            "journal": (d.get("container-title") or [""])[0], "source_db": "crossref"}


def epmc_fulltext_xml(pmcid):
    """Europe PMC 开放获取全文 XML；拿不到返回 None。"""
    try:
        b = _get(f"{EPMC}/{pmcid}/fullTextXML", timeout=120, tries=2)
        return b if b and b.lstrip().startswith(b"<") and len(b) > 5000 else None
    except Exception:
        return None


def jats_to_text(xml_bytes):
    """把 JATS 全文 XML 转成带小节标题的纯文本（给模型读）。"""
    root = ET.fromstring(xml_bytes)
    parts = []
    t = root.find(".//article-meta/title-group/article-title")
    if t is not None: parts.append("# " + "".join(t.itertext()).strip())
    ab = root.find(".//article-meta/abstract")
    if ab is not None: parts.append("## Abstract\n" + " ".join("".join(p.itertext()).strip() for p in ab.iter("p")))
    body = root.find(".//body")

    def walk(sec, depth):
        title = sec.find("title")
        if title is not None: parts.append("#" * min(depth, 6) + " " + "".join(title.itertext()).strip())
        for ch in sec:
            if ch.tag == "p": parts.append("".join(ch.itertext()).strip())
            elif ch.tag == "sec": walk(ch, depth + 1)
            elif ch.tag in ("table-wrap", "fig"):
                cap = ch.find(".//caption")
                if cap is not None: parts.append(f"[{ch.tag} {ch.get('id', '')}] " + " ".join("".join(cap.itertext()).split()))
    if body is not None:
        for sec in body:
            if sec.tag == "sec": walk(sec, 2)
            elif sec.tag == "p": parts.append("".join(sec.itertext()).strip())
    return "\n\n".join(p for p in parts if p)
