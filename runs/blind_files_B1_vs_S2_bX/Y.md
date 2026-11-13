# STN–FOG 研究报告工作稿｜第 4 轮

**本轮重点：补充交叉研究、辨析 θ 振荡的相反结果、评估证据的因果强度、识别现有研究的系统性缺陷，并设计能够真正区分竞争性机制的实验。**

## 二十一、补充一个容易被忽略的研究方向：FOG 不是单纯的运动执行失败

前几轮主要围绕 β、α 和皮层-STN 耦合展开。本轮进一步审查了认知双任务和 STN 单位活动研究。

一个重要发现是：STN 的 θ 活动可能在不同类型的 FOG 中表现出相反方向的变化。

### 21.1 Georgiades et al., 2023：认知负荷导致的步态障碍

[R33] *Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease.*

- PMID：37226972。
- DOI：10.1002/mds.29455。
- 8 名 PD 患者。
- 术中 STN 微电极记录。
- 采用虚拟现实步行任务。
- 通过屏幕上的 Stroop-like 颜色-文字冲突任务增加认知负荷。
- 患者停用抗帕金森药物至少 12 小时。

在 33 次有效的认知提示试次中：

- 18 次未出现步态输出受损。
- 15 次出现冻结或明显步态减慢。
- 其中 8 次被归类为 VR freezing，7 次为显著运动输出减慢。

主要结果：

**发生冻结或明显减速的试次中，认知提示出现后 STN θ（3–8 Hz）活动降低。**

其他频段没有显示同样的显著变化。

作者提出，认知提示可能需要 STN θ 同步活动参与注意力资源重新分配；如果这种活动不能适当维持，患者就可能无法在继续行走的同时完成认知处理。[R33]

### 21.2 与 2019 年研究形成一个非常重要的对照

Georgiades 等人 2019 年的研究 [R9] 发现：

- FOG onset 附近 STN θ 和 β 活动增加。
- STN MUA 出现短暂异常增强。
- 之后出现下肢肌肉放电异常。

而 2023 年研究 [R33] 发现：

- 在认知冲突提示出现后，未来发生步态障碍的试次中，STN θ 活动降低。

这两种结果不能简单地归纳为某一研究正确、另一研究错误。

因为它们实际研究的是不同过程：

| 维度 | 2019 年研究 | 2023 年研究 |
|---|---|---|
| 主要诱因 | VR 步态冻结 | 认知双任务 |
| 信号 | STN MUA | STN MUA |
| 主要时间参考 | FOG onset | 认知提示 |
| 主要发现 | θ/β 异常增强 | θ 活动降低 |
| 可能涉及过程 | 异常运动停止 | 认知资源重新分配失败 |

由此产生一个值得检验的解释：

**θ 活动可能不是 FOG 的单向病理标志物，而是参与不同认知-运动状态转换的动态调节信号。**

在认知任务出现时，θ 活动不足可能反映注意力分配失败；在运动停止已经发生时，θ 活动增强则可能反映异常的运动抑制或网络重组。

目前这只是基于不同实验的机制解释，尚未在同一患者、同一任务中得到验证。

### 21.3 2023 年研究对闭环 DBS 的启示

如果 FOG 的不同诱发机制对应不同神经活动方向，那么以单一 θ 阈值作为 aDBS 控制信号可能产生误判。

例如：

- θ 下降可能意味着认知负荷下的控制资源不足。
- θ 上升可能意味着某些运动停止过程中的异常同步。

如果不结合行为阶段和其他信号，控制算法可能在错误的时刻提高刺激。

这支持将神经活动与 IMU、EMG、任务阶段以及个体化状态分类结合，而不是依赖固定频段的单阈值控制。

---

## 二十二、STN 的运动编码：FOG 研究不应只关注异常振荡

另一个重要交叉方向是 STN 对步态基本运动成分的编码。

[R34] Thenaisie 等人，2022：

*Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease.*

- PMID：36070366。
- DOI：10.1126/scitranslmed.abo1800。
- 18 名 PD 患者。
- 采用神经机器人平台和动力学测量。
- 对步态运动过程进行可控分解。

研究发现，STN 活动能够编码：

1. 腿部肌肉活动的启动；
2. 腿部肌肉活动的终止；
3. 肌肉活动幅度；
4. 步行状态；
5. 运动活力；
6. 部分冻结相关运动状态。

这一研究的价值是把 STN 从一个抽象的振荡发生器，重新理解为参与运动输出组织的神经节点。

**机制意义：**

FOG 可能不只是某个频段振荡过强，而是 STN 对肌肉活动启动、终止和幅度的正常编码关系发生破坏。

这也解释了为什么在一些患者中，局部 β 功率变化不明显，步态输出仍然可能严重异常。

但该研究采用的是受控神经机器人运动范式，不能等同于自由行走中自然发生的 FOG。它提供的是步态编码的基础证据，而不是直接的 FOG 因果证据。[R34]

---

## 二十三、需要重新审视的证据冲突：为什么 β 功率、β 熵和 β burst 可以出现不同方向？

现有文献至少有以下几种看似矛盾的发现：

| 研究 | 条件 | β 结果 |
|---|---|---|
| Toledo 2014 [R1] | 静息、患者间比较 | FOG 患者高 β 增强 |
| Syrkin-Nikolau 2017 [R7] | 无 FOG 的行走 | Freezer β 功率较低、Sample Entropy 较高 |
| Anidi 2018 [R8] | 步行、踏步 | Freezer β burst duration 较长 |
| Pozzi 2019 [R4] | 正常行走 vs 冻结 | STN β 功率和 burst duration 无显著差异 |
| Liu 2022 [R11] | 行走和冻结 epoch | 冻结期间 β 功率较高 |
| Fim Neto 2025 [R15] | 静息 | 高 β burst amplitude 与 FOG 严重度相关 |
| Collomb-Clerc 2025 [R6] | 步态启动及冻结前 | 低 β 和高 β 与不同步态维度呈状态、空间依赖关系 |

这些结果可能同时成立。

需要区分五个独立变量：

1. β 振荡的平均功率；
2. β burst 的持续时间；
3. β burst 的振幅；
4. β burst 的发生率及时间间隔；
5. β 活动与行为及其他神经区域之间的耦合。

例如，患者可以出现：

- 较低的平均 β 功率；
- 较长但数量较少的 β burst；
- 更高的 Sample Entropy；
- 更低的 inter-burst interval entropy。

它们并不构成数学上的矛盾。

真正的问题是：这些指标是否具有独立的生理意义，还是同一个潜在信号变化的不同统计表现？

这一点需要在同一批数据中进行统一计算和交叉验证。

### 23.1 一个重要的分析改进：同时分解 periodic 和 aperiodic activity

传统 PSD 频谱分析通常将整个 β 频段功率作为一个数值。

但是，观测到的频谱可能由两部分组成：

- periodic component：真正的窄带振荡峰；
- aperiodic component：非振荡性、近似 1/f 的背景活动。

如果不区分两者，频谱斜率或整体背景功率变化可能被误认为 β 振荡增强或减弱。

因此，未来的 STN–FOG 分析应同时报告：

- 固定频带功率；
- 个体化振荡峰；
- 振荡峰振幅和带宽；
- periodic/aperiodic 分解；
- burst duration、rate、amplitude；
- burst interval variability；
- Sample Entropy 与 inter-burst interval entropy。

这不是说 aperiodic activity 已经被证明是 FOG 的重要机制，而是一个目前证据不足、值得补充的分析维度。

---

## 二十四、FOG 神经标志物的跨层级整合

现有研究支持把 FOG 相关信号分为四个层级。

<box border radius="lg" padding={3} gap={3}>
  <box gap={1}>
    **第一层：患者易感性**

    <text color="secondary" size="sm">数周、数月乃至长期的患者表型</text>
    - FOG-Q、临床亚型
    - 静息 STN α、高 β 活动
    - 步态自动化能力
    - 多巴胺能与非多巴胺能损伤
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    **第二层：步态状态**

    <text color="secondary" size="sm">单次步行任务或数个步态周期</text>
    - STN 低 β 去同步化
    - β burst duration
    - STN-皮层耦合
    - STN 与下肢 EMG 的协调
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    **第三层：状态转换**

    <text color="secondary" size="sm">冻结前数秒至多个步态周期</text>
    - 高 β 动态
    - θ–α coupling 改变
    - gait-cycle phase abnormalities
    - burst timing 和熵变化
  </box>
  <divider color="subtle"/>
  <box gap={1}>
    **第四层：冻结事件**

    <text color="secondary" size="sm">冻结开始、维持及恢复</text>
    - STN 神经活动变化
    - 皮层-STN 解耦
    - 拮抗肌共同收缩
    - 异常运动停止及恢复时序
  </box>
</box>

这四个层级应当使用不同的统计模型和临床终点。

不能将患者间 FOG-Q 相关性直接当作发作预测准确率，也不能将发作预测准确率直接当作治疗有效性。

---

# STN–FOG 研究报告工作稿｜第 5 轮

**本轮重点：进一步验证竞争性机制、引入运动输出和感觉反馈证据、建立证据等级体系，以及设计能够排除替代解释的关键实验。**

## 二十五、补充关键证据：STN 与 SNr 在步态中的功能并不相同

### 25.1 Gulberti et al., 2023：人体 STN 与 SNr 单神经元记录

[R37] *Subthalamic and nigral neurons are differentially modulated during parkinsonian gait.*

- PMID：36730026。
- DOI：10.1093/brain/awad006。
- 12 名 PD 患者。
- 术中微电极记录。
- 记录 STN、SNr 和邻近区域的单单位及多单位活动。
- 采用仰卧踏步任务。
- 分析运动启动、停止提示、脚跟着地和步态不规则。

主要发现：

| 神经结构 | 运动执行相关 | 注意力提示相关 |
|---|---|---|
| STN | 24% 的神经元出现活动调节 | 8% |
| SNr | 不同于 STN 的运动调节模式 | 15% 的响应神经元出现注意相关变化 |

另外：

- 正常踏步期间 STN 神经活动更加规则。
- 正常踏步期间 β 振荡下降。
- 出现冻结样步态不规则时，β 振荡增加。
- SNr 活动更多体现注意和动作选择方面的调节。

这项研究的重要意义在于，它提供了人体单神经元层面的证据，支持 STN 与 SNr 在步态控制中承担不同但相互关联的功能。

但必须强调，它使用的是仰卧踏步，而不是自然直立行走；冻结样运动不规则也不能直接等同于临床 FOG。

因此，它是人体神经生理机制证据，而非完整的自然 FOG 发作证据。[R37] <Cite refs={["turn816203search0","turn816203search1"]}/>

### 25.2 Breu et al., 2022：STN 对拮抗肌运动输出的影响

[R38] *People With Parkinson's Disease and Freezing of Gait Show Abnormal Low Frequency Activity of Antagonistic Leg Muscles.*

- PMID：35153698。
- DOI：10.3389/fnhum.2021.733067。
- 9 名 FOG 患者。
- 16 名健康对照。
- 同步研究胫骨前肌（TA）和腓肠肌（GA）的频域 EMG。
- 比较 STN-DBS、SNr-DBS 和刺激关闭。

主要发现：

- FOG 患者 TA 和 GA 的 α、低 β 肌肉活动均高于健康对照。
- 这种异常在正常行走期间就存在。
- 冻结期间并没有表现为完全不同的肌肉频谱状态。
- STN-DBS 能降低这种异常活动。
- SNr-DBS 没有产生同样的肌电调节效果。

这里有一个重要的逻辑：

如果异常肌肉活动在冻结前的正常步行阶段就存在，那么它可能是 FOG 易感性的组成部分，而不是冻结发生后的简单结果。

但由于没有同步 STN LFP，不能据此断言 STN β 功率直接导致 TA、GA 的异常活动。[R38] <Cite refs={["turn652765search0","turn652765search1"]}/>

### 25.3 这一证据对竞争模型的影响

R37 和 R38 使 H1、H2、H3 之间的关系更加清楚：

