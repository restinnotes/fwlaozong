# 丘脑底核神经活动与帕金森病冻结步态（FOG）：证据比较、冲突分析与竞争性机制研究

**研究类型：** 功能神经外科与人类神经电生理的系统性叙述综述、证据综合及机制假说构建
**研究重点：** Subthalamic nucleus（STN）、deep brain stimulation（DBS）、Parkinson's disease（PD）、freezing of gait（FOG）
**证据范围：** 人体 STN 单神经元记录、局部场电位（LFP）、皮层—基底节网络、DBS 干预、步态诱发实验、影像学及计算机制研究。

## 第一轮：研究框架、核心争议与证据检索

### 1. 研究问题的操作化

本研究不把“STN 活动是否与 FOG 有关”当作单一问题，而是拆解为五个可以分别检验的问题：

1. **活动水平问题：** FOG 是否伴随 STN 神经活动整体增强或减弱？
2. **频谱问题：** FOG 是否具有特异性的 beta（13–30 Hz）、低频 theta（约 4–8 Hz）或其他频段异常？
3. **时间动力学问题：** FOG 是否由神经振荡的瞬时爆发、持续时间、相位转换或跨频耦合异常所预测？
4. **空间与网络问题：** FOG 是否与 STN 不同亚区、不同方向的电极触点，以及 STN—皮层—脑干网络之间的异常活动有关？
5. **因果干预问题：** 改变 STN 活动能否改善或诱发 FOG？这种效果是否依赖刺激频率、刺激位置、药物状态和运动任务？

这些问题必须分开处理。某个频段在 FOG 期间增强，并不自动证明它导致 FOG；某种 DBS 可以改善步态，也不意味着该 DBS 恰好通过抑制 FOG 相关频段发挥作用。

### 2. 核心分析原则

本研究将采用以下证据层级：

| 层级 | 证据类型 | 可以支持的结论 |
|---|---|---|
| L1 | FOG 发生前、发生中、结束后的神经信号比较 | 时间关联及预测关系 |
| L2 | FOG 患者与非 FOG 患者比较 | 群体差异及易感性 |
| L3 | 刺激、药物、任务等干预 | 对神经活动与 FOG 因果关系的约束 |
| L4 | 单神经元、LFP、皮层—基底节同步等多尺度证据 | 神经编码及网络机制 |
| L5 | 计算模型、理论框架及跨研究综合 | 机制解释与可检验预测 |

特别注意：L1–L4 的实验结果也需要结合实验设计判断因果强度。L5 的机制合理性不能替代人体实验验证。

本研究还将区分三种不同的 FOG：

- **OFF-FOG：** 多巴胺能药物不足时出现或加重的冻结。
- **ON-FOG：** 药物开启后仍存在的冻结。
- **ON-state / levodopa-induced FOG：** 药物状态下新出现或明显加重的冻结。

如果不区分这几种状态，同一个神经指标可能在不同研究中呈现相反结果，却被误认为实验互相矛盾。

---

### 3. 第一批核心原始研究：已经确认的证据

以下是第一轮检索中最值得优先阅读的原始研究。这里特别区分了“实际发生 FOG 时的信号”和“FOG 易感状态下的信号”。

#### 3.1 Syrkin-Nikolau 等：自由行走中的 STN 神经熵与 FOG

**文献 [R1]**

Syrkin-Nikolau J, et al. *Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease.* Neurobiology of Disease, 2017.

DOI: 10.1016/j.nbd.2017.09.002
PMID: 28890315

**研究设计：**

- 14 名 PD 患者，其中 8 名为 Freezers。
- OFF medication、OFF DBS。
- 使用植入式 Activa PC+S 同步记录 STN LFP、下肢运动学及地面反作用力。
- 任务包括直线行走、原地踏步、转弯及障碍物行走。
- 转弯和障碍物任务比普通直线行走更容易诱发 FOG。

**主要结果：**

1. Freezers 在尚未发生 FOG 的行走阶段，STN beta（13–30 Hz）功率反而低于 Non-Freezers。
2. 同一阶段 Freezers 的 beta Sample Entropy 更高。
3. 实际发生 FOG 时，alpha（8–12 Hz）Sample Entropy 高于未冻结行走阶段。
4. 静息状态下没有发现相应的 alpha/beta 功率或熵差异。

**研究意义：**

这项研究对简单的“FOG 就是 STN beta 过度增强”模型构成重要限制。

它提示：

- Freezer 的异常可能表现为 beta 活动的时间结构失稳，而非持续增强。
- FOG 易感性和实际 FOG 发作可能具有不同的电生理特征。
- 只比较平均功率可能遗漏与 FOG 有关的重要动力学信息。

但样本量较小，且研究结果不能直接证明 entropy 增高是冻结的原因。[R1] <Cite refs={["turn742833view1"]}/>

#### 3.2 Chen 等：低 beta 和 theta 与 FOG 易感性相关

**文献 [R2]**

Chen CC, et al. *Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease.* Neurobiology of Disease, 2019.

DOI: 10.1016/j.nbd.2019.104605
PMID: 31494286

**研究设计：**

- STN LFP 记录。
- 比较单任务行走和双任务行走。
- 使用躯干加速度计算 FOG index（iFOG）。
- 研究对象为接受 STN DBS 的 PD 患者。

**主要结果：**

FOG 易感程度增加时：

- 低 beta（15–21 Hz）功率增加。
- theta（5–8 Hz）功率增加。
- 低 beta 增高呈 STN 区域较广泛的分布。
- theta 增高主要局限于腹侧 STN 和/或 SNr 区域，在单任务条件下尤其明显。

**非常重要的限制：**

研究中的 iFOG 是易感性指标，不等于实际发生的 FOG。

只有少数患者在实验行走任务中出现了明确的冻结。因此，不能把这项研究表述为“实际冻结时 STN theta 和 beta 必然升高”。

作者也明确指出，研究没有证明 theta 或低 beta 对 FOG 具有因果作用。[R2] <Cite refs={["turn960086search5","turn263888search8"]}/>

#### 3.3 Georgiades 等：冻结发生前后的 STN 多单位活动

**文献 [R3]**

Georgiades MJ, et al. *Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing.* Brain, 2019.

DOI: 10.1093/brain/awz325
PMID: 31665229

**研究设计：**

- 8 名接受 STN DBS 手术的 PD 患者。
- 手术期间使用微电极记录 STN 多单位活动。
- 利用经过验证的虚拟现实步态任务诱发冻结。
- 同步分析下肢肌电和 STN 神经活动。

**主要结果：**

实际冻结发生时，观察到：

1. STN 病理性多单位活动瞬时增加。
2. beta 和 theta 振荡增加。
3. STN 活动变化与随后出现的异常下肢肌电活动形成时间序列关联。

**研究意义：**

与 [R2] 不同，这项研究直接观察到了冻结事件，而不是仅仅测量易感性。

它支持一种可能的解释：STN 神经活动异常可能在冻结发生过程中参与运动输出受阻。

不过，手术中的虚拟现实步态不等于自然环境下的自由行走，微电极多单位活动也不能与慢性植入电极测得的 LFP 直接等同。[R3] <Cite refs={["turn960086search1"]}/>

#### 3.4 Gulberti 等：STN 与 SN 神经元在步态控制中的不同作用

**文献 [R4]**

Gulberti A, et al. *Subthalamic and nigral neurons are differentially modulated during parkinsonian gait.* Brain, 2023.

DOI: 10.1093/brain/awad006
PMID: 36730026

**研究设计：**

- 12 名 PD 患者。
- DBS 手术期间进行 STN 和 SN 神经元微电极记录。
- 采用仰卧位模拟踏步任务。
- 分析神经元放电频率、放电模式及振荡活动。

**主要结果：**

- 约 24% 的 STN 神经元表现出运动相关放电率增加。
- 约 8% 的 STN 神经元响应注意性提示。
- 响应的 SN 神经元则主要表现为注意性任务相关活动。
- 踏步过程中，STN 神经元放电模式趋于规则化，beta 振荡下降。
- 冻结期间，beta 振荡增加。

**研究意义：**

这项研究支持 STN 在运动执行和步态控制中的作用，也提示 SN 可能更多参与步态任务中的注意性调节。

尤其值得关注的是，正常踏步时 beta 下降、冻结时 beta 上升。这为“正常运动抑制 beta—冻结时 beta 异常反弹”的动态机制提供了支持。

但该研究的仰卧模拟踏步并非正常负重行走，冻结事件的生态效度有限。[R4] <Cite refs={["turn960086search0"]}/>

#### 3.5 Liu 等：同步记录皮层与 STN 电活动

**文献 [R5]**

*Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait.* Frontiers in Neuroscience, 2022.

DOI: 10.3389/fnins.2022.795417
PMID: 35310098

**研究设计：**

- 8 名 PD 患者。
- 同步记录皮层 ECoG、STN LFP 和步态运动学。
- 进行 Timed Up and Go 等步态任务。
- 共完成 41 次行走测试，其中 30 次出现冻结。

**主要结果：**

- 冻结期间 STN beta 功率显著高于非冻结期间。
- 皮层 ECoG 各频段整体功率差异不显著。
- 冻结期间皮层 ECoG 与 STN LFP 在高 beta 和 gamma 频段表现出较高的相干性。
- STN LFP 频段特征对冻结与非冻结阶段具有高于随机水平的分类能力。

**研究意义：**

这项研究的重要价值在于：FOG 可能不只是 STN 局部振荡幅度变化，还涉及皮层—STN 的功能耦合。

但需要注意，ECoG—STN 相干性不能证明皮层向 STN 的因果驱动，也不能排除共同输入或运动伪迹等因素。[R5] <Cite refs={["turn263888search2","turn263888search12"]}/>

#### 3.6 Collomb-Clerc 等：2025 年 STN 空间定位与步态启动

**文献 [R6]**

Collomb-Clerc A, et al. *Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease.* Annals of Neurology, 2025.

DOI: 10.1002/ana.70003
PMID: 40709562

**研究设计：**

- 38 名 PD 患者，其中 35 名报告日常生活中存在 FOG。
- 24 名年龄匹配健康对照。
- OFF 和 ON 多巴胺状态下记录 STN LFP。
- 分析步态启动（gait initiation）与冻结的关系。
- 比较 posterior sensorimotor STN 和 central associative STN。

**主要结果：**

OFF medication 时：

- 12 名患者在实验中实际出现 FOG，共记录 263 次冻结。
- 冻结平均发生于步态启动后的约第 8 步。
- FOG 患者即使在未发生冻结的步态启动阶段，也表现出不同的步态及 STN 活动关系。
- 接近冻结发生时，低 beta 与步态启动参数之间的正常关联受到破坏。
- 同时出现高 beta 与步态参数之间的新关联，且空间分布发生变化。
- 多巴胺治疗改善步态启动和 FOG，并部分恢复 STN 活动模式。

**研究意义：**

这是目前检索到的、具有较大样本量且特别重视 STN 解剖功能分区的研究。

它提示：FOG 可能涉及步态启动控制从一种 STN 功能组织模式向另一种模式的转变，而不只是某个频段功率的简单增加。

它还提供了一个重要研究方向：将步态的 pace、rhythm、balance 分别与不同 STN 亚区关联，而不是将整个 STN 视为同质结构。[R6] <Cite refs={["turn742833view4"]}/>

#### 3.7 Fim Neto 等：alpha 与高 beta 的间歇性活动

**文献 [R7]**

Fim Neto A, et al. *Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease.* Clinical Neurophysiology, 2025.

DOI: 10.1016/j.clinph.2025.01.005
PMID: 39884164

**研究设计：**

- 23 名 PD 患者。
- 14 名 FOG 患者、9 名 Non-FOG 患者。
- 静息状态下分析 STN LFP。
- 同时分析频谱功率与间歇性振荡（burst）特征。

**主要结果：**

- FOG 组 alpha 功率较高。
- alpha burst 振幅较高。
- alpha 间歇性活动与 FOG 严重程度相关。
- 高 beta burst 振幅与 FOG 评分相关，并与 POMA 步行表现指标呈负相关。

**研究意义：**

它说明静息状态下的 FOG 特征可能不仅限于经典 beta 频段。

但这是横断面静息态研究，不能说明这些 burst 在冻结发生前是否出现，也不能直接将其解释为冻结的瞬时机制。[R7] <Cite refs={["turn960086search2","turn960086search3"]}/>

---

### 4. 第一轮发现的核心矛盾

目前最重要的矛盾并不是简单的“某研究发现 beta 增加，另一研究发现 beta 降低”，而是不同实验实际测量了不同的神经状态。

| 研究 | 测量状态 | beta 结果 | 主要含义 |
|---|---|---|---|
| [R1] | Freezer 未冻结时行走 | 低于 Non-Freezer | 易感状态不等于 beta 持续升高 |
| [R2] | 高 FOG 易感步态 | 低 beta 增高 | 易感性可能伴随异常低 beta |
| [R3] | 实际冻结发生过程 | beta、theta 增高 | 发作时可能出现瞬时异常同步 |
| [R4] | 模拟踏步与冻结 | 正常踏步时下降，冻结时增加 | beta 可能与动作状态转换有关 |
| [R5] | 实际冻结与非冻结 | STN beta 增高 | 支持冻结期 beta 增强 |
| [R6] | 步态启动及即将发生的冻结 | 低 beta 关系破坏，高 beta 关系出现 | 频谱与 STN 空间组织均可能发生变化 |
| [R7] | 静息状态 | alpha、高 beta burst 与临床严重程度相关 | 慢性易感性可能有不同于发作期的标记 |

目前可以提出一个初步综合判断：

**FOG 不能被可靠地简化为 STN beta 功率升高。更值得研究的是 STN 活动如何随运动阶段、冻结易感性、实际冻结和运动恢复发生动态变化。**

这是一项跨研究综合结论，而不是已经得到实验验证的统一机制。

### 5. 第一轮暂定结论与下一轮检索重点

目前形成四个值得保留的判断：

1. **状态依赖性：** FOG 易感期、实际冻结期和恢复期可能具有不同的 STN 电生理特征。
2. **时间结构的重要性：** burst、entropy、瞬时同步及跨频耦合可能比整段平均功率更有解释力。
3. **空间异质性：** 腹侧 STN、背侧 STN、运动相关区与联合区不能简单合并。
4. **网络依赖性：** STN 可能是 FOG 网络异常的参与者、放大器或下游读出节点，目前尚不能确定其因果地位。

下一轮将重点研究：

- STN-DBS 的 60 Hz、130 Hz、低频和高频刺激对 FOG 的不同影响。
- DBS 诱发 FOG 与 DBS 改善 FOG 的相反结果。
- STN 与 PPN、SNr、SMA、M1、前额叶和小脑之间的联系。
- 药物反应性与药物抵抗性 FOG。
- beta burst、theta、alpha、gamma 和跨频耦合的机制差异。
- 现有 FOG 理论模型能否解释这些相互冲突的结果。

【继续】

=====（下一轮）=====

# 第二轮：STN-DBS 的因果干预证据、网络定位与机制冲突

**研究进度：** 已完成第一轮 STN 电生理研究的初步梳理。本轮扩展至 DBS 刺激频率、刺激位点、皮层—STN 耦合、STN—SNr 通路及自适应 DBS，并纳入 2026 年新发表的原始研究。

## 6. 一个必须新增的核心发现：FOG 不一定伴随 STN 局部 beta 增强

第一轮重点介绍了多个发现冻结期间 STN beta 或 theta 增强的研究。但继续检索发现，2019 年的一项重要研究提供了与这一模式明显不同的结果。

### 6.1 [R8] Pozzi 等，2019：局部功率不变，但皮层—STN 耦合异常

**原始文献**

Pozzi NG, et al. *Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics.* Brain, 2019;142:2037–2050.

- PMID: **31505548**
- DOI: **10.1093/brain/awz141**
- <Link url="https://pmc.ncbi.nlm.nih.gov/articles/PMC6598629/" title="阅读原文"/>

**研究方法**

研究结合了自然行走环境中的多部位神经电生理记录、步态运动学，以及反映纹状体多巴胺能神经支配的分子影像学。

研究者特别比较：

- 正常行走与实际 FOG。
- 成功通过门口与通过门口时发生的 FOG。
- FOG 与主动停止行走。
- 两侧纹状体多巴胺能支配程度不同的半球。

**关键结果**

1. 冻结时 STN 局部 theta-alpha（4–13 Hz）功率没有一致性显著变化。
2. STN beta 功率没有显著变化。
3. beta burst 持续时间也没有显著变化。
4. 然而，皮层—STN 在 4–13 Hz 的耦合在冻结期间明显降低。
5. 这种解耦主要发生在纹状体多巴胺能支配较少的一侧。
6. 解耦在冻结发生前已经出现，冻结期间持续，恢复行走后消失。
7. 与主动停止相比，低频解耦对 FOG 更有特异性。

另一个关键细节：研究也观察到冻结启动时皮层—STN beta 耦合增加，但类似变化同样可见于正常通过门口或主动停止。因此，**beta 耦合增强不一定是 FOG 特异性事件**。[R8] <Cite refs={["turn945834search7","turn945834search1","turn843871search8"]}/>

**证据评价**

这项研究与第一轮的 [R3]、[R4]、[R5] 形成了直接且重要的实验结果差异。

它支持一种不同的解释：

> STN 局部振荡的平均强度可能不是 FOG 的必要条件；皮层与 STN 在运动转换期间能否维持适当的信息耦合，可能更加重要。

但这仍属于机制推断。相干性降低不等于有效信息传递必然降低，也不能确定是皮层输入异常、STN 输出异常还是共同网络状态改变。

**证据等级：** 直接人体电生理证据；对“局部 beta 功率是 FOG 必要标志物”的假说构成重要反例。

---

## 7. STN-DBS 频率效应：为什么 60 Hz 有时改善 FOG，有时无效？

### 7.1 核心原始干预研究

| 编号及研究 | 设计与人群 | 主要发现 | 证据限制 |
|---|---|---|---|
| [R9] Moreau，2008 | 13 名严重步态障碍患者；盲法比较 60/130 Hz 与刺激关闭 | 等能量的 60 Hz、高电压条件下冻结次数较少；130 Hz 高电压可能加重冻结 | 频率与电压、能量共同变化 |
| [R10] Xie，2012 | 2 名新启动 STN-DBS 即出现 FOG 的患者 | 保持触点、电压、脉宽不变，130→60 Hz 后冻结立即缓解 | 病例数极少，但短时间内频率切换提供了重要因果线索 |
| [R11] Phibbs，2014 | 20 名术后报告步态变化的患者；随机盲法交叉比较 | 60 Hz 与 130 Hz 在主要步幅终点上无显著差异；60 Hz 震颤控制较差 | 不是专门筛选 130 Hz 下仍有严重 FOG 的人群；电压不变导致能量变化 |
| [R12] Khoo，2014 | 随机双盲交叉试验 | 优化触点后的 60 Hz 改善总体运动及轴性症状；最佳低频触点更腹侧 | 同时优化频率和触点，无法隔离纯频率效应 |
| [R13] Xie，2015 | 7 名在 130 Hz 和药物治疗下仍有 FOG 的患者；随机双盲交叉 | 60 Hz 改善 FOG、吞咽及轴性症状，短期随访仍有获益 | 小样本；吞咽是主要终点，FOG 为次要终点 |
| [R14] Xie 等，2018 | 11 名患者初始入组，10 名完成长期随访 | 60 Hz 相对 130 Hz 的 FOG 获益可延续至平均约 14.5 个月，但总体效应有所减弱 | 小样本及特定患者选择，不能推广至全部 STN-DBS 患者 |

原始文献：

- **[R9]** Moreau C, et al. *STN-DBS frequency effects on freezing of gait in advanced Parkinson disease.* Neurology, 2008. PMID: 18420482; DOI: 10.1212/01.wnl.0000303972.16279.46.
- **[R10]** Xie T, Kang UJ, Warnke P. *Effect of stimulation frequency on immediate freezing of gait in newly activated STN DBS in Parkinson's disease.* J Neurol Neurosurg Psychiatry, 2012. PMID: 22696586; DOI: 10.1136/jnnp-2011-302091.
- **[R11]** Phibbs FT, et al. *60 Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation.* Neuromodulation, 2014. PMID: 24165197.
- **[R12]** Khoo HM, et al. *Low-frequency subthalamic nucleus stimulation in Parkinson's disease: a randomized clinical trial.* 2014. PMID: 24449169.
- **[R13]** Xie T, et al. *Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD.* Neurology, 2015. PMID: 25540305; DOI: 10.1212/WNL.0000000000001184.
- **[R14]** *Long-term effect of low frequency stimulation of STN on dysphagia, freezing of gait and other motor symptoms in PD.* 2018. PMID: 29654112.

以上结论可追溯至各研究原始报告。[R9–R14] <Cite refs={["turn911542search4","turn253421search2","turn911542search1","turn911542search5","turn911542search3","turn911542search9"]}/>

### 7.2 频率研究的核心因果问题

常见叙述是：

“60 Hz 改善 FOG，130 Hz 加重 FOG，因此高频刺激可能导致 FOG。”

这个推论过于简单。

至少存在四个相互竞争的解释。

**解释 A：频率本身存在特异性作用。**

低频与高频对基底节—脑干环路的调制模式不同，因此某些 FOG 对 60 Hz 有更好的反应。

这与 [R10] 中保持其他参数不变、仅切换频率即可迅速改变 FOG 的病例观察相符。

**解释 B：刺激能量和组织募集不同。**

频率改变时，即使电压、电流和脉宽不变，单位时间脉冲数也改变。相同电压下的 60 Hz 和 130 Hz 不是完全等剂量的干预。

因此，部分改善可能来自减少不利神经组织的募集或降低总刺激负荷，而不是 60 Hz 具有特殊生理作用。

但“总电能相同”也不能保证两种频率募集完全相同的神经纤维，更不能保证网络效应相同。

**解释 C：FOG 亚型决定刺激反应。**

研究 [R13] 特意选入在常规 130 Hz 下仍存在 FOG 的患者，而 [R11] 纳入的是一般术后步态变化患者。

如果低频主要帮助“高频刺激下持续存在或加重的 FOG”，这两个研究的结果就不一定真正冲突。

**解释 D：有效触点不同。**

[R12] 发现不同频率的最佳刺激触点并不重合。

这意味着可能不存在脱离刺激空间位置的统一最优频率。

### 7.3 本节综合判断

目前可以有条件地支持：

**60 Hz STN-DBS 对一部分存在顽固性 FOG、尤其在常规高频刺激下仍有轴性症状的患者有效。**

但不能支持：

“60 Hz 对所有 FOG 均优于 130 Hz。”

也不能把低频获益直接解释为“STN 的病理性 beta 被特异性抑制”，因为这些临床频率研究通常没有同步测量足以证实该机制的神经电生理指标。

这一区分对功能神经外科尤为重要：**治疗效果是干预证据，尚不是对某个神经振荡机制的直接验证。**

---

## 8. STN—SNr 通路：DBS 能否通过调节基底节输出改善 FOG？

STN 与黑质网状部（substantia nigra pars reticulata，SNr）之间的联系，为解释 DBS 的双向步态效应提供了重要方向。

SNr 是基底节的主要输出核团之一，其输出可影响中脑步行区（mesencephalic locomotor region，MLR）及相关脑干运动控制系统。

因此，可以提出一个假说：

**部分 FOG 的近端病理环节不是 STN 振荡本身，而是 STN 对 SNr—脑干步态控制系统的异常影响。**

如果这一假说成立，单纯优化 STN 刺激可能不如同时调节 STN 与 SNr 有效。

但最新干预研究并没有一致支持这一预测。

### 8.1 关键原始研究

**[R15] Weiss 等，2013：早期随机试验**

*Nigral stimulation for resistant axial motor impairment in Parkinson's disease? A randomized controlled trial.*

- Brain, 2013
- PMID: 23757762
- DOI: 10.1093/brain/awt122

12 名 PD 患者进入双盲、随机交叉试验。研究比较常规 STN-DBS 与 STN+SNr 联合刺激。

结果：

- 主要终点（综合轴性 UPDRS 评分）没有显著组间差异，P=0.470。
- 次要终点 FOG Assessment Course（FOG-AC）显示联合刺激可能改善冻结，P=0.0468。
- 平衡指标并未出现相应的明确改善。

因此，这是一项**主要终点阴性、FOG 次要终点阳性**的研究，不能被概括为联合刺激已经证明有效。[R15] <Cite refs={["turn868952search0","turn868952search12"]}/>

**[R16] Artusi 等，2025：不同 SNr 频率的随机交叉研究**

*Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial.*

- Journal of Parkinson's Disease
- PMID: 39957196
- DOI: 10.1177/1877718X241292315

15 名接受至少一种联合刺激的患者，比较：

- 常规高频 STN-DBS。
- 高频 STN + 高频 SNr。
- 高频 STN + 低频 SNr。

每种刺激模式维持一个月。

**主要终点 NFOG-Q 没有显著改善。**

但约三分之一患者在联合刺激下达到预设的临床重要改善幅度，80% 患者在保持盲法的条件下偏好联合刺激。

这提示可能存在获益亚群，但总体结果不足以证明联合刺激优于优化后的单纯 STN-DBS。[R16] <Cite refs={["turn325509search0","turn325509search1"]}/>

**[R17] Tan 等，2025：报告联合刺激优于 STN**

