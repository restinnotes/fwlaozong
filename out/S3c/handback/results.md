===== open_g6.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "研究覆盖缺少可审计的系统检索过程，无法证明文献覆盖具有完整性。",
   "where": "第七节提出“重要独立队列的覆盖率”“证据与原始文献之间的可追溯性”等评价指标；第1364行又明确说明：“本报告仅依据本次提供的结构化结论、假说、证据表及其文献编号进行综合，没有引入外部文献或新增实验数据。”附录虽然提供15组检索式，但没有给出实际数据库检索记录。",
   "why": "这是整个报告最根本的问题之一。用户要求主动寻找相关研究和交叉方向，但报告没有交代实际检索过哪些数据库、使用什么检索日期和检索式、是否检索引文及参考文献、如何处理预印本和正式发表版本、纳入排除标准是什么、筛选了多少篇以及排除原因。附录中的检索式只是未来检索建议，不能证明检索已经执行。尤其是报告覆盖了STN电生理、DBS、皮层网络、脑干、感觉运动整合、机器学习和动物研究，却没有说明这些领域如何被系统发现和筛选。最后的范围声明实际上承认报告是基于已有结构化材料进行二次综合，而不是独立完成的文献覆盖工作。因此，报告无法排除遗漏了会改变核心判断的重要研究，也无法让第三方复现其证据全景。",
   "severity": "major",
   "fix": "增加独立的文献检索与筛选方法章节。明确PubMed、Embase、Web of Science、Scopus、Cochrane及预印本数据库的实际使用情况、最后检索日期、完整检索式、语言和年份限制、纳入排除标准、双人筛选流程及争议解决方法。报告PRISMA流程和排除理由。对交叉方向分别建立检索模块，并将实际检索结果与尚待执行的检索建议明确分开。不能把结构化资料库中已有的文献数量当作领域覆盖率。"
  },
  {
   "rank": 2,
   "what": "证据分级体系把证据直接性、研究设计质量和因果推断能力混为一谈，且全文核查比例不足。",
   "where": "第1.2节：“A级：直接事件证据”“B级：事件关联或易感性证据”“C级：间接干预或网络证据”。附录 references 和 evidence 中的 basis 字段记录了文献依据类型。",
   "why": "A/B/C实际上描述的是证据与目标问题的接近程度，而不是研究质量或结论可信度。一个只有4名患者、173次事件的观察性研究可以被归为A级，而随机对照干预研究被归为C级。这并不意味着前者的证据确定性高于后者。报告没有建立独立的偏倚风险和证据确定性评价体系。我检查了结构化附录：233条参考文献中，171条只有摘要级证据，只有62条有全文级证据；933条证据记录中有346条来自摘要，另有246条记录没有提供样本量字段。尤其是一些关键研究的完整方法、事件判定、统计模型和效应量并没有被充分提取。例如，2024年Klocke研究的全文实际上报告了12名患者、5名发生冻结的患者、42次冻结事件、75个Pre-FoG步态周期，以及8–12 Hz的STN-肌肉相干性结果；报告却称样本量、频段和时间窗口信息有限。 这使得报告虽然有大量结构化证据记录，却不能保证关键结论已经过原始全文核查。",
   "severity": "major",
   "fix": "将证据评价拆成至少两个独立维度：第一，证据直接性（实际冻结、冻结易感性、间接网络或治疗证据）；第二，证据可信度（偏倚风险、样本量、统计独立性、精确度、重复验证和外推能力）。采用适合研究设计的RoB 2、ROBINS-I等工具，并对临床结局使用GRADE。明确区分摘要核查和全文核查。对关键研究必须提取患者数、事件数、任务、药物及刺激状态、事件判定方法、效应量、置信区间、统计模型和具体图表位置。不能用直接事件证据的标签替代质量评价。"
  },
  {
   "rank": 3,
   "what": "2017年Freezer与Non-Freezer的beta冲突表存在明确的文献归属和实验任务错误。",
   "where": "第2.2节表格：“Storzer等，2017 | SIP无冻结 | Freezer的相对beta功率较低”。该节随后引用：“PMID:24361601; PMID:28892573; PMID:30196050”。",
   "why": "PMID:28892573对应Storzer等人的研究，题为Bicycling suppresses abnormal beta synchrony in Parkinson's disease，研究的是步行和骑车，而不是SIP。该研究报告的一个重要结果是Freezer在运动期间出现约18 Hz的窄带活动增强，并非报告所述的SIP中相对beta功率降低。相对beta降低的研究实际上是Syrkin-Nikolau等人的2017年研究，PMID:28890315，题为Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease。两篇论文的研究任务、测量指标和发现不能互换。 附录中28892573甚至没有对应的独立evidence记录，而28890315有多条记录。这不是简单的作者姓名笔误，而是影响beta冲突分析的证据归属错误。报告因此没有准确区分不同研究中的窄带18 Hz活动、宽频beta功率和beta复杂度。",
   "severity": "major",
   "fix": "重新核对2017年相关原始论文。将Storzer和Syrkin-Nikolau作为两项独立研究处理，分别记录任务、患者数、频段、相对功率、绝对功率、复杂度指标及是否存在实际冻结。重新建立2.2节的证据表，并检查表格中的每个发现是否确实对应其所列PMID。对于每个beta结果，必须同时标明测量对象和比较条件，不能只用Freezer beta升高或降低概括。"
  },
  {
   "rank": 4,
   "what": "关键的原始电生理证据和2026年新发表的直接相关研究没有进入正文的实质性综合，导致证据全景存在重要缺口。",
   "where": "第2.1节称自然行走实际冻结是最重要的直接人体证据；摘要第15行提及MUA，但第2.1节没有独立讨论STN多单位活动研究。第2.6节的非beta指标也没有充分整合相关研究。附录中却存在PMID:31665229、PMID:31494286和PMID:42236313等文献。",
   "why": "至少有以下几类重要证据没有得到应有的分析。第一，2019年Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing，PMID:31665229，利用虚拟现实任务和STN微电极记录研究冻结相关的神经活动，涉及MUA及beta/theta活动与肌肉运动异常之间的时间关系。这与慢性LFP记录属于不同测量层次，不能因为不是自然步行记录就从证据综合中消失。 第二，2019年PMID:31494286研究的是冻结易感步态，报告15–21 Hz低beta和5–8 Hz theta活动与易冻结步态相关。它不是实际冻结事件证据，但恰好是重要的易感性证据，应该纳入B级比较。 第三，2026年Klocke等的Cognitive and Emotional Determinants of Subthalamic Oscillations During Freezing While Turning，PMID:42236313，研究13名患者，发现冻结转弯期间theta功率与焦虑程度正相关、与MoCA评分负相关，而alpha和beta没有相同关联。这是直接影响H3、H5及认知情感机制解释的新证据，正文却没有讨论。 第四，2024年Klocke研究全文已经提供了详细的患者数、冻结事件数、冻结前步态周期及alpha相干性分析，报告却将其描述为定量信息有限。以上缺口共同影响了对beta、theta、MUA、网络协调及认知情感机制的综合判断。",
   "severity": "major",
   "fix": "建立一张独立的关键原始证据覆盖表，至少分为自然冻结LFP、实际冻结MUA、虚拟现实诱发冻结、冻结易感性、冻结前步态异常、认知负荷和认知情感调节。明确区分实际冻结与iFOG易感指标，不能混用。将PMID:31665229、31494286和42236313纳入正文，逐项说明其支持或反对哪些结论。对2024年Klocke研究重新提取完整统计结果，明确它研究的是直线行走中发生的冻结，而不是特定的转弯诱发冻结。"
  },
  {
   "rank": 5,
   "what": "预印本与正式发表版本、同一患者队列的不同分析没有被可靠地去重，独立证据数量存在被高估的风险。",
   "where": "第3.6节：“2025年预印本与正式发表版本可能属于同一研究”。附录references中同时存在多组DOI预印本和正式发表的PMID条目。",
   "why": "这里不应仅仅写成可能。至少存在明确需要建立版本关联的研究：Collomb-Clerc研究的2025年预印本DOI:10.1101/2025.01.10.632393与正式论文PMID:40709562；Garulli研究的2025年预印本DOI:10.1101/2025.04.22.650006与2026年正式论文PMID:41654501；beta burst驱动aDBS研究的预印本DOI:10.1101/2024.06.26.24309418与正式论文PMID:40677701。这些不是三组独立实验重复，而是同一研究的不同版本。 此外，2026年Klocke的转弯冻结预印本与PMID:42236313的认知情感分析具有相同的13名患者及相同的患者编号，属于同一队列的相关分析，而不是独立患者队列重复验证。 报告没有系统建立这些关联。结果是参考文献数量、证据条目数量和独立研究数量之间缺少可靠对应关系。",
   "severity": "major",
   "fix": "建立Study ID、Cohort ID和Version ID三层标识。每篇研究应记录原始队列、患者编号或可核查的队列特征、招募中心、招募时间、预印本版本、正式发表版本及后续二次分析。正式论文替代预印本作为主要引用版本，但保留版本历史。不同论文使用相同患者时，应标注为同一队列的不同分析，不得作为独立重复验证。重新计算独立患者数、独立队列数和独立实验数。"
  },
  {
   "rank": 6,
   "what": "2026年Klocke预印本的患者样本数和冻结前时间窗口存在实质性误读，影响对冻结前预测证据的解释。",
   "where": "第2.1节：“13名PD患者；11名具有有效神经记录；122个含冻结的转弯；224个正常转弯。”同节表格：“Pre-FoG-Turn vs Pre-Reg-Turn | 低beta差异经多重比较校正后不显著”。",
   "why": "原文明确报告13名患者接受STN-LFP记录，其中一名患者的一侧电极因定位问题被排除。122个含冻结的转弯来自11名发生冻结转弯的患者，224个正常转弯来自13名患者。因此，11是出现FoG-Turn的患者数，不是具有有效神经记录的患者数。 更重要的是，论文定义的Pre-FoG-Turn是转弯开始前3秒的时间窗口，而不是实际冻结发生前3秒。原文还报告Pre-FoG-Turn相对于Standing缺乏低beta去同步化，而Pre-Reg-Turn存在相应去同步化；两个Pre-Turn状态直接比较时则没有显著差异。报告只突出后一个阴性比较，却没有充分说明前两个比较的意义。这样容易让读者误认为该研究已经否定冻结发生前的STN beta异常，而实际上它主要检验的是冻结转弯之前的转弯准备状态，并非冻结发生前最后几步的神经活动。此外，这是一篇2026年5月发布的Research Square预印本，应明确标注其尚未经正式同行评审。",
   "severity": "major",
   "fix": "重新核对原文Methods、Results及补充材料。将患者数分别记录为招募患者、有效LFP患者、发生FoG-Turn患者及有效半球数。严格区分Pre-Turn、Pre-FoG和FoG onset三个时间定义。完整呈现Pre-FoG-Turn与Standing、Pre-Reg-Turn之间的全部比较，并补充短时长burst分布结果。将该研究的结论限定为转弯准备阶段和冻结转弯相关的状态变化，不得据此判断冻结发生前最后几步是否存在预测性异常。"
  },
  {
   "rank": 7,
   "what": "H12关于beta burst驱动aDBS的核心判断没有充分整合已经发表的直接对照实验，导致研究空白描述过时。",
   "where": "第4.2节H12：“目前aDBS研究尚未真正区分beta特异性反馈与动态刺激时序效应。”第5.4节又将beta burst触发、随机触发、周期触发和运动学触发作为未来首次需要比较的策略。",
   "why": "2025年已经发表了Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease，PMID:40677701。该研究纳入7名患者，在双盲条件下比较了beta burst驱动aDBS、连续DBS和随机自适应刺激。三种开启刺激条件均能相较OFF改善冻结时间比例，而开启条件之间没有显著差异。转弯和障碍物任务中实际出现冻结的患者只有3名，因此这项研究远不足以证明beta信号没有特异性价值，但它已经直接开展了报告所说的关键比较。 因此，报告将其描述为尚未真正开展的研究问题是不准确的。更重要的是，这项研究的结果本身恰好是H12最需要讨论的证据：动态刺激可能有益，但beta反馈是否具有额外优势仍未确定。",
   "severity": "major",
   "fix": "将PMID:40677701作为正式发表的核心干预证据纳入正文，而不是主要依赖其预印本。具体讨论7人样本、实际冻结事件数量、随机自适应刺激的剂量匹配方式、急性实验条件和未发现组间优势的结果。将研究问题改为：在已有小样本随机控制结果基础上，能否通过更大样本、长期自由活动和自然FOG终点验证beta反馈是否具有额外收益。"
  },
  {
   "rank": 8,
   "what": "STN-SNr联合刺激部分存在原始试验样本数错误和关键一手文献引用缺失。",
   "where": "第2.8节表格：“急性双盲研究 | 10名患者中未发现明确额外优势。”该表之后的引用为：“PMID:35490252; PMID:37104542; PMID:42860886; PMID:42909654; PMID:42968793。”",
   "why": "与该描述对应的急性随机交叉试验PMID:39957196报告有15名患者至少接受过一种联合刺激，并未发现STN-SNr联合刺激在NFOG-Q上相较STN-only具有统计学显著优势，而不是报告中的10名患者。 长期交叉研究PMID:40760816则是24名患者入组、20名完成，联合刺激相较STN-only的FOG-Q改善差异为4.7分。 但是正文引用列表中的PMID:35490252是综述，PMID:37104542是计算模型研究，而不是这两项临床试验的原始论文。关键临床证据的样本数和引用链均存在问题。对于一个用于解释DBS治疗冲突的核心部分，这会直接影响结论的可信度。",
   "severity": "major",
   "fix": "重新核对STN-SNr部分所有临床研究的原始全文，明确入组人数、完成人数、实际接受各刺激条件的人数、随访时长及主要结局。分别引用PMID:39957196和PMID:40760816。对20名完成者的研究报告4.7分效应量及95%置信区间；对15名急性试验参与者报告NFOG-Q阴性结果和个体应答情况。综述和计算模型只能作为补充解释，不能替代原始试验引用。"
  },
  {
   "rank": 9,
   "what": "拟议的统计与因果实验设计可能对运动学中介变量进行过度调整，无法可靠区分原因、反馈和结果。",
   "where": "第4.1节H1、H4、第5.2节：“控制步速、步长、步频、转弯角度及任务负荷后”；第5.3节：“控制X1后，X2和X3是否仍具有独立解释力？”第5.4节建议等剂量比较不同触发策略。",
   "why": "步速、步长、步频、EMG及步态周期异常可能是STN异常影响运动输出的中介变量，而不一定是外部混杂因素。如果真实因果路径是STN异常导致步态运动学改变，继而导致冻结，那么直接控制这些变量可能阻断真正的病理通路，造成过度调整。某些变量还可能是多个病理过程的共同结果，条件化处理会引入碰撞变量偏倚。与此同时，beta触发DBS并不等于选择性操控beta神经机制；刺激会同时影响其他局部和网络活动。即使beta触发优于随机刺激，也仍需证明beta变化是治疗效应的中介，而不是预测性控制变量。报告虽然反复强调因果性尚未验证，但实验设计还没有充分解决这个问题。",
   "severity": "major",
   "fix": "在提出统计模型前，明确绘制因果DAG，分别定义外部混杂因素、患者级调节因素、潜在中介变量和行为结局。分别估计不调整中介变量的总效应，以及适当定义的直接效应。不能把所有运动学变量统一作为协变量。对于神经调控，必须同时报告目标信号是否被实际改变、改变是否先于行为改善、行为改善是否被该信号变化中介，以及其他网络活动是否同步改变。预测模型的独立解释力不能直接等同于因果机制。"
  },
  {
   "rank": 10,
   "what": "H1–H14并不全部构成真正可竞争的机制模型，而是混合了病理机制、调节因素、混杂解释和治疗策略。",
   "where": "第4.1节：“它们并不要求在所有患者中互斥；真正需要竞争的是哪一种机制能够解释特定患者、特定事件和特定治疗反应。”随后提出H1–H14。",
   "why": "这一声明实际上暴露了模型分类的问题。H1局部beta burst机制和H2皮层-STN协调机制可以同时成立；H6易感性与瞬时触发双层机制甚至可以包含H1和H2。H9患者亚型属于调节因素，H10结构连接属于易感性或治疗效应修饰因素，H12是闭环控制策略，H13是慢性治疗适应机制，H14是细胞投射层面的机制。它们并不处在同一个因果层次，也不是对同一个现象的相互排斥解释。H4更接近非特异性任务效应或替代解释，H5则包含三个不同子模型。现有优先级表无法告诉读者究竟哪些模型是在解释同一个神经变化，哪些是在解释患者间差异，哪些是在解释治疗反应。虽然每个假说都有预测和反证条件，但缺少真正的头对头模型比较框架。",
   "severity": "moderate",
   "fix": "将假说重新分层。第一层为近端驱动机制：局部beta、跨区域通信、感觉反馈、动作选择及分布式网络驱动。第二层为调节因素：患者亚型、药物状态、结构连接、刺激位置。第三层为结果或补偿机制：复杂度、运动努力、恢复反应。第四层为治疗机制：aDBS时序、STN-SNr输出和慢性可塑性。只在同一因果层次内建立真正竞争的模型，并对同一患者、同一事件预先定义不同的时间顺序、独立预测和反证条件。采用外部验证及模型比较，而不是仅列出各自的支持文献。"
  },
  {
   "rank": 11,
   "what": "STN-SNr两项2026年Meta分析之间的冲突被识别出来，但没有完成足够深入的方法学裁决。",
   "where": "第2.8节：“一项分析未发现一致额外获益……另一项Meta分析报告联合刺激具有统计学显著改善。”随后解释：“纳入研究、效应量及配对数据处理不同。”",
   "why": "这只是指出了差异，没有解释差异如何改变结论。PMID:42909654纳入10项研究、109名独立可评价患者，冻结结局涉及86名患者，Hedges g为-0.23，95%CI为-1.04至0.59，I²为85.6%，证据确定性为极低。该分析明确考虑配对数据和研究内依赖。另一项PMID:42968793纳入8项交叉随机试验、97名患者，报告SMD为-0.39，95%CI为-0.73至-0.04，I²为23.2%。但其作者指出，由于原始交叉试验缺乏配对汇总数据，合并时采用了平行组近似方法；部分研究还提供了多个数据集。 这意味着两项Meta分析的统计独立性假设和方差处理方式存在实质差异，不能简单理解为两组同等可信的研究得出了不同结论。报告没有展示纳入试验的逐项重叠情况、重复数据集处理和风险偏倚评价，也没有说明哪一项分析的统计处理更适合交叉设计。",
   "severity": "moderate",
   "fix": "增加专门的Meta分析方法学比较表。逐项列出纳入的原始试验、患者数、重复数据集、交叉设计配对数据处理、效应量、置信区间、异质性、偏倚风险和GRADE等级。重点检验平行组近似是否改变效应估计及置信区间。对重叠试验进行去重，并明确区分统计学显著性、临床重要性和证据确定性。"
  },
  {
   "rank": 12,
   "what": "结构化附录中C结论与H假说之间存在编号错配，破坏了知识索引的可靠性。",
   "where": "附录claims中：C29写“机制模型H9：低频STN-DBS及STN+SNr输出通路”；C31写“机制模型H11：自适应DBS的优势可能来自动态刺激时序”；C32写“机制模型H12：STN不同输出投射可能具有不同的FOG相关功能”。但正文第4节中，低频STN-DBS及STN-SNr对应H11，动态刺激时序对应H12，投射特异性机制对应H14。",
   "why": "这不是单纯的编号格式问题。报告第七节明确将C1–C33作为长期稳定的知识索引，并要求新证据匹配既有结论、假说及其关系。如果C29、C31、C32的假说编号与正文不一致，后续检索和自动更新就可能将新证据关联到错误机制。例如，关于STN-SNr输出通路的新研究可能被错误关联到H9患者亚型，而不是H11。H14投射特异性机制也可能被错误更新到H12闭环刺激策略。这会直接破坏报告希望建立的证据—结论—假说映射关系。",
   "severity": "moderate",
   "fix": "建立唯一的假说ID和独立的显示编号，不允许在正文和附录中分别手工维护编号。为每条claim设置明确的hypothesis_id，并通过自动校验检查引用是否存在、编号是否一致、关联方向是否正确。重新检查C29–C33以及全部H1–H14的映射关系。"
  },
  {
   "rank": 13,
   "what": "长期知识积累和持续自主改进目前仍停留在设计建议层面，尚未形成可验证的实际工作机制。",
   "where": "第七节反复使用：“建议建立标准化原始证据登记表”“建议采用以下规则”“建议定期评价”。第1265–1277行提出改进评价指标，但没有提供任何实际改进案例或验证结果。",
   "why": "报告提出了一个合理的知识管理方向，但没有证明这个系统已经能够运行。没有展示一次完整的闭环：发现旧结论或证据记录存在缺陷、定位具体原因、修改证据或模型、重新计算结论、通过独立检查验证修改是否有效。附录的references主要包含ref、PMID、DOI、title和year，缺少标准化作者、期刊、发表状态、版本关系、队列ID和原文位置。evidence中的样本量也没有充分规范化。现有结构难以可靠支持自动识别同一队列、自动发现预印本重复、追踪结论版本变化及重新评价证据强度。因此，第七节实际上是一个知识库建设方案，而不是已经具备长期积累和自主改进能力的证明。",
   "severity": "moderate",
   "fix": "将知识管理方案转化为可运行的证据数据库和版本管理流程。为每项研究建立规范化元数据、队列标识、来源位置、证据提取日期和发表状态；为每条结论保存支持证据、反对证据、适用范围、历史版本及修改原因。建立实际的更新测试集，定期测试文献召回率、重复队列识别准确率、原文证据定位准确率和结论更新准确率。至少提供一个完整的历史案例，展示发现错误、核查原因、实施修正以及独立验证修正有效性的全过程。"
  }
 ],
 "overall": "这份报告有一个值得保留的科学核心：没有把STN beta升高简单等同于FOG，也意识到了患者间易感性、患者内事件变化、皮层-STN协调和DBS干预之间的区别。但它目前最严重的问题在于证据底座尚不够可靠和可审计，而不只是某几个机制假说尚未得到验证。文献检索过程不可复现，部分关键原始研究存在遗漏或错误归属，预印本和正式论文及重复队列没有充分去重，个别关键研究的患者数和时间窗口还出现误读，已经发表的aDBS对照实验也没有被正确整合。这些问题会直接影响报告对beta冲突、冻结前信号及闭环DBS因果机制的判断。此外，H1–H14更像不同因果层次的研究议程，而不是已经构造完成的竞争性机制模型；知识库和自主改进部分也主要是未来规划。我的总体判断是：报告的中心结论具有合理性，机制讨论也有价值，但目前不能把它视为一份已经完成充分文献核查、独立队列去重和严格因果证据评价的完整研究综合。最需要优先修复的是检索与证据来源、关键原始研究的归属和覆盖、队列版本去重，以及冻结事件时间窗口的准确性。"
}