- H1：STN 的病理性同步活动可能限制正常运动输出。
- H2：皮层-STN 信息协调异常可能导致步态执行失败。
- H3：STN 与 SNr 可能分别参与运动和注意控制，二者的整合失调可能增加 FOG 易感性。

它们并不是同一个机制。

尤其不能将 STN 与 SNr 作为同一种结构的替代记录点。

---

## 二十六、感觉反馈和运动自动化：为什么 FOG 患者仍然能够骑自行车？

这是一条重要的交叉研究方向。

FOG 患者往往仍然能够完成某些节律性运动，例如骑自行车，尽管其行走和转弯能力明显受损。

这提示步态和骑行可能依赖不同程度的皮层控制、感觉反馈和运动自动化。

### 26.1 Storzer et al., 2017：骑行对 STN β 的影响

[R39] *Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia.*

- PMID：28892573。
- DOI：10.1002/ana.25047。
- 13 名患者。
- 5 名 Freezer、8 名 Non-freezer。
- 记录 STN LFP。
- 比较骑行与步行。

主要发现：

- Non-freezer 在步行和骑行时均表现为 STN β 功率下降。
- 骑行产生更强的整体 β 抑制。
- Freezer 也出现总体 β 功率下降。
- 但 Freezer 在运动启动时出现约 18 Hz 的窄带功率增加。

这与 Chen 等人的低 β 易感步态研究相互呼应。

尤其重要的是：

整体 β 功率下降，并不代表所有 β 频率成分都下降。

患者可能在整体 β 去同步化的同时，仍保留特定低 β 频率的异常同步化。[R39] <Cite refs={["turn909154search2","turn909154search8"]}/>

### 26.2 Bougou et al., 2024：主动与被动骑行

[R40] *Active and Passive Cycling Decrease Subthalamic β Oscillations in Parkinson's Disease.*

- PMID：37860957。
- DOI：10.1002/mds.29632。
- 12 名患者。
- 6 名 FOG、6 名非 FOG。
- 记录双侧 STN LFP。
- 比较主动骑行、被动骑行。

主要发现：

- 主动和被动骑行均明显降低 STN β 活动。
- FOG 患者的 β 抑制更明显。
- 主动骑行比被动骑行具有更强的高 γ 活动。
- β 抑制不依赖于骑行节律频率。

这提示感觉反馈本身可能足以调节 STN β 活动，而不完全依赖自主运动输出。

但不能据此认为被动骑行已经证明可以治疗自然行走中的 FOG。

**机制推断：** 外部连续感觉输入可能帮助患者绕过部分受损的内部步态生成机制，减少对高层级动作规划和持续运动选择的依赖。[R40] <Cite refs={["turn909154search0","turn909154search7"]}/>

### 26.3 对 FOG 机制研究的启示

未来实验应比较：

- 主动行走；
- 被动下肢运动；
- 主动骑行；
- 被动骑行；
- 外部节律提示行走；
- 无提示行走。

如果外部感觉输入能够在不显著改变运动意图的情况下，恢复 STN β 去同步化和皮层-STN 协调，那么就可以更有力地支持感觉运动反馈机制。

---

## 二十七、DBS 频率研究的进一步扩展：Variable Frequency Stimulation

不能只把 DBS 参数研究理解为 60 Hz 对 130 Hz。

Jia 等人 2024 年发表的研究提供了一个值得纳入的第三种刺激策略。

[R41] *Variable frequency deep brain stimulation of subthalamic nucleus to improve freezing of gait in Parkinson's disease.*

- PMID：38948151。
- DOI：10.1093/nsr/nwae187。
- 28 名 PD 患者。
- 双侧 STN-DBS。
- 受试者在传统 HFS 下仍有 FOG。
- 比较 DBS OFF、HFS、LFS 和 Variable Frequency Stimulation（VFS）。
- 随访 6 个月及 12 个月。

VFS 的设计：

- 在高频刺激和低频刺激之间交替。
- 每 50–300 秒切换一次刺激模式。
- 尝试同时保留 HFS 对震颤、僵硬和运动迟缓的控制，以及 LFS 对步态和轴性症状的潜在优势。

研究发现：

- VFS 的 TUG 时间优于 HFS 和 LFS。
- FOG 次数也优于 HFS 和 LFS。
- VFS 对步态的改善在 6 个月和 12 个月随访中仍然存在。

但这项研究不能视为严格的随机对照证据：

- 研究并没有对不同刺激条件进行随机分组。
- 没有维持所有条件下相同的 TEED。
- 随访没有对照组。
- 不同刺激条件之间可能存在 carry-over effects。

因此，VFS 的结果值得后续试验验证，但尚不能认定其已优于优化后的常规刺激。[R41] <Cite refs={["turn851629search1","turn851629search2"]}/>

---

## 二十八、重新评估现有证据：哪些结果真正具有因果解释力？

现在可以建立一个比简单的文献分类更严格的证据等级。

| 证据等级 | 研究类型 | 典型研究 | 可以得出的结论 |
|---|---|---|---|
| E1 | 横断面患者间相关 | Toledo 2014 | 某些 STN 活动与 FOG 表型相关 |
| E2 | 同一患者内行为状态相关 | Syrkin-Nikolau 2017、Pozzi 2019 | STN 活动随步态和冻结状态改变 |
| E3 | 发作前预测 | Collomb-Clerc 2025、部分 burst 研究 | 某些神经指标可以预示冻结 |
| E4 | 干预后神经活动和行为共同改变 | Yin 2022、Breu 2022 | 刺激可以改变网络指标和临床表现 |
| E5 | 特定神经标志物驱动的闭环干预 | Wilkins 2025 | 具备初步的生物标志物干预可行性 |
| E6 | 选择性扰动某一神经机制并验证行为变化 | 目前缺乏充分人体证据 | 才能较有力地证明特定机制的因果作用 |

特别需要说明：

E4 不自动等于 E6。

例如，STN-DBS 同时降低皮层 PAC 和 FOG，可能意味着：

1. PAC 下降介导 FOG 改善；
2. PAC 下降只是其他网络变化的伴随现象；
3. DBS 同时作用于 PAC 和另一个独立的步态控制机制。

Yin 等人实际上也指出，在 PAC 水平相近的条件下，刺激仍然能够降低冻结严重度。因此 PAC 的下降并不能解释 DBS 的全部治疗效果。

这一点对 H2 和 H5 的机制边界尤其重要。[R35]

---

## 二十九、现有研究的主要系统性缺陷

对现有文献进行横向审查后，我认为有八个必须正视的问题。

### 29.1 FOG 定义和标注标准不统一

研究中存在：

- 临床观察者定义；
- FOG-Q；
- MDS-UPDRS 评分；
- Freezing Index；
- IMU 加速度指标；
- EMG 异常；
- 研究者根据视频人工标注。

这些方法测量的对象不完全一致。

特别是 trembling-in-place 和 akinetic freezing 可能有不同的神经活动表现。

因此未来必须保留 FOG 亚型标签，而不能仅仅建立一个二分类 FOG/non-FOG 标签。

### 29.2 研究对象存在严重的样本选择问题

许多研究只纳入：

- DBS 后仍然有 FOG 的患者；
- 术中能够完成步态任务的患者；
- 能够在实验室中成功诱发 FOG 的患者；
- 能够完成双任务的患者。

这意味着目前的研究样本未必代表所有 PD 患者。

### 29.3 伪重复问题

一个患者可以提供几十次冻结事件、数百个步态周期和多个电极接触点。

这些数据不能被当成数百个独立患者。

如果模型没有正确处理受试者层级，就会低估统计不确定性。

### 29.4 电极位置和组织覆盖并不一致

传统环形电极不能精确区分 STN 的所有功能亚区。

此外，LFP 具有空间扩散和体积传导问题。

因此即使某个接触点位于后部 STN，也不能认为它只反映该区域的局部神经活动。

### 29.5 DBS 伪迹和运动伪迹

FOG 发生时：

- 下肢肌肉活动改变；
- 电极与导线可能产生机械运动；
- 身体姿势改变；
- DBS 刺激可能引入电学伪迹。

这些因素都可能影响高频功率、γ 活动和跨频耦合分析。

### 29.6 研究时间窗不同

1.5 秒、6 秒、单步态周期和整个冻结事件得到的频谱结果可能不同。

未来应统一报告不同时间窗的结果，而不是仅选择最显著的时间窗。

### 29.7 缺乏独立外部验证

机器学习模型在一个中心、一个设备、一个任务中表现良好，不代表能应用于其他中心或日常生活。

例如，2026 年五人队列的 STN-LFP FOG 检测研究虽然检测到 29 次冻结中的 24 次，但其特征重要性随患者及诱发条件改变。

这说明跨患者、跨环境泛化仍是核心难题。[R42]

### 29.8 机制模型之间缺少直接竞争实验

大部分研究只测试自己提出的一个候选指标。

目前缺少在同一患者、同一实验中同时比较：

- β burst；
- θ–α coupling；
- M1 PAC；
- STN 空间分区；
- EMG；
- 步态周期相位；
- 认知负荷。

这使得多个机制模型都能解释同一组现象，却很难判断哪个机制真正具有独立解释力。

---

## 三十、能够区分 H1–H5 的关键实验设计

这是我认为整个研究最有价值的下一步。

建议设计一项前瞻性、多中心、纵向、同步多模态神经生理研究。

<box border radius="lg" padding={3} gap={3}>
  **研究设计概览**

  <title size="xl" color="default">60–80 名 PD 患者</title>
  <text color="secondary" size="sm">建议招募具有不同 FOG 表型的双侧 STN-DBS 患者，兼顾有 FOG 和无 FOG 对照。</text>
  <divider color="subtle"/>
  **同步记录**
  - 双侧 STN LFP
  - 皮层 EEG 或可行时 ECoG
  - 双侧下肢 EMG
  - IMU 和运动学
  - 步态周期及转弯相位
  <divider color="subtle"/>
  **实验条件**
  - 药物 OFF / ON
  - DBS OFF / HFS / LFS
  - 单任务 / 双任务
  - 正常行走 / 转弯 / 过门 / 障碍物
  <divider color="subtle"/>
  **主要终点**

  冻结发生风险、冻结前预测时间、冻结持续时间、步态周期稳定性及神经活动恢复速度。
</box>

### 30.1 主要分析方法

统一提取：

1. STN α、低 β、高 β 和 θ 功率；
2. β burst duration、amplitude、rate；
3. inter-burst interval entropy；
4. Sample Entropy；
5. periodic/aperiodic 功率分解；
6. 皮层-STN coherence；
7. M1 beta-gamma PAC；
8. STN-EMG coherence；
9. 步态周期相位依赖的神经活动；
10. 后部与中央 STN 的空间差异。

### 30.2 必须预注册的统计分析

建议：

- 采用 hierarchical mixed-effects models；
- 患者作为最高层随机效应；
- 电极位置、步态周期和事件作为嵌套层级；
- 预先规定冻结 onset 的判定方法；
- 使用独立患者进行外部验证；
- 采用 leave-one-subject-out 作为内部泛化测试；
- 对所有神经特征执行多重比较校正；
- 通过消融分析检验单一指标是否具有独立贡献。

### 30.3 机制区分的关键结果

| 观察结果 | 更支持的模型 |
|---|---|
| 长 β burst 先于冻结，且选择性干预能降低冻结 | H1 |
| 皮层-STN coupling 变化比局部功率更早、更稳定 | H2 |
| 认知负荷显著改变冻结风险及联合区活动 | H3 |
| 步态相位和神经时间结构比平均功率更有预测力 | H4 |
| 个体化 VTA/纤维连接能够预测刺激疗效 | H5 |

需要强调：同一实验结果可能支持多个模型。应通过预注册的模型比较和选择性扰动，而不是单纯比较相关系数大小，来决定哪种机制具有独立解释力。

# STN 神经活动与帕金森病冻结步态（FOG）：完整研究报告

<text color="secondary" size="sm">最终研究报告｜证据检索截止日期：2026 年 11 月 13 日</text>

研究领域：功能神经外科、DBS、帕金森病、步态电生理。