*DBS-STN&SNr combined stimulation versus DBS-STN monotarget stimulation for Parkinson's disease freezing: A comparative efficacy study.*

- Journal of Parkinson's Disease, 2025
- PMID: 40760816
- DOI: 10.1177/1877718X251359241

多中心随机交叉研究，24 名患者入组，20 名完成全部随访。研究分别采用 STN 单靶点和 STN+SNr 双靶点模式，每阶段持续六个月。

作者报告联合刺激在 FOG-Q 和生活质量评分方面优于单纯 STN 刺激。

这提供了一个阳性结果，但本轮文献质量核查发现该报告存在值得进一步核对的引用和量表呈现问题，因此现阶段不将其作为“联合刺激已经确立疗效”的决定性证据。[R17] <Cite refs={["turn176681search0","turn341412view4"]}/>

**[R18] Weiss 等，2026：多中心随机双盲试验**

*Disease Duration Differentiates Freezing of Gait Response to Subthalamic and Nigral Stimulation for Parkinson's Disease in an Exploratory Multicenter Controlled Trial.*

- Movement Disorders Clinical Practice
- 2026 年 10 月 12 日首次发表
- PMID: 42860886
- DOI: 10.1002/mdc3.70813

这是本轮发现的最重要的新临床证据之一。

研究涉及多个 DBS 中心，45 名患者进入改良意向治疗分析：

- STN 组：23 人。
- STN+SNr 组：22 人。
- 双盲观察 90 天。
- 主要终点为 FOG-AC。

主要终点：

<box gap={1}>
  <text color="secondary" weight="medium" size="xs">90 天时两组 FOG-AC 评分差异</text>
  <title size="xl" color="default" tabularNums>−1.16 分</title>
  <text color="secondary" size="sm">95% CI：−7.03 至 4.71；P=0.692</text>
</box>

即：**没有观察到联合 STN+SNr 刺激在整体患者中优于优化 STN-DBS 的证据。**

研究还发现：

- STN 组有 7 名患者达到临床有意义的改善。
- STN+SNr 组有 8 名患者达到临床有意义的改善。
- 联合刺激应答者的病程平均约 12 年，比非应答者短约 4.5 年。
- 应答似乎是逐渐形成的，并不一定表现为刺激改变后的立即改善。

但病程与疗效的关系属于探索性亚组分析，尚不能作为已经验证的临床分层规则。该研究还受到既往植入电极位置及样本选择的限制。

特别需要注意：研究者没有专门为 SNr 重新设计电极植入，而是从既有 STN-DBS 患者中选择尾端触点可能覆盖 SNr 的病例。因此，“联合刺激无显著获益”并不等于“精准 SNr 刺激一定无效”。[R18] <Cite refs={["turn945834search0","turn545609view5"]}/>

### 8.2 STN+SNr 证据的阶段性综合

| 研究 | 主要 FOG 结论 | 解释 |
|---|---|---|
| [R15] 2013 | 次要 FOG 终点阳性 | 提供初步机制线索 |
| [R16] 2025 | 主要终点阴性，部分患者获益 | 存在可能的应答亚群 |
| [R17] 2025 | 报告联合刺激优于 STN | 阳性结果，需要结合方法和报告质量评价 |
| [R18] 2026 | 主要终点阴性 | 对普遍有效的联合刺激模型构成限制 |

综合而言：

- **有支持：** SNr 相关通路能够影响某些患者的冻结表现。
- **仍有争议：** STN+SNr 是否具有可重复的群体平均获益。
- **尚无直接证明：** 这种潜在获益是否通过修正 STN 的 theta、beta 或 beta burst 实现。
- **值得检验：** 病程、药物反应性、脑干通路完整性与 SNr 刺激响应之间是否存在交互作用。

---

## 9. 刺激空间位置与纤维连接：STN 并非单一功能靶点

电生理研究中的 STN 分区与 DBS 临床研究中的最优刺激区域之间存在一个重要区别：

**记录位置回答“哪里出现了与 FOG 相关的信号”；刺激位置回答“激活哪里的组织及纤维可以改变 FOG”。两者不能直接等同。**

### 9.1 [R19] Strelow 等，2022：刺激的结构连接预测 FOG 改善

*Structural Connectivity of Subthalamic Nucleus Stimulation for Improving Freezing of Gait.*

- Journal of Parkinson's Disease, 2022
- PMID: 35431262
- DOI: 10.3233/JPD-212997

47 名术前存在 FOG 的患者，研究使用个体刺激场建模、基底节通路模型及规范性连接组分析，其中 18 人进行标准化步行诱发评估。

结果：

- FOG 在术后六个月总体改善。
- 有利刺激位置与运动皮层、前额叶及苍白球的结构连接相关。
- 刺激豆状束（lenticular fasciculus）与 FOG 加重相关。
- 与 PPN、黑质相关区域相连的纤维募集与改善相关。

**关键限制：** 规范性 tractography 所预测的连接不是患者本人被 DBS 实际激活的轴突，更不是这些轴突的生理传导方向或具体神经递质作用。[R19] <Cite refs={["turn514611search5","turn176681search2"]}/>

### 9.2 [R20] Temiz 等，2022：前额叶连接可能与 FOG 加重有关

*Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients.*

- Parkinsonism & Related Disorders, 2022
- PMID: 36242900
- DOI: 10.1016/j.parkreldis.2022.10.002

19 名患者进行了术前与术后临床和步态评估，并结合个体刺激场与皮层—STN 纤维连接分析。

结果：

- 不同患者的 FOG 结局高度异质。
- 右侧刺激场与前额叶皮层连接越强，术后 FOG 越严重。
- 右侧刺激场与感觉运动皮层连接越强，FOG 越轻。

这是支持“感觉运动与联合功能网络募集之间存在不同治疗效果”的人体证据。

但它无法说明右侧半球具有绝对优势，也不能证明前额叶—STN 连接本身具有致病性。[R20] <Cite refs={["turn176681search1"]}/>

### 9.3 [R21] Fan 等，2023：FOG 的刺激 sweet spot 和 sour spot

*Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease.*

- Brain Communications, 2023
- PMID: 37701817
- DOI: 10.1093/braincomms/fcad238

研究回顾了 76 名接受双侧高频 STN-DBS、术前存在 FOG 的 PD 患者。

术后：

<grid columns={3} gap={2}>
  <grid-item>
    <box border radius="lg" padding={2} align="center" gap={1}>
      <title size="xl" color="success" tabularNums>42</title>
      <caption>FOG 改善</caption>
    </box>
  </grid-item>
  <grid-item>
    <box border radius="lg" padding={2} align="center" gap={1}>
      <title size="xl" tabularNums>22</title>
      <caption>变化较小</caption>
    </box>
  </grid-item>
  <grid-item>
    <box border radius="lg" padding={2} align="center" gap={1}>
      <title size="xl" color="danger" tabularNums>12</title>
      <caption>FOG 加重</caption>
    </box>
  </grid-item>
</grid>

主要定位结果：

- 最优刺激区域主要位于 STN 背外侧约三分之二区域。
- 右侧腹侧中央 STN 及左侧中央 STN 周围部分内囊区域，与较差结局相关。
- 与 SMA、pre-SMA、PPN 相关的纤维连接更有利于 FOG 改善。
- 与部分内侧和腹外侧前额叶皮层相关的连接，与较差结局相关。

研究使用留一交叉验证，但结构连接预测与临床结局的相关程度有限，不能把这些区域视为已被前瞻性确认的绝对治疗靶点。[R21] <Cite refs={["turn392186search2","turn514611search12"]}/>

### 9.4 [R22] Cherif 等，2025：随机试验支持中央 STN 定向刺激

*Directional Subthalamic Deep Brain Stimulation Better Improves Gait and Balance Disorders in Parkinson's Disease Patients: A Randomized Controlled Study.*

- Annals of Neurology, 2025
- PMID: 39475137
- DOI: 10.1002/ana.27099

10 名术前存在明显 FOG 的患者接受随机双盲交叉比较，使用方向性电极测试：

- Central STN directional DBS。
- Posterior sensorimotor STN directional DBS。
- Ring-mode DBS。

患者在 OFF 多巴胺状态下完成测试，刺激模式之间设有洗脱期，并使用客观步态与姿势指标。

结果：

- 中央 STN 刺激比后部 STN 刺激更有效地改善步态与平衡指标，P=0.027。
- 中央刺激期间冻结发作更少，P<escape><</escape>0.001。
- Ring-mode 相比中央定向刺激，姿势控制较差，P=0.009。

**这一研究具有重要意义：它不只是回顾性空间相关分析，而是通过随机改变刺激方向，观察到相应的步态变化。**

但样本仅 10 人，且刺激模式变化同时改变了多个纤维系统的募集，尚不能指定是哪一束纤维直接产生疗效。[R22] <Cite refs={["turn694355view1","turn780699view1"]}/>

### 9.5 [R23] Nickl 等，2025：更腹侧的刺激触点与步态恶化有关

*Probabilistic mapping of gait changes after STN-DBS for Parkinson's disease.*

- Parkinsonism & Related Disorders, 2025
- PMID: 40408848
- DOI: 10.1016/j.parkreldis.2025.107871

98 名患者的概率刺激场分析发现：

- 42 名患者术后步态问题改善。
- 7 名患者在术后一年出现步态恶化。
- 步态恶化患者的有效刺激触点相对更腹侧。
- 个体预测模型在留一交叉验证中达到 \(R^2=0.45\)。

但其结局主要基于 MDS-UPDRS III 的步态相关条目，并非仅针对客观确认的 FOG。因此，该研究可以支持“步态效应具有空间异质性”，不能单独证明腹侧刺激必然导致冻结。[R23] <Cite refs={["turn392186search5"]}/>

### 9.6 空间定位证据中的真实矛盾

这里有一个比频率争议更深入的问题：

[R19] 报告某些前额叶连接与改善相关；[R20] 和 [R21] 则提示部分前额叶连接与 FOG 恶化相关。[R22] 又显示中央 STN 比后部感觉运动 STN 更有效。

三类结果不应被简单合并为“刺激运动区最好”或“刺激联合区最好”。

主要可能原因是：

1. **前额叶不是一个同质结构。** DLPFC、内侧前额叶、前运动区、pre-SMA 等区域的连接在解剖和功能上不同。
2. **连接指标不同。** 结构纤维数量、规范性连接概率与实际 DBS 激活的纤维并非同一变量。
3. **比较基准不同。** 后部 STN 相比中央 STN、背外侧 STN 相比腹侧 STN，是不同的空间对照。
4. **临床终点不同。** 主观 FOG-Q、客观冻结次数、步态启动、姿势不稳可能涉及不同网络。
5. **研究设计不同。** 回顾性 sweet spot 模型可能受到电极定位、治疗选择与疾病严重程度的混杂；随机方向性刺激提供更强干预约束，但样本较小。

因此，现阶段较稳妥的结论是：

**STN-DBS 对 FOG 的作用显著依赖空间位置及所募集的连接网络，但尚无经过充分前瞻性验证、能够适用于所有 FOG 亚型的单一最佳刺激位点。**

---

## 10. 自适应 DBS：能否用 STN beta burst 作为 FOG 的因果控制信号？

此前的电生理研究提示，平均 beta 功率不能充分解释 FOG，因此一个自然的研究方向是使用 STN beta burst 持续时间驱动自适应 DBS（adaptive DBS，aDBS）。

但是，**某个神经信号能够驱动有效治疗，并不等于该信号就是症状的致病机制。** 这一点可以通过比较基于生物标志物的刺激和不依赖该标志物的刺激来检验。

### 10.1 [R24] Wilkins 等，2025：beta burst 驱动的自适应刺激

*Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.*

- Brain Communications, 2025
- PMID: **40677701**
- DOI: **10.1093/braincomms/fcaf266**
- <Link url="https://pubmed.ncbi.nlm.nih.gov/40677701/" title="PubMed 原始记录"/>

研究纳入 7 名 PD 患者，使用双侧 STN 植入式可记录 DBS 系统。研究者通过实时识别 STN beta burst 的持续时间，调整刺激幅度，并在原地踏步、转弯和障碍物行走中比较以下状态：

- 刺激关闭（OFF）。
- 连续 DBS（cDBS）。
- beta burst 驱动的 aDBS。
- 随机间歇调制 DBS（随机刺激对照）。

主要发现：

1. 7 名患者均实现了实时自适应刺激，研究认为该方案具有可行性及短期耐受性。
2. aDBS 相比刺激关闭改善了冻结及部分运动学指标。
3. 连续 DBS 也改善了相关指标。
4. **aDBS 在主要步态比较中未证明优于连续 DBS。**
5. 基于 beta burst 的调制，也没有在这些比较中显示出明确优于随机间歇调制的冻结改善优势。

这一结果并不否定 beta burst 与运动障碍有关，而是对更强的机制主张提出限制：尚不能说“实时追踪和消除长 beta burst 比其他刺激时序更能特异性解除 FOG”。

研究样本小、刺激模式观察时间有限；它首先是可行性研究，并不是具有充分统计效能的机制证伪试验。[R24] <Cite refs={["turn944056search5","turn944056search7"]}/>

**文献去重发现：** 研究团队于 2024 年发表过同一方向的预印本（PMID: 38978669，DOI: 10.1101/2024.06.26.24309418），与 2025 年正式发表论文具有相同核心作者和七人研究样本。证据库应将其归为同一研究的不同版本，而不是两个独立阳性实验。<Cite refs={["turn362674search0","turn362674search1"]}/>

### 10.2 对 beta 机制的直接启示

可以区分三个命题：

| 命题 | 当前证据判断 |
|---|---|
| STN beta burst 与帕金森运动异常有关 | 有支持 |
| beta burst 可以作为自适应 DBS 的控制输入 | 已证明技术可行 |
| 消除长 beta burst 是改善 FOG 的特异性因果途径 | 尚未证实 |

在下一阶段的试验中，真正有区分力的对照不只是 aDBS 对比刺激关闭，而应包括在刺激总负荷、调制幅度和时间分布上尽可能匹配的随机或错时刺激。

如果只有正确锁定异常 beta burst 的刺激显著优于匹配对照，才更能支持其因果作用。

---

## 11. 2026 年证据：步态周期与多巴胺可能改变对 beta 的解释

### 11.1 [R25] Zhuang 等，2026：以步态周期而不是整段记录为分析单位

*Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease.*

- Neurobiology of Disease, 2026;228:107571
- PMID: **42571859**
- DOI: **10.1016/j.nbd.2026.107571**

研究同步记录 FOG 患者行走时的皮层与 STN LFP，并以每个步态周期作为基本分析单位。

研究设计包含三个部分：比较发生冻结的行走试次与没有冻结的试次；比较高频和低频 STN-DBS；分析左旋多巴治疗前后的皮层—STN 耦合。

主要发现：

- 在最终发生 FOG 的行走试次中，尚未冻结的步态周期已经存在运动学异常。
- 初级躯体感觉皮层（S1）和顶上小叶（SPL）的低 beta 活动存在异常。
- 高频及低频 STN-DBS 均可改善部分步态异常，低频刺激影响的指标范围更广。
- 高频刺激纠正了双支撑阶段 SPL 低 beta 功率异常降低。
- 低频刺激恢复了 S1 在支撑相与摆动相之间的部分相位依赖振荡。
- 左旋多巴能够调节异常 S1—STN theta 相干性，伴随步态改善。

这一结果提出了一个比“平均频谱是否升高”更精确的研究目标：**某一频段的活动是否在正确的步态相位出现。**

同时也对“beta 功率越低越好”提出反例：在特定皮层区域和步态相位，异常的 beta 降低同样可能与冻结易感状态有关。

注意，该研究中 SPL 和 S1 的 beta 结果属于皮层活动，不能直接改写为 STN 局部 beta 的变化。其摘要未提供足以在此确认的样本人数，因此暂不填入未经核实的数字。[R25] <Cite refs={["turn944056search0","turn944056search4"]}/>

### 11.2 [R26] Simpson 等，2026：低 beta 与高 beta 受到运动和多巴胺的相反调制

*Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping.*

- Brain, 2026;149:2409–2421
- PMID: **41388789**
- DOI: **10.1093/brain/awaf464**

研究在 14 名 PD 患者中同步记录 STN LFP 和下肢肌电，比较坐位、站立及原地踏步，并分别测试左旋多巴 ON/OFF 状态。

研究将 beta 分为：

- 低 beta：12–20 Hz。
- 高 beta：21–35 Hz。

观察到的方向性结果非常重要：

| 条件变化 | STN 低 beta | STN 高 beta |
|---|---|---|
| 从坐位/站立转换为踏步 | 增强 | 减弱 |
| 左旋多巴治疗后 | 减弱 | 增强 |

研究还发现，STN 的 beta 活动在步态周期中的变化与对侧腿部肌肉活动相关；左旋多巴能够增强晚期支撑相及抬脚阶段的 beta 抑制。

此外，beta burst 与运动启动时肌肉激活增强相关。

**解释：** 低 beta 与高 beta 可能具有不同功能，不能在研究综合中不加区分地合并为 13–30 Hz 的单一指标。

不过，这项研究主要分析踏步的生理动力学，不能把所有观察到的 beta 调制直接称为“实际 FOG 期间的活动”。其价值主要是为 FOG 机制提供正常和病理踏步的比较基础。[R26] <Cite refs={["turn944056search1","turn944056search3"]}/>

### 11.3 [R27] Wagner 等，2022：不同刺激网络可以产生不同的冻结期皮层图谱

*Combined Subthalamic and Nigral Stimulation Modulates Temporal Gait Coordination and Cortical Gait-Network Activity in Parkinson's Disease.*

- Frontiers in Human Neuroscience, 2022;16:812954
- PMID: **35295883**
- DOI: **10.3389/fnhum.2022.812954**

研究纳入 12 名 PD 患者及 12 名匹配健康对照。患者在正常药物治疗状态下分别接受刺激关闭、STN-DBS、STN+SN 联合刺激，同时完成原地踏步、高密度 EEG 及运动学记录。

12 名 PD 患者中，7 名在实验条件下出现至少一次冻结。

研究发现：

- 联合刺激改善了病情较重一侧的踏步时间变异性。
- 两种刺激模式均可降低部分异常皮层振荡。
- 在单纯 STN-DBS 下，冻结主要伴随中央皮层 alpha/低 beta 增强。
- 在 STN+SN 联合刺激下，冻结伴随更明显的额叶高 beta 增强。

这里的关键发现是：**相似的冻结表型可能发生于不同的网络振荡状态，而同一刺激改变也可能重组冻结时的神经活动分布。**

但 EEG 是皮层测量，不能将其当作 STN 的直接记录；而踏步时间变异性的改善也不等同于患者日常生活中冻结次数必然减少。[R27] <Cite refs={["turn362674search2","turn362674search3"]}/>

---

## 12. 两项 2026 年 Meta 分析得出相反结论：为什么？

在继续检索时，发现两项近期 STN+SNr 联合刺激的 Meta 分析得出了不同判断。这是非常适合用于检验研究综合方法可靠性的案例。

### 12.1 [R28] Kong 等，2026：未证实联合刺激有额外 FOG 获益

*STN-SNr co-stimulation in Parkinson's disease: a systematic review and meta-analysis of motor and freezing-of-gait outcomes.*

- Neurological Sciences，2026 年 10 月 23 日
- PMID: **42909654**
- DOI: **10.1007/s10072-026-09479-2**

该研究截至 2026 年 5 月 1 日检索六个数据库，共纳入 10 项研究、109 名可评价患者，其中 9 项为随机试验。

其 FOG 综合结果为：

<box gap={1}>
  <text color="secondary" size="xs" weight="medium">STN+SNr 相比单纯 STN 的 FOG 效应</text>
  <title size="xl" tabularNums>Hedges' g = −0.23</title>
  <text color="secondary" size="sm">95% CI：−1.04 至 0.59；6 项研究，86 人</text>
  <text color="secondary" size="sm">总体异质性 I² = 85.6%；GRADE：极低确定性</text>
</box>

结论：**没有发现稳定、可确认的额外 FOG 改善效果。**

作者特别区分了“联合刺激优于刺激关闭”和“联合刺激优于优化的单纯 STN-DBS”，并对交叉试验的配对数据结构及同一研究内多个比较的依赖关系进行了处理。

这项分析也不能证明联合刺激无效：置信区间很宽，仍然包含有临床意义的获益及潜在不利效应。[R28] <Cite refs={["turn944056search6","turn533327view2"]}/>

### 12.2 [R29] Haq 等，2026：报告联合刺激具有统计学优势

*Superiority of dual-target STN-SNr deep brain stimulation towards gait in Parkinson's disease: a meta-analysis and meta-regression of randomised trials.*

- BMJ Connections Surgery，2026 年 6 月 15 日
- PMID: **42968793**
- DOI: **10.1136/bmjcsurg-2026-000033**

该研究检索截至 2025 年 10 月，共纳入 8 项随机交叉试验、97 名患者。

报告结果：

<box gap={1}>
  <text color="secondary" size="xs" weight="medium">STN+SNr 相比单纯 STN 的 FOG 效应</text>
  <title size="xl" tabularNums>SMD = −0.39</title>
  <text color="secondary" size="sm">95% CI：−0.73 至 −0.04；I² = 23.2%</text>
</box>

作者据此认为联合刺激具有统计学优势；生活质量未获得相应显著改善。[R29] <Cite refs={["turn944056search2","turn988758search1"]}/>

### 12.3 方法核查：两个结果为什么可能不同？

| 项目 | [R28] Kong | [R29] Haq |
|---|---|---|
| 文献检索截止 | 2026-05-01 | 2025-10 |
| 纳入研究 | 10 项，109 人 | 8 项，97 人 |
| FOG 汇总数据 | 6 项，86 人 | 报告 7 项含 FOG 的研究 |
| 效应量 | Hedges' g −0.23 | SMD −0.39 |
| 置信区间 | 跨越零且较宽 | 略微不跨零 |
| 异质性 | 很高 | 较低 |
| 配对数据处理 | 考虑交叉设计及研究内相关 | 报告采用平行组近似 |
| 结论 | 未证实额外获益 | 报告小至中等改善 |

进一步检查 [R29] 的分析方法和森林图，发现两个必须进入正式证据质量评价的问题。

**第一，交叉试验被当作近似平行组试验分析。**

[R29] 明确说明，由于原始研究未充分报告个体内相关性及配对差值的标准差，其主要汇总分析采用条件均值和标准差进行平行组近似。

这种处理并非在所有情况下都会高估疗效，但会改变方差和权重估计，不能充分利用交叉试验的个体内信息。特别是在患者对刺激反应高度异质的 FOG 研究中，忽略配对信息是一个重要限制。

**第二，同一研究的多个刺激条件分别进入森林图。**

例如，[R29] 的森林图将 Artusi 研究中的两种 SNr 频率以及 Weiss 研究中的三种 SNr 频率分别列为比较，且共同使用同一个 STN 对照条件。

这些比较不是独立样本。如果没有适当调整共享对照组或研究内相关性，合并权重和统计不确定性可能出现偏差。

此外，森林图中的两个较大阴性效应量来自：

- Tan 等 [R17]：SMD 约 −1.23。
- Valldeoriola 等：SMD 约 −1.43。

它们可能对总体阴性效应方向有较大影响。使用发表的森林图权重作简单敏感性检查，在暂时排除这两个比较后，其余比较的加权平均效应量绝对值明显减小。

但这只是用于发现敏感性来源的描述性计算，**不是重新完成的规范 Meta 分析**，不能直接代替重新估计随机效应、相关结构与置信区间。[R29] <Cite refs={["turn988758search0","turn988758search16"]}/>

### 12.4 对两项 Meta 分析的重新评价

这两项分析的冲突并不能通过“选发表更晚的一篇”解决。

更合理的做法是：

1. 回到每项随机试验的原始、配对数据，统一 FOG 终点和药物状态。
2. 对同一患者在多个刺激频率下的数据建立多层模型，而不是直接作为独立比较合并。
3. 分别进行客观冻结事件和主观冻结评分的汇总。
4. 对 [R17] 等效应量较大的研究实施预设敏感性分析。
5. 将本轮已核实的 2026 年多中心随机平行组研究 [R18] 纳入后续更新；由于 [R18] 发表于 2026 年 10 月，不能假定截至 2026 年 5 月的 [R28] 已包含它。

**当前判断：STN+SNr 治疗 FOG 具有生物学合理性和部分患者获益的直接证据，但其群体平均增益仍属争议性结论。**

---

## 13. 第二轮证据自查与更新

本轮发现，一个可信的研究综合系统必须能够主动降低自身过度推断的风险。

### 13.1 本轮已经纠正的潜在偏差

| 初始可能产生的结论 | 新发现的反证或限制 | 更新后的判断 |
|---|---|---|
| 冻结期间 STN beta 一定增强 | [R8] 未观察到一致的 STN 局部 beta 或 burst 持续时间变化 | beta 增强不是已确立的必要条件 |
| 60 Hz 总体优于 130 Hz | [R11] 阴性结果；刺激能量、触点和患者选择不同 | 可能只对特定亚群更有效 |
| STN+SNr 具有明确额外疗效 | [R16]、[R18] 主要终点阴性；[R28] 证据不确定 | 目前存在应答异质性，尚未建立普遍获益 |
| beta burst 可以作为 FOG 的特异性因果控制变量 | [R24] 未显示自适应刺激优于连续或随机调制刺激 | 控制技术可行，特异性机制尚未验证 |
| 更低的 beta 活动一定更有利 | [R25] 特定皮层步态相位存在异常 beta 降低；[R26] 多巴胺可使高 beta 增强 | 必须区分低/高 beta、神经位置及步态相位 |

