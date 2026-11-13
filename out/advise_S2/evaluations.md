===== S2 / open_g6.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "研究覆盖缺少可复现的文献检索与筛选方法，无法证明报告真正完成了系统性证据搜集。这是最根本的结构性问题。",
   "where": "第1节：\"证据范围：以用户提供的结构化知识及 evidence_table.txt 中的原始文献证据为基础。覆盖临床DBS疗效、STN局部场电位（LFP）、频谱功率、beta burst、步态相位调制、皮层-STN耦合、刺激空间定位、闭环DBS、脑干步行网络及FOG临床亚型。\" 第9节则提出未来检索规则和查询式，但没有给出本报告实际采用的检索记录。",
   "why": "全文没有交代实际检索了哪些数据库、最后检索日期、完整检索式、时间范围、语言限制、文献纳入与排除标准、重复记录处理方式、标题摘要筛选流程、全文筛选流程及未纳入研究的理由。附录的gaps/query是未来研究缺口对应的检索建议，不是本次研究的实际检索日志。以已有结构化知识为基础进行扩展，也不等于主动、系统地寻找了可能推翻已有结论的研究。特别是该领域存在大量不同名称的步态冻结研究、步态启动研究、STN电生理研究及闭环刺激研究，单纯依靠已有证据表容易形成既有知识范围内的循环检索。150条文献记录本身不能证明覆盖充分。现在无法判断重要文献究竟不存在、被遗漏，还是检索时没有找到。",
   "severity": "major",
   "fix": "明确报告属于系统综述、范围综述还是叙述性证据综合。建议采用PRISMA-ScR或适合的PRISMA流程，列出PubMed、Embase、Web of Science、Scopus、Cochrane等实际使用的数据库及检索日期，提供可复制的完整检索式。增加纳入排除标准、筛选流程图、重复文献处理记录、全文排除理由、引文追溯及相关研究的前向引用检索。特别区分从旧知识库继承的文献与本次主动检索新增的文献。"
  },
  {
   "rank": 2,
   "what": "预印本与正式发表版本没有进行研究级去重，部分同一研究被作为不同文献和不同证据条目保存。这会破坏证据独立性，是结构化证据库中的重大问题。",
   "where": "结构化附录references中同时存在：\"DOI:10.1101/2024.06.26.24309418\"与\"PMID:40677701\"；\"DOI:10.1101/2025.05.08.25327015\"与\"PMID:40992964\"；\"DOI:10.21203/rs.3.rs-4216535/v1\"与\"PMID:39957196\"；\"DOI:10.1101/2025.01.10.632393\"与\"PMID:40709562\"。这些记录在evidence数组中也分别具有独立的EID。",
   "why": "这些并非全部是独立研究。例如，Wilkins等的2024年beta burst闭环DBS预印本与2025年正式发表论文是同一项7人研究；2025年步态序列效应预印本与PMID 40992964对应的2026年正式发表版本具有相同的18名PD患者及14名健康对照，PubMed还明确标记了正式论文与预印本的更新关系。STN-SNr的15人随机试验也同时以Research Square预印本和正式发表论文出现。2025年步态启动预印本与正式发表的PMID 40709562也包含相同的12名FOG观察阳性患者及263次冻结事件，正式版本扩展了整体队列。相关记录可以在外部文献数据库中核实。【turn546240search0】【turn575044view0】【turn546240search1】【turn546240search5】【turn578867view0】【turn653708search0】【turn575044view1】 报告没有建立version_of、study_id或cohort_id关系。因此，同一研究的多个版本可能被当作不同证据来源，部分相同发现也可能重复支持同一Claim。另有同一研究团队、相同13人转弯冻结队列的不同分析，至少需要进一步标记样本重叠，不能自动视为独立重复验证。",
   "severity": "major",
   "fix": "建立独立于PMID和DOI的study_id，以及cohort_id和version_of字段。正式发表版本作为主要证据记录，预印本保留为版本历史，并记录正式发表前后的数据、分析及结论变化。对于同一队列的不同论文，记录参与者重叠、任务重叠及分析是否独立。重新计算独立研究数量和独立患者数量，重新检查所有Claim的支持证据，避免将重复版本当成独立支持。"
  },
  {
   "rank": 3,
   "what": "附录已经收录若干非常重要的2026年原始研究，但正文没有真正整合这些证据。文献库与研究综合之间存在明显断层。",
   "where": "附录references中包括\"PMID:42571859\"、\"PMID:42236313\"、\"PMID:41810591\"、\"PMID:41741462\"和\"PMID:42297979\"。但正文第3节的STN电生理综合、第4.2节的认知负荷机制以及第8.7节的闭环DBS建议均没有系统讨论这些研究。第10.2节仍将\"优先研究FOG发生前及发生期间，STN低beta运动相关去同步化、beta burst时间结构与皮层-STN网络耦合之间的动态关系\"作为最终重点。",
   "why": "其中至少两项研究直接影响核心研究问题。PMID 42571859于2026年10月发表，采用步态周期锁定的皮层和STN同步LFP记录，比较冻结与非冻结步态周期，并考察HFS、LFS和左旋多巴的调节作用。研究发现S1和SPL的低beta异常，以及S1-STN theta coherence变化；低频刺激还影响S1不同步态相位的振荡。它直接涉及报告最关心的STN-皮层动态、步态相位和低频刺激机制。【turn633171search0】 PMID 42236313则对13名患者的实际转弯冻结进行STN-LFP记录，发现冻结期间theta功率与焦虑程度正相关、与MoCA评分负相关，而alpha和beta没有相应关联。这对报告的theta解释、认知负荷模型H6及FOG患者异质性具有直接意义。【turn270163search0】 这不是普通的参考文献遗漏，而是已经进入附录的关键证据没有进入核心综合。报告因此可能在保留旧结论的同时，忽略了能够修正旧结论的新证据。",
   "severity": "major",
   "fix": "增加独立的2026年新增证据综合章节，尤其重新分析步态周期锁定的皮层-STN活动、认知情绪相关theta活动、药物与刺激对beta信号的影响，以及长期自适应DBS结果。明确区分直接冻结期证据、冻结前预测证据和一般步态调节证据。重新检查H1、H2、H6、H9、H10及最终研究优先级，不能只把新增文献放进附录。"
  },
  {
   "rank": 4,
   "what": "证据等级体系没有真正评价研究质量和偏倚风险。报告将证据直接性、研究发现和证据确定性混在了一起。",
   "where": "第1.2节：\"直接证据、间接干预证据、跨研究推断、机制假说\"。第2.1节使用\"临床干预证据较充分\"，第10节又使用\"跨研究推断：较强\"。",
   "why": "直接证据不等于高质量证据，间接证据也不必然低质量。一个同步记录STN-LFP和FOG的4人研究虽然属于直接证据，但可能存在很大的抽样不确定性、重复测量问题及多重比较风险。一个随机交叉研究虽然属于干预证据，也可能受到洗脱期不足、顺序效应、盲法失效及选择性报告影响。报告虽然在部分研究中记录了样本量、局限和发表偏倚，但没有对纳入研究进行统一的风险偏倚评价，也没有为主要结局形成明确的证据确定性判断。没有系统评估随机研究、观察性研究、预测模型、预印本和Meta分析的质量，就很难解释为什么某个跨研究结论被定为较强。尤其是临床疗效Meta分析之间存在明显不一致，不能仅凭汇总效应或研究数量赋予较高确定性。",
   "severity": "major",
   "fix": "增加独立的质量评价层。随机试验采用RoB 2，非随机干预研究采用ROBINS-I，系统综述采用AMSTAR 2，预测模型采用PROBAST或适当的预测模型偏倚评价工具。按主要结局使用GRADE评估证据确定性。至少分别报告偏倚风险、不一致性、间接性、不精确性和发表偏倚。预印本、会议摘要和正式同行评审论文必须明确区分。证据直接性与证据质量应当成为两个独立维度。"
  },
  {
   "rank": 5,
   "what": "报告识别了Meta分析之间的冲突，却没有完成真正的研究级冲突分析；STN+SNr部分还遗漏了一项重要的随机交叉试验。",
   "where": "第4.5节：\"支持额外获益的研究包括\"以及\"反向证据包括\"。正文列出PMID 42968793和PMID 42909654两项2026年Meta分析，但没有讨论PMID 39957196这项15人随机试验。",
   "why": "两项Meta分析给出的结论明显不同。Haq等的Meta分析纳入8项交叉随机试验、97名患者，报告STN+SNr相较STN单独刺激有统计学显著的FOG改善，SMD=-0.39。Kong等的Meta分析纳入10项研究、109名患者，其中FOG结局汇总6项研究、86名患者，Hedges' g=-0.23，95% CI跨越零，I²=85.6%，证据确定性极低。【turn505047view0】【turn505047view1】 这两项分析可能存在原始研究重叠，其研究选择、配对数据处理、效应量计算和结局定义也需要比较。报告只把它们并列为阳性和阴性Meta分析，没有说明为什么结果不同。更重要的是，PMID 39957196是一项15人双盲随机交叉试验，未发现STN单独刺激与STN-SNr联合刺激之间NFOG-Q存在显著差异，但约三分之一患者获得临床显著改善。它已经出现在附录中，却没有进入正文的反向证据列表。【turn578867view0】 这会使读者无法完整判断双靶点刺激的实际证据结构。",
   "severity": "major",
   "fix": "对所有相关Meta分析建立原始研究纳入矩阵，列出每项试验是否被不同Meta分析重复纳入。比较患者数量、刺激位置、频率、配对设计、随访时间、FOG量表、客观冻结结局、效应量和统计处理方式。将15人随机试验纳入正文。特别区分相对于刺激关闭的改善与相对于优化STN单靶刺激的额外获益。不能采用简单的阳性Meta分析数量与阴性Meta分析数量投票。"
  },
  {
   "rank": 6,
   "what": "竞争性机制假说的因果结构没有定义清楚，部分假说并不真正互斥，实验预测也不足以保证区分不同机制。",
   "where": "H2：\"FOG和beta异常可能由共同的上游网络障碍引起，也可能是FOG发生后运动状态改变造成beta活动变化。\" H1与H2被作为主要竞争关系。第7节又将H6与H7列为需要比较的假说。第6.7节提出：\"在同一患者、同一电极位置及匹配TEED条件下，同时记录STN局部LFP和能够反映PPN/MLR网络状态的信号，并比较60 Hz和130 Hz。只有同时观察局部电生理和网络募集，才有可能真正区分H9与H10。\"",
   "why": "H2实际上混合了至少三种不同解释：上游共同原因同时影响beta和FOG；FOG发生后的运动变化反过来改变beta；beta只是伴随状态的标志。这三种模型具有不同的因果结构和可检验预测，不能合并为一个H2。H1与上游共同原因模型也并非绝对互斥，beta完全可能既是网络状态的指标，又对FOG具有部分因果贡献。此外，控制步速、步幅、APA和运动学指标可能把真正的中介变量当作混杂因素调整，造成过度调整。H6网络负荷、H7自动化运动驱动不足和H8 APA失耦也可能同时成立，而不是互相排斥。H9与H10同样可能同时发生：低频刺激可以同时改变STN局部振荡和邻近纤维募集。单纯同步记录两类信号只能观察共同变化，不能证明哪一条通路介导了疗效。报告对竞争性解释的分类尚未达到严格因果假说的要求。",
   "severity": "major",
   "fix": "为每个机制建立明确的因果图，至少区分STN beta作为因果中介、上游网络状态的共同结果、运动状态变化的后果以及代偿性活动四种模型。明确每个模型的时间顺序、混杂因素、中介变量和反证条件。将机制假说、神经标志物假说、患者分型假说和刺激疗效机制分开分类。对于H9/H10及H4/H5，不能仅依赖同步记录或相关性，必须设计能够选择性改变候选通路或连接的干预条件，并预先指定主要结局。"
  },
  {
   "rank": 7,
   "what": "长期知识结构和证据关系图目前存在无法解析的引用边、错误证据编号及数量不一致，尚不能作为可靠的自动更新知识库。",
   "where": "第9.3节声称建立结论关系图；第9.4节提出新证据触发旧结论重新评价。第10.2节最后写道：\"这也是将现有539条证据从文献汇总转化为可持续检验的研究体系的关键。\"",
   "why": "实际解析结构化附录发现，evidence数组只有538条记录，而正文声称539条。claims中的from字段引用了47个不同的G类来源编号，但交付的JSON顶层没有对应的groups或来源节点表，因此无法在该JSON内解析这些关系。另外，C6的一个evidence引用指向S2_E_DOI_10.21203_rs.3.rs-9617843_v10，但实际evidence数组中不存在该EID。这些问题说明关系图尚未经过完整的引用完整性验证。对于一个强调长期积累、旧结论重新评价和自动更新的系统，这不是单纯的格式错误，而是数据模型本身尚不完整。",
   "severity": "moderate",
   "fix": "建立完整的关系数据库结构，确保每个Claim都能追溯到有效Evidence，每个Evidence都能追溯到具体文献及版本，每个机制假说都能追溯到对应Claim。将外部G类来源节点纳入交付文件，或者将from字段改为可直接解析的Evidence ID。增加自动化完整性检查，包括引用外键、重复EID、缺失来源、文献版本、患者队列关系和总数一致性检查。证据数量应从实际数据自动生成，而不是手工填写。"
  },
  {
   "rank": 8,
   "what": "步态启动研究的证据阶段分类不够准确，把具有明确后续冻结事件的冻结前证据降格成一般FOG易感性证据。",
   "where": "第2.3节：\"这些研究主要分析没有实际冻结发生的步态启动试次，因此更接近FOG易感性证据，而不是实际冻结期间的直接神经活动证据。\" 引用DOI:10.1101/2025.01.10.632393。",
   "why": "需要区分冻结发生时正在进行步态启动，还是步态启动后经过若干步才出现冻结。正式发表的PMID 40709562研究纳入38名PD患者，其中12名在实验中观察到FOG，共有99个包含冻结事件的步行试次和263次冻结事件；首次冻结平均出现在步态启动后约8步。其步态启动期LFP因此不仅反映患者的一般易感性，还包含随后发生实际冻结的试次所提供的事件关联信息。【turn575044view1】 它确实不是实际冻结期间的LFP记录，但属于报告自己定义的Pre-FOG证据。把它主要归入FOG susceptibility，会丢失冻结前预测与长期易感性之间的关键区别，也会低估STN活动在冻结发生前的时间关联。",
   "severity": "moderate",
   "fix": "按照报告第3.1节的四状态框架重新分类该研究。明确区分一般FOG易感患者的步态启动特征、同一患者未冻结试次的步态启动特征，以及随后发生FOG试次的冻结前步态启动特征。使用正式发表版本更新预印本结果，并报告首次冻结与步态启动之间的时间间隔。"
  },
  {
   "rank": 9,
   "what": "至少存在一处可以通过原始全文核实的证据提取错误：慢性自适应DBS研究被记录为没有明确的FOG改善，但全文实际报告了FOG-Q改善。",
   "where": "结构化附录PMID:41741462对应的evidence记录：\"本研究报告aDBS较cDBS具有额外的运动症状改善，但没有明确报告FOG改善。\" 该记录的basis标记为abstract。",
   "why": "该研究的全文明确报告，5名长期接受aDBS的患者在优化后FOG-Q评分平均改善40%。但这不能解释为已经证明长期FOG疗效：样本只有5人，没有充分的统计推断，日常生活可穿戴设备记录的冻结事件仅在2/5患者中减少，其他患者的变化存在明显差异。【turn693740search12】 因此，正确的结论应当是问卷指标出现探索性改善，但客观日常冻结事件的结果异质且证据不足，而不是没有报告FOG改善。该错误说明部分重要研究只提取了摘要，导致全文中的关键结果丢失。",
   "severity": "moderate",
   "fix": "对直接涉及FOG、STN-LFP和自适应DBS的关键研究优先提取全文，而不能只依赖摘要。将FOG-Q、实验室冻结次数和日常生活冻结事件分开记录，并同时报告样本量、统计检验和患者间差异。增加摘要与全文结果的交叉核对，避免将摘要未提及误写为原始研究未报告。"
  },
  {
   "rank": 10,
   "what": "持续自主改进部分提出了合理的工作流程，但没有证明该流程实际运行过，也没有证明改进能够提高研究质量。",
   "where": "第9.5节：\"建议采用以下循环\"，随后列出\"检索覆盖率、证据提取准确性、证据可追溯性、冲突识别能力、预测验证能力\"五类指标。",
   "why": "这些内容目前是一个系统设计建议，而不是经过验证的自主改进机制。报告没有展示任何一次完整的缺陷发现、原因验证、修改、重新检索、重新提取及改进效果评价过程，也没有提供更新前后的准确率、召回率、重复文献识别率、证据提取错误率或引用完整性变化。更重要的是，当前报告本身已经存在预印本重复、539与538数量不一致、引用关系无法解析以及全文结果提取错误等问题，却没有展示系统如何发现并纠正这些缺陷。因此，无法判断这套机制究竟能够自主改进，还是仅仅描述了一套理想化工作流程。",
   "severity": "moderate",
   "fix": "选择一批经过人工核验的原始研究作为固定测试集，实际运行一次完整的知识更新流程。记录更新前后的文献检索召回率、精确率、版本去重准确率、数据提取准确率、证据追溯成功率和Claim更新正确率。由独立研究者对修改结果进行盲法核验。保留每次更新的旧版本、新版本、错误类型、修改原因及验证结果。只有能够证明改进前后指标真实改善，才能将其称为持续自主改进机制。"
  }
 ],
 "overall": "这份报告具有较好的领域知识组织能力，尤其是对STN平均beta功率方向冲突、冻结阶段差异、beta burst时间结构以及STN-皮层网络动态的区分，体现出一定的专业理解。它也注意到了相关性与因果性的区别，并提出了若干有价值的实验假说。但目前最严重的问题不是某个机制解释不够完善，而是证据生产和管理过程尚未达到报告自身设定的科学标准：检索不可复现，预印本与正式发表版本没有可靠去重，部分2026年关键原始研究没有进入正文综合，证据质量没有系统评价，Meta分析之间的冲突没有落实到原始研究层面，机制假说的因果结构也不够严格。结构化附录虽然规模较大，但引用关系存在断裂，且已经出现可以通过原始全文验证的提取错误。因此，目前不宜把它视为已经完成的系统性证据综合，也不宜直接把其539条证据和H1-H13作为成熟、可持续更新的研究知识体系。更准确的定位是：一份具有较好研究框架和机制探索价值、但仍需要进行文献去重、全文复核、证据质量评价、因果模型重构和数据完整性审计的探索性研究综合。"
}