研究对象：丘脑底核（STN）、黑质网状部（SNr）、运动皮层及相关皮层-基底节-脑干运动网络。

研究重点：STN 局部场电位、神经振荡、β burst、神经网络耦合、FOG 发作动态，以及 DBS 对这些过程的调节。

---

# 第一部分：研究报告正文

## 1. 摘要

冻结步态（freezing of gait, FOG）是帕金森病（Parkinson's disease, PD）最具挑战性的轴性运动症状之一。STN-DBS 能够显著改善震颤、僵硬和运动迟缓，但其对 FOG 的效果高度异质：部分患者改善，部分患者无变化，还有一部分患者出现新的或加重的 FOG。

本研究综合用户提供的 82 篇文献摘要及多份全文文本，对相关原始研究进行进一步检索、交叉核对和机制综合，重点分析 STN 神经活动与 FOG 的关系。

### 1.1 核心发现

**第一，STN β 活动与 FOG 有关，但不存在一个适用于所有患者和所有行为阶段的统一 β 功率异常模式。**

已有研究发现：

- FOG 患者静息时高 β 功率可能升高。
- FOG 易感患者行走时可能出现约 18 Hz 的窄带低 β 异常。
- Freezer 在无冻结的行走期间可能表现为较低的平均 β 功率，但较高的 β Sample Entropy。
- 延长的 β burst 与 FOG 易感性及冻结相关。
- 部分真实 FOG 事件期间 STN β 功率增加。
- 另一些真实步行研究却没有发现冻结期间 STN β 功率或 burst duration 显著改变。

这些发现不一定互相矛盾，因为它们测量的时间尺度、行为状态和神经信号属性不同。

**第二，皮层-STN 网络协调可能比单纯 STN 局部功率更接近 FOG 的核心机制之一。**

尤其是：

- 正常行走时存在低频皮层-STN 同步。
- FOG 前可能出现 θ–α 频段解耦。
- 转弯冻结存在运动前区-STN 耦合时序异常。
- M1 的 β-γ phase-amplitude coupling（PAC）与冻结风险及严重度有关。

**第三，STN 内不同亚区可能具有不同作用。**

后部感觉运动区、中央联合区及腹侧区域，可能分别参与运动执行、认知-运动整合及情绪调节。不同空间分区与不同频段的关系，可能解释一部分研究冲突。

**第四，FOG 可能同时涉及异常的下行运动输出。**

STN 活动与拮抗肌共同收缩、异常肌肉募集及运动节律中断有关。STN 与 SNr 在运动执行和注意力控制方面可能具有不同作用。

**第五，DBS 干预证据支持患者特异性和网络特异性。**

60 Hz 低频刺激能够改善部分 HFS 下仍存在 FOG 的患者，但不是普遍有效。STN-SNr 联合刺激、θ 频率刺激及 β burst 驱动的 adaptive DBS 均有初步证据，但尚未建立普遍优于标准优化 STN-DBS 的临床疗效。

### 1.2 总体判断

现阶段最合理的解释是：

> FOG 是一种具有明显个体差异、行为阶段依赖性和网络状态依赖性的运动控制障碍。STN 是其中的重要节点，其局部振荡、神经活动时间结构、皮层连接及下行运动输出共同参与 FOG 的发生和维持。

但目前还不能证明 STN β 活动增强是所有 FOG 的必要或充分原因。

---

## 2. 研究范围与资料检索方法

### 2.1 已使用的资料

本研究使用了两类资料：

**第一类：用户提供的研究材料**

- 82 篇文献的题目和摘要。
- 多份开放获取全文文本合集。
- 提供的 PDF/HTML 全文材料中可检索的相关研究。
- 其中涉及原始电生理研究、DBS 干预研究、影像研究、临床研究和综述。

**第二类：独立外部检索和核验**

针对重要研究，进一步检索 PubMed、PubMed Central、期刊原文页面和公开预印本记录。

主要检索方向：

| 检索主题 | 主要关键词 |
|---|---|
| STN 神经活动 | STN LFP, single-unit, multi-unit activity |
| β 振荡 | beta power, low beta, high beta |
| β burst | burst duration, burst amplitude, burst rate |
| FOG 事件 | freezing onset, pre-freezing, gait freezing |
| 网络活动 | coherence, cortico-STN coupling, PAC |
| 步态行为 | gait initiation, turning, dual-task, walking |
| 空间定位 | sensorimotor STN, associative STN, limbic STN |
| DBS | high frequency, low frequency, adaptive DBS |
| 交叉结构 | SNr, PPN, MLR, EMG, cortical ECoG |

### 2.2 纳入标准

重点纳入：

1. 人体 STN LFP 或神经元放电原始研究。
2. 同步记录步态及 STN 活动的研究。
3. 直接比较 FOG 与正常行走的研究。
4. 研究 FOG 易感性、发作前动态和发作过程的研究。
5. 具有 DBS 干预或药物干预的研究。
6. 能够提供 STN 空间分区或网络连接证据的研究。
7. 对解释 STN–FOG 关系具有直接价值的皮层、SNr、EMG 和运动控制研究。

动物研究和计算模型仅作为机制辅助证据，不与人体原始研究等量看待。

### 2.3 证据等级

本报告采用以下分层：

| 等级 | 证据类型 | 解释 |
|---|---|---|
| E1 | 横断面相关 | 不同患者之间的神经活动差异 |
| E2 | 状态相关 | 同一患者不同运动状态之间的差异 |
| E3 | 时间预测 | 神经活动在 FOG 前出现变化 |
| E4 | 干预调节 | 改变药物或刺激后神经活动和行为共同变化 |
| E5 | 生物标志物驱动干预 | 根据神经活动实时调节 DBS |
| E6 | 机制选择性因果验证 | 选择性改变候选机制并证明行为变化由该机制介导 |

目前 E1–E5 均有一定程度的研究支持，但 E6 级别的充分人体证据仍然不足。

本报告属于结构化证据综合，而不是声称已经完成符合 PRISMA 标准的系统综述。现有资料的数据库覆盖、全文获取和重复队列核查仍有局限。

---

## 3. FOG 的研究对象必须进行分层

FOG 是一种临床表现，不是单一的神经生理状态。

### 3.1 临床亚型

| 亚型 | 特征 | 可能涉及的机制 |
|---|---|---|
| OFF-FOG | 多巴胺不足时出现，左旋多巴部分改善 | 多巴胺能运动控制障碍 |
| ON-FOG | 药物 ON 状态出现或加重 | 多巴胺调节失衡、异常运动控制 |
| ON/OFF-FOG | 药物状态改变后仍存在 | 非多巴胺能网络损伤 |
| Stimulation-induced FOG | 刺激开启后出现或恶化 | 电流扩散、网络误募集、刺激-药物交互 |

### 3.2 发作阶段

建议把 FOG 分成六个研究阶段：

1. Susceptibility：长期易感性。
2. Pre-FOG：冻结前的行为及神经变化。
3. Onset：冻结开始。
4. Maintenance：冻结维持。
5. Termination：冻结结束。
6. Recovery：正常行走恢复。

特别重要的是：

**患者具有 FOG 易感性，不等于其每次行走都会发生 FOG。**

这也是横断面研究与事件研究结果不一致的主要来源之一。

---

## 4. STN β 振荡：现有证据及其真正含义

### 4.1 FOG 患者静息状态的高 β 活动

[R1] Toledo et al., 2014：

*High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease.*

- PMID：24361601。
- 22 名患者。
- FOG：14 人。
- Non-FOG：8 人。
- 记录 STN LFP 与皮层 EEG。
- 比较低 β、高 β 及皮层-STN coherence。

结果：

- FOG 患者 STN 高 β 功率显著升高。
- 左旋多巴降低高 β 活动。
- FOG 同时减轻。
- 高 β coherence 更偏向皮层中线区域。

这支持高 β 活动与 FOG 表型相关。

但该研究不能证明高 β 是单次冻结发作的直接原因，因为主要分析的是患者间差异及药物状态变化。

### 4.2 行走期间约 18 Hz 的异常活动

[R2] Storzer et al., 2017：

*Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia.*

- PMID：28892573。
- DOI：10.1002/ana.25047。
- 13 名患者。
- 5 名 Freezer、8 名 Non-freezer。

研究发现：

- 正常行走期间，非 FOG 患者 β 活动下降。
- Freezer 也表现为总体 β 下降。
- 但 Freezer 存在约 18 Hz 的窄带活动增强。
- 骑行时整体 β 抑制更明显。

这意味着整体 β 功率和窄带 β 活动可以出现相反变化。

该研究为低 β 活动与 FOG 易感性之间的关系提供了重要证据。

### 4.3 β 神经活动复杂度

[R3] Syrkin-Nikolau et al., 2017：

*Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease.*

- PMID：28890315。
- DOI：10.1016/j.nbd.2017.09.002。
- 14 名患者。
- 8 名 Freezer。
- 药物 OFF、DBS OFF。
- 自由行走、踏步、转弯和障碍物任务。

结果：

- Freezer 在没有发生冻结的行走期间，平均 β 功率低于 Non-freezer。
- Freezer 的 β Sample Entropy 更高。
- 真实 FOG 期间，α Sample Entropy 高于其无冻结行走状态。

作者提出，部分 β 活动可能是正常步态节律组织的一部分。

因此，完全抑制 STN β 活动不一定是最佳治疗目标。

### 4.4 β burst duration

[R4] Anidi et al., 2018：

*Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease.*

- PMID：30196050。
- DOI：10.1016/j.nbd.2018.09.004。
- 12 名患者。
- 8 名 Freezer、4 名 Non-freezer。
- 比较无刺激、60 Hz 和 140 Hz。

结果：

- Freezer 在步行期间存在较长的 β burst。
- 延长的 burst 与异常步态有关。
- STN-DBS 能够缩短较长的 burst。
- 较短的生理性 burst 不具有同样的调节模式。

这项研究提出一个重要的治疗原则：

**治疗目标可能是选择性缩短病理性长 β burst，而不是全面抑制 β 活动。**

### 4.5 低 β 和 θ 与易感步态

[R5] Chen et al., 2019：

*Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease.*

- PMID：31494286。
- DOI：10.1016/j.nbd.2019.104605。
- 15 名患者。
- 比较单任务和双任务行走。
- 使用 iFOG 指数识别易感步态。

结果：

- 15–21 Hz 低 β 活动与 FOG 易感步态有关。
- 5–8 Hz θ 活动也与易感步态有关。
- 低 β 变化分布于 STN。
- θ 活动主要位于腹侧 STN 和/或 SNr。

但实际实验中只有少数患者出现真正的冻结，因此应把这项研究归类为易感性证据，而不是充分的 FOG 发作证据。

### 4.6 β 证据的综合判断

| 神经指标 | 现有证据 | 主要限制 |
|---|---|---|
| 平均高 β 功率 | 与 FOG 患者表型有关 | 患者间研究不能直接解释单次发作 |
| 窄带约 18 Hz | 与 FOG 易感步态有关 | 研究任务和频带定义不统一 |
| β burst duration | 与 Freezer 步态及部分 FOG 相关 | 阈值和 burst 算法不同 |
| β Sample Entropy | 与 Freezer 步态复杂度有关 | 不能直接解释因果机制 |
| Inter-burst interval entropy | 新研究提示冻结前下降 | 样本仅 4 人，预印本 |

因此，当前证据支持 STN β 活动异常，但不支持将其简化为“FOG 时 β 功率必然升高”。

<Cite refs={["turn652765search4","turn909154search2","turn183998search2","turn183998search0","turn183998search3","turn851629search0"]}/>

---

## 5. FOG 发作前和发作期间的直接电生理证据

这一部分是研究问题的核心。

### 5.1 Pozzi et al., 2019：STN 局部功率没有显著变化，但网络解耦明显

[R6] *Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics.*

- PMID：31505548。
- DOI：10.1093/brain/awz141。
- 7 名患者。
- 其中 5 人在研究中出现 FOG。
- 共记录 14 次冻结，累计 127 秒。
- 所有冻结均发生在接近门口时。