===== open_g56.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "文献覆盖没有可复现的检索依据，无法证明报告真正完成了主动、系统的研究搜索。这是整个证据综合最根本的问题。",
   "where": "第1节和第2节没有交代数据库、检索式、检索日期、关键词组合、纳入与排除标准、筛选流程或参考文献追溯方法。尤其是报告最后明确写道：“本报告仅依据本次提供的结构化结论、假说、证据表及其文献编号进行综合，没有引入外部文献或新增实验数据。”",
   "why": "参考文献有233条，不等于覆盖了该领域的全部重要证据。读者无法判断这些文献是通过主动检索获得，还是从已有材料中挑选；也无法判断哪些方向搜索过但没有找到研究，哪些研究因为筛选标准被排除。对于一个要求主动发现交叉方向、减少重要证据遗漏的报告，这尤其严重。还无法排除检索偏倚：如果原始材料本身偏重beta和DBS，那么后续综合即使写得非常完整，也可能继承原有的证据盲区。报告的证据截止日期为2026年11月13日，却没有说明如何保证这一日期之前的新发表研究均被检索。",
   "severity": "major",
   "fix": "增加独立的检索方法章节，至少报告PubMed、Embase、Web of Science及相关预印本平台的检索范围、完整检索式、最后检索日期、纳排标准、筛选数量和排除理由。分别检索STN-LFP、MUA、微电极记录、自然FOG、虚拟步态、STN-DBS、皮层-基底节连接、脑干运动区、感觉运动整合及闭环刺激。提供PRISMA式筛选记录和补充检索日志。明确区分已经完成的系统检索与尚未覆盖的研究方向。"
  },
  {
   "rank": 2,
   "what": "证据数据库没有真正解决研究版本、研究队列和独立患者样本的去重问题。论文数量、证据记录数量和独立实验数量之间缺乏可靠映射。",
   "where": "第3.6节承认“2025年预印本与正式发表版本可能属于同一研究”，也承认“2026年部分burst及熵分析重新使用2022年数据”。但是结构化附录的references和evidence仍分别保存了多个版本。例如：DOI:10.1101/2025.01.10.632393与PMID:40709562；DOI:10.1101/2025.04.22.650006与PMID:41654501；DOI:10.1101/2024.06.26.24309418与PMID:40677701。另有Klocke等的2026年转弯冻结预印本DOI:10.21203/rs.3.rs-9617843/v1，以及PMID:42236313对应的2026年论文。",
   "why": "这些记录并不都代表独立研究。Collomb-Clerc和Garulli的预印本与正式论文分别对应同一研究的不同发表版本。更重要的是，Klocke的转弯冻结预印本和2026年认知情绪研究使用相同的13名受试者及相同的患者编号，属于同一队列的不同分析，而不是两次独立患者重复验证。【turn302347view0】【turn623213search3】报告虽然提到了队列重叠风险，却没有在数据库中建立可查询的队列关系。这样一来，同一数据集可能通过不同论文、预印本和二次分析多次进入结论及假说的支持链，夸大证据独立性，也会让后续自动更新错误地把再分析当成新重复验证。",
   "severity": "major",
   "fix": "建立独立于文献编号的Study ID、Cohort ID、Dataset ID和Version ID。每篇论文必须关联其实际患者队列、采集时间、研究中心及数据集。为预印本、正式发表版本、二次分析和重复发表建立明确的版本关系。合并统计时以独立队列和独立实验为单位，而不是以论文数量或evidence记录数量为单位。对于同一队列的不同分析，允许形成不同证据，但必须明确标记其不构成独立重复验证。"
  },
  {
   "rank": 3,
   "what": "主文对重要人体电生理和交叉方向证据的整合明显不充分。附录收录了相关研究，但没有把它们真正纳入核心机制比较。",
   "where": "第2.1节的实际冻结研究主要讨论Pozzi 2019、Thenaisie 2022、Klocke 2024、Garulli 2025和Klocke 2026。第2.5节主要讨论皮层-STN连接，第2.6节讨论非beta指标。可是附录中还包括PMID:31665229、PMID:36730026、PMID:35441231和PMID:42236313。第2.7节对脑干网络的讨论也没有充分展开具体人体研究。参考文献中没有纳入2026年11月11日发表的PMID:43012884。",
   "why": "至少有几类重要证据没有得到应有的综合：\n\n第一，Georgiades等2019年研究使用STN多单位活动记录和虚拟现实冻结诱发范式，报告冻结相关的beta及theta活动变化。这不是自然行走证据，但正是应该单独归类讨论的STN-MUA证据。【turn404063search15】\n\n第二，2023年PMID:36730026研究报告仰卧踏步过程中冻结发作与STN及SNr神经元活动变化有关。它与自然行走研究的任务条件不同，具有解释研究冲突的价值。\n\n第三，Yin等2022年研究在16名PD患者中直接记录M1皮层ECoG，并同步记录自然行走中的冻结。研究分析了451次步行试验和3384秒冻结时间，发现冻结试次中M1 beta-gamma PAC异常，并观察到STN-DBS对PAC和冻结的同步调节。【turn667733search0】这不是STN局部PAC证据，但对于理解STN-皮层网络及DBS治疗机制非常重要。第2.6节笼统讨论PAC，却没有明确整合这项关键研究。\n\n第四，PMID:42236313报告STN theta活动与转弯冻结患者的焦虑程度及MoCA评分相关。该研究在主文中没有得到充分讨论，尽管它直接涉及H3、H5和H9所提出的认知情绪机制。【turn623213search3】\n\n第五，PMID:43012884于报告截止日前发表，研究比较了Med-On状态下执行功能型与感知功能型FOG患者的前额叶任务激活差异，但没有进入参考文献表。【turn553138search2】\n\n这些遗漏会使报告对MUA、PAC、theta、认知情绪和患者亚型的综合不完整。尤其不能因为某项研究不属于自然直立行走，就完全不讨论它；应当将其放在适当的证据层级中。",
   "severity": "major",
   "fix": "重新组织证据全景，至少分别建立自然行走实际冻结、受控任务或虚拟冻结、正常步态及冻结易感性、皮层网络、脑干网络、动物及计算模型六类证据。把上述研究纳入对应类别，明确记录来源是STN-LFP、STN-MUA、皮层ECoG、头皮EEG还是影像学。对于同一队列的多篇研究，明确区分新增数据与新增分析。每项重要研究都必须说明它对哪些现有结论或竞争性假说产生支持、反对或限定作用。"
  },
  {
   "rank": 4,
   "what": "证据直接性、证据可靠性和证据确定性没有得到严格分离，A/B/C证据分类的实际执行也不一致。",
   "where": "第1.2节定义A级为“同步记录STN神经活动与自然行走中经视频或临床确认的实际FOG”。但附录将Collomb-Clerc研究的运动捕捉和运动学识别结果归为A_actual_natural，而原始论文明确指出冻结主要由motion capture识别，没有使用视频记录。【turn990696search0】反过来，PMID:42236313的完整论文报告了临床确认的definite FOG，但附录仍将其事件证据标为unclear。【turn623213search3】",
   "why": "这不仅是个别分类错误，更反映出证据分类规则没有被一致执行。运动捕捉识别、视频确认、临床专家观察和经过验证的运动学算法可以提供不同强度的事件确认，但不能在没有定义的情况下混用。另外，A/B/C主要描述证据与目标问题的直接程度，不代表研究质量或因果确定性。一个只有2名患者、显著结果仅出现在1名患者的直接事件研究，仍可能属于A级，但其群体外推确定性极低。\n\n对附录进行统计，933条证据记录中有346条以abstract为依据，246条的n字段为空。部分核心研究，例如PMID:39470410和PMID:42571859，仍然只有摘要级证据记录，患者数和详细分析条件没有提取完整。报告没有使用统一的偏倚风险评价工具，也没有建立结论级GRADE式确定性评价。",
   "severity": "major",
   "fix": "至少分开四个维度：证据直接性、事件确认方式、研究偏倚风险、结论确定性。事件确认应区分视频确认、临床确认、运动捕捉、IMU算法和虚拟任务诱发。对观察性研究采用适当的偏倚风险工具，对随机干预研究采用RoB 2，对跨研究综合进行GRADE式评价。明确A级不是高质量证据的同义词。重要研究必须优先提取全文，而不能长期停留在摘要层面。"
  },
  {
   "rank": 5,
   "what": "FOG的行为学构念和患者表型虽然被报告承认存在异质性，但没有真正落实到研究证据的统一分类和跨研究比较中。",
   "where": "第2.1节Thenaisie研究列出complete akinesia、leg trembling和shuffling等表现；第3.7节列出FOG-Q、NFOG-Q、UPDRS冻结分项、自然FOG事件数、%FOG和SIP/TBC冻结等不同结局，并指出不能相互替代。第5.1节又把OFF-FOG、ON-FOG、ONOFF-FOG以及左旋多巴反应性与抵抗性作为冲突来源。",
   "why": "指出这些差异并不等于解决了这些差异。现有综合仍然大量使用Freezer、FOG、实际冻结和FOG阳性试次等宽泛标签，而没有为每项研究建立统一的表型信息。不同冻结表现可能涉及不同的运动输出失败；转弯冻结、门口冻结、启动冻结、双任务冻结也不一定共享同一个近端机制。药物反应性FOG和刺激诱发FOG同样不能简单混合。\n\n如果不把冻结表现类型、诱发条件、药物反应性、刺激状态和事件确认方式作为分层变量，那么所谓不同患者的beta方向相反，可能只是不同临床构念被放在一起比较。",
   "severity": "major",
   "fix": "建立统一的FOG表型字典，至少区分akinetic、trembling-in-place、shuffling及混合表现；记录转弯、门口、启动、双任务等触发条件；区分OFF-FOG、ON-FOG、ONOFF-FOG及药物反应程度；同时区分临床量表、实验室实际事件和算法检测结果。跨研究比较必须首先匹配这些条件，无法匹配的研究只能进行限定性综合。"
  },
  {
   "rank": 6,
   "what": "14项假说并不是14个处于同一解释层级的竞争性机制模型，其中相当一部分是调节因素、治疗机制或工程策略。",
   "where": "第4.1节称提出14个可检验假说，并指出它们不要求互斥。H1–H8主要讨论FOG发生机制；H9讨论患者亚型；H10讨论结构连接和刺激空间募集；H11讨论低频DBS及STN-SNr输出；H12讨论自适应DBS时序；H13讨论慢性可塑性；H14讨论STN投射特异性。",
   "why": "这组假说混合了不同层级的问题。例如：\n\n- H1与H2是局部神经动力学和跨区域通信的近端机制。\n- H3与H4涉及动作控制和任务负荷。\n- H6是把持续性易感状态和瞬时触发因素组合起来的整合框架，而不是与H1、H2处于同一层级的竞争模型。\n- H9是患者异质性或效应修饰因素。\n- H10是结构网络和刺激定位的调节机制。\n- H11–H13主要涉及治疗作用路径和时间效应。\n- H14则是细胞投射层级的解剖机制。\n\n这些因素完全可能同时成立。报告虽然承认不互斥，但仍然把它们放在同一个假说集合中排名。结果是，实验即使发现H1和H2同时成立，也没有明确说明这对其他模型意味着什么。许多预测实际上只是要求相关信号在冻结前出现，并没有真正区分不同因果解释。",
   "severity": "major",
   "fix": "将假说重组为三个层级。第一层是同一患者、同一事件的近端因果模型，例如局部beta驱动、皮层-STN协调失效、认知停止控制异常、运动学反馈或共同上游驱动。第二层是患者易感性和效应修饰因素，例如药物反应、结构连接及FOG亚型。第三层是治疗作用机制，例如刺激位置、刺激时序和慢性可塑性。对第一层模型建立明确的因果图、时间顺序、相互排斥的预测及模型比较标准；其余因素作为调节变量单独研究。"
  },
  {
   "rank": 7,
   "what": "因果推断与统计分析方案存在潜在的过度调整问题，而且把神经标志物的预测价值与其病理因果作用混为一谈。",
   "where": "H1要求“控制步速、步长、步频、腿部强直及药物状态后，burst指标仍然能够预测下一次冻结”；H2要求“控制平均beta功率、burst duration、步速及EMG振幅后，低频耦合仍具有独立预测能力”。H1还提出beta burst触发刺激优于随机刺激作为机制支持。",
   "why": "步速、步长、EMG及步态周期异常不一定只是混杂因素。它们可能是STN活动影响步态控制、最终导致FOG的中介变量。如果STN活动通过改变步长和步速增加冻结风险，那么在回归模型中控制这些变量，反而可能阻断真正的病理通路。\n\n同样，beta触发刺激优于随机刺激，可以证明beta信号具有一定的闭环控制价值，却不能单独证明beta振荡是FOG的病理原因。DBS会影响多个网络节点，刺激后行为改善也可能来自其他通路。Coherence增加同样不能证明信号方向是STN向肌肉传递；共同上游输入、感觉反馈和体积传导都可能产生相似结果。\n\n因此，目前的实验判别逻辑没有充分区分预测、直接因果效应和中介机制。",
   "severity": "major",
   "fix": "为每个假说预先建立因果DAG，明确混杂因素、中介变量和结果变量。分别报告不调整运动学的总关联、调整混杂因素后的预测能力，以及针对中介路径的独立分析。闭环刺激试验应区分信号预测价值与神经机制因果性，必要时采用随机化的时序操控、回放触发序列和适当的中介分析。对于网络通信假说，应预先规定方向性、时滞及共同输入排除方法，而不能只依赖普通coherence。"
  },
  {
   "rank": 8,
   "what": "主文H1–H14与结构化附录C1–C33之间存在具体的编号和语义映射错误。",
   "where": "主文H9是“患者亚型及状态依赖的多种神经机制”，H11是“低频DBS及STN-SNr输出通路的多路径作用”，H12是“自适应DBS的动态时序优势”，H14是“STN投射特异性运动功能机制”。但附录C29将低频STN-DBS及STN+SNr机制称为“H9”；C31将自适应DBS机制称为“H11”；C32将STN投射特异性机制称为“H12”。",
   "why": "这不是单纯的编号格式问题。结构化hypotheses中的关系映射显示，H11、H12和H14分别关联其他claim ID，而C29、C31、C32的文字标签却指向不同假说。C29实际上没有正确挂接到主文的H11。这样一来，未来如果根据新证据更新H11或H14，知识索引可能更新错误的结论，破坏报告所要求的证据—结论—假说映射关系。",
   "severity": "major",
   "fix": "不要使用容易随排序变化的编号作为唯一身份。为每个假说建立稳定的H-ID，并让主文、claims、evidence和hypotheses对象全部引用同一个ID。增加自动一致性检查：检查假说名称、claim内容、关系方向及所有引用是否一致；任何修改编号或重排都不能改变实体身份。"
  },
  {
   "rank": 9,
   "what": "第一优先研究的多模态实验设计在受试者组成和记录条件上不够可实施。",
   "where": "第5.2节建议同时纳入自然FOG患者、存在步态障碍但没有FOG的PD患者及正常对照；随后在同步记录表中统一安排“双侧STN-LFP”“M1/PMC/S1相关信号”“下肢EMG”“IMU及步态运动学”等测量。",
   "why": "STN-LFP通常只能在已经植入适当DBS电极、具备感知功能的患者中获得。健康对照和没有STN植入电极的PD对照不可能提供相同的STN-LFP数据。不同患者是否有感知型设备、能否在刺激开启时记录、是否有合适的接触点，也会影响可用数据。\n\n此外，如果M1、PMC和S1信号计划通过侵入性皮层电极获得，就不可能在所有患者中常规实施；如果使用头皮EEG，则必须明确其与皮层ECoG及STN-LFP的信号性质差异。当前方案没有区分围手术期外接电极患者和慢性植入患者，也没有说明各组能够获得哪些共同指标。",
   "severity": "major",
   "fix": "拆分为可执行的研究队列。第一队列为具备STN sensing能力的DBS患者，采集STN-LFP、头皮EEG、EMG、IMU和视频。第二队列为围手术期外接电极患者，在有临床依据和伦理许可时增加皮层ECoG。第三队列为非DBS患者和健康对照，采用非侵入性测量，不强行要求STN-LFP。明确每个队列的共同指标、特有指标、样本量估算、事件发生率、设备兼容性及安全限制。"
  },
  {
   "rank": 10,
   "what": "运动状态下的电生理信号伪迹和信号可比性没有得到系统性审查。",
   "where": "第2.5、2.6节以及第5.2、5.3节大量使用coherence、PAC、theta、alpha、gamma、beta burst及复杂度等指标，但没有建立跨研究统一的信号质量评价表。尤其是H2将低频coherence作为核心通信指标，第5.2节又建议直接比较多区域相位协调。",
   "why": "自然行走中的STN-LFP容易受到电缆运动、机械扰动、ECG、肌电串扰、参考电极、体积传导及刺激伪迹影响。低频theta尤其需要排除心电和运动伪迹。跨区域coherence可能反映共同输入，而不是真正的神经区域间通信。不同研究的采样率、滤波方式、基线归一化、双极接触点组合和伪迹剔除方法也会显著改变频谱结果。\n\n例如，2026年Klocke相关研究本身对运动、电缆及其他伪迹进行了筛查，而报告没有把这些方法学差异系统性纳入跨研究比较。【turn302347view0】这会影响报告对低频网络信号及复杂度指标的机制解释。",
   "severity": "major",
   "fix": "增加专门的信号质量评价维度，逐研究提取ECG处理、运动伪迹检测、电缆伪迹处理、EMG串扰、参考电极、滤波器、采样率、刺激状态和异常片段剔除规则。对coherence使用相位滞后、虚部coherence或其他适当方法进行敏感性分析。对关键theta、alpha和beta发现进行不同参考配置和伪迹处理下的稳健性检验。"
  },
  {
   "rank": 11,
   "what": "部分关键研究的样本分母、事件数量和原始文献记录存在可以核实的错误或不完整之处。",
   "where": "第2.1节Klocke 2026研究写道：“13名PD患者；11名具有有效神经记录”。Garulli研究写道：“研究共观察到27次FOG事件”。第2.2节第266行讨论Singh研究的low-beta显著性，但该研究DOI:10.1016/j.baga.2012.10.002没有作为独立文献进入references和evidence登记表。",
   "why": "Klocke原始预印本的13名患者均有记录，11名是出现冻结转弯的患者，而不是具有有效神经记录的总人数；另有一个半球的电极定位问题需要单独说明。【turn302347view0】Garulli正式论文报告两名患者分别观察到20次和8次冻结事件，但后续神经分析分别使用19次和8次。因此，27是分析事件数，而28是原始观察事件数，报告应当区分。【turn884610search1】\n\n此外，Singh 2013研究是beta方向冲突的重要原始证据，报告却没有将其纳入正式参考文献和结构化证据表，导致第266行所讨论的原始证据无法从报告自己的知识索引中追溯。【turn404063search6】这些问题说明样本分母和引文元数据还没有经过一致的原始全文核查。",
   "severity": "moderate",
   "fix": "统一区分n_enrolled、n_with_valid_neural_data、n_with_event、n_events_observed、n_events_analyzed和n_trials。对每项研究逐一回查全文及补充材料，明确原始事件数与最终分析事件数。建立PMID/DOI完整性检查，确保正文中提到的每项原始研究都进入正式references和evidence表。对不一致的摘要、正文和图表数字保留明确的核查记录。"
  },
  {
   "rank": 12,
   "what": "STN-SNr联合刺激Meta分析的相互冲突没有完成真正的定量和方法学裁决。",
   "where": "第2.8节表格列出长期随机交叉研究、急性双盲研究、2026年多中心研究以及两项2026年Meta分析，并指出“一项分析未发现一致额外获益，另一项Meta分析报告联合刺激具有统计学显著改善”。",
   "why": "报告只提出可能来自纳入研究、效应量和配对数据处理差异，却没有在主文给出两项Meta分析的具体合并效应量、置信区间、I²、研究数量、患者数量、纳入试验重叠程度和偏倚风险。对于小样本交叉试验，是否正确处理配对数据和受试者内相关性尤其重要。两个Meta分析也不能被当成两次独立临床重复验证，因为它们可能重复使用相同的底层试验。\n\n另外，第2.8节报告31项研究、905名患者及FOG-Q的MD=-2.99，但没有充分讨论异质性、证据确定性和该差异是否达到临床重要程度。",
   "severity": "moderate",
   "fix": "建立Meta分析的底层研究对照表，逐项列出纳入试验、队列重叠、刺激靶点、药物状态、随访时间、FOG结局和配对数据处理方法。对STN-SNr联合刺激重新进行统一的数据提取和敏感性分析，报告效应量、95%CI、I²、预测区间及GRADE确定性。对于FOG-Q等临床量表，同时比较统计学显著性和临床重要差异。"
  },
  {
   "rank": 13,
   "what": "预测模型证据的分类不够完整，没有充分区分冻结检测、试次分类和真正的冻结前预测。",
   "where": "第6.1节重点讨论5名患者的虚拟步行机器学习模型，报告weighted F1约0.67、leave-one-trial-out验证及166次假阳性预测，但没有在主文讨论2026年Klocke转弯冻结预印本中的分类模型。",
   "why": "Klocke预印本报告了leave-one-subject-out交叉验证，AUC约0.84，但模型使用的特征包括转弯相关阶段，因此不能直接将其解释为冻结发生前的实时预测能力。【turn302347view0】这项结果并不推翻报告关于早期预测证据不足的判断，却是重要的跨患者分类证据，应该纳入比较。\n\n目前报告对检测、分类和预测的区分仍不充分。一个在冻结已经发生或转弯已经开始后识别冻结试次的模型，与能够提前数秒预测下一次冻结的模型，临床意义完全不同。仅报告F1或AUC无法说明其实际闭环应用价值。",
   "severity": "moderate",
   "fix": "将模型分成三个层次：冻结事件检测、冻结试次或运动状态分类、冻结发生前预测。对每个模型明确特征使用的时间范围、是否包含冻结开始后的数据、训练测试分割单位及是否为独立患者验证。统一报告event-level sensitivity、lead-time distribution、false positives/hour、post-event detection ratio、calibration和external-site validation。"
  },
  {
   "rank": 14,
   "what": "持续自主改进目前只是知识管理方案的设想，没有证明已经形成有效的更新、验证和纠错闭环。",
   "where": "第7.3节提出“新证据出现后的自动重新评价逻辑”，第7.4节提出覆盖率、追溯性、队列重叠识别准确性和独立研究者重复判断等评价指标。",
   "why": "这些内容说明了未来应该怎样改进，但没有展示一个实际运行的系统。报告没有提供自动文献摄取流程、版本变更记录、历史结论更新日志、队列去重测试、错误发现与修正案例，也没有报告独立研究者能否根据现有证据表重复得到相同结论。\n\n更重要的是，当前报告自身仍然存在预印本与正式论文重复、样本分母错误、引文缺漏和假说编号映射错误。也就是说，它提出了质量控制目标，却没有证明当前知识体系已经达到这些目标。",
   "severity": "moderate",
   "fix": "将第7节从原则性建议改为可验证的实施方案。建立版本化证据库、自动文献更新、队列和版本去重、证据冲突提醒、结论变更日志及人工审核流程。设计一组已知存在重复发表、队列重叠和结论冲突的测试文献，建立基准答案，定期测量系统识别准确率。至少展示一次新研究加入后，旧结论如何被重新评价、修改及独立复核的完整案例。"
  }
 ],
 "overall": "这份报告的主要问题不是缺少科学概念或机制假说，而是证据综合的底层可靠性和可审计性还不足以支撑它所呈现的完整程度。最严重的风险来自检索过程不可复现、预印本与正式发表版本及重复队列没有系统去重、重要人体电生理证据没有充分进入主文，以及直接性分类与研究质量评价没有分开。其次，14项假说混合了近端病理机制、患者易感性、治疗作用路径和工程控制策略，尚未形成真正能够相互区分的因果模型。报告已经提出不少正确的方法学警告，但没有始终贯彻到证据分类、统计解释和研究设计中。特别是，控制运动学变量可能造成过度调整，coherence不能直接证明信息传递方向，beta触发刺激的疗效也不能直接证明beta是致病原因。最终建议是先修复检索、原始文献核查、队列去重、证据分级和知识映射，再重新评估跨研究结论及竞争性机制。否则，继续增加文献、证据条目和假说数量，只会扩大一个尚未充分验证的知识体系，而不会真正提高其科学可靠性。"
}