===== S2 / open_g56.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "缺少可复现的系统检索方法，无法证明研究覆盖是否充分。",
   "where": "第5行：\"以用户提供的结构化知识及 evidence_table.txt 中的原始文献证据为基础\"。第九章虽然提出建立可检索证据库，但全文没有完整报告实际检索所使用的数据库、检索日期、各数据库的完整检索式、语言限制、纳入排除标准、筛选过程、重复文献处理方式及检索结果数量。附录中的 TITLE_ABS 检索式主要是针对未来证据缺口提出的检索建议，而不是已经执行的检索记录。",
   "why": "这是研究覆盖方面的根本缺陷。报告列出了大量文献和交叉方向，但无法判断这些文献究竟来自系统检索、原有知识库还是选择性补充。也无法判断是否遗漏了重要的阴性研究、尚未发表的研究、不同刺激靶点研究及最新的事件级电生理研究。文献数量多不等于覆盖全面。尤其是DBS、FOG、电生理和闭环神经调控之间存在大量不同的检索术语，仅依赖少量关键词容易产生系统性遗漏。此外，报告没有检索流程图，无法判断是否存在选择性纳入。",
   "severity": "major",
   "fix": "补充独立的系统检索方法章节。明确PubMed、Embase、Web of Science、Scopus、Cochrane及临床试验注册平台等实际使用的数据库，提供每个数据库的完整检索式、检索截止日期、语言和时间限制、筛选标准、双人筛选与争议解决方法、去重记录及PRISMA流程图。将已经执行的检索与未来建议开展的检索严格区分。对重要交叉方向分别建立检索模块，并通过已知关键原始研究进行反向检索和覆盖率检查。"
  },
  {
   "rank": 2,
   "what": "证据库存在研究版本重复、原始研究与综述重复计入以及潜在队列重叠问题，538条证据记录不能代表538份独立证据。",
   "where": "第1472行：\"将现有539条证据从文献汇总转化为可持续检验的研究体系\"。结构化附录实际上包含538个 evidence 对象。更重要的是，参考文献同时收录了多组同一研究的预印本和正式发表版本，例如：DOI:10.1101/2024.06.26.24309418 与 PMID:40677701（同一项7人beta-burst aDBS研究）；DOI:10.21203/rs.3.rs-4058858/v1 与 PMID:40504072（同一项17人药物与刺激交互研究）；DOI:10.1101/2025.01.10.632393 与 PMID:40709562（同一项38人步态启动研究）。部分Claims还将同一研究的预印本和正式版本分别列为支持证据。另有大量 evidence 记录来自综述对原始研究的重复转述。",
   "why": "这不是简单的参考文献格式问题，而是证据独立性问题。同一队列的预印本和正式论文不能被视为两次独立重复验证；同一原始试验经不同综述转述，也不能自动产生新的独立支持。否则，某个结论可能因为同一批患者被多次记录而显得拥有更多证据。报告已经注意到不能把同一患者的多个冻结事件当成独立患者，却没有建立相应的研究版本、原始队列和证据来源依赖关系。更值得注意的是，538条记录中有145条标记为review，来自24个综述类来源。它们与原始研究之间的重复关系没有得到系统处理。这样会影响Claims的证据数量、证据权重及长期更新结果。预印本与正式版本确实存在相同队列的例子也可从原始记录核对。 【turn833500search0】【turn833500search1】【turn299087search0】【turn320655search0】",
   "severity": "major",
   "fix": "建立三个不同层次的稳定标识：Study ID（研究）、Cohort ID（患者队列）、Version ID（预印本或正式发表版本）。为每个证据片段增加 primary_source、secondary_source、version_of 和 cohort_overlap 字段。正式发表后将预印本关联到正式版本，保留版本历史，但不重复增加独立证据权重。综述转述的原始发现应追溯至原始研究，并明确标注为二手证据。每个Claim应同时报告证据片段数、独立原始研究数、独立队列数及患者总数。重新检查所有538条记录及其867条以上的Claim关联，避免重复支持。"
  },
  {
   "rank": 3,
   "what": "对2025年重要STN步态启动研究的证据性质判断存在实质性错误，而且与结构化附录自身矛盾。",
   "where": "第201行：\"这些研究主要分析没有实际冻结发生的步态启动试次，因此更接近FOG易感性证据，而不是实际冻结期间的直接神经活动证据。\" 对应文献为DOI:10.1101/2025.01.10.632393，正式发表版本为 PMID:40709562。",
   "why": "该研究并非只分析没有冻结的试次。正式发表论文纳入38名PD患者，其中12人在实验记录中实际发生FOG，共263次冻结事件，分布于99个含冻结的步行试次。冻结平均发生在步态启动后第8步。研究同步记录STN-LFP和步态，并比较最终发生冻结与未发生冻结的试次。它确实没有在冻结已经发生的瞬间分析STN信号，其主要神经分析窗口位于步态启动阶段，因此正确分类应是冻结前、事件相关的神经活动证据，而不是冻结期间的直接记录，也不是单纯的FOG易感性证据。报告自己的结构化附录实际上已经记录了38名患者、12名实际冻结患者及263次事件，却在正文中给出了相反的概括。这会直接影响第三章对FOG四种状态的分类，也会低估H1、H3等假说所拥有的事件前证据。原论文明确区分了FOG易感、实际发生和冻结前神经变化。【turn299087search0】【turn320655search0】",
   "severity": "major",
   "fix": "重新阅读该研究全文，分别提取FOG-NOBS、FOG-OBS但当前试次未冻结、FOG-OBS且当前试次最终发生冻结三种条件。将步态启动时记录、随后发生冻结的试次归入Pre-FOG或event-associated evidence，而不是无冻结试次。明确指出神经信号是在冻结发生前采集的，不能冒充During-FOG证据。同步修正第二章、第三章、第五章及H1/H3的证据映射，并检查是否还有其他研究存在相同的时间窗口分类错误。"
  },
  {
   "rank": 4,
   "what": "正文没有充分综合附录中已经收录的若干关键原始研究，导致核心证据叙述不完整。",
   "where": "第三章3.2主要讨论Liu 2022、Thenaisie 2022、Klocke 2026及Syrkin-Nikolau 2017；3.5主要讨论Pozzi 2019和Zhang 2025。可是结构化附录还收录了PMID:31665229、24361601、31494286、42571859、42236313和42297979，正文没有对这些研究进行相应的实质性综合。",
   "why": "其中有几项不应仅作为附录中的补充记录。Georgiades等（2019，PMID:31665229）在8名患者术中使用虚拟现实诱发FOG，并同步记录STN多单位活动和EMG，发现冻结起始伴随STN活动短暂增加及beta/theta节律增强，而且能够与主动停止区分。这是直接事件级神经生理证据。Toledo等（2014，PMID:24361601）研究22名患者，其中FOG组14人、非FOG组8人，发现FOG组STN高beta功率及皮层-STN高beta耦合差异，并观察到左旋多巴治疗前后的变化。Chen等（2019，PMID:31494286）则提供了低beta/theta与冻结易感步态的证据。更重要的是，2026年10月发表的PMID:42571859同步记录皮层与STN-LFP，发现FOG阳性步行试次中的S1/SPL低beta异常，以及S1-STN theta耦合对左旋多巴的反应；PMID:42236313在13名患者实际转弯冻结时记录STN-LFP，发现theta活动与焦虑及MoCA评分相关；PMID:42297979则提供了35人活动依赖性STN神经解码与自适应步态刺激研究。这些结果分别影响H1、H3、H6、H9、H10及闭环DBS策略。它们虽然已经进入附录，却没有充分进入正文的证据比较、机制冲突分析和最终研究优先级。([PMID:31665229](https://pubmed.ncbi.nlm.nih.gov/31665229/))([PMID:24361601](https://pubmed.ncbi.nlm.nih.gov/24361601/))([PMID:31494286](https://pubmed.ncbi.nlm.nih.gov/31494286/))([PMID:42571859](https://pubmed.ncbi.nlm.nih.gov/42571859/))",
   "severity": "major",
   "fix": "逐条检查附录中所有与核心研究问题高度相关、但未进入正文的证据。优先补充上述研究，分别放入FOG易感性、冻结前活动、实际冻结、认知情绪调节和自适应刺激部分。尤其应讨论2019年术中多单位记录与2026年皮层-STN步态周期研究对现有beta模型的补充和挑战。每篇研究必须说明其对已有Claim和竞争性假说究竟是支持、反对还是限定，而不是只增加参考文献。"
  },
  {
   "rank": 5,
   "what": "证据分层没有真正评估研究质量，直接性分类被误当成证据可靠性分层。",
   "where": "第53—60行：报告将证据分为直接证据、间接干预证据、跨研究推断和机制假说。第五章5.6仅指出部分研究属于预印本或小样本研究，没有建立系统的研究质量评价体系。第1374行以后又给出了较强、中等、有限等证据判断，但没有说明这些判断的具体标准。",
   "why": "直接性和可靠性是两个不同维度。一个同步记录实际冻结的4人研究可以属于直接证据，但仍然可能具有极低的精确度和较高的偏倚风险。一个随机交叉研究也可能存在顺序效应、洗脱不足或失访问题。报告目前没有系统评价随机化、盲法、选择偏倚、测量偏倚、重复测量伪重复、多重比较及选择性报告。预印本也没有在每条证据中统一标记。一个具体例子是STN+SNr的阳性Meta分析（PMID:42968793）：原文报告8项交叉RCT中1项低风险、5项中风险、2项高风险，而且由于原始研究缺少配对统计量，部分合并分析采用了平行组近似方法。报告没有讨论这些限制，却将其与另一项GRADE确定性极低的阴性Meta分析并列。两者的证据可靠性并不相同。([原Meta分析](https://connectionssurgery.bmj.com/content/8/1/e000033))",
   "severity": "major",
   "fix": "建立独立于证据直接性的质量评价体系。随机试验使用RoB 2，观察性研究使用ROBINS-I，系统综述使用AMSTAR 2或ROBIS。针对不同Claim采用GRADE或适当的证据确定性框架。将发表状态、样本量、独立患者数、事件数、统计方法、偏倚风险和外部验证情况作为独立字段。明确规定何种证据组合才能将结论标记为强、中等或有限。对于预印本，单独标识其未经同行评审的状态，不能仅在总论中笼统提醒。"
  },
  {
   "rank": 6,
   "what": "证据追溯链不完整，报告并非可独立审计的自包含研究文档。",
   "where": "第5行引用了外部的evidence_table.txt。正文第401—404行、第507—511行、第1169—1171行及第1365—1366行使用了诸如<FileCite ref=\"turn1file0\" />、<FileCite ref=\"turn6file9\" />等临时文件引用。结构化附录中的Claims还包含G1_1_C1、G1_2_C12等from标识，但这些来源节点没有在当前附录中定义。",
   "why": "这些引用无法让独立读者稳定地定位具体原始证据。临时turn编号依赖原来的对话或文件环境，不能作为长期文献标识。47个不同的from来源标识在当前JSON结构中没有对应定义。部分证据记录虽然包含PMID、DOI和quote，但没有明确的论文页码、图表、结果段落或补充材料定位。报告声称每条结论能够追溯至原始文献，但目前只能部分实现文献层面的检索，不能保证具体数值和论断的逐项审计。",
   "severity": "major",
   "fix": "为每条Evidence提供稳定的PMID/DOI、正式发表版本、原文URL、页码或章节、图表编号、原文摘录及提取日期。所有Claims必须能够通过稳定的Evidence ID返回具体原始来源。补充G1等历史来源节点，或将它们转换为当前JSON中可解析的稳定引用。将evidence_table.txt及其版本信息纳入正式交付件，避免依赖临时对话引用。"
  },
  {
   "rank": 7,
   "what": "所谓竞争性假说并不都是真正互斥的机制，部分假说还把不同因果关系混在同一个模型中。",
   "where": "第619—679行的H1与H2；第831—884行的H9与H10；第907—942行的H12与H13。第950—958行又将这些关系作为优先开展区分性实验的竞争性假说。",
   "why": "首先，H1认为STN beta异常具有部分因果贡献，H2认为beta主要是共同上游网络异常或运动状态变化的伴随标志。这两种解释并不必然互斥：beta可以既反映上游网络异常，又对冻结发生产生部分因果贡献。其次，H2本身混合了共同原因和反向因果两种不同机制：前者是上游网络同时影响beta和FOG，后者是FOG发生后的运动变化影响beta。它们需要不同的因果图和实验预测。再次，低频刺激可能同时改变STN局部振荡和PPN/MLR相关通路募集，因此H9与H10可能是并行中介，而非只能二选一。TBS暂停期间的即时反弹与长期神经可塑性也可能同时存在。PMC-STN alpha耦合则可能在某个阶段具有代偿作用，在另一个阶段表现为病理性过度耦合。将这些关系强行设置为相互排斥，可能得到错误的实验结论。",
   "severity": "major",
   "fix": "先为每种机制绘制明确的因果有向图，区分上游共同原因、局部中介、行为后果及反馈环路。将H2拆分为共同原因模型和反向因果模型。将H9/H10重新定义为可以同时存在的不同中介路径，采用正交操纵来判断各自贡献。H12/H13则应分别研究短期刺激暂停效应和长期可塑性效应，同时允许两种现象共存。所有竞争关系必须明确指出哪些预测互斥，哪些只是效应大小不同。"
  },
  {
   "rank": 8,
   "what": "部分关键实验设计即使完成，也未必能够识别其声称要区分的因果机制。",
   "where": "第176行：\"等效TEED不等于等效组织募集\"。第880—884行：建议在同一患者、同一电极位置及匹配TEED条件下，同时记录STN局部LFP和PPN/MLR相关网络信号，并比较60 Hz和130 Hz，以区分H9与H10。H1/H2的预测还提出通过选择性恢复beta动态来检验因果贡献。",
   "why": "这里存在明显的方法学问题。报告已经承认TEED匹配不等于组织募集等效，但随后仍把匹配TEED作为区分局部STN机制和脑干通路机制的实验基础。60 Hz与130 Hz改变时，STN局部神经活动、邻近纤维募集、网络传播和刺激扩散可能同时变化。即使同时观察到STN-LFP和PPN/MLR信号变化，也只能说明两者与治疗条件共同变化，不能确定哪一条通路介导了FOG改善。类似地，改变刺激后beta burst缩短，并不能证明beta是疗效的因果中介，因为刺激本身可能同时改变其他神经过程。此外，H1/H2提出控制步速、步幅、APA等变量，但这些变量可能是STN异常导致FOG的中介。若不先建立因果图就直接调整，可能造成过度调整，反而消除真正的因果效应。",
   "severity": "major",
   "fix": "将观察性同步记录与因果操纵分开设计。H9/H10应采用能够独立改变局部STN调制与特定纤维通路募集的正交刺激条件，例如结合方向性电极、个体化VTA和纤维连接模型，并设置独立的通路刺激对照。预先定义总效应、直接效应及中介效应，确定哪些运动学变量是混杂因素、哪些是中介变量。H1/H2需要真正具有信号特异性的干预对照，并证明神经信号改变先于临床变化，而不只是两者同时改变。"
  },
  {
   "rank": 9,
   "what": "对STN+SNr两项相反Meta分析的冲突解释不够深入，没有比较其原始试验重叠和统计方法。",
   "where": "第489—505行：报告并列呈现STN+SNr联合刺激的阳性和阴性研究及两项2026年Meta分析，但没有系统比较两项Meta分析的原始试验纳入情况和统计方法。",
   "why": "两项Meta分析并不是简单的同等质量、相互独立的相反结果。阳性Meta分析纳入8项交叉RCT、97名患者，其中FOG结局实际由7项研究提供；由于原始试验缺少配对统计量，作者采用了平行组近似方法，可能忽略交叉设计中的受试者内相关性。该研究还报告5项中风险和2项高风险试验。另一项Meta分析纳入6项提供FOG数据的研究、86名患者，并采用考虑配对数据和研究内依赖的方法，最终将FOG额外获益的确定性评为极低。报告仅指出二者结论相反，没有说明纳入研究是否重叠，也没有分析不同统计方法、FOG结局及患者选择如何影响结果。([阳性Meta分析](https://connectionssurgery.bmj.com/content/8/1/e000033))([阴性Meta分析](https://pubmed.ncbi.nlm.nih.gov/42909654/))",
   "severity": "moderate",
   "fix": "增加两项Meta分析的逐篇纳入研究对照表，标明共同原始试验、独有试验、患者队列和结局指标。比较两者的统计模型、交叉试验配对处理、异质性、风险偏倚和GRADE确定性。重新计算可比的FOG结局，并进行排除高风险研究、不同量表及不同刺激频率的敏感性分析。不能将两篇Meta分析简单视为两份独立的正反证据。"
  },
  {
   "rank": 10,
   "what": "长期知识积累和持续自主改进目前仍停留在方案设计阶段，实际结构化数据不足以支持可靠的长期检索和自动更新。",
   "where": "第1227—1254行提出Evidence记录字段；第1322—1362行提出持续改进流程。但当前JSON中的Evidence对象主要只有eid、ref、design、population、n、condition、measure、finding、limitations、quote和basis。",
   "why": "报告建议的结构化字段包括独立患者数、事件数、表型、药物状态、刺激条件、解剖位置、任务、冻结阶段、信号指标、效应量和证据关系，但当前JSON并没有将这些信息分别存储。它们大多被压缩进n、condition、measure等自由文本字段。缺少独立的Study ID、Cohort ID、版本关系、event_phase、publication_status、effect_size和risk_of_bias等字段。这样无法稳定地查询例如Med-Off、Stim-Off、Pre-FOG、low-beta ERD的特定证据集合，也难以自动发现同一队列的新增论文。第九章提出了检索覆盖率、提取准确率等质量指标，却没有给出实际测量结果、基线、阈值或一次完整的改进前后验证。因此，报告展示的是一个未来知识管理系统的设计构想，而不是已经实现并验证的持续自主改进能力。",
   "severity": "major",
   "fix": "将附录升级为真正规范化的证据数据库。使用独立字段记录患者数、事件数、任务、事件阶段、药物状态、刺激参数、信号、结局、效应量、置信区间、风险偏倚、发表状态和原始来源位置。建立研究、队列、论文版本、Evidence、Claim、Mechanism及Hypothesis之间的稳定关系。为自动更新建立版本控制、重复研究检测、证据冲突提醒和重新评价规则。最后使用已知文献集合开展检索与提取基准测试，报告改进前后的准确率、召回率、重复识别率及错误率，而不是只列出拟议的质量指标。"
  },
  {
   "rank": 11,
   "what": "FOG事件阶段和临床结局虽然被指出存在异质性，但尚未形成可以实际执行的统一操作性定义。",
   "where": "第213—242行将神经状态分为FOG易感、冻结前、实际冻结和恢复四种状态；第587—600行指出FOG-Q、NFOG-Q、SWS、冻结次数及冻结时间占比不能互换；第965—1004行建议开展事件锁定数据库。",
   "why": "四种状态目前主要是概念分类，没有明确规定冻结前窗口的时间长度、事件开始和结束判定标准、恢复有效行走的判定标准，以及正常任务匹配窗口的具体要求。不同研究中的冻结前可能是步态启动后若干步、转弯开始前、冻结前几秒，或整个最终发生冻结的试次。这些不是同一个时间尺度。类似地，FOG-Q改善、冻结发生概率下降、冻结时间减少和连续步速改善也不能合并成一个统一的FOG改善结局。报告虽然认识到这些差异，但其Claims和最终结论仍然在一定程度上使用统一的FOG改善或FOG相关活动来概括不同研究。",
   "severity": "moderate",
   "fix": "建立明确的FOG事件本体和统一标注规则。至少定义易感状态、FOG阳性试次、事件前窗口、冻结起始、冻结持续、冻结终止和恢复行走，并规定各自的时间和运动学判定条件。将患者报告量表、诱发任务中的冻结次数、冻结持续时间、冻结概率和连续步态指标作为不同结局类别。综合结论必须标明具体结局类型，只有测量对象真正一致时才能进行定量合并。"
  }
 ],
 "salvaged": true
}

===== S2 / abs_g6.json =====
{
 "standards": [
  {
   "n": 1,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "文献覆盖较广，但检索过程不可复现。没有报告实际使用的数据库、检索日期、完整检索式、纳入排除标准、重复文献处理及筛选流程，因此无法判断是否真正主动、系统地减少了重要文献遗漏。",
     "where": "第5行：“证据范围：以用户提供的结构化知识及 evidence_table.txt 中的原始文献证据为基础。”全文没有提供完整的实际文献检索与筛选记录。"
    },
    {
     "severity": "moderate",
     "what": "部分重要交叉方向虽然进入结构化附录，却没有充分进入正文综合。例如，Klocke等2024年研究直接同步记录STN-LFP、拮抗肌EMG和步态运动学，分析实际冻结前后的STN-肌肉耦合；2026年研究进一步研究了步态周期锁定的皮层-STN信号及其对不同刺激条件的响应。这些证据与H8、H9及分布式网络模型直接相关，但正文没有充分整合。",
     "where": "第4.4节：“但这些研究主要使用原地踏步或没有实际FOG的步态周期。”附录列有PMID:39470410和PMID:42571859，但正文没有相应的系统讨论。两项研究的原始结果可见。"
    }
   ]
  },
  {
   "n": 2,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "2025年步态启动研究的事件阶段描述不够准确。最终同行评审论文报告38名患者，其中12名观察到实际FOG，共263次冻结事件；这些事件通常发生在步态启动后约8步。步态启动阶段的LFP分析确实发生在冻结之前，但不能将整项研究简单描述为没有实际冻结事件的试次。报告的结构化附录已经包含部分正确数据，正文却没有充分保留这一差别。",
     "where": "第201行及第338行：“这些分析主要来自没有实际冻结发生的步态启动试次。”正文引用DOI:10.1101/2025.01.10.632393，而附录同时列出最终同行评审版本PMID:40709562。最终论文明确区分了GI阶段的神经活动与其后发生的FOG事件。"
    },
    {
     "severity": "moderate",
     "what": "部分重要研究的原始证据提取不完整。例如PMID:39470410的附录记录将样本量标为摘要未报告，并且仅标注abstract作为证据基础。但原始论文全文报告最终分析队列为12名患者，并提供实际冻结、肌肉共同激活和STN-肌肉耦合的详细分析。这会降低证据记录的完整性，也使正文对H8的综合不够充分。",
     "where": "结构化附录中的S2_E_PMID_39470410_1：“n: 摘要未报告”；“basis: abstract”。原始论文全文："
    },
    {
     "severity": "minor",
     "what": "证据数量存在内部不一致。正文声称有539条证据，但对所提供JSON附录的实际解析得到538条evidence记录。需要确认是否遗漏一条记录或正文计数未更新。",
     "where": "第1472行：“这也是将现有539条证据从文献汇总转化为可持续检验的研究体系的关键。”与第1477行结构化JSON中的evidence数组不一致。"
    }
   ]
  },
  {
   "n": 3,
   "verdict": "met",
   "issues": [
    {
     "severity": "minor",
     "what": "跨研究综合质量较好，但还没有建立统一的研究质量评价体系。报告讨论了样本量、重复测量伪重复、发表状态和研究局限，却没有为每项研究系统提供偏倚风险、证据确定性或研究质量等级。因此，目前的证据强弱判断主要依赖定性综合。",
     "where": "第5.4至5.8节讨论了小样本、伪重复和发表状态；第608行：“不能将综述转述、预印本和原始同行评审研究视为相同确定性等级。”但结构化附录没有独立的risk-of-bias或GRADE字段。"
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
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "已经建立较好的长期知识积累架构，包括稳定Evidence ID、PMID/DOI、研究条件、结论关系及假说更新规则。但目前主要是结构化数据和流程设计，没有展示实际运行的知识库检索系统、版本控制记录或新文献触发旧结论重新评价的执行案例。尚不能证明新问题能够稳定调用过去的证据，也不能证明更新规则已经实际生效。",
     "where": "第9.2节：“建议保留附件中原有的证据编号”；第9.4节：“建议设置以下更新规则”；第9.4节：“更新时应保留旧版本结论及其证据状态。”这些主要是设计建议，而不是已经验证的运行能力。"
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
     "severity": "severe",
     "what": "报告能够识别部分研究成果的数据质量问题，也提出了持续改进循环，但没有展示完整的自主改进闭环。具体而言，报告指出了Meta分析摘要与正文效应量不一致、VR研究摘要与正文冻结事件数量不一致等问题，却没有进一步展示对差异原因的完整验证、数据修正、重新提取或重新分析，以及修正前后质量指标的比较。因此，目前能够证明的是缺陷识别和改进流程设计，不能证明系统已经能够自主验证原因、实施修复并检验修复效果。",
     "where": "第9.5节：“建议采用以下循环”；第1363行：“例如，2025年网络Meta分析对步速效应量的摘要与正文存在数值差异；2026年VR冻结检测研究也存在正文与摘要事件数量不一致的问题。”报告没有继续展示这些问题的根因验证、修正记录及改进效果。"
    }
   ]
  }
 ],
 "spot_checks": [
  {
   "claim": "STN-DBS能够改善部分PD患者的FOG，但疗效存在显著患者间异质性，不能概括为普遍改善或普遍恶化。",
   "cited": "PMID:27766724; PMID:18413568; PMID:31755599; PMID:26887333; PMID:41659700; PMID:42098512",
   "verdict": "consistent",
   "why": "与原始文献及Meta分析基本一致。Schlenstedt等2017年Meta分析纳入16项步态研究，其中6项提供FOG数据，支持Med-Off/Stim-On条件下的改善。Ferraye等123名患者研究也显示多数术前左旋多巴反应性FOG患者能够从刺激中获益，但11名患者术后首次出现FOG或无法完成步行测试。相反，Guo等2025年网络Meta分析没有发现任何刺激模式在FOG-Q上达到统计学显著改善，I²为88.3%。Behboodi等2026年Meta分析报告总体FOG-Q小幅改善，但仍存在显著异质性。报告正确保留了相反证据，没有把总体改善等同于普遍有效。"
  },
  {
   "claim": "STN-DBS刺激频率与FOG之间存在明显患者和任务依赖性，目前没有充分证据证明低频刺激普遍优于130–150 Hz高频刺激。",
   "cited": "PMID:28529730; PMID:30262859; PMID:18420482; PMID:25540305",
   "verdict": "consistent",
   "why": "原始研究支持这一判断。Xie等2017年综述明确指出，低频刺激的效果受到FOG表型、实际冻结诱发情况、刺激频率、药物状态、TEED和电极位置等因素影响。Su等2018年Meta分析纳入10项研究、132名患者，发现低频刺激在冻结次数方面具有统计学优势，但总体研究仍有限。13名患者的盲法参数比较以及7名患者的60Hz研究也支持部分HFS下仍冻结患者的获益。报告没有将这些结果外推为所有患者均应使用60Hz。"
  },
  {
   "claim": "STN-DBS对FOG的影响具有解剖区域和结构连接网络特异性，刺激接触点是否位于STN内部不足以完整解释临床效果。",
   "cited": "PMID:37701817; PMID:39475137; PMID:26887333; PMID:35431262; PMID:36242900",
   "verdict": "consistent",
   "why": "有较好的原始研究支持。Fan等2023年研究76名患者，发现42人改善、22人变化较小、12人恶化，并识别出不同的STN刺激位置及相关连接网络。Cherif等2025年10人随机双盲交叉研究发现中心STN定向刺激相较后部STN刺激减少FOG发作，ring模式也优于后部刺激，但中心与ring模式之间没有显著FOG发生概率差异。Fleury等研究还支持某些STN邻近区域刺激可能恶化步态。需要保留的限制是，部分结构连接结果依赖规范性连接组和回顾性分析，不能证明具体纤维通路的因果作用。报告对这一限制的总体表述合理。"
  },
  {
   "claim": "现有证据支持STN神经活动与FOG易感状态及实际冻结事件存在关联，但尚未证明某种自发STN活动模式是FOG发生的必要或充分原因。",
   "cited": "PMID:35310098; PMID:31505548; PMID:40709562; PMID:42239677",
   "verdict": "consistent",
   "why": "Liu等2022年研究8名患者，30次含冻结的步行测试中有21次获得较高质量数据，观察到实际冻结期间STN beta功率增加。Pozzi等2019年研究7名患者，发现4–13Hz皮层-STN耦合在冻结前下降、冻结期间持续降低，并在恢复行走后恢复。2025年步态启动研究在38名患者中记录到12名患者的实际FOG，共263次事件，提供了冻结前神经活动与后续冻结的关联证据。2026年VR研究则是小样本STN-LFP冻结检测研究。这些研究支持相关性、时间关联和检测可行性，但不能证明必要性、充分性或独立因果贡献。"
  },
  {
   "claim": "STN平均beta功率与FOG之间不存在跨患者、跨任务和跨冻结阶段均适用的统一方向关系。",
   "cited": "PMID:35310098; PMID:36070366; PMID:28890315; PMID:31505548",
   "verdict": "consistent",
   "why": "这一综合结论有直接证据支持。Liu等2022年研究发现实际冻结期间STN beta功率升高。Syrkin-Nikolau等2017年研究发现Freezers在实际FOG期间的beta功率低于无冻结的自由步行阶段。Pozzi等2019年研究则发现实际冻结期间STN局部beta功率没有显著变化。不同研究还使用了不同的任务、频段、基线和归一化方法。因此，不能将平均beta功率升高作为统一FOG标志物。报告对这些不同结果的并列处理是合理的。"
  },
  {
   "claim": "STN beta活动的时间结构及步态相位调制可能比平均beta功率更接近部分FOG相关病理过程，但现有结果仍然存在任务依赖性。",
   "cited": "PMID:30196050; PMID:31505548; DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "consistent",
   "why": "Anidi等2018年研究12名患者，发现Freezers具有较长的运动相关beta burst，实际冻结期间部分患者的burst持续时间进一步延长；刺激也能够缩短病理性长burst。Pozzi等2019年研究却没有发现冻结期间beta burst持续时间出现显著变化。Klocke等2026年13人预印本进一步报告转弯冻结中的burst持续时间分布重组，但部分平均值比较没有显著差异。这些结果支持研究burst分布、占据率和步态相位调制的价值，但不能证明它们已经优于平均功率成为通用生物标志物。报告使用“可能”并保留不确定性，措辞基本恰当。"
  },
  {
   "claim": "STN低beta、theta活动与FOG易感步态、运动启动、节律和平衡控制有关，但其方向具有频段、解剖区域和时间窗口依赖性。",
   "cited": "PMID:40709562; PMID:42236313; DOI:10.21203/rs.3.rs-9617843/v1",
   "verdict": "consistent",
   "why": "2025年最终同行评审的步态启动研究支持posterior与central STN在低beta调节及pace、rhythm、balance关联方面存在区域差异。2026年Klocke等转弯研究报告实际冻结转弯期间theta功率降低，而正常转弯存在不同的theta调节。2026年认知和情绪研究还在13名患者中发现STN振荡与认知、焦虑和抑郁指标存在关联。总体支持区域和行为阶段依赖性，而不是所有FOG事件具有相同theta或低beta方向。需要注意，这些研究中的部分证据属于预印本，且步态启动研究的LFP分析窗口主要位于冻结之前。"
  },
  {
   "claim": "STN-皮层耦合可能参与FOG发生前后的网络状态转换，但不同频段、脑区和连接指标呈现不同变化。",
   "cited": "PMID:31505548; PMID:41131028",
   "verdict": "consistent",
   "why": "Pozzi等2019年研究支持冻结前及冻结期间theta-alpha皮层-STN去耦合，并观察到恢复行走后重新耦合；同时，冻结开始阶段的beta耦合增强也出现在成功停止行走和通过门洞时。Zhang等2025年19名患者研究发现冻结转弯时PMC-STN alpha coherence增加、M1-STN alpha coherence下降，而beta coherence没有相应显著变化。报告还指出该论文部分冻结持续时间预测结果存在内部统计方向表述问题，这一点有必要保留。证据支持阶段及区域特异性耦合变化，而不是全局同步增强或下降。"
  }
 ]
}

