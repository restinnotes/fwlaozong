"""报告细节量（用户判定 11-14："细节有点缺乏"）：正文字数、引用不同文献数、样本量提及、P 值、效应量/置信区间处数。"""
import re, sys
from pathlib import Path
OUT = Path(__file__).resolve().parents[2] / "out"
for t in sys.argv[1:]:
    p = OUT / t / "report.md"
    if not p.exists(): print(t, "无"); continue
    s = p.read_text(encoding="utf-8")
    body = s.split("### 检索与筛选记录")[0].split("### 附表：各结论的研究独立性")[0]
    refs = set(re.findall(r"(PMID[:：]\s?\d+|DOI[:：]\s?10\.[^\s\]\)；，;,（|]+)", body))
    n = len(re.findall(r"\d+\s*(?:例|名|位|人)", body)) + len(re.findall(r"\bn\s*=\s*\d+", body, re.I))
    pv = len(re.findall(r"\bP\s*[<=＜≤]\s*0?\.\d+", body, re.I))
    es = len(re.findall(r"(?:95%\s*CI|置信区间|\bOR\b|\bHR\b|\bMD\b|\bSMD\b|Cohen|\br\s*=\s*-?0?\.\d+|AUC|\bβ\s*=|效应量)", body))
    print(f"{t}: 正文 {len(body)} 字，引用不同文献 {len(refs)} 篇，样本量提及 {n} 处，P 值 {pv} 处，效应量/区间 {es} 处")
