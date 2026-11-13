===== open_g6.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "检索覆盖存在系统性截断，无法支持报告所要求的广泛证据覆盖。",
   "where": "第2.1—2.2节：“22条检索式中，只有第1条没有发生截断，其余21条均达到或超过取回上限。”例如，动物模型检索命中8134篇，只取回98篇；认知负荷相关检索命中2392篇，只取回99篇。报告同时承认没有检索Embase、Scopus、Web of Science和Cochrane。",
   "why": "这不是一般意义上的检索局限，而是直接影响证据集合构成的结构性问题。按照相关度排序取前100篇，不能保证获得高召回率，更不能保证保留最重要的阴性研究、反证研究和交叉方向研究。尤其是动物模型、认知控制、神经网络及单神经元研究，恰恰是检索量最大的方向。检索截断还可能产生系统性选择偏倚：容易被反复引用、标题直接包含FOG和STN的研究更容易进入，而使用不同术语、研究一般步行控制或提供反证的研究容易遗漏。43篇模型主动点名文献不能替代独立的系统性检索。报告虽然诚实披露了这个问题，但披露限制不等于解决限制。",
   "severity": "major",
   "fix": "重新执行检索。至少增加MEDLINE/PubMed、Embase、Web of Science或Scopus，并补充Cochrane、前向和后向引文追踪。取消每条检索式最多100篇的硬性截断，或者将高命中量检索拆分为可审计的主题子检索。特别补充不以FOG为标题关键词的STN步行生理学、单神经元、运动控制、认知网络和动物机制研究。保留每条检索式的完整结果集、去重记录及筛选理由。"
  },
  {
   "rank": 2,
   "what": "尚未完成筛选的文献已经进入证据提取，且没有在证据数据库中保留明确的筛选状态。",
   "where": "第2.1节：“题目和摘要筛选：纳入82篇，待定327篇，排除258篇。”附录运行记录又称：“证据提取：150篇文献提取出544条证据（纳入文献有全文的读全文，其余和待定文献读摘要）。”",
   "why": "这里存在证据纳入边界不清的问题。150篇证据提取文献并不等于82篇已经纳入的文献，日志明确说明提取过程中还读取了待定文献摘要。但是结构化附录没有为每篇文献及其证据记录提供明确的筛选状态。因而无法判断哪些C1—C21结论使用了已经纳入的研究，哪些可能使用了尚未完成评价的研究。327篇待定文献占初筛记录的近一半，不能把它们视为已经完成筛选。更严重的是，摘要级信息可能直接进入机制综合，而全文可能包含不同的实验条件、阴性结果或限制性解释。这使证据可靠性无法充分追溯。",
   "severity": "major",
   "fix": "为每篇文献增加独立的筛选状态字段：Included、Excluded、Pending，并为每条证据继承该状态。正式综合结论只能使用已经完成筛选的研究。待定文献可以保留为候选证据，但必须单独标注，不能与正式纳入证据混合。对于每项结论，应能够查询其全部支持、反对和待定来源，并进行排除待定文献后的敏感性分析。"
  },
  {
   "rank": 3,
   "what": "将一项明确没有记录真实冻结事件的步态研究，作为冻结期间STN-EMG异常的证据，属于实质性引用错误。",
   "where": "第5.6节：“冻结期间低beta活动与下肢肌肉共同激活可能同时出现。[PMID:41388789]”第7.6节又将PMID:41388789作为APA、双侧肌肉协调及冻结前STN-EMG异常的证据。",
   "why": "核对原始论文后发现，PMID:41388789对应的是Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping。研究纳入14名PD患者，记录坐位、站立和原地踏步时的STN-LFP及下肢EMG。其研究明确说明，分析没有包含真正的冻结事件。因此，它可以支持STN beta与正常或异常踏步肌肉活动之间的关系，却不能直接支持冻结期间或冻结前的肌肉共同激活。论文甚至明确提醒不能把原地踏步结果直接推广到自由行走和真实冻结。 更值得注意的是，真正直接研究这一问题的原始论文已经存在：Klocke等2024年研究（PMID:39470410）同步记录STN-LFP、拮抗肌EMG和步态运动学，在实际行走及冻结过程中观察到冻结前STN-GA coherence增加、拮抗肌共同收缩和肌肉互抑制异常。 这不是简单的引用格式问题，而是把非冻结任务的证据提升成冻结事件证据，改变了证据的直接性。",
   "severity": "major",
   "fix": "将PMID:41388789限定为步态周期及踏步肌肉活动的生理学证据。实际冻结和冻结前STN-EMG关系应优先引用PMID:39470410，并结合PMID:36070366中真实冻结时的低beta及膝伸肌异常激活结果。重新检查H8的全部证据来源，逐条区分正常踏步、冻结易感状态、冻结前和实际冻结。"
  },
  {
   "rank": 4,
   "what": "研究范围声称覆盖单神经元和多模态神经活动，但正文实际上主要围绕STN-LFP频谱展开，若干关键原始研究只出现在结构化附录，没有进入核心综合。",
   "where": "第1.1节明确列出“STN-LFP和单神经元电生理”。但第5节的核心电生理综述主要讨论beta、theta、alpha、burst及皮层-STN coherence。结构化附录中则包含PMID:36730026、PMID:39470410和PMID:42571859，正文没有对这些研究进行相应的系统讨论。",
   "why": "这些不是边缘文献，而是能够改变机制解释的重要研究。第一，PMID:36730026使用术中微电极记录，纳入12名患者，分析了113个STN单单位神经元。研究发现，正常踏步时STN放电频率增加，而冻结样步态不规则期间放电频率与正常踏步相近，beta振荡活动则出现变化。必须注意，该研究的冻结样步态不等同于经过临床确认的真实FOG，作者也明确指出当时尚没有人体真实冻结期间的单神经元放电特征描述。这个边界对于区分单神经元放电与LFP群体振荡非常重要。 第二，PMID:39470410是直接记录真实冻结期间STN-LFP和拮抗肌EMG的研究，对H8尤其重要。第三，PMID:42571859于2026年10月发表，已经比较冻结与非冻结步态周期中的皮层-STN信号，并研究HFS、LFS和左旋多巴对这些异常的调节。它直接涉及步态周期锁定的生物标志物和刺激机制，却没有进入正文的机制综合。 这说明结构化证据库和最终报告之间没有完成真正的证据整合。正文因此容易形成一种偏向：把STN-FOG问题主要解释为LFP beta异常，而低估神经元放电、肌肉输出和皮层-基底节-脊髓整合。",
   "severity": "major",
   "fix": "增加独立的单神经元及神经肌肉机制章节。明确区分单单位、多单位、LFP、皮层记录和外周EMG。对PMID:36730026明确标注冻结样步态而非真实FOG；对PMID:39470410完整提取全文中的样本量、冻结标注、实验条件、STN-EMG耦合及拮抗肌结果；将PMID:42571859纳入2026年最新证据综合。要求每项进入附录的高相关原始研究都经过正文整合判断，或者明确说明不纳入的原因。"
  },
  {
   "rank": 5,
   "what": "对研究冲突的综合存在选择性呈现，部分最能区分竞争性机制的阴性结果和效应方向没有被充分利用。",
   "where": "第5.4节的beta冲突表仅列出beta增加、beta降低和运动相关beta抑制增强。第5.7节对Zhang等2025年研究只写：“部分PMC-STN alpha指标与冻结持续时间存在关系。”第7.3节仍将H4代偿性耦合和H5病理性过度耦合基本作为对等竞争解释。",
   "why": "至少存在两个值得纠正的地方。第一，Pozzi等2019年研究（PMID:31505548）在报告中被引用来支持冻结期间theta-alpha皮层-STN耦合下降，但该研究同时报告了一个非常重要的局部STN阴性结果：实际冻结期间，STN低频功率、beta功率和beta burst持续时间与正常步行相比没有显著差异。这个结果直接限制了将局部STN beta异常作为普遍冻结机制的解释。原始研究的这些阴性结果应当进入第5.4节的冲突矩阵，而不能只选择其耦合结果。 第二，Zhang等2025年研究（PMID:41131028）发现，TurnPre阶段增强的PMC-STN alpha coherence与更短的冻结持续时间相关。也就是说，这一结果的方向目前更支持H4所提出的代偿性解释，而不是H5所提出的病理性过度耦合解释。它不能最终证明代偿机制，但已经提供了能够区分两个模型的方向性证据。报告只说存在相关关系，却没有说明相关方向，也没有相应调整H4和H5的当前支持程度。 这使所谓的竞争性机制分析没有真正利用已有证据来区分模型。",
   "severity": "major",
   "fix": "重做冲突矩阵。对每项研究分别记录显著增加、显著降低和无显著差异，不能只保留方向明确的阳性结果。将Pozzi研究的局部beta阴性结果与皮层-STN去耦合结果放在同一证据框架中。对PMC-STN alpha研究报告完整的阶段、效应方向、效应量及置信区间，并明确指出现阶段H4获得了方向性支持，H5仍然是需要额外验证的替代解释，而不是默认与H4同等得到支持。"
  },
  {
   "rank": 6,
   "what": "胆碱能PET研究存在错误的PMID引用，并且对研究适用范围的表述不够精确。",
   "where": "第3.3节：“14例胆碱能PET研究提示FOG严重程度与多个脑区胆碱能末梢功能降低相关。[PMID:40635563]”",
   "why": "PMID:40635563实际对应的是Disease-Modifying Trials in Treated Parkinson's Disease: Stable Treated Does Not Equate with Biological Stability，与胆碱能PET及FOG研究无关。真正的原始论文是PMID:40512756，标题为Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease。该研究确实纳入14名PD患者，但研究对象是ON-medication FOG，发现胆碱能示踪剂空间协变模式与ON-FoG严重程度相关，并没有发现相应的OFF-FoG关联。 因此这里既有引用编号错误，也存在将ON-state特异性发现泛化成一般FOG机制的风险。读者按照正文提供的PMID无法找到支持该结论的论文。",
   "severity": "moderate",
   "fix": "将引用更正为PMID:40512756。将结论改为：在14名ON-state FOG患者中，特定胆碱能空间协变模式与ON-FoG严重程度相关，不能据此推断其同样解释OFF-FoG或所有FOG表型。同步检查正文、证据表和JSON参考文献之间的PMID一致性。"
  },
  {
   "rank": 7,
   "what": "证据可靠性等级缺乏可复核的操作标准，且原始研究和二手综述的引用层级没有始终得到严格执行。",
   "where": "第1.2节将证据可靠性分为较强、中等和较弱，但没有给出可重复的判定规则。第4.4节介绍13例60 Hz刺激研究时引用PMID:28529730；第5.4节介绍beta降低证据时引用PMID:33240199。",
   "why": "PMID:28529730本身是低频与高频STN-DBS研究的mini-review，不是那项13例患者试验的原始论文。原始Moreau等研究是PMID:18420482。虽然mini-review总结了原始试验，但报告讨论具体患者数量、刺激参数和随访结果时，应直接引用原始研究。 类似地，PMID:33240199也是电生理mini-review。不能因为综述总结了某项研究，就把它等同于独立原始证据。另一个问题是，报告没有对纳入研究进行可复核的偏倚风险评价，例如患者选择、结局测量、混杂因素、缺失数据、统计单位和发表偏倚等。简单给出较强、中等、较弱的标签，并不足以说明为什么某个小样本研究比另一个研究可靠。预印本和摘要级证据也没有在每个具体结论旁持续标识。",
   "severity": "moderate",
   "fix": "为每篇研究增加独立的质量评价记录，至少包括研究设计、偏倚风险、结局可靠性、患者数量、统计单位、药物及刺激条件、是否全文、是否同行评审。对于临床干预研究采用适当的随机试验或观察性研究偏倚评价工具。正文涉及具体原始结果时优先引用原始论文，综述只能作为背景或补充来源。预印本、摘要和单病例结果必须在具体证据条目中明确标记。"
  },
  {
   "rank": 8,
   "what": "结构化证据数据库存在数量不一致和引用关系断裂，长期知识积累机制尚未通过数据完整性验证。",
   "where": "第2.3节称结构化知识部分有539条证据，运行日志有544条证据。第9.5节仍将这两个数字列为待解决问题。附录JSON中的实际evidence数组为538条，此外C6存在指向不存在的证据ID的引用。",
   "why": "目前不是两个数字存在差异，而是至少有三个版本：正文539条、运行日志544条、结构化JSON实际538条。报告声称保留原始数字，但没有确定哪一个才是最终知识库版本。进一步检查发现，C6引用的证据ID为S2_E_DOI_10.21203_rs.3.rs-9617843_v10，而实际证据记录中的对应ID为S2_E_DOI_10.21203_rs.3.rs-9617843_v1_0，导致引用关系无法解析。这虽然不一定直接改变当前某项科学结论，却直接破坏了证据—结论—假说图谱的可追溯性。对于报告提出的长期更新、旧结论重评和自主改进机制，这是必须解决的基础问题。",
   "severity": "moderate",
   "fix": "确定唯一的证据数据源和版本号。重新生成正文数字、参考文献表和结构化JSON，不允许分别维护多个独立计数。建立自动化完整性检查：证据数量一致、Evidence ID唯一、所有结论引用的证据ID均存在、所有文献ID均能解析、所有支持和反对关系均有有效目标。每次更新保留版本差异及修改原因。"
  },
  {
   "rank": 9,
   "what": "部分竞争性假说虽然提出了实验预测，但目前的实验设计还不能真正识别所声称的因果机制。",
   "where": "H1/H2提出通过步态相位特异性beta调节区分病因与伴随标志。H9/H10提出通过60/80/130 Hz比较区分PPN/MLR通路募集和STN局部振荡重组。第8.3、8.5节主要建议随机交叉刺激、VTA和连接组分析。",
   "why": "这里存在因果识别问题。首先，改变STN刺激参数并不等于只改变beta。常规DBS可能同时改变STN局部活动、皮层-STN通信、邻近组织及下游通路。如果刺激后beta变化并且FOG改善，仍不能证明beta变化介导了临床改善。其次，60/80/130 Hz刺激可能同时改变局部神经动力学和纤维募集，TEED相等也不能保证组织募集相等。因此，单纯比较刺激频率、VTA和结构连接组，不能独立区分H9与H10。报告在第8.5节已经承认规范性连接组和VTA不能完成因果验证，但第8.3节的主要实验设计仍然没有给出真正独立操纵两条机制的方案。最终可能出现实验结果符合两个假说，却无法判断哪个机制成立的情况。",
   "severity": "moderate",
   "fix": "对每组竞争性假说明确写出可识别的因果变量、干预变量、机制中介和反事实对照。H1/H2需要能够独立改变目标beta动力学并验证操纵是否成功的方案，而不能仅依靠普通DBS开启或关闭。H9/H10需要尽可能独立改变局部STN活动和特定纤维通路募集，并同步测量相应神经响应。如果现有技术无法独立操纵某条通路，应明确写出当前不可识别，而不是把相关性实验称为能够区分机制的决定性实验。"
  },
  {
   "rank": 10,
   "what": "TBS-DBS机制讨论没有充分呈现原始试验的主要阴性结果，容易使探索性假说显得比实际证据更成熟。",
   "where": "第7.9节H12/H13将TBS-DBS组织为即时病理驱动反弹与长期神经可塑性两种竞争解释。第8.8节仅称目前TBS相关证据主要来自短期探索性研究。",
   "why": "PMID:40383539对应的随机、双盲、短期研究纳入15名PD患者。其主要结局FoG-Course在整个患者样本中并未显示TBS-DBS优于连续DBS。只有7/15名患者主观评价TBS-DBS相当或更好。 报告虽然指出长期效果未知，却没有在H12/H13的核心讨论中充分呈现这个主要阴性结果。更重要的是，该试验没有直接操纵暂停时间，也没有证明暂停期间STN病理活动反弹，更没有证明长期神经可塑性。因而H12和H13是值得研究的解释，但不是该临床试验已经提供的机制证据。即时反弹和长期可塑性也不一定互相排斥，可能同时存在。",
   "severity": "moderate",
   "fix": "在H12/H13之前明确报告试验的主要阴性结果、患者偏好亚组和随访时间。将两种解释明确标注为作者提出的待检验假说，而不是已经得到临床试验支持的机制。后续实验分别操纵刺激暂停时间和累计治疗时间，测量即时症状变化、暂停期间神经活动及长期停刺激后的残留效应。"
  }
 ],
 "overall": "这份报告已经意识到STN-FOG研究中的患者异质性、任务依赖性、时间阶段差异以及相关性与因果性的区别，但目前仍不能作为可靠、完整的证据综合版本。最严重的问题不在于某一个机制模型必然错误，而在于证据集合本身尚未完成：检索被大范围截断，待定文献混入证据提取，部分原始研究被错误引用或没有进入正文，关键阴性结果和方向性结果没有充分参与机制判断，结构化证据库还存在引用关系断裂。尤其是把没有真实冻结事件的踏步研究用作冻结期证据，以及未充分整合真正的STN-LFP、EMG和单神经元研究，直接影响了报告对STN神经活动机制的判断。13项假说虽然具有一定启发性，但目前还不能认为已经形成了充分可区分的因果模型。我的总体判断是：这是一份具有研究框架价值、但证据审计和机制综合尚未闭环的工作版本。应优先修复检索、筛选、原始文献核对和正文—证据库一致性，再重新评估C1—C21及H1—H13，而不是在现有基础上继续增加假说或扩充文字。"
}