===== S2 / refcheck.json =====
[
 {
  "ref": "PMID:27766724",
  "pmid": "27766724",
  "doi": "10.1111/ene.13167",
  "title": "Effect of high-frequency subthalamic neurostimulation on gait and freezing of gait in Parkinson's disease: a systematic review and meta-analysis.",
  "verdict": "ok",
  "found_title": "Effect of high-frequency subthalamic neurostimulation on gait and freezing of gait in Parkinson's disease: a systematic review and meta-analysis.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:21777828",
  "pmid": "21777828",
  "doi": "10.1016/s1474-4422(11)70143-0",
  "title": "Freezing of gait: moving forward on a mysterious clinical phenomenon.",
  "verdict": "ok",
  "found_title": "Freezing of gait: moving forward on a mysterious clinical phenomenon.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:28529730",
  "pmid": "28529730",
  "doi": "10.1186/s40035-017-0083-7",
  "title": "Effect of low versus high frequency stimulation on freezing of gait and other axial symptoms in Parkinson patients with bilateral STN DBS: a mini-review.",
  "verdict": "ok",
  "found_title": "Effect of low versus high frequency stimulation on freezing of gait and other axial symptoms in Parkinson patients with bilateral STN DBS: a mini-review.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:18413568",
  "pmid": "18413568",
  "doi": "10.1212/01.wnl.0000310416.90757.85",
  "title": "Effects of subthalamic nucleus stimulation and levodopa on freezing of gait in Parkinson disease.",
  "verdict": "ok",
  "found_title": "Effects of subthalamic nucleus stimulation and levodopa on freezing of gait in Parkinson disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:19815246",
  "pmid": "19815246",
  "doi": "10.1016/j.neurol.2009.07.018",
  "title": "[Deep brain stimulation and gait disorders in Parkinson disease].",
  "verdict": "ok",
  "found_title": "[Deep brain stimulation and gait disorders in Parkinson disease].",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:11285786",
  "pmid": "11285786",
  "doi": "",
  "title": "[Gait disorders in Parkinson disease. Gait freezing and falls: therapeutic management].",
  "verdict": "ok",
  "found_title": "[Gait disorders in Parkinson disease. Gait freezing and falls: therapeutic management].",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:26887333",
  "pmid": "26887333",
  "doi": "10.1002/mds.26545",
  "title": "Subthalamic stimulation may inhibit the beneficial effects of levodopa on akinesia and gait.",
  "verdict": "ok",
  "found_title": "Subthalamic stimulation may inhibit the beneficial effects of levodopa on akinesia and gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:23445615",
  "pmid": "23445615",
  "doi": "10.1159/000346432",
  "title": "Levodopa-resistant freezing of gait and executive dysfunction in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Levodopa-resistant freezing of gait and executive dysfunction in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:30153383",
  "pmid": "30153383",
  "doi": "10.1002/mds.27417",
  "title": "Evidence for subtypes of freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Evidence for subtypes of freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:31755599",
  "pmid": "31755599",
  "doi": "10.1002/mds.27892",
  "title": "Deep Brain Stimulation for Freezing of Gait in Parkinson's Disease With Early Motor Complications.",
  "verdict": "ok",
  "found_title": "Deep Brain Stimulation for Freezing of Gait in Parkinson's Disease With Early Motor Complications.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:33027712",
  "pmid": "33027712",
  "doi": "10.1016/j.parkreldis.2020.09.043",
  "title": "Clinical patterns of gait freezing in Parkinson's disease and their response to interventions: An observer-blinded study.",
  "verdict": "ok",
  "found_title": "Clinical patterns of gait freezing in Parkinson's disease and their response to interventions: An observer-blinded study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:31647540",
  "pmid": "31647540",
  "doi": "10.1093/brain/awz314",
  "title": "Freezing of gait: understanding the complexity of an enigmatic phenomenon.",
  "verdict": "ok",
  "found_title": "Freezing of gait: understanding the complexity of an enigmatic phenomenon.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:31275238",
  "pmid": "31275238",
  "doi": "10.3389/fneur.2019.00659",
  "title": "New Onset On-Medication Freezing of Gait After STN-DBS in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "New Onset On-Medication Freezing of Gait After STN-DBS in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35418844",
  "pmid": "35418844",
  "doi": "10.3389/fnhum.2022.788200",
  "title": "Subthalamic Deep Brain Stimulation Lead Asymmetry Impacts the Parkinsonian Gait Disorder.",
  "verdict": "ok",
  "found_title": "Subthalamic Deep Brain Stimulation Lead Asymmetry Impacts the Parkinsonian Gait Disorder.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35431262",
  "pmid": "35431262",
  "doi": "10.3233/jpd-212997",
  "title": "Structural Connectivity of Subthalamic Nucleus Stimulation for Improving Freezing of Gait.",
  "verdict": "ok",
  "found_title": "Structural Connectivity of Subthalamic Nucleus Stimulation for Improving Freezing of Gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36242900",
  "pmid": "36242900",
  "doi": "10.1016/j.parkreldis.2022.10.002",
  "title": "Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients.",
  "verdict": "ok",
  "found_title": "Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36211167",
  "pmid": "36211167",
  "doi": "10.4103/aian.aian_980_21",
  "title": "Dramatic Recovery of Freezing of Gait with Subthalamic Nucleus Deep Brain Stimulation.",
  "verdict": "ok",
  "found_title": "Dramatic Recovery of Freezing of Gait with Subthalamic Nucleus Deep Brain Stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35490252",
  "pmid": "35490252",
  "doi": "10.1186/s40035-022-00298-x",
  "title": "Stepping up to meet the challenge of freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Stepping up to meet the challenge of freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35017551",
  "pmid": "35017551",
  "doi": "10.1038/s41531-021-00276-6",
  "title": "Gaps and roadmap of novel neuromodulation targets for treatment of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Gaps and roadmap of novel neuromodulation targets for treatment of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36185822",
  "pmid": "36185822",
  "doi": "10.3389/fnsys.2022.995375",
  "title": "Abnormal neural oscillations during gait and dual-task in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Abnormal neural oscillations during gait and dual-task in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35310098",
  "pmid": "35310098",
  "doi": "10.3389/fnins.2022.795417",
  "title": "Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait.",
  "verdict": "ok",
  "found_title": "Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36070366",
  "pmid": "36070366",
  "doi": "10.1126/scitranslmed.abo1800",
  "title": "Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37701817",
  "pmid": "37701817",
  "doi": "10.1093/braincomms/fcad238",
  "title": "Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37304345",
  "pmid": "37304345",
  "doi": "10.1016/j.ibneur.2023.05.008",
  "title": "Deep brain stimulation (DBS) as a therapeutic approach in gait disorders: What does it bring to the table?",
  "verdict": "ok",
  "found_title": "Deep brain stimulation (DBS) as a therapeutic approach in gait disorders: What does it bring to the table?",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.21203/rs.3.rs-4058858/v1",
  "pmid": "",
  "doi": "10.21203/rs.3.rs-4058858/v1",
  "title": "The effect of Levodopa and Stimulation on post-surgery Freezing of Gait in STN-DBS Parkinson's Disease patients: a clinical and kinematic analysis",
  "verdict": "ok",
  "found_title": "The effect of Levodopa and Stimulation on post-surgery Freezing of Gait in STN-DBS Parkinson's Disease patients: a clinical and kinematic analysis",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40496972",
  "pmid": "40496972",
  "doi": "10.3389/fnagi.2025.1511845",
  "title": "Predictive model for the therapeutic effect of bilateral subthalamic nucleus deep brain stimulation on the freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Predictive model for the therapeutic effect of bilateral subthalamic nucleus deep brain stimulation on the freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40504072",
  "pmid": "40504072",
  "doi": "10.1002/mdc3.70170",
  "title": "Differential Effects of Levodopa and Stimulation on Post-Surgery Freezing of Gait in Subthalamic Nucleus Deep Brain Stimulation Parkinson's Disease Patients: A Clinical and Kinematic Analysis.",
  "verdict": "ok",
  "found_title": "Differential Effects of Levodopa and Stimulation on Post-Surgery Freezing of Gait in Subthalamic Nucleus Deep Brain Stimulation Parkinson's Disease Patients: A Clinical and Kinematic Analysis.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40092840",
  "pmid": "40092840",
  "doi": "10.1136/bmjno-2024-000898",
  "title": "Gait and balance worsening after bilateral deep brain stimulation of the subthalamic nucleus (STN-DBS) for Parkinson's disease: a systematic review.",
  "verdict": "ok",
  "found_title": "Gait and balance worsening after bilateral deep brain stimulation of the subthalamic nucleus (STN-DBS) for Parkinson's disease: a systematic review.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40926219",
  "pmid": "40926219",
  "doi": "10.1186/s12984-025-01712-x",
  "title": "Nigral stimulation for freezing of gait: kinematic gait parameters inform optimization of stimulation frequency.",
  "verdict": "ok",
  "found_title": "Nigral stimulation for freezing of gait: kinematic gait parameters inform optimization of stimulation frequency.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41659700",
  "pmid": "41659700",
  "doi": "10.3389/fnagi.2025.1723706",
  "title": "Effects of different types of deep brain stimulation on gait disorders in patients with Parkinson's disease: a network meta-analysis of randomized controlled trials.",
  "verdict": "ok",
  "found_title": "Effects of different types of deep brain stimulation on gait disorders in patients with Parkinson's disease: a network meta-analysis of randomized controlled trials.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40992964",
  "pmid": "40992964",
  "doi": "10.1016/j.parkreldis.2025.108062",
  "title": "Subthalamic deep brain stimulation alleviates the gait sequence effect and freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Subthalamic deep brain stimulation alleviates the gait sequence effect and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41865085",
  "pmid": "41865085",
  "doi": "10.1007/s00415-026-13765-6",
  "title": "What is new in Freezing of Gait?",
  "verdict": "ok",
  "found_title": "What is new in Freezing of Gait?",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41553951",
  "pmid": "41553951",
  "doi": "10.1159/000549859",
  "title": "Simultaneous High-Frequency Subthalamic and Ultra-Low-Frequency Nigral Deep Brain Stimulation Improved Motor Symptoms and Freezing of Gait in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Simultaneous High-Frequency Subthalamic and Ultra-Low-Frequency Nigral Deep Brain Stimulation Improved Motor Symptoms and Freezing of Gait in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42098512",
  "pmid": "42098512",
  "doi": "10.1007/s10143-026-04312-y",
  "title": "Deep brain stimulation for freezing of gait in Parkinson's disease: An updated systematic review, meta-analysis, and a single-center clinical experience.",
  "verdict": "ok",
  "found_title": "Deep brain stimulation for freezing of gait in Parkinson's disease: An updated systematic review, meta-analysis, and a single-center clinical experience.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42403079",
  "pmid": "42403079",
  "doi": "10.1111/ejn.70610",
  "title": "Freezing of Gait Levodopa Response Pattern in Parkinson's Disease Provides Clues to Pathophysiology.",
  "verdict": "ok",
  "found_title": "Freezing of Gait Levodopa Response Pattern in Parkinson's Disease Provides Clues to Pathophysiology.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42045915",
  "pmid": "42045915",
  "doi": "10.1186/s12984-026-01997-6",
  "title": "Using explainable AI to identify disease-relevant and deep brain stimulation treatment-sensitive gait features in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Using explainable AI to identify disease-relevant and deep brain stimulation treatment-sensitive gait features in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42207737",
  "pmid": "42207737",
  "doi": "10.1159/000551518",
  "title": "Changes in Gait among Patients with Parkinson's Disease Treated with Deep Brain Stimulation: A Systematic Review and Meta-Analysis.",
  "verdict": "ok",
  "found_title": "Changes in Gait among Patients with Parkinson's Disease Treated with Deep Brain Stimulation: A Systematic Review and Meta-Analysis.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42240331",
  "pmid": "42240331",
  "doi": "10.1177/15459683261448483",
  "title": "Low-Frequency STN-DBS for Standing and Gait Initiation in Parkinson's Disease: A Double-Blinded Randomised Cross-Over Feasibility Trial.",
  "verdict": "ok",
  "found_title": "Low-Frequency STN-DBS for Standing and Gait Initiation in Parkinson's Disease: A Double-Blinded Randomised Cross-Over Feasibility Trial.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42297979",
  "pmid": "42297979",
  "doi": "10.1038/s41591-026-04432-4",
  "title": "Activity-dependent adaptive deep brain stimulation improves gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Activity-dependent adaptive deep brain stimulation improves gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42860886",
  "pmid": "42860886",
  "doi": "10.1002/mdc3.70813",
  "title": "Disease Duration Differentiates Freezing of Gait Response to Subthalamic and Nigral Stimulation for Parkinson's Disease in an Exploratory Multicenter Controlled Trial.",
  "verdict": "ok",
  "found_title": "Disease Duration Differentiates Freezing of Gait Response to Subthalamic and Nigral Stimulation for Parkinson's Disease in an Exploratory Multicenter Controlled Trial.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40512756",
  "pmid": "40512756",
  "doi": "10.1093/brain/awaf231",
  "title": "Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Cholinergic patterns correlate with dopamine medication ON freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40635563",
  "pmid": "40635563",
  "doi": "10.1002/mds.30259",
  "title": "Disease-Modifying Trials in Treated Parkinson's Disease: \"Stable Treated\" Does Not Equate with Biological Stability.",
  "verdict": "ok",
  "found_title": "Disease-Modifying Trials in Treated Parkinson's Disease: \"Stable Treated\" Does Not Equate with Biological Stability.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40383539",
  "pmid": "40383539",
  "doi": "10.1177/1877718x251320941",
  "title": "Effects of theta burst stimulation on the Parkinsonian gait disorder and cortical gait-network activity.",
  "verdict": "ok",
  "found_title": "Effects of theta burst stimulation on the Parkinsonian gait disorder and cortical gait-network activity.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42211297",
  "pmid": "42211297",
  "doi": "10.3389/fneur.2026.1767807",
  "title": "A multimodal machine learning model for predicting postoperative worsening of FOGQ in Parkinson's disease following STN-DBS.",
  "verdict": "ok",
  "found_title": "A multimodal machine learning model for predicting postoperative worsening of FOGQ in Parkinson's disease following STN-DBS.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42823526",
  "pmid": "42823526",
  "doi": "10.1007/s00415-026-14160-x",
  "title": "Non-motor symptoms burden and motor recovery following STN-DBS in Parkinson's disease: a data-driven longitudinal analysis.",
  "verdict": "ok",
  "found_title": "Non-motor symptoms burden and motor recovery following STN-DBS in Parkinson's disease: a data-driven longitudinal analysis.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42185340",
  "pmid": "42185340",
  "doi": "10.1038/s41531-026-01406-8",
  "title": "Machine learning-based optimization of dual subthalamic nucleus and substantia nigra targeting in deep brain stimulation.",
  "verdict": "ok",
  "found_title": "Machine learning-based optimization of dual subthalamic nucleus and substantia nigra targeting in deep brain stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42058451",
  "pmid": "42058451",
  "doi": "10.1016/j.prdoa.2026.100444",
  "title": "Gait and balance deterioration following deep brain stimulation in Parkinson's disease: a counterfactual review.",
  "verdict": "ok",
  "found_title": "Gait and balance deterioration following deep brain stimulation in Parkinson's disease: a counterfactual review.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:18420482",
  "pmid": "18420482",
  "doi": "10.1212/01.wnl.0000303972.16279.46",
  "title": "STN-DBS frequency effects on freezing of gait in advanced Parkinson disease.",
  "verdict": "ok",
  "found_title": "STN-DBS frequency effects on freezing of gait in advanced Parkinson disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:25540305",
  "pmid": "25540305",
  "doi": "10.1212/wnl.0000000000001184",
  "title": "Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD.",
  "verdict": "ok",
  "found_title": "Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:24165197",
  "pmid": "24165197",
  "doi": "10.1111/ner.12131",
  "title": "60-Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation.",
  "verdict": "ok",
  "found_title": "60-Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:30100532",
  "pmid": "30100532",
  "doi": "10.1016/j.clinph.2018.07.013",
  "title": "Decreasing subthalamic deep brain stimulation frequency reverses cognitive interference during gait initiation in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Decreasing subthalamic deep brain stimulation frequency reverses cognitive interference during gait initiation in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:30262859",
  "pmid": "30262859",
  "doi": "10.1038/s41598-018-32161-3",
  "title": "Frequency-dependent effects of subthalamic deep brain stimulation on motor symptoms in Parkinson's disease: a meta-analysis of controlled trials.",
  "verdict": "ok",
  "found_title": "Frequency-dependent effects of subthalamic deep brain stimulation on motor symptoms in Parkinson's disease: a meta-analysis of controlled trials.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:30637270",
  "pmid": "30637270",
  "doi": "10.1002/mdc3.12658",
  "title": "Deep Brain Stimulation at Variable Frequency to Improve Motor Outcomes in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Deep Brain Stimulation at Variable Frequency to Improve Motor Outcomes in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38579455",
  "pmid": "38579455",
  "doi": "10.1016/j.neurot.2024.e00348",
  "title": "Neuroscience fundamentals relevant to neuromodulation: Neurobiology of deep brain stimulation in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Neuroscience fundamentals relevant to neuromodulation: Neurobiology of deep brain stimulation in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37970314",
  "pmid": "37970314",
  "doi": "10.4103/aian.aian_95_23",
  "title": "Changes in Optimal Stimulation Frequency with Time for Gait Disturbances in Patients with PD after STN-DBS-A Longitudinal Study.",
  "verdict": "ok",
  "found_title": "Changes in Optimal Stimulation Frequency with Time for Gait Disturbances in Patients with PD after STN-DBS-A Longitudinal Study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39223361",
  "pmid": "39223361",
  "doi": "10.1007/s10143-024-02761-x",
  "title": "Efficacy of subthalamic deep brain stimulation programming strategies for gait disorders in Parkinson's disease: a systematic review and meta-analysis.",
  "verdict": "ok",
  "found_title": "Efficacy of subthalamic deep brain stimulation programming strategies for gait disorders in Parkinson's disease: a systematic review and meta-analysis.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38948151",
  "pmid": "38948151",
  "doi": "10.1093/nsr/nwae187",
  "title": "Variable frequency deep brain stimulation of subthalamic nucleus to improve freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Variable frequency deep brain stimulation of subthalamic nucleus to improve freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.64898/2025.12.17.25342333",
  "pmid": "",
  "doi": "10.64898/2025.12.17.25342333",
  "title": "Low-Frequency Adaptive Deep Brain Stimulation for Parkinson’s Disease",
  "verdict": "ok",
  "found_title": "Low-Frequency Adaptive Deep Brain Stimulation for Parkinson’s Disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:32246798",
  "pmid": "32246798",
  "doi": "10.1002/mds.28048",
  "title": "A Novel DBS Paradigm for Axial Features in Parkinson's Disease: A Randomized Crossover Study.",
  "verdict": "ok",
  "found_title": "A Novel DBS Paradigm for Axial Features in Parkinson's Disease: A Randomized Crossover Study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:33240199",
  "pmid": "33240199",
  "doi": "10.3389/fneur.2020.571086",
  "title": "Neural Correlates of Freezing of Gait in Parkinson's Disease: An Electrophysiology Mini-Review.",
  "verdict": "ok",
  "found_title": "Neural Correlates of Freezing of Gait in Parkinson's Disease: An Electrophysiology Mini-Review.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40918851",
  "pmid": "40918851",
  "doi": "10.7759/cureus.89437",
  "title": "A Case of Acute-Onset, Refractory Freezing of Gait Following Subthalamic Nucleus Deep Brain Stimulation Adjustment.",
  "verdict": "ok",
  "found_title": "A Case of Acute-Onset, Refractory Freezing of Gait Following Subthalamic Nucleus Deep Brain Stimulation Adjustment.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41383649",
  "pmid": "41383649",
  "doi": "10.1093/braincomms/fcaf474",
  "title": "20 Hz beta stimulation of the subthalamic nucleus improves response inhibition in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "20 Hz beta stimulation of the subthalamic nucleus improves response inhibition in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42968793",
  "pmid": "42968793",
  "doi": "10.1136/bmjcsurg-2026-000033",
  "title": "Superiority of dual-target STN-SNr deep brain stimulation towards gait in Parkinson's disease: a meta-analysis and meta-regression of randomised trials.",
  "verdict": "ok",
  "found_title": "Superiority of dual-target STN-SNr deep brain stimulation towards gait in Parkinson's disease: a meta-analysis and meta-regression of randomised trials.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35173666",
  "pmid": "35173666",
  "doi": "10.3389/fneur.2021.786166",
  "title": "Non-motor Adverse Effects Avoided by Directional Stimulation in Parkinson's Disease: A Case Report.",
  "verdict": "ok",
  "found_title": "Non-motor Adverse Effects Avoided by Directional Stimulation in Parkinson's Disease: A Case Report.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:34858125",
  "pmid": "34858125",
  "doi": "10.3389/fnins.2021.733203",
  "title": "Differential Effects of Pathological Beta Burst Dynamics Between Parkinson's Disease Phenotypes Across Different Movements.",
  "verdict": "ok",
  "found_title": "Differential Effects of Pathological Beta Burst Dynamics Between Parkinson's Disease Phenotypes Across Different Movements.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39475137",
  "pmid": "39475137",
  "doi": "10.1002/ana.27099",
  "title": "Directional Subthalamic Deep Brain Stimulation Better Improves Gait and Balance Disorders in Parkinson's Disease Patients: A Randomized Controlled Study.",
  "verdict": "ok",
  "found_title": "Directional Subthalamic Deep Brain Stimulation Better Improves Gait and Balance Disorders in Parkinson's Disease Patients: A Randomized Controlled Study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40117663",
  "pmid": "40117663",
  "doi": "10.3171/2024.10.jns241470",
  "title": "Enhancement of gait improvement in Parkinson disease with anterior subthalamic nucleus deep brain stimulation.",
  "verdict": "ok",
  "found_title": "Enhancement of gait improvement in Parkinson disease with anterior subthalamic nucleus deep brain stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40274625",
  "pmid": "40274625",
  "doi": "10.1007/s00702-025-02931-1",
  "title": "Ventral STN stimulation is associated with improved axial motor outcomes in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Ventral STN stimulation is associated with improved axial motor outcomes in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40408848",
  "pmid": "40408848",
  "doi": "10.1016/j.parkreldis.2025.107871",
  "title": "Probabilistic mapping of gait changes after STN-DBS for Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Probabilistic mapping of gait changes after STN-DBS for Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41594737",
  "pmid": "41594737",
  "doi": "10.3390/brainsci16010016",
  "title": "Symptom-Specific Networks and the DBS-Modulated Network in Parkinson's Disease: A Connectivity-Based Review.",
  "verdict": "ok",
  "found_title": "Symptom-Specific Networks and the DBS-Modulated Network in Parkinson's Disease: A Connectivity-Based Review.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41261259",
  "pmid": "41261259",
  "doi": "10.1007/s00415-025-13521-2",
  "title": "Altered pedunculopontine pathways in freezing of gait: a diffusion tensor imaging study based on dopaminergic degeneration status.",
  "verdict": "ok",
  "found_title": "Altered pedunculopontine pathways in freezing of gait: a diffusion tensor imaging study based on dopaminergic degeneration status.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41654501",
  "pmid": "41654501",
  "doi": "10.1038/s41531-026-01280-4",
  "title": "Deep neurobehavioral phenotyping uncovers neural fingerprints of locomotor deficits in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Deep neurobehavioral phenotyping uncovers neural fingerprints of locomotor deficits in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.1101/2025.01.10.632393",
  "pmid": "",
  "doi": "10.1101/2025.01.10.632393",
  "title": "Subthalamic Signature of Freezing of Gait in Parkinson’s Disease",
  "verdict": "ok",
  "found_title": "Subthalamic Signature of Freezing of Gait in Parkinson’s Disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40072634",
  "pmid": "40072634",
  "doi": "10.1007/s00415-025-13000-8",
  "title": "Could adaptive deep brain stimulation treat freezing of gait in Parkinson's disease?",
  "verdict": "ok",
  "found_title": "Could adaptive deep brain stimulation treat freezing of gait in Parkinson's disease?",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40709562",
  "pmid": "40709562",
  "doi": "10.1002/ana.70003",
  "title": "Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:24361601",
  "pmid": "24361601",
  "doi": "10.1016/j.nbd.2013.12.005",
  "title": "High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:28890315",
  "pmid": "28890315",
  "doi": "10.1016/j.nbd.2017.09.002",
  "title": "Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:30196050",
  "pmid": "30196050",
  "doi": "10.1016/j.nbd.2018.09.004",
  "title": "Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:23861319",
  "pmid": "23861319",
  "doi": "10.1093/cercor/bht170",
  "title": "The neural correlates of upper limb motor blocks in Parkinson's disease and their relation to freezing of gait.",
  "verdict": "ok",
  "found_title": "The neural correlates of upper limb motor blocks in Parkinson's disease and their relation to freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:24142148",
  "pmid": "24142148",
  "doi": "10.1093/brain/awt272",
  "title": "Freezing of gait in Parkinson's disease is associated with functional decoupling between the cognitive control network and the basal ganglia.",
  "verdict": "ok",
  "found_title": "Freezing of gait in Parkinson's disease is associated with functional decoupling between the cognitive control network and the basal ganglia.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39466340",
  "pmid": "39466340",
  "doi": "10.1007/s43440-024-00673-7",
  "title": "Effects of puerarin on gait disturbance in a 6-hydroxydopamine mouse model of Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Effects of puerarin on gait disturbance in a 6-hydroxydopamine mouse model of Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39965098",
  "pmid": "39965098",
  "doi": "10.1093/brain/awaf063",
  "title": "Low β predicts motor output and cell degeneration in the A53T Parkinson's disease rat model.",
  "verdict": "ok",
  "found_title": "Low β predicts motor output and cell degeneration in the A53T Parkinson's disease rat model.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39470410",
  "pmid": "39470410",
  "doi": "10.1093/brain/awae223",
  "title": "Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.1101/2025.05.08.25327015",
  "pmid": "",
  "doi": "10.1101/2025.05.08.25327015",
  "title": "Subthalamic Nucleus Deep Brain Stimulation Alleviates the Sequence Effect and Freezing of Gait in Parkinson’s Disease",
  "verdict": "ok",
  "found_title": "Subthalamic Nucleus Deep Brain Stimulation Alleviates the Sequence Effect and Freezing of Gait in Parkinson’s Disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39957196",
  "pmid": "39957196",
  "doi": "10.1177/1877718x241292315",
  "title": "Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial.",
  "verdict": "ok",
  "found_title": "Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40648292",
  "pmid": "40648292",
  "doi": "10.3390/s25134036",
  "title": "An Experimental Approach for Investigating Freezing of Gait in Parkinson's Disease Using Virtual Reality and Neural Sensing: A Pilot Study.",
  "verdict": "ok",
  "found_title": "An Experimental Approach for Investigating Freezing of Gait in Parkinson's Disease Using Virtual Reality and Neural Sensing: A Pilot Study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40677701",
  "pmid": "40677701",
  "doi": "10.1093/braincomms/fcaf266",
  "title": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42239677",
  "pmid": "42239677",
  "doi": "10.3389/fneur.2026.1793291",
  "title": "An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42829632",
  "pmid": "42829632",
  "doi": "10.25259/sni_176_2026",
  "title": "Local field potential biomarkers for adaptive deep brain stimulation in Parkinson's disease: A scoping review.",
  "verdict": "ok",
  "found_title": "Local field potential biomarkers for adaptive deep brain stimulation in Parkinson's disease: A scoping review.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42571859",
  "pmid": "42571859",
  "doi": "10.1016/j.nbd.2026.107571",
  "title": "Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:31505548",
  "pmid": "31505548",
  "doi": "10.1093/brain/awz141",
  "title": "Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics.",
  "verdict": "ok",
  "found_title": "Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:31665229",
  "pmid": "31665229",
  "doi": "10.1093/brain/awz325",
  "title": "Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing.",
  "verdict": "ok",
  "found_title": "Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:31494286",
  "pmid": "31494286",
  "doi": "10.1016/j.nbd.2019.104605",
  "title": "Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36730026",
  "pmid": "36730026",
  "doi": "10.1093/brain/awad006",
  "title": "Subthalamic and nigral neurons are differentially modulated during parkinsonian gait.",
  "verdict": "ok",
  "found_title": "Subthalamic and nigral neurons are differentially modulated during parkinsonian gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37860957",
  "pmid": "37860957",
  "doi": "10.1002/mds.29632",
  "title": "Active and Passive Cycling Decrease Subthalamic β Oscillations in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Active and Passive Cycling Decrease Subthalamic β Oscillations in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.1101/2024.06.26.24309418",
  "pmid": "",
  "doi": "10.1101/2024.06.26.24309418",
  "title": "Beta Burst-Driven Adaptive Deep Brain Stimulation Improves Gait Impairment and Freezing of Gait in Parkinson’s Disease",
  "verdict": "ok",
  "found_title": "Beta Burst-Driven Adaptive Deep Brain Stimulation Improves Gait Impairment and Freezing of Gait in Parkinson’s Disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36810199",
  "pmid": "36810199",
  "doi": "10.7554/elife.82467",
  "title": "The aperiodic exponent of subthalamic field potentials reflects excitation/inhibition balance in Parkinsonism.",
  "verdict": "ok",
  "found_title": "The aperiodic exponent of subthalamic field potentials reflects excitation/inhibition balance in Parkinsonism.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37273691",
  "pmid": "37273691",
  "doi": "10.3389/fneur.2023.1163811",
  "title": "Case report: Bilateral double beta peak activity is influenced by stimulation, levodopa concentrations, and motor tasks, in a Parkinson's disease patient on chronic deep brain stimulation.",
  "verdict": "ok",
  "found_title": "Case report: Bilateral double beta peak activity is influenced by stimulation, levodopa concentrations, and motor tasks, in a Parkinson's disease patient on chronic deep brain stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37888906",
  "pmid": "37888906",
  "doi": "10.1002/mds.29634",
  "title": "Paradoxical Modulation of STN β-Band Activity with Medication Compared to Deep Brain Stimulation.",
  "verdict": "ok",
  "found_title": "Paradoxical Modulation of STN β-Band Activity with Medication Compared to Deep Brain Stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39884164",
  "pmid": "39884164",
  "doi": "10.1016/j.clinph.2025.01.005",
  "title": "Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.1101/2025.01.01.631000",
  "pmid": "",
  "doi": "10.1101/2025.01.01.631000",
  "title": "The role of STN beta oscillations on lower extremity muscle activity in Parkinsonian stepping",
  "verdict": "ok",
  "found_title": "The role of STN beta oscillations on lower extremity muscle activity in Parkinsonian stepping",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.64898/2026.08.13.744293",
  "pmid": "",
  "doi": "10.64898/2026.08.13.744293",
  "title": "Reduced entropy of subthalamic beta bursts predicts freezing of gait in Parkinson’s disease",
  "verdict": "ok",
  "found_title": "Reduced entropy of subthalamic beta bursts predicts freezing of gait in Parkinson’s disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41388789",
  "pmid": "41388789",
  "doi": "10.1093/brain/awaf464",
  "title": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping.",
  "verdict": "ok",
  "found_title": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41557560",
  "pmid": "41557560",
  "doi": "10.1159/000550545",
  "title": "Local Field Potentials in Movement Disorders: A Narrative Review.",
  "verdict": "ok",
  "found_title": "Local Field Potentials in Movement Disorders: A Narrative Review.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.21203/rs.3.rs-9617843/v1",
  "pmid": "",
  "doi": "10.21203/rs.3.rs-9617843/v1",
  "title": "Subthalamic Signatures of Freezing while Turning in Parkinson’s Disease",
  "verdict": "ok",
  "found_title": "Subthalamic Signatures of Freezing while Turning in Parkinson’s Disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42422531",
  "pmid": "42422531",
  "doi": "10.1093/braincomms/fcag245",
  "title": "Reduced pre-movement subthalamic beta desynchronization marks motor deficit in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Reduced pre-movement subthalamic beta desynchronization marks motor deficit in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42580034",
  "pmid": "42580034",
  "doi": "10.1016/j.ebiom.2026.106418",
  "title": "Corticostriatal glutamate mechanisms underlying beta synchrony and motor deficits via striatal NMDA receptors in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Corticostriatal glutamate mechanisms underlying beta synchrony and motor deficits via striatal NMDA receptors in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42236313",
  "pmid": "42236313",
  "doi": "10.1111/ejn.70570",
  "title": "Cognitive and Emotional Determinants of Subthalamic Oscillations During Freezing While Turning in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Cognitive and Emotional Determinants of Subthalamic Oscillations During Freezing While Turning in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36270803",
  "pmid": "36270803",
  "doi": "10.1523/eneuro.0325-22.2022",
  "title": "Cortico-Subthalamic Field Potentials Support Classification of the Natural Gait Cycle in Parkinson's Disease and Reveal Individualized Spectral Signatures.",
  "verdict": "ok",
  "found_title": "Cortico-Subthalamic Field Potentials Support Classification of the Natural Gait Cycle in Parkinson's Disease and Reveal Individualized Spectral Signatures.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37226972",
  "pmid": "37226972",
  "doi": "10.1002/mds.29455",
  "title": "Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40640214",
  "pmid": "40640214",
  "doi": "10.1038/s41531-025-01067-z",
  "title": "Theta-frequency subthalamic stimulation enhances conflict resolution in Parkinson's disease patients with freezing of gait through frontal cortex modulation.",
  "verdict": "ok",
  "found_title": "Theta-frequency subthalamic stimulation enhances conflict resolution in Parkinson's disease patients with freezing of gait through frontal cortex modulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41131028",
  "pmid": "41131028",
  "doi": "10.1038/s41531-025-01173-y",
  "title": "Neural signatures of turn-induced freezing of gait in Parkinson's disease: insights from phase-specific cortico-subthalamic dynamics.",
  "verdict": "ok",
  "found_title": "Neural signatures of turn-induced freezing of gait in Parkinson's disease: insights from phase-specific cortico-subthalamic dynamics.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:23039143",
  "pmid": "23039143",
  "doi": "10.3171/2012.8.jns112006",
  "title": "Effects of deep brain stimulation in the subthalamic nucleus or globus pallidus internus on step initiation in Parkinson disease: laboratory investigation.",
  "verdict": "ok",
  "found_title": "Effects of deep brain stimulation in the subthalamic nucleus or globus pallidus internus on step initiation in Parkinson disease: laboratory investigation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38636820",
  "pmid": "38636820",
  "doi": "10.1016/j.brs.2024.04.006",
  "title": "Auditory cues modulate the short timescale dynamics of STN activity during stepping in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Auditory cues modulate the short timescale dynamics of STN activity during stepping in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38135193",
  "pmid": "38135193",
  "doi": "10.1016/j.nbd.2023.106384",
  "title": "Subthalamic and pallidal neurons are modulated during externally cued movements in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Subthalamic and pallidal neurons are modulated during externally cued movements in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38509158",
  "pmid": "38509158",
  "doi": "10.1038/s41598-024-57252-2",
  "title": "Gait-related beta-gamma phase amplitude coupling in the subthalamic nucleus of parkinsonian patients.",
  "verdict": "ok",
  "found_title": "Gait-related beta-gamma phase amplitude coupling in the subthalamic nucleus of parkinsonian patients.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39755754",
  "pmid": "39755754",
  "doi": "10.1038/s41746-024-01364-6",
  "title": "N2GNet tracks gait performance from subthalamic neural signals in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "N2GNet tracks gait performance from subthalamic neural signals in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.1101/2025.08.20.25333478",
  "pmid": "",
  "doi": "10.1101/2025.08.20.25333478",
  "title": "Subthalamic nucleus encoding steers adaptive therapies for gait in Parkinson’s disease",
  "verdict": "ok",
  "found_title": "Subthalamic nucleus encoding steers adaptive therapies for gait in Parkinson’s disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:32634599",
  "pmid": "32634599",
  "doi": "10.1016/j.brs.2020.06.018",
  "title": "Neural closed-loop deep brain stimulation for freezing of gait.",
  "verdict": "ok",
  "found_title": "Neural closed-loop deep brain stimulation for freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37429355",
  "pmid": "37429355",
  "doi": "10.1016/j.brs.2023.07.003",
  "title": "Kinematic adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Kinematic adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:37932548",
  "pmid": "37932548",
  "doi": "10.1038/s41591-023-02584-1",
  "title": "A spinal cord neuroprosthesis for locomotor deficits due to Parkinson's disease.",
  "verdict": "ok",
  "found_title": "A spinal cord neuroprosthesis for locomotor deficits due to Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41741462",
  "pmid": "41741462",
  "doi": "10.1038/s41531-026-01269-z",
  "title": "Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles.",
  "verdict": "ok",
  "found_title": "Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41810591",
  "pmid": "41810591",
  "doi": "10.1002/mds.70261",
  "title": "Stimulation and Medication Effects on Subthalamic Nucleus Beta-Band Power in Parkinson's Disease: Implications for Adaptive Deep Brain Stimulation.",
  "verdict": "ok",
  "found_title": "Stimulation and Medication Effects on Subthalamic Nucleus Beta-Band Power in Parkinson's Disease: Implications for Adaptive Deep Brain Stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:24937008",
  "pmid": "24937008",
  "doi": "10.1371/journal.pone.0100291",
  "title": "Functional reorganization of the locomotor network in Parkinson patients with freezing of gait.",
  "verdict": "ok",
  "found_title": "Functional reorganization of the locomotor network in Parkinson patients with freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:28119584",
  "pmid": "28119584",
  "doi": "10.3389/fnhum.2016.00649",
  "title": "A Neurocomputational Model of the Effect of Cognitive Load on Freezing of Gait in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "A Neurocomputational Model of the Effect of Cognitive Load on Freezing of Gait in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35441231",
  "pmid": "35441231",
  "doi": "10.1093/brain/awac121",
  "title": "Cortical phase-amplitude coupling is key to the occurrence and treatment of freezing of gait.",
  "verdict": "ok",
  "found_title": "Cortical phase-amplitude coupling is key to the occurrence and treatment of freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35917720",
  "pmid": "35917720",
  "doi": "10.1016/j.nicl.2022.103123",
  "title": "Imaging the neural underpinnings of freezing of gait in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Imaging the neural underpinnings of freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39464215",
  "pmid": "39464215",
  "doi": "10.1093/braincomms/fcae246",
  "title": "Cerebellar activity in hemi-parkinsonian rats during volitional gait and freezing.",
  "verdict": "ok",
  "found_title": "Cerebellar activity in hemi-parkinsonian rats during volitional gait and freezing.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39606789",
  "pmid": "39606789",
  "doi": "10.3389/fnhum.2024.1495272",
  "title": "Beta-gamma phase-amplitude coupling of scalp electroencephalography during walking preparation in Parkinson's disease differs depending on the freezing of gait.",
  "verdict": "ok",
  "found_title": "Beta-gamma phase-amplitude coupling of scalp electroencephalography during walking preparation in Parkinson's disease differs depending on the freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39759396",
  "pmid": "39759396",
  "doi": "10.3389/fnagi.2024.1458005",
  "title": "Attenuated afferent inhibition correlated with impaired gait performance in Parkinson's disease patients with freezing of gait.",
  "verdict": "ok",
  "found_title": "Attenuated afferent inhibition correlated with impaired gait performance in Parkinson's disease patients with freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39973482",
  "pmid": "39973482",
  "doi": "10.1177/1877718x241305713",
  "title": "Metabolic connectivity of freezing in Parkinson's disease.",
  "verdict": "ok",
  "found_title": "Metabolic connectivity of freezing in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40538160",
  "pmid": "40538160",
  "doi": "10.1177/1877718x251348669",
  "title": "Unveiling the neural network of freezing of gait in Parkinson's disease: A coordinate-based network study.",
  "verdict": "ok",
  "found_title": "Unveiling the neural network of freezing of gait in Parkinson's disease: A coordinate-based network study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40678756",
  "pmid": "40678756",
  "doi": "10.3389/fnins.2025.1560333",
  "title": "Gait dynamics and brain function abnormalities in Parkinson's disease with freezing of gait: a clinical study using resting-state fMRI and wearable devices.",
  "verdict": "ok",
  "found_title": "Gait dynamics and brain function abnormalities in Parkinson's disease with freezing of gait: a clinical study using resting-state fMRI and wearable devices.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41415889",
  "pmid": "41415889",
  "doi": "10.3389/fnagi.2025.1695806",
  "title": "Abnormal subthalamic nucleus functional connectivity and machine learning classification in Parkinson's disease: a multisite functional magnetic resonance imaging study.",
  "verdict": "ok",
  "found_title": "Abnormal subthalamic nucleus functional connectivity and machine learning classification in Parkinson's disease: a multisite functional magnetic resonance imaging study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41420410",
  "pmid": "41420410",
  "doi": "10.1111/ejn.70374",
  "title": "Cognitive-Motor Conflict During Step Initiation: Neural and Biomechanical Insights Into Freezing of Gait in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Cognitive-Motor Conflict During Step Initiation: Neural and Biomechanical Insights Into Freezing of Gait in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42641912",
  "pmid": "42641912",
  "doi": "10.1016/j.neuroscience.2026.08.038",
  "title": "Midfrontal oscillatory alterations during gait imagination and observation in Parkinson's disease with freezing of gait.",
  "verdict": "ok",
  "found_title": "Midfrontal oscillatory alterations during gait imagination and observation in Parkinson's disease with freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42778807",
  "pmid": "42778807",
  "doi": "10.1007/s00415-026-14149-6",
  "title": "Frequency-Specific EEG burst dynamics in Parkinson's Disease and freezing of gait.",
  "verdict": "ok",
  "found_title": "Frequency-Specific EEG burst dynamics in Parkinson's Disease and freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42331397",
  "pmid": "42331397",
  "doi": "10.1111/ejn.70587",
  "title": "Deciphering Freezing of Gait: What Neuropathology Reveals About an Episodic Phenomenon.",
  "verdict": "ok",
  "found_title": "Deciphering Freezing of Gait: What Neuropathology Reveals About an Episodic Phenomenon.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:39355431",
  "pmid": "39355431",
  "doi": "10.1162/netn_a_00376",
  "title": "The effect of deep brain stimulation on cortico-subcortical networks in Parkinson's disease patients with freezing of gait: Exhaustive exploration of a basic model.",
  "verdict": "ok",
  "found_title": "The effect of deep brain stimulation on cortico-subcortical networks in Parkinson's disease patients with freezing of gait: Exhaustive exploration of a basic model.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38101024",
  "pmid": "38101024",
  "doi": "10.1016/j.parkreldis.2023.105952",
  "title": "Subthalamic functional connectivity associated with freezing of gait dopa-response.",
  "verdict": "ok",
  "found_title": "Subthalamic functional connectivity associated with freezing of gait dopa-response.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.1101/2023.02.27.529710",
  "pmid": "",
  "doi": "10.1101/2023.02.27.529710",
  "title": "The effect of deep brain stimulation on cortico-subcortical networks in Parkinson’s disease patients with freezing of gait: Exhaustive exploration of a basic model",
  "verdict": "ok",
  "found_title": "The effect of deep brain stimulation on cortico-subcortical networks in Parkinson’s disease patients with freezing of gait: Exhaustive exploration of a basic model",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.21203/rs.3.rs-4216535/v1",
  "pmid": "",
  "doi": "10.21203/rs.3.rs-4216535/v1",
  "title": "Subthalamic and Nigral Stimulation for Freezing of Gait in Parkinson disease: randomized pilot trial",
  "verdict": "ok",
  "found_title": "Subthalamic and Nigral Stimulation for Freezing of Gait in Parkinson disease: randomized pilot trial",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:38363617",
  "pmid": "38363617",
  "doi": "10.3233/jpd-230181",
  "title": "Kinematic Effects of Combined Subthalamic and Dorsolateral Nigral Deep Brain Stimulation in Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Kinematic Effects of Combined Subthalamic and Dorsolateral Nigral Deep Brain Stimulation in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:40760816",
  "pmid": "40760816",
  "doi": "10.1177/1877718x251359241",
  "title": "DBS-STN&amp;SNr combined stimulation versus DBS-STN monotarget stimulation for Parkinson's disease freezing: A comparative efficacy study.",
  "verdict": "ok",
  "found_title": "DBS-STN&amp;SNr combined stimulation versus DBS-STN monotarget stimulation for Parkinson's disease freezing: A comparative efficacy study.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:42909654",
  "pmid": "42909654",
  "doi": "10.1007/s10072-026-09479-2",
  "title": "STN-SNr co-stimulation in Parkinson's disease: a systematic review and meta-analysis of motor and freezing-of-gait outcomes.",
  "verdict": "ok",
  "found_title": "STN-SNr co-stimulation in Parkinson's disease: a systematic review and meta-analysis of motor and freezing-of-gait outcomes.",
  "title_sim": 1.0
 },
 {
  "ref": "DOI:10.64898/2026.02.02.702843",
  "pmid": "",
  "doi": "10.64898/2026.02.02.702843",
  "title": "Body-segment coordination as a new predictor of freezing of gait in people with Parkinson’s disease",
  "verdict": "ok",
  "found_title": "Body-segment coordination as a new predictor of freezing of gait in people with Parkinson’s disease",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:35786442",
  "pmid": "35786442",
  "doi": "10.7554/elife.75253",
  "title": "Therapeutic deep brain stimulation disrupts movement-related subthalamic nucleus activity in parkinsonian mice.",
  "verdict": "ok",
  "found_title": "Therapeutic deep brain stimulation disrupts movement-related subthalamic nucleus activity in parkinsonian mice.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:19811797",
  "pmid": "19811797",
  "doi": "10.1016/j.neurol.2009.07.017",
  "title": "[Pharmacological hypotheses and therapeutic strategies for gait disorders in Parkinson's disease].",
  "verdict": "ok",
  "found_title": "[Pharmacological hypotheses and therapeutic strategies for gait disorders in Parkinson's disease].",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:36110462",
  "pmid": "36110462",
  "doi": "10.7759/cureus.27887",
  "title": "Deep Brain Stimulation and Microelectrode Recording for the Treatment of Parkinson's Disease.",
  "verdict": "ok",
  "found_title": "Deep Brain Stimulation and Microelectrode Recording for the Treatment of Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "PMID:41386553",
  "pmid": "41386553",
  "doi": "10.1016/j.brs.2025.103002",
  "title": "Mechanisms mediating dynamic changes in neural responses during deep brain stimulation.",
  "verdict": "ok",
  "found_title": "Mechanisms mediating dynamic changes in neural responses during deep brain stimulation.",
  "title_sim": 1.0
 }
]