===== abs_g6.json =====
{
 "standards": [
  {
   "n": 1,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "文献覆盖面较广，结构化附录包含大量研究和证据记录，但检索过程不可复核。报告没有明确说明检索数据库、完整检索式、各数据库检索日期、纳入排除标准、筛选流程及重复队列识别方法。文献数量不能直接证明重要研究没有遗漏。尤其缺少可重复的文献覆盖审计。",
     "where": "报告写明“证据截止日期：2026年11月13日”，但末尾又说明“本报告仅依据本次提供的结构化结论、假说、证据表及其文献编号进行综合，没有引入外部文献或新增实验数据。”没有提供完整检索方法。<FileCite ref=\"turn0file0\" line_range_start={7} line_range_end={7} /> <FileCite ref=\"turn0file0\" line_range_start={1364} line_range_end={1364} />"
    },
    {
     "severity": "moderate",
     "what": "部分重要交叉证据虽然进入参考文献或结构化附录，但没有充分进入正文的机制综合。包括：Georgiades等人的STN术中MUA研究（PMID:31665229），涉及8名患者、19次VR诱发运动阻滞及STN放电与下肢EMG的时间关系；Klocke等2026年关于认知、焦虑与STN theta活动的研究（PMID:42236313）；以及2026年基于STN神经活动的activity-dependent aDBS研究（PMID:42297979）。后两项分别直接影响H4认知情绪负荷解释和H12动态刺激解释。尤其是2026年aDBS研究，正文没有充分讨论其患者特异性频段及冻结改善结果。",
     "where": "直接事件证据主要展开为“2019年：冻结相关的皮层-STN低频解耦”“2022年：自然冻结期间STN低beta活动增强”及后续研究。H4支持依据为“[PMID:41131028; PMID:41388789; PMID:28892573]”，H12支持依据为“[DOI:10.1101/2024.06.26.24309418; PMID:32634599]”，没有将上述2026研究纳入相应正文论证。<FileCite ref=\"turn0file0\" line_range_start={81} line_range_end={106} /> <FileCite ref=\"turn0file0\" line_range_start={735} line_range_end={738} /> <FileCite ref=\"turn0file0\" line_range_start={916} line_range_end={936} />"
    },
    {
     "severity": "minor",
     "what": "没有纳入2026年国际FOG共识组织更新的FOG临床定义和视频技术标注标准（Gilat等，DOI:10.1038/s41582-025-01179-3）。这项研究直接涉及FOG事件定义、视频标注和患者亚型分类。报告虽然强调统一事件标注，但没有利用这项重要标准化成果。特别是shuffling应区分阵发性冻结表现与持续性小碎步，避免将两者混为同一结局。",
     "where": "报告将“shuffling steps with minimal effective forward movement”列为冻结表现，并提出“视频及专家标注 | 实际冻结起止时间和亚型”，但没有给出与最新共识一致的操作性定义。<FileCite ref=\"turn0file0\" line_range_start={136} line_range_end={142} /> <FileCite ref=\"turn0file0\" line_range_start={1006} line_range_end={1013} />"
    }
   ]
  },
  {
   "n": 2,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "存在一处重要的原始文献归属错误。2017年Freezer在SIP期间beta功率较低的研究是Syrkin-Nikolau等人（PMID:28890315），不是Storzer等人。Storzer等人（PMID:28892573）研究的是行走和骑车，发现两种运动状态下STN beta总体受到抑制，同时Freezer存在运动启动相关的约18 Hz窄带功率增强。两项研究的任务、频谱特征和结论不同。错误归属会影响beta方向冲突的解释。",
     "where": "表格原文：“Storzer等，2017 | SIP无冻结 | Freezer的相对beta功率较低”。其后引用列表包含PMID:28892573，却没有在该表述处引用真正支持低beta结果的PMID:28890315。<FileCite ref=\"turn0file0\" line_range_start={237} line_range_end={249} />"
    },
    {
     "severity": "moderate",
     "what": "STN+SNr联合刺激部分的原始临床证据引用不完整。20名完成患者、额外改善4.7分FOG-Q的长期随机交叉研究应直接引用PMID:40760816；10名患者的急性双盲交叉研究应引用PMID:38363617。正文对应引用列表却包含PMID:35490252（综述）和PMID:37104542（计算模型），没有列出上述关键原始临床试验。虽然原始试验出现在参考文献和结构化附录中，但正文无法直接追溯到最重要的原始证据。",
     "where": "表格原文：“20名完成患者中，STN+SNr相较STN-only的FOG-Q额外改善4.7分”；其后引用为“[PMID:35490252; PMID:37104542; PMID:42860886; PMID:42909654; PMID:42968793]”。<FileCite ref=\"turn0file0\" line_range_start={457} line_range_end={467} />"
    },
    {
     "severity": "moderate",
     "what": "预印本与正式发表版本没有得到充分的版本核对和去重。2025年Garulli预印本DOI:10.1101/2025.04.22.650006已有对应正式发表版本PMID:41654501。2025年Collomb-Clerc相关预印本DOI:10.1101/2025.01.10.632393也需要与正式发表的PMID:40709562明确匹配。报告仍将这类关系表述为“可能属于同一研究”。此外，2026年Klocke研究DOI:10.21203/rs.3.rs-9617843/v1和Beaudoin研究DOI:10.64898/2026.08.13.744293应明确标注为预印本，不能与正式同行评审论文给予完全相同的证据成熟度。",
     "where": "报告写道：“2025年预印本与正式发表版本可能属于同一研究”；同时正文分别使用上述预印本DOI描述研究结果，但没有一致标记发表状态。<FileCite ref=\"turn0file0\" line_range_start={193} line_range_end={194} /> <FileCite ref=\"turn0file0\" line_range_start={227} line_range_end={229} /> <FileCite ref=\"turn0file0\" line_range_start={587} line_range_end={594} />"
    },
    {
     "severity": "moderate",
     "what": "部分关键研究的证据提取停留在摘要层面，没有充分利用原始全文。一个例子是PMID:39470410：原文提供了12名患者、5名FOG患者、7名非FOG患者，以及alpha频段（8–12 Hz）STN-腓肠肌相干性和步态周期相关结果。报告却称具体样本量、频段和时间窗口信息有限。另一个例子是PMID:42297979：附录仅采用摘要，因而没有提取全文中的35名患者神经活动研究和4名患者活动依赖性刺激可行性研究，也没有纳入P2、P3的FOG改善结果。这些信息对比较beta特异性刺激与活动状态依赖刺激非常重要。",
     "where": "关于PMID:39470410，正文写道：“现有报告对样本数量、具体频段、时间窗口及统计模型提供的信息有限。”结构化附录对PMID:42297979则注明“摘要未报告患者人数、Freezer比例或具体临床特征”，并标记“basis:abstract”。<FileCite ref=\"turn0file0\" line_range_start={148} line_range_end={166} /> <FileCite ref=\"turn0file0\" line_range_start={1368} line_range_end={1369} />"
    }
   ]
  },
  {
   "n": 3,
   "verdict": "met",
   "issues": [
    {
     "severity": "minor",
     "what": "机制综合已经比较深入，但部分竞争性解释尚未完全转化为同一实验中的可区分变量。例如H3、H4和H5涉及认知负荷、焦虑、动作选择及注意资源竞争；2026年Klocke等研究（PMID:42236313）已经发现转弯冻结期间STN theta功率与焦虑程度及MoCA评分相关。然而，第一优先级自然FOG多模态实验没有明确纳入焦虑量表、认知表现及认知双任务负荷的同步测量。建议补充这些变量，以免将认知情绪因素产生的STN变化误判为局部运动病理或反馈异常。",
     "where": "H4提出“注意负荷、视觉空间导航、步速下降及步长变化”等解释；但5.2节“同步记录内容”仅列出LFP、皮层信号、EMG、IMU、视频和测力平台，没有明确列出认知及情绪测量。<FileCite ref=\"turn0file0\" line_range_start={715} line_range_end={735} /> <FileCite ref=\"turn0file0\" line_range_start={1006} line_range_end={1013} />"
    }
   ]
  },
  {
   "n": 4,
   "verdict": "met",
   "issues": []
  },
  {
   "n": 5,
   "verdict": "not_testable",
   "issues": []
  },
  {
   "n": 6,
   "verdict": "met",
   "issues": []
  },
  {
   "n": 7,
   "verdict": "not_testable",
   "issues": []
  }
 ],
 "spot_checks": [
  {
   "claim": "STN参与PD相关FOG运动控制，但尚不能认定STN是唯一或始发病理位置。",
   "cited": "PMID:31505548; PMID:31665229; PMID:36070366; PMID:39470410; PMID:40709562; DBS干预研究",
   "verdict": "consistent",
   "why": "与原始证据一致。自然行走LFP、术中STN单神经元/MUA记录及冻结事件研究共同支持STN参与FOG相关运动网络。Georgiades等研究还记录了8名患者的19次VR诱发运动阻滞，发现STN放电及beta/theta活动与冻结相关运动输出异常有关。不过该研究属于术中VR任务，不等同于自然行走。现有证据仍不能证明STN是FOG唯一或始发病理位置。PMID:31665229。"
  },
  {
   "claim": "实际FOG事件附近存在STN神经活动异常，但频段、方向和时间阶段具有明显异质性。",
   "cited": "PMID:31505548; PMID:36070366; PMID:39470410; DOI:10.1101/2025.04.22.650006; DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "consistent",
   "why": "与原始研究一致。Pozzi研究发现冻结相关皮层-STN低频耦合下降；Thenaisie研究发现实际冻结期间低beta增强；Klocke研究发现冻结前后的STN-肌肉协调异常；Garulli研究发现复杂度变化，但显著结果主要来自一名患者；2026年转弯冻结预印本发现冻结转弯期间低beta相对功率增加，但冻结前转弯与正常转弯的直接比较没有得到显著差异。报告正确区分了冻结前、冻结中和恢复期，也没有把不同指标当成同一现象。"
  },
  {
   "claim": "表2.2所述Storzer等2017年研究发现，Freezer在没有冻结的SIP阶段相对beta功率较低。",
   "cited": "PMID:28892573（Storzer et al., 2017）",
   "verdict": "wrong",
   "why": "这是明确的原始文献归属错误。PMID:28892573研究的是行走和骑车，报告Freezer在运动启动时出现约18 Hz窄带功率增强，并非SIP期间相对beta功率降低。真正报告Freezer在无冻结运动期间beta功率较低的是Syrkin-Nikolau等人的PMID:28890315。2026年综述也将这两项研究分别列出。该错误不推翻报告关于beta不是普遍FOG标志的总体结论，但该表格行不能成立。"
  },
  {
   "claim": "Pozzi等2019年研究发现，冻结开始前约1.5秒皮层-STN的4–13 Hz耦合下降；冻结开始时beta耦合增加，但成功停止和门口通过也可出现类似beta耦合变化。",
   "cited": "PMID:31505548",
   "verdict": "consistent",
   "why": "与原始研究报告一致。研究同步记录7名患者的EEG和STN-LFP，其中5名有FOG，分析14次实际冻结事件。低频耦合下降发生于冻结前并在冻结期间持续，恢复行走后重新出现。beta耦合增加并非FOG特异，因为成功停止等动作转换也出现类似变化。需要注意，小样本和重复事件的患者内聚类限制了群体推断，研究也没有证明耦合下降具有因果作用。"
  },
  {
   "claim": "Thenaisie等2022年研究发现，实际冻结期间STN低beta活动增强，并与双腿交替运动受损相关；冻结终止后低beta活动消退。",
   "cited": "PMID:36070366",
   "verdict": "consistent",
   "why": "核心结果与原始研究一致。研究中FOG神经分析涉及4名患者和173次冻结事件，报告了冻结期间低beta活动增强及冻结终止后的活动变化，并结合下肢肌电分析步态恢复。报告正确指出事件数不能代替患者数，也没有把时间关联直接解释为因果关系。"
  },
  {
   "claim": "Anidi等2018年研究发现，Freezer在SIP和前向步行中存在较长的STN beta burst duration，部分实际冻结事件也出现延长。",
   "cited": "PMID:30196050; PMID:31505548; DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "consistent",
   "why": "与原始研究总体一致。Anidi研究发现Freezer的病理性beta burst持续时间与冻结易感性相关，部分发生SIP冻结的患者还出现冻结期间burst持续时间延长。但这不意味着自然FOG期间所有患者的平均burst duration都会增加。Pozzi研究没有发现稳定的冻结期burst duration延长，Klocke 2026预印本则显示长时程burst比例变化与平均持续时间差异可以并存。报告对这几类指标进行了合理区分。"
  },
  {
   "claim": "Collomb-Clerc等2025年研究发现，STN活动与步态启动运动学之间的关系能够反映后续FOG风险，首次FOG发生在GI后中位约8步。",
   "cited": "DOI:10.1101/2025.01.10.632393; PMID:40709562",
   "verdict": "consistent",
   "why": "与正式发表研究的主要结果一致。研究纳入38名患者，FOG观察组12名，分析99个阳性GI试次和263次FOG事件，首次FOG发生在GI后中位约8步。报告也正确强调，这属于同一试次后续冻结风险的关联证据，不是冻结发生前最后一秒的即时触发信号。正式发表版本应作为主要引用，并与预印本合并管理。"
  },
  {
   "claim": "DBS总体具有一定FOG治疗价值，但STN+SNr联合刺激相较STN单靶点的额外获益仍存在冲突。",
   "cited": "PMID:42098512; PMID:40760816; PMID:38363617; PMID:39957196; PMID:42860886; PMID:42909654; PMID:42968793",
   "verdict": "consistent",
   "why": "与现有临床证据一致。DBS综合Meta分析报告FOG-Q平均差MD=-2.99，95%CI[-5.69,-0.29]，但结果涉及不同靶点、频率及药物状态，不能全部归因于STN。STN+SNr方面，长期随机交叉研究报告20名完成患者额外改善4.7分FOG-Q；10名患者的急性双盲研究没有发现明确额外优势；2026年多中心研究在90天时也没有证明联合刺激优于STN-only。两项2026年Meta分析的结论不同。因此，报告将其判定为存在冲突而非已确立的联合刺激优势，是合理的。"
  }
 ]
}