===== open_g56.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "核心电生理证据存在明显的选择性整合，导致最重要的科学冲突没有被完整呈现。这是整份报告最严重的问题。",
   "where": "第五章5.1：“目前至少有两类相对直接的事件级证据：1. 冻结期间局部STN beta活动或beta burst发生变化；2. 冻结期间皮层-STN低频耦合发生异常。”第五章5.4又将beta结果概括为升高、降低和运动相关抑制增强三类。",
   "why": "结构化附录实际上已经收录了多项重要的原始研究，但主文没有真正整合它们。例如：PMID:28890315研究了14名患者，其中8名为Freezers，发现实际FOG期间STN beta功率相较无冻结步行反而降低，同时alpha Sample Entropy升高；PMID:31665229在8名患者中通过术中VR步态任务、微电极和EMG同步记录，观察到冻结起始时STN多单位活动及beta、theta活动短暂增加，并将其与自主停止行走进行比较；PMID:24361601在22名患者中发现FOG组STN high-beta功率升高，并观察到左旋多巴治疗后high-beta下降及FOG受到抑制；PMID:31494286发现冻结易感步态中low-beta和theta活动升高。2025年的PMID:39884164还报告了静息STN alpha及high-beta间歇活动与FOG严重程度的关联。更重要的是，2026年10月发表的PMID:42571859已经研究了步态周期锁定的皮层-STN活动、S1/SPL低beta异常以及S1-STN theta耦合变化，但没有进入主文讨论。以上均为不同类型的重要证据，而不是可以简单归并为beta升高或降低的重复研究。【turn372188search12】【turn529100search4】【turn529100search5】【turn529100search6】【turn529100search0】【turn529100search2】此外，附录中PMID:31505548的原始结果还显示，实际冻结期间STN局部beta功率和beta burst持续时间均未出现显著变化，主要异常是皮层-STN低频耦合。这一阴性结果在主文5.1中没有得到应有的重视。结果是：报告看起来分析了beta方向冲突，实际上遗漏了相当一部分最有解释价值的冲突证据。",
   "severity": "major",
   "fix": "重新建立STN电生理证据矩阵，至少分别整理FOG易感状态、实际冻结、冻结前、冻结恢复四类状态，并区分LFP、单神经元放电、多单位活动、皮层-STN耦合及复杂度指标。将PMID:28890315、24361601、31494286、31665229、31505548、39884164和42571859等纳入正文逐项比较。尤其要解释为什么实际冻结期间有时出现beta升高、有时降低、有时没有变化，而不能仅用任务不同作为笼统解释。"
  },
  {
   "rank": 2,
   "what": "检索和筛选流程没有形成一个边界清晰、可审计的最终证据集，报告的覆盖能力不足以支撑其综合性结论。",
   "where": "第二章2.1：“题目和摘要筛选：纳入82篇，待定327篇，排除258篇。”第二章2.2：“22条检索式中，只有第1条没有发生截断，其余21条均达到或超过取回上限。”附录运行记录：“证据提取：150篇文献提取出544条证据（纳入文献有全文的读全文，其余和待定文献读摘要）。”",
   "why": "首先，21条检索式均被前100条的取回上限截断，且动物模型、认知负荷、STN振荡等方向的命中量远远超过取回量。按报告自己的数字，667篇中有327篇仍处于待定状态，没有完成明确的纳入或排除。其次，正式纳入只有82篇，证据提取却涉及150篇，多出的68篇来自何种待定文献、为什么选择这些文献、其证据是否进入C1-C21及H1-H13，均没有交代。第三，题目和摘要筛选完全由单一GPT流程完成，没有双人独立筛选、人工仲裁或独立复核。第四，没有提供逐篇排除原因及完整筛选审计表。这不是简单的系统综述格式问题，而是证据池本身的纳入边界不清楚。",
   "severity": "major",
   "fix": "重新执行可复现的检索和筛选。对命中量较大的检索式进行分页、分年份或分主题检索，不使用未经处理的前100条截断结果作为最终候选集。明确区分纳入、排除和待定文献。待定文献不能直接作为支持综合结论的证据。对筛选和提取结果进行独立人工核查，并记录每篇文献的最终状态、排除理由和证据来源。若仍采用叙述性综述，也应确保实际分析的文献均有明确纳入依据。"
  },
  {
   "rank": 3,
   "what": "FOG、FOG易感性、冻结样步态异常和一般运动减速之间的操作性定义没有真正统一，跨研究比较存在构念混淆。",
   "where": "第五章5.1：“FOG susceptibility：患者具有冻结易感性，但测试时没有发生实际冻结。”“Pre-FOG：冻结前的运动准备或过渡阶段。”第五章5.4则将不同研究的beta升高、降低结果并列讨论。",
   "why": "报告虽然在概念上区分了四种行为状态，但没有为每项原始研究明确标注实际采用的冻结定义。例如，PMID:31494286使用躯干加速度计计算的iFOG指数区分冻结易感步态与正常步态，并非只分析实际冻结事件；PMID:37226972将8次VR冻结和7次显著步态减速合并为受影响试次；PMID:36730026采用仰卧踏步过程中步态振幅下降超过50%的freezing-like irregularities，这不能直接等同于自然直立行走中的真实FOG。PMID:28890315则分别分析无冻结步行和实际冻结期间的STN活动。这些研究的行为学对象并不相同。若把它们统称为FOG相关活动，容易把冻结易感标志、运动减速的继发变化和实际冻结期间的神经变化混在一起，进而制造或掩盖频段方向冲突。",
   "severity": "major",
   "fix": "为每项研究建立独立的FOG操作性定义字段，至少记录临床视频诊断、患者自述或问卷分类、加速度计冻结指数、步态运动学阈值、EMG标准、真实冻结事件以及freeze-like行为。将研究结论明确标记为易感性证据、冻结前证据、实际事件证据或替代行为证据。不能将不同定义的Freezer组直接视为同一研究对象。"
  },
  {
   "rank": 4,
   "what": "将一项没有实际冻结事件记录的研究解释为冻结期间的神经生理证据，属于明确的原始证据误用。",
   "where": "第五章5.6：“冻结期间低beta活动与下肢肌肉共同激活可能同时出现。[PMID:41388789]”",
   "why": "PMID:41388789的原始研究是Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping。其14名患者接受的是坐位、站立和踏步任务中的STN-LFP及下肢EMG记录，研究并没有实际冻结事件分析，也没有按FOG与非FOG患者进行分组。文章报告的是运动状态及左旋多巴对低、高beta活动的不同影响，以及beta burst与运动启动时肌肉活动的关系。不能将运动启动时的肌肉共同激活直接转述为实际冻结期间的低beta与肌肉共同激活。【turn358589search2】这会使读者误以为该研究提供了直接的FOG事件同步神经肌肉证据。",
   "severity": "major",
   "fix": "删除或改写这句话。将PMID:41388789归类为正常及异常帕金森步态中的STN-肌肉活动研究，明确说明没有直接观察实际FOG。若要讨论冻结期间的神经肌肉共同激活，应寻找具有同步FOG事件标注、STN记录及下肢EMG的原始研究，并明确区分直接观察与作者的机制推测。"
  },
  {
   "rank": 5,
   "what": "部分关键文献存在PMID错配或引用二手综述代替原始研究的问题，削弱了证据的可追溯性。",
   "where": "第三章3.3：“14例胆碱能PET研究提示FOG严重程度与多个脑区胆碱能末梢功能降低相关。[PMID:40635563]”第四章4.4：“一项随机、双盲、交叉研究纳入13例患者……[PMID:28529730]”",
   "why": "第一处PMID明显错误：PMID:40635563实际对应Disease-Modifying Trials in Treated Parkinson's Disease: Stable Treated Does Not Equate with Biological Stability，而不是胆碱能PET研究。真正的14例胆碱能PET研究是PMID:40512756，题为Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease。【turn529100search1】【turn358589search0】第二处引用PMID:28529730实际上是2017年的mini-review，不是所描述的13例原始随机交叉试验。对应的原始研究是PMID:18420482。【turn358589search1】【turn358589search5】这说明报告没有始终遵守其声称的原始研究优先原则。即使二手综述准确转述了结果，也不能代替原始研究成为核心定量结论的主要证据来源。",
   "severity": "major",
   "fix": "使用PMID/DOI与题名进行自动交叉核验，检查每处正文引用是否与参考文献中的实际研究一致。对核心临床试验直接引用原始论文，同时可以附加综述作为背景来源。对于仅能从综述获得的研究细节，必须标明属于二手转述，不应写成已经直接核验原始论文的发现。"
  },
  {
   "rank": 6,
   "what": "竞争性机制假说在逻辑上并不都互斥，部分实验预测也不能真正区分所声称的竞争机制。",
   "where": "第七章7.10：“其中最值得优先开展直接竞争性实验的是：H1 vs H2、H4 vs H5、H9 vs H10、H12 vs H13。”",
   "why": "H1认为beta状态转换异常可能参与FOG，H2认为beta可能是共同上游障碍的下游表现，两者完全可能同时成立：beta可以是上游网络障碍的下游结果，同时又成为影响运动输出的中介。H4与H5对PMC-STN alpha耦合的代偿性和病理性解释，也可能在不同患者或不同时间阶段同时成立。H9和H10更不是真正互斥的机制：同一次刺激完全可能同时改变STN局部振荡和STN-脑干通路活动。H12与H13也可能分别解释刺激暂停的即时效应和重复治疗的长期效应。当前报告主要通过相关性预测和反证条件来区分这些模型，没有充分说明哪些干预能够选择性改变某个机制而不同时影响其他机制。因此，虽然提出了13项假说，但尚未形成真正可识别的因果模型体系。",
   "severity": "major",
   "fix": "首先建立因果图，明确上游原因、STN活动、运动输出、FOG事件和治疗反应之间的关系。区分必要原因、充分原因、共同原因、中介变量和代偿反应。允许多个模型同时成立，并说明它们的适用患者亚型及行为阶段。对于真正竞争的机制，应提出能够选择性改变一个机制、同时测量其他机制的干预设计，而不是仅比较相关系数或神经活动方向。"
  },
  {
   "rank": 7,
   "what": "证据可靠性等级缺少可重复的判定标准，研究质量评价仍然主要依赖叙述性判断。",
   "where": "第一章1.2：“较强：有明确原始研究支持，且主要结果具有一定重复性。”“中等：有直接研究支持，但样本量、实验条件或研究间一致性有限。”“较弱：主要依赖小样本、单病例、二手综述、预印本或探索性分析。”第四章4.1还使用“直接临床证据较充分”的判断。",
   "why": "上述分级没有说明具体的判定阈值。例如，什么程度的重复性才能达到较强？样本量、置信区间、研究偏倚、效应量和外部验证分别占多大权重？随机交叉试验、回顾性队列、病例报告和二手综述是否采用相同标准？报告虽然在个别研究中指出统计局限，但没有对150篇文献进行系统的偏倚风险评价，也没有对Meta分析中的原始研究重叠、发表偏倚和证据确定性进行统一处理。这样一来，证据等级可能反映作者对文献的印象，而不是可复核的科学评价。",
   "severity": "moderate",
   "fix": "建立针对不同研究设计的质量评价体系。临床随机试验、观察性研究、病例研究和电生理实验应分别评价。建议明确偏倚风险、测量直接性、精确度、一致性、重复性和发表偏倚等维度。对于Meta分析，还应核对原始研究重叠情况，避免多篇综述重复引用同一研究被误认为独立重复验证。将证据确定性和研究结果是否支持某个机制分开记录。"
  },
  {
   "rank": 8,
   "what": "低频刺激通过改变电流扩散和纤维募集的机制解释缺少必要的电场与参数层面论证。",
   "where": "第七章7.7，H9：“60 Hz等低频STN-DBS可能通过改变电流扩散和纤维募集，影响STN邻近的PPN/MLR及下行步行网络。”",
   "why": "报告没有明确说明频率变化如何导致空间电场分布或组织募集发生改变。DBS刺激场涉及电极结构、接触点、极性、电流分布、刺激幅度、脉宽及刺激速率等因素。刺激频率改变可能影响神经组织的时间响应和激活阈值，但不能在没有参数模型的情况下，将频率变化直接等同于电流空间扩散变化。尤其在等效TEED实验中，如果通过改变电压补偿频率，电压本身又会改变刺激场和可能的组织募集。因此，低频刺激的效果可能同时受到时间参数、刺激幅度及空间募集的影响。【turn665081search7】目前H9没有将这些因素分离。",
   "severity": "moderate",
   "fix": "明确区分刺激频率、每脉冲电场、总能量输送和实际神经组织募集。采用患者个体化电场/VTA及纤维激活模型，分别报告固定幅度、固定TEED及不同接触点条件下的结果。对于PPN/MLR通路机制，应提出可测量的纤维募集预测，而不是仅根据低频刺激有效推断其作用于脑干通路。"
  },
  {
   "rank": 9,
   "what": "结构化证据数据库的版本和引用关系存在实际完整性错误，不符合报告提出的长期可追溯要求。",
   "where": "第二章2.3：“证据表包含539条证据，而检索运行日志记录……544条证据。”第九章9.5再次将539与544的差异列为改进需求。结构化附录JSON中的实际evidence数组则包含538条记录。附录C6还存在无法解析的证据编号。",
   "why": "同一份最终报告出现539、544和实际538三个不同数字，意味着证据表、运行日志和最终输出没有统一版本。进一步检查发现，C6引用了不存在的证据ID `S2_E_DOI_10.21203_rs.3.rs-9617843_v10`，实际对应的记录编号为`S2_E_DOI_10.21203_rs.3.rs-9617843_v1_10`。这不只是排版问题：当新研究加入、旧结论更新或反证触发复核时，错误的引用关系会使证据无法可靠追踪。",
   "severity": "moderate",
   "fix": "以一个版本化数据库作为报告生成的唯一数据源，自动生成参考文献数、证据条数、结论数和假说数。生成时执行完整性测试，包括唯一ID、引用目标存在性、文献标识一致性、证据状态和版本差异检查。任何无法解析的证据关系都应阻止正式版本发布。"
  },
  {
   "rank": 10,
   "what": "部分未经同行评审的2026年预印本被用于支持重要机制结论，但正文没有在引用位置明确标示其出版状态。",
   "where": "第五章5.3：“Klocke等的研究提供了新的转弯任务证据。”第五章5.5：“2026年Beaudoin等的研究进一步分析了4名患者的STN-LFP数据……”并报告AUC=0.825。",
   "why": "Beaudoin研究的DOI:10.64898/2026.08.13.744293对应bioRxiv预印本；Klocke研究的DOI:10.21203/rs.3.rs-9617843/v1对应Research Square预印本，而不是已经完成同行评审的正式期刊论文。【turn372188search0】【turn372188search47】Beaudoin研究只有4名独立患者，虽然使用了患者留一交叉验证，但这不等于独立外部验证。AUC=0.825不能直接理解为已经获得稳定的跨患者预测性能。报告虽然在附录说明部分材料需要重新核验，但正文没有在这些关键结果旁边明确标出预印本状态，容易使读者高估证据成熟度。",
   "severity": "moderate",
   "fix": "在正文首次引用时明确标记预印本、同行评审状态和独立患者数量。将预印本结果作为探索性证据，不与已同行评审并经过独立重复的原始研究赋予相同权重。分类模型必须报告患者级独立验证、置信区间和外部验证情况。"
  }
 ],
 "overall": "这份报告的主要问题不是缺少机制假说，而是现有证据尚未被完整、准确地转化为这些机制假说的依据。尤其严重的是，附录中已经存在的多项关键原始研究没有进入主文综合，导致beta功率、beta burst、theta、神经熵及单神经元活动之间的冲突被部分简化；检索和筛选流程又存在大量截断、待定文献及证据池边界不清的问题。此外，存在原始研究误归类、PMID错配和机制解释不够严密等具体错误。报告关于STN参与FOG、患者异质性及分布式网络作用的总体方向具有研究价值，但目前的证据链不足以充分支持其所提出的机制优先级。最需要做的不是继续增加H14、H15等新假说，而是先把已有原始证据重新核验、补齐、分层和反证，确保每项综合结论都能追溯到正确的研究、正确的行为状态和正确的实验条件。"
}