===== B0_gpt4 / open_g6.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "文献检索与证据纳入过程不可复现，所谓“广覆盖”缺乏可审计的操作性证据。报告虽然明确声明不是 PRISMA 系统综述，但仍将自身定位为基于原始文献核验的广覆盖研究综述，并据此提出跨研究综合结论。问题不在于没有使用 PRISMA，而在于没有提供足以证明覆盖范围、检索完整性和文献选择可靠性的检索记录。",
   "where": "第 1.3 节：“通过 PubMed/PMC、出版社原始页面、开放全文及 DOI 信息交叉核对候选文献。”“本文为广覆盖研究综述，不把搜索到的文献数等同于穷尽全部相关文献。”",
   "why": "没有数据库的完整检索式、实际检索日期、检索字段、语言限制、纳入与排除标准、去重方法、筛选数量、排除理由及各研究方向的覆盖情况。所谓“迭代检索”也没有留下可复现的迭代轨迹。读者无法判断研究遗漏是因为检索策略没有覆盖、筛选时被排除，还是作者没有识别到相关研究。尤其是报告同时涉及 STN 电生理、皮层网络、脑干、DBS 参数和临床表型，不同方向的文献检索难度与证据规模差异很大，不能仅凭最终列出 59 篇文献推断覆盖充分。更重要的是，后续的“研究冲突”“证据支持程度”和“最值得优先研究的方向”都依赖文献集合是否具有代表性。即使每篇已纳入论文都核验正确，系统性遗漏仍可能使综合结论发生偏差。",
   "severity": "major",
   "fix": "补充可复现的检索附录：逐数据库给出完整检索式、检索日期、检索字段和时间范围；明确原始研究、综述、会议摘要、预印本及临床试验的处理规则；提供去重和筛选流程及排除理由；对 STN-LFP、微电极、皮层-STN、DBS 干预、脑干网络和 FOG 表型分别建立检索覆盖表。再通过已纳入核心论文的参考文献追溯、被引文献追踪及相关试验注册记录进行补充检索。若无法完成这些工作，应将结论明确限定为非系统性叙述综述，不使用容易让读者误认为已充分覆盖的表述。"
  },
  {
   "rank": 2,
   "what": "证据确定性评价缺乏明确标准，研究质量与结论可信度没有真正建立对应关系。报告虽然建立了 finding、synthesis、mechanism 等层次，但没有建立可重复执行的研究质量评价体系。尤其是 supported、well-supported、contested 等状态，缺少明确的判定规则。",
   "where": "第 8.3 节：“status 代表本研究对证据确定性的定性评价，不是通过 GRADE 全套程序独立计算的正式评级。”附录 C7、C12、C13、C18 等仍使用 well-supported。",
   "why": "这导致一个关键问题：读者无法知道 well-supported 究竟意味着有多项独立研究、存在高质量随机干预、具有跨实验室重复性，还是仅仅有多篇论文报告了相似结果。不同研究的证据质量差别极大。例如，8 名患者的术中虚拟冻结实验、7 名患者的慢性 LFP 研究、静息态横断面研究以及随机对照干预，不能仅通过 supports 关系放在同一个证据权重层级。报告没有系统评价随机化、盲法、样本选择、缺失数据、信号质量、多重比较、预注册及选择性报告风险。对部分研究甚至没有确认患者人数，例如 E2、E25、E37、E38，却仍将其用于重要机制综合。也没有说明哪些数据来自摘要，哪些来自全文的图表或补充材料。这使证据层次看起来严密，实际上缺乏可复核的质量依据。",
   "severity": "major",
   "fix": "为原始研究建立独立的质量评价表，至少区分研究设计、患者级样本量、实际冻结事件数量、测量有效性、行为标签可靠性、混杂控制、统计方法和报告偏倚。为不同设计使用适合的风险偏倚工具。明确 supported、well-supported、contested 的判定条件。对直接观察真实 FOG 的证据、虚拟冻结、易感性指标和一般步态生理研究分别评级。每项关键数值增加原文页码、图表或补充材料定位，并标明全文核验状态。"
  },
  {
   "rank": 3,
   "what": "STN+SNr 两项 Meta 分析的冲突没有得到足够深入的统计学裁决，特别是对阳性 Meta 分析 R29 的多臂试验重复计权问题处理得不够明确。",
   "where": "第 4.4 节：“R28 对研究内相关性进行了显式处理，并将其 FOG 结论评为极低确定性。”“R29 采用了平行组近似并报告显著效应。”报告随后将两者作为方法不同的 Meta 分析并列比较。",
   "why": "核对 R29 原文后可以发现，问题不只是使用平行组近似。其森林图将 Artusi 2025 的两种 SNr 刺激条件分别与同一 STN 对照比较，又将 Weiss 2025 的三种 SNr 频率分别与同一 STN 对照比较。这些比较中的患者并不是独立样本。森林图最终汇总的两组比较人数均为 119，但该 Meta 分析报告的独立患者总数为 97。原文也承认多个研究提供了多组数据。与此同时，交叉试验缺少配对差值和患者内相关系数，作者使用平行组近似。两种处理问题叠加，使效应量、标准误和研究权重的可靠性需要重新审查。R29 中 Tan 2025 的效应量达到 SMD=-1.23，权重为 12.5%，而该原始研究本身还有值得核查的设计报告问题。相比之下，R28 明确处理配对数据和研究内依赖，并将 FOG 证据评为极低确定性。因此，两篇 Meta 分析并不是两个同等可信的相反结论。报告虽然识别了统计方法差异，却没有展示 R29 的重复计权对显著性和置信区间的实际影响。【turn960361view0】【turn372336view0】【turn594705view0】",
   "severity": "major",
   "fix": "对 R29 进行独立统计复核。多臂交叉试验应采用正确的多臂模型、配对效应量或适当的共享对照处理，不能将同一患者的不同刺激条件视为独立样本。对未知患者内相关系数进行不同取值的敏感性分析。特别进行排除 Tan 2025、排除多频率重复比较以及仅纳入低偏倚研究的分析。将 R28 与 R29 的纳入研究、患者队列、结局定义和效应量计算逐项对应。最终应给出可信度排序，而不只是保留两个相反的显著性结论。"
  },
  {
   "rank": 4,
   "what": "Tan 2025（R17）阳性联合刺激研究的原始报告存在需要认真核查的内部方法学矛盾，报告没有充分处理，却将其作为支持 STN+SNr 疗效的随机交叉研究。",
   "where": "第 4.3 节：“同年的 Tan 等 [R17] 报告联合刺激优于单纯 STN 刺激。”附录 E17：“24 人入组；20 人完成随访。”“报告联合刺激比单纯 STN 改善更多 FOG-Q 和生活质量评分。”",
   "why": "核对原文发现，研究方法部分将其描述为前瞻性随机交叉研究，但伦理声明部分却明确称其为回顾性研究。这种设计性质不一致需要澄清。研究主要使用 FOG-Q 和 PDQ-39 等量表，作者明确承认没有使用可穿戴设备或步态实验室进行客观步态测量。因此，其阳性结果主要反映患者报告的冻结严重程度和生活质量变化，并不等同于视频确认的实际冻结事件减少。报告只笼统写了“部分研究报告细节需要进一步质量复核”，没有说明这项研究究竟存在哪些问题。更值得注意的是，该研究在 R29 的森林图中贡献了较大的阳性效应量。若其研究设计、随机化和结局测量存在偏倚，可能影响联合刺激的整体证据判断。【turn121967view2】【turn121967view5】【turn372336view0】",
   "severity": "major",
   "fix": "单独核查 R17 的原始研究注册信息、研究方案、伦理审批性质、随机序列、交叉顺序、洗脱期、失访处理及盲法实施。要求解释前瞻性随机研究与回顾性研究表述之间的矛盾。在无法澄清前，应将其风险偏倚标记为不确定，不能直接视为低偏倚随机证据。Meta 分析应增加排除该研究的敏感性分析，并将其主观量表结局与客观冻结事件结局分开讨论。"
  },
  {
   "rank": 5,
   "what": "六个竞争性机制模型实际上不是同一逻辑层级上的竞争模型，彼此存在明显嵌套、交叉和共同成立的可能性，因而没有真正解决机制之间的竞争关系。",
   "where": "第六节：“下面的模型刻意采用较强的形式，确保可以通过实验区分。”第 6.6 节：“多个模型可能共同作用。”",
   "why": "H1 是局部频段活动机制，H2 是时间编码机制，H3 是认知到运动阻断的阶段性过程，H4 是跨区域网络机制，H5 是解剖通路机制，H6 是因果起始位置的替代解释。这些模型描述的是不同层级的问题，而不是六种互斥的病理机制。例如，长 beta burst 完全可能只在特定步态相位出现，因此 H1 和 H2 可以同时成立。皮层-STN 解耦可以是 H3 早期认知控制失败的表现，而 STN-SNr-MLR 输出异常又可以是 H1 或 H2 的下游结果。H6 则几乎可以容纳所有 STN 不是主要致病节点的情况。这样一来，即使实验同时发现多个预测，仍然无法判断哪个模型获得了独立支持。反过来，阴性结果也可能被解释为模型之间共同作用或患者亚型不同。报告虽然承认模型不完全互斥，却没有给出足以区分其主要因果位置的结构。",
   "severity": "major",
   "fix": "先建立明确的因果结构图，将模型拆分为上游触发因素、STN 局部状态、跨网络通信、下游运动输出和代偿性活动等层次。再定义真正相互竞争的因果解释，例如 STN 是必要的近端介质、STN 是上游网络失稳的下游响应，或不同患者存在不同主要起始节点。明确哪些变量可以共同出现，哪些因果主张互相排斥。为每个竞争模型规定至少一个其他模型不能同时满足的关键预测，并设计对应的干预对照。"
  },
  {
   "rank": 6,
   "what": "结构化知识附录存在证据与机制假说相互循环支持的问题，同时部分 supports 和 contradicts 关系在逻辑上使用不当。",
   "where": "附录 JSON：H4 的 claims 将 C21 标记为 supports，而 C21 本身的内容是“皮层-STN低频解耦可能参与FOG发生前的运动状态转换失败”，其 level 为 mechanism、status 为 speculative。H5 对 C22、H3 对 C20、H6 对 C23 也存在类似关系。H1 则将 C17 标记为 contradicts。",
   "why": "C21、C22、C23 等本身就是根据相关原始研究归纳出来的机制解释，不能再作为独立于其原始证据的证据支持对应假说。否则在知识图谱或未来自动综合时，可能把同一项原始研究先计为一个 finding，再计为一个 synthesis，最后又计为一个机制 claim，形成重复计权甚至循环论证。另一方面，C17 的实际内容是 beta burst 自适应 DBS 尚未证明优于对照，这不等于已经反驳 beta 的因果作用。C3 反驳的是 beta 增强对所有 FOG 的普遍必要性，但 H1 已经限定为特定亚型，也不能直接把它视为对 H1 整体的反证。STN+SNr 总体治疗效果不显著同样不能直接反驳某条通路在特定亚型中参与 FOG 的机制。这里混淆了未证明、受到限制、反对普遍性主张和真正的实验反证。",
   "severity": "major",
   "fix": "将原始实验结果、跨研究综合和机制假说设置为有方向的依赖关系，而不是让机制 claim 再反过来充当自身假说的独立证据。假说应直接关联原始 EID，或者明确记录其引用的综合结论及其全部上游证据。严格定义 supports、contradicts、qualifies、not-tested 的语义。只有在相同患者亚型、实验条件、神经来源、时间窗和结局下出现真正不相容的结果，才能标记为 contradicts。未达到统计学显著性或没有证明因果中介，应标记为未确认，而不是直接反证。"
  },
  {
   "rank": 7,
   "what": "第七节提出的判别性研究无法完整检验第六节的全部机制模型，尤其无法真正检验 H5 的 STN-SNr-MLR 输出门控机制。",
   "where": "第 7.1 节第一阶段：“双侧 STN LFP”“适合的皮层 EEG/ECoG”“下肢拮抗肌 EMG”“IMU、足底压力和同步视频。”第二阶段刺激条件：“Beta burst 触发刺激”“步态相位触发刺激”“网络异常触发刺激”“连续 DBS”“与各闭环模式刺激负荷相匹配的随机时序刺激”。",
   "why": "H5 的核心预测涉及 STN、SNr、PPN/CuN 或 MLR 相关通路之间的时间顺序和输出门控，但研究设计没有安排 SNr 或脑干神经活动记录，也没有 SNr 或相关脑干通路的随机刺激条件。仅凭 STN、皮层和肌肉记录，无法确认 STN 异常是否通过 SNr-MLR 通路产生下游效应。H6 同样涉及脑干、感觉整合和其他非 STN 网络，而拟议记录没有覆盖关键脑干节点。H4 预测恢复特定皮层-STN 耦合可以改善冻结，但网络异常触发 STN 刺激不等于真正恢复了目标耦合。因此，这个试验能够较好地比较 H1、H2 和部分 H3，却不足以区分 H4、H5、H6 的关键因果预测。",
   "severity": "major",
   "fix": "将研究设计与假说范围严格对应。可以缩小首轮研究的机制目标，只检验 STN beta、步态相位和皮层-STN 耦合；也可以在具有临床植入条件的患者中增加 SNr、PPN/CuN 相关记录，并设计目标通路募集的随机对照刺激条件。对于无法安全直接记录的脑干结构，应明确哪些模型只能间接检验，不能将间接相关性描述为已经完成通路因果验证。"
  },
  {
   "rank": 8,
   "what": "虽然引用了 2026 年国际 FOG 联盟更新定义，但没有把新定义真正落实到研究证据的逐项编码和事件时间分析中。",
   "where": "第 1.1 节：“进一步规范了临床诊断和视频标注，并强调区分 akinetic freezing、kinetic trembling 及其他运动不成功的冻结表现。”第 7.1 节：“按照新 FOG 定义进行双盲视频标注。”",
   "why": "2026 年 International Consortium for Freezing of Gait 的共识不仅更新了临床定义，还提出了技术性事件起止规则，要求确认实际迈步尝试，明确 FOG episode 的结束条件，并区分 akinetic、kinetic-trembling 和 kinetic-no-trembling 三种表现。报告没有完整呈现 kinetic-no-trembling 这一类别，也没有讨论 FOG core、两次有效步伐结束事件等具体规则。更重要的是，附录没有逐项记录各原始研究使用的 FOG 起止标准、事件分类、人工标注者一致性及自动检测验证情况。不同研究如果采用不同的冻结起点，冻结前 1 秒、2 秒或整个冻结期的神经活动就不是完全相同的分析窗口。对于本报告这种高度依赖时间对齐的机制研究，这会直接影响 beta burst、theta 变化和跨网络解耦的比较，而不仅仅是临床术语不统一。【turn259508search1】",
   "severity": "major",
   "fix": "增加 FOG 定义和标注质量专表，逐研究记录临床定义、视频技术定义、起止规则、冻结表现类型、是否确认迈步尝试、标注者数量及一致性。明确哪些研究能够按照新定义重新解释，哪些只能保留为历史性冻结候选证据。对事件起点和终点进行敏感性分析，避免将不同定义下的神经时间窗直接合并。"
  },
  {
   "rank": 9,
   "what": "队列重叠和患者级证据独立性仍然没有得到完整解决，现有的重复队列警示不足以支撑严格的跨研究证据计权。",
   "where": "第 1.3 节：“对于无法确认独立性的研究，保留潜在队列重叠警示。”第 8.1 节：“已明确 [R47]/[R48] 不是独立队列。”",
   "why": "报告已经发现 R1/R34、R3/R30、R47/R48 等潜在或确定的队列关系，这是重要改进，但还没有形成完整的研究队列对应表。尤其是同一研究团队在同一中心、相近时期、使用相似植入设备开展的多项研究，可能使用同一患者的不同分析结果。R6、R22、R59 等来自相关研究团队和临床平台，也需要进一步核查患者来源。对 263 次冻结事件、115 次非冻结试次或多个电极触点的统计，不能增加独立患者数量。虽然正文明确提醒这一点，但附录没有提供跨论文患者队列依赖关系，未来基于 EID 数量进行证据汇总仍可能高估独立重复性。",
   "severity": "moderate",
   "fix": "建立 cohort_id 层，记录中心、招募时期、临床试验编号、植入设备、患者特征和队列来源。对每篇论文标注独立队列、部分重叠、完全重叠或未知。将患者数、事件数、试次数和电极数分开统计。跨研究综合时以独立患者队列作为重要证据单位，对同一队列的重复分析不重复提高证据确定性。"
  },
  {
   "rank": 10,
   "what": "多巴胺相关 FOG 亚型虽然被列为重要解释变量，却没有真正进入跨研究证据矩阵，导致报告没有完成自己提出的关键分层分析。",
   "where": "第 1.2 节：“本文将 FOG 至少划分为四种。”第 3.1 节将药物状态列为研究冲突的可能来源。第 2.1 节各研究的 condition 字段主要记录 ON/OFF 状态，但没有系统记录患者的 OFF-FOG、ONOFF-FOG、ON-FOG 或双相 FOG 分类。",
   "why": "必须区分患者的临床 FOG 表型与某一次实验的药物状态。例如，在 OFF 药物条件下记录，不代表患者属于 OFF-FOG；一个 ONOFF-FOG 患者在 OFF 状态下也可能发生冻结。R17 的评估处于 medication-off 状态，而 R18 的主要评估处于 medication-on、STN stimulation-on 状态，两者不是完全相同的临床情境。若只记录 ON/OFF，而不记录患者是否经过充分药物挑战、冻结是否在充分 ON 状态下持续存在，就无法判断不同电生理结果是否来自不同 FOG 亚型。报告在理论部分承认药物亚型重要，但没有将其用于核心研究的逐项比较。需要注意，2026 年 ICFOG 共识本身也指出，药物反应亚型尚缺乏统一分类标准，仍需要标准化药物挑战研究。【turn121967view2】【turn783030view1】【turn259508search1】",
   "severity": "moderate",
   "fix": "将患者临床 FOG 亚型和实验记录状态分成两个独立字段。记录标准化左旋多巴挑战结果、药物剂量与时间、DBS 状态、测试时实际冻结情况及其持续性。不能仅凭实验是在 ON 或 OFF 状态进行就推断临床亚型。对缺乏可靠亚型信息的旧研究明确标注 unknown，并在综合结论中限制其解释范围。"
  },
  {
   "rank": 11,
   "what": "R18 这项被称为最新关键随机证据的研究，其非确证性统计设计和样本选择限制没有得到充分呈现。",
   "where": "第 4.3 节：“2026 年 10 月发表的探索性多中心随机双盲研究纳入 45 名进入改良意向治疗分析的患者。”“两组主要终点差异不显著，P=0.692。”",
   "why": "原始论文明确说明，主要终点采用 P<0.2 的探索性判定阈值，样本量按照单侧 alpha=0.2 进行设计，研究属于 non-confirmatory exploratory study，统计结果主要用于描述和生成假说。研究也不是前瞻性地为患者植入独立 SNr 电极，而是从既有 DBS 队列中选择电极位置满足 STN-SNr 边界条件的患者，且未达到原计划的 54 人样本量。报告虽然称其为探索性研究，却没有明确呈现这些限制，也没有报告主要终点的效应量和置信区间。P=0.692 不能证明两种治疗等效，也不能排除具有临床意义的亚组效应。另一方面，较短病程应答者的发现仍然属于探索性亚组结果，不能直接转化为患者选择规则。【turn783030view0】【turn783030view2】【turn783030view3】",
   "severity": "moderate",
   "fix": "在证据矩阵中补充研究的统计设计性质、预设 alpha、样本量目标、实际完成样本量、主要效应量及 95% 置信区间。明确说明其主要结论是没有观察到总体显著优势，而不是证明无效或等效。将病程相关应答结果标为探索性假说，等待独立的预设分层研究验证。"
  },
  {
   "rank": 12,
   "what": "因果机制检验部分仍然过度依赖生物标志物的时间先后和统计中介分析，没有充分解决 DBS 多通路作用造成的中介识别问题。",
   "where": "第 7.4 节：“标志物变化发生在运动行为改善之前。”“临床改善程度应与病理 beta 活动的变化相对应。”“预设中介分析在合理的未测量混杂假设下支持机制路径。”",
   "why": "神经标志物先变化、冻结随后改善，并不自动证明标志物是治疗效应的中介。DBS 同时影响 STN 局部神经元、传入和传出轴突、皮层网络及下游脑干结构。某个 beta 指标可能只是这些变化的伴随读出。即使刺激是随机分配的，刺激后的生物标志物并没有被随机化，标志物与冻结之间仍可能存在未测量混杂，甚至可能存在由治疗本身引起的中介—结局混杂。报告已经承认 DBS 有多重网络作用，却没有明确给出如何识别单一神经中介的统计因果结构。",
   "severity": "moderate",
   "fix": "将目标标志物的选择性调节与一般 DBS 疗效分开检验。设计具有相同刺激总量和不同神经时序的随机对照条件，预先定义 target engagement，并测量其他可能同时改变的神经指标。对中介分析明确列出因果图、识别假设、治疗诱导混杂及敏感性分析。若不能实现足够的选择性干预，应将结论限定为机制一致性证据，而不是已证明的因果中介。"
  },
  {
   "rank": 13,
   "what": "长期证据积累和自主改进目前主要停留在数据结构与维护规则的设计层面，没有证明已经形成能够持续检索、更新和验证的证据系统。",
   "where": "第 8.1 节：“本次完成的是证据结构和推断逻辑的改进与交叉核验。”第 8.2 节：“应建立的长期证据维护规则。”附录使用 eid、ref、cid、hid 作为结构化标识。",
   "why": "静态 JSON 可以保存知识，但不等于具有长期记忆、版本管理、自动检索和证据更新能力。报告没有展示文献版本历史、每条 claim 的修改记录、旧结论被新证据触发重新评价的实际案例，也没有展示检索测试或更新测试。8.1 节的自我审计表将若干改进列为已实施，但没有提供审计前后的版本、可复核的修改差异或独立验证结果。它证明了作者提出了较好的证据维护理念，却没有证明持续自主改进已经真正发生。尤其是原始证据定位、队列重叠信息、证据状态变更历史和数据提取来源尚未完整纳入结构化附录。",
   "severity": "moderate",
   "fix": "建立有版本号的长期证据库，保存原始文献元数据、全文定位、数据提取记录、患者队列 ID、证据依赖关系和每次 claim 修改的历史。设置新文献触发旧结论复核的明确规则。为更新流程建立测试案例，例如加入一项反证研究后，检查相关 claim 是否正确降级、关联假说是否重新评价，以及不相关结论是否保持不变。将已经实际运行并验证的功能与未来计划严格区分。"
  }
 ],
 "overall": "这份报告有较好的问题意识，尤其是没有把 STN beta 增强直接等同于 FOG 的原因，也主动区分了实际冻结、冻结易感性、步态生理编码和 DBS 疗效，并尝试建立竞争性机制模型。但最重要的缺陷在于：证据检索不可复现，研究质量评价缺乏统一标准，部分关键临床证据尤其是 STN+SNr 阳性研究没有得到足够严格的原始方法学审查，Meta 分析的统计依赖问题也没有被充分裁决。更深层的问题是，机制模型仍然是不同解释层级的集合，结构化附录存在循环支持和证据重复计权风险，而拟议研究设计又不能检验全部核心模型。因此，目前最可靠的部分是对现有结果异质性和因果不确定性的描述；最不可靠的部分是对证据强度的等级判断、STN+SNr 干预证据的整体权重，以及六种机制模型之间的区分程度。它可以作为一份有价值的机制综述框架，但距离可复现、可审计、可持续更新且真正能够指导机制判别实验的成熟证据综合报告，还有几项结构性问题需要解决。"
}