### 13.2 证据库必须保留的元数据

正式结构化附录中，每一条电生理证据都需要尽可能保留：

- **神经来源：** STN 左/右侧、功能亚区、电极触点、皮层区域、SNr。
- **临床表型：** OFF-FOG、ON-FOG、药物诱发 FOG、DBS 诱发 FOG；实际观察到的 FOG 与问卷提示的 FOG 应分开。
- **行为状态：** 静息、步态启动、稳定行走、转弯、通过门口、双任务、模拟踏步、主动停止。
- **时间定义：** 发作前、发作期、恢复期；时间窗长度及事件对齐方式。
- **信号指标：** 绝对/相对功率、低/高 beta、burst、entropy、相干性、相位耦合、神经元放电。
- **干预条件：** 药物 ON/OFF、DBS ON/OFF、频率、幅度、脉宽、触点和刺激方向。
- **独立样本标识：** 同一队列的预印本、正式发表、长期随访、不同分析不能自动计为新的独立证据。

最重要的是设置结论的失效条件。

例如，“STN beta 升高是 FOG 的必要条件”这一主张，只要出现方法可靠、冻结确认明确、神经记录质量合格且未见相应升高的实验，就必须重新评价，而不能简单将其排除为异常值。

[R8] 已经使这一强形式主张无法作为普遍结论保留。

---

## 14. 第二轮形成的竞争性机制框架（待第三轮进一步验证）

目前至少有五种可以产生不同实验预测的机制解释：

| 暂定模型 | 核心机制 | 最有区分力的预测 | 当前最主要的问题 |
|---|---|---|---|
| **M1：STN 病理性同步导致运动阻断** | 过强或过长的 STN beta 活动，使运动程序无法正常切换 | 实际冻结前应出现可重复的 STN beta 异常；选择性消除异常同步应减少冻结 | [R1]、[R8] 和 [R24] 限制其普遍性 |
| **M2：皮层—STN 网络解耦** | 步态控制所需的跨区域信息传递在关键时刻失效 | 即使 STN 局部功率不变，冻结前仍应出现具有预测性的跨区域耦合异常 | [R8] 支持，但耦合不能直接等同信息传递或因果驱动 |
| **M3：步态周期相位编码失稳** | STN 及相关皮层区域无法在正确的支撑/摆动阶段调整活动 | 相位锁定指标应优于整段平均频谱指标；相位特异性刺激应优于非特异刺激 | [R25]、[R26] 提供基础，针对 FOG 的随机机制试验仍缺乏 |
| **M4：STN—SNr—脑干步态输出门控异常** | 异常基底节输出阻碍脑干步行系统的有效募集 | 对特定纤维或输出通路的刺激应改变冻结，疗效依赖靶点位置和网络状态 | [R15–R23] 提供干预约束，但 SNr 额外疗效不稳定 |
| **M5：STN 异常只是共同网络失稳的读出** | 冻结主要由皮层、感觉整合、注意或脑干系统失稳引起，STN 活动是伴随或代偿反应 | 调节 STN 信号不必然特异性解除 FOG；其他网络指标可能更早、更稳定预测冻结 | 尚缺乏在同一患者中跨网络同步记录及正交干预的充分证据 |

这里的 M1–M5 是**明确的研究假说，不是已经验证的模型**。它们也不一定完全互斥；真正可区分的是各模型的强形式预测，例如某种活动是否为冻结的必要条件，或某条通路是否介导了刺激的疗效。

第三轮将继续处理本轮尚未完成的关键方向：PPN/MLR、脑干与小脑通路；额叶执行控制和认知双任务；药物诱发及药物抵抗性 FOG；冻结与正常停止的对照；步态测量及运动伪迹；以及早期理论模型与新电生理证据的符合程度。在此基础上，将进一步收敛机制模型并设计能够真正区分它们的实验。

【继续】

=====（下一轮）=====

# 第三轮：脑干步行系统、认知冲突、多巴胺亚型及神经—肌肉因果链

**本轮研究重点：** 解释为什么同样是 FOG，STN theta 可以升高也可以降低；为什么 STN-DBS 能改善某些冻结却无法改善另一些冻结；以及 STN 异常如何可能通过脑干和脊髓运动输出导致实际步行中断。

## 15. 新发现的关键矛盾：双任务冻结时，STN theta 反而下降

前两轮已经发现：

- [R2]：FOG 易感步态中，STN 区域 theta 增强。
- [R3]：虚拟现实冻结期间，STN theta 增强。
- [R8]：实际冻结前后，皮层—STN 的 theta-alpha 耦合降低。

第三轮发现了一项尤其重要的直接研究，它提示 theta 变化方向可能取决于冻结发生的具体阶段与诱发原因。

### 15.1 [R30] Georgiades 等，2023：认知负荷下 STN theta 减弱

**原始文献**

Georgiades MJ, et al. *Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease.* Movement Disorders, 2023;38:1549–1554.

- PMID：**37226972**
- DOI：**10.1002/mds.29455**
- <Link url="https://pmc.ncbi.nlm.nih.gov/articles/PMC10946988/" title="开放获取全文"/>

**研究设计**

- 8 名 PD 患者。
- DBS 手术期间进行 STN 微电极多单位活动记录（MUA）。
- 患者进行虚拟现实踏步任务，同时处理认知提示。
- 分析 33 次认知线索试次：18 次保持正常虚拟步行，8 次发生虚拟冻结，7 次出现显著运动减慢。
- 按认知线索出现时间和虚拟脚步进行神经活动对齐。

**关键结果**

与正常完成双任务的试次相比，出现冻结或显著减慢的试次表现为：

1. **认知提示出现附近，STN theta（3–8 Hz）活动显著降低。**
2. 降低不仅出现在认知提示之后，也延伸至后续虚拟步态阶段。
3. 研究同时观察到短暂的 STN 多单位总体放电率增加。
4. 其他频段没有得到同样明确的显著差异。

因此，这项研究并不能被概括为“冻结时 STN 活动整体降低”。它真正揭示的是：STN 的 theta 振荡成分和总体放电率可以发生不同方向的变化。[R30] <Cite refs={["turn369990search1","turn369990search2"]}/>

### 15.2 与 2019 年研究的关系

值得注意的是，[R30] 与 [R3] 来自部分相同的研究团队，均使用手术期间虚拟现实步态及 STN 微电极记录。

但两项研究测量的事件不同：

| 比较维度 | [R3] 2019 | [R30] 2023 |
|---|---|---|
| 主要问题 | 冻结发生时 STN 有何异常？ | 为什么认知提示会破坏正在进行的运动？ |
| 时间对齐 | 冻结发生及其前后 | 认知提示及随后的脚步 |
| 主要对照 | 冻结和非冻结运动状态 | 双任务成功与双任务导致运动异常 |
| theta 结果 | 冻结相关 theta 增强 | 认知负荷诱发异常时 theta 减弱 |
| 神经指标 | STN 微电极多单位活动 | STN 微电极多单位活动 |

2023 年论文作者也专门讨论了与此前 theta 增强结果不同的问题，认为认知加工时的 theta 减弱可能代表注意资源重新配置不足，而冻结临近时的 theta 增强可能反映另外一个阶段。

不过，这一解释尚未经直接验证；此外，2023 年研究将真正冻结与严重减慢合并分析，不能证明 theta 减弱仅存在于严格定义的冻结事件中。

两项研究可能存在研究团队和数据来源上的关联，尚不能把它们无条件当作两个完全独立队列的重复验证。

### 15.3 一个可以检验的双阶段假说

可以提出：

**H-theta：FOG 并非始终表现为 theta 增强或减弱，而是存在“认知控制募集不足—随后运动阻断增强”的时间序列。**

该假说预测：

- 在认知冲突提示之后、明显运动减慢之前，STN theta 可能异常减弱。
- 在随后真正发生运动冻结的时刻，STN theta 或多单位同步可能增加。
- 如果患者成功处理认知冲突，则应出现适当的早期 theta 调制，而不进入后续运动阻断状态。
- 如果把整段记录直接平均，早期下降和后期增强可能互相抵消。

这可以同时解释 [R3] 和 [R30] 的部分差异，但目前仍只是待证伪模型。

最关键的验证方式是在同一患者、同一实验范式、同一种神经记录中，同时测量认知提示、运动减慢、冻结开始和重新迈步四个事件，而不是分别从不同实验推断过程顺序。

---

## 16. 更早的 STN 研究：低 beta 异常并不是 2019 年以后才发现

### 16.1 [R31] Singh 等，2013：自由步态中的 beta 调制异常

Singh A, et al. *Freezing of gait-related oscillatory activity in the human subthalamic nucleus.* Basal Ganglia, 2013;3:25–32.

DOI：**10.1016/j.baga.2012.10.002**

研究记录了 6 名 PD 患者在跑步机行走过程中的 STN LFP：

- 3 名患者表现为较慢但连续的行走。
- 3 名患者出现严重的步态犹豫或冻结。

没有冻结的患者在行走时，相比坐位或站立，STN beta（12–35 Hz）活动广泛下降。

而存在冻结的患者未显示同样正常的 beta 抑制模式，并出现较明显的低 beta（约 12–22 Hz）活动。

**这是一项早期、直接支持低 beta 与异常步态相关的原始研究。**

它解释了为什么 [R2] 关注约 18 Hz 的低 beta，而不是把所有 beta 频率合并。

但研究只有 6 人，且采用术后早期记录。不能把三名 Freezer 的观察当作对所有 FOG 表型的普遍规律。[R31] <Cite refs={["turn338816search2","turn338816search11"]}/>

### 16.2 必须保留的反例

[R1] 在慢性植入、自然行走条件下，Freezer 未冻结时的 beta 功率低于 Non-Freezer，与 [R31] 的方向不同。

这表明，研究冲突至少涉及以下三个彼此独立的比较：

- 患者间：Freezer 与 Non-Freezer。
- 患者内：走路与静止。
- 事件内：冻结前、冻结时及冻结后。

不能把这三个比较的效应方向放在同一个坐标上解释。

特别是，**“行走期间 beta 下降幅度不足”不等价于“行走期间绝对 beta 功率高于另一组患者”。** 在不同基线功率、不同频谱分段和不同归一化方式下，这两种结论完全可能同时成立。

---

## 17. Beta burst 与步态周期：病理性同步和生理性同步可能被混为一谈

### 17.1 [R32] Toledo 等，2014：静息高 beta 与 FOG 表型相关

Toledo JB, et al. *High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease.* Neurobiology of Disease, 2014.

- PMID：**24361601**
- DOI：**10.1016/j.nbd.2013.12.005**

研究分析了 22 名 PD 患者的 STN 电活动，其中 14 名存在 FOG、8 名无 FOG。

结果显示：

- FOG 患者静息 STN 高 beta（22–35 Hz）活动更强。
- 左旋多巴治疗能够降低部分高 beta 活动。
- 高 beta 异常可能与皮层—STN 的异常同步有关。

但这主要是患者间的静息状态比较，并非实际冻结发作前后的连续电生理记录。因此，它更适合被解释为 FOG 表型相关特征，而不是冻结发生的直接触发信号。[R32]

### 17.2 [R33] Storzer 等，2017：运动本身也可能增强狭窄频段 beta

Storzer L, et al. *Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia.* Annals of Neurology, 2017.

- PMID：**28892573**
- DOI：**10.1002/ana.25047**

研究比较 PD 患者骑车和行走期间的 STN 活动，纳入 5 名 Freezer 和 8 名 Non-Freezer。

两类运动均可引起广泛的 beta 抑制，但部分 Freezer 在运动中还表现出约 18 Hz 的狭窄频段 beta 增强，而且这种增强并不要求当时实际发生 FOG。

这提示至少需要区分：

- 广泛的运动相关 beta 去同步化。
- 运动过程中某一狭窄频带的同步增强。
- 与实际冻结事件时间锁定的异常活动。

否则，“beta 增加”与“beta 减少”可能只是研究者观察了不同的频谱成分。[R33]

### 17.3 [R34] Anidi 等，2018：持续时间可能比平均功率更重要

Anidi C, et al. *Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease.* Neurobiology of Disease, 2018.

- PMID：**30196050**
- DOI：**10.1016/j.nbd.2018.09.004**

研究纳入 12 名 PD 患者，包括 8 名 Freezer 和 4 名 Non-Freezer，利用植入式记录系统研究步态期间的 STN beta burst。

主要发现：

1. Freezer 的较长持续时间 beta burst 更明显。
2. 部分真实冻结发作伴随异常长 burst。
3. 在 Freezer 内部比较冻结与非冻结时，burst 的功率本身并没有显示同样明确的差异。
4. 60 Hz 和 140 Hz DBS 都可以减少长时间 beta burst，并改善部分步态指标。
5. 左右 STN beta burst 持续时间的不对称性，与步幅时间的不对称性相关。

这为一个更精确的解释提供了支持：

**可能造成问题的不是 beta 活动本身，而是 beta 活动无法在运动需要时及时终止。**

但 burst 持续时间与 FOG 同时变化，仍然不能证明长 burst 是冻结的原因。DBS 也可能先改变运动状态，然后间接改变 beta burst。[R34]

### 17.4 [R35] Fischer 等，2018：正常踏步也需要有节律的 STN beta 调制

Fischer P, et al. *Alternating Modulation of Subthalamic Nucleus Beta Oscillations during Stepping.* Journal of Neuroscience, 2018.

- PMID：**29760182**
- DOI：**10.1523/JNEUROSCI.3596-17.2018**

16 名 PD 患者接受 STN LFP 记录，并执行有节律的踏步任务。

研究发现，STN beta 活动随左右脚踏步周期交替调制，而不是在整个踏步过程中始终维持同一水平。

这是一个重要的生理学约束：

**正常运动并不要求 beta 信号始终很低，而要求神经活动按照运动阶段进行适当的时间调节。** [R35]

### 17.5 [R36] Thenaisie 等，2022：STN 包含可解码的步态信息

Thenaisie Y, et al. *Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease.* Science Translational Medicine, 2022.

- PMID：**36070366**
- DOI：**10.1126/scitranslmed.abo1800**

研究在 18 名 PD 患者中同步分析 STN 神经电活动和步态相关运动学。

结果表明，STN 活动包含与下肢运动幅度、步态状态及运动活力相关的信息。

这意味着不能将全部步态相关 STN 活动视为病理性噪声。某些活动可能是运动指令、感觉反馈或正常动作状态的编码。

不过，从 STN LFP 能够解码运动状态，并不能证明 STN 必然是生成该状态的原因。[R36]

### 17.6 综合：beta 应被看作多个动力学过程，而非单一强度指标

将 [R1]、[R8]、[R26] 和 [R31–R36] 放在一起，可以形成一套更严格的研究区分。

| beta 指标 | 可能反映的过程 | 主要误判风险 |
|---|---|---|
| 静息平均 beta 功率 | 长期运动障碍、疾病状态或 FOG 表型 | 错当作冻结瞬时机制 |
| 运动相对静息的 beta 抑制 | 运动相关状态转换 | 错当作绝对 beta 功率 |
| 低 beta / 高 beta | 不同神经网络或药物调制 | 合并频带后方向相互抵消 |
| beta burst 持续时间 | 神经同步状态的稳定性 | 用功率替代持续时间 |
| 步态周期锁定的 beta | 正常运动编码及其异常 | 把生理性同步当作病理性同步 |
| 冻结前后的 beta 变化 | 候选发作信号 | 错把冻结后的反应当作原因 |

目前最值得进一步检验的 beta 机制不是“beta 越高越容易 FOG”，而是：

**在步态控制需要快速转换的特定阶段，病理性持续同步可能妨碍正常、短暂且相位特异的 STN 活动调制。**

这是一项能够整合若干结果的工作假说，但它仍须面对 [R8] 中冻结期间未发现显著长 beta burst 改变的反例。

---

## 18. 从 STN 活动到腿部肌肉：冻结的神经—肌肉输出链

### 18.1 [R37] Klocke 等，2024：STN—肌肉耦合异常与主动停止不同

Klocke P, et al. *Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease.* Brain, 2024;147:4056–4071.

- PMID：**39470410**
- DOI：**10.1093/brain/awae223**

这项研究的特色是同时记录：

- STN LFP。
- 下肢拮抗肌表面肌电（EMG）。
- 步态运动学。
- 自然行走中的实际冻结。
- 患者主动停止行走的对照事件。

研究发现，从正常行走进入 FOG 时：

1. STN 振荡活动在冻结前及冻结期间存在异常转换。
2. 下肢拮抗肌原有的交替活动模式受到破坏。
3. 拮抗肌共同收缩（co-contraction）增加。
4. 腓肠肌的激活时序发生异常。
5. **在冻结出现前，STN 与腓肠肌之间的相干性增加。**

这比单纯发现“STN beta 发生变化”更接近运动执行层面，因为它同时描述了神经信号与最终肌肉输出之间的关系。[R37] <Cite ref="turn515016search2"/>

### 18.2 为什么这项研究具有特殊价值？

FOG 的实际临床现象是患者试图迈步，却无法产生有效步伐。因此，真正的机制模型必须解释神经活动怎样转化为下肢运动失败。

可以提出如下待检验的因果链：

<box border radius="lg" padding={3} gap={2}>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **STN 及其相关网络的异常时序活动**
    <caption>局部同步、跨区域耦合或阶段转换失稳</caption>
  </box>
  <row justify="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </row>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **下降运动控制信号异常**
    <caption>脑干—脊髓通路及肌肉激活协调受到干扰</caption>
  </box>
  <row justify="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </row>
  <box background="surface-secondary" radius="md" padding={3} align="center">
    **拮抗肌协调失效**
    <caption>共同收缩增加、交替活动时序破坏</caption>
  </box>
  <row justify="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </row>
  <box border radius="md" padding={3} align="center">
    **迈步尝试无效：FOG**
  </box>
  <caption>图示为由 [R37] 启发的假说性因果链，不代表实验已经确定各环节的因果方向。</caption>
</box>

与这条链竞争的另一种解释是：

**下肢运动控制先发生异常，随后异常本体感觉反馈同时改变肌肉活动和 STN 信号。**

由于 STN—肌肉相干性可以来自共同输入、下降通路、上行感觉反馈或多种信号混合，仅凭相干性增强不能区分上述解释。

有区分力的实验应同时分析 STN、肌肉、足底压力及感觉输入，并使用具有明确时间靶点的闭环干预，而不是只比较冻结前后的相关系数。

---

## 19. PPN、中脑步行区与楔形核：支持网络机制，但不支持简单的“刺激即可解除冻结”

### 19.1 脑干网络为什么重要？

STN 可以通过基底节输出网络影响脑干步态控制，但中脑步行区并非单一核团。

相关结构包括：

- 脚桥核（pedunculopontine nucleus，PPN）。
- 楔形核（cuneiform nucleus，CuN）。
- 相关网状结构及下降脊髓通路。

PPN 与 CuN 的功能并不完全相同。因此，研究中使用的“PPN 区”“中脑步行区”“PPN/CuN 联合刺激”不能不加区分地视为相同靶点。

### 19.2 [R46] Thevathasan 等，2012：PPN alpha 在冻结前降低

*Alpha oscillations in the pedunculopontine nucleus correlate with gait performance in parkinsonism.*

- PMID：**22232591**
- DOI：**10.1093/brain/awr315**

研究直接记录接受 PPN 区电极植入患者在自然行走期间的 LFP。

主要发现：

- PPN 区 alpha 振荡与行走速度相关。
- 较好的行走表现伴随较高 alpha 活动。
- 冻结期间 PPN alpha 活动受到抑制。
- alpha 与 beta 活动在 PPN 区域具有不同的空间分布。

研究中时间对齐的冻结前 alpha 降低分析，主要来自一名患者的多次冻结事件。

这一点非常重要：**同一人的多次冻结不能被当作多个独立患者的重复验证。**

该研究支持“脑干步态相关振荡活动可能在冻结发生前出现异常”，但尚不能证明 PPN alpha 下降是必要的冻结触发因素。[R46] <Cite ref="turn233206view1"/>

### 19.3 干预证据：早期希望与后续随机研究不一致

| 研究 | 设计 | 结果 |
|---|---|---|
| [R44] Ferraye，2010 | 6 名药物及 STN-DBS 治疗后仍有严重 FOG 的患者；PPN 区双侧刺激、含双盲交叉评估 | 一年后 OFF 药物状态下部分冻结时间改善，但双盲阶段及其他主要终点未显示可靠改善 |
| [R45] Thevathasan，2011 | 5 名严重顽固性 FOG 患者；双侧 PPN 刺激前瞻性随访 | 自评冻结改善，但样本极小，缺少充分的同期随机对照 |
| [R49] Nosko，2015 | 9 名患者；比较 PPN 区低频与较高频刺激 | 提示部分患者对较低频率有更好反应，但存在明显个体差异 |
| [R47] Bourilhon，2022 | 6 名患者；PPN、CuN 和假刺激随机双盲交叉，每种条件约 2 个月 | 主要姿势准备指标阴性；CuN 改善某些步态运动学，但临床量表未显示可靠获益 |
| [R48] Bourilhon，2022 | 上述相同 6 名患者的两年以上长期随访 | 没有观察到持续、可靠的临床获益 |

尤其是 [R47]，研究发现 CuN 刺激对部分步幅和速度指标有利，但并没有据此获得明确的总体临床改善。PPN 刺激在某些运动学指标上甚至表现得比假刺激差。

[R48] 与 [R47] 是**同一六人队列的不同随访报告，不应在证据汇总中按十二名患者计算**。[R44–R49] <Cite refs={["turn391286search2","turn391286search4","turn878074search1"]}/>

### 19.4 对 STN—SNr—PPN 机制模型的约束

这些干预结果并不否认脑干步态网络参与 FOG。

但它们否定了过于直接的临床推论：

“只要 STN 的异常经 SNr 抑制 PPN，就应该可以通过刺激 PPN 可靠解除 FOG。”

实际结果表明至少还需要考虑：

- 电极是否准确募集相关脑干神经元及纤维。
- PPN 与 CuN 不同部分的功能差异。
- 刺激是增强、阻断还是重组有效输出。
- 步态启动、持续迈步、平衡和冻结是否具有不同神经控制环节。
- 晚期患者的下游系统是否仍具备可恢复功能。
- 临床量表能否捕捉某一特定运动学环节的改善。

因此，**PPN/MLR 机制目前是有电生理支持、但临床干预验证仍不充分的网络解释**，不能把其理论合理性误认为已证实的治疗机制。

---

## 20. 认知冲突、视觉环境与额叶网络：FOG 可以发生于运动执行失败之前

### 20.1 [R39] Matar 等，2013：运动输出对认知冲突及门口环境特别敏感

*Using virtual reality to explore the role of conflict resolution and environmental salience in freezing of gait in Parkinson's disease.*

- PMID：**23831480**
- DOI：**10.1016/j.parkreldis.2013.06.002**

研究比较了 36 名 Freezer、37 名 Non-Freezer 和 18 名健康对照，使用虚拟现实脚踏任务测试：

- 需要抑制既定反应的认知线索。
- 狭窄门口。
- 自动门开启等环境变化。

Freezer 在抑制反应和处理上述视觉环境线索时，表现出更长的脚步反应延迟。

这表明，FOG 易感性不仅与运动输出能力有关，还与认知冲突解决和环境信息处理有关。

但这里记录的是虚拟现实任务中的脚步延迟，不能把所有反应延迟都判为真实负重行走中的 FOG。[R39] <Cite ref="turn515016search1"/>

### 20.2 [R38] Shine 等，2013：额顶认知控制网络与基底节功能解耦

*Freezing of gait in Parkinson's disease is associated with functional decoupling between the cognitive control network and the basal ganglia.*

- PMID：**24142148**
- DOI：**10.1093/brain/awt272**

研究利用虚拟现实运动任务及功能磁共振，比较冻结易感和非冻结患者的脑网络活动。

结果支持一个模型：当认知控制、视觉环境处理和步态控制之间的需求增加时，额顶认知控制网络与基底节之间的功能协调可能失效。

这一结果与自然行走时皮层—STN 低频耦合下降的研究 [R8] 存在机制上的一致性。

但要明确区分：

- [R38] 的证据主要来自 BOLD 功能连接及虚拟运动任务。
- [R8] 的证据来自实际步行和电生理耦合。

二者使用的信号、时间尺度和运动条件不同，因此只能说彼此提供了跨模态支持，不能视为同一神经过程已被直接重复证明。[R38] <Cite ref="turn515016search6"/>

### 20.3 [R50] Tian 等，2026：真实冻结前两秒的网络异常

*Aberrant Beta-Band Network Alteration Preceding Freezing of Gait in Parkinson's Disease.*

- PMID：**41760132**
- DOI：**10.1002/mds.70230**

研究在 18 名存在 FOG 的 PD 患者中同步记录行走 EEG，并比较实际冻结与主动停止之前两秒的皮层网络组织。

冻结前出现：