主要结果：

| 指标 | FOG vs 正常行走 |
|---|---|
| STN θ–α 功率 | 无显著差异 |
| STN β 功率 | 无显著差异 |
| β burst duration | 无显著差异 |
| 双侧 STN β coupling | 有变化趋势，未达显著 |
| 皮层-STN θ–α coupling | 明显解耦 |

这种低频解耦：

- 在 FOG 前开始。
- 冻结期间持续。
- 恢复正常行走后消失。
- 主要出现在多巴胺能支配较弱的一侧。
- 涉及 SMA、M1 和顶叶运动相关区域。

研究还发现，这种解耦不能简单归因于正常主动停止或成功通过门口。

这是支持 FOG 网络协调失败模型的重要直接证据。

### 5.2 Georgiades et al., 2019：STN 多单位活动在冻结 onset 增加

[R7] *Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing.*

- PMID：31665229。
- DOI：10.1093/brain/awz325。
- 8 名患者。
- 术中虚拟现实诱发 FOG。
- 使用微电极记录 STN MUA。
- 同步记录下肢 EMG。

结果：

- 冻结 onset 附近出现 STN 多单位异常活动增加。
- θ 和 β 节律活动增加。
- 随后出现异常下肢肌肉放电。
- 与主动停止相比，FOG 存在不同的 STN 活动模式。

这为 STN 参与 FOG onset 提供了时间顺序证据。

但 MUA 与慢性 DBS 电极 LFP 不是同一信号，不能把该研究直接作为 LFP β 功率增加的证明。

### 5.3 Liu et al., 2022：真实步行中的 β 功率增加

[R9] *Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait.*

- PMID：35310098。
- DOI：10.3389/fnins.2022.795417。
- 8 名患者。
- 41 次 TUG 测试。
- 其中 30 次出现冻结。
- 21 份冻结记录达到较好的信号质量标准。

结果：

- STN β 功率在 FOG 期间高于非 FOG 期间。
- 皮层 ECoG 平均功率没有同样显著的差异。
- 皮层与 STN 存在高 β 和 γ coherence。

需要特别注意：

研究发现的显著 coherence 是相对于 shuffled surrogate 的比较，不等于证明 FOG 时 coherence 必然高于正常行走。

### 5.4 Yin et al., 2022：皮层 PAC 与 FOG

[R10] *Cortical phase-amplitude coupling is key to the occurrence and treatment of freezing of gait.*

- PMID：35441231。
- DOI：10.1093/brain/awac121。
- 16 名患者。
- 同步 M1 ECoG、STN-DBS 和三维步态追踪。
- 451 次 TUG 测试。

结果：

- M1 高 β-γ PAC 出现在包含 FOG 的试次中。
- 即使某个冻结试次中有一段未冻结的正常行走，其 PAC 仍可能异常。
- PAC 与 FOG 严重度相关。
- STN-DBS 降低异常 PAC，同时改善 FOG。

但在 PAC 水平相似的情况下，DBS 仍能改善 FOG。

因此，PAC 不能解释全部 DBS 治疗效果。

### 5.5 Klocke et al., 2024：STN 与下肢肌肉输出的异常协调

[R17] *Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease.*

- PMID：39470410。
- DOI：10.1093/brain/awae223。
- 12 名患者。
- 同步 STN LFP、EMG 和步态运动学。
- 包括主动停止对照。

结果：

- 冻结前及冻结期间出现 STN activation-deactivation 异常。
- 腓肠肌与 STN 的 coherence 在冻结前增加。
- 拮抗肌互反控制受损。
- 拮抗肌共同收缩增加。
- 腓肠肌募集和激活时序异常。

这提示 FOG 可能涉及从皮层-基底节网络到下肢运动神经元的时序传递障碍。

### 5.6 这一组研究的共同结论

真实冻结事件期间的 STN 功率变化并不完全一致。

但越来越多证据指向：

- 运动相关神经活动的动态组织异常；
- 皮层-STN 协调改变；
- 神经活动与肌肉输出之间的时序失调。

<Cite refs={["turn183998search1","turn439670search2","turn614724search3","turn347724search7","turn439670search0"]}/>

---

## 6. 其他频段：α 和 θ 不能被忽略

### 6.1 θ 活动的相反结果

[R8] Shine et al., 2014：

*Abnormal patterns of theta frequency oscillations during the temporal evolution of freezing of gait in Parkinson's disease.*

- PMID：24099920。
- DOI：10.1016/j.clinph.2013.09.006。
- 24 名 FOG 患者。
- 四导联头皮 EEG。

结果：

- FOG 时额叶和中央区域 θ 功率增加。
- 行走向冻结的转换期间，额叶和中央区域 θ 耦合增加。

[R5] Chen et al. 2019 则发现易感步态中的 STN 低 β 和 θ 活动增加。

[R33] Xie et al., 2025 的 5 Hz STN 刺激研究还发现，θ 频率刺激可以改善 FOG 患者的认知冲突解决表现。

而 Georgiades 等人 2023 年的术中研究：

*Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease.*

- PMID：37226972。
- DOI：10.1002/mds.29455。

发现认知提示之后，未来出现冻结或显著减速的试次中 STN θ 活动降低。

这并不必然构成生理学矛盾。

因为这些研究分别测量：

- 皮层 θ；
- STN LFP θ；
- STN MUA θ；
- 认知提示后；
- 冻结 onset；
- 易感步态；
- 已经发生的冻结。

**因此 θ 的功能意义可能具有脑区、信号类型和行为阶段特异性。**

### 6.2 α 活动

[R20] Fim Neto et al., 2025：

*Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease.*

- PMID：39884164。
- DOI：10.1016/j.clinph.2025.01.005。
- 23 名患者。
- 14 名 FOG、9 名非 FOG。
- 静息 STN LFP。

结果：

- FOG 患者 α 功率更高。
- α burst amplitude 与 FOG 严重度相关。
- 高 β burst amplitude 也与 FOG 严重度相关。

但静息状态结果不能直接解释真实冻结发生时的 α 活动。

### 6.3 认知和情绪相关的 STN θ

[R19] Klocke et al., 2026：

*Cognitive and Emotional Determinants of Subthalamic Oscillations During Freezing While Turning in Parkinson's Disease.*

- PMID：42236313。
- DOI：10.1111/ejn.70570。
- 13 名患者。

发现：

- 转弯冻结期间 STN θ 功率与焦虑程度正相关。
- θ 功率与 MoCA 认知评分负相关。
- 正常转弯期间没有相同的症状关联。
- α 和 β 活动没有显示同样的关系。

这支持认知-情绪因素对 STN 活动的调节作用。

---

## 7. STN 的空间分区及网络连接

### 7.1 Collomb-Clerc et al., 2025：较大样本的空间分区电生理研究

[R16] *Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease.*

- PMID：40709562。
- DOI：10.1002/ana.70003。
- 38 名 PD 患者。
- 其中 35 人报告日常生活中有 FOG。
- 24 名健康对照。
- 267 个有效 STN 双极记录位置。
- 其中 139 个位于后部感觉运动区，128 个位于中央联合区。

研究将步态启动分成：

- Pace：速度和推进能力。
- Rhythm：步态节律。
- Balance：平衡控制。

主要发现：

1. FOG 患者即使在没有发生冻结的步态启动试次中，也存在不同的步态策略。
2. 低 β 与步态节律、平衡之间的关系在 FOG 患者中更加广泛。
3. 低 β 活动关联从后部感觉运动 STN 延伸到中央联合 STN。
4. 临近 FOG 时，后部 STN 高 β 与节律、速度出现异常关联。
5. 中央 STN 高 β 与平衡控制出现异常关联。
6. 左旋多巴部分恢复 STN 活动模式。

这项研究的重要贡献是将 FOG 分成三个状态：

- 无冻结；
- FOG 易感；
- 即将发生 FOG。

它提示 STN 活动不仅与是否冻结相关，也与患者如何组织步态有关。

### 7.2 Temiz et al., 2022：皮层-STN 连接与术后 FOG

[R14] *Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients.*

- PMID：36242900。
- DOI：10.1016/j.parkreldis.2022.10.002。
- 19 名患者。
- 使用个体电极位置、VAT/VTA 和纤维束连接模型。

结果：

- 感觉运动皮层-STN 连接与 FOG 改善相关。
- 前额叶-STN 连接与 FOG 恶化相关。
- 术后 FOG 的个体变化差异很大。

### 7.3 Fan et al., 2023：76 人刺激位置和网络研究

[R15] *Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease.*

- PMID：37701817。
- DOI：10.1093/braincomms/fcad238。
- 76 名 FOG 患者。
- 回顾性研究。
- 双侧 HFS-STN-DBS。
- 使用个体化 VTA 和连接组。

发现：

- STN 背外侧约三分之二区域与 FOG 改善相关。
- 右侧腹内侧区域及左侧中央 STN 周围内囊与 FOG 恶化相关。
- SMA/pre-SMA 相关纤维与 FOG 改善相关。
- mPFC/vlPFC 相关纤维与 FOG 恶化相关。

但结构连接模型通过 LOOCV，而功能连接模型没有通过。

因此，结构连接的预测证据更强，不能把两者视为同等可靠。

### 7.4 刺激位置与记录位置不能混淆

这一点需要特别强调：

- Collomb-Clerc 研究的是 STN 哪个位置的神经活动与步态表现相关。
- Fan 和 Temiz 研究的是 STN 哪个位置的刺激与临床疗效相关。

两者是不同问题。

不能仅凭某个区域 LFP 与 FOG 相关，就认定刺激该区域一定能治疗 FOG。

<Cite refs={["turn347724search4","turn180143search0","turn180143search3"]}/>

---

## 8. DBS 干预证据

### 8.1 高频 STN-DBS 的总体疗效

[R26] Schlenstedt et al., 2017：

*Effect of high-frequency subthalamic neurostimulation on gait and freezing of gait in Parkinson's disease.*

- PMID：27766724。
- DOI：10.1111/ene.13167。
- 系统综述及 Meta-analysis。
- 纳入 16 项步态研究，其中 6 项提供 FOG 评分数据。

研究总体支持 HFS-STN-DBS 对药物 OFF 状态下的步态和 FOG 有改善作用。

但在药物 ON、刺激 ON 状态下，FOG 获益并不稳定。

这与临床上晚期、药物 ON 状态仍存在 FOG 的现象一致。

### 8.2 60 Hz 低频刺激

| 研究 | 样本量 | 主要结果 |
|---|---:|---|
| Moreau 2008 [R21] | 13 | 能量匹配的 60 Hz 高电压条件改善 FOG |
| Phibbs 2014 [R22] | 20 | 60 Hz 与 130 Hz 步幅无显著差异 |
| Khoo 2014 [R23] | 14 | 重新优化接触点后 60 Hz 轴性症状较好 |
| Xie 2015 [R24] | 7 | 60 Hz 改善 FOG 和吞咽 |
| Xie 2018 [R25] | 11 | 长期低频获益存在，但随时间减弱 |
| Conway 2021 [R27] | 14 | 改善部分步态节律指标，但没有普遍改善临床运动终点 |
| Barbosa 2025 [R28] | 17 | 60 Hz 轴性评分较好，但总体 FOG 次数没有显著优于 130 Hz |

综合来看，60 Hz 在部分患者中有价值，但不构成普遍优于 130 Hz 的结论。

### 8.3 药物与刺激之间存在个体特异性交互

[R28] Barbosa et al., 2025：

- 17 名长期 STN-DBS 患者。
- 全部患者在 MedON/StimON 时仍存在 FOG。
- 60 Hz 条件维持相同 TEED。

结果：

- 整体 60 Hz 和 130 Hz 的 FOG 次数没有显著差异。
- 60 Hz 轴性评分更好。
- 9 人在 60 Hz 下的 FOG 改善优于 130 Hz。
- 3 人左旋多巴改善但刺激恶化。
- 5 人刺激改善但左旋多巴恶化。

这证明不同患者的 FOG 可能由不同病理过程主导。