===== B0_gpt4 / open_g56.json =====
{
 "problems": [
  {
   "rank": 1,
   "what": "FOG证据的分类体系没有真正贯彻到证据综合中，实际冻结、虚拟冻结、模拟冻结、冻结易感性和一般步态异常仍然存在混用。这是影响核心科学结论的结构性问题。",
   "where": "第1.1节将实际FOG、原地踏步冻结、虚拟冻结、iFOG和FOG问卷明确区分，但第2.1节又将这些不同类型的研究统一放入“STN神经活动与FOG的核心直接证据”矩阵。例如[R4]被描述为“踏步时 beta 下降，冻结时增加”；[R3]使用虚拟步态任务；[R2]研究冻结易感性；[R7]研究静息态表型。",
   "why": "这些研究回答的不是同一个问题。尤其[R4]（Gulberti 2023，PMID 36730026，DOI 10.1093/brain/awad006）虽然报告了冻结相关活动，但其实际实验是在手术中的仰卧踏步任务，所谓冻结是FoG-like stepping irregularities：踏步幅度较前三步下降至少50%，持续超过3秒。作者还专门通过术前FOG评分验证这种替代指标。它不是自然直立行走中的视频确认冻结。类似地，[R3]和[R30]使用仰卧虚拟现实踏步任务，其中还涉及显著运动减慢。将这些结果与[R5]、[R8]等自然行走中的实际冻结并列，容易人为增加STN活动与真实FOG之间的直接证据数量。更严重的是，不同终点可能产生不同方向的神经活动变化，因而会影响对beta和theta冲突的解释。",
   "severity": "major",
   "fix": "建立严格的证据终点分级：A类为真实直立行走中视频确认的FOG；B类为具有运动学或肌电验证的冻结样事件；C类为虚拟冻结或替代任务；D类为FOG易感性；E类为静息表型。每条研究证据必须标记所属类别。核心机制结论首先使用A类证据建立，再使用其他类别解释和补充。必须进行排除C、D、E类研究后的敏感性综合，确认核心结论是否仍然成立。"
  },
  {
   "rank": 2,
   "what": "检索过程不可复现，无法判断研究覆盖是否充分，也无法判断报告中的文献集合是否存在系统性遗漏。",
   "where": "第1.3节：“围绕STN-LFP、微电极单/多单位记录、皮层—STN耦合、FOG事件、步态周期、STN-DBS……”；“通过PubMed/PMC、出版社原始页面、开放全文及DOI信息交叉核对候选文献。”以及“本文为广覆盖研究综述，不把搜索到的文献数等同于穷尽全部文献。”",
   "why": "这些是检索主题和平台的描述，不是可复现的检索方法。报告没有提供具体检索日期、各数据库完整检索式、布尔逻辑、时间范围、语言限制、文献筛选标准、排除原因、重复记录数量及最终筛选流程。也没有说明是否系统检索Embase、Web of Science、Scopus、Cochrane、临床试验注册平台和相关参考文献。承认不是PRISMA系统综述是合理的，但不能因此免除广覆盖叙述综述的检索透明度要求。",
   "severity": "major",
   "fix": "补充完整检索附录，至少提供每个数据库的实际检索式、检索日期、时间范围、筛选标准、筛选记录数量和排除原因。采用数据库检索、前向及后向引文追踪、相关综述参考文献追踪相结合的方法。另建立检索覆盖矩阵，说明哪些研究方向已覆盖、哪些仅进行了有限检索、哪些尚未检索。"
  },
  {
   "rank": 3,
   "what": "没有对原始研究进行统一、正式的偏倚风险和证据确定性评价，导致supported、well-supported等结论标签缺乏可验证的判定标准。",
   "where": "第1.4节的证据分层和第8.3节：“status代表本研究对证据确定性的定性评价，不是通过GRADE全套程序独立计算的正式评级。”结构化附录中大量使用supported、well-supported、contested和speculative。",
   "why": "报告虽然承认没有正式使用GRADE，但实际上仍然对证据强度进行了分类，却没有定义各个标签的具体判定条件。没有对随机交叉试验统一使用RoB 2，没有对观察性研究使用适当的偏倚评价工具，也没有系统评估选择偏倚、测量偏倚、失访、选择性报告和混杂。小样本研究、术中微电极研究、虚拟步态研究与真实行走研究的证据质量差异很大，不能只根据研究结果是否一致来判定证据强度。例如C7将STN及相关网络的步态阶段特异活动组织标记为well-supported，但其中部分研究主要证明一般步态编码，并没有直接证明FOG特异性机制。报告没有充分区分证据的一致性、质量、直接性和确定性。",
   "severity": "major",
   "fix": "建立统一的原始研究质量评价体系。临床随机研究采用RoB 2，观察性研究采用适当的ROBINS-I或同等工具，并针对不同证据类型评估直接性、精确性、一致性及发表偏倚。对跨研究结论采用明确的确定性分级规则。将研究结果方向与证据确定性分别存储，避免把多项低质量研究的一致结果直接升级为well-supported。"
  },
  {
   "rank": 4,
   "what": "关键原始研究的数据提取不够完整，部分核心证据连真正发生冻结的患者数量都没有明确提取，无法支持严格的患者级证据评价。",
   "where": "结构化附录E37：“本次核验未确认可独立复核的完整人数。”E2、E25也存在类似的样本量未确认情况。第2.1节将[R37]列为实际行走冻结的关键证据。",
   "why": "这是可以通过原始文献核查发现的具体遗漏。[R37] Klocke等2024年Brain研究（PMID 39470410，DOI 10.1093/brain/awae223）明确报告：最终分析队列为12人，但实验中实际出现FOG的只有5人，共42次冻结事件；其中39次为trembling-in-place型，只有3次为akinetic型。报告不仅没有提取这些重要信息，还将完整患者数标记为未确认。这里的12名受试者、5名实际冻结患者和42次冻结事件具有完全不同的证据含义。此外，该研究的冻结亚型高度集中于trembling-in-place，不能不加限定地推广至所有FOG类型。其他核心研究也存在没有报告具体效应量、置信区间、统计检验结果和事件级分析窗口的问题。",
   "severity": "major",
   "fix": "对所有核心原始研究重新核查全文和补充材料。每项研究至少提取总入组人数、最终分析人数、实际发生FOG的人数、FOG事件数量、冻结亚型、患者级效应、事件级效应、药物状态、DBS状态、实验任务、记录位置、统计方法和主要效应量。每项数据同时记录原始文献的表格、图号或具体段落位置。无法确认的信息应标记为未核实，而不是让它进入已经完成核验的证据集合。"
  },
  {
   "rank": 5,
   "what": "虽然报告意识到了患者、试次和冻结事件之间的统计依赖，但没有展示已经完成的患者级去重和独立证据计算，仍存在重复证据和伪重复风险。",
   "where": "第1.3节：“同一队列的不同论文可以作为不同分析证据，但不能重复累计独立患者。”第2.1节：“不能因为一个患者发生大量冻结就认为具有相同数量的独立证据。”第8.1节仅明确列举了[R47]/[R48]等部分队列关系。",
   "why": "这些原则是正确的，但报告没有给出完整的队列关系图或患者级研究重叠矩阵。例如[R59]只有4名患者，却包含38次冻结试次和115次非冻结试次；[R6]的冻结事件集中于12名患者；[R37]的42次冻结仅来自5名实际发生冻结的患者。不能将这些事件数量与其他研究的患者数量直接比较。不同论文可能来自同一研究中心、相同研究团队、相同植入平台或连续招募的患者群体。报告已经注意到[R1]/[R34]、[R47]/[R48]及[R3]/[R30]等潜在关联，但没有系统解决所有可能的重叠问题。结果是读者仍然无法判断究竟有多少独立患者真正支持某个机制。",
   "severity": "major",
   "fix": "建立研究队列去重表，记录研究中心、招募时间、研究团队、植入设备、患者特征、队列来源和可能的重叠关系。将独立患者数与重复分析次数分开统计。对于不能确认独立性的研究明确标记潜在重叠，并在证据汇总中进行最保守的独立样本估计。跨研究综合应以患者为主要独立单位，而不是冻结事件或试次数。"
  },
  {
   "rank": 6,
   "what": "六个机制模型虽然提出了不同预测，但尚未真正形成严谨的竞争性假说体系；附录中的支持、反驳关系还存在明确的逻辑错误。",
   "where": "第六节：“下面的模型刻意采用较强的形式，确保可以通过实验区分。”以及“多个模型可能共同作用。”结构化附录中H1将C3和C17标记为contradicts，H5将C10标记为contradicts。",
   "why": "首先，H1至H6并非真正相互排斥的机制模型。H1 beta同步、H2相位编码、H3认知控制双阶段和H4皮层-STN解耦可以同时发生。报告虽然承认这一点，却没有进一步明确哪些是不同层级的机制、哪些是同一机制的不同阶段、哪些是真正竞争的因果解释。其次，部分证据关系标记不符合逻辑。H1明确限定为特定FOG亚型，但C3仅说明beta增强不是所有FOG的必要条件，这并不反驳特定亚型中的beta因果模型。C17说明beta burst闭环刺激尚未证明特异性因果机制，也不构成对H1的直接反驳。H5中C10说明STN+SNr联合刺激尚无稳定的总体临床优势，这不能反驳STN-SNr-MLR通路参与部分FOG的机制。治疗总体效果阴性，不等于相关神经通路没有参与疾病机制。把缺乏验证、不能推广和真正反证都标记为contradicts，会污染知识图谱。",
   "severity": "major",
   "fix": "重新定义假说之间的关系类型，至少区分直接支持、间接支持、限制适用范围、削弱、真正反驳、尚未检验和证据不足。将模型拆分为病因节点、网络状态、神经编码、运动执行和临床表现等层级。对每个模型规定具体患者亚型、记录区域、频段边界、时间窗口、效应方向、预测阈值和独立证伪条件。设计能够同时比较多个模型的同一患者内实验，而不是仅列出各模型都能解释的现象。"
  },
  {
   "rank": 7,
   "what": "第八节的自我审计没有形成真正的验证闭环，报告把自己宣称的改进当成了改进有效的证据。",
   "where": "第8.1节标题为“本次研究发现并纠正的问题”，表格列出“已实施的改进”和“复核结果”；第8.1节最后又说明：“本次完成的是证据结构和推断逻辑的改进与交叉核验。”",
   "why": "发现问题、实施修改和证明修改有效是三个不同步骤。当前表格只是作者对自身工作过程的描述，没有提供审计前后的文献遗漏率、错误引用率、患者重复计算率、证据分类一致性、独立审查结果或其他可量化指标。例如，“纳入反方向研究后，强beta模型降级为contested”说明结论发生了变化，但没有证明检索遗漏已经减少，也没有证明分类错误已经得到系统解决。报告也没有说明是否由第二名研究者独立核验。这样的自我审计无法证明系统真正改善。",
   "severity": "major",
   "fix": "建立独立的审计验证机制。保留每次修改前后的证据版本，记录问题发现来源、修改操作、受影响的研究和结论。由独立审查者重新执行文献检索、证据分类和引用核验。建立可量化指标，例如核心文献召回率、错误证据归类率、患者重复计算率、引用准确率和研究者间一致性。只有通过独立复核的改进才能标记为已验证。"
  },
  {
   "rank": 8,
   "what": "STN+SNr两项Meta分析的冲突分析仍然不够深入，没有充分评价阳性Meta分析本身的统计学和偏倚风险。",
   "where": "第4.4节：“[R28]对研究内相关性进行了显式处理……[R29]采用了平行组近似并报告显著效应。”",
   "why": "报告已经发现了一个重要问题，但停留在方法差异的描述层面。Haq等[R29]的全文明确说明，纳入的全部研究均为交叉试验，但由于原始研究缺少配对差值和患者内相关系数，Meta分析采用平行组近似。该分析还报告了8项试验中1项低偏倚风险、5项中等风险、2项高风险，并且部分研究贡献了多个数据集。这样的分析存在患者内相关性处理和重复数据集权重问题。Kong等[R28]则明确考虑了配对数据及研究内依赖，并将FOG证据确定性评为极低。两项分析虽然报告的效应量不同，但不能简单视为两套同等可靠的独立证据。报告没有进一步检查哪些原始研究和终点造成了结果变化，也没有比较不同配对相关性假设下结论是否稳定。",
   "severity": "moderate",
   "fix": "增加逐项原始试验对照表，列出两项Meta分析分别纳入的研究、患者数、结局量表、比较条件、随访时间和数据处理方式。重点进行配对相关系数的不同假设下的敏感性分析、共享对照处理分析、重复数据集剔除分析和高偏倚风险研究剔除分析。明确说明哪项分析在统计结构上更可信，以及现有数据能否支持联合刺激的临床重要优势。"
  },
  {
   "rank": 9,
   "what": "长期知识积累系统目前只是一个结构化数据格式和更新原则的设想，还不能称为已经建立的可持续证据系统。",
   "where": "第8.2节：“每条证据以eid作为可追溯最小单位，文献以ref去重，跨研究结论以cid保存，竞争性假说以hid保存。”第8.3节说明附录JSON的使用边界。",
   "why": "EID、CID和HID是有价值的标识设计，但目前没有提供完整的数据模式、字段约束、版本管理、文献原始来源、数据提取记录、证据状态变化历史和查询接口。更重要的是，没有展示新文献进入后如何自动或半自动识别受影响的旧结论。例如新增一项直接反驳H1的研究，系统如何识别相关EID、CID和HID？哪些旧结论需要重新评估？如何保存旧版本及修改理由？当前附录只能证明报告采用了结构化表示，不能证明已经具备长期检索和证据更新能力。",
   "severity": "moderate",
   "fix": "将结构化附录升级为具有明确版本的证据数据库。每条证据应包含原始文献标识、来源定位、提取者、核验者、最后核验日期、研究队列、终点类型、统计数据和质量评价。每条结论保存历史版本、适用范围、支持及反驳证据、修改原因。建立文献更新后自动生成受影响结论清单的机制，并用实际新增文献测试检索、关联和重新评价是否有效。"
  },
  {
   "rank": 10,
   "what": "研究覆盖仍有具体遗漏，尤其缺少对FOG诱发任务及客观临床终点验证研究的充分整合。",
   "where": "第1.3节列出的检索方向、第5.1节至第5.3节，以及结构化附录R1-R59的references列表。",
   "why": "一个具体例子是O'Day等2020年的研究“The turning and barrier course reveals gait parameters for detecting freezing of gait and measuring the efficacy of deep brain stimulation”（PMID 32348346，DOI 10.1371/journal.pone.0231984）。该研究验证了转弯和障碍物步态任务对FOG的诱发和测量能力，并报告了60 Hz及140 Hz STN-DBS条件下的实际冻结和相关步态指标变化。它与本报告讨论的FOG诱发任务、冻结测量可靠性、DBS频率效应和闭环控制指标直接相关，却没有进入参考文献列表。这个遗漏说明，现有59篇文献并不能仅凭数量证明研究方向已经充分覆盖。",
   "severity": "moderate",
   "fix": "对FOG诱发任务、行为终点验证、运动学与肌电测量、DBS参数优化、闭环算法、临床试验和相关数据集进行专项补充检索。建立研究方向覆盖清单，逐项记录代表性研究、证据空白和尚未纳入的候选文献。对遗漏研究说明是否与核心问题相关，以及不纳入的理由。"
  },
  {
   "rank": 11,
   "what": "提出的判别性研究虽然方向合理，但从机制发现到因果验证的实验设计仍缺少关键的实施和验证细节。",
   "where": "第7.1节：“建议采用两阶段、多中心、患者内重复随机的机制试验。”第7.1节至7.4节提出beta burst、步态相位、网络异常、连续DBS和随机刺激等比较。",
   "why": "目前的设计同时包含多种神经信号、多种步态任务、多个刺激条件和多个FOG终点，实验复杂度很高。报告没有明确说明不同闭环模式是否能在现有植入式设备上同时实现，如何处理刺激伪迹和实时信号质量，如何确定刺激触发阈值，如何进行条件间洗脱和随机化，以及如何保证患者和评估者盲法。第一阶段发现的个体化标志物如何进入第二阶段、是否需要独立患者队列进行外部验证，也没有明确规定。尤其是网络异常触发刺激，如果无法在临床设备上实时稳定测量，就不能直接与其他刺激条件进行公平比较。多种任务和标志物还会产生严重的多重比较及选择性报告风险。",
   "severity": "moderate",
   "fix": "先将研究拆分为独立的机制发现、独立验证和随机因果干预三个阶段。优先选择能够由现有设备可靠测量的标志物，分别进行实时可行性验证。预先规定刺激算法、触发阈值、随机化、洗脱、盲法、主要终点和统计分析计划。采用独立患者队列验证预测性能，并在正式试验前完成设备兼容性、伪迹控制、安全性及患者内统计功效评估。"
  },
  {
   "rank": 12,
   "what": "研究对STN证据的外部适用范围仍然不够明确，尤其是不同多巴胺反应性FOG亚型之间缺少直接的电生理比较。",
   "where": "第1.2节将FOG划分为OFF-FOG、ONOFF-FOG、ON-FOG和Biphasic FOG；第2.1节及附录E1-E59列出不同药物和刺激状态的研究。",
   "why": "报告正确指出FOG具有不同药物反应亚型，但这些亚型主要作为临床背景变量出现，没有真正形成STN电生理证据的分层体系。很多核心研究是在OFF药物、OFF DBS或特定手术条件下进行的，部分研究使用术中仰卧任务或严重PD患者的植入式记录。现有证据不足以说明同一个beta、theta或耦合指标在OFF-FOG、ONOFF-FOG和ON-FOG中具有相同的方向和机制。尤其不能因为某项研究在OFF药物条件下观察到异常活动，就将其推广到左旋多巴诱发的ON-FOG。",
   "severity": "moderate",
   "fix": "建立患者级药物反应分层证据表。对每项电生理研究明确标记药物反应亚型、药物剂量和记录时点，并区分药物ON/OFF与FOG实际发生状态。未来研究应在同一患者内进行严格的药物挑战和步态记录，直接比较不同FOG亚型的STN频谱、burst、相位编码和皮层-STN耦合特征。"
  }
 ],
 "overall": "这份报告已经形成了比较完整的研究框架，尤其是没有简单地把STN beta增强等同于FOG病因，也认识到了预测标志物、治疗效应和因果机制之间的区别。但最重要的问题是：报告的证据管理和科学推断体系尚未达到其自身设定的严谨程度。FOG终点分类没有贯彻到底，检索不可复现，原始研究的数据提取和质量评价不充分，患者与事件的独立性没有得到完整核验，竞争性机制模型及其证据关系存在逻辑问题，自我审计也没有独立验证。由此产生的核心风险是：报告提出的网络失稳综合解释可能具有合理性，但目前无法充分判断它究竟是被多项相互独立的直接证据支持，还是部分由不同任务、不同终点、不同患者群体和不同证据层级的结果拼接而成。最需要优先解决的不是继续增加机制模型或文献数量，而是重新核实核心原始研究、严格分离FOG终点、完成患者级证据去重和质量评价，并使每一项跨研究结论都能被独立复核和反驳。"
}