===== abs_g6.json =====
{
 "standards": [
  {
   "n": 1,
   "verdict": "partly",
   "issues": [
    {
     "severity": "severe",
     "what": "检索范围广，但检索截断造成实质性遗漏风险。22条检索式中21条达到100篇取回上限，尤其动物模型、认知负荷、神经振荡及皮层-丘脑底核网络等方向。667篇候选文献中327篇仍处于待定状态，不能认为已经完成充分筛选。即使43篇主动补充的必读文献降低了遗漏风险，也不能弥补大规模检索截断。",
     "where": "§2.2：“22条检索式中，只有第1条没有发生截断，其余21条均达到或超过取回上限”；“动物模型相关检索命中8134篇，只取回98篇”；“327篇待定文献没有被题目和摘要筛选明确排除”。"
    },
    {
     "severity": "moderate",
     "what": "数据库覆盖有限。只使用Europe PMC，没有检索Embase、Scopus、Web of Science和Cochrane，也没有明确说明系统性前向、后向引文追踪或临床试验注册平台检索。对于DBS临床试验、神经外科刺激参数研究和跨学科机制研究，存在遗漏风险。",
     "where": "§2.1：“数据库：Europe PMC REST API”；§2.2：“未检索 Embase、Scopus、Web of Science 和 Cochrane”。"
    },
    {
     "severity": "moderate",
     "what": "已经发现的部分重要新证据没有充分进入正文综合。例如，2026年10月发表的PMID:42571859研究涉及步态周期锁定的皮层-丘脑底核活动、冻结相关低频活动及不同刺激条件，但主要只出现在结构化附录中，没有在正文的STN-皮层耦合和刺激频率讨论中得到充分分析。这属于检索之后的证据整合遗漏。",
     "where": "§5.7主要讨论：“Pozzi等，2019”及“Zhang等，2025”；附录则另外列有PMID:42571859。该研究的发表时间为2026年10月，早于报告检索截止日期。"
    }
   ]
  },
  {
   "n": 2,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "存在明确的PMID错引。PMID:40635563实际对应Disease-Modifying Trials in Treated Parkinson's Disease: Stable Treated Does Not Equate with Biological Stability，而不是14例胆碱能PET研究。所述胆碱能PET研究实际对应PMID:40512756，标题为Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease。正确文献虽然出现在参考文献表中，但正文引用错误，影响证据追溯。",
     "where": "§4.3：“14例胆碱能PET研究提示FOG严重程度与多个脑区胆碱能末梢功能降低相关。[PMID:40635563]”。"
    },
    {
     "severity": "moderate",
     "what": "预印本与正式发表版本没有建立明确的版本关联，存在重复计算独立证据的风险。例如，DOI:10.1101/2024.06.26.24309418与PMID:40677701是同一项beta-burst驱动自适应DBS研究的预印本和正式发表版本，涉及同一研究队列。二者分别进入参考文献表和证据表，甚至同时被用于C6、C12。如果作为独立研究计数，会夸大重复验证程度。",
     "where": "结构化附录同时列出：“DOI:10.1101/2024.06.26.24309418”和“PMID:40677701”；两者分别具有独立Evidence ID。"
    },
    {
     "severity": "moderate",
     "what": "证据数量存在三重不一致。正文称结构化证据表有539条，运行日志有544条，但实际附件JSON中的evidence数组只有538条。报告虽然发现了前两者之间的差异，却没有核对最终交付的结构化附录，因此证据总量及版本一致性仍未得到确认。",
     "where": "§2.3：“证据表包含539条证据，而检索运行日志记录从150篇文献中提取544条证据”；附录JSON实际包含538条evidence记录。"
    },
    {
     "severity": "minor",
     "what": "部分研究的样本量描述没有充分区分整体研究队列与实际发生FOG的事件亚组。Thenaisie等2022年研究并非整体只纳入4人：论文报告18名患者，12名参与步态实验，其中4名实际出现冻结事件。报告所述4人是正确的FOG事件亚组，但直接称研究样本只有4人容易造成研究规模误解。",
     "where": "§5.1：“4名PD患者”；“但该研究样本只有4人”。"
    }
   ]
  },
  {
   "n": 3,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "缺少系统性的研究质量和偏倚风险评价。报告对研究进行较强、中等、较弱的定性分级，也分析了不少单项研究的局限，但没有给出可重复的分级规则，也没有对临床RCT、观察性队列和预测模型系统使用RoB 2、ROBINS-I或适当的模型偏倚评价工具。因此，不同证据的可信度仍主要依赖叙述性判断。",
     "where": "§1.2：“较强：有明确原始研究支持，且主要结果具有一定重复性”；“中等：有直接研究支持，但样本量、实验条件或研究间一致性有限”；§2.1：“未进行PRISMA预注册，也未进行双人独立筛选”。"
    },
    {
     "severity": "moderate",
     "what": "STN+SNr联合刺激的正文综合遗漏了重要的相反方向证据。§8.8重点引用PMID:42909654的阴性Meta分析和PMID:42860886的45例探索性试验，但没有在正文讨论PMID:42968793。后者于2026年6月发表，纳入8项交叉RCT、97名患者，报告STN+SNr相较单独STN刺激显著降低FOG严重程度，SMD=-0.39，95% CI为-0.73至-0.04，I²=23.2%。虽然该Meta分析存在交叉试验配对数据不足、采用平行组近似计算等限制，但它是重要的相反证据。正文应比较两项Meta分析的纳入标准、统计处理、偏倚风险和证据确定性，而不应只呈现阴性结果。",
     "where": "§8.8：“2026年Meta分析纳入6项FOG研究、86名患者，联合刺激相较单独STN刺激的汇总效应为Hedges' g=-0.23”；同节只进一步讨论45例研究。附录却包含PMID:42968793及其8项RCT、97例患者的阳性结果。"
    },
    {
     "severity": "moderate",
     "what": "对PMID:42571859的综合不足。该2026年研究涉及步态周期锁定的皮层低频活动、S1-STN theta coherence，以及HFS和LFS对相关活动及冻结的调节。它对平均beta功率、步态相位调制、皮层-STN网络和低频刺激机制都有直接意义。报告虽然在附录保留了该证据，但没有将其充分纳入§4.4、§5.4和§5.7的正文比较，导致最新网络电生理证据没有真正改变现有机制综合。",
     "where": "§5.7：“Pozzi等，2019”；“Zhang等，2025”；§4.4主要讨论60 Hz、80 Hz和130 Hz研究。附录另有PMID:42571859，但正文没有相应的研究讨论。"
    },
    {
     "severity": "minor",
     "what": "对Zhang等2025年研究的统计方向评价可能存在误读。报告认为论文内部统计结果与图注方向不一致，但原论文定义的百分比变化为(Walk-Turn)/Walk，正系数对应的可能是转弯期相对行走基线的下降。图注所述PMC-STN coherence增加与较短冻结持续时间相关，可以与该归一化方向相容。需要结合公式和系数符号解释，而不能仅凭文字表述不同就认定研究内部矛盾。",
     "where": "§5.7：“论文内部部分统计结果及图注的方向报告存在不一致，部分效应的统计证据较弱。”"
    }
   ]
  },
  {
   "n": 4,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "证据-结论-假说的分层设计较好，但结构化关联仍有具体错误。C6引用了一个不存在的Evidence ID：S2_E_DOI_10.21203_rs.3.rs-9617843_v10，而实际证据记录的ID为S2_E_DOI_10.21203_rs.3.rs-9617843_v1_10。该错误会使程序化检索或后续更新无法正确定位证据。",
     "where": "结构化附录JSON中C6的evidence关联：“S2_E_DOI_10.21203_rs.3.rs-9617843_v10”；实际evidence记录使用：“S2_E_DOI_10.21203_rs.3.rs-9617843_v1_10”。"
    },
    {
     "severity": "moderate",
     "what": "缺少预印本与正式发表版本之间的version-of关系。至少一组同一研究的两个版本被作为独立文献和独立证据记录使用，C6和C12还同时关联这两个版本。长期知识系统需要明确区分文献版本与独立研究，避免同一患者队列在证据网络中重复提供支持。",
     "where": "附录中同时存在DOI:10.1101/2024.06.26.24309418和PMID:40677701；两者分别建立Evidence ID，但没有明确的版本关联字段。"
    },
    {
     "severity": "moderate",
     "what": "证据与结论的关联还需要进一步精细化。PMID:42571859主要提供步态周期锁定的皮层低beta和皮层-STN theta coherence证据，并非直接的STN beta burst持续时间研究。它可以支持步态相位调制，但不宜不加区分地作为STN beta burst机制的直接支持。与此同时，该研究与C2的刺激频率及C8的皮层-STN耦合关系也有直接关联，却没有完整反映在对应的证据关系中。",
     "where": "结构化附录C6的证据关系与PMID:42571859记录；C2和C8的证据关联中没有对应的该研究记录。"
    }
   ]
  },
  {
   "n": 5,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "报告已经设计了较好的长期知识积累结构，包括稳定Evidence ID、研究条件字段、结论和假说关系、更新触发条件。但是这些主要是设计方案，没有展示已经运行的持久化知识库、历史版本、跨报告检索记录或新证据触发旧结论修订的真实案例。因此，能够建立长期积累机制的设计已经具备，但长期运行能力尚未得到验证。",
     "where": "§9.1：“建议将知识库从简单的文献列表升级为具有证据关系和版本管理能力的研究知识系统”；§9.3：“建议以下情况自动触发旧结论复核”。"
    },
    {
     "severity": "minor",
     "what": "尚未提供知识更新历史或结论变更日志。虽然给出了C1-C21和H1-H13的重新评价触发条件，但没有展示某篇新论文进入系统后，哪些旧证据、结论和假说被修改，以及修改前后的证据等级变化。",
     "where": "§9.2：“每条证据可以支持一个结论；反驳一个结论；限定结论的适用条件”；§9.3主要使用未来条件句描述更新方式。"
    }
   ]
  },
  {
   "n": 6,
   "verdict": "met",
   "issues": []
  },
  {
   "n": 7,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "报告能够发现系统和研究成果中的缺陷，并提出改进流程，但没有完成从缺陷发现到原因验证、实际修复和效果验证的完整闭环。例如，21条截断检索没有重新执行，327篇待定文献没有完成筛选，539与544条证据的差异没有查明，实际附录538条的额外差异也没有修复，错误PMID和缺失Evidence ID仍然存在。这说明缺陷识别能力较强，但自主改进尚未得到实际证明。",
     "where": "§9.5：“本次资料整理本身也存在值得进一步修正的问题”；“22条检索式中21条发生截断”；“327篇文献处于待定状态”；“结构化知识部分报告539条证据，而运行日志报告544条”；§9.5：“下一轮知识库改进不应只是增加文献数量”。"
    },
    {
     "severity": "moderate",
     "what": "没有建立改进效果的量化验证指标。例如，补充检索后重要原始研究的召回率是否提高、独立研究与重复预印本的区分准确率是否提高、引用错误率是否下降、证据关联完整率是否提高，均没有实际测试结果。因此，无法判断提出的质量控制流程是否真正改善了系统。",
     "where": "§9.4：“建议每次更新执行以下检查”；§9.5列出改进需求，但没有报告任何修复前后对照或验证结果。"
    }
   ]
  }
 ],
 "spot_checks": [
  {
   "claim": "C1：STN-DBS能够改善部分患者FOG，但疗效存在明显异质性。",
   "cited": "PMID:18413568; PMID:31755599; PMID:27766724; PMID:41659700; PMID:42098512",
   "verdict": "consistent",
   "why": "123例连续病例研究显示，术前存在FOG的患者多数能够通过STN刺激重现左旋多巴带来的改善，但有11例术后首次出现FOG或无法完成步行测试。EARLYSTIM二次分析显示24个月时刺激组FOG比例从52%下降到34%，药物组没有相同变化。2017年Meta分析只有6项研究提供FOG数据。2026年Meta分析纳入31项研究、905例患者，21项提供FOG-Q数据，报告总体小幅改善，但混合不同刺激靶点。2026年网络Meta分析的10项FOG-Q研究则没有任何DBS模式达到统计学显著改善，I²=88.3%。因此，报告关于部分患者获益和疗效异质性的综合结论成立。报告也正确指出总体DBS Meta结果不能完全归因于STN。【turn855985search3】【turn855985search2】【turn169697search1】【turn169697search0】【turn855985search4】"
  },
  {
   "claim": "C2：低频刺激可能改善特定HFS下发生FOG的患者，但不能认为60 Hz普遍优于高频刺激。",
   "cited": "PMID:28529730; PMID:24165197; PMID:25540305; PMID:41659700; PMID:38948151; PMID:40504072",
   "verdict": "consistent",
   "why": "Xie等2017年Mini-review总结的积极结果主要来自常规HFS下实际出现FOG的选择性患者，且多项阳性研究样本很小。Phibbs等随机盲法交叉研究纳入20人，没有发现60 Hz相较130 Hz在主要步幅指标上的显著改善。2026年网络Meta分析也没有发现60 Hz或其他DBS模式能够显著改善FOG-Q。报告对60 Hz疗效的患者选择性、药物状态、TEED和任务依赖性解释与原始研究一致。【turn421716search0】【turn421716search1】【turn169697search0】"
  },
  {
   "claim": "C3：STN刺激位置和结构连接网络可能比单一STN坐标更能解释部分临床差异。",
   "cited": "PMID:37701817; PMID:36242900; PMID:35431262; PMID:39475137; PMID:40709562",
   "verdict": "consistent",
   "why": "76例回顾性研究识别出背外侧STN相关改善区域和腹内侧中央区域相关恶化区域；19例前瞻性研究发现感觉运动皮质-STN连接与较轻FOG相关，而前额叶-STN连接与较重FOG相关；47例研究发现运动区、前额叶和PPN/SNr相关通路与改善有关。另有10例随机双盲交叉研究发现central STN定向刺激较posterior STN减少FOG发作。报告将这些结果定位为跨研究关联，而不是已经确立的固定最佳刺激位置，判断恰当。【turn817105search3】【turn817105search0】【turn817105search2】【turn817105search1】"
  },
  {
   "claim": "C4：STN神经活动与FOG易感状态及实际冻结事件有关。",
   "cited": "PMID:35310098; PMID:36070366; PMID:30196050; PMID:31505548; PMID:40709562",
   "verdict": "consistent",
   "why": "Liu等同步记录研究在8名患者中发现FOG期间STN beta功率高于非冻结行走期间。Thenaisie等研究的18名总体患者中，12名参加步态实验，其中4名实际发生FOG，这些事件中观察到低beta增强。Anidi等研究在5名实际发生冻结的患者中发现beta burst持续时间延长。Pozzi等研究发现冻结期间皮层-STN低频耦合下降。Collomb-Clerc等2025年研究进一步发现，后续出现FOG的步态启动试次存在不同的STN区域-步态维度关联。这些证据支持神经活动与FOG状态相关，但不能证明必要性或因果性，符合报告的表述。【turn331606search0】【turn145413view0】【turn116097view0】【turn331606search4】【turn736057search0】"
  },
  {
   "claim": "C5：平均STN beta功率不存在跨患者、跨任务和跨冻结阶段的统一变化方向。",
   "cited": "PMID:35310098; PMID:36070366; PMID:28890315; PMID:31505548; PMID:37860957; PMID:33240199",
   "verdict": "consistent",
   "why": "Liu等和Thenaisie等报告实际FOG期间beta或低beta增强；Syrkin-Nikolau等报告FOG患者在未冻结行走时的STN beta活动低于非FOG患者；Pozzi等没有发现冻结期STN beta功率的相应显著变化，但发现皮层-STN低频耦合下降。Bougou等骑行研究观察的是运动相关beta抑制增强，而不是实际FOG期间的功率变化。报告区分了平均功率、运动相关ERD、burst持续时间和任务状态，因此其不存在统一beta方向的结论与证据一致。【turn331606search0】【turn145413view0】【turn305791view0】【turn331606search4】"
  },
  {
   "claim": "C6：STN beta burst时间结构可能比平均beta功率更接近部分FOG相关机制，但仍需验证。",
   "cited": "PMID:30196050; DOI:10.64898/2026.08.13.744293; DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "consistent",
   "why": "Anidi等研究发现实际冻结期间beta burst持续时间延长；Klocke等2026年预印本报告冻结转弯中的长burst比例和分布发生重组，但平均burst持续时间并不必然增加；Beaudoin等2026年预印本在4名患者中观察到冻结前转弯的burst间隔熵变化，并报告AUC约0.825。这些结果支持时间结构可能提供平均功率之外的信息，但样本量小、存在预印本，而且没有充分证明burst指标在独立患者中稳定优于平均功率。报告使用“可能”和“候选机制”的限定是合理的。【turn116097view0】【turn257893search34】"
  },
  {
   "claim": "C7：Theta及低beta活动与步态启动、节律和平衡有关，但具有明显阶段依赖性。",
   "cited": "PMID:31494286; PMID:40709562; DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "consistent",
   "why": "Storzer等研究将低beta和theta变化与FOG易感性联系起来，但易感状态不等于实际冻结。Collomb-Clerc等研究发现步态启动阶段posterior和central STN活动与pace、rhythm及balance的关系具有FOG试次特异性。Klocke等预印本则报告正常转弯准备阶段theta增强，而实际冻结转弯期间theta峰值功率降低。报告明确指出，FoG-Turn相对Walking的显著性不能替代FoG-Turn与Regular Turn的直接统计比较，因此没有把这些结果强行整合为已验证的统一时间序列模型。【turn435325search2】【turn736057search0】【turn257893search34】"
  },
  {
   "claim": "C8：STN-皮层耦合可能参与冻结前后的网络状态转换，但变化具有区域和阶段特异性。",
   "cited": "PMID:31505548; PMID:41131028",
   "verdict": "consistent",
   "why": "Pozzi等2019年研究发现实际冻结期间SMA、M1和顶叶皮层与STN之间的4–13 Hz低频耦合下降，并在恢复行走时恢复。Zhang等2025年研究在19名患者中发现PMC-STN和M1-STN alpha coherence存在不同的阶段性变化，支持不同皮层区域与STN之间的网络重组。报告同时强调coherence不能确定信息传递方向，也不能证明皮层对STN的因果驱动，因此核心结论与原始研究一致。【turn331606search4】【turn392324view0】【turn392324view1】"
  }
 ]
}