- 右侧额顶、额叶、顶枕、视觉及岛叶相关区域的局部 beta 连接增强。
- 较低频段的额叶—后部皮层连接减弱。
- 网络组织更加局部分隔，而部分远距离协调减弱。

这是对“网络协调失败”模型的有价值补充，因为其比较对象不是任意静止阶段，而是患者主动停止行走。

不过，EEG 重建的皮层连接不是 STN 直接记录。更不能直接据此认定右额顶 beta 增强驱动 STN，从而造成冻结。[R50] <Cite ref="turn391286search0"/>

### 20.4 网络结果中的两种解释

**解释一：认知控制能力不足。** 在转弯、门口、双任务等需要重新选择运动程序的情况下，皮层—基底节网络无法提供适当的控制信号。

**解释二：冲突触发过度抑制。** 感觉与认知输入之间产生竞争，STN 通过运动抑制网络发挥一种过强的“暂停”作用，最终妨碍迈步。

二者可以在同一患者身上产生相似 FOG 表型，却对 STN theta 提出不同预测：

- 如果是控制募集不足，冻结前早期可能出现任务相关 theta 调制不足，与 [R30] 相容。
- 如果是过度抑制，真正运动阻断时可能出现 theta/beta 同步及 STN 神经元活动增强，与 [R3] 相容。

因此，接下来的核心不是再证明“认知任务能够诱发 FOG”，而是判断认知线索出现后究竟首先发生了哪一种神经转换。

---

## 21. 多巴胺反应不同的 FOG 不是一个同质人群

### 21.1 [R41] Espay 等，2012：真正的左旋多巴诱发 FOG

*"On" state freezing of gait in Parkinson disease: a paradoxical levodopa-induced complication.*

- PMID：**22262741**
- DOI：**10.1212/WNL.0b013e3182477ec0**

四名患者在三个药物状态下接受评估：

- OFF：停药后。
- ON：常规左旋多巴剂量产生充分药效后。
- Supra-ON：高于常规剂量。

患者在 ON 和 Supra-ON 状态下出现或加重 FOG，而且冻结程度呈剂量依赖性增加；与此同时，其他典型帕金森运动症状得到改善。

这证明存在一种临床表型：**提高多巴胺能刺激可以改善肢体运动迟缓，却使冻结步态恶化。**

但仅有四例，不能推断该亚型的流行率，也不能证明 STN 具有特定的病理振荡方向。[R41] <Cite ref="turn565391search1"/>

### 21.2 [R42] McKay 等，2019：药物充分起效后仍持续的 FOG

*Freezing of Gait can persist after an acute levodopa challenge in Parkinson's disease.*

- PMID：**31799377**
- DOI：**10.1038/s41531-019-0099-z**

55 名患者完成左旋多巴挑战，其中 45 名达到研究预先规定的充分运动症状改善标准。

在这 45 名患者中：

| 表型 | 人数 | 解释 |
|---|---:|---|
| ONOFF-FOG | 19 | 充分 ON 后冻结仍持续 |
| OFF-FOG | 11 | 冻结能够被左旋多巴改善 |
| NO-FOG | 15 | 研究评估条件下未表现 FOG |

研究还检测血清左旋多巴浓度，以减少“药物根本没有充分起效”导致的误分类。

因此，**ONOFF-FOG 不等于左旋多巴诱发的 ON-FOG**：

前者强调药物充分起效后冻结仍存在；后者强调药物使冻结新出现或恶化。[R42] <Cite ref="turn391286search1"/>

### 21.3 [R43] Nonnekes 与 Bloem，2020：双相冻结

*Biphasic Levodopa-Induced Freezing of Gait in Parkinson's Disease.*

- PMID：**32417798**
- DOI：**10.3233/JPD-201997**

这一病例研究描述了更复杂的多巴胺反应曲线：冻结可以在药物作用的某些中间阶段出现，而在不同药物浓度或效应阶段减轻。

对研究设计的启示是：把药物暴露仅编码为二元 ON/OFF 可能不够，某些患者需要记录给药后的时间、剂量和临床运动状态。

但这是病例报告，双相机制尚不能推广至一般 PD-FOG 人群。[R43] <Cite ref="turn565391search4"/>

### 21.4 [R40] Lench 等，2024：药物反应性与 STN 网络连接有关

*Subthalamic functional connectivity associated with freezing of gait dopa-response.*

- PMID：**38101024**
- DOI：**10.1016/j.parkreldis.2023.105952**

55 名 PD 患者接受功能连接研究，其中：

- FOG 患者 38 名。
- 药物反应性 FOG：22 名。
- 药物无反应性 FOG：16 名。
- 无 FOG：17 名。

结果发现：

- 药物反应性 FOG 与右侧 STN—小脑步行相关区域及颞枕皮层较强的功能连接有关。
- 药物反应性 FOG 也表现出较强的左侧 STN—枕叶连接。
- 药物无反应性 FOG 表现出较强的左侧 STN—中央后回连接。
- 部分连接强度与左旋多巴改善 FOG 的幅度相关，而不是简单与总体运动评分相关。

这支持药物反应性不同的 FOG 可能涉及不同的感觉—运动网络。

但研究使用静息态 BOLD 功能连接，而非 STN LFP。它不能说明上述连接的电生理频率，也不能证明它们直接决定药物疗效。[R40] <Cite ref="turn391286search3"/>

### 21.5 [R58] Fraix 等，2013：多巴胺同时改变冻结和脑干频谱

*Pedunculopontine nucleus area oscillations during stance, stepping and freezing in Parkinson's disease.*

- PMID：**24386308**
- DOI：**10.1371/journal.pone.0083919**

研究在 7 名接受 PPN 区电极植入的患者中分析脑干 LFP；其中有可用于冻结比较的踏步记录。

在 OFF 药物状态下，患者原地踏步期间频繁出现冻结；左旋多巴治疗后，冻结时间占试次的比例从约 61.7% 降至 7.3%。

与此同时，PPN 区 alpha 活动增加，beta 与 gamma 活动下降。

这是重要的脑干电生理—临床联合观察，但不能确定药物首先改变 PPN 振荡，还是通过改善整体运动状态间接改变这些振荡。

另外，研究部分统计涉及多个电极触点；触点和事件数均不能替代独立患者数。[R58] <Cite ref="turn565391search0"/>

### 21.6 本节综合判断

FOG 研究中至少应预先区分：

- 药物可改善的 OFF-FOG。
- 充分药物作用下仍持续的 ONOFF-FOG。
- 药物诱发或明显加重的 ON-FOG。
- 具有双相药物反应的 FOG。

这些群体的 STN 振荡方向、网络参与和 DBS 治疗反应可能不同。

**因此，任何没有充分描述药物状态的“FOG 患者 STN beta/theta 特征”都应被视为条件不明的证据，而不是普遍机制结论。**

---

## 22. FOG 的判定标准和机器学习误差可能改变神经机制结论

### 22.1 [R56] 2026 年 ICFOG 共识：重新定义实际冻结事件

Gilat M, et al. *An updated definition of freezing of gait.* Nature Reviews Neurology, 2026.

- PMID：**41513745**
- DOI：**10.1038/s41582-025-01179-3**

国际 FOG 联盟（ICFOG）提出了新的临床和视频评分定义，核心是：

**患者正在尝试迈步，但不能形成有效的步伐。**

与此前部分研究使用的“脚部前向运动减少”定义相比，新定义更加重视可观察到的迈步尝试，并明确：

- 冻结可以发生于步态启动、转弯及不同方向的迈步。
- 并非所有连续小碎步都属于 FOG。
- 主动停止行走不是 FOG。
- 冻结可以表现为无明显下肢运动的 akinetic FOG，或伴随震颤、低效碎步等的 kinetic FOG。
- 视频评分时，冻结结束通常要求恢复连续两个有效步伐，或者患者停止尝试迈步。

该文件属于经过专家讨论形成的共识，不是关于 STN 活动的原始实验证据。但对于重新评价既往电生理研究中的 FOG 标签，它具有直接的方法学价值。[R56] <Cite ref="turn515016search0"/>

### 22.2 [R57] Zoetewei 等，2024：任务选择决定能否可靠捕获 FOG

*Which Gait Tasks Produce Reliable Outcome Measures of Freezing of Gait in Parkinson's Disease?*

- PMID：**39121137**
- DOI：**10.3233/JPD-240134**

研究纳入 63 名明确的 Freezer，并在其中 26 人中评估五周后的重测可靠性。

结果表明：

- 360° 原地转身特别容易诱发 FOG。
- OFF 药物状态一般比 ON 状态更敏感。
- TUG、360° 转身、认知双任务及门口任务的组合，比仅采用单一直线行走更有利于获得冻结事件。
- 即使采用标准任务，冻结时间百分比的最小可检测变化仍然较大。

这意味着电生理研究中“没有观察到 FOG”可能只是任务诱发不足，不等于患者缺少冻结易感性。[R57] <Cite ref="turn756115search2"/>

### 22.3 [R54]、[R55]：自动判定算法的误差不是可以忽略的小问题

2024 年 Yang 等研究 [R54] 纳入 12 名患者，发现基于惯性测量单元（IMU）的 FOG 算法能否泛化到新任务、能否识别主动停止，与训练数据组成密切相关。

2026 年多中心研究 [R55] 进一步表明：

| 评估场景 | 冻结时间百分比与人工视频标注的一致性 ICC |
|---|---:|
| 本地队列 | 0.886 |
| 六个外部队列平均 | 0.562 |
| 使用约 50 分钟外部数据调整后 | 0.732 |

[R55] 训练队列为 85 名参与者、2,043 次试验，外部验证包含 256 名参与者、1,058 次试验。

这说明，即使是相同类型的 FOG 自动标注系统，换一个研究中心、摄像角度、任务或患者群体，其可靠性也可能明显下降。[R54, R55] <Cite refs={["turn756115search0","turn756115search3"]}/>

### 22.4 [R52] Alberts 等，2026：STN LFP 可以检测部分冻结，但泛化仍有限

*An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease.*

- PMID：**42239677**
- DOI：**10.3389/fneur.2026.1793291**

研究在 5 名 PD 患者中利用慢性 STN LFP，开发基于多个频段、burst 及动态统计特征的深度学习检测系统。

模型通过三秒历史窗口判断窗口结束时是否处于 FOG 状态，测试包含 8 次行走试验。

报告的窗口级性能为：

- Weighted F1 ≈ 0.67。
- Macro F1 ≈ 0.62。
- 平均灵敏度 ≈ 0.59。
- 平均精确率 ≈ 0.55。

研究还发现，同一患者不同诱发任务的特征重要性可能不同。

**本轮原文质量复核发现一处需要保留的内部数据不一致：**

论文摘要报告检测到 24/29 次冻结；正文结果段落和表格则报告测试集共有 30 次冻结、检测到 24/30 次。两者都被写成约 80%。

在没有作者澄清前，结构化证据库应记录“正文 24/30、摘要 24/29 不一致”，而不是无条件选取其中一个数字。

此外，论文的冻结事件检测标准允许一次冻结期间至少 25% 的预测窗口被判为阳性。因此，这里的事件检测率不等于模型完整、连续地识别出每次冻结。

模型还需要在测试试验早期使用已标记数据进行个体化调整，尚不能等同于完全不需标注、可在新患者中直接运行的实时预警系统。

这是技术可行性的证据，不是对某一种 STN 频谱机制的独立验证。[R52] <Cite refs={["turn218560search1","turn498362view3"]}/>

### 22.5 [R51] Leedom 等，2026：低 beta burst 可能更多反映一般 PD，而非 FOG

*Frequency-Specific EEG burst dynamics in Parkinson's Disease and freezing of gait.*

- PMID：**42778807**
- DOI：**10.1007/s00415-026-14149-6**

研究分析 237 名参与者的静息 EEG，其中 149 名 PD、88 名健康对照；PD 患者中 73 名存在 FOG、76 名不存在。

主要结果：

- PD 患者整体表现出更频繁、持续时间更短的低 beta burst。
- 在仅比较 PD 患者并进行统计调整后，低 beta burst 对 Freezer 和 Non-Freezer 的区分并不稳健。
- FOG 严重程度与 theta burst 振幅相关的特征更一致。

这提示某些看似“FOG 相关”的神经指标，可能只是 PD 的一般性病理特征。

但该研究测量的是 ON 药物静息状态的**头皮 EEG，而非 STN LFP**。因此，它不能直接否定 STN 中长 beta burst 与实际冻结的关系。[R51] <Cite ref="turn957799search0"/>

---

## 23. 第三轮后需要重点检验的六项竞争性假说

为了保证假说真正可检验，本研究不再只使用“网络失调”“同步异常”这样难以证伪的宽泛解释，而是要求每个假说明确其预测和失败条件。

| 编号 | 机制假说 | 最有区分力的预测 | 关键反证 |
|---|---|---|---|
| H1 | **STN beta 运动阻断模型** | 在特定 FOG 亚型中，冻结前存在长 beta burst 或低 beta 异常增加；提前削弱该活动可减少 FOG | 严格确认的 FOG 在干预前没有相应异常，或者选择性抑制异常后 FOG 不变 |
| H2 | **步态相位编码失稳模型** | 步态周期锁定特征比整段平均 beta 更好地预测冻结；相位匹配刺激优于等负荷随机刺激 | 控制步幅和运动阶段后，相位指标失去预测效应 |
| H3 | **认知控制—运动阻断双阶段模型** | 认知线索后早期 theta 调制不足，随后实际冻结期出现异常 STN 同步；同一患者可观察到这一时间顺序 | 严格时间对齐后不存在可重复的双阶段过程 |
| H4 | **皮层—STN 网络解耦模型** | 冻结前低频耦合异常优于 STN 局部功率预测 FOG，并区别于主动停止 | 相干性异常完全由运动减慢、视觉输入或共同伪迹解释 |
| H5 | **STN—SNr—脑干输出门控模型** | 与下降步态通路匹配的刺激位置及特定 STN—肌肉耦合变化预测疗效 | 精准通路刺激及预先指定的中介指标改变后，冻结仍无相应变化 |
| H6 | **STN 为下游读出/代偿节点模型** | STN 信号可用于检测 FOG，但针对它的时间特异性调节未必优于非特异刺激；其他网络异常可能更早出现 | 对 STN 某特定信号的选择性干预能够稳定且特异地预防 FOG，并证明中介关系 |

各模型的证据和地位不同：

- H1 具有较多局部电生理证据，但其“普遍必要性”已受到 [R1] 和 [R8] 限制。
- H2 受到 [R25]、[R26]、[R35]、[R36] 支持，但直接的相位锁定治疗试验不足。
- H3 可解释 [R3] 与 [R30] 的 theta 方向冲突，但双阶段序列尚未在同一实验中验证。
- H4 获得 [R8]、[R38]、[R50] 的跨模态支持，但有效连接方向与真正因果驱动仍未知。
- H5 有 [R37] 的神经—肌肉联合记录和若干 DBS 干预作为基础，但 [R18]、[R44]、[R47]、[R48] 的阴性结果必须得到解释。
- H6 是一个必须保留的替代解释，尤其适用于避免把高预测准确率直接当作病因证据。

### 最有价值的一项判别实验

如果只能优先开展一项研究，应考虑**同一患者内、跨诱发任务、同时记录神经活动与肌肉输出的随机闭环干预试验**。

实验至少设置：

1. 预先按左旋多巴挑战结果区分 FOG 亚型。
2. 同步记录双侧 STN LFP、皮层活动、下肢 EMG、足底压力及视频。
3. 使用步态启动、360° 转身、门口和双任务诱发冻结，同时设置主动停止对照。
4. 先在独立训练阶段确定个体化神经标志物，再锁定分析方案。
5. 比较 beta burst 触发、皮层—STN 耦合触发、步态相位触发及刺激负荷匹配的随机调制。
6. 在独立的测试日评估冻结次数、冻结时间、首次无效迈步之前的预警时间，以及刺激相关不良步态效应。

最关键的是检验**机制—干预交互作用**：

如果某个信号真正介导冻结，那么选择性针对它的刺激应当在该信号异常的试次中产生更大获益，而不是仅仅使患者总体运动评分改善。

此外，不能把一个患者的数百次冻结当作数百个独立受试者；统计模型必须同时处理患者、试次、事件及刺激阶段的层级结构。

---

## 24. 第三轮质量复核与证据库更新

### 24.1 新增的非多巴胺系统证据

**[R53] Bohnen 等，2024**

*Dynamic balance and gait impairments in Parkinson's disease: novel cholinergic patterns.*

- PMID：**39252998**
- DOI：**10.1093/braincomms/fcae286**

研究在 125 名 PD 患者中利用胆碱能神经末梢 PET 标记，分析动态平衡和步态障碍与脑内胆碱能神经支配之间的关系。

研究支持步态和平衡障碍涉及多巴胺之外的胆碱能网络。这对于解释晚期、药物抵抗性 FOG 具有潜在价值。

但该研究的主要临床结局并不是对每次实际 FOG 的同步观测，不能直接证明胆碱能缺损导致 STN 某一频段异常。[R53] <Cite ref="turn756115search10"/>

### 24.2 本轮完成的证据质量检查

| 发现的问题 | 具体研究 | 处理方法 |
|---|---|---|
| 静息态差异被解释成冻结发作机制 | [R7]、[R32]、[R51] | 分别归档为表型关联，不直接升级为触发机制 |
| 同一研究团队或队列可能重复计算 | [R1]/[R34]、[R3]/[R30] | 设置潜在队列重叠标识；独立性未确认前不得简单累计样本 |
| 相同患者的长期随访被视为独立试验 | [R47]/[R48] | 明确记录为同一六人队列 |
| EEG、fMRI、STN-LFP 混合使用同一机制标签 | [R38]、[R40]、[R50]、[R51] | 保留信号来源和测量尺度，不做未经验证的跨模态等同 |
| 将模拟脚踏减慢等同于实际 FOG | [R3]、[R30]、[R39] | 单列虚拟现实冻结及严重减慢，区别于真实负重行走 |
| 研究内部检测事件数不一致 | [R52] | 同时保留摘要 24/29 和正文 24/30，并标记待核查 |
| 将同一患者不同触点或多次事件当作独立样本 | [R46]、[R58] | 区分患者数、触点数、试次数、冻结事件数 |
| 将预测能力误认为机制因果性 | [R36]、[R52] | 归档为解码/检测证据，因果强度单独评价 |

### 24.3 截至第三轮，哪些结论可以保留？

**较有把握的结论**

STN 参与帕金森病步态的神经控制，其活动受到步态周期、运动任务、药物状态和 DBS 的调制。[R25, R26, R35, R36]

FOG 与 STN 的局部活动和皮层—基底节网络异常存在多种可重复观察到的关联，但这些关联并不服从简单、统一的“beta 必然升高”规律。[R1–R8, R30–R34]

STN-DBS 能改变 FOG，但疗效受到刺激位置、频率、药物状态和患者表型影响。[R9–R24]

**仍有实质争议的结论**

STN 的长 beta burst、低 beta 增高、theta 调制异常或皮层—STN 解耦，哪一种在实际冻结前具有最高的特异性和可重复性。

STN+SNr 或 PPN/CuN 额外刺激能否为经过优化的常规 STN-DBS 提供稳定、临床重要的额外获益。

FOG 的最初因果障碍究竟发生在皮层认知控制、STN 运动状态转换、脑干步行输出，还是多个环节之间的协调关系。

**目前仍属于假说的结论**

某一 STN 振荡异常是所有 FOG 的必要或充分原因；消除该异常即可特异性解除冻结；不同药物反应亚型共享同一种 STN 发作机制。

### 24.4 下一轮的整合目标

前三轮已建立涵盖 **R1–R58** 的候选文献体系，包含 STN 微电极和 LFP、真实步行、皮层网络、药物挑战、DBS 随机试验、脑干靶点、影像和冻结事件标注方法。

下一轮将对参考文献进行最后的交叉核验，把可证实的研究信息整合成**完整而不依赖前文的研究报告**，同时生成用户要求的 JSON 结构化附录。附录将明确连接原始研究、证据条目、跨研究结论和竞争性假说，并将本文发现的数据不一致、潜在队列重复及结论失效条件保留下来，供后续研究更新使用。

【继续】

=====（下一轮）=====

# 丘脑底核神经活动与帕金森病冻结步态的关系：证据冲突、网络机制与因果检验

**研究报告终稿｜截至 2026 年 11 月 13 日**

**领域：** 功能神经外科、运动障碍、神经电生理、神经调控
**核心对象：** Subthalamic nucleus（STN）、Deep Brain Stimulation（DBS）、Parkinson's disease（PD）、Freezing of gait（FOG）

**研究性质：** 基于原始文献核验的结构化叙述综述与机制比较研究。本文不声称完成了具备完整检索日志和双人独立筛选的 PRISMA 系统综述，也不声称进行了新的患者级 Meta 分析。

## 摘要

**背景：** 帕金森病冻结步态是药物和脑深部电刺激治疗中的重要难题。STN 作为基底节运动网络的关键节点，其病理性神经活动被认为可能参与 FOG，但现有研究对 beta、theta、alpha 振荡的变化方向、时间特征、空间定位及因果意义存在明显分歧。

**目的：** 比较 STN 神经活动与 FOG 关系的直接证据，解释研究冲突，评估 DBS 干预提供的因果约束，并提出具有相互区分预测和明确证伪条件的机制模型。

**方法：** 围绕 STN-LFP、微电极单/多单位记录、皮层—STN 耦合、FOG 事件、步态周期、STN-DBS、SNr、PPN/CuN、药物状态、行为任务及 FOG 自动检测等方向进行迭代检索。优先核对原始论文的 PMID、DOI、摘要和可获得的全文，区分实际冻结、冻结易感性、静息表型以及刺激疗效。通过证据矩阵、反例分析和因果推断约束开展综合。

**结果：** 人体研究显示：部分实际 FOG 伴随 STN beta/theta 增强，但另一些研究发现局部 beta 不变、皮层—STN 低频解耦，或在冻结易感状态下 beta 降低。长 beta burst、神经信号熵、步态相位调制、STN 功能亚区和跨网络耦合提供了超越平均功率的解释。低频及方向性 STN-DBS 对特定患者有益，但疗效具有明显异质性。2026 年多中心随机研究未证明 STN+SNr 联合刺激总体优于优化 STN 刺激；同期的 Meta 分析也存在方法和结论分歧。[R1–R8, R18, R22, R24–R26, R28, R29]

**结论：**

> **最能被现有证据支持的结论不是“FOG 由 STN beta 增强引起”，而是“FOG 涉及状态依赖、频率依赖、空间依赖及时间依赖的皮层—基底节—脑干步态控制失稳”。**

STN 可能在不同 FOG 亚型及不同发作阶段表现为运动阻断执行节点、网络状态转换节点或异常活动的下游读出。现有证据尚不足以确认其中任何一种为普遍机制。下一阶段研究应通过同一患者内的时间分辨记录、主动停止对照、严格药物分型，以及神经标志物锁定的随机干预区分这些模型。

---

## 一、研究范围、概念与证据方法

### 1.1 FOG 的定义

FOG 的核心临床特征是患者试图迈步，但无法产生有效步伐。2026 年国际 FOG 联盟更新定义，进一步规范了临床诊断和视频标注，并强调区分 akinetic freezing、kinetic trembling 及其他运动不成功的冻结表现。[R56]

以下现象不应自动视为同一终点：

| 现象 | 本文如何归类 | 与 FOG 的关系 |
|---|---|---|
| 视频确认的真实步行冻结 | 实际 FOG | 最直接的发作证据 |
| 原地踏步中的冻结 | 步态替代任务 FOG | 具有较高相关性，但缺乏完整位移及负重特征 |
| 虚拟现实中的脚步停顿 | 虚拟冻结/运动阻断 | 神经机制线索，不能与真实冻结完全等同 |
| 惯性传感器 iFOG 升高 | 冻结候选指标或易感程度 | 需与人工视频验证 |
| FOG-Q/NFOG-Q 升高 | 临床表型或回顾性严重程度 | 不能确定神经活动发生的具体时间 |
| 主动停止行走 | 负对照 | 用于检验 FOG 特异性 |
| 一般步幅缩短或运动迟缓 | 非特异性步态障碍 | 可与 FOG 共存，但不等价 |

这一区分决定了研究之间是否真正具有可比性。

### 1.2 多巴胺相关亚型

本文将 FOG 至少划分为四种：

- **OFF-FOG：** 多巴胺能药物不足时出现，服药后减轻。
- **ONOFF-FOG：** 充分药物起效后仍持续存在。
- **ON-FOG：** 药物作用期间新出现或明显加重。
- **Biphasic FOG：** 药物作用过程中呈现非单调、双相反应。

这些表型有临床研究支持。[R41–R43]

需要特别强调：ONOFF-FOG 不是左旋多巴诱发 FOG。前者是药物无法消除冻结；后者是药物本身使冻结加重。

### 1.3 研究检索与核验

本研究采用了以下检索方向：

| 研究方向 | 主要检索对象 |
|---|---|
| STN 局部活动 | LFP、single unit、multi-unit、beta、theta、alpha、gamma |
| 动态神经编码 | beta burst、sample entropy、gait-cycle locking、interhemispheric asymmetry |
| 网络电生理 | cortex-STN coherence、ECoG、EEG、M1、SMA、pre-SMA、S1 |
| 临床干预 | 60/130 Hz、低/高频 DBS、directional DBS、STN+SNr、adaptive DBS |
| 脑干系统 | PPN、CuN、MLR、brainstem locomotor circuits |
| 表型与替代机制 | levodopa response、dual task、cognitive conflict、sensorimotor integration |
| 证据质量 | FOG annotation、automatic detection、cross-validation、meta-analysis |