===== B0_gpt4 / abs_g6.json =====
{
 "standards": [
  {
   "n": 1,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "研究覆盖面较广，包含STN-LFP、微电极记录、beta/theta/alpha、burst、皮层-STN耦合、步态周期、DBS频率与空间定位、SNr、PPN/CuN、药物亚型及自动检测等交叉方向。但检索过程不可复现：没有完整数据库检索式、各数据库检索日期、纳入排除标准、筛选数量、排除文献清单及引文追溯记录。因此，59篇文献不能证明重要研究已被充分覆盖，也无法独立评估遗漏风险。",
     "where": "第1.3节：“通过 PubMed/PMC、出版社原始页面、开放全文及 DOI 信息交叉核对候选文献”；“本文为广覆盖研究综述，不把搜索到的文献数等同于穷尽全部相关文献。”（L75-L86）"
    },
    {
     "severity": "minor",
     "what": "虽然列出了大量交叉方向，但部分研究方向尚未形成完整的证据链。例如，不同FOG运动表现亚型、不同DBS靶点之间的比较，以及不同感觉运动通路的独立作用，没有全部进入统一的研究覆盖矩阵。",
     "where": "第1.3节研究方向表（L63-L86）；第2.1节证据矩阵（L107-L124）。"
    }
   ]
  },
  {
   "n": 2,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "部分原始研究的有效分析样本量没有与招募人数区分。R1虽然招募14名患者，其中8名Freezer，但原文明确有5名患者被排除在神经信号分析之外。报告只给出14人和8名Freezer，没有明确列出神经分析的实际样本量，容易高估直接电生理证据的有效样本规模。",
     "where": "第2.1节R1：“14 名 PD，8 Freezer”；结构化附录E1：“n: 14人；Freezer 8人”。原文明确说明5/14患者被排除于神经分析。【turn243818view0】"
    },
    {
     "severity": "minor",
     "what": "R2的样本量在附录中标记为未确认，但原始全文明确报告15名患者，其中只有3名在实验期间实际出现FOG。该研究的主要分析指标是基于躯干加速度计算的iFOG，而不是全部患者的视频确认冻结事件。报告正确区分了易感性与实际冻结，但未完整提取样本信息。",
     "where": "结构化附录E2：“n: 未在本次核验中确认可独立复核的完整人数”；第2.1节R2：“低beta 15–21 Hz 与 theta 5–8 Hz 和 FOG 易感指标相关”。原文方法和结果见PMID 31494286。【turn767053view0】"
    },
    {
     "severity": "minor",
     "what": "R4的仰卧踏步任务与自然负重行走存在明显差异。原始研究记录的是仰卧模拟步态中的冻结相关活动，不能与真实自由行走中的视频确认FOG完全等同。报告虽然列出了仰卧踏步条件和相应限制，但在综合证据时仍应明确标记为模拟冻结或冻结样运动异常。",
     "where": "第2.1节R4：“踏步时 beta 下降，冻结时增加”；结构化附录E4：“仰卧踏步、注意性提示和冻结相关运动异常”。PMID 36730026。【turn888907view0】"
    },
    {
     "severity": "moderate",
     "what": "R37的直接神经肌肉证据缺少重要的患者级分母和冻结表现分型。原始研究分析了12名患者，其中5名出现FOG，共记录42次冻结相关事件；其中绝大多数表现为原地震颤样冻结，而非典型完全运动不能。报告没有提取这些信息，可能使STN-肌肉耦合结果被过度推广到所有FOG亚型。",
     "where": "第2.1节R37：“实际行走冻结；STN LFP、EMG、运动学”；结构化附录E37：“n: 本次核验未确认可独立复核的完整人数”。原始研究PMID 39470410。【turn535686view0】"
    },
    {
     "severity": "minor",
     "what": "R24的总样本量为7人，但自由行走分析仅涉及5人，实际自由行走冻结事件的患者数量更少。报告提到小样本和统计效能不足，却没有明确区分总样本、完成自由行走任务的样本以及实际发生冻结的样本。",
     "where": "第4.5节：“2025 年 Wilkins 等 [R24] 在 7 人中研究基于 STN beta burst 持续时间的实时自适应刺激”；结构化附录E24：“实时burst驱动刺激可行并有短期运动获益”。原始研究PMID 40677701。【turn686332search0】"
    }
   ]
  },
  {
   "n": 3,
   "verdict": "met",
   "issues": [
    {
     "severity": "moderate",
     "what": "冲突分析已经涉及任务、时间窗、频段、药物状态、测量尺度及统计层级，但没有系统地把不同FOG运动学亚型作为跨研究比较变量。报告在定义部分区分了akinetic freezing和kinetic trembling，但后续证据矩阵没有持续应用这一分类。R37中不同冻结表现的比例说明，这可能是影响研究结果方向的重要来源。",
     "where": "第1.1节：“区分 akinetic freezing、kinetic trembling”；第3.1至3.3节的冲突分析（L168-L242）。"
    },
    {
     "severity": "minor",
     "what": "机制模型具有清晰预测和证伪条件，但H2步态相位编码失稳与H4皮层-STN解耦在部分预测上存在重叠。虽然报告承认模型可能共同作用，但仍可以进一步明确两者各自独立的必要条件和干预中介指标。",
     "where": "第6节H2：“步态周期相位编码失稳”；H4：“皮层—STN网络解耦”；模型比较表（L406-L452）。"
    }
   ]
  },
  {
   "n": 4,
   "verdict": "met",
   "issues": [
    {
     "severity": "minor",
     "what": "原始文献、单项证据、跨研究综合、机制模型和研究假说之间的层次清晰，附录也建立了ref、eid、cid和hid关联。需要注意的是，supported、well-supported、contested等状态属于作者定性判断，尚没有可重复执行的评分规则。报告已明确说明不是正式GRADE评级，因此这是标准化程度的不足，而不是知识层次混乱。",
     "where": "第1.4节知识分层（L88-L99）；第8.3节：“status代表本研究对证据确定性的定性评价，不是通过GRADE全套程序独立计算的正式评级。”（L621-L625）"
    }
   ]
  },
  {
   "n": 5,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "结构化附录具有良好的长期检索基础，JSON结构有效，包含文献、证据、结论和假说之间的关联。但目前只能确认单份报告内部存在结构化数据，不能确认这些数据已经进入持久化证据库，也没有版本控制、修改历史、文献去重审计记录和逐条证据更新日志。",
     "where": "第8.2节：“每条证据以 eid 作为可追溯最小单位，文献以 ref 去重，跨研究结论以 cid 保存，竞争性假说以 hid 保存。”（L604-L607）"
    },
    {
     "severity": "moderate",
     "what": "新研究触发旧结论重新评价的规则已经提出，但没有展示实际执行记录。例如，没有展示一项新研究进入数据库后，如何自动或定期定位相关旧结论、重新计算证据权重、保存旧版本并记录结论变化。因此目前证明的是维护方案，而不是已经运行的长期积累系统。",
     "where": "第8.2节：“当出现新研究时”；“如果新研究直接反驳必要性主张，将该结论标记为 contested 并重新限定适用范围。”（L608-L616）"
    }
   ]
  },
  {
   "n": 6,
   "verdict": "met",
   "issues": [
    {
     "severity": "minor",
     "what": "总体科学推断较严谨，明确区分相关性、预测能力、治疗效果和因果介质，也没有把H1-H6之间的理论兼容性误写成实验验证。不过，部分模拟冻结研究在文字上仍需要更严格标注，避免不同实验终点被视为等价的真实FOG。",
     "where": "第1.1节、第2.1节R4以及第6节各机制模型；第9.2节：“目前不能声称 STN beta 增强是所有 FOG 的必要或充分原因。”（L642-L650）"
    }
   ]
  },
  {
   "n": 7,
   "verdict": "partly",
   "issues": [
    {
     "severity": "moderate",
     "what": "报告提供了较好的自我审计实例，包括纠正beta单一增强叙事、区分FOG易感性与实际冻结、检查队列重叠以及降低DBS因果推断强度。但所谓改进后的效果主要由报告自身描述，没有提供独立复核结果、修改前后的检索覆盖率、证据分类一致性或错误率等可验证指标。",
     "where": "第8.1节：“本次研究发现并纠正的问题”；“已实施的改进”；“复核结果”（L590-L602）。"
    },
    {
     "severity": "moderate",
     "what": "没有证明系统能够自主、持续发现新缺陷并形成闭环改进。报告展示了一次研究过程中的自我审计，但没有展示定期重新检索、自动发现冲突、触发旧结论复审、实施改进及独立验证改进有效性的连续过程。",
     "where": "第8.2节：“应建立的长期证据维护规则”；第8.1节：“本次完成的是证据结构和推断逻辑的改进与交叉核验，不是通过新临床数据证明某一机制模型更准确。”（L602-L616）"
    }
   ]
  }
 ],
 "spot_checks": [
  {
   "claim": "C1：在部分真实或虚拟冻结事件中，STN beta及theta活动升高。",
   "cited": "R3、R4、R5",
   "verdict": "consistent",
   "why": "R3的术中虚拟步态冻结研究报告STN多单位活动及theta/beta异常增强；R5在真实TUG冻结中观察到STN beta增强，因此该限定性结论有原始证据支持。R4则属于仰卧模拟踏步，不能与真实自由行走FOG等同。总体结论成立，但不应把三项研究视为相同等级的真实冻结证据。原始文献：PMID 31665229、36730026、35310098。【turn274424search0】【turn888907view0】"
  },
  {
   "claim": "C3：STN局部beta增强不是现有研究已经确立的所有FOG事件的必要条件。",
   "cited": "R8、R1、R3、R5",
   "verdict": "consistent",
   "why": "R8在自由行走研究中发现，实际冻结期间局部STN beta功率和burst持续时间没有一致变化，但冻结前出现4–13 Hz皮层-STN低频解耦。这是限制普遍beta增强模型的重要直接反例。R1也显示冻结易感性、非冻结行走和实际冻结具有不同的神经特征。不过，R8仅有7名患者，不能据此证明所有FOG亚型均不需要beta异常。报告使用“尚未确立必要条件”而不是“已证明不必要”，表述合理。PMID 31505548、28890315。【turn279520search3】【turn243818view0】"
  },
  {
   "claim": "C4：STN beta burst持续时间及活动熵可能提供平均beta功率之外的FOG相关信息。",
   "cited": "R1、R7、R8、R34、R24",
   "verdict": "consistent",
   "why": "R34发现Freezer具有较长的beta burst，且刺激可缩短较长burst；R1发现非冻结行走中的beta Sample Entropy与Freezer表型相关，而实际FOG期间增加的是alpha Sample Entropy；R7提供静息alpha及高beta burst的表型关联。因此，时间结构和熵指标可能补充平均功率是合理的跨研究综合。但必须保留频段和行为状态区别，不能把R1的beta熵直接解释成实际冻结时的beta熵。PMID 30196050、28890315、39884164。【turn102461search0】【turn243818view0】"
  },
  {
   "claim": "C6：部分FOG在发生前出现皮层-STN低频耦合异常，而局部STN功率可以不出现同步变化。",
   "cited": "R8、R25、R5",
   "verdict": "consistent",
   "why": "R8是这一结论最直接的证据：冻结前出现4–13 Hz皮层-STN耦合异常，而局部STN beta功率和burst持续时间没有一致变化。R25进一步研究了步态周期相关的皮层低beta相位调制及S1-STN theta相干性。值得注意的是，R25部分低beta异常来自S1/SPL皮层，而非STN局部功率。报告正确保留了这一空间来源区别。该结论仍受小样本及耦合方向无法确定的限制。PMID 31505548、42571859。【turn279520search3】"
  },
  {
   "claim": "C8：STN-DBS对FOG的作用受到刺激空间位置和募集网络影响。",
   "cited": "R19、R20、R21、R22、R23",
   "verdict": "consistent",
   "why": "相关研究提供了相互补充的证据：结构连接及sweet-spot研究发现不同刺激位置和网络募集与步态结局相关；R22的10人随机双盲方向性刺激研究也发现中央STN刺激在部分步态和冻结指标上优于后部感觉运动STN刺激。报告没有把这些结果升级成适用于所有患者的固定最优刺激地图，因此结论与证据强度相符。需要注意，多数空间连接研究是回顾性分析，R23的主要结局也不完全等同于FOG。PMID 35431262、36242900、37701817、39475137、40408848。【turn157655search0】"
  },
  {
   "claim": "C9：60 Hz STN-DBS可能改善某些常规高频刺激下持续存在的FOG，但并非所有患者均优于130 Hz。",
   "cited": "R9、R10、R11、R12、R13、R14",
   "verdict": "consistent",
   "why": "R13在7名常规治疗下仍有FOG的患者中发现60 Hz相对130 Hz具有改善；R14报告部分获益可延续至长期，但效应减弱。相反，R11的20人随机盲法研究没有发现主要步幅终点的显著改善，并报告低频下震颤控制较差。不同研究的人群选择、刺激参数、触点和结局不同。报告采用特定患者可能获益而非普遍优越的结论，符合原始证据。PMID 24165197、25540305、29654112。【turn505312search2】【turn505312search0】【turn505312search1】"
  },
  {
   "claim": "C10：STN+SNr联合刺激是否总体优于优化后的单纯STN刺激，目前尚无稳定确证。",
   "cited": "R15、R16、R17、R18、R28、R29",
   "verdict": "consistent",
   "why": "R18的2026年多中心随机双盲研究中，STN组23人、STN+SNr组22人，90天主要FOG-AC结局没有显著组间差异。R28 Meta分析未证实额外获益，R29则报告统计学优势，但其纳入的交叉试验缺少配对统计数据，采用平行组近似处理，存在忽略患者内相关性的风险。两项Meta分析存在研究重叠，也不是独立临床验证。报告保留这种方法学冲突，没有简单采用显著性投票，判断合理。PMID 42860886、42909654、42968793。【turn192650search0】【turn498941search0】"
  },
  {
   "claim": "C17：基于STN beta burst的实时自适应DBS已证明技术可行，但其改善FOG的特异性机制尚未确立。",
   "cited": "R24",
   "verdict": "consistent",
   "why": "R24的7人先导研究显示beta burst驱动自适应刺激在技术上可行，并观察到相对于刺激关闭的步态改善。但自适应刺激没有显示出相对于连续刺激或随机间歇刺激的稳定优势，实际自由行走冻结分析的样本也非常有限。因此，现有研究支持技术可行性和潜在治疗价值，但没有证明beta burst是FOG的特异性致病介质或治疗中介。报告对此保持了正确的因果谨慎。PMID 40677701。【turn686332search0】"
  }
 ]
}