### 8.4 Variable Frequency Stimulation

[R29] Jia et al., 2024：

- 28 名 FOG 患者。
- VFS 在 HFS 和 LFS 之间交替。
- 12 个月随访。
- VFS 在 TUG 和冻结次数方面优于单独 HFS 或 LFS。

但研究没有随机对照，且未保持 TEED 一致，因此应视为值得进一步验证的临床策略。

### 8.5 刺激诱发步态恶化

[R30] Fleury et al., 2016：

*Subthalamic stimulation may inhibit the beneficial effects of levodopa on akinesia and gait.*

- PMID：26887333。
- DOI：10.1002/mds.26545。
- 17 名患者纳入，12 名完成完整评估。

部分刺激接触点位于 STN 背侧和前方邻近结构，刺激可以改善僵硬、震颤，却加重步态及 FOG。

这说明 STN-DBS 的治疗结果取决于实际募集的神经组织，而不只是刺激频率。

### 8.6 β burst 驱动的 adaptive DBS

[R31] Wilkins et al., 2025：

*Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.*

- PMID：40677701。
- DOI：10.1093/braincomms/fcaf266。
- 7 名患者。
- 使用 Summit RC+S。
- 根据个体化 β burst duration 实时调节刺激幅度。

结果：

- aDBS 可行且耐受性良好。
- FOG 时间比例及步态指标较 DBS OFF 改善。
- 整体效果与 cDBS 相近。

这是候选生物标志物驱动干预的初步人体证据。

但尚未证明 aDBS 优于充分优化的 cDBS。

### 8.7 其他值得跟踪的干预

- [R32] Negi et al., 2025：60 Hz beta-burst adaptive DBS，8 人，预印本。
- [R33] Xie et al., 2025：5 Hz STN 刺激改善 FOG 患者冲突解决能力，但不是直接 FOG 疗效试验。
- [R34] Artusi et al., 2025：STN-SNr 随机双盲交叉试验，15 人；NFOG-Q 主要终点没有显著改善。
- [R35] Zhuang et al., 2026：以步态周期为单位的皮层-STN 研究，发现 S1 和 SPL 的低 β 异常及相位依赖变化。
- [R36] Alberts et al., 2026：5 人 STN-LFP 机器学习研究，成功检测 29 次冻结中的 24 次。
- [R37] Beaudoin et al., 2026：4 人预印本，提示冻结前 β burst 时间间隔熵下降。

这些研究拓展了候选神经标志物和干预策略，但证据成熟度不同，不能相互替代。

<Cite refs={["turn614724search1","turn614724search0","turn614724search4","turn851629search1","turn180143search1","turn180143search2","turn905534search0","turn971971search1","turn359279search2","turn851629search0"]}/>

---

## 9. 为什么研究结果存在冲突？

综合上述证据，冲突至少来自九个方面。

### 9.1 患者间差异与同一患者内差异

静息时 Freezer 与 Non-freezer 的差异，不能推导为同一患者冻结前后的变化。

### 9.2 FOG 易感性与真实冻结

iFOG 指数高的步态不一定会发生实际冻结。

Chen 等人的研究主要是易感步态证据，而不是实际冻结事件证据。

### 9.3 行为诱发条件

转弯、过门、双任务、障碍物和踏步可能涉及不同神经网络。

Pozzi 的 14 次冻结全部由过门诱发，而其他研究主要使用转弯和踏步。

### 9.4 分析时间窗

整个冻结期间的平均功率可能掩盖冻结前的短暂变化。

### 9.5 神经信号测量类型

MUA、LFP、ECoG、EEG、EMG 和运动学指标不能直接互换。

### 9.6 STN 空间分区

不同接触点可能记录到不同神经群体。

### 9.7 药物和 DBS 状态

药物 ON/OFF 和刺激 ON/OFF 会改变神经活动。

### 9.8 频带和算法定义

13–20 Hz、15–21 Hz、20–35 Hz 等频段边界并不完全一致。

### 9.9 样本量和统计独立性

重复冻结事件不是独立患者。

例如 38 名患者可以提供数百次步态周期，但真正的受试者层级样本仍是 38 人。

---

## 10. 竞争性机制模型

以下五种模型构成当前最值得检验的竞争性解释。

它们可以共同参与 FOG，但必须能够通过实验被区分。

### H1：STN 病理性 β burst 驱动模型

**核心机制：**

持续时间过长的 β burst 限制运动相关信息处理，使步态执行受到抑制。

**主要支持证据：** [R1]、[R4]、[R7]、[R31]。

**预测：**

- 长 β burst 先于 FOG。
- Burst duration 比平均功率更有预测价值。
- 选择性调节长 burst 能降低冻结风险。
- 正常短 burst 应保留。

**证伪：**

在充分采样和独立验证后，长 β burst 不预测冻结，且选择性改变 burst duration 不影响冻结风险。

### H2：皮层-STN 网络协调失败模型

**核心机制：**

FOG 主要是运动网络之间的动态通信失败。

**主要支持证据：** [R6]、[R10]、[R18]、[R35]。

**预测：**

- 网络耦合变化早于冻结。
- 网络时序特征比局部平均功率更能预测冻结。
- 恢复正确耦合能够改善步态。

**证伪：**

在控制行为阶段和运动伪迹后，网络耦合不再提供独立预测价值，而局部 burst 指标可以独立解释并控制冻结。

### H3：认知-情绪资源竞争模型

**核心机制：**

FOG 患者需要更多认知资源维持步态，当双任务、焦虑和环境复杂度超过资源容量时，步态自动化控制失败。

**主要支持证据：** [R5]、[R19]、[R33]、[R39]。

**预测：**

- 认知负荷和焦虑影响 FOG 风险。
- 联合区和前额叶网络活动随认知负荷变化。
- 不同 FOG 诱发条件具有不同神经标志物。

**证伪：**

控制认知负荷和情绪状态后，相关网络活动不再预测冻结。

### H4：步态相位与神经动力学状态转换模型

**核心机制：**

FOG 是一种动态状态转换，关键在于步态周期中的神经活动时序和相位组织失常。

**主要支持证据：** [R3]、[R18]、[R35]、[R37]。

**预测：**

- 相位依赖指标优于整段频谱平均值。
- 冻结前存在可重复的状态转换轨迹。
- burst 时间间隔和相位稳定性具有独立预测价值。

**证伪：**

在多中心独立验证中，步态相位和神经时间结构不能提供超过传统功率指标的预测价值。

### H5：解剖-网络选择性刺激模型

**核心机制：**

刺激结果由实际募集的神经亚区和纤维通路决定。

**主要支持证据：** [R14]、[R15]、[R30]、[R34]。

**预测：**

- 个体化 VTA 和纤维连接能够预测 FOG 反应。
- 选择性募集运动相关通路能够减少刺激诱发 FOG。
- 不同患者的最佳刺激网络不同。

**证伪：**

前瞻性控制研究中，个体化 VTA 和纤维连接无法预测治疗效果。

### 10.1 五种机制模型的比较

| 模型 | 核心变量 | 主要时间尺度 | 最关键的验证方法 |
|---|---|---|---|
| H1 | β burst duration | 毫秒至秒 | β burst 驱动 aDBS |
| H2 | θ–α coherence | 秒至运动阶段 | 同步皮层-STN 记录 |
| H3 | 认知负荷、θ、联合区活动 | 秒至分钟 | 双任务和情绪负荷实验 |
| H4 | 相位、熵、状态转换 | 多个步态周期 | 步态周期锁定分析 |
| H5 | VTA、纤维连接 | 分钟至长期 | 个体化刺激和连接组预测 |

---

## 11. 推荐的下一阶段研究设计

建议开展多中心、前瞻性、纵向人体研究。

### 11.1 样本设计

目标样本：60–80 名双侧 STN-DBS 患者。

尽量包括：

- 有 FOG 患者；
- 无 FOG 患者；
- OFF-FOG；
- ON-FOG；
- ON/OFF-FOG；
- DBS responsive；
- stimulation-induced FOG。

### 11.2 同步测量

- 双侧 STN LFP。
- 可行时皮层 ECoG，或使用 EEG。
- 下肢 EMG。
- IMU 和三维运动学。
- 步态周期相位。
- 药物及刺激参数。
- 个体化 MRI/CT 电极重建。

### 11.3 实验任务

| 任务 | 主要研究目的 |
|---|---|
| 正常直线行走 | 基础步态控制 |
| 转弯 | 动作切换 |
| 通过门口 | 环境约束 |
| 障碍物 | 运动计划更新 |
| 双任务 | 认知资源竞争 |
| 外部节律提示 | 感觉反馈补偿 |
| 主动/被动骑行 | 运动自动化与感觉输入 |

### 11.4 预注册的主要分析

同时提取：

- STN α、θ、低 β、高 β 功率；
- β burst duration、amplitude、rate；
- inter-burst interval entropy；
- Sample Entropy；
- periodic/aperiodic spectral components；
- cortical-STN coherence；
- M1 PAC；
- STN-EMG coherence；
- 步态相位依赖的振荡变化。

统计方法：

1. 使用分层混合效应模型。
2. 将患者、接触点、步态周期和冻结事件正确嵌套。
3. 使用受试者层级独立验证。
4. 预先定义 FOG onset。
5. 控制多重比较。
6. 进行模型消融分析。
7. 比较单一指标与多模态指标的增量预测价值。

### 11.5 最关键的干预研究

建议进行受试者内随机交叉设计：

- 优化后的连续 HFS；
- 优化后的连续 LFS；
- β burst-driven aDBS；
- 相位或网络状态驱动的 aDBS；
- 随机间歇刺激对照。

应尽可能控制 TEED、个体化 VTA 和药物状态，并明确报告不同刺激方案的运动症状与 FOG 之间的权衡。

最终目标不是寻找最强的神经振荡抑制，而是恢复正常的步态网络协调。

---

## 12. 长期知识积累与持续改进机制

本研究建议建立一个可以持续更新的证据系统，而不是把报告当作一次性文献总结。

### 12.1 四层知识结构

<box border radius="lg" padding={3} gap={2}>
  <box background="surface-secondary" radius="md" padding={3}>
    **第一层：Reference**

    PMID、DOI、题目、年份、发表状态、全文来源。
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3}>
    **第二层：Evidence**

    样本量、任务、药物状态、刺激状态、记录位置、神经指标、结果及局限。
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3}>
    **第三层：Claims**

    跨研究结论、证据等级、反向证据、置信程度。
  </box>
  <box align="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </box>
  <box background="surface-secondary" radius="md" padding={3}>
    **第四层：Hypotheses**

    机制模型、预测、证伪条件、下一步实验。
  </box>
</box>

### 12.2 新证据触发重新评价的规则

| 新证据 | 应重新评价的旧结论 |
|---|---|
| 独立重复 β burst 结果 | H1 的普遍性 |
| 多中心重复网络解耦 | H2 的可靠性 |
| 认知负荷随机干预 | H3 的因果性 |
| 长期步态相位追踪 | H4 的预测价值 |
| 前瞻性个体化 VTA 试验 | H5 的临床可迁移性 |
| 大样本 aDBS 随机对照 | β burst 作为治疗控制信号的有效性 |

### 12.3 持续质量控制

建议每次更新执行：

1. PMID/DOI 核验。
2. 预印本与正式发表版本去重。
3. 队列重叠检查。
4. 研究设计和样本量核验。
5. 原始发现与作者解释分离。
6. 负面结果登记。
7. 反向证据自动关联。
8. 更新相关 Claim 的证据状态。
9. 重新评估 Hypothesis 的预测及证伪条件。
10. 记录修改原因和版本。

### 12.4 本轮研究发现的系统性缺陷及改进

| 缺陷 | 本研究采取的改进 |
|---|---|
| 将不同预印本重复计数 | 按 DOI、PMID 和队列去重 |
| 把易感性误认为真实 FOG | 按行为状态重新分类 |
| 把 MUA 与 LFP 混用 | 明确记录信号类型 |
| 把 coherence 显著误认为状态差异 | 区分 surrogate 和行为条件对照 |
| 把多个冻结事件当作独立患者 | 强调患者层级统计 |
| 将机制推断当作实验结果 | 分离 observation、inference 和 hypothesis |
| 过度强调 β | 纳入 α、θ、PAC、熵和 EMG |
| 把 DBS 疗效简单归因于频率 | 纳入位置、网络、TEED 和药物交互 |