===== factcheck.json =====
[
 {
  "paper": "Syrkin-Nikolau et al., 2017（Freezer在SIP期间beta功率降低的研究）；被错误归属给Storzer et al., 2017",
  "pmid": "28890315",
  "doi": "",
  "report_says": "报告表2.2将“Freezer在没有冻结的SIP阶段相对beta功率较低”归于Storzer等人2017年的研究，并引用PMID:28892573。",
  "judge_says": "PMID:28892573对应的Storzer等人研究考察的是行走和骑车，发现两种运动状态下STN beta总体受到抑制，同时Freezer存在运动启动相关的约18 Hz窄带功率增强，并未报告SIP期间相对beta功率较低。真正报告Freezer在无冻结运动期间beta功率较低的是Syrkin-Nikolau等人的研究（PMID:28890315）。报告将两篇研究的作者、任务和结果错误对应。",
  "source": "abs_g6.json",
  "pid": "PMID:28890315",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "During the SIP task (without FOG) there was lower relative beta power in the Freezer compared to Non-Freezer groups (H(1) = 7.17, P = 0.036), which resulted in a greater attenuation of resting state beta power in Freezers (F (1, 15) = 28.37, P < 0.001).",
   "Relative alpha and beta power was calculated by dividing the summed absolute alpha or beta power by the summed power in the 40–70Hz band during the resting state, and allowed comparison across subjects, whose raw signal magnitude can vary by one or two orders of magnitude, see supplementary information.",
   "The SIP task was performed at the time of initial programming before STN DBS was activated in 12/14 subjects. Two subjects performed the SIP task at 6 months post initial programming. The FW and TBC tasks were performed on the same day, after a mean of 14.6 months (range 6 – 27 months) of STN DBS."
  ],
  "judge_quotes": [
   "Subthalamic Neural Entropy is a feature of Freezing of Gait in freely moving people with Parkinson’s disease",
   "Syrkin-Nikolau Judy a Koop Mandy Miller a Prieto Thomas a Anidi Chioma a Afzal Muhammad Furqan a Velisar Anca a Blumenfeld Zack a Martin Talora a Trager Megan a Bronte-Stewart Helen a b *",
   "During the SIP task (without FOG) there was lower relative beta power in the Freezer compared to Non-Freezer groups (H(1) = 7.17, P = 0.036), which resulted in a greater attenuation of resting state beta power in Freezers (F (1, 15) = 28.37, P < 0.001).",
   "Subjects completed three tasks: (1) Stepping in Place 6 (SIP); (2) Forward Walking 7 (FW); (3) Turning and Barrier Course 8 (TBC), Figure 1."
  ],
  "why": "报告的核心实验结果有明确全文依据：Syrkin-Nikolau等人的研究确实发现，在没有FOG的SIP阶段，Freezer组相对于Non-Freezer组具有较低的relative beta power。因此，不能认定这一科学发现与全文不符。但报告将该结果归于Storzer等人并引用PMID:28892573，这一作者和文献归属与附件所标识的论文不一致。附件论文的作者是Syrkin-Nikolau等人，PMID为28890315，因此报告的结果描述得到支持，但其文献归属没有附件依据，整体判为partly。指控者的描述也应判为partly：其中关于真正报告SIP无冻结期间Freezer相对beta功率较低的是Syrkin-Nikolau等人（PMID:28890315）的判断，得到全文明确支持；但关于PMID:28892573的Storzer研究考察步行和骑车、存在约18 Hz运动启动相关窄带功率增强、没有报告SIP结果等具体描述，附件全文没有提供该研究的信息，不能据此确认或否定。另一个重要限定是，论文所称relative beta power是以静息状态40–70 Hz功率进行归一化的指标，比较对象是Non-Freezer组，而不是简单表示Freezer自身运动时的绝对beta功率降低。此外，SIP任务多数在DBS激活前完成，而FW和TBC在平均14.6个月DBS治疗后完成。综上，附件足以证明SIP结果确实存在于Syrkin-Nikolau论文，但不足以独立验证Storzer论文的具体结果及两篇论文之间的全部错误对应指控。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "PMID:39470410（STN-腓肠肌相干性与步态周期研究）",
  "pmid": "39470410",
  "doi": "",
  "report_says": "报告称：“现有报告对样本数量、具体频段、时间窗口及统计模型提供的信息有限。”",
  "judge_says": "原文提供了明确的样本量和频段信息：共12名患者，其中5名FOG患者、7名非FOG患者；研究分析了alpha频段（8–12 Hz）的STN-腓肠肌相干性及其与步态周期的关系。因此，报告对该研究可提取的样本量、频段和研究结果信息的描述不准确或不充分。",
  "source": "abs_g6.json",
  "pid": "PMID:39470410",
  "verdict": "no_fulltext"
 },
 {
  "paper": "PMID:42297979（2026年基于STN神经活动的activity-dependent自适应深部脑刺激研究）",
  "pmid": "42297979",
  "doi": "",
  "report_says": "报告结构化附录仅依据摘要，并注明：“摘要未报告患者人数、Freezer比例或具体临床特征”（basis:abstract）。",
  "judge_says": "原文全文包含摘要之外的重要信息：35名患者的神经活动研究，以及4名患者的活动依赖性刺激可行性研究；还报告了P2、P3患者的FOG改善结果。报告仅依据摘要提取证据，未反映原文全文中的患者数量、研究分组及刺激干预结果，对该研究的证据内容呈现不完整。",
  "source": "abs_g6.json",
  "pid": "PMID:42297979",
  "verdict": "no_fulltext"
 },
 {
  "paper": "Collomb-Clerc et al., 2025，STN电生理与步态启动/冻结步态研究（预印本及正式发表版本）",
  "pmid": "40709562",
  "doi": "10.1101/2025.01.10.632393",
  "report_says": "附录将该研究的冻结事件证据归类为A_actual_natural，即符合自然行走中经视频或临床确认的实际冻结事件；同时将预印本和正式发表版本分别保存为文献及证据记录。",
  "judge_says": "原始论文明确指出，冻结事件主要通过motion capture（运动捕捉）及运动学分析识别，并没有使用视频记录，因此不符合报告所定义的A类事件确认标准。此外，预印本与正式发表版本属于同一研究的不同发表版本，不应作为独立研究重复计入证据。",
  "source": "open_g56.json",
  "pid": "PMID:40709562",
  "report_supported": "no",
  "judge_supported": "partly",
  "report_quotes": [
   "GI scores related to pace, rhythm, and balance were derived from kinetics, and FOG was identified using kinematics.",
   "In patients with PD, motion capture was used to annotate FOG episodes, characterized by an arrest in walking with failure to initiate or continue stepping. Each FOG episode was marked online and verified offline by 2 independent reviewers (see Supplementary Fig S1).",
   "Last, whereas the FOG events were primarily detected using motion capture, each trial was verified online and reviewed offline by independent raters, although video recordings were not used. Future studies should incorporate video-based validation to improve rater reliability and analysis of exact FOG onset.",
   "First, this study was conducted under controlled experimental conditions, which may not fully capture the variability of FOG in everyday life."
  ],
  "judge_quotes": [
   "GI scores related to pace, rhythm, and balance were derived from kinetics, and FOG was identified using kinematics.",
   "In patients with PD, motion capture was used to annotate FOG episodes, characterized by an arrest in walking with failure to initiate or continue stepping. Each FOG episode was marked online and verified offline by 2 independent reviewers (see Supplementary Fig S1).",
   "Last, whereas the FOG events were primarily detected using motion capture, each trial was verified online and reviewed offline by independent raters, although video recordings were not used. Future studies should incorporate video-based validation to improve rater reliability and analysis of exact FOG onset.",
   "During the DOPAOFF recording session (1,229 trials), we observed FOG episodes in 12 of these 35 patients with PD during straight-ahead walking or turning (FOG-OBS), whereas 23 patients with PD had no FOG episodes (FOG-NOBS) (Fig 1E-G)."
  ],
  "why": "报告的A_actual_natural分类与全文披露的事件确认方法不符。论文确实记录了真实行走过程中发生的FOG事件，并由两名独立审查者进行在线标记和离线核查，因此实际冻结事件的存在有依据。但论文明确说明，事件主要通过motion capture识别，没有使用视频记录，并且研究是在受控实验条件下进行的。全文没有说明独立审查者进行了临床确认，也没有证据表明这些事件经过临床确认。因此，不能据此认定符合报告所定义的自然行走中经视频或临床确认的A类标准。指控者关于运动捕捉识别、未使用视频以及受控实验环境的描述有明确全文依据。另一方面，全文没有提及预印本、预印本与正式发表版本的对应关系，也没有说明文献记录或证据记录的保存及去重方式。因此，仅凭全文无法判断两种发表版本是否被分别保存，更无法判断是否被作为独立研究重复计数。综合而言，报告的核心证据分类与全文不符，故report_supported为no；指控者的事件识别方法判断有依据，但关于预印本与正式版本是否重复计数的判断无法由全文证实，故judge_supported为partly。",
  "verdict": "accusation_holds"
 },
 {
  "paper": "Klocke et al., 2026，Subthalamic Signatures of Freezing while Turning in Parkinson's Disease（转弯冻结预印本）",
  "pmid": "",
  "doi": "10.21203/rs.3.rs-9617843/v1",
  "report_says": "第2.1节称研究纳入13名PD患者，其中11名具有有效神经记录。",
  "judge_says": "原始预印本中13名患者均有神经记录；11名指的是出现转弯冻结的患者，而不是具有有效神经记录的总人数。报告混淆了有效记录人数与发生冻结事件的人数。",
  "source": "open_g56.json",
  "pid": "DOI:10.21203/rs.3.rs-9617843/v1",
  "report_supported": "partly",
  "judge_supported": "yes",
  "report_quotes": [
   "We recorded subthalamic local field potentials synchronized to gait kinematics in the medication-OFF and stimulation-Off state in 13 Parkinson’s disease patients with freezing of gait.",
   "STN-LFPs synchronized to gait kinematics in the medication-OFF and stimulation-Off state of 13 PwPD with FoG were recorded.",
   "We were able to confirm localization of all leads in the STN in all but one hemisphere (subject 15, left STN), which was subsequently excluded from spectral analyses.",
   "Due to a malfunction in IMU recordings in subject 6, analyses requiring kinematic input were excluded."
  ],
  "judge_quotes": [
   "We subsequently analysed the spectral modulation and beta burst characteristics across locomotor states including 224 regular turns (n = 13), 122 turns containing freezing (n = 11), unimpaired walking (1191 gait cycles, n = 12), as well as the transition periods before initiating turning (Fig. 1).",
   "Subject-averaged spectral power of epochs of FoG that occurred during turning (time series drawn from FoG start to FoG end) (grey, n = 11), compared to epochs of equal length during regular turning (blue, n = 11)."
  ],
  "why": "报告关于纳入13名PD患者的说法有全文依据，但关于其中11名具有有效神经记录的说法没有依据，且与原文明确报告13名患者均进行了STN-LFP记录不符，因此整体判定为partly。原文确实报告13名患者的神经记录。需要注意，受试者15只有一个半球（左STN）因电极定位问题被排除出频谱分析，并非整名患者被排除；受试者6因IMU故障被排除的是需要运动学输入的分析，而非神经记录。另一方面，结果部分明确将122次包含冻结的转弯标记为n=11，图3进一步将转弯冻结相关的频谱数据标记为n=11。因此，指控者关于11名指发生转弯冻结的患者、而非具有有效神经记录的总人数的解释有全文依据。报告混淆了神经记录人数与发生冻结转弯的患者人数。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Klocke et al., 2026，Cognitive and Emotional Determinants of Subthalamic Oscillations During Freezing While Turning in Parkinson's Disease",
  "pmid": "42236313",
  "doi": "",
  "report_says": "附录将该研究的冻结事件证据标记为unclear（不明确）。",
  "judge_says": "完整论文明确报告了临床确认的definite FOG，因此将事件确认方式标记为unclear不符合原文。此外，该研究与Klocke转弯冻结预印本使用相同的13名受试者及相同的患者编号，属于同一队列的不同分析，不能视为两次独立患者重复验证。",
  "source": "open_g56.json",
  "pid": "PMID:42236313",
  "verdict": "no_fulltext"
 },
 {
  "paper": "Garulli et al., 2026，PD步态障碍及冻结步态的深度神经行为表型研究（预印本及正式发表版本）",
  "pmid": "41654501",
  "doi": "10.1101/2025.04.22.650006",
  "report_says": "第2.1节称研究共观察到27次FOG事件；同时将预印本和正式发表版本分别保存为文献及证据记录。",
  "judge_says": "正式论文报告两名患者分别观察到20次和8次冻结事件，原始观察总数为28次；后续神经分析实际使用的是19次和8次，共27次。报告将分析纳入的27次事件误写为原始观察到的事件总数。此外，预印本与正式论文属于同一研究的不同发表版本，不应作为独立研究重复计入。",
  "source": "open_g56.json",
  "pid": "PMID:41654501",
  "report_supported": "no",
  "judge_supported": "partly",
  "report_quotes": [
   "Subject 1 had 20 freezing episodes, during turning and continuous walking (median duration: 7 s, range 1–33 s). Subject 2 had 8 freezing episodes, mainly during turning (median duration: 3.5 s, range 2–8 s).",
   "We parsed the data in episodes of FoG and of gait (Subj. 1—gait episodes: 20, FOG episodes: 19; Subj. 2—gait episodes: 9, FOG episodes: 8). Finally, the mean of each feature per episode was computed."
  ],
  "judge_quotes": [
   "Subject 1 had 20 freezing episodes, during turning and continuous walking (median duration: 7 s, range 1–33 s). Subject 2 had 8 freezing episodes, mainly during turning (median duration: 3.5 s, range 2–8 s).",
   "We parsed the data in episodes of FoG and of gait (Subj. 1—gait episodes: 20, FOG episodes: 19; Subj. 2—gait episodes: 9, FOG episodes: 8). Finally, the mean of each feature per episode was computed."
  ],
  "why": "正式论文明确区分了原始观察数量和后续分析纳入数量。第164行报告患者1观察到20次、患者2观察到8次冻结事件，原始观察总数为28次。第170行则报告神经分析中患者1纳入19次FOG事件、患者2纳入8次，共27次。因此，27次确实是后续分析使用的事件数量，但不是原始观察到的事件总数。报告把分析纳入数量表述为观察总数，遗漏了会改变结论的关键限定，属于误读，report_supported为no。指控者关于20+8=28次原始观察、19+8=27次分析纳入，以及报告混淆两种数量的描述均有全文明确依据。不过，全文没有提及预印本，也没有说明预印本与正式发表版本之间的关系，因此仅凭全文无法核实两者是否属于同一研究的不同发表版本，也无法判断是否应合并记录。故对指控者的整体描述评为partly。",
  "verdict": "accusation_holds"
 },
 {
  "paper": "Singh et al., 2013，Freezing of gait-related oscillatory activity in the human subthalamic nucleus",
  "pmid": "",
  "doi": "10.1016/j.baga.2012.10.002",
  "report_says": "正文第2.2节第266行讨论了该研究关于low-beta显著性的结果，但没有将其作为独立文献纳入正式参考文献表和结构化evidence表。",
  "judge_says": "该研究是关于FOG期间STN低beta振荡变化的重要原始证据。报告既然在正文使用其研究结果，就应将其纳入正式参考文献及结构化证据登记，否则正文所讨论的原始证据无法通过报告自身的知识索引追溯。",
  "source": "open_g56.json",
  "verdict": "paper_not_in_kb"
 },
 {
  "paper": "Philipp Klocke et al., 2024, Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease",
  "pmid": "39470410",
  "doi": "10.1093/brain/awae223",
  "report_says": "报告称该研究的样本量、频段和时间窗口等定量信息有限。",
  "judge_says": "原文全文实际上报告了12名患者，其中5名发生冻结，共42次冻结事件、75个Pre-FoG步态周期，并提供了8–12 Hz的STN-肌肉相干性分析结果。报告对该研究定量信息的描述不准确，遗漏了全文已经提供的具体数据。",
  "source": "open_g6.json",
  "pid": "PMID:39470410",
  "verdict": "no_fulltext"
 },
 {
  "paper": "Storzer et al., 2017, Bicycling suppresses abnormal beta synchrony in Parkinson's disease",
  "pmid": "28892573",
  "doi": "",
  "report_says": "报告将Storzer等2017年的研究描述为SIP无冻结任务，并称Freezer的相对beta功率较低。",
  "judge_says": "原文研究的是步行和骑车，而不是SIP。研究报告的一个重要结果是Freezer在运动期间出现约18 Hz的窄带活动增强，并非SIP任务中相对beta功率降低。报告混淆了实验任务、测量指标和研究发现。相对beta功率降低实际上来自Syrkin-Nikolau等2017年的另一篇研究（PMID:28890315）。",
  "source": "open_g6.json",
  "pid": "PMID:28890315",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "Subjects completed three tasks: (1) Stepping in Place 6 (SIP); (2) Forward Walking 7 (FW); (3) Turning and Barrier Course 8 (TBC), Figure 1.",
   "During the SIP task (without FOG) there was lower relative beta power in the Freezer compared to Non-Freezer groups (H(1) = 7.17, P = 0.036), which resulted in a greater attenuation of resting state beta power in Freezers (F (1, 15) = 28.37, P < 0.001).",
   "Among the eight Freezers, four exhibited freezing episodes (FEs) during FW, five during SIP, and seven during TBC.",
   "Syrkin-Nikolau Judy a Koop Mandy Miller a Prieto Thomas a Anidi Chioma a Afzal Muhammad Furqan a Velisar Anca a Blumenfeld Zack a Martin Talora a Trager Megan a Bronte-Stewart Helen a b *"
  ],
  "judge_quotes": [
   "Subjects completed three tasks: (1) Stepping in Place 6 (SIP); (2) Forward Walking 7 (FW); (3) Turning and Barrier Course 8 (TBC), Figure 1.",
   "During the SIP task (without FOG) there was lower relative beta power in the Freezer compared to Non-Freezer groups (H(1) = 7.17, P = 0.036)",
   "Among the eight Freezers, four exhibited freezing episodes (FEs) during FW, five during SIP, and seven during TBC."
  ],
  "why": "报告的实质性实验描述和结果有全文依据：这篇论文确实包含SIP任务，并明确报告Freezer在SIP无冻结时段的相对beta功率低于Non-Freezer。因此，指控者称该PMID论文研究的不是SIP、相对beta功率降低并非该研究结果，与全文不符。但是，报告存在两个需要区分的问题：第一，全文作者是Syrkin-Nikolau等人，而不是Storzer等人，因此将该结果归给Storzer缺乏全文依据；第二，SIP并非整个实验过程中都没有冻结，8名Freezer中有5名在SIP期间出现冻结发作，beta功率差异具体针对without FOG的时段。指控者关于相对beta功率结果实际来自Syrkin-Nikolau等人这一点有依据，但其关于该PMID论文研究步行和骑车、发现约18 Hz窄带活动增强的描述，不能由本篇全文支持。综上，报告的实验结果描述部分正确，但作者归属需要核对；指控者也只有部分判断得到全文支持。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Syrkin-Nikolau et al., 2017, Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease",
  "pmid": "28890315",
  "doi": "",
  "report_says": "报告将Freezer相对beta功率较低的发现归属于Storzer等2017年的研究，没有正确区分这一结果的原始文献来源。",
  "judge_says": "评委指出，相对beta功率降低的发现实际来自Syrkin-Nikolau等2017年的研究（PMID:28890315），而不是Storzer等人的研究（PMID:28892573）。两篇论文的任务范式和神经指标不同，不能将其结果互换或错误归属。",
  "source": "open_g6.json",
  "pid": "PMID:28890315",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "During the SIP task (without FOG) there was lower relative beta power in the Freezer compared to Non-Freezer groups (H(1) = 7.17, P = 0.036), which resulted in a greater attenuation of resting state beta power in Freezers (F (1, 15) = 28.37, P < 0.001).",
   "There were no differences in beta power or beta SampEn in the resting state or during FW (without FOG) between the Freezer and Non-Freezer groups.",
   "Relative alpha and beta power was calculated by dividing the summed absolute alpha or beta power by the summed power in the 40–70Hz band during the resting state, and allowed comparison across subjects, whose raw signal magnitude can vary by one or two orders of magnitude, see supplementary information."
  ],
  "judge_quotes": [
   "Subthalamic Neural Entropy is a feature of Freezing of Gait in freely moving people with Parkinson’s disease",
   "Syrkin-Nikolau Judy a Koop Mandy Miller a Prieto Thomas a Anidi Chioma a Afzal Muhammad Furqan a Velisar Anca a Blumenfeld Zack a Martin Talora a Trager Megan a Bronte-Stewart Helen a b *",
   "Subjects completed three tasks: (1) Stepping in Place 6 (SIP); (2) Forward Walking 7 (FW); (3) Turning and Barrier Course 8 (TBC), Figure 1.",
   "Synchronous STN local field potentials (LFPs), shank angular velocities, and ground reaction forces were measured in fourteen PD subjects (eight Freezers) off medication, OFF deep brain stimulation (DBS), using an investigative, implanted, sensing neurostimulator (Activa® PC+S, Medtronic, Inc.)"
  ],
  "why": "全文明确报告了Freezer相对Non-Freezer的相对beta功率降低，研究作者为Syrkin-Nikolau等人。因此，本文可以支持该结果确实出现在PMID:28890315这篇研究中，但不能仅凭本文证明Storzer等人没有报告过类似结果。另一个重要限定是，该组间差异具体出现在Stepping in Place（SIP）且没有FOG的条件下；静息状态和Forward Walking（FW）且没有FOG时，Freezer与Non-Freezer之间没有beta功率差异。如果报告将结果泛化为所有行走任务或未注明SIP条件，则缺少重要限定。对于指控者，全文支持其关于Syrkin-Nikolau等人报告了这一结果的描述，也支持该研究采用SIP、FW和TBC任务以及STN局部场电位等神经指标的描述。但是，全文没有提及Storzer等人或PMID:28892573，也没有提供另一篇论文的任务范式和神经指标，因此无法独立验证两篇论文之间的差异，也无法确认该结果并非同时出现在Storzer等人的研究中。两项判断均只能得到部分支持。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Philipp Klocke et al., 2026, Subthalamic Signatures of Freezing while Turning in Parkinson's Disease（Research Square预印本）",
  "pmid": "",
  "doi": "10.21203/rs.3.rs-9617843/v1",
  "report_says": "报告称13名PD患者中有11名具有有效神经记录，并将Pre-FoG-Turn与Pre-Reg-Turn之间低beta差异经多重比较校正后不显著作为主要结果。",
  "judge_says": "原文报告13名患者接受了STN-LFP记录，其中一名患者的一侧电极因定位问题被排除，但这不意味着只有11名患者具有有效神经记录。11名实际是出现FoG-Turn的患者数；122个含冻结的转弯来自这11名患者，而224个正常转弯来自全部13名患者。此外，Pre-FoG-Turn定义为转弯开始前3秒，而不是实际冻结发生前3秒。原文还报告，Pre-FoG-Turn相对于Standing缺乏低beta去同步化，而Pre-Reg-Turn存在相应去同步化；只有两种Pre-Turn状态直接比较时没有显著差异。报告仅突出最后一个阴性比较，容易错误地将其解释为冻结发生前神经异常不存在。该研究于2026年5月6日发布于Research Square，属于预印本，尚未经正式同行评审。",
  "source": "open_g6.json",
  "pid": "DOI:10.21203/rs.3.rs-9617843/v1",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "We recorded subthalamic local field potentials synchronized to gait kinematics in the medication-OFF and stimulation-Off state in 13 Parkinson’s disease patients with freezing of gait.",
   "We were able to confirm localization of all leads in the STN in all but one hemisphere (subject 15, left STN), which was subsequently excluded from spectral analyses.",
   "We subsequently analysed the spectral modulation and beta burst characteristics across locomotor states including 224 regular turns (n = 13), 122 turns containing freezing (n = 11), unimpaired walking (1191 gait cycles, n = 12), as well as the transition periods before initiating turning (Fig. 1).",
   "When directly comparing the frequency domain spectra of Pre FoG-Turn and Pre Reg-Turn, however, no differences were found (Fig. 3B).",
   "Numerically, Pre FoG-Turns displayed greater power (13-15 Hz) compared to Pre Reg-Turns, yet this did not reach statistical significance after correcting for multiple comparisons (P > 0.05).",
   "We found a lack of low beta band desynchronization in the time-frequency domain in Pre FoG-Turns compared to Standing, while desynchronization of the high beta (non-parametric cluster-based permutation analysis: P = 0.002) and alpha bands was preserved (P = 0.006) (Fig. 2D). Similar to Regular Walking, Pre Reg-Turns showed full attenuation of both the alpha and low- / high beta bands (non-parametric cluster-based permutation analysis: P = 0.002; Fig. 2E)."
  ],
  "judge_quotes": [
   "We recorded subthalamic local field potentials synchronized to gait kinematics in the medication-OFF and stimulation-Off state in 13 Parkinson’s disease patients with freezing of gait.",
   "We were able to confirm localization of all leads in the STN in all but one hemisphere (subject 15, left STN), which was subsequently excluded from spectral analyses.",
   "We subsequently analysed the spectral modulation and beta burst characteristics across locomotor states including 224 regular turns (n = 13), 122 turns containing freezing (n = 11), unimpaired walking (1191 gait cycles, n = 12), as well as the transition periods before initiating turning (Fig. 1).",
   "Turn transitions were studied provided our interest in pre-monitory STN activation abnormalities preceding a turn. Therefore, we analysed the 3-second epochs before turn start of either locomotor state and labelled epochs Pre Reg-Turn if preceding a Reg-Turn, and Pre FoG-Turn if preceding a FoG-Turn.",
   "We found a lack of low beta band desynchronization in the time-frequency domain in Pre FoG-Turns compared to Standing, while desynchronization of the high beta (non-parametric cluster-based permutation analysis: P = 0.002) and alpha bands was preserved (P = 0.006) (Fig. 2D). Similar to Regular Walking, Pre Reg-Turns showed full attenuation of both the alpha and low- / high beta bands (non-parametric cluster-based permutation analysis: P = 0.002; Fig. 2E).",
   "When directly comparing the frequency domain spectra of Pre FoG-Turn and Pre Reg-Turn, however, no differences were found (Fig. 3B).",
   "Numerically, Pre FoG-Turns displayed greater power (13-15 Hz) compared to Pre Reg-Turns, yet this did not reach statistical significance after correcting for multiple comparisons (P > 0.05).",
   "Posted Date: May 6th, 2026",
   "DOI: https://doi.org/10.21203/rs.3.rs-9617843/v1"
  ],
  "why": "报告的说法判定为partly。第一，报告将11人解释为具有有效神经记录的患者，没有全文依据。论文明确报告13名患者接受STN-LFP记录，因定位问题被排除的是subject 15左侧STN的一个半球，而不是整名患者。结果部分明确说明，11是出现含冻结转弯的患者人数（122 turns containing freezing, n=11）；正常转弯则来自13名患者（224 regular turns, n=13）。第二，报告所述的Pre-FoG-Turn与Pre-Reg-Turn直接比较未通过多重比较校正，确实有原文依据。因此，不能把这个阴性比较本身认定为虚构或误读。但如果将它作为主要结论，却不报告两种状态各自与Standing的比较，就遗漏了重要限定：Pre-FoG-Turn相对Standing缺乏低beta去同步化，而Pre-Reg-Turn相对Standing存在低beta去同步化。这些结果与两种Pre-Turn状态之间直接比较不显著并不矛盾，因为它们是不同的统计对比。遗漏前述结果会改变读者对研究结论的理解。此外，Pre-FoG-Turn的定义是转弯开始前3秒，而不是实际冻结开始前3秒。指控者对这些人数、时间定义及统计结果的描述均有全文依据。不过，指控者关于报告仅突出某一结果的判断，仍取决于报告本身的实际内容，不能单独由论文验证。指控者关于预印本及尚未经正式同行评审的说法也需要保留限定：全文列出了2026年5月6日的Posted Date和v1 DOI，但没有明确声明其同行评审状态。因此，指控者的核心论文解读得到支持，但其出版状态的完整表述不能仅凭全文确认，判定为partly。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease",
  "pmid": "40677701",
  "doi": "10.1101/2024.06.26.24309418",
  "report_says": "报告在H12中称，目前aDBS研究尚未真正区分beta特异性反馈与动态刺激时序效应，并将beta burst触发、随机触发、周期触发和运动学触发之间的比较作为未来尚待开展的关键实验。",
  "judge_says": "2025年已经发表的这项研究实际纳入7名患者，通过双盲实验比较了beta burst驱动aDBS、连续DBS和随机自适应刺激。三种开启刺激条件相较OFF均改善了冻结时间比例，但开启条件之间没有显著差异。转弯和障碍物任务中实际出现冻结的患者只有3名。该研究已经开展了报告称尚未开展的关键比较。报告没有正确整合这一已发表的直接对照实验，也没有讨论其未发现beta反馈额外优势的结果及其样本量限制。",
  "source": "open_g6.json",
  "pid": "PMID:40677701",
  "report_supported": "partly",
  "judge_supported": "yes",
  "report_quotes": [
   "Participants were tested OFF DBS and on three stimulation conditions: cDBS, aDBS and randomly adapting DBS (rDBS). During cDBS stimulation amplitude is held constant, whereas during rDBS stimulation amplitude varies randomly using the same ramp rate and therapeutic window as aDBS. The pattern of rDBS was determined by randomly shuffling the adaption pattern observed during the calibration aDBS runs to maintain similar total electrical energy delivered (TEED) and patterns of adaption but unlinking it with the beta biomarker.",
   "It is worth noting that the majority of previous work examining the effects of aDBS, outside of the initial Little et al.27 2013 publication, have not included any control condition where stimulation varies in a random fashion unlinked to a biomarker. Such an inclusion is crucial for better understanding the effects of aDBS. Here we found that, at the group level, the randomly adapting DBS performed similarly compared to cDBS and aDBS despite being uncoupled to the biomarker of interest.",
   "aDBS did not exhibit superior performance compared to cDBS.",
   "Only seven individuals were tested due to the discontinuation of the Summit™ RC + S."
  ],
  "judge_quotes": [
   "In a double-blind design, participants performed a harnessed stepping-in-place task, a free walking turning and barrier course, instrumented measures of bradykinesia and clinical motor assessments in four conditions: OFF stimulation, on adaptive, continuous or randomly adapting deep brain stimulation.",
   "Overall, there was a significant effect of stimulation condition on percent time freezing (F(3,27) = 4.73, P = 0.0089, ηp2 = 0.34; Fig. 5). Post-hoc pairwise comparisons showed significant reductions compared to OFF stimulation for aDBS (t = 2.95, P = 0.031) cDBS (t = 3.25, P = 0.013), and rDBS (t = 3.52, P = 0.0080). No difference was observed between ON stimulation conditions (aDBS–cDBS: t = 0.47, P = 0.97; aDBS–rDBS: t = 0.70, P = 0.90; cDBS–rDBS: t = 0.24, P = 1.00).",
   "Two participants did not perform the turning and barrier course.",
   "Two of the three participants who demonstrated freezing in the OFF condition showed improvements in freezing for aDBS and cDBS. The two other participants showed no freezing across any conditions.",
   "Only seven individuals were tested due to the discontinuation of the Summit™ RC + S.",
   "The current study only tested the acute effects of aDBS. It is unknown from the current study whether there would be additional benefit if on the controller for longer than the 2 h tested here."
  ],
  "why": "报告的说法只能判定为部分有依据。关键问题在于，论文已经直接开展了beta burst驱动aDBS与随机自适应DBS（rDBS）的对照。rDBS并非简单关闭反馈，而是将校准阶段观察到的aDBS刺激调整模式随机打乱，在保持相近总电能、治疗窗口和调整模式的同时，使刺激调整与beta生物标志物脱钩。这正是检验beta特异性反馈是否具有超出动态刺激调整本身的额外效果的重要对照。研究发现，aDBS、cDBS和rDBS组间没有显著差异，论文明确指出随机自适应刺激在组水平上表现相似，且aDBS没有优于cDBS。因此，将beta burst与随机自适应刺激的比较描述为尚未开展的未来实验，遗漏了已经发表的直接证据。不过，论文没有比较周期触发或运动学触发刺激，因此这两类比较仍然可以作为未来研究方向。指控者对研究设计、主要结果和样本量的描述有全文依据。具体而言，转弯和障碍物任务中，三种开启刺激条件相较OFF均显著降低冻结时间比例，开启条件之间没有显著差异；该任务只有5名患者完成，其中3名在OFF条件下出现冻结，另外2名在所有条件下均未冻结。另需限定的是，在另一项原地踏步任务中，rDBS相较OFF仅达到统计学趋势（P=0.062），并非显著改善。研究总样本量为7人，且仅测试急性效果，论文明确将这些情况列为研究局限。因此，指控者的核心判断成立，但三种刺激均显著改善冻结时间这一结论应限定于转弯和障碍物任务。",
  "verdict": "accusation_partly"
 },
 {
  "paper": "STN-SNr联合刺激急性随机交叉试验（PMID:39957196）",
  "pmid": "39957196",
  "doi": "",
  "report_says": "报告第2.8节将急性双盲研究描述为10名患者参与，并称未发现联合刺激具有明确的额外优势；引用PMID:35490252、37104542、42860886、42909654和42968793。",
  "judge_says": "对应的原始急性随机交叉试验实际报告有15名患者至少接受过一种联合刺激条件，而不是10名。该研究确实没有发现STN-SNr联合刺激在NFOG-Q上相较STN-only具有统计学显著优势。报告引用的PMID:35490252对应综述，PMID:37104542对应计算模型研究，并非这项急性临床试验的原始论文。因而存在样本量错报和一手文献引用错误。",
  "source": "open_g6.json",
  "pid": "PMID:39957196",
  "report_supported": "partly",
  "judge_supported": "partly",
  "report_quotes": [
   "Fifteen patients received at least one combined stimulation.",
   "The change of the NFOG-Q score showed no significant difference between S and C1 (16.8 ± 7.9 vs. 16.6 ± 9.0, respectively; p = 0.64) or between S and C2 (16.8 ± 7.9 vs. 15.7 ± 8.5, respectively; p = 0.19) (Table 2, Figure 1).",
   "We found a significant improvement of motor complications (MDS-UPDRS part IV) with the combined STN-SNr stimulation, both comparing C1 vs. S (3.6 ± 3.8 vs 4.9 ± 3.8; p = 0.047) and C2 vs. S (2.7 ± 3.1 vs 4.9 ± 3.8; p = 0.006) (Table 2, Figure 2).",
   "Sleep quality (PDSS-2 scale) showed an improvement in C1 vs. S (13.6 ± 7.6 and 16.6 ± 8.2; p = 0.04) but not in C2 vs. S (16.2 ± 9.4 and 16.6 ± 8.2; p = 0.95) (Table 2).",
   "Our study did not prove a statistically significant improvement in NFOG-Q with STN-SNr stimulation; however, one-third of patients experienced a clinically meaningful FoG improvement, and the majority preferred to maintain STN-SNr stimulation."
  ],
  "judge_quotes": [
   "A total of 16 PD patients have been recruited and randomized in the two centers (6 at the Turin center and 10 at the Toulouse center). One patient did not tolerate either C1 or C2 stimulation parameters due to a severe resting tremor suddenly appearing few seconds after parameter changes and was excluded from efficacy data analysis (mITT population).",
   "Thus, data are presented for the 15 patients (13 males and 2 females) who received at least one combined stimulation setting.",
   "The change of the NFOG-Q score showed no significant difference between S and C1 (16.8 ± 7.9 vs. 16.6 ± 9.0, respectively; p = 0.64) or between S and C2 (16.8 ± 7.9 vs. 15.7 ± 8.5, respectively; p = 0.19) (Table 2, Figure 1).",
   "All patients received in a different order for a total study period of 3 months: 1) one month of HF STN-DBS (“S”); 2) one month of combined HF stimulation of the STN and SNr at 130 Hz (“C1”); 3) one month of combined HF stimulation of the STN and LF stimulation of the SNr at 60 Hz (“C2”).",
   "A cross-over, double-blind, randomized controlled clinical trial on 12 PD patients showed FoG improvement with the combined stimulation of STN and SNr at HF, using a scoring based on a single course assessment; similar to our study, a substantial proportion of patients (10 out of 12) expressed a preference for continuing the combined stimulation over standard STN stimulation."
  ],
  "why": "报告的说法只有部分成立。首先，样本量10人没有本文依据。本文主试验共随机16人，其中1人因不能耐受刺激而被排除在疗效分析之外，最终15人至少接受过一种联合刺激条件。其次，报告关于联合刺激没有明确额外优势的说法，在主要结局NFOG-Q上有依据：C1与标准STN刺激比较p=0.64，C2比较p=0.19，均无统计学显著差异。但如果将这一结论扩大为联合刺激在所有临床结局上都没有额外优势，则不准确，因为本文报告了运动并发症的显著改善，以及C1条件下睡眠质量的显著改善。因此，必须限定为FoG的NFOG-Q主要结局。指控者的说法也只有部分成立：15人至少接受一种联合刺激，以及NFOG-Q未达到统计学显著差异，均有明确全文依据。不过，本文的15人研究并非急性试验，其每种刺激条件持续一个月，总研究期为三个月。讨论部分另外提到一项既往交叉、双盲随机临床试验，该试验有12名患者，其中10人是表达继续接受联合刺激偏好的人数，而不是试验总样本量。这两个研究不能混为一谈。此外，附件全文没有提供PMID:35490252、37104542、42860886、42909654和42968793与具体参考文献条目的对应信息，因此无法仅凭这篇全文核实其中哪些是综述、计算模型研究，或判断报告是否存在一手文献引用错误。综合而言，报告关于样本量的表述有误，但关于NFOG-Q未显示统计学显著优势的表述有依据；指控者正确识别了15人和主要结局结果，但对急性试验的样本量及PMID引用错误的判断，不能全部由本篇全文证实。",
  "verdict": "accusation_partly"
 }
]