===== B0_gpt4 / refcheck.json =====
[
 {
  "ref": "R1",
  "pmid": "28890315",
  "doi": "10.1016/j.nbd.2017.09.002",
  "title": "Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease",
  "verdict": "ok",
  "found_title": "Subthalamic neural entropy is a feature of freezing of gait in freely moving people with Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R2",
  "pmid": "31494286",
  "doi": "10.1016/j.nbd.2019.104605",
  "title": "Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease",
  "verdict": "ok",
  "found_title": "Subthalamic nucleus oscillations correlate with vulnerability to freezing of gait in patients with Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R3",
  "pmid": "31665229",
  "doi": "10.1093/brain/awz325",
  "title": "Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing",
  "verdict": "ok",
  "found_title": "Hitting the brakes: pathological subthalamic nucleus activity in Parkinson's disease gait freezing.",
  "title_sim": 1.0
 },
 {
  "ref": "R4",
  "pmid": "36730026",
  "doi": "10.1093/brain/awad006",
  "title": "Subthalamic and nigral neurons are differentially modulated during parkinsonian gait",
  "verdict": "ok",
  "found_title": "Subthalamic and nigral neurons are differentially modulated during parkinsonian gait.",
  "title_sim": 1.0
 },
 {
  "ref": "R5",
  "pmid": "35310098",
  "doi": "10.3389/fnins.2022.795417",
  "title": "Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait",
  "verdict": "ok",
  "found_title": "Synchronized Intracranial Electrical Activity and Gait Recording in Parkinson's Disease Patients With Freezing of Gait.",
  "title_sim": 1.0
 },
 {
  "ref": "R6",
  "pmid": "40709562",
  "doi": "10.1002/ana.70003",
  "title": "Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease",
  "verdict": "ok",
  "found_title": "Subthalamic Electrophysiological Mapping of Gait Initiation Dynamics and Freezing in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R7",
  "pmid": "39884164",
  "doi": "10.1016/j.clinph.2025.01.005",
  "title": "Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Alpha and high beta subthalamic intermittent activity correlates with freezing of gait severity in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R8",
  "pmid": "31505548",
  "doi": "10.1093/brain/awz141",
  "title": "Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics",
  "verdict": "ok",
  "found_title": "Freezing of gait in Parkinson's disease reflects a sudden derangement of locomotor network dynamics.",
  "title_sim": 1.0
 },
 {
  "ref": "R9",
  "pmid": "18420482",
  "doi": "10.1212/01.wnl.0000303972.16279.46",
  "title": "STN-DBS frequency effects on freezing of gait in advanced Parkinson disease",
  "verdict": "ok",
  "found_title": "STN-DBS frequency effects on freezing of gait in advanced Parkinson disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R10",
  "pmid": "22696586",
  "doi": "10.1136/jnnp-2011-302091",
  "title": "Effect of stimulation frequency on immediate freezing of gait in newly activated STN DBS in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Effect of stimulation frequency on immediate freezing of gait in newly activated STN DBS in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R11",
  "pmid": "24165197",
  "doi": "10.1111/ner.12131",
  "title": "60-Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation",
  "verdict": "ok",
  "found_title": "60-Hz frequency effect on gait in Parkinson's disease with subthalamic nucleus deep brain stimulation.",
  "title_sim": 1.0
 },
 {
  "ref": "R12",
  "pmid": "24449169",
  "doi": "",
  "title": "Low-frequency subthalamic nucleus stimulation in Parkinson's disease: a randomized clinical trial",
  "verdict": "ok",
  "found_title": "Low-frequency subthalamic nucleus stimulation in Parkinson's disease: a randomized clinical trial.",
  "title_sim": 1.0
 },
 {
  "ref": "R13",
  "pmid": "25540305",
  "doi": "10.1212/WNL.0000000000001184",
  "title": "Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD",
  "verdict": "ok",
  "found_title": "Low-frequency stimulation of STN-DBS reduces aspiration and freezing of gait in patients with PD.",
  "title_sim": 1.0
 },
 {
  "ref": "R14",
  "pmid": "29654112",
  "doi": "10.1136/jnnp-2018-318060",
  "title": "Long-term effect of low frequency stimulation of STN on dysphagia, freezing of gait and other motor symptoms in PD",
  "verdict": "ok",
  "found_title": "Long-term effect of low frequency stimulation of STN on dysphagia, freezing of gait and other motor symptoms in PD.",
  "title_sim": 1.0
 },
 {
  "ref": "R15",
  "pmid": "23757762",
  "doi": "10.1093/brain/awt122",
  "title": "Nigral stimulation for resistant axial motor impairment in Parkinson's disease? A randomized controlled trial",
  "verdict": "ok",
  "found_title": "Nigral stimulation for resistant axial motor impairment in Parkinson's disease? A randomized controlled trial.",
  "title_sim": 1.0
 },
 {
  "ref": "R16",
  "pmid": "39957196",
  "doi": "10.1177/1877718X241292315",
  "title": "Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial",
  "verdict": "ok",
  "found_title": "Subthalamic and nigral stimulation for freezing of gait in Parkinson's disease: Randomized pilot trial.",
  "title_sim": 1.0
 },
 {
  "ref": "R17",
  "pmid": "40760816",
  "doi": "10.1177/1877718X251359241",
  "title": "DBS-STN&SNr combined stimulation versus DBS-STN monotarget stimulation for Parkinson's disease freezing: A comparative efficacy study",
  "verdict": "ok",
  "found_title": "DBS-STN&amp;SNr combined stimulation versus DBS-STN monotarget stimulation for Parkinson's disease freezing: A comparative efficacy study.",
  "title_sim": 1.0
 },
 {
  "ref": "R18",
  "pmid": "42860886",
  "doi": "10.1002/mdc3.70813",
  "title": "Disease Duration Differentiates Freezing of Gait Response to Subthalamic and Nigral Stimulation for Parkinson's Disease in an Exploratory Multicenter Controlled Trial",
  "verdict": "ok",
  "found_title": "Disease Duration Differentiates Freezing of Gait Response to Subthalamic and Nigral Stimulation for Parkinson's Disease in an Exploratory Multicenter Controlled Trial.",
  "title_sim": 1.0
 },
 {
  "ref": "R19",
  "pmid": "35431262",
  "doi": "10.3233/JPD-212997",
  "title": "Structural Connectivity of Subthalamic Nucleus Stimulation for Improving Freezing of Gait",
  "verdict": "ok",
  "found_title": "Structural Connectivity of Subthalamic Nucleus Stimulation for Improving Freezing of Gait.",
  "title_sim": 1.0
 },
 {
  "ref": "R20",
  "pmid": "36242900",
  "doi": "10.1016/j.parkreldis.2022.10.002",
  "title": "Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients",
  "verdict": "ok",
  "found_title": "Freezing of gait depends on cortico-subthalamic network recruitment following STN-DBS in PD patients.",
  "title_sim": 1.0
 },
 {
  "ref": "R21",
  "pmid": "37701817",
  "doi": "10.1093/braincomms/fcad238",
  "title": "Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Optimal subthalamic stimulation sites and related networks for freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R22",
  "pmid": "39475137",
  "doi": "10.1002/ana.27099",
  "title": "Directional Subthalamic Deep Brain Stimulation Better Improves Gait and Balance Disorders in Parkinson's Disease Patients: A Randomized Controlled Study",
  "verdict": "ok",
  "found_title": "Directional Subthalamic Deep Brain Stimulation Better Improves Gait and Balance Disorders in Parkinson's Disease Patients: A Randomized Controlled Study.",
  "title_sim": 1.0
 },
 {
  "ref": "R23",
  "pmid": "40408848",
  "doi": "10.1016/j.parkreldis.2025.107871",
  "title": "Probabilistic mapping of gait changes after STN-DBS for Parkinson's disease",
  "verdict": "ok",
  "found_title": "Probabilistic mapping of gait changes after STN-DBS for Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R24",
  "pmid": "40677701",
  "doi": "10.1093/braincomms/fcaf266",
  "title": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R25",
  "pmid": "42571859",
  "doi": "10.1016/j.nbd.2026.107571",
  "title": "Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Gait-cycle-locked cortico-subthalamic signatures underlying freezing of gait and their modulation in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R26",
  "pmid": "41388789",
  "doi": "10.1093/brain/awaf464",
  "title": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping",
  "verdict": "ok",
  "found_title": "Dopamine and the dynamics of subthalamic and leg muscle activities in parkinsonian stepping.",
  "title_sim": 1.0
 },
 {
  "ref": "R27",
  "pmid": "35295883",
  "doi": "10.3389/fnhum.2022.812954",
  "title": "Combined Subthalamic and Nigral Stimulation Modulates Temporal Gait Coordination and Cortical Gait-Network Activity in Parkinson's Disease",
  "verdict": "ok",
  "found_title": "Combined Subthalamic and Nigral Stimulation Modulates Temporal Gait Coordination and Cortical Gait-Network Activity in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R28",
  "pmid": "42909654",
  "doi": "10.1007/s10072-026-09479-2",
  "title": "STN-SNr co-stimulation in Parkinson's disease: a systematic review and meta-analysis of motor and freezing-of-gait outcomes",
  "verdict": "ok",
  "found_title": "STN-SNr co-stimulation in Parkinson's disease: a systematic review and meta-analysis of motor and freezing-of-gait outcomes.",
  "title_sim": 1.0
 },
 {
  "ref": "R29",
  "pmid": "42968793",
  "doi": "10.1136/bmjcsurg-2026-000033",
  "title": "Superiority of dual-target STN-SNr deep brain stimulation towards gait in Parkinson's disease: a meta-analysis and meta-regression of randomised trials",
  "verdict": "ok",
  "found_title": "Superiority of dual-target STN-SNr deep brain stimulation towards gait in Parkinson's disease: a meta-analysis and meta-regression of randomised trials.",
  "title_sim": 1.0
 },
 {
  "ref": "R30",
  "pmid": "37226972",
  "doi": "10.1002/mds.29455",
  "title": "Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease",
  "verdict": "ok",
  "found_title": "Subthalamic Nucleus Activity during Cognitive Load and Gait Dysfunction in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R31",
  "pmid": "",
  "doi": "10.1016/j.baga.2012.10.002",
  "title": "Freezing of gait-related oscillatory activity in the human subthalamic nucleus",
  "verdict": "ok",
  "found_title": "Freezing of gait-related oscillatory activity in the human subthalamic nucleus",
  "title_sim": 1.0
 },
 {
  "ref": "R32",
  "pmid": "24361601",
  "doi": "10.1016/j.nbd.2013.12.005",
  "title": "High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "High beta activity in the subthalamic nucleus and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R33",
  "pmid": "28892573",
  "doi": "10.1002/ana.25047",
  "title": "Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia",
  "verdict": "ok",
  "found_title": "Bicycling suppresses abnormal beta synchrony in the Parkinsonian basal ganglia.",
  "title_sim": 1.0
 },
 {
  "ref": "R34",
  "pmid": "30196050",
  "doi": "10.1016/j.nbd.2018.09.004",
  "title": "Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Neuromodulation targets pathological not physiological beta bursts during gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R35",
  "pmid": "29760182",
  "doi": "10.1523/JNEUROSCI.3596-17.2018",
  "title": "Alternating Modulation of Subthalamic Nucleus Beta Oscillations during Stepping",
  "verdict": "ok",
  "found_title": "Alternating Modulation of Subthalamic Nucleus Beta Oscillations during Stepping.",
  "title_sim": 1.0
 },
 {
  "ref": "R36",
  "pmid": "36070366",
  "doi": "10.1126/scitranslmed.abo1800",
  "title": "Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease",
  "verdict": "ok",
  "found_title": "Principles of gait encoding in the subthalamic nucleus of people with Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R37",
  "pmid": "39470410",
  "doi": "10.1093/brain/awae223",
  "title": "Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Supraspinal contributions to defective antagonistic inhibition and freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R38",
  "pmid": "24142148",
  "doi": "10.1093/brain/awt272",
  "title": "Freezing of gait in Parkinson's disease is associated with functional decoupling between the cognitive control network and the basal ganglia",
  "verdict": "ok",
  "found_title": "Freezing of gait in Parkinson's disease is associated with functional decoupling between the cognitive control network and the basal ganglia.",
  "title_sim": 1.0
 },
 {
  "ref": "R39",
  "pmid": "23831480",
  "doi": "10.1016/j.parkreldis.2013.06.002",
  "title": "Using virtual reality to explore the role of conflict resolution and environmental salience in freezing of gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Using virtual reality to explore the role of conflict resolution and environmental salience in freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R40",
  "pmid": "38101024",
  "doi": "10.1016/j.parkreldis.2023.105952",
  "title": "Subthalamic functional connectivity associated with freezing of gait dopa-response",
  "verdict": "ok",
  "found_title": "Subthalamic functional connectivity associated with freezing of gait dopa-response.",
  "title_sim": 1.0
 },
 {
  "ref": "R41",
  "pmid": "22262741",
  "doi": "10.1212/WNL.0b013e3182477ec0",
  "title": "\"On\" state freezing of gait in Parkinson disease: a paradoxical levodopa-induced complication",
  "verdict": "ok",
  "found_title": "\"On\" state freezing of gait in Parkinson disease: a paradoxical levodopa-induced complication.",
  "title_sim": 1.0
 },
 {
  "ref": "R42",
  "pmid": "31799377",
  "doi": "10.1038/s41531-019-0099-z",
  "title": "Freezing of Gait can persist after an acute levodopa challenge in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Freezing of Gait can persist after an acute levodopa challenge in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R43",
  "pmid": "32417798",
  "doi": "10.3233/JPD-201997",
  "title": "Biphasic Levodopa-Induced Freezing of Gait in Parkinson's Disease",
  "verdict": "ok",
  "found_title": "Biphasic Levodopa-Induced Freezing of Gait in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R44",
  "pmid": "19773356",
  "doi": "10.1093/brain/awp229",
  "title": "Effects of pedunculopontine nucleus area stimulation on gait disorders in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Effects of pedunculopontine nucleus area stimulation on gait disorders in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R45",
  "pmid": "21725254",
  "doi": "10.1227/NEU.0b013e31822b6f71",
  "title": "Pedunculopontine nucleus stimulation improves gait freezing in Parkinson disease",
  "verdict": "ok",
  "found_title": "Pedunculopontine nucleus stimulation improves gait freezing in Parkinson disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R46",
  "pmid": "22232591",
  "doi": "10.1093/brain/awr315",
  "title": "Alpha oscillations in the pedunculopontine nucleus correlate with gait performance in parkinsonism",
  "verdict": "ok",
  "found_title": "Alpha oscillations in the pedunculopontine nucleus correlate with gait performance in parkinsonism.",
  "title_sim": 1.0
 },
 {
  "ref": "R47",
  "pmid": "34744048",
  "doi": "10.3233/JPD-212793",
  "title": "Pedunculopontine and Cuneiform Nuclei Deep Brain Stimulation for Severe Gait and Balance Disorders in Parkinson's Disease: Interim Results from a Randomized Double-Blind Clinical Trial",
  "verdict": "ok",
  "found_title": "Pedunculopontine and Cuneiform Nuclei Deep Brain Stimulation for Severe Gait and Balance Disorders in Parkinson's Disease: Interim Results from a Randomized Double-Blind Clinical Trial.",
  "title_sim": 1.0
 },
 {
  "ref": "R48",
  "pmid": "35121249",
  "doi": "10.1016/j.parkreldis.2022.01.010",
  "title": "Stimulation of the pedunculopontine and cuneiform nuclei for freezing of gait and falls in Parkinson disease: Cross-over single-blinded study and long-term follow-up",
  "verdict": "ok",
  "found_title": "Stimulation of the pedunculopontine and cuneiform nuclei for freezing of gait and falls in Parkinson disease: Cross-over single-blinded study and long-term follow-up.",
  "title_sim": 1.0
 },
 {
  "ref": "R49",
  "pmid": "25185212",
  "doi": "10.1136/jnnp-2013-307511",
  "title": "Low-frequency versus high-frequency stimulation of the pedunculopontine nucleus area in Parkinson's disease: a randomised controlled trial",
  "verdict": "ok",
  "found_title": "Low-frequency versus high-frequency stimulation of the pedunculopontine nucleus area in Parkinson's disease: a randomised controlled trial.",
  "title_sim": 1.0
 },
 {
  "ref": "R50",
  "pmid": "41760132",
  "doi": "10.1002/mds.70230",
  "title": "Aberrant Beta-Band Network Alteration Preceding Freezing of Gait in Parkinson's Disease",
  "verdict": "ok",
  "found_title": "Aberrant Beta-Band Network Alteration Preceding Freezing of Gait in Parkinson's Disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R51",
  "pmid": "42778807",
  "doi": "10.1007/s00415-026-14149-6",
  "title": "Frequency-Specific EEG burst dynamics in Parkinson's Disease and freezing of gait",
  "verdict": "ok",
  "found_title": "Frequency-Specific EEG burst dynamics in Parkinson's Disease and freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "R52",
  "pmid": "42239677",
  "doi": "10.3389/fneur.2026.1793291",
  "title": "An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease",
  "verdict": "ok",
  "found_title": "An initial machine learning model applied to local field potential data from the subthalamic nucleus to detect freezing of gait in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R53",
  "pmid": "39252998",
  "doi": "10.1093/braincomms/fcae286",
  "title": "Dynamic balance and gait impairments in Parkinson's disease: novel cholinergic patterns",
  "verdict": "ok",
  "found_title": "Dynamic balance and gait impairments in Parkinson's disease: novel cholinergic patterns.",
  "title_sim": 1.0
 },
 {
  "ref": "R54",
  "pmid": "",
  "doi": "10.1186/s12984-024-01320-1",
  "title": "Freezing of gait assessment with inertial measurement units and deep learning: effect of tasks, medication states, and stops",
  "verdict": "ok",
  "found_title": "Freezing of gait assessment with inertial measurement units and deep learning: effect of tasks, medication states, and stops.",
  "title_sim": 1.0
 },
 {
  "ref": "R55",
  "pmid": "42230618",
  "doi": "10.1038/s41531-026-01407-7",
  "title": "Deep learning for freezing of gait assessment using inertial measurement units: a multicentre validation study",
  "verdict": "ok",
  "found_title": "Deep learning for freezing of gait assessment using inertial measurement units: a multicentre validation study.",
  "title_sim": 1.0
 },
 {
  "ref": "R56",
  "pmid": "41513745",
  "doi": "10.1038/s41582-025-01179-3",
  "title": "An updated definition of freezing of gait",
  "verdict": "ok",
  "found_title": "An updated definition of freezing of gait.",
  "title_sim": 1.0
 },
 {
  "ref": "R57",
  "pmid": "39121137",
  "doi": "10.3233/JPD-240134",
  "title": "Which Gait Tasks Produce Reliable Outcome Measures of Freezing of Gait in Parkinson's Disease?",
  "verdict": "ok",
  "found_title": "Which Gait Tasks Produce Reliable Outcome Measures of Freezing of Gait in Parkinson's Disease?",
  "title_sim": 1.0
 },
 {
  "ref": "R58",
  "pmid": "24386308",
  "doi": "10.1371/journal.pone.0083919",
  "title": "Pedunculopontine nucleus area oscillations during stance, stepping and freezing in Parkinson's disease",
  "verdict": "ok",
  "found_title": "Pedunculopontine nucleus area oscillations during stance, stepping and freezing in Parkinson's disease.",
  "title_sim": 1.0
 },
 {
  "ref": "R59",
  "pmid": "42522567",
  "doi": "10.1093/brain/awag259",
  "title": "Distinct roles of the human cuneiform and pedunculopontine nuclei in gait and freezing of gait",
  "verdict": "ok",
  "found_title": "Distinct roles of the human cuneiform and pedunculopontine nuclei in gait and freezing of gait.",
  "title_sim": 1.0
 }
]