===== factcheck.json =====
[
 {
  "paper": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping",
  "pmid": "41388789",
  "doi": "",
  "report_says": "第5.6节将该研究作为冻结期间低beta活动与下肢肌肉共同激活可能同时出现的证据；第7.6节又将其作为APA、双侧肌肉协调及冻结前STN-EMG异常的证据。",
  "judge_says": "原研究纳入14名PD患者，记录坐位、站立和原地踏步时的STN-LFP及下肢EMG，没有记录真正的冻结事件。因此不能用它直接证明实际冻结期间或冻结前存在肌肉共同激活。作者也明确提醒，不能将原地踏步结果直接推广到自由行走和真实冻结。直接研究真实冻结期间STN-LFP与拮抗肌EMG的研究是Klocke等2024年论文（PMID:39470410）。",
  "source": "open_g6.json",
  "pid": "PMID:41388789",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "Overall, stepping was associated with the highest low-beta band activities and the lowest high-beta activities compared with standing and sitting.",
   "Furthermore, STN beta bursts were associated with increased muscle activation at movement initiation, potentially reducing the ability to move freely.",
   "It is further speculated that elevated muscle co-activation, especially during movement phases when the muscles are normally expected to act in opposition, may reflect altered or maladaptive motor control strategies.",
   "PL, as a major mover and stabilizer of the foot and ankle, acts complementary to GA during stepping, especially in the stance phase.",
   "The reduction in STN beta activity appears to precede changes in EMG activity (Fig. 3A), suggesting a causal relationship where STN activity influences muscle activation.",
   "In fact, increases in pathological beta and theta rhythms in the STN have been observed to precede a temporal chain of abnormal lower limb muscle firing detected by EMG.34",
   "Further analysis examined STN-muscle coherence and IMC (between the gastrocnemius-peroneus longus coherence of the same leg) in relation to the stepping phase."
  ],
  "judge_quotes": [
   "Local field potentials (LFPs) in the STN and leg muscle activity measured as EMG of the gastrocnemius and peroneus longus were recorded in 14 PD patients during sitting, standing and stepping, ON and OFF levodopa.",
   "The paradigm consisted of three separate segments: resting (sitting), standing and stepping.",
   "During the stepping-in-place condition, patients were instructed to step at a comfortable and consistent frequency, and to imagine themselves walking normally.",
   "Moreover, analyses in this study focused on steps that could be reliably detected using force plate measurements and did not include episodes of hastening or true freezing.",
   "Therefore, attributing the present effects directly to free walking should be approached cautiously, although a previous study showed similar pattern of STN beta-band modulation aligned to the stepping phase within each step cycle during free walking in a few patients.",
   "Whether the observed increases in STN beta activity and intermuscular coherence during the late stance phase when OFF levodopa are associated with poor motor performance during free walking remains to be tested in future studies.",
   "Additionally, while the gastrocnemius and peroneus longus were selected in this study for their known roles in stance stability and foot control, simultaneous monitoring of multiple muscles in future studies, especially multiple antagonistic muscle pairs, such as the gastrocnemius and tibialis anterior may offer more insight on the pathophysiology of free walking."
  ],
  "why": "报告的说法部分有依据，但存在关键的外推问题。第一，第5.6节所述的生理现象有一定依据：论文发现原地踏步时STN低beta活动高于坐位和站立，并发现STN beta bursts与运动启动时GA和PL肌肉EMG活动增加有关。作者也在引言中提出了肌肉共同激活可能反映异常运动控制的假设。但是，这些结果并非来自真实冻结事件。更重要的是，beta burst与EMG的关联分析使用的是广义beta活动，不能直接等同于低beta特异性与拮抗肌共同激活的关联。GA与PL在文中被描述为互补作用的肌肉，而不是拮抗肌。作者还明确提出，未来需要监测更多肌肉，尤其是GA与TA这样的拮抗肌对。因此，将这些发现描述为真实冻结期间低beta与下肢肌肉共同激活同时出现的证据，缺少改变结论的重要限定。第二，第7.6节的说法也只有部分依据。论文确实记录了左右两侧GA和PL的EMG，也报告了STN活动与EMG变化之间的时间关系，并在引言中引用了既往关于STN beta/theta活动先于异常下肢肌肉放电的研究。但是，本文没有报告anticipatory postural adjustments（APA）的测量或分析。虽然记录了双侧肌肉活动，其IMC分析明确针对同一侧GA与PL之间的协调，而非左右肢体之间的双侧协调。此外，本文观察到的STN-EMG时间关系发生在原地踏步的特定步态阶段，不能据此认定为冻结发生前的异常。指控者关于研究设计、未记录真实冻结以及不能直接推广到自由行走的描述，均得到全文明确支持。特别是作者在Limitations中直接说明，分析没有纳入真实冻结事件，并要求对自由行走的外推保持谨慎。不过，关于Klocke等2024年论文（PMID:39470410）是直接研究真实冻结期间STN-LFP与拮抗肌EMG的研究，这一具体信息没有出现在所提供的本文全文中，因此不能仅依据本文独立确认。综合而言，报告存在过度外推和部分证据归属不准确的问题；指控者对本文研究设计及其局限性的核心判断成立，但其关于另一篇论文的具体说法无法由本文验证。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Pozzi等，2019年，冻结期间theta-alpha皮层-STN耦合及STN局部振荡活动研究",
  "pmid": "31505548",
  "doi": "",
  "report_says": "第5.4节的beta冲突表主要呈现beta增加、降低及运动相关beta抑制增强等结果；第5.4节引用该研究支持冻结期间theta-alpha皮层-STN耦合下降，但没有充分呈现其局部STN阴性结果。",
  "judge_says": "原研究不仅报告了冻结期间theta-alpha皮层-STN耦合下降，还发现实际冻结期间STN低频功率、beta功率和beta burst持续时间与正常步行相比均无显著差异。这些阴性结果直接限制了将局部STN beta异常解释为普遍冻结机制的结论，应与耦合结果一并报告。",
  "source": "open_g6.json",
  "pid": "PMID:31505548",
  "report_supported": "partly",
  "judge_supported": "yes",
  "report_quotes": [
   "In contrast, gait freezing was characterized by a low frequency cortical-subthalamic decoupling in the hemisphere with less striatal dopaminergic innervation (H−) (Fig. 4A).",
   "We first studied power changes in low frequency (i.e. θ-α rhythms) and in the β-frequency band of the two STN and did not find any differences during gait freezing in comparison to (effective) walking (Fig. 3A and B).",
   "We also assessed the duration of β-burst and did not find a difference between (effective) walking and gait freezing (Fig. 3C)."
  ],
  "judge_quotes": [
   "We first studied power changes in low frequency (i.e. θ-α rhythms) and in the β-frequency band of the two STN and did not find any differences during gait freezing in comparison to (effective) walking (Fig. 3A and B).",
   "We also assessed the duration of β-burst and did not find a difference between (effective) walking and gait freezing (Fig. 3C).",
   "In contrast, gait freezing was characterized by a low frequency cortical-subthalamic decoupling in the hemisphere with less striatal dopaminergic innervation (H−) (Fig. 4A).",
   "Despite the lack of subthalamic activity changes during gait freezing in our study, exaggerated STN β-synchronization may still influence dynamic motor processing in favour of gait freezing development (Anidi et al., 2018)."
  ],
  "why": "报告的说法判为partly：原文明确支持冻结期间theta-alpha皮层-STN耦合下降，因此将该研究作为这一网络耦合结果的依据是正确的。但原文同时明确报告了三个局部STN阴性结果：低频（theta-alpha）功率无显著差异、beta功率无显著差异、beta burst持续时间无显著差异。如果第5.4节只呈现耦合下降而没有充分呈现这些结果，就会使研究发现的整体图景不完整，尤其可能造成将网络耦合异常与局部STN振荡异常混为一谈的问题。不过，附件没有提供报告第5.4节本身，因此无法独立核实beta冲突表的具体内容及其实际遗漏程度。指控者的说法判为yes：上述三个阴性结果均有原文直接依据，而且原文第100行附近的结果明确报告了theta-alpha皮层-STN解耦，说明两类结果确实同时存在。阴性结果限制了将局部STN beta异常视为普遍冻结机制的解释，但不能据此断言STN beta活动完全不参与冻结。原文讨论部分明确保留了这种可能性。另需注意，研究比较的是患者冻结期间与患者自身有效步行（effective walking），而不是与健康对照者的正常步行；研究仅纳入7名患者，并记录到14次冻结事件。因此，指控者的核心判断成立，但应避免将实验结果扩大为对所有冻结情境的绝对结论。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Zhang等，2025年，PMC-STN alpha coherence与冻结持续时间研究",
  "pmid": "41131028",
  "doi": "",
  "report_says": "第5.7节仅称部分PMC-STN alpha指标与冻结持续时间存在关系，没有说明相关方向；第7.3节仍将H4代偿性耦合与H5病理性过度耦合作为基本对等的竞争解释。",
  "judge_says": "原研究发现，TurnPre阶段增强的PMC-STN alpha coherence与更短的冻结持续时间相关。这一效应方向目前更支持H4所提出的代偿性解释，而不是H5所提出的病理性过度耦合解释。报告遗漏了具有机制区分价值的相关方向，没有据此调整两个假说的当前支持程度。",
  "source": "open_g6.json",
  "pid": "PMID:41131028",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "Increased PMC-STN alpha coherence during the TurnPre phase (but not during the TurnStart phase) relative to walking predicted shorter freezing episodes (β = 0.205, p = 0.006).",
   "The increased coherence between the PMC and STN may reflect a compensatory mechanism to maintain motor control in the face of disrupted cortical signals; however, this abnormal coupling could also contribute to the rigidity and motor impairments characteristic of FOG."
  ],
  "judge_quotes": [
   "Increased PMC-STN alpha coherence during the TurnPre phase (but not during the TurnStart phase) relative to walking predicted shorter freezing episodes (β = 0.205, p = 0.006).",
   "During normal turning, significantly higher PMC-STN alpha coherence was observed in the TurnPre phase (p = 0.0045, Fig. 3A). In contrast, during turning freeze, there was an increase in PMC-STN alpha coherence (p = 0.048) and a decrease in M1-STN alpha coherence (p = 0.043) during the TurnStart phase (Fig. 3B).",
   "The increased coherence between the PMC and STN may reflect a compensatory mechanism to maintain motor control in the face of disrupted cortical signals; however, this abnormal coupling could also contribute to the rigidity and motor impairments characteristic of FOG.",
   "B Freezing of Turning: A delayed and exaggerated increase in PMC-STN alpha coherence and concurrent decoupling of M1-STN alpha coherence was observed during the TurnStart phase."
  ],
  "why": "报告的说法只能部分得到全文支持。首先，报告称原文没有说明相关方向，这与图4图注明确矛盾：原研究明确指出，TurnPre阶段相对于行走状态增强的PMC-STN alpha coherence预测更短的冻结发作。这是具有机制区分价值的方向性结果，不能仅概括为存在相关关系。其次，原文讨论确实同时提出了代偿性耦合和病理性耦合两种可能解释，因此将其描述为竞争性解释有依据；但将二者视为基本对等，忽略了TurnPre阶段增强的耦合与更短冻结持续时间之间的关系，缺少重要限定。指控者的判断也只能部分得到支持：其关于相关方向的描述有明确原文依据，而且这一方向确实更符合代偿性解释；但原文没有正式宣布H4优于H5。讨论仍然保留了病理性解释，并且明确区分了TurnPre阶段与冻结发生时TurnStart阶段延迟且夸大的PMC-STN alpha coherence增强。因此，更准确的结论是：TurnPre阶段的持续时间预测结果为H4提供了相对更有利的证据，但不足以据此排除H5或认定原研究已经完成了两个机制假说的正式比较。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease",
  "pmid": "40512756（正确文献）；40635563（报告错误引用）",
  "doi": "",
  "report_says": "第3.3节称14例胆碱能PET研究提示FOG严重程度与多个脑区胆碱能末梢功能降低相关，并引用PMID:40635563。",
  "judge_says": "PMID:40635563实际对应Disease-Modifying Trials in Treated Parkinson's Disease: Stable Treated Does Not Equate with Biological Stability，与胆碱能PET和FOG研究无关。真正的原始论文是PMID:40512756。该研究确实纳入14名PD患者，但研究对象是ON-medication FOG，发现胆碱能示踪剂空间协变模式与ON-FoG严重程度相关，并没有发现相应的OFF-FoG关联。因此报告既引用了错误的PMID，也将ON-state特异性结果泛化为一般FOG机制。",
  "source": "open_g6.json",
  "pid": "PMID:33240199",
  "report_supported": "partly",
  "judge_supported": "cannot_tell",
  "report_quotes": [
   "Additionally, cholinergic loss in the pedunculopontine nucleus may play a role in FoG, as it stands at the crossroads between supraspinal and spinal gait centers (50).",
   "This review is focused on the electrophysiological findings related to PDFOG+, in which the studies of imaging findings are excluded. However, excellent reviews on imaging technology can be found in recent papers (36, 37, 116)."
  ],
  "judge_quotes": [
   "Following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses statement (61), the eligibility criteria for articles included those published before March 2020, written in English, and currently published journal or full-length conference articles.",
   "This review is focused on the electrophysiological findings related to PDFOG+, in which the studies of imaging findings are excluded. However, excellent reviews on imaging technology can be found in recent papers (36, 37, 116).",
   "Additionally, cholinergic loss in the pedunculopontine nucleus may play a role in FoG, as it stands at the crossroads between supraspinal and spinal gait centers (50)."
  ],
  "why": "报告的说法为partly：全文确实提到PPN胆碱能功能丧失可能参与FOG，因此存在一般性胆碱能机制的依据。但全文没有报告14例患者的胆碱能PET研究，也没有提及FOG严重程度与多个脑区胆碱能末梢功能降低之间的相关性。相反，作者明确说明本文聚焦于电生理研究，并排除影像学研究结果。因此，不能将这句一般性机制描述视为对报告所述具体PET研究结果的完整支持，缺少的研究证据和限定条件具有实质意义。指控者的说法为cannot_tell：全文没有出现PMID:40635563或PMID:40512756，也没有提供所谓原始研究的14例患者、ON-medication FOG、胆碱能示踪剂空间协变模式或ON与OFF状态关联差异等信息。全文的研究纳入时间限定为2020年3月之前，且明确排除影像学研究。故仅凭这篇全文，既不能验证指控者关于两个PMID对应关系的判断，也不能验证其对ON/OFF研究结果的描述。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Moreau等，2008年，13例患者60 Hz低频STN-DBS原始研究",
  "pmid": "18420482（原始研究）；28529730（报告引用的mini-review）",
  "doi": "",
  "report_says": "第4.4节介绍13例60 Hz刺激研究时引用PMID:28529730，作为该项具体临床试验的文献依据。",
  "judge_says": "PMID:28529730本身是低频与高频STN-DBS研究的mini-review，并不是纳入13例患者的原始试验论文。对应的原始Moreau等研究是PMID:18420482。报告在讨论具体患者数量、刺激参数和随访结果时，应直接引用原始研究，而不能将综述作为原始试验证据。",
  "source": "open_g6.json",
  "verdict": "paper_not_in_kb"
 },
 {
  "paper": "PMID:33240199，STN电生理相关mini-review",
  "pmid": "33240199",
  "doi": "",
  "report_says": "第5.4节将PMID:33240199作为STN beta降低的证据来源。",
  "judge_says": "PMID:33240199是一篇电生理mini-review，而不是原始研究。报告不能将综述对既有研究的总结等同于独立的原始实验结果。讨论具体beta降低现象时，应追溯并引用相应原始论文，而不能将二手综述作为原始证据。",
  "source": "open_g6.json",
  "pid": "PMID:33240199",
  "report_supported": "yes",
  "judge_supported": "yes",
  "report_quotes": [
   "In the works by Gratkowski and Storzer, a decreased beta-band activity was observed in the STN from DBS leads.",
   "Later, Storzer et al. (115) observed a reduction of beta power in the STN during cycling compared to walking in both PDFoG+ and PDFoG– groups during the OFF state.",
   "During their active gait paradigm, Syrkin-Nikolau et al. (30) compared stepping in place, forward walking, and instrumented walking, which included a turning and barrier course. During stepping in place, a decreased STN beta-band power was found in the PDFoG+ compared to the PDFoG–.",
   "During FoG events, increased alpha sample entropy and decreased beta power were found compared to walking without FoG."
  ],
  "judge_quotes": [
   "The major aim of this review is to highlight the most up-to-date studies that explain the mechanisms underlying FoG through electrophysiology explorations.",
   "Following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses statement (61), the eligibility criteria for articles included those published before March 2020, written in English, and currently published journal or full-length conference articles. PubMed was used as the primary information source with the search query “EEG OR LFP AND Parkinson's Disease AND Freezing of Gait.”",
   "In the works by Gratkowski and Storzer, a decreased beta-band activity was observed in the STN from DBS leads.",
   "Later, Storzer et al. (115) observed a reduction of beta power in the STN during cycling compared to walking in both PDFoG+ and PDFoG– groups during the OFF state.",
   "During their active gait paradigm, Syrkin-Nikolau et al. (30) compared stepping in place, forward walking, and instrumented walking, which included a turning and barrier course."
  ],
  "why": "两个说法可以同时成立。第一，报告的说法有全文依据。该综述明确总结了STN beta降低的现象，包括Gratkowski和Storzer的研究、Storzer等人的骑行与步行比较，以及Syrkin-Nikolau等人的步行实验。因此，将PMID:33240199作为STN beta降低这一现象的文献依据，并不与全文内容矛盾。第二，指控者的说法也有全文依据。文章标题明确标明为Electrophysiology Mini-Review，摘要明确说明其目的是总结既有研究，方法部分也明确描述了文献检索过程。尤其重要的是，文章将具体STN beta变化归属于其他研究者，并标注了原始文献编号（如26、73、115、30），而不是将这些结果报告为本文作者独立开展的实验。因此，PMID:33240199可以支持报告所述现象，但不能因此被视为产生该实验结果的原始研究。如果报告只是将其作为综述性文献引用，则没有读错；如果将其当作独立原始实验数据的来源，则存在证据类型混淆。追溯并引用相应原始论文是合理的证据引用要求。",
  "verdict": "accusation_rejected"
 },
 {
  "paper": "TBS-DBS随机、双盲、短期临床研究",
  "pmid": "40383539",
  "doi": "",
  "report_says": "第7.9节将TBS-DBS机制组织为即时病理驱动反弹与长期神经可塑性两种竞争解释；第8.8节仅概括称TBS相关证据主要来自短期探索性研究，没有在核心机制讨论中充分呈现该试验的主要阴性结果。",
  "judge_says": "原研究是一项随机、双盲、短期研究，纳入15名PD患者。主要结局FoG-Course在整个患者样本中并未显示TBS-DBS优于连续DBS，只有7/15名患者主观评价TBS-DBS相当或更好。该试验也没有直接操纵刺激暂停时间，没有证明暂停期间STN病理活动反弹，更没有证明长期神经可塑性。因此报告遗漏了主要阴性结果，并应明确区分临床试验实际发现与H12、H13提出的待检验机制假说。",
  "source": "open_g6.json",
  "pid": "PMID:40383539",
  "report_supported": "partly",
  "judge_supported": "yes",
  "report_quotes": [
   "The spacing of stimulation trains and insertion of stimulation pauses with TBS-DBS might represent a double-edged sword for DBS application.",
   "On the one hand, there is evidence of re-emerging tremor during spaced thalamic deep brain stimulation depending on the length and timing of the stimulation pause.",
   "The finding of impaired, short-term efficacy in tremor suppression by non-continuous DBS was interpreted as the inability to mask burst-driver inputs to the thalamus.",
   "This might partially explain the slightly inferior short-term effect on objective gait parameters and the FoG-Course of TBS-DBS as a whole group compared to cDBS.",
   "On the other hand, we assumed TBS-DBS to be potentially advantageous for gait due to the following reasons:",
   "TBS-DBS with its temporal patterning might slowly, progressively increase its subthalamic efficacy in the long-term by beneficial neuroplastic effects from TBS-DBS.",
   "For the exploration of the full effect strength, a long-term evaluation of TBS-DBS would be necessary, which has not been performed here in the randomised study of short-term effects.",
   "The most important limitation in the evaluation of patterned DBS algorithms is the assessment of short-term effects of TBS-DBS on gait within one day, since the effects of patterned DBS might evolve over time and axial symptoms typically respond over a longer time course."
  ],
  "judge_quotes": [
   "In this monocentric, randomised, double-blind, short-term study, 12 age-matched controls (11 male, age 59 ± 8 years) and 15 PD participants (14 male, age 62 ± 9 years, disease duration 15 ± 6 years) with subthalamic stimulation (76 ± 39 months) were assessed with clinical scores (FoG-Course, MDS-UPDRS) and a standardized gait course simulating everyday life situations.",
   "The primary outcome, the relative change of FoG-Course by DBS, was not superior with TBS-DBS compared to cDBS in the entire sample.",
   "Seven of fifteen PD participants rated subjectively TBS-DBS equal or better than cDBS (“TBS-preference group”).",
   "In detail, the TBS pattern consists of 5 cycles per second, with each cycle containing 0.1s bursts at 200 Hz followed by a 0.1s pause.",
   "During the standardized gait course a mobile, 24-channel EEG system and 6 wearable axial kinematic sensors were used.",
   "On the one hand, there is evidence of re-emerging tremor during spaced thalamic deep brain stimulation depending on the length and timing of the stimulation pause.",
   "In this study, we found no superior effects of TBS-DBS compared to cDBS for the FoG-Course or the MDS-UPDRS III in the entirety of the group.",
   "Since axial symptoms might change over days, the EEG might potentially point to advantageous long-term changes, which could not be proven in that acute experimental setting.",
   "For the exploration of the full effect strength, a long-term evaluation of TBS-DBS would be necessary, which has not been performed here in the randomised study of short-term effects.",
   "The FoG-Course was not significantly different between TBS-DBS and OFF-DBS and TBS-DBS and cDBS in the whole sample (all p values > 0.362."
  ],
  "why": "报告的机制框架有明确原文依据。作者确实使用“double-edged sword”描述TBS-DBS的间歇刺激模式，并分别讨论了两个方向：一是刺激暂停可能使丘脑burst-driver输入重新显现，从而影响短期疗效；二是时间模式可能通过长期神经可塑性改善治疗效果。因此，将其概括为潜在的短期不利机制与长期有利机制，基本符合原文。但存在重要限定：第一种解释引用的是既往间歇性丘脑DBS研究中的震颤重新出现现象，作者只认为它可能部分解释本试验的结果，并没有证明TBS暂停期间STN病理活动反弹。第二种解释也只是作者提出的假设，原文明确承认尚未进行长期评估，不能作为已证实机制。指控者对原研究的描述有全文依据：研究确为随机、双盲、短期研究，共纳入15名PD患者；摘要明确报告全组FoG-Course主要结局未显示TBS-DBS优于cDBS，7/15名患者主观评价相当或更好。方法部分只采用固定的0.1秒刺激暂停，没有比较不同暂停时长；研究使用移动EEG和运动学传感器，没有直接证明暂停期间STN病理活动反弹。作者也明确承认长期神经可塑性尚未得到证明。需要补充一个统计学限定：原文报告全组主要结局未显示TBS-DBS优越，但不能据此简单说TBS-DBS在直接组间比较中显著劣于cDBS，因为原文另报告TBS-DBS与cDBS的FoG-Course直接比较未达到统计学显著性（all p values > 0.362）。因此，报告对两种机制的组织方式有依据，但若没有充分呈现全组主要阴性结果及机制尚未验证的限定，就属于重要信息呈现不充分。至于报告第8.8节实际是否遗漏或低估了该结果，这是对报告文本本身的判断，不能仅凭论文全文独立核实。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping",
  "pmid": "41388789",
  "doi": "",
  "report_says": "第五章5.6称，冻结期间低beta活动与下肢肌肉共同激活可能同时出现，并引用该研究作为证据。",
  "judge_says": "原研究纳入14名帕金森病患者，记录坐位、站立和踏步任务中的STN-LFP及下肢EMG，没有实际冻结事件分析，也没有FOG与非FOG患者分组。研究报告的是不同运动状态及左旋多巴对低、高beta活动的影响，以及beta burst与运动启动时肌肉活动的关系，并非实际冻结期间的低beta与肌肉共同激活。",
  "source": "open_g56.json",
  "pid": "PMID:41388789",
  "report_supported": "partly",
  "judge_supported": "yes",
  "report_quotes": [
   "Low-beta (12–20 Hz) and high-beta (21–35 Hz) were differentially modulated by stepping movements and levodopa, with reduced high-beta and increased low-beta during stepping compared with standing and sitting.",
   "Furthermore, STN beta bursts were associated with increased muscle activation at movement initiation, potentially reducing the ability to move freely.",
   "It is further speculated that elevated muscle co-activation, especially during movement phases when the muscles are normally expected to act in opposition, may reflect altered or maladaptive motor control strategies.",
   "Moreover, analyses in this study focused on steps that could be reliably detected using force plate measurements and did not include episodes of hastening or true freezing."
  ],
  "judge_quotes": [
   "Local field potentials (LFPs) in the STN and leg muscle activity measured as EMG of the gastrocnemius and peroneus longus were recorded in 14 PD patients during sitting, standing and stepping, ON and OFF levodopa.",
   "A total of 14 patients were recruited for the study",
   "All 1-min segments of standing and stepping included in the analysis were performed without hand support, except for one particularly frail patient who required support during stepping and standing.",
   "Moreover, analyses in this study focused on steps that could be reliably detected using force plate measurements and did not include episodes of hastening or true freezing.",
   "It should be recognized that most patients in this study were tremor dominant or exhibited main symptoms of bradykinesia and rigidity, hence, comparisons between patients with and without FOG were not feasible.",
   "Overall, stepping was associated with the highest low-beta band activities and the lowest high-beta activities compared with standing and sitting.",
   "A permutation cluster analysis revealed a significant increase in EMG beta band amplitudes around STN beta burst onset between OFF and ON medication for both the gastrocnemius (P = 0.020; Fig. 5C and the peroneus longus (P = 0.040; Fig. 5D)."
  ],
  "why": "报告的说法有部分依据，但不能作为该研究直接证明冻结期间低beta活动与下肢肌肉共同激活同时出现的证据。原文确实报告了踏步时STN低beta活动高于坐位和站立，并发现STN beta bursts与运动启动时下肢肌肉活动增加有关；引言也提出了肌肉共同激活可能反映异常运动控制的假设。然而，这些结果针对的是踏步及特定步态阶段，而非实际冻结事件。尤其重要的是，作者在Limitations中明确说明分析不包括真正的冻结事件（true freezing），并明确指出无法进行FOG与非FOG患者之间的比较。此外，beta bursts与EMG活动的关系并不等同于已经证实低beta与肌肉共同激活之间存在特定关联。因此，报告引用该研究支持冻结期间这种现象，缺少改变结论的关键限定条件，判定为partly。指控者对原文研究设计、样本、任务、分析内容及局限性的描述均有明确全文依据，判定为yes。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease",
  "pmid": "40512756（报告误引为40635563）",
  "doi": "",
  "report_says": "第三章3.3称，一项14例胆碱能PET研究发现FOG严重程度与多个脑区胆碱能末梢功能降低相关，引用PMID:40635563。",
  "judge_says": "PMID:40635563实际对应Disease-Modifying Trials in Treated Parkinson's Disease: Stable Treated Does Not Equate with Biological Stability，与胆碱能PET研究无关。真正的14例胆碱能PET研究是PMID:40512756，题为Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease。",
  "source": "open_g56.json",
  "pid": "PMID:33240199",
  "report_supported": "partly",
  "judge_supported": "cannot_tell",
  "report_quotes": [
   "Additionally, cholinergic loss in the pedunculopontine nucleus may play a role in FoG, as it stands at the crossroads between supraspinal and spinal gait centers (50).",
   "This review is focused on the electrophysiological findings related to PDFOG+, in which the studies of imaging findings are excluded. However, excellent reviews on imaging technology can be found in recent papers (36, 37, 116).",
   "PET and MRI provide the means to study the loss of brain structure in PDFoG+. These neuroimaging techniques have been extensively utilized to understand the pathophysiological mechanisms of PDFoG+ (36, 37, 116)."
  ],
  "judge_quotes": [
   "This review is focused on the electrophysiological findings related to PDFOG+, in which the studies of imaging findings are excluded.",
   "Additionally, cholinergic loss in the pedunculopontine nucleus may play a role in FoG, as it stands at the crossroads between supraspinal and spinal gait centers (50)."
  ],
  "why": "报告的说法只能获得部分支持。全文确实提到胆碱能功能丧失可能参与FOG，但具体限定为脚桥核（pedunculopontine nucleus），且表述为 may play a role。全文没有报告14例患者的胆碱能PET研究，没有提到FOG严重程度与多个脑区胆碱能末梢功能降低之间的相关性，也没有提供报告所称的具体研究结果。因此，不能将全文对胆碱能功能丧失的一般性描述等同于报告所述的具体PET研究发现。尤其需要注意，作者明确说明本文排除了影像学研究的具体发现。另一方面，指控者关于PMID:40635563对应Disease-Modifying Trials in Treated Parkinson's Disease、而PMID:40512756对应14例胆碱能PET研究的说法，在所提供的全文中均找不到对应的PMID、论文标题或文献题录信息。全文只能证明作者提及了胆碱能功能丧失及影像学研究，不能核实这两个PMID与论文标题之间的对应关系。因此，严格依据全文，指控者的具体文献身份判断应为cannot_tell，而不能判定为yes。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "13例患者随机、双盲、交叉试验的原始研究",
  "pmid": "18420482（报告误引为28529730）",
  "doi": "",
  "report_says": "第四章4.4将PMID:28529730作为一项纳入13例患者的随机、双盲、交叉原始研究引用。",
  "judge_says": "PMID:28529730实际对应2017年的mini-review（二手综述），并非所描述的原始随机交叉试验。对应的原始研究是PMID:18420482。",
  "source": "open_g56.json",
  "verdict": "paper_not_in_kb"
 },
 {
  "paper": "PMID:31494286，STN电生理与冻结易感步态研究",
  "pmid": "31494286",
  "doi": "",
  "report_says": "报告将该研究纳入FOG相关神经活动证据的比较，但没有明确标注其实际研究的是冻结易感状态。",
  "judge_says": "原研究使用躯干加速度计计算iFOG指数，区分冻结易感步态与正常步态，并非直接分析实际冻结事件。其证据应归类为冻结易感性证据，不能直接等同于真实FOG发生期间的神经活动。",
  "source": "open_g56.json",
  "pid": "PMID:31494286",
  "verdict": "no_fulltext"
 },
 {
  "paper": "PMID:37226972，VR冻结与步态减速研究",
  "pmid": "37226972",
  "doi": "",
  "report_says": "报告将该研究纳入FOG相关证据讨论，但没有明确标注其受影响试次的具体行为定义。",
  "judge_says": "原研究将8次VR冻结和7次显著步态减速合并为受影响试次。这些试次并非全部属于实际冻结事件，不能将其结果直接解释为真实FOG期间的神经生理变化。",
  "source": "open_g56.json",
  "pid": "PMID:37226972",
  "report_supported": "cannot_tell",
  "judge_supported": "yes",
  "report_quotes": [
   "Gait freezing is a common, disabling symptom of Parkinson's disease characterized by sudden motor arrest during walking.",
   "Episodes of cognitive cue-associated freezing and VR gait slowing were pooled and compared against segments where VR gait metrics were unaffected by concurrent cognitive processing.",
   "The remaining 15 trials were pooled and classed as cognitive cue-associated VR freezing (n = 8) or significant VR gait slowing where there was >50% FPV reduction (n = 7)."
  ],
  "judge_quotes": [
   "Maintaining validated definitions of VR motor arrests, a “freeze” was defined as any footstep latency >2× a participant's mFSL. Significant VR gait slowing (vs. normal progression) following cognitive cue presentation was pre-defined as >50% reduction in FPV compared to pre-cue footsteps. Episodes of cognitive cue-associated freezing and VR gait slowing were pooled and compared against segments where VR gait metrics were unaffected by concurrent cognitive processing.",
   "The remaining 15 trials were pooled and classed as cognitive cue-associated VR freezing (n = 8) or significant VR gait slowing where there was >50% FPV reduction (n = 7).",
   "Further research is required to explore whether the presently reported reduction in θ frequency activity relates specifically to altered cognitive processing or to freezing itself.",
   "The current study is potentially limited by the surgically mandated supine positioning of the patients, which minimizes any contribution related to anticipatory postural adjustments along with the anxiety of potential falls.",
   "Future work should obtain recordings from implanted DBS systems postoperatively in ambulant patients undergoing concurrent cognitive dual-tasking, which should also guide reconciliation with previous work in LFPs."
  ],
  "why": "report_supported 判为 cannot_tell，是因为附件只有原始论文，没有提供被指控的那份研究报告，因而无法核实报告是否纳入该研究、是否遗漏了具体行为定义。不过，原论文明确给出了受影响试次的操作性定义和构成，不能将原论文描述为没有定义。judge_supported 判为 yes。原文明确说明，15个受影响试次由8次认定为VR freezing的试次和7次显著VR gait slowing试次组成，后者定义为FPV下降超过50%。因此，15个试次并非全部属于冻结事件。进一步地，作者明确指出，尚需研究才能确定θ活动下降究竟特异性关联于认知加工改变还是冻结本身；研究还采用仰卧位VR任务，并提出未来需要在行走状态下进一步研究。因此，指控者认为不能将这组混合试次的神经生理结果直接等同于真实FOG期间特异性的神经生理变化，有全文依据。但需保留一个限定：原文确实将其中8次按操作性标准认定为VR freezing，并非否认这8次冻结事件的存在。",
  "verdict": "cannot_tell"
 },
 {
  "paper": "PMID:36730026，仰卧踏步及freezing-like irregularities研究",
  "pmid": "36730026",
  "doi": "",
  "report_says": "报告将该研究纳入FOG相关证据讨论，但没有明确标注其行为任务与自然直立行走中的真实冻结不同。",
  "judge_says": "原研究采用仰卧踏步任务，以步态振幅下降超过50%定义freezing-like irregularities。这种替代行为不能直接等同于自然直立行走中的真实FOG。",
  "source": "open_g56.json",
  "pid": "PMID:36730026",
  "verdict": "no_fulltext"
 },
 {
  "paper": "Klocke等，转弯任务研究（Research Square预印本）",
  "pmid": "",
  "doi": "10.21203/rs.3.rs-9617843/v1",
  "report_says": "第五章5.3称Klocke等的研究提供了新的转弯任务证据，但没有在正文引用位置明确标示其预印本状态。",
  "judge_says": "该DOI对应Research Square预印本，并非已经完成同行评审的正式期刊论文。报告应明确标注其未经同行评审的出版状态，不能使读者将其与已发表的同行评审原始研究等同看待。",
  "source": "open_g56.json",
  "pid": "DOI:10.21203/rs.3.rs-9617843/v1",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "Here, we report findings from turning motions with and without FoG in PwPD, in whom we previously reported neuronal abnormalities related to FoG occurring during regular walking.",
   "The aim of this study was to characterize the subthalamic signature of freezing while turning.",
   "Our findings advance the pathophysiological understanding of the neural mechanisms underlying freezing while turning"
  ],
  "judge_quotes": [
   "Posted Date: May 6th, 2026",
   "DOI: https://doi.org/10.21203/rs.3.rs-9617843/v1",
   "Research Article",
   "Supplementary material is available at NPJ Parkinson's Disease online."
  ],
  "why": "报告的实质性描述有全文依据。论文明确报告了帕金森病患者转弯及转弯过程中冻结（freezing while turning）的研究，包含实验方法、神经信号分析、运动学结果和分类模型，因此将其描述为提供新的转弯任务证据并无明显误读。但附件只有论文全文，没有报告第五章5.3的正文及其引用位置，因而无法直接核实报告是否确实遗漏了预印本状态标注，整体判为partly。指控者的描述也有部分依据：论文首页列出了Research Square格式的DOI、版本号v1和Posted Date，表明这是一份有明确发布日期和版本信息的在线稿件。不过，全文没有明确出现“preprint”“not peer-reviewed”或“not yet peer-reviewed”等表述，也没有明确声明尚未完成同行评审。另一方面，全文还写有补充材料可在NPJ Parkinson's Disease在线获取。因此，仅凭全文可以支持其具有预印本式发布信息，但不能将其未经同行评审、并非正式期刊论文这一判断视为全文明确证实的事实。两个判断均为partly。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Beaudoin等，2026年STN-LFP与FOG预测研究（bioRxiv预印本）",
  "pmid": "",
  "doi": "10.64898/2026.08.13.744293",
  "report_says": "第五章5.5称Beaudoin等2026年的研究分析了4名患者的STN-LFP数据，并报告AUC=0.825，但正文没有明确标注预印本状态。",
  "judge_says": "该DOI对应bioRxiv预印本，尚未经同行评审。研究只有4名独立患者，患者留一交叉验证不等于独立外部验证，因此AUC=0.825不能直接解释为已经获得稳定的跨患者预测性能。",
  "source": "open_g56.json",
  "pid": "DOI:10.64898/2026.08.13.744293",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "STN local field potential recordings during gait were analyzed from four individuals with Parkinson’s disease from a previously published dataset(16).",
   "Using Shannon entropy alone, the model achieved strong classification performance (AUC = 0.825, accuracy = 0.773), reliably separating pre-freeze from stable turns across patients (Figure 1D).",
   "preprint (which was not certified by peer review)",
   "doi: bioRxiv preprint"
  ],
  "judge_quotes": [
   "preprint (which was not certified by peer review)",
   "STN local field potential recordings during gait were analyzed from four individuals with Parkinson’s disease from a previously published dataset(16).",
   "Predictive performance was assessed using leave-one-patient-out logistic regression and threshold classifiers.",
   "Using Shannon entropy alone, the model achieved strong classification performance (AUC = 0.825, accuracy = 0.773), reliably separating pre-freeze from stable turns across patients (Figure 1D).",
   "Across models, entropy consistently provided the most robust and generalizable discrimination between pre-freeze and stable turns, and additional features did not yield meaningful improvements beyond this single measure."
  ],
  "why": "报告的核心数据有明确依据：论文确实分析了4名帕金森病患者的STN局部场电位数据，并报告基于Shannon entropy的患者留一交叉验证AUC为0.825。但论文明确标注为bioRxiv预印本，并明确注明未经同行评审。因此，如果报告正文确实没有标明预印本状态，则属于遗漏重要文献状态限定，评级为partly，而不是no。指控者的描述同样有部分充分依据：预印本状态、4名受试者和leave-one-patient-out方法均由原文明确记载。论文没有报告独立外部验证队列，因此不能将内部患者留一交叉验证等同于独立外部验证。仅凭4名患者得到的AUC=0.825，也不足以证明稳定、可推广的跨患者预测性能。不过，后两点属于对研究设计和证据强度的合理方法学判断，并非论文明确作出的结论；论文实际上使用了'reliably separating ... across patients'及'robust and generalizable discrimination'等表述。因此，指控者的核心谨慎性判断有依据，但不能说这些限制是论文作者明确承认的结论。另需说明，附件只有论文全文，无法独立核实报告第五章5.5是否确实遗漏了预印本标注。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease",
  "pmid": "40512756",
  "doi": "",
  "report_says": "§4.3将14例胆碱能PET研究引用为PMID:40635563。",
  "judge_says": "PMID:40635563实际对应另一篇文献Disease-Modifying Trials in Treated Parkinson's Disease: Stable Treated Does Not Equate with Biological Stability，并非胆碱能PET研究。该胆碱能PET研究的正确PMID是40512756。",
  "source": "abs_g6.json",
  "pid": "PMID:40512756",
  "verdict": "no_fulltext"
 },
 {
  "paper": "Thenaisie等，2022年，PD患者STN神经活动与步态冻结（FOG）研究",
  "pmid": "36070366",
  "doi": "",
  "report_says": "§5.1称研究纳入4名PD患者，并进一步称该研究样本只有4人。",
  "judge_says": "原研究总体纳入18名患者，其中12名参加步态实验，只有4名在实验中实际发生冻结事件。4人是发生FOG的事件亚组，而不是整个研究的样本量。报告将FOG事件亚组人数描述为研究整体样本量，造成研究规模误解。",
  "source": "abs_g6.json",
  "pid": "PMID:36070366",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "Four participants exhibited frequent episodes of freezing of gait, predominantly whilst turning.",
   "Four patients exhibited episodes of freezing, which differed in their types and severity (duration and frequency of events).",
   "We included 18 patients with PD ( Table S1) who exhibited severe motor fluctuations and varying deficits of gait and balance.",
   "20 patients with Parkinson’s disease were recruited for the study.",
   "Overall, 17 patients were retained for analyses on the neurorobotic platform and 12 for gait experiments."
  ],
  "judge_quotes": [
   "We exploited this platform in 18 patients with Parkinson’s disease, which allowed us to demonstrate that the subthalamic nucleus encodes the initiation, termination, and vigor of leg muscle activation.",
   "20 patients with Parkinson’s disease were recruited for the study.",
   "15 patients performed the walking tasks (small, big and mixed steps).",
   "Overall, 17 patients were retained for analyses on the neurorobotic platform and 12 for gait experiments.",
   "Four participants exhibited frequent episodes of freezing of gait, predominantly whilst turning.",
   "Four patients exhibited episodes of freezing, which differed in their types and severity (duration and frequency of events)."
  ],
  "why": "报告的说法 partly：全文确实明确提到4名患者发生FOG，因此数字4有原文依据。但这4人是FOG事件亚组，并非整个研究的样本量。全文摘要和Results明确报告18名PD患者，Methods则进一步说明研究共招募20人，其中17人保留用于神经机器人平台分析、12人保留用于步态实验分析。将FOG亚组的4人说成整个研究仅有的4名受试者，遗漏了决定研究规模的关键限定，属于样本范围误读。指控者的说法 partly：其核心判断，即4人属于FOG亚组而非整体样本，得到全文明确支持；18人也确实出现在摘要和Results中。不过，指控者对样本流程的表述不够精确：Methods报告实际招募20人，而非18人；15人实际进行了步态任务，12人是最终保留用于步态实验分析的人数。因此，不能将18人、12人和4人简单理解为全文始终一致的三个样本量层级。总体而言，指控者指出报告把FOG亚组误当作整体样本量这一核心问题是有依据的，但其对研究总体招募人数及步态实验参与人数的描述需要补充限定。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Zhang等，2025年，PMC-STN/M1-STN coherence与冻结步态研究",
  "pmid": "41131028",
  "doi": "",
  "report_says": "§5.7认为论文内部部分统计结果与图注的方向报告存在不一致。",
  "judge_says": "原论文定义的百分比变化为(Walk-Turn)/Walk，因此正系数可能表示转弯期相对于行走基线的下降。图注中PMC-STN coherence增加与较短冻结持续时间相关的描述，可能与该归一化方向相容，并不必然构成统计方向矛盾。报告可能没有结合原论文公式及系数符号正确解释统计结果。",
  "source": "abs_g6.json",
  "pid": "PMID:41131028",
  "report_supported": "no",
  "judge_supported": "yes",
  "report_quotes": [
   "The fixed effects were defined as the normalized electrophysiological changes, calculated by:",
   "Percentage Change (%) = (Value_Walk - Value_TurnPre or TurnStart) / Value_Walk × 100",
   "Our analysis revealed that the decreases in the PMC alpha power (β = 0.154, p = 0.035) (Fig. 4A) and increases in PMC-STN alpha coherence (β = 0.205, p = 0.006) (Fig. 4B) during the TurnPre phase, but not the TurnStart phase, significantly predicted the freezing duration within the trial.",
   "Increased PMC-STN alpha coherence during the TurnPre phase (but not during the TurnStart phase) relative to walking predicted shorter freezing episodes (β = 0.205, p = 0.006)."
  ],
  "judge_quotes": [
   "The fixed effects were defined as the normalized electrophysiological changes, calculated by:",
   "Percentage Change (%) = (Value_Walk - Value_TurnPre or TurnStart) / Value_Walk × 100",
   "PMC alpha power reduction during the TurnPre phase (but not during the TurnStart phase) relative to walking positively correlated with freezing duration (β = 0.154, p = 0.035)",
   "Increased PMC-STN alpha coherence during the TurnPre phase (but not during the TurnStart phase) relative to walking predicted shorter freezing episodes (β = 0.205, p = 0.006)."
  ],
  "why": "报告的判断缺乏充分依据，关键问题是没有区分论文中的两种归一化公式。Methods 的 Data normalization and comparison 部分定义了 Normalized Value (%) = Value_Phase / Value_Walk × 100；但在 Statistical analysis 部分，论文明确规定，线性混合效应模型的固定效应使用另一公式，即 Percentage Change (%) = (Value_Walk - Value_TurnPre or TurnStart) / Value_Walk × 100。后一个公式才是解释 β = 0.205 的关键。由于分子方向是 Walk 减 Turn，正系数表示该百分比变化越大，即转弯期 coherence 相对于行走基线越低，预测的冻结持续时间越长。反过来，转弯期 PMC-STN coherence 相对行走基线增加，对应较小或负的百分比变化，因此预测较短的冻结持续时间。这与 Figure 4B 图注的方向完全相容。Figure 4A 中 PMC alpha power 下降与冻结持续时间正相关，也与同一公式及正系数 β = 0.154 相符。此外，Results 正文称 coherence increases predicted freezing duration，但没有明确说是更长还是更短，不能据此认定其与图注矛盾。因此，报告所称的统计方向不一致，实际上忽略了模型自变量的反向百分比编码；指控者的解释有全文依据。",
  "verdict": "accusation_holds"
 },
 {
  "paper": "Beta-burst驱动的自适应DBS研究（预印本与正式发表版本）",
  "pmid": "40677701",
  "doi": "10.1101/2024.06.26.24309418",
  "report_says": "将DOI:10.1101/2024.06.26.24309418和PMID:40677701分别列入参考文献表及证据表，建立两个独立Evidence ID，并同时用于C6和C12的证据支持。",
  "judge_says": "这两个文献记录实际上是同一项beta-burst驱动自适应DBS研究的预印本和正式发表版本，使用同一研究队列，并非两项独立研究。报告没有建立明确的版本关联，若将其作为独立证据计数，会重复计算同一研究，夸大独立研究的数量和重复验证程度。",
  "source": "abs_g6.json",
  "pid": "PMID:40677701",
  "report_supported": "cannot_tell",
  "judge_supported": "cannot_tell",
  "report_quotes": [
   "The goal of the study was to investigate the feasibility, safety and tolerability of beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson’s disease.",
   "Seven individuals with Parkinson’s disease were implanted with the investigational Summit™ RC + S deep brain stimulation system (Medtronic, PLC, Dublin, Ireland)."
  ],
  "judge_quotes": [
   "Seven participants (5 male, 2 female) with clinically established Parkinson’s disease underwent bilateral implantation of DBS leads (model 3389, Medtronic, PLC, Dublin, Ireland) in the sensorimotor region of the STN.",
   "The initial planned cohort was 15 individuals, but recruitment was halted after discontinuation of the Summit™ RC + S in October 2022.",
   "The current pilot study demonstrated initial safety, tolerability, and feasibility of adaptive deep brain stimulation for freezing of gait in Parkinson’s disease in the acute laboratory setting, supporting the future investigation of its longer-term efficacy in the at-home setting."
  ],
  "why": "全文描述的是 PMID:40677701 对一项 beta burst-driven adaptive DBS 研究的正式论文报告，包括研究目的、研究设计及7名参与者的信息。但全文没有提及 DOI:10.1101/2024.06.26.24309418，没有说明该 DOI 对应的预印本，也没有建立预印本与正式发表版本之间的关联。因此，无法根据全文判断报告是否将两个记录分别列入参考文献表和证据表、建立两个独立 Evidence ID，并同时用于 C6 和 C12。报告的具体处理方式不属于论文全文提供的信息。对于指控者，全文虽然明确支持这篇论文报告的是一项包含7名参与者的研究，但没有提供预印本的研究队列、参与者信息或版本关联，因而不能据此确认两个文献记录是否使用同一队列、是否属于同一研究的预印本和正式发表版本。尤其不能仅凭正式论文报告了7名参与者，就推断其与预印本使用相同队列。故两项判断均为 cannot_tell，而不能将缺少版本关联信息直接判定为报告错误，也不能将指控者的描述判定为全文明确支持。",
  "verdict": "cannot_tell"
 },
 {
  "paper": "PMID:42571859，步态周期锁定的皮层低频活动、S1-STN theta coherence及不同刺激条件研究",
  "pmid": "42571859",
  "doi": "",
  "report_says": "在结构化证据关联中将该研究关联至C6（STN beta burst时间结构相关机制）。",
  "judge_says": "原研究主要提供步态周期锁定的皮层低beta活动和皮层-STN theta coherence证据，并研究HFS、LFS对相关活动及冻结的调节，并非直接研究STN beta burst持续时间。该研究可以支持步态相位调制机制，但不宜不加区分地作为STN beta burst机制的直接证据。其与C2（刺激频率）和C8（皮层-STN耦合）也有直接关联。",
  "source": "abs_g6.json",
  "pid": "PMID:42571859",
  "verdict": "no_fulltext"
 },
 {
  "paper": "Syrkin-Nikolau 等，关于步态冻结期间β频段功率变化的原始研究",
  "pmid": "28890315",
  "doi": "",
  "report_says": "实际冻结（实际FOG发作）期间β功率呈上升，与评委引用的原始研究结果相反。",
  "judge_says": "原始研究实际报告的是冻结期间β功率下降。X直接引用了该原始研究，而Y主要通过电生理综述（PMID:33240199）转述了相反的结果。",
  "source": "blind_S2_vs_S3a_aX_g56_9b0417f2",
  "pid": "PMID:28890315",
  "report_supported": "no",
  "judge_supported": "yes",
  "report_quotes": [
   "Among Freezers, beta power was lower during FOG compared to during forward walking without FOG (N = 8 STNs, F(1,51) = 14.45, P < 0.001, Table 4 ).",
   "When Freezers exhibited FOG, beta power was even lower and neural entropy increased in the alpha band."
  ],
  "judge_quotes": [
   "Among Freezers, beta power was lower during FOG compared to during forward walking without FOG (N = 8 STNs, F(1,51) = 14.45, P < 0.001, Table 4 ).",
   "Freezers demonstrated lower beta power and greater alpha SampEn during FOG compared to walking without FOG.",
   "When Freezers exhibited FOG, beta power was even lower and neural entropy increased in the alpha band."
  ],
  "why": "原文明确报告，在Freezers中，实际FOG期间的STN beta功率相对于无FOG的前向行走期间下降（lower），且结论部分进一步强调FOG期间beta功率甚至更低（even lower）。因此，报告所称实际FOG期间beta功率上升，与论文全文直接报告的结果相反，不受全文支持。指控者关于原文报告beta功率下降的描述有明确依据。需要区分功率（power）和样本熵（Sample Entropy）：论文报告FOG期间增加的是alpha SampEn，而不是beta power；不能将神经熵增加解释为beta功率增加。",
  "verdict": "accusation_holds"
 },
 {
  "paper": "14例帕金森病患者胆碱能PET研究",
  "pmid": "40512756",
  "doi": "",
  "report_says": "将这项14例患者的胆碱能PET研究引用为PMID:40635563。",
  "judge_says": "PMID:40635563实际对应的是一篇关于帕金森病疾病修饰试验的综述，并非胆碱能PET研究。该PET研究的正确PMID是40512756。",
  "source": "blind_S2_vs_S3a_aX_g56_9b0417f2",
  "pid": "PMID:40512756",
  "verdict": "no_fulltext"
 },
 {
  "paper": "关于转弯期间神经耦合变化与冻结关系的研究",
  "pmid": "41131028",
  "doi": "",
  "report_says": "认为该研究内部统计结果不一致，存在统计矛盾。",
  "judge_says": "原文区分了正常转弯阶段TurnPre与冻结转弯阶段TurnStart的耦合变化，并报告TurnPre阶段耦合增强与较短的冻结时间相关。这些结果可以通过不同时间阶段的差异解释，不应简单认定为统计矛盾。",
  "source": "blind_S2_vs_S3a_aX_g56_9b0417f2",
  "pid": "PMID:41131028",
  "report_supported": "no",
  "judge_supported": "yes",
  "report_quotes": [
   "Enhanced PMC-STN coherence appeared during TurnPre in normal turning and TurnStart in freezing turning, with TurnPre alpha suppression and coherence predicting freezing duration.",
   "During normal turning, significantly higher PMC-STN alpha coherence was observed in the TurnPre phase (p = 0.0045, Fig. 3A). In contrast, during turning freeze, there was an increase in PMC-STN alpha coherence (p = 0.048) and a decrease in M1-STN alpha coherence (p = 0.043) during the TurnStart phase (Fig. 3B).",
   "Increased PMC-STN alpha coherence during the TurnPre phase (but not during the TurnStart phase) relative to walking predicted shorter freezing episodes (β = 0.205, p = 0.006)."
  ],
  "judge_quotes": [
   "During normal turning, significantly higher PMC-STN alpha coherence was observed in the TurnPre phase (p = 0.0045, Fig. 3A). In contrast, during turning freeze, there was an increase in PMC-STN alpha coherence (p = 0.048) and a decrease in M1-STN alpha coherence (p = 0.043) during the TurnStart phase (Fig. 3B).",
   "Our analysis revealed that the decreases in the PMC alpha power (β = 0.154, p = 0.035) and increases in PMC-STN alpha coherence (β = 0.205, p = 0.006) during the TurnPre phase, but not the TurnStart phase, significantly predicted the freezing duration within the trial.",
   "Increased PMC-STN alpha coherence during the TurnPre phase (but not during the TurnStart phase) relative to walking predicted shorter freezing episodes (β = 0.205, p = 0.006).",
   "The turning process is segmented into four phases: TurnPre (1.5 seconds before turn initiation), TurnStart (the first 1.5 seconds of rotation), TurnEnd (the last 1.5 seconds of stabilization), and TurnPost (1.5 seconds after completing the turn) (Fig. 1C)."
  ],
  "why": "全文明确区分了不同转弯状态和时间阶段的耦合变化：正常转弯时，PMC-STN alpha coherence在TurnPre阶段相对于步行显著增强（p=0.0045）；冻结转弯时，PMC-STN alpha coherence增强发生在TurnStart阶段（p=0.048），同时M1-STN alpha coherence下降（p=0.043）。此外，预测模型发现TurnPre阶段的PMC-STN alpha coherence变化与冻结持续时间显著相关，图4图注进一步明确指出，TurnPre阶段耦合增强预测较短的冻结时间（β=0.205，p=0.006）。这两组结果分别涉及不同的转弯阶段和分析目的，并不构成统计矛盾。还需注意，方法部分将预测变量的百分比变化定义为（Value_Walk−Value_TurnPre或TurnStart）/Value_Walk×100，因此耦合增强对应负向变化值，正的回归系数并不意味着耦合增强会延长冻结时间。综上，指控者对原文的描述有明确全文依据，而仅凭这些结果认定论文存在内部统计矛盾，属于忽略阶段和变量定义后的错误解读。",
  "verdict": "accusation_holds"
 },
 {
  "paper": "14例胆碱能PET研究",
  "pmid": "40512756",
  "doi": "",
  "report_says": "将14例胆碱能PET研究标注为PMID:40635563。",
  "judge_says": "PMID:40635563实际对应一篇疾病修饰试验综述，并非该胆碱能PET研究。该PET研究的正确PMID是40512756。",
  "source": "blind_S2_vs_S3a_aX_g6_9b0417f2",
  "pid": "PMID:40512756",
  "verdict": "no_fulltext"
 },
 {
  "paper": "胆碱能PET研究（Cholinergic PET study）",
  "pmid": "40512756",
  "doi": "",
  "report_says": "报告X将胆碱能PET研究标注为PMID:40635563。",
  "judge_says": "PMID:40635563实际对应一篇疾病修饰治疗综述，并非胆碱能PET研究。胆碱能PET研究的正确PMID为40512756。",
  "source": "blind_S2_vs_S3a_bX_g56_bd01352f",
  "pid": "PMID:40512756",
  "verdict": "no_fulltext"
 }
]