通过 PubMed/PMC、出版社原始页面、开放全文及 DOI 信息交叉核对候选文献。保留能确认真实存在、且具有 PMID 或 DOI 的研究。

**核验规则：**

1. 记录发表年份、正式发表版本和主要研究设计。
2. 区分患者数、试次数、电极触点数、冻结事件数。
3. 同一队列的不同论文可以作为不同分析证据，但不能重复累计独立患者。
4. 研究摘要不足以支持的具体数值不予补造。
5. 系统综述与 Meta 分析不能作为独立于其纳入原始研究的新实验样本。
6. 对无法确认独立性的研究，保留潜在队列重叠警示。

本文为广覆盖研究综述，不把搜索到的文献数等同于穷尽全部相关文献。

### 1.4 证据知识分层

| 层次 | 结构化表示 | 示例 |
|---|---|---|
| 原始文献 | `references` | [R8] 2019 年 Brain 原始研究 |
| 单项研究证据 | `evidence` | [R8] 冻结前皮层—STN 低频耦合下降 |
| 单项发现 | `claims.level=finding` | STN beta 在某一特定条件下升高 |
| 跨研究综合 | `claims.level=synthesis` | beta 增强不是 FOG 的普遍必要条件 |
| 机制解释 | `claims.level=mechanism` | 步态状态转换时网络耦合失稳 |
| 待检验研究假说 | `hypotheses` | 相位编码失稳模型及其证伪条件 |

任何一层都不能自动升级到下一层。特别是，**能预测 FOG 的信号不一定造成 FOG；能改善 FOG 的刺激也未必通过改变该信号发挥作用。**

---

## 二、STN 神经活动与 FOG 的核心直接证据

### 2.1 证据矩阵

| 文献 | 人群与实验 | 主要神经发现 | 对机制的约束 |
|---|---|---|---|
| [R31] Singh，2013 | 6 名 PD；跑步机，3 名有严重冻结/犹豫 | Freezer 行走时约 12–22 Hz 低 beta 增强或正常抑制不足 | 支持异常低 beta 与步态障碍相关 |
| [R32] Toledo，2014 | 22 名 PD；14 FOG、8 非 FOG；STN 与皮层记录 | FOG 组静息高 beta 22–35 Hz 更强；左旋多巴可降低 | 表型相关，不证明发作触发 |
| [R1] Syrkin-Nikolau，2017 | 14 名 PD，8 Freezer；OFF 药物、OFF DBS，自由行走 | Freezer 未冻结行走时 beta 更低、beta entropy 更高；实际冻结时 alpha entropy 更高 | 反对简单持续 beta 增强模型 |
| [R33] Storzer，2017 | 13 名 PD；行走与骑车 | Freezer 运动时可出现约 18 Hz 狭窄 beta 增强，未必发生冻结 | 区分运动相关异常与实际 FOG |
| [R34] Anidi，2018 | 12 名 PD；慢性 STN LFP、行走、原地踏步、DBS | Freezer 存在更长 beta burst；60/140 Hz 刺激缩短长 burst 并改善步态 | 支持时间持续性的重要性 |
| [R2] Chen，2019 | STN LFP、单/双任务行走 | 低 beta 15–21 Hz 与 theta 5–8 Hz 和 FOG 易感指标相关 | 主要反映易感性，不等于发作 |
| [R3] Georgiades，2019 | 8 名 PD；术中微电极、虚拟步态冻结 | 冻结时 STN 多单位活动及 theta/beta 振荡增强 | 支持运动阻断相关异常活动 |
| [R8] Pozzi，2019 | 7 名 PD；自由行走、慢性 STN LFP、皮层记录 | 局部 beta 和 burst 持续时间无一致性变化；皮层—STN 4–13 Hz 解耦 | 构成局部 beta 必要性模型的反例 |
| [R5] Liu，2022 | 8 名 PD；ECoG、STN LFP、TUG | 冻结期 STN beta 增强；高 beta/gamma 相干性异常 | 支持局部活动与网络耦合共同变化 |
| [R4] Gulberti，2023 | 12 名 PD；术中 STN/SN 微电极、仰卧踏步 | 踏步时 beta 下降，冻结时增加；STN/SN 神经元任务调制不同 | 支持运动阶段和核团分工 |
| [R30] Georgiades，2023 | 8 名 PD；虚拟双任务、STN 微电极 | 认知冲突诱发运动异常时 theta 降低，伴短暂放电率增加 | 早期认知调制与冻结期活动可能不同 |
| [R37] Klocke，2024 | 实际行走冻结；STN LFP、EMG、运动学 | 冻结前 STN—下肢肌肉耦合改变；拮抗肌协调障碍 | 将网络信号连接到最终运动输出 |
| [R7] Fim Neto，2025 | 23 名 PD；静息 STN LFP | FOG 患者 alpha 功率/burst 较高；高 beta burst 幅度与严重程度相关 | 可能是慢性表型标志，而非发作信号 |
| [R6] Collomb-Clerc，2025 | 38 名 PD；步态启动、STN 空间定位、药物 ON/OFF | 临近冻结时低 beta—步态关系失调，高 beta—步态关系重组 | 提示空间与行为变量之间的映射失稳 |
| [R25] Zhuang，2026 | 同步皮层—STN LFP 与真实步态周期 | FOG 易感行走中的 S1/SPL 低 beta 相位调制异常；DBS 和左旋多巴可改变部分异常 | 支持步态周期分析而非整段平均 |
| [R26] Simpson，2026 | 14 名 PD；STN LFP、下肢 EMG、药物状态 | 踏步和左旋多巴对低 beta/高 beta 的作用方向不同 | 不能将整个 beta 频段视为单一生理过程 |

这些研究的一个共同特点是：很多样本仅有个位数到十余名患者。对实际 FOG 的事件对齐结果，需要尤其重视患者级重复性，不能因为一个患者发生大量冻结就认为具有相同数量的独立证据。

主要原始研究资料可核对：[R1–R8, R25, R26, R31–R34]。<Cite refs={["turn301639search3","turn301639search10","turn301639search9","turn301639search1","turn702648search5","turn301639search5","turn261439search0","turn261439search8","turn261439search2"]}/>

### 2.2 低 beta、高 beta 与 theta：方向不一致

现有发现不能被合并为“STN 振荡增强”一个指标。

**低 beta（约 12–22 Hz）：** [R2]、[R31]、[R33] 支持其与异常行走或 FOG 易感性有关，但 [R1] 中 Freezer 的广义 beta 功率反而更低。[R26] 进一步说明正常踏步过程中某些低 beta 活动本来就可以增强。

**高 beta（约 21–35 Hz）：** [R32] 发现其与 FOG 表型及左旋多巴反应有关，[R7] 发现其 burst 幅度与临床严重程度相关。但 [R8] 未发现实际冻结期间存在一致的局部 beta 增强。

**Theta（约 3–8 Hz）：** [R2]、[R3] 观察到 theta 与冻结易感或冻结有关；[R30] 却发现认知负荷导致冻结或严重减慢时 theta 降低。

这些结果说明，振荡活动必须至少同时标记：

- 具体频段及其上下限。
- 神经组织来源。
- 行为任务。
- 药物与刺激状态。
- 比较对象。
- 相对冻结事件的时间。
- 绝对功率、相对功率、burst 或相干性等不同指标。

尤其不能把“皮层 beta 下降”直接写成“STN beta 下降”，也不能把 theta 功率和 theta 相干性视为同一变量。

### 2.3 直接 FOG 与 FOG 易感性的根本差异

FOG 易感性可能反映网络的长期不稳定倾向，而实际发作反映某一次运动状态转换失败。

两者之间可能存在如下关系：

**慢性易感性 → 任务触发下神经控制负荷升高 → 瞬时网络失稳 → 无效迈步 → 运动恢复。**

但目前这条链中的每一个箭头都不能视为已经证明的因果关系。

一个研究发现 Freezer 静息高 beta，并不要求同一患者冻结前高 beta 必须再次增强；同样，Freezer 未冻结时 beta 较低，也不能直接证明其冻结发生时仍然较低。

---

## 三、冲突分析：哪些是真矛盾，哪些是方法差异？

### 3.1 “FOG 时 beta 增强”与“FOG 时 beta 不变”

最直接的对比是 [R3]、[R5] 与 [R8]。

[R3] 在手术中虚拟步态冻结时发现 STN theta/beta 和多单位活动异常增加。[R5] 在真实 TUG 冻结期间发现 STN beta 功率升高。

与之不同，[R8] 在自由行走的 7 名患者中发现，冻结时 STN 局部 beta 功率及 beta burst 持续时间没有一致性显著变化，却出现皮层—STN 低频解耦，而且解耦能够区别于主动停止。

这三项研究对**局部 beta 变化的结果方向确实不同**。

可能来源包括：

| 来源 | 具体问题 | 预期影响 |
|---|---|---|
| 实验生态效度 | 虚拟步态、TUG、自由行走是否调用相同运动控制系统？ | 虚拟运动阻断可能更受认知冲突影响 |
| 神经测量尺度 | 微电极多单位活动与慢性宏电极 LFP | 放电率、局部同步和群体输入可能不一致 |
| 事件时间窗 | 冻结发生瞬间与整段冻结 | 瞬时增强可能被平均稀释 |
| 行为对照 | 非冻结行走、成功通过门口、主动停止 | 能否区分一般停止与异常冻结 |
| 频段分组 | 合并 beta 与低/高 beta 分开 | 可能使相反方向的活动抵消 |
| 药物状态 | OFF、ON、不同 DBS washout | 改变网络基线与冻结亚型 |
| 统计层级 | 按患者还是按事件检验 | 可能产生伪重复与夸大确定性 |

**综合结论 C：** STN beta 增强可以伴随部分冻结事件，但“局部 beta 必然增强”已受到反例限制。

仍然可能成立的是一个较弱模型：某些 FOG 亚型或发作阶段具有病理性 beta 同步，但这种同步并非所有冻结事件的必要条件。

### 3.2 Theta 增强与 theta 降低

[R3] 发现冻结期间 theta 增强，[R30] 发现认知提示导致运动异常时 theta 减弱。

有两种主要解释。

第一种是**不同阶段假说**：认知线索之后发生 theta 调节不足，运动控制失败之后出现异常 theta 同步。第二种是**不同病理亚型假说**：有些冻结由认知控制不足主导，另一些由运动阻断主导，因此 theta 方向不同。

这两种解释在跨研究比较中都成立，但它们提出不同预测：

- 阶段假说要求在同一患者、同一冻结事件中观察到先下降后增强的时间序列。
- 亚型假说要求 theta 变化方向在患者内部相对稳定，却随诱发任务或疾病表型分组而不同。

目前没有充分的同一患者内实验完成这一关键区分。

### 3.3 PPN alpha 降低与异常 alpha 增强

早期 PPN 记录 [R46] 发现，较高 alpha 活动与较好的行走表现相关，冻结时 alpha 降低。

然而，2026 年 Yeche 等 [R59] 同步记录 4 名药物抵抗性 FOG 患者的 PPN 和 CuN，并使用步态启动运动学精确对齐神经活动。研究发现：

- CuN alpha 活动在预期姿势调整（APA）前增加，与步伐节律相关。
- PPN beta 在姿势调整期间去同步化，随后出现与迈步相关的 alpha 调制。
- 38 次最终发生 FOG 的试次相比 115 次非 FOG 试次，出现了时间失配、过强的 MLR alpha 同步及异常 PPN beta 调制。
- CuN 刺激改善了部分步态节律指标，而 PPN 刺激对前向推进可能不利。

这与“所有 PPN/MLR alpha 下降都会导致冻结”这一简单模型不一致。[R59] <Cite ref="turn810618search0"/>

可能的解释是：**alpha 信号的空间来源和出现时机，比其总体强度更重要。**

因此，PPN/CuN 的证据进一步支持对 STN 研究同样适用的原则：不能把有益的生理性同步和错误时间出现的病理性同步混为一谈。

不过 [R59] 只有 4 名患者，且与既往 PPN/CuN 研究可能存在研究平台与患者来源关联；尚不足以独立建立新的普遍机制。

### 3.4 研究冲突的一个核心统计原因：错误的比较对象

建议今后每篇论文都明确使用以下对比编码：

| 对比编码 | 实际比较 | 允许的解释 |
|---|---|---|
| B1 | Freezer vs Non-Freezer，静息 | 表型差异 |
| B2 | Freezer vs Non-Freezer，非冻结行走 | 步态易感状态差异 |
| B3 | 同一患者行走 vs 静止 | 运动状态调制 |
| B4 | 同一患者 FOG vs 非 FOG | 发作关联 |
| B5 | FOG 前 vs 主动停止前 | 冻结特异性候选信号 |
| B6 | DBS/药物 ON vs OFF | 干预相关变化 |
| B7 | 不同 DBS 模式随机比较 | 刺激参数对结果的因果影响 |
| B8 | 标志物锁定刺激 vs 匹配随机刺激 | 更接近特定神经标志物的机制检验 |

在此前研究中，B1、B2 和 B4 经常被统一表述为“FOG 相关活动”，这造成了许多表面矛盾。

---

## 四、DBS 干预证据：能够证明什么？

### 4.1 低频与高频 STN-DBS

| 文献 | 设计 | 结果 |
|---|---|---|
| [R9] Moreau，2008 | 13 人；盲法比较 60、130 Hz 与 OFF | 等能量低频条件减少冻结；部分高电压高频条件加重冻结 |
| [R10] Xie，2012 | 2 例新启用 DBS 后即出现 FOG | 保持其他参数不变，130→60 Hz 后迅速缓解 |
| [R11] Phibbs，2014 | 20 人；随机盲法比较 | 60 Hz 未改善主要步幅终点，震颤控制较差 |
| [R12] Khoo，2014 | 随机双盲交叉 | 优化触点后的 60 Hz 改善轴性运动指标，最佳触点更腹侧 |
| [R13] Xie，2015 | 7 名顽固性 FOG 患者；随机双盲 | 60 Hz 相比 130 Hz 改善 FOG 和吞咽相关指标 |
| [R14] Xie，2018 | 11 名基线、10 名长期随访 | 60 Hz 的部分 FOG 获益持续至平均约 14.5 个月，但效应减弱 |

这些试验不能用简单的阳性研究数与阴性研究数投票。

[R11] 没有专门选择在高频刺激下仍持续冻结的患者，[R13] 则特意选择这类患者。此外，不同研究对刺激总能量、触点和幅度的处理不同。[R9–R14] <Cite refs={["turn702648search3","turn702648search1","turn702648search0","turn118244search2","turn702648search4"]}/>

更可靠的综合是：

**60 Hz 可以是特定患者 FOG 的有效刺激选择，但其疗效不能只归因于频率；更不能推导为低频 STN-DBS 普遍优于高频。**

### 4.2 刺激空间位置比单纯频率更复杂

空间连接研究形成了三个主要发现：

- [R19]：与运动、额叶、苍白球及脑干相关的连接可能预测 FOG 改善。
- [R20]：右侧前额叶网络募集较强与较差的 FOG 结局相关，而感觉运动网络募集与改善相关。
- [R21]：回顾性 sweet spot 分析提示背外侧 STN 及 SMA/pre-SMA/PPN 相关连接可能有利，但特定腹侧或邻近区域可能不利。

2025 年的随机双盲方向性刺激研究 [R22] 在 10 名严重 FOG 患者中发现，中央 STN 定向刺激优于后部感觉运动 STN 定向刺激，冻结事件也更少。

[R23] 在 98 人的回顾性概率映射中发现，术后步态恶化与更腹侧的刺激位置有关。

这些结果共同说明 STN 不应作为空间同质结构分析，但还不足以产生一张对所有患者适用的精确刺激地图。[R19–R23] <Cite refs={["turn407744search6","turn810892search2","turn810892search1","turn810892search0","turn407744search2"]}/>

此外，[R22] 的中央 STN 获益并不意味着 [R21] 所识别的所有非背外侧区域都有利。两项研究的空间比较、刺激范围及结局指标并不完全一致。

### 4.3 STN+SNr 联合刺激

2013 年 Weiss 等的随机交叉研究 [R15] 在总体轴性主要终点上阴性，但 FOG 次要终点提示潜在获益。

2025 年 Artusi 等 [R16] 报告主要 FOG 终点未达到显著差异，但存在可能的应答亚群。同年的 Tan 等 [R17] 报告联合刺激优于单纯 STN 刺激。

**最新关键随机证据 [R18]：**

2026 年 10 月发表的探索性多中心随机双盲研究纳入 45 名进入改良意向治疗分析的患者：

- 优化 STN-DBS：23 人。
- STN+SNr：22 人。
- 随访 90 天。
- 主要终点 FOG-AC。

两组主要终点差异不显著，P=0.692。达到临床有意义改善的患者分别为 7 人和 8 人。联合刺激的响应可能与较短病程有关，但属于探索性分析。

因此，不能把 STN+SNr 视为已经确立的 FOG 标准强化方案。[R15–R18] <Cite refs={["turn702648search2","turn407744search5","turn407744search3","turn407744search0"]}/>

### 4.4 两项 Meta 分析的冲突

2026 年两项 Meta 分析给出不同结果：

| 指标 | [R28] Kong | [R29] Haq |
|---|---:|---:|
| FOG 总效应 | Hedges' g = −0.23 | SMD = −0.39 |
| 95% CI | −1.04 至 0.59 | −0.73 至 −0.04 |
| 异质性 | I² = 85.6% | I² = 23.2% |
| 结论 | 未证实额外获益 | 报告统计学优势 |

重要的方法学差异包括：

- 原始试验纳入时间和范围。
- 交叉设计的配对数据处理。
- 同一研究多个刺激条件之间的相关性。
- 不同 FOG 终点的标准化方式。
- 效应量较大研究的权重。
- 共享对照条件是否得到恰当处理。

[R28] 对研究内相关性进行了显式处理，并将其 FOG 结论评为极低确定性。[R29] 采用了平行组近似并报告显著效应。

**这两项 Meta 分析不能视为两项独立随机验证，更不能用其中一篇的显著 P 值覆盖另一篇的结果。** 它们是对部分相同原始研究采用不同分析方案后的结果。[R28, R29] <Cite refs={["turn798145view3","turn407744search7"]}/>

下一次规范更新需要患者内配对差值或合理的相关性敏感性分析，并纳入 2026 年 10 月的 [R18]。

### 4.5 Beta burst 自适应 DBS

2025 年 Wilkins 等 [R24] 在 7 人中研究基于 STN beta burst 持续时间的实时自适应刺激。

研究证明该方案技术上可行，并观察到步态获益，但没有证明该方式在主要冻结比较中优于连续刺激或随机间歇调制。

因此：

- beta burst 可以成为控制系统输入。
- 闭环刺激可以改善运动表现。
- 但尚未证明 beta burst 是 FOG 的特异性因果介质。

这是**预测价值、控制价值和病因价值之间必须分开的典型实例**。[R24] <Cite ref="turn407744search4"/>

---

## 五、STN 之外的网络证据

### 5.1 认知控制与环境诱发

[R39] 通过虚拟现实实验显示，FOG 患者对认知冲突、狭窄门口和环境线索转换特别敏感。[R38] 的功能影像研究支持认知控制网络与基底节之间存在异常协调。

2026 年 Tian 等 [R50] 在 18 名 FOG 患者中，比较冻结与主动停止前两秒的 EEG 网络活动，发现冻结前局部 beta 网络连接增强及部分低频长距离连接减弱。

这些发现支持认知—运动网络失稳，但 BOLD/EEG 不能直接当作 STN 神经元的记录。[R38, R39, R50]

### 5.2 STN—SNr—脑干系统

STN 通过基底节输出网络影响脑干步态控制。PPN 与 CuN 是相关脑干系统的重要组成部分，但并非功能相同的单一靶点。

PPN alpha 与行走表现的关联 [R46]、药物对 PPN 频谱和冻结的同步影响 [R58]，以及 CuN/PPN 相位调制研究 [R59]，均支持脑干系统参与步态控制。

不过，干预结果明显不一致：

- [R44]：PPN 刺激在某些长期冻结指标中有潜在获益，双盲阶段未建立稳定疗效。
- [R45]：5 人前瞻性研究报告部分持续获益。
- [R49]：9 人随机交叉研究提示较低频 PPN 刺激在部分患者中更好。
- [R47]：6 人 PPN/CuN 随机双盲试验，主要终点阴性。
- [R48]：相同队列长期随访未证实稳定临床获益。
- [R59]：4 人研究发现 CuN 和 PPN 的步态作用不同，刺激效果也不一致。

因此，**脑干系统参与 FOG 的证据强于“直接刺激某一个脑干核团就能可靠解除冻结”的证据。**

### 5.3 下肢肌肉协调与感觉反馈

[R37] 同时记录 STN、下肢肌肉和运动学，发现冻结前 STN—肌肉耦合异常，并伴随拮抗肌协同失效。

这提供了从神经活动到实际运动输出的候选机制链，但并不能确定异常信号是下降运动指令，还是异常肌肉活动导致的上行感觉反馈。

[R40] 的 STN 功能连接研究进一步提示，药物反应性不同的 FOG 涉及不同感觉—运动网络。胆碱能 PET 研究 [R53] 则支持 PD 步态和平衡障碍具有超出多巴胺系统的神经基础。

这些方向说明，即使发现 STN 信号发生改变，也需要认真考虑共同病因及代偿性改变。

---

## 六、六个竞争性机制模型

下面的模型刻意采用较强的形式，确保可以通过实验区分，而不是让所有结果都被解释为“网络异常”。

### H1：STN 病理性 beta 同步导致运动阻断

**机制：** 在运动状态需要切换时，STN 的低 beta 或异常长 beta burst 造成过度稳定的运动抑制状态，妨碍生成有效迈步。

**主要证据：** [R3]、[R5]、[R31]、[R34]。

**最强反例：** [R1]、[R8]；[R24] 未证实专门追踪 beta burst 的刺激优于匹配对照。

**可区分预测：**

- 冻结前应有高于正常行走和主动停止的长 beta burst 占用时间。
- 若该活动是真正介质，对其进行提前、选择性干预应减少 FOG。
- 临床改善程度应与病理 beta 活动的变化相对应。

**证伪条件：** 在预先指定的 FOG 亚型、记录位点和时间窗中，大量可确认的冻结没有相应 beta 异常；或者有效消除目标异常后，冻结概率不发生预期下降。

**状态：** 有支持，但强形式受到反证约束。

### H2：步态周期相位编码失稳

**机制：** STN 及相关皮层区域不能在正确的姿势调整、支撑相或摆动相生成适当的神经活动。问题不一定是振荡过强，而可能是正确活动出现于错误时间。

**主要证据：** [R6]、[R25]、[R26]、[R35]、[R36]、[R59]。

**预测：**

- 步态周期对齐的神经指标应比整段平均功率更能预测实际冻结。
- 冻结前可观察到 beta/theta 相位调制减弱、时序漂移或错误相位的同步增强。
- 相位锁定刺激应优于脉冲数及总刺激负荷匹配的随机刺激。

**证伪条件：** 控制步速、步幅和步态阶段后，相位特征不再具有独立预测价值，且针对相位的干预不优于相应匹配对照。

**状态：** 生理基础较强，针对 FOG 的特异性因果验证不足。

### H3：认知控制不足—运动阻断的双阶段模型

**机制：** 冲突、门口或双任务先导致控制信号募集失败，随后异常 STN 抑制/同步活动参与运动阻断。

**主要证据：** [R3]、[R30]、[R38]、[R39]。

**预测：**

- 冲突线索之后首先出现任务相关 theta 调制不足。
- 真正冻结开始附近随后出现 STN 放电或某些振荡活动异常增强。
- 同一人的成功双任务试次不应出现完整的异常双阶段序列。

**证伪条件：** 在足够的同一人冻结事件中，两个阶段的先后关系不稳定，或在控制普通认知错误与运动迟缓后不具备 FOG 特异性。

**状态：** 能解释 theta 结果冲突，但尚未经完整的同一实验验证。

### H4：皮层—STN 网络解耦

**机制：** 步态状态转换依赖多个网络之间的动态通信，FOG 发生于某些必要的跨区域耦合关系突然瓦解。

**主要证据：** [R8]、[R38]、[R50]，以及 [R5] 所显示的其他频段耦合异常。

**预测：**

- 冻结前低频皮层—STN 耦合异常比 STN 局部功率更稳定。
- 这种变化能够区别 FOG、主动停止和普通运动减慢。
- 恢复适当跨网络时序的干预应改善 FOG。

**证伪条件：** 在控制共同输入、速度、运动伪迹及非平稳信号影响后，解耦现象消失；或针对该耦合的干预改变了信号却不能改变冻结。

**状态：** 具有重要的直接人体证据，但信息流方向和必要性未定。

### H5：STN—SNr—MLR 输出门控失灵

**机制：** STN 的异常活动通过基底节输出系统影响 SNr、PPN/CuN 及下降运动控制通路，使计划中的步态转换无法转化为有效肌肉活动。

**主要证据：** [R15–R23]、[R37]、[R44–R49]、[R58]、[R59]。