===== blind_B0_gpt3_vs_S2.json（better/items 已换成版本名）=====
[
 {
  "seat": "aX",
  "judge": "g6",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "S2"
  },
  "why": "总体而言，Y更好地完成了研究任务。决定性优势不是篇幅，而是研究覆盖、证据可追溯性、冲突综合、竞争性机制的可检验性，以及长期知识积累能力的综合优势。Y不仅回答了STN神经活动与FOG是否相关，还进一步回答了哪些研究观察的是易感性、哪些观察的是实际冻结，为什么不同研究会出现相反结果，以及怎样通过实验区分局部beta病理、网络解耦、脑干通路调节和认知运动竞争等解释。它还将研究成果转化成能够继续更新的证据—结论—假说体系。X并非质量较差：其对14项核心STN电生理研究的叙述比较集中，研究条件、关键指标及局限性讲解清楚，作为聚焦STN-LFP机制的研究综述具有较高价值。但相比之下，X的交叉研究覆盖、结构化证据规模、竞争性假说细分和持续更新机制均有所不足。因此，如果目标是建立能够支持后续研究、持续纳入新证据并重新评价既有机制的研究成果，应优先选择Y。需要保留的最终判断是：Y虽然更好，但其538条证据记录仍需区分原始实验、综述转述、预印本和机制推测，不能把证据数据库规模直接等同于因果证据强度。"
 },
 {
  "seat": "aX",
  "judge": "g56",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "S2"
  },
  "why": "Y总体上更好地完成了研究任务。决定性优势不是篇幅或引用数量，而是它在核心STN电生理研究之外，补充了重要的临床干预、脑干运动网络、认知机制及2025—2026年新证据；更完整地解释了不同研究之间的冲突；提出了具有明确区分性预测和证伪条件的竞争性机制；并建立了可以持续更新的证据—结论—假说知识体系。X是一份质量较高、相对聚焦且谨慎的研究报告，在核心电生理证据的组织方面表现良好，但在覆盖广度、冲突综合和长期知识管理方面不及Y。Y并非没有缺陷：需要修正PMID 36070366的发表状态，核对538/539条记录的数量差异，区分独立研究与同一研究拆分出的证据条目，并进一步复核部分预印本及摘要提取数据。上述问题属于可以明确定位和修正的质量缺陷，不足以改变Y整体优于X的判断。"
 },
 {
  "seat": "bX",
  "judge": "g6",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "tie"
  },
  "why": "X总体上更好地完成了研究任务。决定性优势不在于篇幅或证据记录数量，而在于它将更广泛的研究覆盖、更细粒度的原始证据、更深入的冲突分析、可区分的竞争性机制以及长期知识更新机制结合起来。尤其是对beta功率方向冲突、beta burst时间结构、皮层-STN动态耦合和DBS作用机制的分析，X更接近一份能够指导后续功能神经外科研究的综合研究报告。Y是一份质量较高、方法透明、核心论证较严谨的研究综述，特别是在主要原始电生理研究和机制模型方面表现良好。但相较之下，它对最新证据的吸收、复杂争议的拆解和知识体系的持续更新设计仍不够充分。因此，综合coverage、evidence、synthesis和structure四项优势，最终判断X更好；rigor则两者各有优势，判定为平局。"
 },
 {
  "seat": "bX",
  "judge": "g56",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "tie"
  },
  "why": "X总体更好地完成了研究任务。决定性优势不在篇幅，而在于它将更广泛的原始研究和交叉领域证据转化成了可追溯、可比较、可反驳、可更新的研究体系。它不仅识别STN beta功率方向不一致的问题，还进一步区分了不同运动状态、频段、时间结构、解剖区域和网络连接所代表的生理过程，并提出具有明确判别实验的竞争性机制。X尤其出色地完成了研究结果冲突分析、证据与假说分层，以及长期知识积累和自主质量改进设计。Y是一份质量较高、重点突出、结构清晰的研究报告，其检索方法披露和部分全脑网络交叉证据具有独特价值，但证据覆盖、原始证据颗粒度、临床干预冲突分析及长期知识管理能力相对有限。因此，如果目标是建立能够持续检索、重新评价证据并指导后续功能神经外科研究的知识体系，X是更合适的选择。"
 }
]

===== blind_B0_gpt4_vs_S2.json（better/items 已换成版本名）=====
[
 {
  "seat": "aX",
  "judge": "g6",
  "better": "B0_gpt4",
  "items": {
   "coverage": "S2",
   "evidence": "B0_gpt4",
   "synthesis": "B0_gpt4",
   "structure": "S2",
   "rigor": "B0_gpt4"
  },
  "why": "总体选择X。Y在研究覆盖和知识库结构方面明显领先，尤其适合作为后续文献发现、跨方向研究和长期知识积累的基础。X则在本研究任务最重要的三个方面——原始证据准确性、矛盾解释的可靠性和机制因果推断的科学严谨性——表现更好。Y提出了更多机制模型，但其对Syrkin-Nikolau 2017及Thenaisie 2022研究的关键误读，直接影响了核心beta证据冲突的判断；预印本与正式论文重复记录也削弱了证据体系的可信度。X没有Y那样广泛的研究地图和复杂的知识库，但其核心证据链更加可靠，六个竞争性机制也具有明确的可检验预测和证伪条件。对于以STN神经活动与FOG关系、研究冲突及因果机制判别为中心的任务，可靠解释原始证据比扩大文献和假说数量更加重要。因此，X是更好的最终研究报告；Y的研究覆盖、文献索引和知识管理框架值得保留，但应先纠正原始文献误读、完成版本去重和证据数量核对，再将其优势整合进X。"
 },
 {
  "seat": "aX",
  "judge": "g56",
  "better": "B0_gpt4",
  "items": {
   "coverage": "S2",
   "evidence": "B0_gpt4",
   "synthesis": "B0_gpt4",
   "structure": "B0_gpt4",
   "rigor": "B0_gpt4"
  },
  "why": "Y在研究覆盖和部分新兴电生理机制方面更有优势，特别是分阶段皮层-STN耦合、beta burst分布及低频刺激的竞争性机制解释。但研究任务的核心不只是收集更多论文或提出更多假说，而是可靠地判断STN神经活动与FOG之间究竟存在什么关系，以及哪些解释真正得到实验支持。X在证据可追溯性、冲突分析、知识分层和因果推断方面表现更好。它不仅保留支持beta异常的研究，也认真处理反例、阴性结果、统计方法差异和队列重叠，并将这些证据转化为具有明确区分预测和证伪条件的机制模型。因此，尽管Y是一份更广泛的研究资料库，X是完成本次科学研究任务质量更高、结论更值得信赖的报告。"
 },
 {
  "seat": "bX",
  "judge": "g6",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "B0_gpt4",
   "rigor": "B0_gpt4"
  },
  "why": "总体而言，X更好地完成了研究任务，但优势不是简单来自篇幅或文献数量，而是来自更广泛的STN/DBS研究覆盖、更细粒度的原始证据提取、更完整的冲突分析，以及更丰富的竞争性机制和区分性实验设计。尤其值得肯定的是X的长期知识积累与持续改进设计：它建立了稳定的证据编号、结论关系图、新证据触发旧结论重新评价的规则，以及包含检索覆盖率、证据提取准确性、可追溯性、冲突识别和预测验证的质量控制流程。这直接回应了研究任务中的长期积累和自主改进要求，Y虽然也有自我审计和更新规则，但尚未达到同等程度。Y的优势主要集中在知识分层、研究方法透明度和FOG事件测量规范性。最理想的后续版本应以X为主体，吸收Y的2026年FOG定义共识、PPN/CuN直接电生理证据、多中心检测外部验证，以及更加明确的finding层级，并修正X的证据计数和摘要/正文数值不一致问题。两份报告都没有真正通过新实验验证某个竞争性机制，因此X的13个假说及Y的6个模型都应继续保持假说地位。最终判断：X是更完整、更适合长期积累和后续研究迭代的研究成果；Y则是方法学表达和知识分层方面更好的参考版本。"
 },
 {
  "seat": "bX",
  "judge": "g56",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "B0_gpt4",
   "rigor": "B0_gpt4"
  },
  "why": "综合判断为X略胜。Y在科学严谨性和知识分层方面更好，特别适合作为结构清晰、方法学边界明确的研究综述。但研究任务不仅要求准确解释现有神经电生理证据，还要求尽可能覆盖相关研究方向、分析冲突、提出可区分的机制假说，并建立能够长期积累和自主改进的研究体系。X在这些方面整体完成得更充分：研究覆盖更广，原始证据提取更细，竞争性假说更多，研究优先级和验证方案更具体。尤其是第九部分建立了稳定证据编号、证据—结论—假说关联、旧结论更新触发规则、检索查询模板、质量评价指标和持续审计循环，较好回应了长期积累及持续自主改进两项要求。Y也有自我审计和知识更新机制，但尚未达到X那样具体的证据维护和更新设计。因此，虽然Y在严谨性与结构上具有明确优势，X对整个研究任务的综合完成程度更高。"
 }
]

===== blind_B1_vs_S2.json（better/items 已换成版本名）=====
[
 {
  "seat": "aX",
  "judge": "g6",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "tie"
  },
  "why": "总体上Y更好地完成了研究任务。这个判断不是基于篇幅或证据条目数量本身，而是基于其在研究覆盖、证据追溯、跨研究综合、竞争性机制区分和长期知识管理方面形成了更完整的研究体系。尤其是Y不仅总结已有结果，还建立了证据与结论之间的关联，提出可证伪的竞争性假说，并设计了能够区分这些假说的实验及后续更新机制。X并非质量较低的报告，其正文对若干重要交叉研究的具体分析甚至更突出，且具有更清晰的E1-E6因果证据分层。最理想的改进方向是以Y为主体，吸收X关于STN步态编码、STN/SNr单单位活动、拮抗肌输出及感觉反馈的专门分析，同时保留X较清晰的因果证据等级体系。Y仍需加强对部分二手证据的原始文献复核，并避免13个假说之间的概念重叠。尽管如此，按照本研究任务的七项总体标准及指定的五项分项标准，Y具有更明显的综合优势。"
 },
 {
  "seat": "aX",
  "judge": "g56",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "S2"
  },
  "why": "Y更好地完成了研究任务。决定性优势不是篇幅或引用数量，而是它在核心STN电生理证据上具有更完整的覆盖，在相互矛盾的研究结果之间建立了更细致的条件性解释，并提出了更多能够通过实验区分的竞争性机制。它还将研究成果组织成可持续更新的证据—结论—机制—假说体系，较好地回应了长期积累和持续改进要求。X并非质量较差：其优势是研究焦点更集中、E1–E6证据等级清晰，并且提出了一项相对完整、可执行的多中心研究设计。但X遗漏了若干重要的直接FOG证据和跨研究冲突，机制竞争也相对简化。Y的主要改进方向是加强预印本与正式论文的队列去重、统一证据记录数量，并对每条核心Claim开展更严格的原始文献复核。因此，综合五项评价，选择Y。"
 },
 {
  "seat": "bX",
  "judge": "g6",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "B1",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "B1"
  },
  "why": "总体判断为X更好地完成了研究任务，但优势并非所有维度都成立。X在研究覆盖的时效性、跨研究深度综合、竞争性机制的可检验性以及长期知识结构方面更有优势。特别是它不满足于提出beta异常或网络失调等宽泛解释，而是进一步提出能够通过选择性干预区分的机制模型，并明确相应的预测、反证条件和实验优先级。这直接回应了研究问题的核心。Y的优势在于原始文献证据呈现、方法学透明度及系统性偏倚审查，并补充了若干X没有充分展开的交叉研究方向。因此，X并非证据质量全面优于Y，而是其在研究任务最核心的机制综合、竞争性假说和知识体系建设方面取得了更好的整体平衡。若进一步改进X，最值得补充的是明确检索与筛选流程、统一原始文献和预印本的证据等级，并加强运动伪迹、样本选择及外部验证方面的审查。"
 },
 {
  "seat": "bX",
  "judge": "g56",
  "better": "S2",
  "items": {
   "coverage": "S2",
   "evidence": "S2",
   "synthesis": "S2",
   "structure": "S2",
   "rigor": "S2"
  },
  "why": "综合判断，X更好地完成了研究任务。决定性优势不是篇幅或文献数量，而是它同时具备更广的证据覆盖、更细致的原始证据追溯、更完整的冲突解释、更明确的知识分层，以及更可操作的竞争性机制假说。特别是X不仅提出STN beta可能具有因果作用或仅仅是运动状态标志这两种解释，还进一步提出了区分局部STN振荡与脑干通路作用、代偿性与病理性网络耦合的具体实验预测，能够将文献综合推进到可证伪的研究设计。Y并非质量较差的报告，其在认知负荷、theta动态、STN-SNr功能差异、肌肉输出、骑行及感觉反馈方面有值得吸收的内容，尤其是periodic/aperiodic频谱分解可以补强X的分析框架。但Y的近年临床综合证据覆盖、证据索引粒度、机制竞争设计及长期更新体系均相对不足。建议以X作为主知识库和后续研究基础，将Y的独特神经生理分析方向整合进去，同时优先修正X的来源版本标注、证据数量统计及原始研究去重问题。"
 }
]