===== bodycheck.json =====
{
 "citations": [
  {
   "cite": "PMID:18413568",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:19811797",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:21777828",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:23039143",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:24937008",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:25540305",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:26887333",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:27766724",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:28119584",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:28529730",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:30100532",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:30153383",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:30196050",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:30262859",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:31275238",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:31505548",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:31647540",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:31755599",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:33240199",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:35310098",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:35418844",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:35431262",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:35441231",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:36070366",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:36242900",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:37701817",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:37860957",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:38101024",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:38948151",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39464215",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40383539",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40496972",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40504072",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40635563",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40648292",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40677701",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40709562",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:40992964",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:41131028",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:41388789",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:41553951",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:41659700",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42098512",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42239677",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42860886",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42909654",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.1101/2025.01.10.632393",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.21203/rs.3.rs-4058858/v1",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.64898/2025.12.17.25342333",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.64898/2026.08.13.744293",
   "verdict": "in_kb"
  }
 ],
 "possible_mismatch": [
  {
   "cite": "PMID:40635563",
   "context": "- 14例胆碱能PET研究提示FOG严重程度与多个脑区胆碱能末梢功能降低相关",
   "own_sim": 0.029,
   "better_match": "PMID:40918851",
   "better_sim": 0.412
  },
  {
   "cite": "PMID:26887333",
   "context": "- 17例步态恶化患者的接触点研究发现，特定背侧、前方及邻近区域刺激与FOG恶化相关",
   "own_sim": 0.282,
   "better_match": "PMID:37701817",
   "better_sim": 0.59
  },
  {
   "cite": "PMID:35310098",
   "context": "| beta增加 | Freezers或实际冻结期间beta功率升高 |",
   "own_sim": 0.321,
   "better_match": "DOI:10.64898/2026.08.13.744293",
   "better_sim": 0.607
  }
 ]
}