这些改进使证据结构更适合后续更新，但其有效性仍需要通过独立研究和可重复的证据提取流程进行验证。

---

## 13. 最终结论

### 13.1 目前证据最支持什么？

**一、STN 神经活动与 FOG 有明确关联。**

其中 β burst dynamics、低频活动和网络耦合是最值得持续研究的指标。

**二、FOG 不存在单一的 STN 神经电生理签名。**

患者易感性、冻结前状态、冻结期间和恢复期可能对应不同活动模式。

**三、皮层-STN 网络协调是当前最值得重视的机制方向之一。**

但其是否为 FOG 的主要因果机制仍待选择性干预验证。

**四、STN 空间位置和纤维连接具有临床意义。**

刺激位置与网络募集可能解释部分术后 FOG 改善和恶化。

**五、闭环 DBS 是重要的转化方向。**

但目前仍缺乏足够的大样本、长期、跨中心随机对照证据，证明某一 STN 神经标志物驱动的 aDBS 优于最优化连续刺激。

### 13.2 目前不能得出什么结论？

不能认为：

- 所有 FOG 都是 STN β 功率升高导致的。
- FOG 发作期间一定存在持续的 STN 高 β。
- β burst 是唯一或充分的致病机制。
- 皮层-STN 解耦已经被证明是 FOG 的必要原因。
- 中央 STN 活动增强一定代表代偿失败。
- 60 Hz 对所有 FOG 患者都优于 130 Hz。
- STN-SNr 联合刺激已被证明普遍优于 STN 单靶点。
- 当前机器学习 FOG 检测模型已经可以直接应用于临床。

### 13.3 最值得投入研究资源的问题

我认为优先级最高的三个问题是：

1. **同一患者的 STN 局部 β burst 和皮层-STN 网络耦合，谁先发生变化？**
2. **不同 FOG 表型是否对应不同的 STN 空间分区和神经状态转换？**
3. **能否通过选择性调节这些动态活动，而不是单纯提高或降低 DBS 频率，真正减少日常生活中的冻结？**

最终的研究方向应该从寻找一个统一 FOG biomarker，转向建立患者特异性、任务特异性和时间状态特异性的神经控制模型。

---

# 第二部分：结构化证据附录

以下 JSON 是本报告的核心知识索引。它包含经过核对的代表性参考文献、原始证据、跨研究 Claims 和竞争性 Hypotheses。

说明：

- PMID 和 DOI 至少提供一个。
- 预印本明确标注。
- 同一研究的预印本与正式版本不重复计为独立队列。
- `status` 表示当前证据强度，而非统计学显著性。
- `relation` 表示证据对某项 Claim 的支持、反驳或限定。
- `falsifiers` 是未来可实际检验的证伪条件。

## 结构化附录（JSON）