===== bodycheck.json =====
{
 "citations": [
  {
   "cite": "PMID:24165197",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:24361601",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:28890315",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:28892573",
   "verdict": "not_in_kb_exists",
   "real_title": "Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia."
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
   "cite": "PMID:31505548",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:32155442",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:32634599",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:33368872",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:35490252",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:36070366",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:37104542",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:37842127",
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
   "cite": "PMID:38391752",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39229492",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39295169",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39464215",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39470410",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39475137",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:39606789",
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
   "cite": "PMID:42098512",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42239677",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42571859",
   "verdict": "in_kb"
  },
  {
   "cite": "PMID:42829632",
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
   "cite": "PMID:42968793",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.1101/2024.06.26.24309418",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.1101/2025.01.10.632393",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.1101/2025.04.22.650006",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "in_kb"
  },
  {
   "cite": "DOI:10.64898/2026.08.13.744293",
   "verdict": "in_kb"
  }
 ],
 "possible_mismatch": []
}

===== blind_S2_vs_S3c.json =====
[
 {
  "seat": "aX",
  "judge": "g6",
  "better": "S3c",
  "items": {
   "coverage": "S3c",
   "evidence": "S3c",
   "synthesis": "S3c",
   "structure": "S3c",
   "rigor": "S3c"
  },
  "why": "Y更好地完成了研究任务。决定性优势不是篇幅，而是它更集中地回答了STN神经活动究竟如何与实际FOG事件关联这一核心问题，并建立了从患者易感性、冻结前变化、实际冻结到恢复阶段的证据框架。它对局部beta动力学、皮层-STN通信、步态周期协调、感觉运动反馈及分布式网络机制之间的竞争关系进行了更细致的分析，同时提出了具有可区分预测和反证条件的机制模型。其证据数据库和结论层级也更适合持续更新及后续研究复用。X的主要优势是临床DBS治疗证据更加系统，尤其是低频刺激、刺激空间定位、STN+SNr和TBS-DBS的比较，并且保留了Y遗漏的Liu等2022年直接电生理研究。因此，X并非低质量报告。但就研究问题的针对性、证据分层、机制综合和科学严谨性而言，Y具有整体优势。Y仍应补入Liu等2022年研究，并进一步核查不同研究版本和队列重叠，才能形成更完整的证据体系。"
 },
 {
  "seat": "aX",
  "judge": "g56",
  "better": "S3c",
  "items": {
   "coverage": "S3c",
   "evidence": "S3c",
   "synthesis": "S3c",
   "structure": "S3c",
   "rigor": "S3c"
  },
  "why": "Y总体上更好地完成了研究任务。决定性优势不是篇幅或引用数量，而是它更准确地把握了核心科学问题：STN神经活动与FOG的关系必须同时从患者易感性、事件发生前、实际冻结、恢复及神经调控因果性几个层面理解。Y对直接人体电生理证据的分析更细致，对beta方向冲突、burst时间结构、皮层-STN通信和步态周期协调的综合更有解释力，并提出了14组具有区分性预测和反证条件的机制模型。它还建立了较完整的证据—发现—综合结论—机制—假说知识结构。不过，Y并非没有缺陷：应补入Liu等2022年（PMID:35310098）的同步STN-LFP/ECoG研究，并吸收X对DBS术后步态恶化、刺激空间定位及PMC-STN alpha耦合代偿与病理竞争解释的部分内容。X在临床DBS治疗策略和知识更新流程方面有值得保留的优势，但整体而言，Y在直接证据处理、冲突解释、知识分层和科学严谨性方面表现更好，因此判定Y胜出。"
 },
 {
  "seat": "bX",
  "judge": "g6",
  "better": "S3c",
  "items": {
   "coverage": "S3c",
   "evidence": "S3c",
   "synthesis": "S3c",
   "structure": "S2",
   "rigor": "S3c"
  },
  "why": "综合判断，X更好地完成了研究任务。决定性优势不是篇幅或文献数量，而是它更深入地处理了研究问题的核心：STN神经活动究竟是FOG的局部致病驱动、分布式网络失调的表现，还是运动状态和任务负荷变化的伴随信号。X在直接事件证据的分层、研究冲突的解释、竞争性机制的提出、反证条件及因果实验设计方面整体更成熟。Y在知识层级表达、竞争性假说的成对组织以及Liu等2022年直接电生理研究的覆盖方面具有明确优势，值得保留。X的主要改进方向是补入该项遗漏研究，进一步核查不同论文之间的患者队列重叠，并加强预印本与正式发表版本的独立性审计。总体上，X更接近一套能够持续更新、检验机制并指导后续功能神经外科研究的证据综合体系。"
 },
 {
  "seat": "bX",
  "judge": "g56",
  "better": "S3c",
  "items": {
   "coverage": "S3c",
   "evidence": "S3c",
   "synthesis": "S3c",
   "structure": "S3c",
   "rigor": "S3c"
  },
  "why": "总体选择X。决定性优势不是篇幅或单纯的文献数量，而是它更好地完成了研究问题最重要的工作：将STN局部神经动力学、实际冻结事件、步态周期、皮层-STN通信和分布式运动网络放在同一证据框架中，解释为什么不同研究会出现相反结果，并将这些矛盾转化为可检验的竞争性机制。X的证据数据库也更适合后续长期积累、检索和重新评价。不过，X并非完全胜任：需要补入Liu等2022年的直接事件级研究，进一步整合2025年阴性网络Meta分析的结果，并真正开展独立文献检索。Y值得保留的内容包括其对DBS刺激频率、解剖定位、STN+SNr联合刺激及PMC-STN alpha耦合竞争机制的分析。最合理的后续改进方向是以X的证据数据库和知识关联体系为基础，吸收Y在临床干预证据及竞争性机制比较方面的优点。"
 }
]