===== blind_S2_vs_S3a.json =====
[
 {
  "seat": "aX",
  "judge": "g6",
  "better": "S3a",
  "items": {
   "coverage": "S3a",
   "evidence": "S3a",
   "synthesis": "S3a",
   "structure": "S3a",
   "rigor": "S3a"
  },
  "why": "总体而言，Y更好地完成了研究任务。决定性优势不是篇幅，而是研究过程更加透明、原始研究证据更加具体、研究冲突分析更加深入、知识层级更加明确，并且将机制解释转化为具有预测和反证条件的竞争性假说。尤其是Y不仅提出STN beta可能具有因果作用，也认真考虑运动状态伴随标志、分布式网络失调、区域功能分工及代偿性耦合等替代解释。它还将检索缺陷、数据不一致和未来更新机制纳入研究体系，较好地满足了长期积累与持续改进要求。X并非明显较差：它包含Y遗漏的STN+SNr阳性Meta分析等重要证据，也有成熟的竞争性机制模型和知识更新框架。但X对检索过程、来源可靠性及部分原始研究条件的交代相对不足。最终选择Y，置信度为中高。需要注意，Y仍有21条检索式被截断、327篇待定文献、个别引文错配等问题。它是更好的研究综合报告，而不是已经达到可直接作为完整系统综述发表的证据评价。"
 },
 {
  "seat": "aX",
  "judge": "g56",
  "better": "S3a",
  "items": {
   "coverage": "S3a",
   "evidence": "S2",
   "synthesis": "S3a",
   "structure": "S2",
   "rigor": "S3a"
  },
  "why": "总体上，Y更好地完成了研究任务，但优势属于方法透明度和综合深度上的优势，而不是简单的篇幅或文献数量优势。Y在coverage、synthesis和rigor方面占优，X在evidence的引用准确性及structure的知识分层设计方面占优。两份报告共享相同的结构化证据库，因此真正的区别主要在于如何检索、选择、呈现和解释证据。Y更清楚地展示了研究覆盖的形成过程，更充分整合了冻结前、冻结中及不同步态任务的电生理发现，也更诚实地披露了检索和筛选缺陷。X则具有更成熟的Evidence-Claim-Mechanism-Hypothesis知识管理设计，并在部分关键原始文献引用上更可靠。最终选择Y，但建议将X的四层知识管理架构、证据关系图和假说更新机制整合进Y，同时修正Y的错误文献编号及对个别研究结果的过度解释。这样的整合版本会更接近高质量、可持续更新的功能神经外科研究证据体系。"
 },
 {
  "seat": "bX",
  "judge": "g6",
  "better": "S2",
  "items": {
   "coverage": "tie",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "tie"
  },
  "why": "总体选择Y。理由不是篇幅，而是研究任务的核心在于比较STN神经活动与实际冻结事件之间的证据，并解释相互冲突的实验结果。Y更充分地使用了原始电生理研究、直接冻结与正常转弯比较、不同药物及行为阶段的结果，也更完整地呈现了低频刺激、定向刺激和STN+SNr治疗证据之间的冲突。其四层知识架构和证据更新机制也更清楚。X最突出的优势是检索过程透明、交叉研究方向较广，并且主动检查了自身资料整理中的缺陷，这些方面值得保留。但其检索截断严重，且部分重要原始研究和最新Meta分析没有充分进入正文综合。Y仍然不是完整的系统综述，其机制模型也没有获得因果实验验证；尤其需要进一步解决PMC-STN alpha耦合的解释冲突、两项STN+SNr Meta分析的差异，以及beta活动究竟是冻结的因果驱动还是运动状态伴随标志。综合证据质量、机制综合和知识组织，Y更好地完成了研究任务。"
 },
 {
  "seat": "bX",
  "judge": "g56",
  "better": "S3a",
  "items": {
   "coverage": "tie",
   "evidence": "S3a",
   "synthesis": "S3a",
   "structure": "S2",
   "rigor": "S3a"
  },
  "why": "总体而言，X更好地完成了研究任务。主要优势不是篇幅，而是研究过程的可审计性、事件级电生理证据的细致分析、研究冲突来源的系统拆解，以及竞争性机制假说的可检验性。X尤其擅长区分临床刺激疗效、局部STN神经活动、分布式网络变化和因果机制，避免把治疗效果直接等同于病因验证。Y在知识分层、部分最新DBS临床证据和个别原始研究的引用方面具有优势，但对定向刺激随机研究的关键结果存在误读，削弱了证据可靠性。需要强调，X并非没有明显缺陷：检索截断严重、部分重要临床研究未进入正文综合、胆碱能PET引用错误，以及证据数量尚未完全核对。最合理的评价是：X是更成熟的研究综合与机制假说生成报告，Y则提供了更清晰的知识分类框架和若干值得吸收的最新临床证据。若进一步修订，建议保留X的主体结构和机制分析，吸收Y对定向刺激、低频刺激及STN-SNr研究的补充，并逐项核验原始文献和证据记录。"
 }
]