**预测：**

- 具有特定 SNr/MLR 纤维连接模式的患者更可能对相应网络刺激有反应。
- STN、脑干活动及拮抗肌控制变化之间存在可重复的时间次序。
- 精准通路刺激应该比单纯依靠解剖核团中心的刺激更具特异性。

**证伪条件：** 在确认刺激实际募集目标通路的前提下，通路调节既不能改变预测的生理中介，也不能改变冻结。

**状态：** 网络解剖合理，部分干预有支持，但群体治疗效应仍有争议。

### H6：STN 信号主要是共同失稳的读出或代偿反应

**机制：** FOG 主要起始于皮层感觉—运动整合、注意控制、脑干或脊髓系统。STN 活动随网络状态变化，并非所有冻结的关键致病节点。

**主要证据：** [R1]、[R8]、[R24]、[R40]、[R50]、[R53]、[R59]。

**预测：**

- STN 信号可能具有预测能力，但特异性地改变它不一定比非特异刺激有效。
- 某些皮层、脑干或肌肉协调异常可能早于 STN 信号变化。
- FOG 不同亚型可能具有不同的主要致病网络。

**证伪条件：** 在适当控制其他网络变化后，证明 STN 某一特定信号对某一 FOG 亚型具有稳定的必要性，并通过选择性干预确认其因果中介作用。

**状态：** 必须保留的竞争性替代解释；并非已验证机制。

### 模型之间真正有区分力的比较

| 实验观察 | 较符合的模型 | 受到限制的模型 |
|---|---|---|
| 局部 beta 不变，冻结前低频跨网络解耦 | H4、H6 | 强形式 H1 |
| 先 theta 下降、后 beta/放电异常增强 | H3 | 单阶段统一振荡模型 |
| 相位锁定刺激明显优于等负荷随机刺激 | H2 | 纯平均功率模型 |
| 只有特定脑干纤维募集可改善 FOG | H5 | 与空间无关的 STN 局部模型 |
| STN 生物标志物改变，却未出现相应 FOG 改善 | H6 或非介质性标志物模型 | 对应强因果模型 |
| 相同 FOG 表型存在多种互不相同的神经特征 | H6 或多亚型机制 | 单一普遍机制 |

必须注意：**多个模型可能共同作用。** 这里的竞争性不是声称 H1–H6 在生物学上完全互斥，而是通过预先指定的必要性、时间顺序、交互作用和干预中介预测来形成真正可检验的差异。

---

## 七、优先推荐的判别性研究

### 7.1 总体设计

建议采用两阶段、多中心、患者内重复随机的机制试验。

**第一阶段：自然步态观察及标志物发现。**

在同一患者中同步记录：

- 双侧 STN LFP。
- 适合的皮层 EEG/ECoG（取决于临床植入与安全条件）。
- 下肢拮抗肌 EMG。
- IMU、足底压力和同步视频。
- 精确的药物时间、剂量及 DBS 参数。

采用多种冻结诱发任务：步态启动、直线行走、360° 转身、通过门口、双任务和障碍物任务。

主动停止必须作为预先指定的负对照。

按照新 FOG 定义进行双盲视频标注。自动检测只用于辅助，不作为未经验证的唯一金标准。[R54–R57]

**第二阶段：预先锁定标志物的干预检验。**

在第一阶段结束后锁定模型，不在测试数据上重新选择最佳频段或阈值。

随机比较：

- Beta burst 触发刺激。
- 步态相位触发刺激。
- 网络异常触发刺激（只有在实时可靠测量可行时实施）。
- 连续 DBS。
- 与各闭环模式刺激负荷相匹配的随机时序刺激。

具体刺激参数必须由临床安全范围、设备能力及独立伦理审查决定；研究不应假定提高刺激强度就能更好地验证机制。

### 7.2 主要终点

首要临床终点应采用视频确认的实际冻结事件，而不是仅以 FOG 问卷替代：

1. 每单位有效暴露时间的冻结发生率。
2. 冻结时间百分比。
3. 每次冻结的持续时间。
4. 冻结前预警的灵敏度、误报率及提前量。
5. 非冻结行走时的步态性能和刺激副作用。

每项终点需要预先规定优先级和多重比较策略。

### 7.3 统计结构

数据至少具有四级相关结构：

**患者 → 访视/刺激阶段 → 行走试次 → 步态周期/冻结事件。**

因此，分析应采用适当的多层模型、广义混合模型或生存/重复事件模型，并考虑：

- 患者随机效应。
- 任务类型与药物亚型的交互作用。
- 刺激顺序及潜在 carryover。
- 同一人的重复冻结事件。
- 不同刺激模式的总负荷。
- 电极位置和有效刺激场。
- 运动伪迹、步速及运动幅度。
- 基于患者而非事件的交叉验证。

需要先由先导数据估计患者内和患者间效应方差，再进行功效分析；目前不能从既往小样本研究合理推导一个通用样本量。

### 7.4 关键判别：相关性与介导效应

仅观察到：

“刺激改变 beta，同时 FOG 改善”

不足以证明 beta 是治疗机制。

更强的证据应包括：

1. 干预确实改变了预先指定的神经标志物。
2. 标志物变化发生在运动行为改善之前。
3. 标志物变化程度与冻结改善存在合理的剂量—反应关系。
4. 具有相同总刺激负荷、但不匹配该神经标志物的刺激疗效更弱。
5. 预设中介分析在合理的未测量混杂假设下支持机制路径。

即使满足上述条件，也需要谨慎解释，因为 DBS 可以同时改变多个神经网络。

---

## 八、证据系统的自我审计与可持续更新

### 8.1 本次研究发现并纠正的问题

| 问题 | 审计前的风险 | 已实施的改进 | 复核结果 |
|---|---|---|---|
| 统一 beta 增高叙事 | 忽略反方向及阴性研究 | 纳入 [R1]、[R8]、[R26] | 强形式命题降级为 contested |
| 误把易感性当作实际冻结 | 错误扩大直接证据范围 | 对 [R2]、[R7]、[R32] 重新标记实验条件 | 表型关联与发作关联分离 |
| 重复计算患者 | 夸大独立研究支持度 | 标记预印本、正式论文、同一队列随访及潜在重叠 | 已明确 [R47]/[R48] 不是独立队列 |
| DBS 机制过度推断 | 治疗有效即认为其通过 beta 发挥作用 | 加入随机调制对照及中介判断标准 | [R24] 不再被解释为 beta 病因验证 |
| Meta 分析结论不一致 | 按显著性或发表时间选择结论 | 检查交叉试验依赖结构及效应异质性 | 保留 [R28]/[R29] 冲突，不强行合并 |
| FOG 自动标注不可靠 | 标注误差造成虚假神经特征 | 加入外部验证研究 [R54]、[R55] | 不把模型检测率当作机制证据 |
| 新脑干证据遗漏 | 将 PPN/CuN 视为单一功能节点 | 纳入 2026 年原始研究 [R59] | 更正“FOG 必须伴随 MLR alpha 降低”的过强解释 |

本次完成的是**证据结构和推断逻辑的改进与交叉核验**，不是通过新临床数据证明某一机制模型更准确。

### 8.2 应建立的长期证据维护规则

每条证据以 `eid` 作为可追溯最小单位，文献以 `ref` 去重，跨研究结论以 `cid` 保存，竞争性假说以 `hid` 保存。

当出现新研究时：

- 如果新研究支持旧结论，增加证据链接，但不自动提高确定性。
- 如果新研究直接反驳必要性主张，将该结论标记为 contested 并重新限定适用范围。
- 如果新研究采用更严格的随机设计，应重新评价此前仅凭观察研究建立的因果主张。
- 如果发现样本重叠，须重新计算独立证据数量。
- 如果 FOG 定义、事件标注或分析频段改变，旧结果应按新标准重新审查可比性。
- 如果研究数据或摘要存在内部不一致，应保留原始不一致记录，待原作者澄清。

本研究的一个具体质量问题是：[R52] 的摘要与正文对冻结事件检测数量分别报告 24/29 和 24/30。附录保留该不一致，而不是未经核实就选取其中一个数字。

### 8.3 结构化附录的使用边界

附录中的 `status` 代表本研究对证据确定性的定性评价，不是通过 GRADE 全套程序独立计算的正式评级。

`relation=contradicts` 表示某研究对特定主张构成限制或反例，不意味着两个研究在所有实验条件下绝对互斥。

对于没有足够信息判断患者级独立性的研究，不能依赖附录将患者数简单相加。

---

## 九、最终综合结论

### 9.1 可以较有把握保留的结论

STN 参与步态的运动执行、状态转换及神经信息编码。STN 的振荡活动具有明显的运动、药物、时间及空间依赖性。[R4, R6, R26, R35, R36]

部分 FOG 与 STN beta/theta 增强相关，但不存在可靠证据表明所有 FOG 都需要局部 beta 增强。[R1–R8, R30–R34]

FOG 与皮层—STN、STN—脑干及感觉—运动网络之间的异常协调有关。该结论作为跨研究综合具有支持，但各网络的具体因果方向尚未确定。[R8, R25, R37, R38, R50, R59]

DBS 可以改善或加重 FOG，刺激频率、触点位置、募集的纤维网络和患者临床亚型都会改变干预效果。[R9–R24]

### 9.2 尚不能成立的强主张

目前不能声称：

- STN beta 增强是所有 FOG 的必要或充分原因。
- STN theta 的某一个固定变化方向能够统一解释 FOG。
- 某个 STN 亚区是所有 FOG 的最优刺激位置。
- 60 Hz STN-DBS 普遍优于 130 Hz。
- STN+SNr、PPN 或 CuN 刺激具有已经确立的普遍额外疗效。
- 高性能 FOG 检测算法已经证实其使用的神经特征具有因果意义。

### 9.3 最值得优先研究的方向

综合现有证据，最有前景的是把以下三个维度结合，而不是继续孤立地测量平均 beta 功率：

**第一，状态转换。** 确认异常发生在认知冲突、步态启动、有效行走、冻结还是恢复阶段。

**第二，空间与网络。** 确认异常来自 STN 的哪一亚区、哪一侧以及哪些皮层或脑干连接。

**第三，时间编码。** 确认是平均功率、burst 持续时间、步态相位耦合、跨网络同步，还是神经—肌肉时序出现异常。

最终需要解决的是：

**某一 STN 活动究竟是冻结的前置原因、参与放大过程的中介、患者尝试恢复运动时的代偿信号，还是整个步态网络失稳的伴随读出？**

这才是未来神经电生理研究和新型 DBS 机制试验需要真正区分的问题。

---

## 结构化附录：可追溯证据、结论与竞争性假说

以下 JSON 保留前述研究的原始编号。`references` 是文献身份层，`evidence` 是单项研究证据层，`claims` 是发现与综合判断层，`hypotheses` 是可检验机制层。空字符串表示未确认的信息，而非断言该信息不存在。

