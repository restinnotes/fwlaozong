# 自主科研系统（功能神经外科 / DBS–STN–FOG 起步）

仓库：https://github.com/restinnotes/fwlaozong 。当前主线 **S3d3**，进度看 `STATUS.md`。

**没有入库的东西**（`.gitignore`）：`papers/` 下载的论文全文（版权）、`runs/` 每次调用的原始输入输出（输入里含全文；只保留 `calls.jsonl`、`luna_calls.jsonl` 两个汇总）、`kb/kb.sqlite3` 知识库二进制、`spec/` 同学的 AROS 方案原文、`logs/`。换机器跑要先重建知识库（`run.py system`）。

用户给研究目的，系统用 gpt3/gpt4（本机 Pro Bridge CLI，GPT-6 Thinking max）完成检索规划、筛选、证据提取、综合、写报告和评审；本地脚本只做模型做不了或做不全的机械活：Europe PMC/PubMed 检索、开放全文下载、知识库存储、引用核验。本地下载不到的全文，一批一次交给 `codex exec -m gpt-6-luna`（max）去合法开放来源下载，再作为附件上传给 gpt3。

流程照 musicclaude 的《迭代准则》改写：先跑 One-shot 基线 B0，系统版本必须在同样的评审下赢过 B0 才算有价值。

## 先读

1. `STATUS.md` — 现在在哪、下一步
2. `总任务书.md` — 目的和授权边界
3. `标准.md` — 成果要做到什么（只有用户能改）
4. `迭代准则.md` — 怎么一步步改（八步 + 先验证原因 + 流程自己改自己）
5. `主线.md` — 现行流水线

## 常用命令（在 `D:\fwlaozong` 下）

```bash
python tools/run.py check
```

```bash
python tools/run.py oneshot --tag B0
```

```bash
python tools/run.py system --tag S1
```

```bash
python tools/run.py refcheck --tag B0_gpt3
```

```bash
python tools/run.py review --tag S1
```

```bash
python tools/run.py blind --a B0_gpt3 --b S1
```

```bash
python tools/run.py stats
```

换研究问题：在 `questions/` 下放一个新的 `Q2.md`，所有命令加 `--q Q2`。

## 目录

| 路径 | 内容 |
|---|---|
| `tools/llm.py` | gpt3/gpt4 调用：按编号缓存、两账号分流和失败换号、异常活动冷却 50 分钟、每账号间隔 7 秒、`runs/calls.jsonl` |
| `tools/lit.py` | Europe PMC / PubMed 检索、按 PMID/DOI 查文献、开放全文 XML 转文本 |
| `tools/fetch.py` | 全文获取：本地优先，luna 兜底（每批一次） |
| `tools/kb.py` | 分层知识库 `kb/kb.sqlite3` |
| `tools/run.py` | 全部流程入口 |
| `prompts/` | 各步提示词（不含具体研究问题的内容，问题从 `questions/` 读） |
| `questions/` | 研究问题 |
| `out/<版本>/` | 每一版成果和测量 |
| `papers/` | 下载的全文（不可信数据，只上传不执行） |
| `runs/` | 每次模型调用的输入、输出、失败记录 |
| `spec/` | 同学的 AROS 方案原文（只在本地，不入库），只作候选设计参考 |

## 依赖

- `gpt3` / `gpt4`：`D:\musicclaude\gpt2agent-safechain\bin\`（`gpt3 help` 看完整说明）。musicclaude 同时在用同一账号。
- `codex`（npm 全局），模型 `gpt-6-luna`。
- Python 3.12；流水线只用标准库，工作台需要 streamlit、pandas。

## 研究者工作台

```bash
streamlit run tools/workbench.py
```

文献、证据矩阵（原文双栏对照）、结论与假说的人工确认/驳回、评估结果、导出。只有这里的人工操作能把记录设成 verified。

## 三组对照

A = `B0`（One-shot），B = `B1`（同提示词 + 系统检索到的同一批材料作附件：`python tools/run.py material --tag B1 --src S1`），C = 系统版本。留出验收题 `questions/Q2.md` 只在收敛前跑一次。