===== 盲比原文 blind_S2_vs_S3c_aX_g56_87c8d2c0（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "Y",
      "why": "Y对核心研究方向的覆盖更全面，尤其是自然行走中的实际冻结事件、STN-LFP、MUA、EMG、步态启动、步态周期锁定、皮层-STN通信、感觉运动整合、脑干网络、神经影像及机器学习预测。还覆盖动物模型、患者亚型及不同神经调控策略。X在临床DBS疗效、刺激频率、STN空间定位、STN+SNr及TBS方面有更详细的讨论，并包含Y遗漏的重要直接研究Liu等2022（PMID:35310098），即8名患者同步记录STN-LFP、ECoG和实际冻结事件的研究。X在部分刺激位置和术后步态恶化研究方面也有独特覆盖。但总体而言，Y对STN-FOG相关电生理及交叉机制的覆盖更广，且纳入了更多2024—2026年的相关研究。优势不是单纯来自文献数量，而是涉及了更多不同的研究问题和证据类型。"
    },
    "evidence": {
      "better": "Y",
      "why": "Y的证据提取更细致。其证据记录能够区分独立患者数、冻结事件数、试次数、药物状态、刺激状态、任务范式、记录位置、冻结阶段、神经指标及研究局限。尤其是对Thenaisie等2022年研究（PMID:36070366），Y不仅记录4名实际发生FOG的患者及173次冻结事件，还识别了患者编号P3/P4不一致、不同患者的信号显著性差异，以及事件数量与严重程度之间缺少正式统计验证等问题。Y还明确指出2026年熵研究重新分析既有数据，不能作为独立队列重复验证。X同样具有结构化证据表，且其全文证据比例较高，并保留了Y遗漏的Liu等2022年研究。不过，X将PMID:36070366对应的正式发表研究与未同行评审预印本状态混写，存在文献版本对应问题。Y的不足是部分记录仅依据摘要，且部分样本量字段未填写，仍需全文核验。总体上，Y的证据可追溯性、实验条件还原能力及局限识别能力更强。"
    },
    "synthesis": {
      "better": "Y",
      "why": "Y对研究冲突的解释更深入，尤其是区分患者间FOG易感性、后续发生FOG的步态启动试次、冻结前、实际冻结及恢复阶段。一个突出优势是对Syrkin-Nikolau等2017年研究的重新解释：冻结期间beta降低的比较涉及TBC冻结与FW无冻结的不同任务，而Non-Freezer在没有冻结时也可能出现TBC相关beta下降，因此不能简单认定beta降低是FOG特异性现象。Y还区分平均burst duration与长burst比例、局部功率与跨区域耦合、平均频谱与步态相位调制，并讨论队列重叠、重复数据分析和统计伪重复问题。X也有较好的九类冲突归纳，并提出PMC-STN alpha耦合的代偿性与病理性两种解释，以及低频刺激的局部振荡与脑干通路两种机制。但Y对具体研究条件与相反结果之间的联系分析更充分，也更清楚地指出哪些矛盾尚不能裁决。"
    },
    "structure": {
      "better": "Y",
      "why": "Y的知识结构更贴近任务要求的五层关系。证据表保存原始研究及实验条件；Claims进一步区分finding、synthesis和mechanism；Hypotheses再将机制解释转化为可检验预测。各层之间通过Evidence ID、Claim ID和Hypothesis ID建立支持、限定及反对关系。其33项结论和14项假说形成了较完整的证据映射。X的四层Evidence-Claims-Mechanisms-Hypotheses模型也很清晰，并通过关系图和版本更新规则体现了良好的知识组织能力。但X的Claims层没有像Y一样明确区分单项研究发现与跨研究综合结论，部分知识层级仍然合并。Y在层级区分及证据关系表达方面略胜。"
    },
    "rigor": {
      "better": "Y",
      "why": "Y对相关性、时间先后关系和因果性的区分更严格。它明确采用A/B/C证据分类，区分自然实际冻结、原地踏步、虚拟现实模拟、步态启动易感性和静息态关联，并反复强调事件数不等于独立患者数。对2025年步态启动研究，Y指出随后发生FOG的试次不能直接等同于冻结前即时触发信号；对2026年冻结转弯研究，指出Pre-FoG与Pre-Regular-Turn之间的低beta差异未通过多重比较校正。它还讨论了研究队列重叠、预印本与正式发表版本、算法跨患者泛化、假阳性和冻结后识别等问题。假说部分为不同机制提供了具体预测和反证条件，避免将网络模型或临床DBS疗效当作局部STN活动的因果验证。X同样有较强的科学谨慎性，尤其明确区分刺激干预证据与内源性神经活动证据，并为假说设置反证条件。但其部分跨任务比较的混杂解释、数据再分析问题及文献版本核对不如Y充分。"
    }
  },
  "better": "Y",
  "why": "Y总体上更好地完成了研究任务。决定性优势不是篇幅或引用数量，而是它更准确地把握了核心科学问题：STN神经活动与FOG的关系必须同时从患者易感性、事件发生前、实际冻结、恢复及神经调控因果性几个层面理解。Y对直接人体电生理证据的分析更细致，对beta方向冲突、burst时间结构、皮层-STN通信和步态周期协调的综合更有解释力，并提出了14组具有区分性预测和反证条件的机制模型。它还建立了较完整的证据—发现—综合结论—机制—假说知识结构。不过，Y并非没有缺陷：应补入Liu等2022年（PMID:35310098）的同步STN-LFP/ECoG研究，并吸收X对DBS术后步态恶化、刺激空间定位及PMC-STN alpha耦合代偿与病理竞争解释的部分内容。X在临床DBS治疗策略和知识更新流程方面有值得保留的优势，但整体而言，Y在直接证据处理、冲突解释、知识分层和科学严谨性方面表现更好，因此判定Y胜出。"
  }
}</escape>