===== 盲比原文 blind_S2_vs_S3a_aX_g56_9b0417f2（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "Y",
      "why": "Y的研究覆盖略好。其优势不在于引用数量，而在于提供了可审计的主动检索过程：22条检索式、667篇去重记录、82篇纳入、327篇待定，并主动覆盖LFP、单神经元活动、步态启动、转弯、认知负荷、脑干、小脑、动物模型、闭环DBS及阴性研究等交叉方向。Y还讨论了正常步态编码、骑行任务、神经解码和动物模型转化等X正文涉及较少的内容。但Y有明显检索截断：21/22条检索式达到100篇取回上限，327篇仍未完成筛选，因此不能称为全面检索。值得注意的是，两份报告的结构化JSON附录实际上相同，包含相同的150条参考文献及538条证据记录，不能把Y的正文覆盖优势理解为拥有更大的独立文献证据库。另一方面，X主动讨论了Y正文遗漏的2026年阳性STN-SNr Meta分析（PMID:42968793），这是X的覆盖优势。综合判断仍略倾向Y。"
    },
    "evidence": {
      "better": "X",
      "why": "两份报告使用相同的结构化证据库，但X在部分关键争议的原始文献追溯和引用准确性上更好。例如，X直接引用Syrkin-Nikolau等的原始研究（PMID:28890315）说明实际冻结期间beta功率下降，而Y主要通过电生理综述（PMID:33240199）转述这一相反结果。更重要的是，Y将14例胆碱能PET研究错误引用为PMID:40635563，该编号实际对应的是一篇关于帕金森病疾病修饰试验的综述；正确的PET研究编号是PMID:40512756，而X使用了正确编号。这是影响证据可追溯性的实质性错误。外部核对支持这一判断（）。不过，Y对Collomb-Clerc等2025年步态启动研究（PMID:40709562）的正式发表版本、患者数量和实验条件交代得更详细，优于X引用预印本的处理。因此X只是略胜，并非整体证据处理全面优于Y。"
    },
    "synthesis": {
      "better": "Y",
      "why": "Y的跨研究综合更充分地结合了实验条件、行为阶段和神经活动指标。特别是将FOG易感性、冻结前、实际冻结及恢复阶段分开，进一步结合2025年步态启动研究、转弯冻结研究和正常步态编码研究，解释为什么同一频段可能在不同条件下呈现相反方向。Y还更充分讨论了连续步态改善与发作性冻结改善之间的分离，以及PMC-STN和M1-STN连接的阶段特异性。X的九类冲突归纳、低频刺激机制比较及竞争性假说同样优秀，但对部分新研究的行为阶段和具体预测结果整合不如Y。需要指出，Y对PMID:41131028研究内部统计结果不一致的判断略显过度：原文实际上区分了正常转弯TurnPre与冻结转弯TurnStart的耦合变化，并报告TurnPre耦合增强与较短冻结相关，这可以通过时间阶段差异解释，不宜简单认定为统计矛盾（）。"
    },
    "structure": {
      "better": "X",
      "why": "X的长期知识组织结构更清晰。它明确建立Evidence、Claims、Mechanisms、Hypotheses四层体系，将C1-C17作为研究结论、C18-C21作为机制模型、H1-H13作为可检验假说，并通过稳定Evidence ID、证据关系图、假说关联及新证据触发旧结论复核建立知识更新机制。这种设计尤其符合任务要求的原始证据、单项发现、跨研究结论、机制模型和研究假说之间的分层关系。Y也建立了原始文献到证据、单项发现、综合结论和假说的关联链，并有六层研究证据结构，但机制模型与综合结论、假说之间的独立层级不如X明确。X在长期知识积累的可检索性和版本化组织方面略胜。"
    },
    "rigor": {
      "better": "Y",
      "why": "Y在研究过程透明度和自我审查方面明显更好。它明确交代检索数据库、检索日期、检索式数量、筛选结果、全文获取情况、证据提取来源，以及未进行PRISMA预注册和双人独立筛选等限制。更重要的是，它主动披露21条检索式被截断、327篇文献待定，以及539条结构化证据与544条提取记录之间的差异，没有把研究覆盖包装成已经穷尽。X虽然也讨论了小样本、伪重复、预印本和统计报告不一致等问题，并提出质量控制流程，但没有提供同等程度的实际检索及筛选审计记录。此外，Y仍存在错误PMID引用、对部分研究内部矛盾判断过度，以及证据计数与实际JSON附录538条记录未完全对齐等问题。因此Y并非没有质量缺陷，但其方法透明度、局限披露和研究过程可复核性总体优于X。"
    }
  },
  "better": "Y",
  "why": "总体上，Y更好地完成了研究任务，但优势属于方法透明度和综合深度上的优势，而不是简单的篇幅或文献数量优势。Y在coverage、synthesis和rigor方面占优，X在evidence的引用准确性及structure的知识分层设计方面占优。两份报告共享相同的结构化证据库，因此真正的区别主要在于如何检索、选择、呈现和解释证据。Y更清楚地展示了研究覆盖的形成过程，更充分整合了冻结前、冻结中及不同步态任务的电生理发现，也更诚实地披露了检索和筛选缺陷。X则具有更成熟的Evidence-Claim-Mechanism-Hypothesis知识管理设计，并在部分关键原始文献引用上更可靠。最终选择Y，但建议将X的四层知识管理架构、证据关系图和假说更新机制整合进Y，同时修正Y的错误文献编号及对个别研究结果的过度解释。这样的整合版本会更接近高质量、可持续更新的功能神经外科研究证据体系。"
}</escape>

