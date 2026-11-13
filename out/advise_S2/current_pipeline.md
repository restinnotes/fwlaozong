# 主线：现行流水线

**当前主线版本**：S2（11-13 收下：S1 的流程 + 分片综合）。基线：B0（One-shot，A 组）、B1（同材料 One-shot，B 组）。

## 系统 v0（S1）的步骤

| 步 | 层 | 做什么 | 谁做 | 命令 | 产出 |
|---|---|---|---|---|---|
| plan | L1 | 拆子问题、出 12–25 条 Europe PMC 检索式、联网点名必读文献 | gpt3 GPT-6 max | `run.py plan` | `out/<tag>/plan.json` |
| search | L1 | 本地跑检索式（每条取前 100 篇），必读文献查真假并核对本地检索有没有覆盖 | 脚本（Europe PMC / PubMed 公开接口） | `run.py search` | 知识库 `papers`、`queries`；`pool.json`、`search_seeds.json` |
| screen | L1 | 每批 30 篇看题目+摘要，include / maybe / exclude | gpt3/gpt4 GPT-6，并行 4 | `run.py screen` | `screening` 表 |
| fetch | L2 | include 的文献拿全文：本地 Europe PMC 开放全文 → 拿不到的一次交给 codex luna | 脚本 + `codex exec -m gpt-6-luna` max | `run.py fetch` | `papers/`；`runs/luna_calls.jsonl` |
| extract | L3 | 有全文的一篇一调用（文本内联或 PDF 附件上传）；只有摘要的 20 篇一批 | gpt3/gpt4 GPT-6，并行 4 | `run.py extract` | `evidence` 表 |
| synthesize | L4 | 分片综合：全部证据按年份切片（每片 ≤4.8 万字）各出局部结论 → 分组合并 → 最终合并出结论、竞争性假说、缺口；证据关联由程序按 from 映射，不让模型抄 | gpt3/gpt4 GPT-6 | `run.py synthesize` | `synth_parts.json`、`synth_merge*.json`、`synthesis.json` |
| report | L5 | 只用知识库内容写报告；放不下时结论内联、完整证据表作附件 | gpt3 GPT-6 | `run.py report` | `report.md`、`appendix.json`、`evidence_table.txt` |

知识库：`kb/kb.sqlite3`（`tools/kb.py`），文献 → 证据 → 结论 → 假说四层，每次写入记 `history`。

## 测法

见 `迭代准则.md` 第七节。命令：`run.py refcheck`、`run.py review`、`run.py blind`。

## 修订记录

- 11-13 建立 S1（系统 v0）。
- 11-13 收下 S2：综合改为分片 + 合并（修 S1 截断缺陷 P4）。盲比 vs B0_gpt3 4:0、vs B1 4:0、vs B0_gpt4 2:2。