===== 盲比原文 blind_S2_vs_S3c_aX_g6_87c8d2c0（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "Y",
      "why": "Y覆盖的研究方向更广，尤其加强了自然行走中的实际冻结事件、STN局部电生理、皮层-STN通信、STN-肌肉协调、步态周期编码、感觉运动整合、脑干网络、神经复杂度及机器学习预测等交叉方向。参考文献和结构化证据也更丰富。不过，Y遗漏了Liu等2022年8名患者的同步STN-LFP、皮层ECoG和步态记录研究，该研究发现实际冻结期间STN beta功率升高，是重要的直接证据；X纳入了这项研究。X在60/130 Hz刺激比较、刺激位置、STN+SNr及TBS-DBS临床证据方面也更详细。因此Y总体覆盖更好，但并非没有重要遗漏。【turn560248search0】"
    },
    "evidence": {
      "better": "Y",
      "why": "Y的证据登记更细致，能够区分独立患者数、冻结事件数、任务试次数、冻结易感性、冻结前、实际冻结及恢复阶段，并记录药物状态、刺激状态、频段、记录位置、统计指标和研究局限。它还明确区分原始研究、二级文献、预印本及正式发表版本，并将证据与具体结论的支持或限定关系关联起来。X同样具有较详细的原始文献证据表，但存在可核查的文献状态错误：将PMID:36070366对应的Thenaisie等2022年Sci Transl Med正式发表研究标记为未经同行评审的medRxiv预印本；其预印本实际上具有另一个DOI（10.1101/2022.02.08.22270370）。这削弱了X的文献追溯可靠性。【turn421858view0】【turn104057search0】需要指出，Y仍有较多仅依据摘要提取的证据，也存在预印本与正式发表版本可能重复登记的问题。"
    },
    "synthesis": {
      "better": "Y",
      "why": "Y对核心科学矛盾的分析更深入。它不仅解释beta功率升高与降低的冲突，还区分患者间易感性与患者内事件变化、自然步行与SIP、冻结前与冻结期间、平均功率与burst时间结构、局部振荡与跨区域耦合。尤其有价值的是，Y注意到2026年转弯研究中，相对于站立基线出现的低beta异常，并未在Pre-FoG-Turn与Pre-Regular-Turn的直接比较中获得校正后的显著差异。这避免了将基线比较误解为冻结预测证据。Y还把任务负荷、运动学反馈、感觉运动整合和分布式网络失调作为竞争性解释，并提出相应反证条件。X的临床刺激疗效冲突分析更详尽，但对直接电生理研究之间的细粒度比较不及Y。"
    },
    "structure": {
      "better": "Y",
      "why": "Y的知识分层更完整。其结构化附录明确区分finding（单项研究发现）、synthesis（跨研究综合结论）和mechanism（机制模型），再与独立的H1-H14假说关联。证据记录还具有支持、限定等关系，便于检索特定结论的原始依据、反对证据及适用条件。Y进一步建立了研究版本、潜在队列重叠、证据更新触发条件和假说反证条件的管理机制。X也提出了Evidence、Claims、Mechanisms、Hypotheses四层结构，并且在质量控制流程和新证据触发旧结论更新方面有较好的设计；但其结构化结论主要分为synthesis和mechanism，缺少Y明确设置的单项研究发现层。因此，Y更适合长期积累和跨问题复用。"
    },
    "rigor": {
      "better": "Y",
      "why": "Y对科学不确定性的处理更加严格。它反复区分直接事件证据、易感性关联和间接干预证据，明确指出DBS治疗有效不能证明某种STN内源性振荡具有因果作用。它特别重视患者数与事件数的区别、重复测量伪重复、研究队列重叠、预印本与正式发表版本的关系、运动学混杂、任务匹配、阴性结果和多重比较校正。对于机器学习研究，还区分冻结事件检测、提前预测、冻结后识别及跨患者泛化，并提出独立患者验证和误报率等要求。X也有良好的因果性限定、反证条件和数据质量检查，但其部分文献状态错误及对个别研究独立性处理不够充分，使其整体严谨性略逊于Y。需要强调，两份报告都没有将提出的机制模型误称为已经完成实验验证的因果机制，但Y对这种界限的落实更加系统。"
    }
  },
  "better": "Y",
  "why": "Y更好地完成了研究任务。决定性优势不是篇幅，而是它更集中地回答了STN神经活动究竟如何与实际FOG事件关联这一核心问题，并建立了从患者易感性、冻结前变化、实际冻结到恢复阶段的证据框架。它对局部beta动力学、皮层-STN通信、步态周期协调、感觉运动反馈及分布式网络机制之间的竞争关系进行了更细致的分析，同时提出了具有可区分预测和反证条件的机制模型。其证据数据库和结论层级也更适合持续更新及后续研究复用。X的主要优势是临床DBS治疗证据更加系统，尤其是低频刺激、刺激空间定位、STN+SNr和TBS-DBS的比较，并且保留了Y遗漏的Liu等2022年直接电生理研究。因此，X并非低质量报告。但就研究问题的针对性、证据分层、机制综合和科学严谨性而言，Y具有整体优势。Y仍应补入Liu等2022年研究，并进一步核查不同研究版本和队列重叠，才能形成更完整的证据体系。"
}</escape>