===== 盲比原文 blind_S2_vs_S3a_aX_g6_9b0417f2（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "Y",
      "why": "Y在研究覆盖方面更有可审计性和系统性。它明确报告了22条检索式、43篇主动补充的必读文献、667篇去重后进入筛选的文献，以及82篇纳入、327篇待定和258篇排除的结果。覆盖了临床DBS疗效、刺激频率、解剖定位、STN-LFP、beta burst、神经复杂度、皮层-STN耦合、FOG解码、患者分型、认知运动网络、PPN/MLR、SNr、TBS及动物模型等方向。X也覆盖了大部分重要主题，并且包含Y遗漏的2026年STN+SNr阳性Meta分析（PMID:42968793），因此X在个别交叉方向上有优势。但Y的检索覆盖范围和主动补充过程更透明。需要强调，Y有21/22条检索式达到取回上限，且327篇文献仍待定，不能声称已经穷尽文献。"
    },
    "evidence": {
      "better": "Y",
      "why": "Y对原始研究的证据呈现总体更可靠，尤其是患者数量、实际冻结事件数量、药物和刺激状态、实验任务及统计结果的区分更加具体。例如，Y对Anidi等（2018，PMID:30196050）的描述明确指出5名患者在原地踏步时实际发生FOG，并报告冻结期间beta burst持续时间延长及F(1,815)=13.114、P<0.001。这与原始论文全文相符。X虽然也引用该研究，但对双侧不对称相关分析及是否发生实际冻结的描述不够清楚。Y还较好地区分了同行评审研究、预印本及摘要证据。不过，Y存在可核验的引文错误：其将14例胆碱能PET研究标为PMID:40635563，而该编号实际对应一篇疾病修饰试验综述；正确的PET研究编号是PMID:40512756，X在此处引用正确。Y的部分beta降低证据也依赖综述而非直接原始研究。因此Y只是相对更好，并非没有重要证据追溯问题。"
    },
    "synthesis": {
      "better": "Y",
      "why": "Y更深入地解释了研究结果为什么冲突，而不只是罗列相反发现。它系统区分FOG易感性、冻结前、实际冻结和恢复阶段，进一步分析任务范式、药物状态、刺激状态、STN解剖位置、频段边界、统计指标及重复测量带来的差异。尤其有价值的是指出：相对于正常步行基线的显著性，不能替代冻结转弯与正常转弯之间的直接比较；不同复杂度指标也不能简单合并为神经复杂度升高或降低。Y将这些矛盾进一步转化为H1/H2（beta因果驱动或伴随标志）、H4/H5（PMC-STN alpha代偿或病理性过度耦合）、H9/H10（低频刺激作用于脑干通路或STN局部振荡）等竞争性解释，并给出区分性预测和反证条件。X也有相当完整的机制假说，但Y的研究条件对照、统计学批判及证据与假说之间的连接更充分。"
    },
    "structure": {
      "better": "Y",
      "why": "Y建立了更清晰的多层知识组织结构：临床治疗反应、局部神经活动、时间动力学与网络耦合、解剖及分布式网络、神经解码与治疗控制、因果机制六个层次；同时建立Evidence、Claims、Mechanisms、Hypotheses四层知识关系。它还明确区分全文与摘要来源，设计稳定Evidence ID，记录研究条件、支持或反驳关系、关联假说及后续更新触发条件。X也有Evidence到Claims、Mechanisms和Hypotheses的四层结构，以及知识图谱和版本更新思想，因此两者都达到了较好的知识分层水平。但Y把检索来源、单项研究发现、跨研究结论和机制假说之间的关系交代得更完整，也更便于后续审计和复用。"
    },
    "rigor": {
      "better": "Y",
      "why": "Y在科学严谨性方面优势最明显。它主动声明报告属于结构化叙述性证据综合，而不是PRISMA系统综述或Meta分析，并明确披露没有进行双人独立筛选、没有检索Embase、Scopus、Web of Science和Cochrane，以及21条检索式被截断、327篇文献尚待定等限制。它还指出结构化知识中的539条证据与运行日志中的544条证据存在5条差异，没有擅自解释；明确区分患者数量和冻结事件数量，强调试次数不能代替独立患者数量；讨论机器学习患者内数据泄漏、多重比较、预印本、摘要证据及原始论文内部统计不一致等问题。X也有很好的相关性与因果性区分，并给出反证条件，但没有提供同等程度的检索审计和证据质量控制。需要保留的限制是，Y自身仍存在引文编号错误和部分证据来源不够直接的问题，因此不能将其视为已经完成严格系统综述的成果。"
    }
  },
  "better": "Y",
  "why": "总体而言，Y更好地完成了研究任务。决定性优势不是篇幅，而是研究过程更加透明、原始研究证据更加具体、研究冲突分析更加深入、知识层级更加明确，并且将机制解释转化为具有预测和反证条件的竞争性假说。尤其是Y不仅提出STN beta可能具有因果作用，也认真考虑运动状态伴随标志、分布式网络失调、区域功能分工及代偿性耦合等替代解释。它还将检索缺陷、数据不一致和未来更新机制纳入研究体系，较好地满足了长期积累与持续改进要求。X并非明显较差：它包含Y遗漏的STN+SNr阳性Meta分析等重要证据，也有成熟的竞争性机制模型和知识更新框架。但X对检索过程、来源可靠性及部分原始研究条件的交代相对不足。最终选择Y，置信度为中高。需要注意，Y仍有21条检索式被截断、327篇待定文献、个别引文错配等问题。它是更好的研究综合报告，而不是已经达到可直接作为完整系统综述发表的证据评价。"
}</escape>

===== 盲比原文 blind_S2_vs_S3a_bX_g56_bd01352f（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "tie",
      "why": "X的研究覆盖框架更广，明确检索了22类方向，涉及实际冻结事件、冻结前电生理、beta burst、神经复杂度、皮层-STN耦合、正常步态编码、闭环DBS、动物模型及认知运动网络，并提供检索和筛选记录。Y则补充了若干X正文没有充分讨论的重要临床证据，包括2025年定向STN-DBS随机交叉研究（PMID:39475137）、2026年低频刺激随机试验（PMID:42240331）及STN-SNr联合刺激的阳性Meta分析（PMID:42968793），对DBS临床证据的更新更充分。X的21/22条检索式发生截断，327篇文献仍处于待定状态；Y则完全没有报告可复核的检索流程。两者在覆盖方向上各有优势，难以确定绝对领先者。"
    },
    "evidence": {
      "better": "X",
      "why": "X在单项研究层面提供了更充分的样本量、冻结事件数量、药物和刺激状态、任务条件、信号分析方法及研究局限，尤其对Liu、Thenaisie、Anidi、Pozzi等事件级电生理研究进行了具体分析。X还使用了2025年正式发表的STN步态启动研究（PMID:40709562），而Y主要引用其此前的预印本版本。Y也有值得肯定之处，例如直接引用了Syrkin-Nikolau原始研究（PMID:28890315），并正确使用胆碱能PET研究的PMID:40512756。不过，两份报告均存在引用问题：X将胆碱能PET研究误标为PMID:40635563，该编号实际对应疾病修饰治疗综述；Y则错误解释了Cherif等的定向刺激随机研究，原研究实际发现central STN定向刺激优于posterior STN，FOG事件更少，而不是其正文所述的ring模式优于posterior STN（PMID:39475137）。Y的这一错误直接影响区域功能分工的证据解释。综合原始证据细节、研究条件可追溯性和结论准确性，X略好，但仍需要修正引用错误。"
    },
    "synthesis": {
      "better": "X",
      "why": "X不仅列举研究冲突，还将其系统分解为患者表型、任务范式、冻结阶段、频段定义、信号分析方法、STN解剖位置、侧别、药物和刺激状态、统计单位及二手证据等来源。特别是区分FOG易感状态、冻结前、实际冻结和恢复阶段，并讨论平均beta功率、beta ERD、burst持续时间及burst分布之间的区别。其H1-H13竞争性假说具有较具体的区分性预测、反证条件及实验设计，尤其是H1/H2、H4/H5和H9/H10的机制竞争。Y同样具有较好的冲突分析，例如补充Pozzi研究中冻结转换阶段的低频去耦合，以及Klocke研究中FoG-Turn与Regular Turn的直接低beta比较，但对部分研究之间的统计条件、替代解释及机制之间的交互关系讨论不如X充分。X更好地将观察结果转化为可以被反驳的研究问题。"
    },
    "structure": {
      "better": "Y",
      "why": "Y的知识分层更清晰地对应研究成果的认识论层级：原始证据（Evidence）、研究结论（Claims）、机制模型（Mechanisms）和可检验假说（Hypotheses），并通过具体实例说明从原始观察到因果假说的推导过程。Y还首先区分FOG易感性、事件动力学和治疗可调控性三个不同研究对象，避免不同类型的证据相互替代。X具有更丰富的六层证据结构、C1-C21结论体系和H1-H13假说体系，但其直接证据、跨研究推断、机制模型和假说之间的认识论边界没有Y的四层结构表达得明确。Y在知识组织的清晰度和层级表达方面略占优势。"
    },
    "rigor": {
      "better": "X",
      "why": "X明确说明自身属于结构化叙述性证据综合，而非预注册系统综述或Meta分析，并公开数据库、22条检索式、检索截断、筛选结果、全文获取情况及单模型筛选的局限。它还明确区分主观FOG量表、客观冻结事件、冻结持续时间、步速和平衡，强调患者数量与冻结事件数量不能混淆，并指出不能由DBS治疗有效直接推断内源性STN活动具有因果作用。对统计基线、患者内重复测量、伪重复、多重比较和预印本证据的警惕也比较充分。X还主动发现了539条与544条证据记录之间的不一致，虽然没有进一步解释JSON附录实际538条证据的差异。Y虽然也强调相关性与因果性的区别，提出反证条件和独立队列验证，但没有提供检索、筛选及证据提取过程，且存在定向刺激研究结果解释错误。两份报告的JSON附录实际上均包含150篇参考文献、538条证据、21项结论、13项假说和14项研究缺口；Y正文所称539条证据也与附录不一致。X在主动质量控制和方法学透明度方面更好，但两者均需进一步核对数据版本。"
    }
  },
  "better": "X",
  "why": "总体而言，X更好地完成了研究任务。主要优势不是篇幅，而是研究过程的可审计性、事件级电生理证据的细致分析、研究冲突来源的系统拆解，以及竞争性机制假说的可检验性。X尤其擅长区分临床刺激疗效、局部STN神经活动、分布式网络变化和因果机制，避免把治疗效果直接等同于病因验证。Y在知识分层、部分最新DBS临床证据和个别原始研究的引用方面具有优势，但对定向刺激随机研究的关键结果存在误读，削弱了证据可靠性。需要强调，X并非没有明显缺陷：检索截断严重、部分重要临床研究未进入正文综合、胆碱能PET引用错误，以及证据数量尚未完全核对。最合理的评价是：X是更成熟的研究综合与机制假说生成报告，Y则提供了更清晰的知识分类框架和若干值得吸收的最新临床证据。若进一步修订，建议保留X的主体结构和机制分析，吸收Y对定向刺激、低频刺激及STN-SNr研究的补充，并逐项核验原始文献和证据记录。"
}</escape>

===== 盲比原文 blind_S2_vs_S3a_bX_g6_bd01352f（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "tie",
      "why": "两份报告的结构化附录实际上相同，均包含150条文献记录、538条证据记录、21项结论、13项假说和14项研究缺口，底层证据池没有明显差别。X的优势是明确披露22条检索式、Europe PMC检索、筛选过程，并覆盖动物模型、计算模型、认知负荷、脑干及小脑网络等交叉方向。Y的优势是正文纳入了X没有充分展开的重要研究，包括Su等的低频DBS Meta分析、Cherif等的定向刺激随机试验、Syrkin-Nikolau等的原始电生理研究，以及第二项2026年STN+SNr Meta分析。X存在21/22条检索式达到取回上限、327篇文献尚未完成筛选的问题；Y则缺乏可复核的检索与筛选方法。两者优势互补，难以判定明显胜负。"
    },
    "evidence": {
      "better": "Y",
      "why": "Y对关键原始研究的具体结果、实验条件和患者数量交代得更充分。特别是Syrkin-Nikolau等2017年研究，直接报告Freezers实际冻结期间STN beta功率低于无冻结行走期间，同时alpha Sample Entropy升高，为beta方向冲突提供了重要原始证据。Y还准确呈现Klocke等2026年预印本中FoG-Turn与Regular Turn之间12–15 Hz低beta功率的直接比较（P=0.0274），以及beta burst分布重组；X没有充分呈现这一直接比较。此外，Y纳入了Cherif等10人随机交叉定向刺激研究，并对STN+SNr干预的不同Meta分析进行了并列引用。上述证据可以分别核对原始研究，而不只是依赖综述转述。【turn134023search0】【turn596444search1】【turn737537search2】Y仍有改进空间，例如2025年步态启动研究正文使用了预印本DOI，而非优先引用最终发表的Annals of Neurology论文。"
    },
    "synthesis": {
      "better": "Y",
      "why": "Y对关键冲突的整合更贴近具体实验结果。它不仅区分冻结易感、冻结前、实际冻结和恢复，还将beta功率降低与升高、beta burst重组、theta阶段变化以及不同皮层区域的alpha耦合变化放在具体任务和行为阶段中比较。尤其是STN+SNr证据，Y同时呈现了2026年一项报告额外获益的Meta分析和另一项未发现额外获益的Meta分析，使治疗证据的冲突更加完整。【turn667649search1】【turn667649search8】Y提出的H1–H13具有竞争性预测和反证条件，并将低频刺激的PPN/MLR通路机制与STN局部振荡机制区分开来。X的冲突分析和机制假说同样丰富，但遗漏了上述部分关键结果，降低了其跨研究综合的完整性。需要指出，Y也没有充分讨论两项STN+SNr Meta分析可能存在的原始试验重叠，因此尚未彻底解释其结果差异。"
    },
    "structure": {
      "better": "Y",
      "why": "Y的知识分层更清楚地划分为四层：原始证据、研究结论、机制模型、可检验假说。尤其明确区分C1–C17的经验性结论、C18–C21的机制模型和H1–H13的竞争性假说，避免把机制解释误当成实验结论。它还设计了稳定Evidence ID、证据关系图、结论版本保留、新证据触发旧结论复核及质量控制指标。X也建立了较完善的证据—结论—假说关联体系，并提供更详细的证据登记字段，但正文将C1–C21整体称为结构化结论，经验发现与机制模型的边界不如Y明确。Y在长期知识积累和新证据更新方面的设计也更具有可操作性。"
    },
    "rigor": {
      "better": "tie",
      "why": "X的优势在于检索方法透明，明确说明仅使用Europe PMC、没有PRISMA预注册和双人独立筛选、21/22条检索式发生截断、327篇文献尚未完成筛选，并主动披露证据计数不一致。X还注意到2025年PMC-STN alpha研究正文与图注对冻结持续时间预测方向存在不一致，体现了对原始论文内部报告质量的审查。【turn254970view0】Y的优势在于更加具体地区分原始观察、二手引用、患者数量与冻结事件数量，并较好地区分相关性、时间先后关系和因果机制。其不足是没有交代实际检索与筛选流程，也没有充分指出上述PMC-STN论文的内部报告矛盾。另一个共同的数据质量问题是，两份报告正文均出现539条证据的表述，而实际结构化JSON附录只有538条；X虽然披露了539与544之间的差异，但也没有完全解决这一问题。X的检索透明度与Y的原始证据判读准确性各有优势，综合而言难分高下。"
    }
  },
  "better": "Y",
  "why": "总体选择Y。理由不是篇幅，而是研究任务的核心在于比较STN神经活动与实际冻结事件之间的证据，并解释相互冲突的实验结果。Y更充分地使用了原始电生理研究、直接冻结与正常转弯比较、不同药物及行为阶段的结果，也更完整地呈现了低频刺激、定向刺激和STN+SNr治疗证据之间的冲突。其四层知识架构和证据更新机制也更清楚。X最突出的优势是检索过程透明、交叉研究方向较广，并且主动检查了自身资料整理中的缺陷，这些方面值得保留。但其检索截断严重，且部分重要原始研究和最新Meta分析没有充分进入正文综合。Y仍然不是完整的系统综述，其机制模型也没有获得因果实验验证；尤其需要进一步解决PMC-STN alpha耦合的解释冲突、两项STN+SNr Meta分析的差异，以及beta活动究竟是冻结的因果驱动还是运动状态伴随标志。综合证据质量、机制综合和知识组织，Y更好地完成了研究任务。"
}</escape>