```json
{"references": [{"ref": "R1", "pmid": "24361601", "doi": "10.1016/j.nbd.2013.12.005", "title": "High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease", "year": 2014}, {"ref": "R2", "pmid": "28892573", "doi": "10.1002/ana.25047", "title": "Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia", "year": 2017}, {"ref": "R3", "pmid": "28890315", "doi": "10.1016/j.nbd.2017.09.002", "title": "Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease", "year": 2017}, {"ref": "R4", "pmid": "30196050", "doi": "10.1016/j.nbd.2018.09.004", "title": "Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease", "year": 2018}, {"ref": "R5", "pmid": "31494286", "doi": "10.1016/j.nbd.2019.104605", "title": "Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease", "year": 2019}, {"ref": "R6", "pmid": "31505548", "doi": "10.1093/brain/awz141", "title": "Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics", "year": 2019}, {"ref": "R7", "pmid": "31665229", "doi": "10.1093/brain/awz325", "title": "Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing", "year": 2019}, {"ref": "R8", "pmid": "24099920", "doi": "10.1016/j.clinph.2013.09.006", "title": "Abnormal patterns of theta frequency oscillations during the temporal evolution of freezing of gait in Parkinson's disease", "year": 2014}, {"ref": "R9", "pmid": "35310098", "doi": "10.3389/fnins.2022.795417", "title": "Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait", "year": 2022}, {"ref": "R10", "pmid": "35441231", "doi": "10.1093/brain/awac121", "title": "Cortical phase-amplitude coupling is key to the occurrence and treatment of freezing of gait", "year": 2022}, {"ref": "R11", "pmid": "36070366", "doi": "10.1126/scitranslmed.abo1800", "title": "Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease", "year": 2022}, {"ref": "R12", "pmid": "36730026", "doi": "10.1093/brain/awad006", "title": "Subthalamic and nigral neurons are differentially modulated during parkinsonian gait", "year": 2023}, {"ref": "R13", "pmid": "35153698", "doi": "10.3389/fnhum.2021.733067", "title": "People With Parkinson's Disease and Freezing of Gait Show Abnormal Low Frequency Activity of Antagonistic Leg Muscles", "year": 2022}, {"ref": "R14", "pmid": "36242900", "doi": "10.1016/j.parkreldis.2022.10.002", "title": "Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients", "year": 2022}, {"ref": "R15", "pmid": "37701817", "doi": "10.1093/braincomms/fcad238", "title": "Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease", "year": 2023}, {"ref": "R16", "pmid": "40709562", "doi": "10.1002/ana.70003", "title": "Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease", "year": 2025}, {"ref": "R17", "pmid": "39470410", "doi": "10.1093/brain/awae223", "title": "Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease", "year": 2024}, {"ref": "R18", "pmid": "41131028", "doi": "10.1038/s41531-025-01173-y", "title": "Neural signatures of turn-induced freezing of gait in Parkinson's disease: insights from phase-specific cortico-subthalamic dynamics", "year": 2025}, {"ref": "R19", "pmid": "42236313", "doi": "10.1111/ejn.70570", "title": "Cognitive and Emotional Determinants of Subthalamic Oscillations During Freezing While Turning in Parkinson's Disease", "year": 2026}, {"ref": "R20", "pmid": "39884164", "doi": "10.1016/j.clinph.2025.01.005", "title": "Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease", "year": 2025}, {"ref": "R21", "pmid": "18420482", "doi": "10.1212/01.wnl.0000303972.16279.46", "title": "STN-DBS frequency effects on freezing of gait in advanced Parkinson disease", "year": 2008}, {"ref": "R22", "pmid": "24165197", "doi": "10.1111/ner.12131", "title": "60-Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation", "year": 2014}, {"ref": "R23", "pmid": "24449169", "doi": "10.1002/mds.25810", "title": "Low-frequency subthalamic nucleus stimulation in Parkinson's disease: a randomized clinical trial", "year": 2014}, {"ref": "R24", "pmid": "25540305", "doi": "10.1212/WNL.0000000000001184", "title": "Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD", "year": 2015}, {"ref": "R25", "pmid": "29654112", "doi": "10.1136/jnnp-2018-318060", "title": "Long-term effect of low frequency stimulation of STN on dysphagia, freezing of gait and other motor symptoms in PD", "year": 2018}, {"ref": "R26", "pmid": "27766724", "doi": "10.1111/ene.13167", "title": "Effect of high-frequency subthalamic neurostimulation on gait and freezing of gait in Parkinson's disease", "year": 2017}, {"ref": "R27", "pmid": "34376190", "doi": "10.1186/s12984-021-00921-4", "title": "Low-frequency STN-DBS provides acute gait improvements in Parkinson's disease: a double-blinded randomised cross-over feasibility trial", "year": 2021}, {"ref": "R28", "pmid": "40504072", "doi": "10.1002/mdc3.70170", "title": "Differential Effects of Levodopa and Stimulation on Post-Surgery Freezing of Gait in Subthalamic Nucleus Deep Brain Stimulation Parkinson's Disease Patients: A Clinical and Kinematic Analysis", "year": 2025}, {"ref": "R29", "pmid": "38948151", "doi": "10.1093/nsr/nwae187", "title": "Variable frequency deep brain stimulation of subthalamic nucleus to improve freezing of gait in Parkinson's disease", "year": 2024}, {"ref": "R30", "pmid": "26887333", "doi": "10.1002/mds.26545", "title": "Subthalamic stimulation may inhibit the beneficial effects of levodopa on akinesia and gait", "year": 2016}, {"ref": "R31", "pmid": "40677701", "doi": "10.1093/braincomms/fcaf266", "title": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease", "year": 2025}, {"ref": "R32", "pmid": "41480041", "doi": "10.64898/2025.12.17.25342333", "title": "Low-Frequency Adaptive Deep Brain Stimulation for Parkinson's Disease", "year": 2025}, {"ref": "R33", "pmid": "40640214", "doi": "10.1038/s41531-025-01067-z", "title": "Theta-frequency subthalamic stimulation enhances conflict resolution in Parkinson's disease patients with freezing of gait through frontal cortex modulation", "year": 2025}, {"ref": "R34", "pmid": "39957196", "doi": "10.1177/1877718X241292315", "title": "Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial", "year": 2025}, {"ref": "R35", "pmid": "42571859", "doi": "10.1016/j.nbd.2026.107571", "title": "Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease", "year": 2026}, {"ref": "R36", "pmid": "42239677", "doi": "10.3389/fneur.2026.1793291", "title": "An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease", "year": 2026}, {"ref": "R37", "pmid": "", "doi": "10.64898/2026.08.13.744293", "title": "Reduced entropy of subthalamic beta bursts predicts freezing of gait in Parkinson's disease", "year": 2026}, {"ref": "R38", "pmid": "33240199", "doi": "10.3389/fneur.2020.571086", "title": "Neural Correlates of Freezing of Gait in Parkinson's Disease: An Electrophysiology Mini-Review", "year": 2020}, {"ref": "R39", "pmid": "36185822", "doi": "10.3389/fnsys.2022.995375", "title": "Abnormal neural oscillations during gait and dual-task in Parkinson's disease", "year": 2022}, {"ref": "R40", "pmid": "28529730", "doi": "10.1186/s40035-017-0083-7", "title": "Effect of low versus high frequency stimulation on freezing of gait and other axial symptoms in Parkinson patients with bilateral STN DBS: a mini-review", "year": 2017}, {"ref": "R41", "pmid": "", "doi": "10.3389/fnhum.2024.1495272", "title": "Beta-gamma phase-amplitude coupling of scalp electroencephalography during walking preparation in Parkinson's disease differs depending on the freezing of gait", "year": 2024}], "evidence": [{"eid": "E1", "ref": "R1", "design": "横断面患者间LFP/EEG比较及左旋多巴干预", "population": "PD，有FOG与无FOG", "n": "22（FOG 14，非FOG 8）", "condition": "静息及药物干预", "measure": "STN低/高β功率、皮层-STN coherence", "finding": "FOG患者高β功率较高，左旋多巴后下降并伴随FOG改善", "limitations": "不能直接说明单次FOG onset的神经变化；样本量较小"}, {"eid": "E2", "ref": "R2", "design": "同步LFP与步态运动学观察研究", "population": "PD Freezer与Non-freezer", "n": "13（5与8）", "condition": "行走及主动骑行", "measure": "STN β功率及频谱峰", "finding": "Freezer运动启动时存在约18Hz窄带异常；骑行更强地抑制总体β", "limitations": "不能证明18Hz活动直接导致冻结"}, {"eid": "E3", "ref": "R3", "design": "自由行走LFP与非线性动力学分析", "population": "PD Freezer与Non-freezer", "n": "14（8名Freezer）", "condition": "药物OFF、DBS OFF，正常行走和FOG", "measure": "STN β/α功率、Sample Entropy", "finding": "无冻结行走时Freezer平均β较低但β熵较高；FOG期间α熵升高", "limitations": "熵指标不能直接解释因果；结果依赖任务和算法"}, {"eid": "E4", "ref": "R4", "design": "随机交叉DBS干预与步态LFP记录", "population": "PD Freezer与Non-freezer", "n": "12（8名Freezer）", "condition": "药物OFF，DBS OFF、60Hz、140Hz", "measure": "STN β burst duration及步态运动学", "finding": "Freezer具有延长的运动相关β burst；DBS缩短病理性长burst并改善步态", "limitations": "样本量小；burst阈值和任务范式影响结果"}, {"eid": "E5", "ref": "R5", "design": "单任务与双任务行走LFP观察研究", "population": "PD患者", "n": "15；仅少数在实验中出现真实FOG", "condition": "单任务和双任务行走", "measure": "STN低β、θ、iFOG", "finding": "15-21Hz低β和5-8Hz θ与易感步态相关", "limitations": "主要测量FOG易感性，而非实际冻结发作"}, {"eid": "E6", "ref": "R6", "design": "真实步行同步LFP、EEG、运动学和DAT影像", "population": "PD患者", "n": "7，其中5人发生FOG", "condition": "真实行走、过门诱发冻结", "measure": "STN功率、β burst、皮层-STN coherence", "finding": "STN局部功率和burst无显著变化；冻结前及冻结期间低频皮层-STN解耦", "limitations": "仅14次冻结；均为过门诱发；任务覆盖有限"}, {"eid": "E7", "ref": "R7", "design": "术中虚拟现实诱发FOG及微电极记录", "population": "PD接受STN-DBS手术患者", "n": "8", "condition": "术中VR步态冻结", "measure": "STN MUA、θ/β活动、下肢EMG", "finding": "FOG onset伴随STN多单位活动及θ/β活动短暂增加，随后出现异常肌肉放电", "limitations": "MUA不是慢性DBS LFP；术中VR范式；样本小"}, {"eid": "E8", "ref": "R8", "design": "步态冻结前后头皮EEG观察研究", "population": "PD伴明显FOG患者", "n": "24", "condition": "药物OFF，TUG、行走与冻结", "measure": "额叶/中央θ功率及跨区域耦合", "finding": "冻结期间额叶和中央θ增加；步行向冻结转换时θ耦合增加", "limitations": "头皮EEG不能直接定位STN"}, {"eid": "E9", "ref": "R9", "design": "同步ECoG、STN LFP和运动捕捉", "population": "PD伴FOG患者", "n": "8", "condition": "TUG真实步行", "measure": "STN β功率、ECoG、coherence、FOG分类", "finding": "FOG期间STN β功率升高；频带特征分类高于机会水平", "limitations": "21份冻结数据达到较好质量；coherence对照为shuffled surrogate"}, {"eid": "E10", "ref": "R10", "design": "自由步行ECoG、运动捕捉和STN-DBS干预", "population": "PD接受STN-DBS患者", "n": "16", "condition": "刺激ON/OFF，单任务和双任务", "measure": "M1 β-γ PAC、FOG持续时间", "finding": "高β-γ PAC与冻结风险和严重度相关；DBS降低PAC并改善FOG", "limitations": "PAC下降不能解释全部DBS获益；不能直接证明PAC为唯一介导机制"}, {"eid": "E11", "ref": "R11", "design": "神经机器人步态编码研究", "population": "PD患者", "n": "18", "condition": "受控腿部运动及步态组成任务", "measure": "STN神经活动、肌肉活动启动/终止/幅度", "finding": "STN编码腿部肌肉活动及步行状态", "limitations": "受控运动范式不等于自然行走FOG"}, {"eid": "E12", "ref": "R12", "design": "术中单单位和多单位记录", "population": "中度PD患者", "n": "12", "condition": "仰卧踏步、启动/停止提示", "measure": "STN和SN神经元放电、β振荡", "finding": "STN偏向运动执行调节，SNr偏向注意相关调节；冻结样不规则期间STN β增加", "limitations": "仰卧踏步，不是自然直立步行；冻结样不规则不能完全等同临床FOG"}, {"eid": "E13", "ref": "R13", "design": "肌电频谱观察及STN/SNr刺激干预", "population": "PD Freezer及健康对照", "n": "9名Freezer、16名健康对照", "condition": "药物OFF，刺激OFF、STN-DBS、SNr-DBS", "measure": "TA/GA α和低β EMG", "finding": "Freezer正常步行和冻结期间均有低频异常肌肉活动；STN刺激降低该活动", "limitations": "未同步记录STN LFP，不能证明LFP变化介导肌电改善"}, {"eid": "E14", "ref": "R14", "design": "术前术后电极位置、VTA及tractography研究", "population": "PD接受STN-DBS患者", "n": "19", "condition": "术前与术后", "measure": "FOG、步态、皮层-STN连接", "finding": "感觉运动连接与FOG改善相关，前额叶连接与恶化相关", "limitations": "小样本；连接组相关不能直接证明通路因果"}, {"eid": "E15", "ref": "R15", "design": "回顾性VTA和连接组研究", "population": "双侧HFS-STN-DBS且有FOG患者", "n": "76", "condition": "术后临床随访", "measure": "VTA、纤维束、FOG-Q", "finding": "背外侧STN及SMA/pre-SMA通路与改善相关；腹内侧及前额叶通路与恶化相关", "limitations": "回顾性选择；仅76/776符合影像和资料标准；功能连接模型未通过LOOCV"}, {"eid": "E16", "ref": "R16", "design": "分区LFP、动力学、运动学和药物干预", "population": "PD患者及健康对照", "n": "38名PD、24名健康对照", "condition": "DOPA OFF/ON，步态启动和冻结", "measure": "267个STN双极记录位置，低β、高β、步态pace/rhythm/balance", "finding": "FOG易感与实际发生对应不同STN空间和频段关联；药物部分恢复异常关系", "limitations": "实际观察到FOG者12人；多个dipole和步态周期须按患者层级统计"}, {"eid": "E17", "ref": "R17", "design": "STN LFP、EMG、运动学和主动停止对照", "population": "PD患者", "n": "12", "condition": "正常行走、转弯、冻结", "measure": "STN activation-deactivation、拮抗肌co-contraction、STN-EMG coherence", "finding": "冻结前及冻结期间存在STN和下肢肌肉时序协调异常", "limitations": "冻结事件数量有限；部分亚型为trembling-in-place"}, {"eid": "E18", "ref": "R18", "design": "同步M1/PMC ECoG、STN LFP和转弯运动学", "population": "PD患者", "n": "19", "condition": "药物OFF/ON，正常转弯与转弯冻结", "measure": "分阶段α功率、PMC-STN coherence", "finding": "转弯冻结存在相位特异性皮层-STN动态异常", "limitations": "任务特异性；不能直接推广到所有FOG触发情境"}, {"eid": "E19", "ref": "R19", "design": "LFP与认知/情绪量表的线性混合效应模型", "population": "PD转弯冻结患者", "n": "13", "condition": "正常转弯与冻结转弯", "measure": "STN θ、α、β功率，MoCA、HADS", "finding": "冻结转弯期间θ与焦虑正相关、与MoCA负相关", "limitations": "相关性研究；不能证明焦虑导致STN θ变化"}, {"eid": "E20", "ref": "R20", "design": "静息LFP频谱及burst分析", "population": "PD患者", "n": "23（FOG 14，非FOG 9）", "condition": "静息", "measure": "STN α、高β功率及间歇振荡", "finding": "α burst和高β burst幅度与FOG严重度相关", "limitations": "静息记录不能直接代表冻结发生时的活动"}, {"eid": "E21", "ref": "R21", "design": "随机双盲交叉刺激研究", "population": "严重轴性症状及FOG的PD患者", "n": "13", "condition": "60Hz、130Hz、不同电压和等能量条件", "measure": "SWS、FOG次数、UPDRS", "finding": "60Hz高电压等能量条件改善冻结", "limitations": "样本小；临床选择性人群；震颤控制可能下降"}, {"eid": "E22", "ref": "R22", "design": "随机盲法频率交叉研究", "population": "双侧STN-DBS且有步态投诉的PD患者", "n": "20", "condition": "60Hz与130Hz，其他参数不变", "measure": "步幅和步态指标", "finding": "未发现60Hz在主要步幅终点上的优势", "limitations": "TEED未匹配，冻结难以在实验中稳定诱发"}, {"eid": "E23", "ref": "R23", "design": "随机双盲前瞻性交叉研究", "population": "双侧STN-DBS的PD患者", "n": "14", "condition": "60Hz和130Hz，各自优化接触点", "measure": "UPDRS、轴性症状、步态", "finding": "60Hz最佳接触点较腹侧，轴性症状改善较好", "limitations": "不是专门的真实FOG事件诱发研究"}, {"eid": "E24", "ref": "R24", "design": "随机双盲刺激交叉研究", "population": "常规130Hz下仍有FOG的PD患者", "n": "7", "condition": "药物ON，60Hz、130Hz、DBS OFF", "measure": "FOG、吞咽造影、UPDRS", "finding": "60Hz改善FOG和吞咽，误吸事件降低", "limitations": "样本极小，疗效外推有限"}, {"eid": "E25", "ref": "R25", "design": "前瞻性随机序列双盲交叉随访", "population": "药物难治性FOG的STN-DBS患者", "n": "11，10人完成长期随访", "condition": "60Hz和130Hz，平均14.5个月随访", "measure": "FOG、SWS、吞咽和UPDRS", "finding": "60Hz长期改善FOG，但总体获益随时间减弱", "limitations": "样本小；长期效应可能受到疾病进展影响"}, {"eid": "E26", "ref": "R26", "design": "系统综述及Meta-analysis", "population": "PD-STN-DBS研究", "n": "16项步态研究，6项提供FOG评分", "condition": "不同术后随访时段", "measure": "步态和FOG临床评分", "finding": "HFS对药物OFF状态步态和FOG有总体获益", "limitations": "原始研究异质性；药物ON状态效果不稳定"}, {"eid": "E27", "ref": "R27", "design": "双盲随机交叉可行性研究", "population": "双侧STN-DBS的PD患者", "n": "14", "condition": "药物OFF，低频与高频刺激", "measure": "步态节律和加速度指标", "finding": "低频改善部分躯干节律指标", "limitations": "不等于证明FOG事件减少"}, {"eid": "E28", "ref": "R28", "design": "横断面五条件临床及IMU研究", "population": "术后持续FOG患者", "n": "17", "condition": "药物ON/OFF、刺激ON/OFF、60Hz/130Hz", "measure": "FOG次数、SWS、IMU、轴性评分", "finding": "60Hz总体FOG次数不显著优于130Hz，但个体响应异质", "limitations": "样本小；非盲法；不同患者的药物-刺激交互不同"}, {"eid": "E29", "ref": "R29", "design": "前瞻性VFS试点及纵向随访", "population": "STN-DBS且有FOG的PD患者", "n": "28", "condition": "HFS、LFS、VFS及6/12个月", "measure": "TUG、冻结次数、UPDRS", "finding": "VFS在步态和冻结指标上优于单独HFS或LFS", "limitations": "非随机；未维持TEED一致；随访无对照组"}, {"eid": "E30", "ref": "R30", "design": "刺激位置与可逆性步态恶化临床研究", "population": "STN-DBS后步态/运动不能恶化患者", "n": "17纳入，12完成", "condition": "药物ON/OFF、刺激ON/OFF及不同接触点", "measure": "SWS、FOG、步态和电极位置", "finding": "部分背侧/前方刺激可逆性恶化步态并抑制左旋多巴获益", "limitations": "选择性纳入刺激恶化患者；不能代表所有STN-DBS患者"}, {"eid": "E31", "ref": "R31", "design": "双盲实验室beta-burst驱动aDBS试点", "population": "PD-STN-DBS患者", "n": "7", "condition": "DBS OFF、aDBS、cDBS、随机刺激", "measure": "β burst duration、冻结时间、步态运动学", "finding": "aDBS可行且安全，改善步态，效果与cDBS相近", "limitations": "样本小；急性实验室研究；尚未证明优于优化cDBS"}, {"eid": "E32", "ref": "R32", "design": "60Hz beta-burst自适应刺激预印本", "population": "双侧STN-DBS患者", "n": "8", "condition": "60Hz cDBS/aDBS与临床140Hz", "measure": "β burst duration、FOG、UPDRS", "finding": "60Hz缩短β burst，基线FOG患者步态改善", "limitations": "预印本；样本小；尚未同行评审"}, {"eid": "E33", "ref": "R33", "design": "认知任务和刺激状态fMRI干预研究", "population": "PD患者及健康对照", "n": "90名PD（52名FOG）及37名健康对照；刺激fMRI子组18名FOG", "condition": "冲突任务、5Hz与130Hz STN刺激", "measure": "Flanker冲突解决、前额叶BOLD", "finding": "5Hz改善冲突解决能力和额叶激活", "limitations": "并非真实步行FOG疗效试验"}, {"eid": "E34", "ref": "R34", "design": "双盲随机交叉STN-SNr联合刺激试验", "population": "药物/常规刺激难治性FOG患者", "n": "15进入至少一种联合刺激条件", "condition": "STN单独、STN+高频SNr、STN+低频SNr", "measure": "NFOG-Q、运动并发症、患者偏好", "finding": "主要FOG终点无显著差异，约三分之一患者临床改善", "limitations": "样本小；不能证明联合刺激整体优于STN单靶点"}, {"eid": "E35", "ref": "R35", "design": "步态周期锁定皮层-STN同步记录和刺激调节", "population": "PD-FOG患者", "n": "摘要未报告", "condition": "FOG与非FOG步态周期、HFS/LFS、左旋多巴", "measure": "S1/SPL低β、S1-STN θ coherence", "finding": "步态周期相位依赖神经特征与冻结易感有关", "limitations": "样本量及独立重复情况仍需进一步核实"}, {"eid": "E36", "ref": "R36", "design": "STN-LFP机器学习冻结检测", "population": "PD患者", "n": "5", "condition": "VR物理、焦虑和认知负荷诱发任务", "measure": "LFP功率、alpha/beta burst、机器学习分类", "finding": "成功检测29次冻结中的24次，平均加权F1为0.67", "limitations": "极小样本；需要跨中心和日常环境外部验证"}, {"eid": "E37", "ref": "R37", "design": "STN beta burst时间结构预印本", "population": "PD患者", "n": "4", "condition": "稳定行走、冻结前和冻结期间", "measure": "inter-burst interval entropy、时间变异性", "finding": "冻结前burst间隔熵下降，LOPO AUC约0.825", "limitations": "预印本；仅4人；高度探索性"}], "claims": [{"cid": "C1", "text": "STN β活动与FOG相关，但不存在统一适用于所有患者和行为阶段的β功率变化方向。", "level": "synthesis", "status": "well-supported", "uncertainty": "不同任务、药物状态、运动阶段和信号指标会改变β结果。", "evidence": [{"eid": "E1", "relation": "supports"}, {"eid": "E2", "relation": "supports"}, {"eid": "E3", "relation": "qualifies"}, {"eid": "E4", "relation": "supports"}, {"eid": "E5", "relation": "supports"}, {"eid": "E6", "relation": "contradicts"}, {"eid": "E9", "relation": "supports"}]}, {"cid": "C2", "text": "延长的STN β burst是FOG易感性和部分冻结过程的重要候选生物标志物。", "level": "synthesis", "status": "supported", "uncertainty": "尚未证明长burst是所有FOG发作的必要条件或充分原因。", "evidence": [{"eid": "E3", "relation": "qualifies"}, {"eid": "E4", "relation": "supports"}, {"eid": "E31", "relation": "supports"}, {"eid": "E37", "relation": "qualifies"}]}, {"cid": "C3", "text": "FOG可以伴随低频皮层-STN耦合中断，而不一定伴随STN局部β功率显著改变。", "level": "finding", "status": "supported", "uncertainty": "直接人体证据主要来自小样本真实步行研究，仍需独立重复。", "evidence": [{"eid": "E6", "relation": "supports"}, {"eid": "E9", "relation": "qualifies"}, {"eid": "E18", "relation": "supports"}]}, {"cid": "C4", "text": "FOG易感状态、冻结前状态和冻结发生状态具有不同的STN神经活动模式。", "level": "synthesis", "status": "supported", "uncertainty": "不同任务范式和FOG亚型仍可能改变具体神经特征。", "evidence": [{"eid": "E5", "relation": "supports"}, {"eid": "E6", "relation": "supports"}, {"eid": "E16", "relation": "supports"}, {"eid": "E18", "relation": "supports"}]}, {"cid": "C5", "text": "STN后部感觉运动区和中央联合区与步态速度、节律和平衡之间存在不同的频段及空间关联。", "level": "finding", "status": "supported", "uncertainty": "功能分区依赖个体解剖配准，不能直接等同于刺激最佳靶点。", "evidence": [{"eid": "E16", "relation": "supports"}, {"eid": "E15", "relation": "qualifies"}]}, {"cid": "C6", "text": "STN活动异常与拮抗肌协调和下肢运动输出失调有关。", "level": "synthesis", "status": "supported", "uncertainty": "现有研究尚未充分证明STN LFP异常是肌肉异常的直接原因。", "evidence": [{"eid": "E7", "relation": "supports"}, {"eid": "E12", "relation": "supports"}, {"eid": "E13", "relation": "supports"}, {"eid": "E17", "relation": "supports"}]}, {"cid": "C7", "text": "认知和情绪因素能够调节STN低频活动及FOG相关行为。", "level": "synthesis", "status": "supported", "uncertainty": "认知、焦虑与神经活动的方向依赖任务和行为阶段，尚未建立统一因果链。", "evidence": [{"eid": "E5", "relation": "supports"}, {"eid": "E19", "relation": "supports"}, {"eid": "E33", "relation": "supports"}]}, {"cid": "C8", "text": "STN-DBS的FOG疗效受到刺激位置、纤维通路、药物状态和患者表型影响。", "level": "synthesis", "status": "well-supported", "uncertainty": "个体化刺激预测仍需要前瞻性外部验证。", "evidence": [{"eid": "E14", "relation": "supports"}, {"eid": "E15", "relation": "supports"}, {"eid": "E28", "relation": "supports"}, {"eid": "E30", "relation": "supports"}]}, {"cid": "C9", "text": "60Hz低频STN刺激能够改善部分患者的FOG，但不普遍优于130Hz。", "level": "synthesis", "status": "well-supported", "uncertainty": "TEED、接触点、任务诱发和患者筛选导致研究异质性。", "evidence": [{"eid": "E21", "relation": "supports"}, {"eid": "E22", "relation": "contradicts"}, {"eid": "E23", "relation": "supports"}, {"eid": "E24", "relation": "supports"}, {"eid": "E25", "relation": "supports"}, {"eid": "E28", "relation": "qualifies"}]}, {"cid": "C10", "text": "β burst驱动的aDBS具有初步可行性，但尚未证明优于优化后的连续DBS。", "level": "finding", "status": "supported", "uncertainty": "样本量小，缺少长期家庭环境随机对照试验。", "evidence": [{"eid": "E31", "relation": "supports"}, {"eid": "E32", "relation": "qualifies"}]}, {"cid": "C11", "text": "STN-SNr联合刺激可能使部分难治性FOG患者获益，但整体额外疗效尚未确立。", "level": "synthesis", "status": "contested", "uncertainty": "响应者可能具有不同疾病病程和运动认知表型。", "evidence": [{"eid": "E12", "relation": "supports"}, {"eid": "E13", "relation": "qualifies"}, {"eid": "E34", "relation": "qualifies"}]}, {"cid": "C12", "text": "STN神经活动时间结构、熵和步态相位指标可能提供超越平均功率的FOG预测信息。", "level": "mechanism", "status": "speculative", "uncertainty": "不同熵指标并不等价，尚缺乏统一定义和外部验证。", "evidence": [{"eid": "E3", "relation": "supports"}, {"eid": "E35", "relation": "supports"}, {"eid": "E37", "relation": "supports"}]}, {"cid": "C13", "text": "STN局部β活动增强是所有FOG的必要且充分原因。", "level": "mechanism", "status": "weak", "uncertainty": "存在真实FOG期间STN局部功率无显著变化的研究，也存在不同频段和网络异常。", "evidence": [{"eid": "E4", "relation": "qualifies"}, {"eid": "E6", "relation": "contradicts"}, {"eid": "E16", "relation": "qualifies"}]}], "hypotheses": [{"hid": "H1", "name": "STN病理性β burst驱动模型", "text": "延长的STN β burst限制运动相关信息处理和步态执行灵活性，促使系统进入冻结状态。", "claims": [{"cid": "C1", "relation": "supports"}, {"cid": "C2", "relation": "supports"}, {"cid": "C13", "relation": "contradicts"}], "predictions": ["个体内长β burst应在FOG onset之前增加。", "β burst duration比平均β功率具有更稳定的冻结预测能力。", "选择性缩短病理性长burst应降低冻结风险。", "保留正常短burst比全面抑制β更有利于步态。"], "falsifiers": ["独立队列中长β burst不预测FOG。", "充分控制伪迹和行为阶段后长burst与FOG无关。", "选择性改变burst duration不改变冻结风险。"]}, {"hid": "H2", "name": "皮层-STN网络协调失败模型", "text": "FOG主要由SMA、M1、PMC与STN之间的动态协调和信息传递失败造成，而非STN局部功率单独升高。", "claims": [{"cid": "C3", "relation": "supports"}, {"cid": "C4", "relation": "supports"}, {"cid": "C13", "relation": "supports"}], "predictions": ["低频皮层-STN耦合变化先于部分FOG事件。", "网络时序指标比局部平均功率具有更高的跨任务预测价值。", "恢复异常耦合时序能够改善步态控制。"], "falsifiers": ["独立队列中网络耦合不提供局部LFP之外的预测价值。", "选择性改变网络耦合不影响冻结风险。"]}, {"hid": "H3", "name": "认知-情绪资源竞争模型", "text": "FOG易感患者的步态自动化能力下降，认知负荷、焦虑和环境复杂度超过可用控制资源后导致步态冻结。", "claims": [{"cid": "C7", "relation": "supports"}, {"cid": "C4", "relation": "supports"}], "predictions": ["双任务和焦虑负荷能够改变STN θ活动及联合区参与。", "认知控制改善可能降低认知诱发FOG风险。", "不同认知和情绪触发的FOG具有不同神经特征。"], "falsifiers": ["控制认知负荷和焦虑后，相关神经活动不能预测FOG。", "针对认知控制的干预不改变认知诱发冻结。"]}, {"hid": "H4", "name": "步态相位与神经动力学状态转换模型", "text": "FOG是步态周期内神经活动时序、相位和复杂度组织失常所导致的非线性状态转换。", "claims": [{"cid": "C4", "relation": "supports"}, {"cid": "C12", "relation": "supports"}], "predictions": ["步态相位锁定指标优于整段频谱平均功率。", "冻结前存在可重复的神经状态转换轨迹。", "burst时间间隔熵和相位稳定性能够预测冻结风险。"], "falsifiers": ["独立患者和任务中步态相位指标不能提供增量预测价值。", "神经状态转换特征不能稳定重复。"]}, {"hid": "H5", "name": "解剖-网络选择性刺激模型", "text": "STN-DBS的FOG疗效取决于刺激募集的功能亚区和连接纤维通路，而不只是频率或总能量。", "claims": [{"cid": "C5", "relation": "supports"}, {"cid": "C8", "relation": "supports"}, {"cid": "C9", "relation": "supports"}, {"cid": "C11", "relation": "qualifies"}], "predictions": ["个体化VTA和纤维连接能够预测刺激响应。", "选择性募集感觉运动相关通路可减少FOG恶化。", "不同患者的最佳刺激网络存在差异。"], "falsifiers": ["前瞻性多中心试验中个体化VTA不能预测FOG疗效。", "控制刺激参数后纤维通路与临床响应无稳定关联。"]}]}
```