===== 盲比原文 blind_S2_vs_S3c_bX_g56_c81368a7（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "X",
      "why": "X覆盖的研究方向更广，也更贴近STN神经活动与FOG的核心问题。除自然冻结事件、Freezer/Non-Freezer差异和beta burst外，还系统涉及皮层-STN通信、STN-肌肉协调、theta/alpha/gamma、神经复杂度、感觉运动整合、脑干及小脑网络、患者亚型、闭环DBS和预测模型。其结构化数据库包含233条参考文献和933条证据记录，Y分别为150条和538条；这不是简单的篇幅优势，而是涉及更多独立研究和交叉方向。不过，X遗漏了重要的Liu等2022年研究（PMID:35310098）：该研究同步记录8名患者的STN-LFP、皮层ECoG及步态，观察到实际冻结期间STN beta功率升高，Y对此有明确讨论【turn725827search0】。X还明确说明没有引入外部文献，因此没有充分证明完成了独立主动检索。Y在临床DBS疗效、低频刺激和刺激位置方面的覆盖更完整。综合研究方向及证据广度，仍判X更好。"
    },
    "evidence": {
      "better": "X",
      "why": "X的证据追溯和原始研究条件记录明显更完善。其证据记录系统区分患者数、冻结事件数、试次数和信号窗口，并记录研究设计、药物状态、刺激状态、任务、记录位置、信号指标、具体发现、局限及证据来源是摘要还是全文。尤其值得肯定的是，X明确识别了2026年beta burst熵研究对2022年Thenaisie数据的二次分析，没有把它误当成独立队列重复验证。Y也提供了不少可靠的原始研究细节，且补充了X遗漏的Liu研究，但存在具体的文献状态错误：将PMID:36070366标注为尚未同行评审的medRxiv预印本，而该PMID对应的实际文献已经发表于2022年Science Translational Medicine【turn225843view0】。Y的结构化证据中还存在至少一个无法对应的证据ID。X在证据标准化、可追溯性及来源核查方面更可靠。"
    },
    "synthesis": {
      "better": "X",
      "why": "X对研究冲突的解释更深入，尤其是把患者间易感性、患者内冻结事件、冻结前、冻结中及恢复阶段分开，避免将不同研究的beta结果简单合并。它进一步区分平均功率、相对功率、beta burst持续时间、burst分布、ERD、coherence和复杂度等不同构念，并系统分析任务差异、运动学混杂、药物状态、统计伪重复、队列重叠及结局指标不一致。X提出14项机制假说，分别提供区分性预测、反证条件和实验方案。Y的优势是对60 Hz与高频刺激、STN空间定位，以及PMC-STN alpha耦合的代偿性与病理性解释进行了更明确的竞争性分析；也讨论了阴性网络Meta分析与阳性Meta分析之间的冲突【turn354174search1】。但就STN局部活动与实际FOG事件的综合解释而言，X的时间阶段和方法学分析更完整。"
    },
    "structure": {
      "better": "X",
      "why": "X建立了更适合长期检索和更新的知识结构。其JSON数据库明确区分单项研究发现、跨研究综合结论和机制模型，并通过稳定的Evidence ID、Claim ID和Hypothesis ID建立关联。33条结论包含证据支持、反对关系及不确定性说明，14项假说进一步关联具体结论、预测和反证条件。15项研究缺口还提供了后续检索方向。Y的四层知识结构（Evidence、Claims、Mechanisms、Hypotheses）在正文中的图示和解释更直观，也明确展示了从原始证据到机制假说的推导关系。但其结构化证据分类和关联的标准化程度不及X。考虑到长期积累、跨问题复用及新证据触发旧结论更新，X更有优势。"
    },
    "rigor": {
      "better": "X",
      "why": "X对科学不确定性的处理更加系统。它明确区分直接事件证据、易感性关联和间接干预证据，反复强调相关性不等于因果性，并专门处理患者数与事件数的区别、伪重复、队列重叠、预印本与正式发表版本、二次数据分析及不同FOG结局之间的不可互换性。其竞争性假说还明确规定了什么结果能够支持或反驳相应机制，而不是把网络模型的合理性当成实验验证。Y同样具有较强的科学谨慎性，尤其注意临床DBS改善与内源性STN神经活动之间的因果区别。不过，前述Thenaisie文献发表状态错误，以及部分证据关联缺陷，降低了其整体严谨性。X也有不足：部分最新研究仍属于预印本，且其主动检索范围没有得到充分证明。两份报告都提出了持续改进流程，但都没有实际展示多轮自主修正及改进效果的验证。"
    }
  },
  "better": "X",
  "why": "总体选择X。决定性优势不是篇幅或单纯的文献数量，而是它更好地完成了研究问题最重要的工作：将STN局部神经动力学、实际冻结事件、步态周期、皮层-STN通信和分布式运动网络放在同一证据框架中，解释为什么不同研究会出现相反结果，并将这些矛盾转化为可检验的竞争性机制。X的证据数据库也更适合后续长期积累、检索和重新评价。不过，X并非完全胜任：需要补入Liu等2022年的直接事件级研究，进一步整合2025年阴性网络Meta分析的结果，并真正开展独立文献检索。Y值得保留的内容包括其对DBS刺激频率、解剖定位、STN+SNr联合刺激及PMC-STN alpha耦合竞争机制的分析。最合理的后续改进方向是以X的证据数据库和知识关联体系为基础，吸收Y在临床干预证据及竞争性机制比较方面的优点。"
}</escape>

===== 盲比原文 blind_S2_vs_S3c_bX_g6_c81368a7（X/Y 见文件名 aX=前者在 X 位）=====
<escape>{
  "items": {
    "coverage": {
      "better": "X",
      "why": "X对研究领域的覆盖更广，尤其是自然行走实际FOG事件、STN局部beta及非beta活动、MUA、STN-肌肉协调、皮层-STN通信、步态周期调制、神经复杂度、患者亚型、DBS空间定位、SNr联合刺激、自适应DBS及FOG预测。X还纳入了脑干、小脑、感觉运动整合和动物模型等交叉方向。Y的临床DBS疗效及低频刺激证据覆盖较好，而且补充了X遗漏的重要直接研究：Liu等2022年同步STN-LFP、皮层ECoG和步态研究，纳入8名患者、41次步行测试，其中30次出现冻结，21次达到较高数据质量，报告冻结期间STN beta功率升高。该遗漏是X在核心证据覆盖上的明显缺陷。 但综合研究方向的广度、近年研究覆盖及交叉领域整合，X仍然更好。"
    },
    "evidence": {
      "better": "X",
      "why": "X的证据追溯体系更细致。其结构化附录将原始文献、具体实验设计、独立患者数、冻结事件数、药物和刺激状态、任务范式、记录位置、信号指标、结果及研究局限逐条对应，并保留原文引语和证据来源类型。尤其重视患者数与事件数的区别，以及平均功率、相对功率、ERD、burst duration、burst分布和coherence之间的不可互换性。X还区分直接事件证据、易感性证据和间接干预证据，并指出二次分析不能视为独立队列重复验证。Y也具有较好的结构化原始证据表，且补充了Liu等2022年的直接研究，但部分研究的实验条件和定量结果在正文中没有得到同等充分的展开。X的优势不是证据条目数量本身，而是证据细节、来源追溯和结论映射的完整程度。"
    },
    "synthesis": {
      "better": "X",
      "why": "X对研究冲突的综合更深入。它不仅分析beta升高与降低的矛盾，还分别处理任务差异、冻结前后时间阶段、频段边界、平均功率与burst分布、患者间与患者内效应、运动学混杂、队列重叠及临床量表与实际冻结事件之间的构念差异。尤其重要的是，X将局部beta动力学、皮层-STN低频通信、步态周期协调、感觉反馈、动作选择、分布式网络和患者易感状态纳入统一框架，并提出14项包含具体预测和反证条件的机制假说。其多模态事件级研究、运动学匹配对照和等剂量闭环DBS实验设计具有较强的机制判别价值。Y的优势是H1/H2、PMC-STN alpha代偿与病理性过耦合、低频刺激局部机制与脑干通路机制等竞争关系划分得更明确。但整体而言，X对冲突来源、替代解释和后续实验的整合更全面。"
    },
    "structure": {
      "better": "Y",
      "why": "Y的知识分层表达更明确。它明确建立原始证据、研究结论、机制模型和可检验假说四层结构，并通过具体示例解释从单项研究发现到跨研究结论、机制解释和因果验证假说的转换。还使用关系图表示证据、结论和假说之间的支持关系，并建立新证据触发旧结论重新评价的规则。X同样具有较完善的结构化附录，包括233条文献记录、933条证据记录、33项结论或机制条目、14项假说及15项研究缺口，并区分synthesis和mechanism层级。但其正文中的知识层次主要以证据、研究、结论和假说展开，对单项研究发现与跨研究结论之间的独立层次表达不如Y直观。因此，Y在知识层级的可理解性和关系展示方面略胜，X则在知识索引的细粒度和记录规模方面更有优势。"
    },
    "rigor": {
      "better": "X",
      "why": "X在科学推断边界和方法学问题识别方面更严格。它明确区分患者间易感性、患者内事件关联和神经调控因果性，采用A/B/C证据等级，并特别强调N患者不等于N冻结事件、不等于N试次或N信号窗口。对冻结前、冻结中和恢复阶段分别分析，避免把事件发生后的信号变化解释为提前触发机制。它还区分相关性、预测能力与因果干预，讨论伪重复、患者队列重叠、二次数据分析、多重比较及机器学习假阳性，并提出患者级外部验证和等剂量刺激对照。联网核对还发现一个两份报告均未充分处理的问题：2024年Klocke研究与2026年Klocke转弯冻结预印本的受试者编号显示，至少存在12名患者重叠，因此不能简单将两者视为独立队列重复验证。 X虽然专门讨论了队列重叠问题，但仍遗漏了这一具体重叠，说明其证据独立性审计尚不完整。Y也正确强调相关性不等于因果性，但在统计单位、数据复用和预测模型误报方面的讨论不如X充分。另外，两份报告都主要提出持续改进流程和评价指标，并未真正展示一个经过多轮实施、验证和修正的自主改进闭环。"
    }
  },
  "better": "X",
  "why": "综合判断，X更好地完成了研究任务。决定性优势不是篇幅或文献数量，而是它更深入地处理了研究问题的核心：STN神经活动究竟是FOG的局部致病驱动、分布式网络失调的表现，还是运动状态和任务负荷变化的伴随信号。X在直接事件证据的分层、研究冲突的解释、竞争性机制的提出、反证条件及因果实验设计方面整体更成熟。Y在知识层级表达、竞争性假说的成对组织以及Liu等2022年直接电生理研究的覆盖方面具有明确优势，值得保留。X的主要改进方向是补入该项遗漏研究，进一步核查不同论文之间的患者队列重叠，并加强预印本与正式发表版本的独立性审计。总体上，X更接近一套能够持续更新、检验机制并指导后续功能神经外科研究的证据综合体系。"
}</escape>