```json
{
  "references": [
    {
      "ref": "R1",
      "pmid": "28890315",
      "doi": "10.1016/j.nbd.2017.09.002",
      "title": "Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease",
      "year": 2017
    },
    {
      "ref": "R2",
      "pmid": "31494286",
      "doi": "10.1016/j.nbd.2019.104605",
      "title": "Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease",
      "year": 2019
    },
    {
      "ref": "R3",
      "pmid": "31665229",
      "doi": "10.1093/brain/awz325",
      "title": "Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing",
      "year": 2019
    },
    {
      "ref": "R4",
      "pmid": "36730026",
      "doi": "10.1093/brain/awad006",
      "title": "Subthalamic and nigral neurons are differentially modulated during parkinsonian gait",
      "year": 2023
    },
    {
      "ref": "R5",
      "pmid": "35310098",
      "doi": "10.3389/fnins.2022.795417",
      "title": "Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait",
      "year": 2022
    },
    {
      "ref": "R6",
      "pmid": "40709562",
      "doi": "10.1002/ana.70003",
      "title": "Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease",
      "year": 2025
    },
    {
      "ref": "R7",
      "pmid": "39884164",
      "doi": "10.1016/j.clinph.2025.01.005",
      "title": "Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease",
      "year": 2025
    },
    {
      "ref": "R8",
      "pmid": "31505548",
      "doi": "10.1093/brain/awz141",
      "title": "Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics",
      "year": 2019
    },
    {
      "ref": "R9",
      "pmid": "18420482",
      "doi": "10.1212/01.wnl.0000303972.16279.46",
      "title": "STN-DBS frequency effects on freezing of gait in advanced Parkinson disease",
      "year": 2008
    },
    {
      "ref": "R10",
      "pmid": "22696586",
      "doi": "10.1136/jnnp-2011-302091",
      "title": "Effect of stimulation frequency on immediate freezing of gait in newly activated STN DBS in Parkinson's disease",
      "year": 2012
    },
    {
      "ref": "R11",
      "pmid": "24165197",
      "doi": "10.1111/ner.12131",
      "title": "60-Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation",
      "year": 2014
    },
    {
      "ref": "R12",
      "pmid": "24449169",
      "doi": "",
      "title": "Low-frequency subthalamic nucleus stimulation in Parkinson's disease: a randomized clinical trial",
      "year": 2014
    },
    {
      "ref": "R13",
      "pmid": "25540305",
      "doi": "10.1212/WNL.0000000000001184",
      "title": "Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD",
      "year": 2015
    },
    {
      "ref": "R14",
      "pmid": "29654112",
      "doi": "10.1136/jnnp-2018-318060",
      "title": "Long-term effect of low frequency stimulation of STN on dysphagia, freezing of gait and other motor symptoms in PD",
      "year": 2018
    },
    {
      "ref": "R15",
      "pmid": "23757762",
      "doi": "10.1093/brain/awt122",
      "title": "Nigral stimulation for resistant axial motor impairment in Parkinson's disease? A randomized controlled trial",
      "year": 2013
    },
    {
      "ref": "R16",
      "pmid": "39957196",
      "doi": "10.1177/1877718X241292315",
      "title": "Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial",
      "year": 2025
    },
    {
      "ref": "R17",
      "pmid": "40760816",
      "doi": "10.1177/1877718X251359241",
      "title": "DBS-STN&SNr combined stimulation versus DBS-STN monotarget stimulation for Parkinson's disease freezing: A comparative efficacy study",
      "year": 2025
    },
    {
      "ref": "R18",
      "pmid": "42860886",
      "doi": "10.1002/mdc3.70813",
      "title": "Disease Duration Differentiates Freezing of Gait Response to Subthalamic and Nigral Stimulation for Parkinson's Disease in an Exploratory Multicenter Controlled Trial",
      "year": 2026
    },
    {
      "ref": "R19",
      "pmid": "35431262",
      "doi": "10.3233/JPD-212997",
      "title": "Structural Connectivity of Subthalamic Nucleus Stimulation for Improving Freezing of Gait",
      "year": 2022
    },
    {
      "ref": "R20",
      "pmid": "36242900",
      "doi": "10.1016/j.parkreldis.2022.10.002",
      "title": "Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients",
      "year": 2022
    },
    {
      "ref": "R21",
      "pmid": "37701817",
      "doi": "10.1093/braincomms/fcad238",
      "title": "Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease",
      "year": 2023
    },
    {
      "ref": "R22",
      "pmid": "39475137",
      "doi": "10.1002/ana.27099",
      "title": "Directional Subthalamic Deep Brain Stimulation Better Improves Gait and Balance Disorders in Parkinson's Disease Patients: A Randomized Controlled Study",
      "year": 2025
    },
    {
      "ref": "R23",
      "pmid": "40408848",
      "doi": "10.1016/j.parkreldis.2025.107871",
      "title": "Probabilistic mapping of gait changes after STN-DBS for Parkinson's disease",
      "year": 2025
    },
    {
      "ref": "R24",
      "pmid": "40677701",
      "doi": "10.1093/braincomms/fcaf266",
      "title": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease",
      "year": 2025
    },
    {
      "ref": "R25",
      "pmid": "42571859",
      "doi": "10.1016/j.nbd.2026.107571",
      "title": "Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease",
      "year": 2026
    },
    {
      "ref": "R26",
      "pmid": "41388789",
      "doi": "10.1093/brain/awaf464",
      "title": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping",
      "year": 2026
    },
    {
      "ref": "R27",
      "pmid": "35295883",
      "doi": "10.3389/fnhum.2022.812954",
      "title": "Combined Subthalamic and Nigral Stimulation Modulates Temporal Gait Coordination and Cortical Gait-Network Activity in Parkinson's Disease",
      "year": 2022
    },
    {
      "ref": "R28",
      "pmid": "42909654",
      "doi": "10.1007/s10072-026-09479-2",
      "title": "STN-SNr co-stimulation in Parkinson's disease: a systematic review and meta-analysis of motor and freezing-of-gait outcomes",
      "year": 2026
    },
    {
      "ref": "R29",
      "pmid": "42968793",
      "doi": "10.1136/bmjcsurg-2026-000033",
      "title": "Superiority of dual-target STN-SNr deep brain stimulation towards gait in Parkinson's disease: a meta-analysis and meta-regression of randomised trials",
      "year": 2026
    },
    {
      "ref": "R30",
      "pmid": "37226972",
      "doi": "10.1002/mds.29455",
      "title": "Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease",
      "year": 2023
    },
    {
      "ref": "R31",
      "pmid": "",
      "doi": "10.1016/j.baga.2012.10.002",
      "title": "Freezing of gait-related oscillatory activity in the human subthalamic nucleus",
      "year": 2013
    },
    {
      "ref": "R32",
      "pmid": "24361601",
      "doi": "10.1016/j.nbd.2013.12.005",
      "title": "High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease",
      "year": 2014
    },
    {
      "ref": "R33",
      "pmid": "28892573",
      "doi": "10.1002/ana.25047",
      "title": "Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia",
      "year": 2017
    },
    {
      "ref": "R34",
      "pmid": "30196050",
      "doi": "10.1016/j.nbd.2018.09.004",
      "title": "Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease",
      "year": 2018
    },
    {
      "ref": "R35",
      "pmid": "29760182",
      "doi": "10.1523/JNEUROSCI.3596-17.2018",
      "title": "Alternating Modulation of Subthalamic Nucleus Beta Oscillations during Stepping",
      "year": 2018
    },
    {
      "ref": "R36",
      "pmid": "36070366",
      "doi": "10.1126/scitranslmed.abo1800",
      "title": "Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease",
      "year": 2022
    },
    {
      "ref": "R37",
      "pmid": "39470410",
      "doi": "10.1093/brain/awae223",
      "title": "Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease",
      "year": 2024
    },
    {
      "ref": "R38",
      "pmid": "24142148",
      "doi": "10.1093/brain/awt272",
      "title": "Freezing of gait in Parkinson's disease is associated with functional decoupling between the cognitive control network and the basal ganglia",
      "year": 2013
    },
    {
      "ref": "R39",
      "pmid": "23831480",
      "doi": "10.1016/j.parkreldis.2013.06.002",
      "title": "Using virtual reality to explore the role of conflict resolution and environmental salience in freezing of gait in Parkinson's disease",
      "year": 2013
    },
    {
      "ref": "R40",
      "pmid": "38101024",
      "doi": "10.1016/j.parkreldis.2023.105952",
      "title": "Subthalamic functional connectivity associated with freezing of gait dopa-response",
      "year": 2024
    },
    {
      "ref": "R41",
      "pmid": "22262741",
      "doi": "10.1212/WNL.0b013e3182477ec0",
      "title": "\"On\" state freezing of gait in Parkinson disease: a paradoxical levodopa-induced complication",
      "year": 2012
    },
    {
      "ref": "R42",
      "pmid": "31799377",
      "doi": "10.1038/s41531-019-0099-z",
      "title": "Freezing of Gait can persist after an acute levodopa challenge in Parkinson's disease",
      "year": 2019
    },
    {
      "ref": "R43",
      "pmid": "32417798",
      "doi": "10.3233/JPD-201997",
      "title": "Biphasic Levodopa-Induced Freezing of Gait in Parkinson's Disease",
      "year": 2020
    },
    {
      "ref": "R44",
      "pmid": "19773356",
      "doi": "10.1093/brain/awp229",
      "title": "Effects of pedunculopontine nucleus area stimulation on gait disorders in Parkinson's disease",
      "year": 2010
    },
    {
      "ref": "R45",
      "pmid": "21725254",
      "doi": "10.1227/NEU.0b013e31822b6f71",
      "title": "Pedunculopontine nucleus stimulation improves gait freezing in Parkinson disease",
      "year": 2011
    },
    {
      "ref": "R46",
      "pmid": "22232591",
      "doi": "10.1093/brain/awr315",
      "title": "Alpha oscillations in the pedunculopontine nucleus correlate with gait performance in parkinsonism",
      "year": 2012
    },
    {
      "ref": "R47",
      "pmid": "34744048",
      "doi": "10.3233/JPD-212793",
      "title": "Pedunculopontine and Cuneiform Nuclei Deep Brain Stimulation for Severe Gait and Balance Disorders in Parkinson's Disease: Interim Results from a Randomized Double-Blind Clinical Trial",
      "year": 2022
    },
    {
      "ref": "R48",
      "pmid": "35121249",
      "doi": "10.1016/j.parkreldis.2022.01.010",
      "title": "Stimulation of the pedunculopontine and cuneiform nuclei for freezing of gait and falls in Parkinson disease: Cross-over single-blinded study and long-term follow-up",
      "year": 2022
    },
    {
      "ref": "R49",
      "pmid": "25185212",
      "doi": "10.1136/jnnp-2013-307511",
      "title": "Low-frequency versus high-frequency stimulation of the pedunculopontine nucleus area in Parkinson's disease: a randomised controlled trial",
      "year": 2015
    },
    {
      "ref": "R50",
      "pmid": "41760132",
      "doi": "10.1002/mds.70230",
      "title": "Aberrant Beta-Band Network Alteration Preceding Freezing of Gait in Parkinson's Disease",
      "year": 2026
    },
    {
      "ref": "R51",
      "pmid": "42778807",
      "doi": "10.1007/s00415-026-14149-6",
      "title": "Frequency-Specific EEG burst dynamics in Parkinson's Disease and freezing of gait",
      "year": 2026
    },
    {
      "ref": "R52",
      "pmid": "42239677",
      "doi": "10.3389/fneur.2026.1793291",
      "title": "An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease",
      "year": 2026
    },
    {
      "ref": "R53",
      "pmid": "39252998",
      "doi": "10.1093/braincomms/fcae286",
      "title": "Dynamic balance and gait impairments in Parkinson's disease: novel cholinergic patterns",
      "year": 2024
    },
    {
      "ref": "R54",
      "pmid": "",
      "doi": "10.1186/s12984-024-01320-1",
      "title": "Freezing of gait assessment with inertial measurement units and deep learning: effect of tasks, medication states, and stops",
      "year": 2024
    },
    {
      "ref": "R55",
      "pmid": "42230618",
      "doi": "10.1038/s41531-026-01407-7",
      "title": "Deep learning for freezing of gait assessment using inertial measurement units: a multicentre validation study",
      "year": 2026
    },
    {
      "ref": "R56",
      "pmid": "41513745",
      "doi": "10.1038/s41582-025-01179-3",
      "title": "An updated definition of freezing of gait",
      "year": 2026
    },
    {
      "ref": "R57",
      "pmid": "39121137",
      "doi": "10.3233/JPD-240134",
      "title": "Which Gait Tasks Produce Reliable Outcome Measures of Freezing of Gait in Parkinson's Disease?",
      "year": 2024
    },
    {
      "ref": "R58",
      "pmid": "24386308",
      "doi": "10.1371/journal.pone.0083919",
      "title": "Pedunculopontine nucleus area oscillations during stance, stepping and freezing in Parkinson's disease",
      "year": 2013
    },
    {
      "ref": "R59",
      "pmid": "42522567",
      "doi": "10.1093/brain/awag259",
      "title": "Distinct roles of the human cuneiform and pedunculopontine nuclei in gait and freezing of gait",
      "year": 2026
    }
  ],
  "evidence": [
    {
      "eid": "E1",
      "ref": "R1",
      "design": "慢性植入式STN-LFP与自由步态运动学同步记录",
      "population": "PD患者，Freezer与Non-Freezer",
      "n": "14人；Freezer 8人",
      "condition": "OFF药物、OFF DBS；静息、行走、转弯、障碍物、原地踏步",
      "measure": "STN beta功率、Sample Entropy、alpha entropy、步态指标",
      "finding": "Freezer未冻结行走时beta功率较低而beta entropy较高；冻结时alpha entropy较高",
      "limitations": "小样本；患者间和患者内效应需区分；与R34存在潜在队列重叠；不能推断因果"
    },
    {
      "eid": "E2",
      "ref": "R2",
      "design": "STN-LFP与运动学相关性分析",
      "population": "接受STN-DBS的PD患者",
      "n": "未在本次核验中确认可独立复核的完整人数",
      "condition": "单任务及双任务行走；FOG易感性评估",
      "measure": "STN低beta 15–21 Hz、theta 5–8 Hz、iFOG",
      "finding": "低beta与theta功率和FOG易感性相关；theta空间分布偏腹侧STN/SNr区域",
      "limitations": "主要是易感指标而非视频确认的实际冻结；没有证明因果方向"
    },
    {
      "eid": "E3",
      "ref": "R3",
      "design": "术中STN微电极多单位活动记录",
      "population": "PD-FOG患者",
      "n": "8人",
      "condition": "虚拟现实步态任务；冻结发生前后",
      "measure": "STN多单位放电、theta和beta活动、下肢运动表现",
      "finding": "虚拟冻结时STN病理性多单位活动及theta/beta振荡增强",
      "limitations": "非真实负重自由行走；术中状态可能影响结果；不能从时间关联单独推断因果"
    },
    {
      "eid": "E4",
      "ref": "R4",
      "design": "术中STN和黑质神经元微电极记录",
      "population": "中度PD患者",
      "n": "12人",
      "condition": "仰卧踏步、注意性提示和冻结相关运动异常",
      "measure": "单神经元放电率、放电模式和beta振荡",
      "finding": "STN和黑质神经元具有不同任务调制；踏步时STN beta下降，冻结时增加",
      "limitations": "仰卧模拟步态与自然行走不同；不能直接对应慢性LFP"
    },
    {
      "eid": "E5",
      "ref": "R5",
      "design": "同步皮层ECoG、STN-LFP和TUG步态记录",
      "population": "接受STN-DBS手术的PD-FOG患者",
      "n": "8人；41次行走测试；30次测试出现冻结",
      "condition": "实际步态冻结与非冻结比较",
      "measure": "STN beta功率、ECoG功率、皮层-STN相干性",
      "finding": "冻结期STN beta增强；高beta和gamma皮层-STN相干性出现异常",
      "limitations": "小患者样本；多个试次不独立；记录质量和运动伪迹需控制"
    },
    {
      "eid": "E6",
      "ref": "R6",
      "design": "步态启动运动学、STN-LFP及空间分区分析",
      "population": "PD患者及健康对照",
      "n": "PD 38人，健康对照24人；12名PD患者在实验中出现263次冻结",
      "condition": "OFF和ON多巴胺；步态启动；后部感觉运动STN与中央联合STN",
      "measure": "低beta、高beta、步态节律和运动学指标",
      "finding": "接近冻结时低beta与步态参数的关联失调，出现不同的高beta空间-行为关系；药物可部分改善",
      "limitations": "冻结集中于患者子集；重复事件非独立；电生理关联不等于因果控制"
    },
    {
      "eid": "E7",
      "ref": "R7",
      "design": "静息STN-LFP横断面比较",
      "population": "PD Freezer及Non-Freezer",
      "n": "23人；FOG 14人，非FOG 9人",
      "condition": "静息记录；临床FOG严重程度比较",
      "measure": "alpha功率、alpha burst、高beta burst",
      "finding": "FOG组alpha功率和burst幅度较高；高beta burst幅度与冻结严重程度及POMA表现相关",
      "limitations": "没有同步观察实际冻结；不能确定这些活动是否是发作机制"
    },
    {
      "eid": "E8",
      "ref": "R8",
      "design": "慢性STN-LFP、皮层电活动、运动学及分子影像",
      "population": "自由行走PD-FOG患者",
      "n": "7人",
      "condition": "有效行走、通过门口、主动停止、实际冻结及恢复",
      "measure": "局部STN功率、beta burst、皮层-STN 4–13 Hz耦合",
      "finding": "冻结时没有一致的局部beta功率或burst持续时间变化；皮层-STN低频解耦在冻结前出现并与多巴胺缺损不对称性相关",
      "limitations": "小样本；耦合指标不能确定方向性信息传递；长期电极记录具有空间采样限制"
    },
    {
      "eid": "E9",
      "ref": "R9",
      "design": "盲法DBS频率和电压参数比较",
      "population": "存在严重步态问题的晚期PD患者",
      "n": "13人",
      "condition": "60 Hz、130 Hz、不同电压及刺激关闭",
      "measure": "冻结次数和运动评分",
      "finding": "等能量60 Hz高电压条件冻结较少；130 Hz高电压条件可加重冻结",
      "limitations": "频率、电压与组织募集同时变化；特定晚期样本；短期观察"
    },
    {
      "eid": "E10",
      "ref": "R10",
      "design": "病例内即时DBS频率切换",
      "population": "新启用STN-DBS后立即出现FOG的PD患者",
      "n": "2人",
      "condition": "其他刺激参数不变，比较130 Hz和60 Hz",
      "measure": "即时FOG表现",
      "finding": "频率从130 Hz降低到60 Hz后冻结迅速缓解",
      "limitations": "极小病例数；频率变化同时改变单位时间的刺激脉冲数"
    },
    {
      "eid": "E11",
      "ref": "R11",
      "design": "随机盲法交叉比较",
      "population": "STN-DBS后报告步态变化的PD患者",
      "n": "20人",
      "condition": "保持电压等参数不变比较60 Hz和130 Hz",
      "measure": "主要终点为步幅；兼顾其他步态表现",
      "finding": "主要步幅终点没有显著差异；低频下震颤控制较差",
      "limitations": "未专门选择顽固性高频FOG；相同电压不等于相同刺激能量"
    },
    {
      "eid": "E12",
      "ref": "R12",
      "design": "随机双盲交叉临床试验",
      "population": "接受STN-DBS的PD患者",
      "n": "本次核验未确认完整样本数",
      "condition": "分别优化60 Hz和130 Hz触点后比较",
      "measure": "UPDRS运动评分及轴性症状",
      "finding": "优化后的60 Hz改善部分运动和轴性指标；低频最佳触点相对更腹侧",
      "limitations": "频率和最佳触点共同改变；不等同于纯频率因果效应"
    },
    {
      "eid": "E13",
      "ref": "R13",
      "design": "随机双盲交叉试验",
      "population": "130 Hz和药物治疗下仍有FOG的PD患者",
      "n": "7人",
      "condition": "药物ON；比较130 Hz、60 Hz和DBS OFF",
      "measure": "吞咽检查、FOG及轴性运动评估",
      "finding": "60 Hz相比常规130 Hz改善FOG和部分吞咽、轴性指标",
      "limitations": "样本量小；吞咽为主要关注终点；短期效果"
    },
    {
      "eid": "E14",
      "ref": "R14",
      "design": "随机序列交叉及长期随访",
      "population": "常规130 Hz下存在顽固性FOG的PD患者",
      "n": "11人完成初访；10人完成长期随访",
      "condition": "60 Hz相对130 Hz；平均随访14.5个月",
      "measure": "FOG、吞咽、UPDRS",
      "finding": "60 Hz的部分FOG和轴性症状改善延续至长期，但效应有所减弱",
      "limitations": "小样本；选择性纳入；与早期研究方向及研究团队关联，独立性需核查"
    },
    {
      "eid": "E15",
      "ref": "R15",
      "design": "随机双盲交叉试验",
      "population": "STN刺激下仍有轴性障碍的PD患者",
      "n": "12人",
      "condition": "优化STN与STN+SNr刺激",
      "measure": "主要综合轴性UPDRS终点及次要FOG-AC",
      "finding": "主要轴性终点阴性；FOG次要终点提示潜在改善",
      "limitations": "小样本、次要终点阳性；不能当作联合刺激确证性试验"
    },
    {
      "eid": "E16",
      "ref": "R16",
      "design": "随机交叉先导试验",
      "population": "接受STN-DBS且存在FOG的PD患者",
      "n": "15名患者进入联合刺激测试",
      "condition": "常规STN、STN+高频SNr、STN+低频SNr；每种模式约1个月",
      "measure": "NFOG-Q及临床响应",
      "finding": "主要NFOG-Q终点没有显著组间优势；部分患者达到临床重要改善",
      "limitations": "小样本及多刺激条件；亚组结果探索性；正式论文在线发表于2025年"
    },
    {
      "eid": "E17",
      "ref": "R17",
      "design": "多中心前瞻性随机交叉比较",
      "population": "存在显著FOG的PD患者",
      "n": "24人入组；20人完成随访",
      "condition": "STN单靶点与STN+SNr联合刺激，每模式6个月",
      "measure": "FOG-Q、生活质量评分",
      "finding": "报告联合刺激比单纯STN改善更多FOG-Q和生活质量评分",
      "limitations": "样本少；交叉研究需考虑顺序及延迟效应；部分研究报告细节需要进一步质量复核"
    },
    {
      "eid": "E18",
      "ref": "R18",
      "design": "探索性多中心随机双盲对照试验",
      "population": "已接受STN-DBS且持续FOG的PD患者",
      "n": "45人进入改良意向治疗分析；STN 23人，STN+SNr 22人",
      "condition": "优化STN对比STN+SNr，随访90天",
      "measure": "主要终点FOG-AC；临床应答及病程关联",
      "finding": "主要终点无显著差异，P=0.692；应答者分别为7人与8人；联合刺激应答可能与较短病程有关",
      "limitations": "亚组探索性；刺激位置由已有电极限制；未专门植入独立SNr靶点"
    },
    {
      "eid": "E19",
      "ref": "R19",
      "design": "回顾性刺激场和结构连接分析",
      "population": "术前存在FOG的STN-DBS患者",
      "n": "47人；18人有标准化诱发冻结测试",
      "condition": "术前术后6个月；刺激场及规范性连接组",
      "measure": "FOG-Q、结构连接、刺激体积",
      "finding": "有利刺激连接涉及运动皮层、前额叶、苍白球和部分脑干相关纤维；刺激豆状束与加重有关",
      "limitations": "结构连接为模型推断，不能证明实际轴突募集或因果传导"
    },
    {
      "eid": "E20",
      "ref": "R20",
      "design": "术前术后临床评估与刺激场连接分析",
      "population": "STN-DBS患者",
      "n": "19人",
      "condition": "比较不同皮层-STN纤维募集与FOG结局",
      "measure": "FOG、步态运动学、前额叶及感觉运动连接",
      "finding": "右前额叶相关募集与较差FOG结局相关，右感觉运动连接与较好结局相关",
      "limitations": "小样本、回顾性连接分析；不能建立半球和纤维因果特异性"
    },
    {
      "eid": "E21",
      "ref": "R21",
      "design": "回顾性刺激sweet spot及连接组映射",
      "population": "双侧STN-DBS且术前有FOG的PD患者",
      "n": "76人",
      "condition": "术后FOG改善、无明显变化及加重分组",
      "measure": "FOG评分、刺激体积、结构连接",
      "finding": "42人改善、22人变化较小、12人加重；背外侧及部分运动相关网络与改善相关",
      "limitations": "回顾性；结构影像连接和真实刺激效应不同；存在患者选择混杂"
    },
    {
      "eid": "E22",
      "ref": "R22",
      "design": "随机双盲方向性刺激交叉研究",
      "population": "术前有严重FOG的PD患者",
      "n": "10人",
      "condition": "中央STN、后部感觉运动STN和ring-mode",
      "measure": "客观步态、姿势控制和冻结次数",
      "finding": "中央STN刺激优于后部STN刺激，且冻结事件更少",
      "limitations": "样本量小；刺激方向改变同时募集多个纤维系统；短期评估"
    },
    {
      "eid": "E23",
      "ref": "R23",
      "design": "回顾性概率刺激场映射和交叉验证",
      "population": "STN-DBS的PD患者",
      "n": "98人",
      "condition": "术后一年的步态改善与恶化",
      "measure": "MDS-UPDRS III步态项目、刺激位置、概率映射",
      "finding": "42人步态改善、7人恶化；恶化组有效触点相对更腹侧；预测模型LOOCV R²约0.45",
      "limitations": "结局非纯FOG；恶化患者数少；回顾性预测可能受选择偏差影响"
    },
    {
      "eid": "E24",
      "ref": "R24",
      "design": "植入式STN beta burst驱动自适应DBS可行性研究",
      "population": "PD患者",
      "n": "7人",
      "condition": "DBS OFF、连续DBS、自适应DBS、随机间歇调制",
      "measure": "冻结、原地踏步、转弯及运动学",
      "finding": "实时burst驱动刺激可行并有短期运动获益，但未证明对FOG优于连续或随机调制刺激",
      "limitations": "小样本；设备和算法限制；先导试验统计效能不足"
    },
    {
      "eid": "E25",
      "ref": "R25",
      "design": "步态周期对齐的皮层-STN同步LFP及刺激调制研究",
      "population": "PD-FOG患者",
      "n": "本次核验未确认摘要之外可独立复核的人数",
      "condition": "冻结试次与非冻结试次；高/低频DBS及左旋多巴",
      "measure": "S1、SPL低beta；S1-STN theta相干性；步态相位",
      "finding": "冻结易感步态周期存在皮层低beta相位异常；DBS与药物分别改变部分频谱及耦合指标",
      "limitations": "具体低beta效应主要来自皮层，不能误称为STN局部功率；仍缺少针对相位机制的独立因果验证"
    },
    {
      "eid": "E26",
      "ref": "R26",
      "design": "STN-LFP、下肢EMG与药物状态比较",
      "population": "PD患者",
      "n": "14人",
      "condition": "坐位、站立、踏步、左旋多巴ON/OFF",
      "measure": "STN低beta、高beta、步态周期调制和肌肉活动",
      "finding": "踏步使低beta增强而高beta减弱；左旋多巴具有相反的频段调制方向",
      "limitations": "主要研究一般踏步而非实际FOG发作；频段定义与部分其他研究不同"
    },
    {
      "eid": "E27",
      "ref": "R27",
      "design": "STN与STN+SNr刺激期间高密度EEG及踏步研究",
      "population": "PD患者及健康对照",
      "n": "PD 12人，健康对照12人",
      "condition": "药物ON；刺激OFF、STN、STN+SN",
      "measure": "皮层振荡、冻结及踏步时间变异",
      "finding": "联合刺激改善部分踏步时间变异；不同刺激模式下冻结伴随不同皮层频谱空间模式",
      "limitations": "头皮EEG而非STN直接记录；步态变异改善不等于日常FOG必然改善"
    },
    {
      "eid": "E28",
      "ref": "R28",
      "design": "系统综述及Meta分析",
      "population": "STN+SNr与STN比较的PD研究",
      "n": "10项研究，109名可评价患者；FOG分析6项、86人",
      "condition": "截至2026-05-01的研究",
      "measure": "FOG效应量、UPDRS、异质性和GRADE",
      "finding": "FOG Hedges' g=-0.23，95% CI -1.04至0.59；未证明额外获益，证据确定性极低",
      "limitations": "高度异质；小样本；汇总既有试验而不是独立患者实验；尚未纳入2026年10月发表的R18"
    },
    {
      "eid": "E29",
      "ref": "R29",
      "design": "随机研究Meta分析与Meta回归",
      "population": "STN+SNr比较研究中的PD患者",
      "n": "8项试验，97人",
      "condition": "检索至2025-10",
      "measure": "FOG标准化效应量及异质性",
      "finding": "报告SMD=-0.39，95% CI -0.73至-0.04，提示联合刺激统计学优势",
      "limitations": "交叉试验采用平行组近似；同研究多个比较共享对照；与R28纳入研究存在重叠"
    },
    {
      "eid": "E30",
      "ref": "R30",
      "design": "术中微电极记录与虚拟双任务",
      "population": "PD患者",
      "n": "8人；33次认知线索试次",
      "condition": "认知提示后正常运动、虚拟冻结或严重减慢",
      "measure": "STN theta及多单位放电率",
      "finding": "导致冻结或严重减慢的认知负荷试次中theta减弱，伴短暂放电率增加",
      "limitations": "冻结和严重减慢合并分析；虚拟运动与自然步行不同；与R3有潜在团队及队列关联"
    },
    {
      "eid": "E31",
      "ref": "R31",
      "design": "术后STN-LFP与跑步机步态比较",
      "population": "PD患者",
      "n": "6人；3人存在严重步态犹豫或冻结",
      "condition": "坐位、站立和跑步机行走",
      "measure": "低beta 12–22 Hz和广义beta 12–35 Hz",
      "finding": "无冻结者行走时广泛beta抑制；有冻结者低beta异常增强",
      "limitations": "极小样本；步态犹豫与严格FOG分类可能不同"
    },
    {
      "eid": "E32",
      "ref": "R32",
      "design": "STN-LFP与皮层EEG横断面比较",
      "population": "PD Freezer与Non-Freezer",
      "n": "22人；FOG 14人，非FOG 8人",
      "condition": "静息及左旋多巴状态",
      "measure": "STN高beta 22–35 Hz功率、皮层-STN相干性",
      "finding": "FOG患者高beta较高；左旋多巴降低相关活动并伴随FOG改善",
      "limitations": "主要是表型及药物状态比较；不能证明实际冻结前高beta升高"
    },
    {
      "eid": "E33",
      "ref": "R33",
      "design": "运动状态STN电活动比较",
      "population": "PD Freezer与Non-Freezer",
      "n": "13人；Freezer 5人、Non-Freezer 8人",
      "condition": "行走与骑车",
      "measure": "beta广泛抑制及约18 Hz狭窄同步活动",
      "finding": "Freezer运动时可见狭窄低beta增强，即使没有当时实际冻结",
      "limitations": "小样本；运动相关异常不能直接解释冻结触发"
    },
    {
      "eid": "E34",
      "ref": "R34",
      "design": "慢性STN-LFP、步态与DBS频率实验",
      "population": "PD Freezer与Non-Freezer",
      "n": "12人；8名Freezer、4名Non-Freezer",
      "condition": "OFF药物；刺激OFF、60 Hz、140 Hz",
      "measure": "beta burst持续时间、双侧不对称性、冻结及步态指标",
      "finding": "Freezer长beta burst更明显；DBS缩短病理长burst并改善步态",
      "limitations": "小样本；与R1有潜在队列重叠；DBS的多重网络作用无法排除"
    },
    {
      "eid": "E35",
      "ref": "R35",
      "design": "STN-LFP与有节律踏步",
      "population": "PD患者",
      "n": "16人",
      "condition": "交替下肢踏步",
      "measure": "STN beta随踏步周期的动态变化",
      "finding": "正常踏步时beta活动存在左右交替和相位相关调制",
      "limitations": "非FOG专门研究；主要支持生理步态编码"
    },
    {
      "eid": "E36",
      "ref": "R36",
      "design": "神经机器人平台与STN-LFP运动编码研究",
      "population": "PD患者",
      "n": "18人",
      "condition": "控制下肢运动、肌肉激活及运动状态转换",
      "measure": "STN信号和下肢运动/肌肉激活参数",
      "finding": "STN包含运动启动、终止及肌肉激活幅度等可解码信息",
      "limitations": "解码能力不是生成运动的因果证明；平台不同于自然FOG"
    },
    {
      "eid": "E37",
      "ref": "R37",
      "design": "实际FOG中的STN-LFP、肌电与步态同步记录",
      "population": "存在FOG的PD患者",
      "n": "本次核验未确认可独立复核的完整人数",
      "condition": "行走、实际冻结及主动停止",
      "measure": "STN-下肢肌肉相干性、拮抗肌活动、共同收缩",
      "finding": "冻结前STN-肌肉耦合异常，冻结时拮抗肌抑制失效及共同收缩增加",
      "limitations": "相干性不能区分下降驱动、上行反馈与共同输入"
    },
    {
      "eid": "E38",
      "ref": "R38",
      "design": "虚拟步态功能磁共振网络研究",
      "population": "PD-FOG相关人群",
      "n": "本次核验未确认可独立复核的完整人数",
      "condition": "虚拟任务中的冻结和认知控制负荷",
      "measure": "额顶认知控制网络与基底节BOLD功能连接",
      "finding": "冻结与认知控制网络和基底节功能解耦有关",
      "limitations": "BOLD时间分辨率有限；虚拟冻结不等于真实自由步行；非STN电生理"
    },
    {
      "eid": "E39",
      "ref": "R39",
      "design": "虚拟现实行为实验",
      "population": "PD Freezer、Non-Freezer及健康对照",
      "n": "Freezer 36人、Non-Freezer 37人、健康对照18人",
      "condition": "认知冲突、狭窄门口和环境线索转换",
      "measure": "虚拟步态反应延迟及运动中断",
      "finding": "Freezer对抑制控制需求及视觉环境挑战表现出更显著运动延迟",
      "limitations": "行为模型不能直接证明STN的具体神经活动机制"
    },
    {
      "eid": "E40",
      "ref": "R40",
      "design": "静息态功能连接与左旋多巴反应分析",
      "population": "不同多巴胺反应性的PD-FOG患者和非FOG患者",
      "n": "55人；FOG 38人，其中反应性22人、无反应性16人",
      "condition": "按药物反应性分组",
      "measure": "STN与小脑、视觉和躯体感觉皮层BOLD连接",
      "finding": "药物反应性不同的FOG具有不同STN功能连接模式",
      "limitations": "静息BOLD关联；不能推断具体电生理频段或连接因果方向"
    },
    {
      "eid": "E41",
      "ref": "R41",
      "design": "多药物剂量状态病例系列",
      "population": "怀疑左旋多巴诱发FOG的PD患者",
      "n": "4人",
      "condition": "OFF、ON、Supra-ON",
      "measure": "FOG与其他帕金森运动症状",
      "finding": "提高左旋多巴剂量可以使FOG加重，同时改善其他运动症状",
      "limitations": "病例数极少；不涉及同步STN神经记录"
    },
    {
      "eid": "E42",
      "ref": "R42",
      "design": "急性左旋多巴挑战及血药浓度检测",
      "population": "PD患者",
      "n": "55人完成挑战；45人符合充分ON标准",
      "condition": "OFF到充分药物ON",
      "measure": "MDS-UPDRS III、冻结表型及血清左旋多巴",
      "finding": "45人中19人为ONOFF-FOG，11人为OFF-FOG，15人为NO-FOG",
      "limitations": "挑战研究不是STN电生理；临床表型划分仍受诱发任务影响"
    },
    {
      "eid": "E43",
      "ref": "R43",
      "design": "病例报告",
      "population": "具有双相左旋多巴诱发FOG的PD患者",
      "n": "病例报告",
      "condition": "不同药物作用阶段",
      "measure": "冻结与药物时间-反应关系",
      "finding": "FOG可能呈现非单调双相药物反应",
      "limitations": "个案证据；不能推断群体比例或STN活动规律"
    },
    {
      "eid": "E44",
      "ref": "R44",
      "design": "PPN区刺激临床研究，含双盲交叉评估",
      "population": "药物和STN刺激下仍严重冻结的PD患者",
      "n": "6人",
      "condition": "双侧PPN区刺激及一年随访",
      "measure": "FOG问卷、冻结时间及步态临床指标",
      "finding": "长期部分冻结指标改善，但盲法比较没有建立稳定的主要临床获益",
      "limitations": "小样本；电极位置差异；刺激效应可能存在延迟与持续效应"
    },
    {
      "eid": "E45",
      "ref": "R45",
      "design": "PPN刺激前瞻性研究",
      "population": "严重顽固性FOG及平衡障碍PD患者",
      "n": "5人",
      "condition": "双侧PPN刺激及长期观察",
      "measure": "步态与跌倒相关问卷、UPDRS",
      "finding": "报告部分FOG及跌倒相关表现的持续改善",
      "limitations": "样本极小；缺乏充分随机同期对照；可能存在刺激延迟洗脱"
    },
    {
      "eid": "E46",
      "ref": "R46",
      "design": "PPN区LFP与真实步态记录",
      "population": "接受PPN区电极植入的帕金森综合征患者",
      "n": "多个患者及电极；冻结前分析主要受少量患者事件限制",
      "condition": "静息、自然行走、冻结",
      "measure": "PPN alpha和beta功率、行走速度",
      "finding": "PPN alpha与较好行走表现相关，冻结时减弱；alpha与beta具有不同空间分布",
      "limitations": "冻结事件的患者级重复有限；多电极不等于独立患者"
    },
    {
      "eid": "E47",
      "ref": "R47",
      "design": "随机双盲PPN/CuN临床刺激试验中期分析",
      "population": "严重步态及平衡障碍PD患者",
      "n": "6人",
      "condition": "PPN、CuN及假刺激",
      "measure": "姿势准备、步态运动学和临床结局",
      "finding": "主要终点未证实显著获益；CuN改善部分步态指标，PPN结果不稳定",
      "limitations": "极小样本；刺激区域异质；与R48属于相同研究队列"
    },
    {
      "eid": "E48",
      "ref": "R48",
      "design": "PPN/CuN刺激交叉研究与长期随访",
      "population": "R47相关PD队列",
      "n": "6人；非新的独立六人队列",
      "condition": "长期刺激、临床随访",
      "measure": "FOG、跌倒及步态表现",
      "finding": "长期随访未确定持续可靠的总体临床获益",
      "limitations": "队列与R47重叠；小样本；长期疾病进展等混杂"
    },
    {
      "eid": "E49",
      "ref": "R49",
      "design": "随机双盲交叉PPN频率研究",
      "population": "严重步态障碍的PD患者",
      "n": "9人",
      "condition": "PPN区10–25 Hz与60–80 Hz",
      "measure": "运动不能、步态问题及日间嗜睡",
      "finding": "7/9患者在较低频率下表现较好，另有患者加重",
      "limitations": "极小样本；观察时间短；PPN区定位及频率反应异质"
    },
    {
      "eid": "E50",
      "ref": "R50",
      "design": "真实步行EEG网络与主动停止对照",
      "population": "PD-FOG患者",
      "n": "18人",
      "condition": "冻结与主动停止前2秒",
      "measure": "皮层beta相位锁定、低频连接和网络模块度",
      "finding": "冻结前局部beta连接增强，部分额叶到后部皮层的低频连接减弱",
      "limitations": "皮层EEG不是STN直接记录；网络推断易受体积传导与运动伪迹影响"
    },
    {
      "eid": "E51",
      "ref": "R51",
      "design": "三中心静息头皮EEG burst分析",
      "population": "PD患者及健康对照",
      "n": "237人；PD 149人、健康对照88人",
      "condition": "PD患者药物ON；FOG分型",
      "measure": "低beta burst频率、持续时间及theta burst幅度",
      "finding": "PD总体低beta burst更频繁且较短；调整后Freezer与Non-Freezer的低beta差异不稳健；theta幅度与FOG严重程度相关",
      "limitations": "头皮EEG而非STN；静息而非冻结；药物给药时间跨中心不完全统一"
    },
    {
      "eid": "E52",
      "ref": "R52",
      "design": "STN-LFP特征机器学习FOG检测先导研究",
      "population": "慢性植入电极的PD患者",
      "n": "5人；测试集8次行走试验",
      "condition": "步态任务中的FOG窗口检测",
      "measure": "多频段LFP、burst、窗口级F1及事件检测率",
      "finding": "报告weighted F1约0.67、macro F1约0.62；摘要24/29与正文24/30事件检测数量不一致",
      "limitations": "小样本、个体化标记依赖、研究内部数字不一致；检测不证明因果"
    },
    {
      "eid": "E53",
      "ref": "R53",
      "design": "胆碱能PET与动态平衡研究",
      "population": "PD患者",
      "n": "125人",
      "condition": "不同动态平衡与步态任务",
      "measure": "胆碱能神经末梢PET、平衡功能分域",
      "finding": "步态与动态平衡障碍涉及多个皮层、丘脑和小脑相关胆碱能网络",
      "limitations": "非直接FOG发作或STN电生理；影像相关不证明致病通路"
    },
    {
      "eid": "E54",
      "ref": "R54",
      "design": "IMU与深度学习FOG检测方法研究",
      "population": "PD-FOG患者",
      "n": "12人",
      "condition": "不同任务、药物状态、主动停止",
      "measure": "自动FOG标注泛化与停止事件混淆",
      "finding": "模型对任务、状态及主动停止的处理会影响FOG判定表现",
      "limitations": "与STN机制无直接关系；主要用于解释行为标签误差"
    },
    {
      "eid": "E55",
      "ref": "R55",
      "design": "多中心IMU冻结自动标注外部验证",
      "population": "来自多个中心的PD-FOG患者",
      "n": "本地85人、外部256人",
      "condition": "本地训练、六个外部队列及少量外部数据微调",
      "measure": "冻结时间百分比与人工视频的一致性ICC",
      "finding": "ICC本地0.886，外部平均0.562，微调后0.732",
      "limitations": "不同中心采集与标注异质；算法结果不可直接替代人工金标准"
    },
    {
      "eid": "E56",
      "ref": "R56",
      "design": "国际专家共识及定义更新",
      "population": "FOG临床和研究评价",
      "n": "共识文献，非独立实验队列",
      "condition": "临床与视频冻结定义",
      "measure": "冻结表现、有效迈步尝试及事件起止规则",
      "finding": "强调存在迈步尝试却无法产生有效步伐，并明确不同冻结类型及视频判定原则",
      "limitations": "共识不是神经机制实验；不能替代数据验证"
    },
    {
      "eid": "E57",
      "ref": "R57",
      "design": "FOG诱发任务敏感性和重测研究",
      "population": "确诊Freezer",
      "n": "63人；26人完成重测",
      "condition": "OFF及ON药物；转弯、TUG、门口和双任务",
      "measure": "冻结发生率、冻结时间百分比、ICC及最小可检测变化",
      "finding": "360度转身尤其敏感；OFF更容易诱发；多任务组合提高检出率，但严重程度测量误差仍较大",
      "limitations": "临床任务研究，不直接证明STN机制；冻结的日内及跨访视波动较大"
    },
    {
      "eid": "E58",
      "ref": "R58",
      "design": "PPN区LFP与踏步、药物状态同步研究",
      "population": "接受PPN区电极植入的PD-FOG患者",
      "n": "7人",
      "condition": "OFF及ON左旋多巴；静止、站立、原地踏步",
      "measure": "PPN区alpha、beta、gamma及冻结时间",
      "finding": "左旋多巴显著减少踏步冻结，伴PPN alpha增强、beta和gamma减弱",
      "limitations": "不能确定频谱变化是药物直接作用还是运动改善的结果；触点不是独立患者"
    },
    {
      "eid": "E59",
      "ref": "R59",
      "design": "PPN与CuN同步LFP、步态启动运动学和刺激比较",
      "population": "药物抵抗性FOG的PD患者",
      "n": "4人；38次冻结试次、115次非冻结试次",
      "condition": "APA、步态启动、FOG及PPN/CuN/假刺激",
      "measure": "CuN alpha、PPN beta及alpha、步态节律和推进",
      "finding": "CuN与PPN有不同步态相位编码；冻结前出现错误时序的MLR alpha同步及PPN beta异常；刺激效应因核团而异",
      "limitations": "仅4名患者；事件数不能等同独立样本；与既往同中心研究存在潜在队列关联"
    }
  ],
  "claims": [
    {
      "cid": "C1",
      "text": "在部分真实或虚拟冻结事件中，STN beta及theta活动升高。",
      "level": "finding",
      "status": "supported",
      "uncertainty": "结果取决于冻结任务、信号记录方式和时间窗；不是全部FOG的普遍规律。",
      "evidence": [
        {"eid": "E3", "relation": "supports"},
        {"eid": "E5", "relation": "supports"},
        {"eid": "E4", "relation": "supports"},
        {"eid": "E8", "relation": "qualifies"},
        {"eid": "E30", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C2",
      "text": "FOG易感患者的STN beta平均功率持续高于非FOG患者。",
      "level": "synthesis",
      "status": "contested",
      "uncertainty": "静息、运动及冻结前状态的不同比较产生相反方向结果；广义beta与低/高beta也不可直接合并。",
      "evidence": [
        {"eid": "E32", "relation": "supports"},
        {"eid": "E31", "relation": "supports"},
        {"eid": "E2", "relation": "supports"},
        {"eid": "E1", "relation": "contradicts"},
        {"eid": "E33", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C3",
      "text": "STN局部beta增强不是现有研究已经确立的所有FOG事件的必要条件。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "直接反例样本较小；不能排除特定STN微区或时间窗口存在尚未被记录的异常。",
      "evidence": [
        {"eid": "E8", "relation": "supports"},
        {"eid": "E1", "relation": "qualifies"},
        {"eid": "E3", "relation": "qualifies"},
        {"eid": "E5", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C4",
      "text": "STN beta burst持续时间及活动熵可能提供平均beta功率之外的FOG相关信息。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "时间结构指标的独立预测效应尚未在充分规模的多中心患者级外部验证中确认。",
      "evidence": [
        {"eid": "E34", "relation": "supports"},
        {"eid": "E1", "relation": "supports"},
        {"eid": "E7", "relation": "supports"},
        {"eid": "E8", "relation": "qualifies"},
        {"eid": "E24", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C5",
      "text": "FOG相关STN theta可以升高也可以降低，其方向受认知任务及时间阶段影响。",
      "level": "synthesis",
      "status": "contested",
      "uncertainty": "双阶段解释尚未在同一患者内直接验证；可能还涉及不同FOG亚型。",
      "evidence": [
        {"eid": "E3", "relation": "supports"},
        {"eid": "E2", "relation": "supports"},
        {"eid": "E30", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C6",
      "text": "部分FOG在发生前出现皮层-STN低频耦合异常，而局部STN功率可以不出现同步变化。",
      "level": "finding",
      "status": "supported",
      "uncertainty": "核心直接证据来自小样本；耦合指标不能确认信号传递方向。",
      "evidence": [
        {"eid": "E8", "relation": "supports"},
        {"eid": "E25", "relation": "qualifies"},
        {"eid": "E5", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C7",
      "text": "STN及相关皮层和脑干区域具有步态阶段特异的神经活动组织。",
      "level": "synthesis",
      "status": "well-supported",
      "uncertainty": "该判断支持生理性步态编码；其中哪些异常对FOG具有因果性尚不明确。",
      "evidence": [
        {"eid": "E35", "relation": "supports"},
        {"eid": "E36", "relation": "supports"},
        {"eid": "E26", "relation": "supports"},
        {"eid": "E6", "relation": "supports"},
        {"eid": "E25", "relation": "supports"},
        {"eid": "E59", "relation": "supports"}
      ]
    },
    {
      "cid": "C8",
      "text": "STN-DBS对FOG的作用受到刺激空间位置和募集网络影响。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "结构连接研究主要是相关性；方向性刺激试验患者人数有限；尚无统一最优空间靶点。",
      "evidence": [
        {"eid": "E19", "relation": "supports"},
        {"eid": "E20", "relation": "supports"},
        {"eid": "E21", "relation": "supports"},
        {"eid": "E22", "relation": "supports"},
        {"eid": "E23", "relation": "supports"}
      ]
    },
    {
      "cid": "C9",
      "text": "60 Hz STN-DBS可能改善某些常规高频刺激下持续存在的FOG，但并非所有患者均优于130 Hz。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "患者选择、频率、电压、总能量、触点及随访时长共同影响结果。",
      "evidence": [
        {"eid": "E9", "relation": "supports"},
        {"eid": "E10", "relation": "supports"},
        {"eid": "E13", "relation": "supports"},
        {"eid": "E14", "relation": "supports"},
        {"eid": "E11", "relation": "qualifies"},
        {"eid": "E12", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C10",
      "text": "STN+SNr联合刺激是否总体优于优化后的单纯STN刺激，目前尚无稳定确证。",
      "level": "synthesis",
      "status": "contested",
      "uncertainty": "阳性与阴性研究共存；个体反应异质性大；两个Meta分析因方法不同得出不同结论。",
      "evidence": [
        {"eid": "E15", "relation": "qualifies"},
        {"eid": "E16", "relation": "supports"},
        {"eid": "E17", "relation": "contradicts"},
        {"eid": "E18", "relation": "supports"},
        {"eid": "E28", "relation": "supports"},
        {"eid": "E29", "relation": "contradicts"}
      ]
    },
    {
      "cid": "C11",
      "text": "PPN/CuN和其他脑干步态网络参与FOG，但直接刺激这些核团的临床效应高度异质。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "人体样本小，核团定位困难；部分研究队列重复；生理机制与临床疗效不能直接等同。",
      "evidence": [
        {"eid": "E46", "relation": "supports"},
        {"eid": "E58", "relation": "supports"},
        {"eid": "E59", "relation": "supports"},
        {"eid": "E44", "relation": "qualifies"},
        {"eid": "E45", "relation": "supports"},
        {"eid": "E47", "relation": "qualifies"},
        {"eid": "E48", "relation": "qualifies"},
        {"eid": "E49", "relation": "supports"}
      ]
    },
    {
      "cid": "C12",
      "text": "FOG具有至少部分可区分的多巴胺反应亚型。",
      "level": "synthesis",
      "status": "well-supported",
      "uncertainty": "亚型间边界仍受测量任务、给药时间和剂量影响；双相FOG主要来自病例证据。",
      "evidence": [
        {"eid": "E41", "relation": "supports"},
        {"eid": "E42", "relation": "supports"},
        {"eid": "E43", "relation": "supports"},
        {"eid": "E40", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C13",
      "text": "FOG诱发任务、标注规则及自动检测的泛化误差可显著影响神经电生理研究结论。",
      "level": "synthesis",
      "status": "well-supported",
      "uncertainty": "特定误差对具体STN研究效应量的影响需要重分析原始数据才能定量确定。",
      "evidence": [
        {"eid": "E56", "relation": "supports"},
        {"eid": "E57", "relation": "supports"},
        {"eid": "E54", "relation": "supports"},
        {"eid": "E55", "relation": "supports"}
      ]
    },
    {
      "cid": "C14",
      "text": "实际FOG涉及STN-下肢肌肉耦合变化及拮抗肌协调失效。",
      "level": "finding",
      "status": "supported",
      "uncertainty": "已观察到关联，但尚未确定是下降因果驱动、共同输入还是感觉反馈。",
      "evidence": [
        {"eid": "E37", "relation": "supports"},
        {"eid": "E26", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C15",
      "text": "认知冲突、视觉环境和额顶网络组织异常与FOG易感及发作有关。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "认知任务和影像研究不能直接指定STN为最初因果来源。",
      "evidence": [
        {"eid": "E39", "relation": "supports"},
        {"eid": "E38", "relation": "supports"},
        {"eid": "E50", "relation": "supports"},
        {"eid": "E30", "relation": "supports"}
      ]
    },
    {
      "cid": "C16",
      "text": "目前不能仅凭STN信号的预测能力将其判定为FOG致病介质。",
      "level": "synthesis",
      "status": "well-supported",
      "uncertainty": "这是因果推断约束，而不是证明STN信号只具有伴随意义。",
      "evidence": [
        {"eid": "E52", "relation": "supports"},
        {"eid": "E36", "relation": "supports"},
        {"eid": "E24", "relation": "supports"},
        {"eid": "E8", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C17",
      "text": "基于STN beta burst的实时自适应DBS已证明技术可行，但其改善FOG的特异性机制尚未确立。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "目前可行性研究样本量及统计效能不足，不能据此断言闭环刺激无优势。",
      "evidence": [
        {"eid": "E24", "relation": "supports"},
        {"eid": "E34", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C18",
      "text": "将STN-F0G定义为单一脑区、单一频段、单一方向的异常活动模型，不足以解释全部观察结果。",
      "level": "synthesis",
      "status": "well-supported",
      "uncertainty": "多维度描述更符合证据，但具体统一机制及因果结构尚未确立。",
      "evidence": [
        {"eid": "E1", "relation": "supports"},
        {"eid": "E3", "relation": "supports"},
        {"eid": "E8", "relation": "supports"},
        {"eid": "E25", "relation": "supports"},
        {"eid": "E26", "relation": "supports"},
        {"eid": "E30", "relation": "supports"},
        {"eid": "E59", "relation": "supports"}
      ]
    },
    {
      "cid": "C19",
      "text": "步态相位编码失稳可能是FOG的重要近端机制。",
      "level": "mechanism",
      "status": "speculative",
      "uncertainty": "尚缺乏充分规模的相位锁定随机干预试验来证明特异性因果作用。",
      "evidence": [
        {"eid": "E35", "relation": "supports"},
        {"eid": "E25", "relation": "supports"},
        {"eid": "E6", "relation": "supports"},
        {"eid": "E59", "relation": "supports"}
      ]
    },
    {
      "cid": "C20",
      "text": "部分FOG可能由认知控制募集失败后出现的STN运动阻断状态引起。",
      "level": "mechanism",
      "status": "speculative",
      "uncertainty": "需要在同一冻结事件中确认早期theta异常与后续同步增强的时间序列。",
      "evidence": [
        {"eid": "E30", "relation": "supports"},
        {"eid": "E3", "relation": "supports"},
        {"eid": "E39", "relation": "supports"}
      ]
    },
    {
      "cid": "C21",
      "text": "皮层-STN低频解耦可能参与FOG发生前的运动状态转换失败。",
      "level": "mechanism",
      "status": "speculative",
      "uncertainty": "目前直接电生理支持主要来自小样本，不能区分因果输入、共同网络状态与下游响应。",
      "evidence": [
        {"eid": "E8", "relation": "supports"},
        {"eid": "E38", "relation": "supports"},
        {"eid": "E50", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C22",
      "text": "STN通过SNr及MLR相关输出门控参与某些冻结事件。",
      "level": "mechanism",
      "status": "speculative",
      "uncertainty": "结构及生理证据支持相关网络，但随机干预尚未确立特异性中介和普遍临床效应。",
      "evidence": [
        {"eid": "E37", "relation": "supports"},
        {"eid": "E19", "relation": "supports"},
        {"eid": "E59", "relation": "supports"},
        {"eid": "E18", "relation": "qualifies"},
        {"eid": "E47", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C23",
      "text": "FOG可以由STN之外的多网络异常主导，STN局部信号在部分情况下可能是代偿或下游读出。",
      "level": "mechanism",
      "status": "speculative",
      "uncertainty": "缺少足以确认最初病理节点的正交干预与同时多网络记录。",
      "evidence": [
        {"eid": "E8", "relation": "supports"},
        {"eid": "E40", "relation": "supports"},
        {"eid": "E53", "relation": "qualifies"},
        {"eid": "E24", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C24",
      "text": "不同研究中的低beta和高beta不能视为同一功能变量。",
      "level": "synthesis",
      "status": "supported",
      "uncertainty": "不同论文频段边界不统一，尚需要患者个体频谱峰值的统一重新分析。",
      "evidence": [
        {"eid": "E26", "relation": "supports"},
        {"eid": "E32", "relation": "supports"},
        {"eid": "E33", "relation": "supports"},
        {"eid": "E31", "relation": "supports"}
      ]
    },
    {
      "cid": "C25",
      "text": "PPN/MLR alpha在冻结时可能出现不同方向的变化，时空组织比统一的功率方向更有解释力。",
      "level": "synthesis",
      "status": "contested",
      "uncertainty": "早期研究和2026年研究在脑干采样位置、时间对齐及患者数量上存在差异。",
      "evidence": [
        {"eid": "E46", "relation": "supports"},
        {"eid": "E59", "relation": "qualifies"},
        {"eid": "E58", "relation": "qualifies"}
      ]
    },
    {
      "cid": "C26",
      "text": "R52对冻结事件检测数量的摘要与正文存在24/29和24/30的不一致。",
      "level": "finding",
      "status": "supported",
      "uncertainty": "需要原作者澄清；在澄清前不将任一数字作为确定的患者级检测准确率。",
      "evidence": [
        {"eid": "E52", "relation": "supports"}
      ]
    }
  ],
  "hypotheses": [
    {
      "hid": "H1",
      "name": "STN病理性beta同步运动阻断模型",
      "text": "在特定FOG亚型中，过强、持续时间过长或错误运动阶段出现的STN beta同步直接妨碍运动程序切换。该模型应限定神经来源、频段和时间窗，不能声称所有FOG必然具有相同beta变化。",
      "claims": [
        {"cid": "C1", "relation": "supports"},
        {"cid": "C4", "relation": "supports"},
        {"cid": "C3", "relation": "contradicts"},
        {"cid": "C17", "relation": "contradicts"},
        {"cid": "C24", "relation": "supports"}
      ],
      "predictions": [
        "预先指定的FOG亚型中，长beta burst占用时间在实际冻结之前显著增加。",
        "异常beta应优于普通运动迟缓和主动停止时的beta变化预测冻结。",
        "准确锁定异常beta的刺激优于脉冲数、总刺激负荷匹配的随机刺激。",
        "神经beta异常的降低应在时间上先于冻结风险下降。"
      ],
      "falsifiers": [
        "在足够数量的独立患者中，严格确认的冻结没有预定的beta异常。",
        "特异性削弱目标beta活动后，FOG发生率和持续时间不变。",
        "预测效应完全由步速、肌肉活动或运动伪迹解释。"
      ]
    },
    {
      "hid": "H2",
      "name": "步态周期相位编码失稳模型",
      "text": "STN及其相关网络不能在正确的步态周期阶段维持或切换神经活动，导致预期姿势调整、支撑、摆动与迈步程序之间的时间协调失败。异常可以表现为同步过强、过弱或相位失配。",
      "claims": [
        {"cid": "C7", "relation": "supports"},
        {"cid": "C19", "relation": "supports"},
        {"cid": "C24", "relation": "supports"},
        {"cid": "C3", "relation": "supports"}
      ],
      "predictions": [
        "步态周期对齐的STN和皮层特征比整段平均beta功率更好预测实际冻结。",
        "冻结试次中的异常首先表现为相位调制减弱、错误相位增强或跨周期时序漂移。",
        "在控制步速和步幅之后，相位指标仍具有独立预测信息。",
        "相位锁定刺激在相同刺激总负荷条件下优于非相位锁定刺激。"
      ],
      "falsifiers": [
        "在独立患者中，相位指标的预测能力不优于非相位特异指标。",
        "运动学混杂调整后，相位异常消失。",
        "正确相位与随机相位刺激在冻结改善及生理中介上没有可重复差异。"
      ]
    },
    {
      "hid": "H3",
      "name": "认知控制不足到运动阻断的双阶段模型",
      "text": "复杂环境或双任务首先导致STN相关控制网络的认知募集不足，随后在运动执行层面出现异常同步或放电增加，使冻结发生。该模型提出两个具有明确顺序的机制阶段。",
      "claims": [
        {"cid": "C5", "relation": "supports"},
        {"cid": "C15", "relation": "supports"},
        {"cid": "C20", "relation": "supports"},
        {"cid": "C1", "relation": "supports"}
      ],
      "predictions": [
        "认知冲突提示后应先出现STN任务相关theta调制不足。",
        "只有随后发展为实际冻结的试次才出现第二阶段的异常运动阻断活动。",
        "同一患者的成功双任务试次应保留较正常的早期theta响应。",
        "降低认知冲突或改善任务提示应优先改变第一阶段，而非只改变最终肌肉共同收缩。"
      ],
      "falsifiers": [
        "同一患者中找不到可重复的早期和晚期神经异常时间顺序。",
        "正常认知错误与普通运动减慢出现完全相同的两阶段序列。",
        "校正运动及任务难度后，theta时间变化与冻结没有独立关联。"
      ]
    },
    {
      "hid": "H4",
      "name": "皮层-STN网络解耦模型",
      "text": "FOG的近端原因是皮层和STN之间与步态状态转换有关的动态耦合失败，而不是必须存在某种STN局部功率增强。异常耦合可以影响运动计划更新和有效迈步的维持。",
      "claims": [
        {"cid": "C6", "relation": "supports"},
        {"cid": "C21", "relation": "supports"},
        {"cid": "C15", "relation": "supports"},
        {"cid": "C3", "relation": "supports"}
      ],
      "predictions": [
        "冻结前4–13 Hz或个体化低频皮层-STN耦合异常优于局部STN功率预测FOG。",
        "耦合变化应能够区别冻结、主动停止、门口通过和普通步态减慢。",
        "耦合异常应在有效步态恢复时消失或恢复正常组织。",
        "通过时序特异性干预恢复目标耦合时，冻结风险应相应下降。"
      ],
      "falsifiers": [
        "共同输入、体积传导、运动伪迹和信号非平稳性控制后，耦合异常消失。",
        "耦合异常出现于所有主动停止事件而没有FOG特异性。",
        "干预有效改变目标耦合但不改变相应冻结风险。"
      ]
    },
    {
      "hid": "H5",
      "name": "STN-SNr-MLR输出门控模型",
      "text": "部分FOG来自STN对基底节输出和脑干步态网络的异常调制，使计划中的迈步无法形成正确的下降运动信号及下肢拮抗肌协调。疗效取决于实际募集的通路和病程阶段，而非仅取决于刺激是否位于STN。",
      "claims": [
        {"cid": "C8", "relation": "supports"},
        {"cid": "C11", "relation": "supports"},
        {"cid": "C14", "relation": "supports"},
        {"cid": "C22", "relation": "supports"},
        {"cid": "C10", "relation": "contradicts"}
      ],
      "predictions": [
        "特定STN-SNr-MLR纤维连接特征能够前瞻性预测通路刺激对FOG的改善。",
        "STN与脑干网络改变应在部分冻结中先于拮抗肌共同收缩和无效迈步。",
        "精准刺激靶通路应优于未募集该通路的等负荷刺激。",
        "药物反应性、病程和脑干通路完整性应与刺激疗效发生交互作用。"
      ],
      "falsifiers": [
        "确认有效募集目标通路后，冻结和预先指定的下降运动中介均未改善。",
        "目标通路连接强度对独立样本中的刺激疗效没有预测价值。",
        "STN-肌肉时序异常完全由周围感觉反馈解释。"
      ]
    },
    {
      "hid": "H6",
      "name": "共同网络失稳与STN下游读出模型",
      "text": "FOG首先发生于皮层认知控制、感觉整合、脑干或其他神经网络。STN的功率、burst和耦合异常可作为网络状态读出、反馈响应或代偿活动，因而可能具有预测价值却未必是全部FOG的因果介质。",
      "claims": [
        {"cid": "C16", "relation": "supports"},
        {"cid": "C17", "relation": "supports"},
        {"cid": "C23", "relation": "supports"},
        {"cid": "C12", "relation": "supports"},
        {"cid": "C3", "relation": "supports"}
      ],
      "predictions": [
        "不同FOG亚型可能具有不同的最早异常脑网络，而不共享一种必要的STN频谱变化。",
        "部分皮层、脑干或神经肌肉指标应先于STN局部异常。",
        "STN标志物可能实现FOG检测，但专门抑制它不一定优于随机或连续刺激。",
        "改变非STN网络的有效干预可改善冻结，而不一定同步改变特定STN功率指标。"
      ],
      "falsifiers": [
        "在严格控制其他网络变量后，确定某种STN神经活动对指定FOG亚型具有必要性。",
        "针对该STN活动的选择性随机干预稳定、特异地预防FOG，且中介分析支持其因果作用。",
        "跨网络高时间分辨率记录反复证明STN特定异常是独立于外部触发的最早病理事件。"
      ]
    }
  ]
}
```

【完成】