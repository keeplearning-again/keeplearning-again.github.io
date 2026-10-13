# 网站已有内容清单

以下为 2026-10-13 升级前的内容快照；新版主页见 [升级说明](HOMEPAGE_UPGRADE.md)。该快照中，本地网站有 1 个个人主页和 17 个内容详情页，另有 2 份简历。主要可用内容是个人经历、4 篇学习笔记，以及简历中的论文和研究项目；网站的论文与项目详情页目前都是模板示例。

内容判断以实际 HTML 正文、`index.json` 和 PDF 附件为依据。「有正文」表示已有实质文字，不表示内容经过学术审校或已经适合直接发布。

## 个人主页

入口：[主页文件](../index.html)。主页的 5 个区块为 `about`、`section-features`、`section-experience`、`posts`、`contact`。

| 部分 | 已有内容 | 完成情况 |
| --- | --- | --- |
| 身份与头像 | Ruiqiang Xiao、HKUST MSc student、学校链接、头像与社交入口 | 已配置；身份信息需要更新核对 |
| Biography | 一句个人介绍，以 `His research interest relies in` 结尾 | 句子尚未写完 |
| 研究兴趣 | 医学图像分割、计算机视觉与机器学习；多模态生物医学图像整合；AI4Science 与 AI + Engineering | 已有方向列表 |
| 技能 | Python 90%、Pytorch 80%、Photography 10% | 已有展示 |
| 教育与经历 | HKUST 硕士、香港建造业机器人中心研究实习、NUS 交换、东南大学本科；包含成绩与荣誉 | 已有时间线；部分日期和简历不同 |
| Recent Posts | 差分隐私文章入口，阅读时间显示为 0 分钟 | 区块存在，但指向空正文文章 |
| Contact 与 CV | 邮箱、联系说明、`uploads/resume.pdf` 下载入口 | 已有入口 |

导航包含 Home、Posts、Publication and Project、Contact、CV。其中 `Publication and Project` 指向 `/#projects`，而主页没有 `projects` 区块。论文和项目的列表文件分别存在于 [publication/index.html](../publication/index.html) 和 [project/index.html](../project/index.html)。

## 博客

`post/` 中共有 10 个详情页，均存在于搜索索引中。

### 已有正文的学习笔记

| 页面 | 已有内容 | 后续可完善的方向 |
| --- | --- | --- |
| [Self-attention mechanism and Transformers](../post/transformer/index.html) | 输入与输出、序列标注、自注意力、多头注意力、CNN/RNN 对比、Transformer 编码器和解码器、训练、Teacher Forcing、Scheduled Sampling；是现有原创笔记中篇幅最长的一篇 | 补图示、参考文献，统一中英文和公式呈现 |
| [Typora+Markdown快速入门](../post/markdown+typora/index.html) | Markdown 的用途、标题、列表、公式、代码块、文本格式、引用、视频、折叠内容等使用笔记 | 检查公式、快捷键与格式示例的实际展示 |
| [Computer vision basic tasks](../post/计算机视觉任务/index.html) | 分类、定位、检测、语义与实例分割；机器学习范式、交叉熵、研究方向 | 补反向传播等目前只有标题的部分 |
| [Some ChatGPT findings](../post/chatgpt总结/index.html) | ChatGPT 能力边界、语言模型基本理解、写作辅助用途与使用笔记 | 摘要描述的是注意力历史与 Transformer decoder，与正文不符；页面记录日期为 2022-08-15，需核对 |

### 未完成条目

| 页面 | 当前内容 | 完成情况 |
| --- | --- | --- |
| [Basic concept in differencial privacy in reinforcement learning](../post/20230326_differencial_privacy/index.html) | 有标题、作者、日期与页面框架 | 正文为空；标题及路径中的 `differencial` 拼写需检查，改 URL 时要处理旧链接 |
| [Some interesting findings of attention mechanism history](../post/attention机制溯源/index.html) | 摘要介绍注意力机制历史的讨论动机；正文只有「明确ChatGPT能解决问题的边界」一句 | 摘要与正文不匹配，文章未展开 |
| [车道线论文大合集](../post/车道线论文大合集/index.html) | 仅有页面框架；目录名说明预期主题 | 标题、正文、摘要为空，搜索索引发布时间为 `0001-01-01` |

### 模板教程

| 页面 | 内容与配套文件 | 判断依据 |
| --- | --- | --- |
| [Welcome to Wowchemy, the website builder for Hugo](../post/getting-started/index.html) | Wowchemy 入门说明；开头另有一段测试代码 | 正文说明模板用途和初始示例内容 |
| [Writing technical content in Markdown](../post/writing-technical-content/index.html) | 代码、数学、图表等功能演示；附 `results.csv`、`line-chart.json` | 正文自述为 Wowchemy 技术内容示例 |
| [Display Jupyter Notebooks with Academic](../post/jupyter/index.html) | Python、Jupyter 安装和发布教程；有输出截图 | 正文为 Academic/Wowchemy 发布功能教程；仓库没有原始 `.ipynb` |

## 论文页面

论文列表：[publication/index.html](../publication/index.html)。3 个详情页都是模板，不能当作真实学术成果。

| 页面 | 当前内容与附件 |
| --- | --- |
| [An example conference paper](../publication/conference-paper/index.html) | 2013 年会议论文示例；Lorem ipsum 摘要；`cite.bib`；1 页 `conference-paper.pdf`，正文为 `Example PDF` 与占位文字 |
| [An example journal article](../publication/journal-article/index.html) | 2015 年期刊论文示例；Lorem ipsum 摘要；`cite.bib` |
| [An example preprint / working paper](../publication/preprint/index.html) | 2019 年预印本示例；Lorem ipsum 摘要与功能演示链接 |

两个 BibTeX 文件中的作者仍为 `Bighetti, Nelson and Ford, Robert`，与页面上的作者显示不一致。简历中的真实 GAEI-UNet 论文尚未出现在这些论文页或搜索索引里。

## 项目、演讲与幻灯片

| 类型 | 页面 | 当前内容 |
| --- | --- | --- |
| 项目 | [Example Project](../project/example/index.html) | 大段 Lorem ipsum；关联示例论文和示例演讲 |
| 项目 | [External Project](../project/external-project/index.html) | 外部项目链接功能示例 |
| 演讲 | [Example Talk](../talk/example-talk/index.html) | Markdown slides 功能说明；示例活动日期为 2030-06-01，地点为 Wowchemy HQ |
| 幻灯片 | [Slides](../slides/example/index.html) | Markdown、代码高亮、公式、分步显示、演讲备注和主题功能演示 |

活动列表在 `event/`，演讲详情在 `talk/`；这是现有静态输出的路由组织方式。两处路径都已经被页面引用。

## 简历里的真实内容

网站 CV 入口指向 [resume.pdf](../uploads/resume.pdf)，另保留 [resume_old.pdf](../uploads/resume_old.pdf)，均为 2 页。以下信息来自简历已有文字，描述历史材料，论文发表状态和项目当前进度需另行核对。

### 论文素材

**GAEI-UNet: Global Attention and Elastic Interaction U-Net for Vessel Image Segmentation**。两份简历均列出这篇 2023 年论文，并在研究经历中写到提交至 arXiv。

两份文件的作者记录不同：`resume.pdf` 列 Xiao, R. 与 Wan, Z.；`resume_old.pdf` 还列 Xiang, Y.。正式建立论文页前，需要以最终论文版本核对作者、标题、链接和状态。

### 项目素材

| 简历中的研究经历 | 已有材料 | 可对应的网站内容 |
| --- | --- | --- |
| Multi-Task, Multi-Prompt Medical Image Inpainting with Transformer-Based Model | 2023-09 起的远程研究经历；多任务、多提示、支持集、上下文学习与图像修复思路 | 多模态医学图像理解或图像修复项目页 |
| Medical Image Segmentation using Active Contour and Deep Learning Methods | 2022-09 至 2023-06；弹性交互、主动轮廓、U 形网络与注意力模块 | GAEI-UNet 论文页及医学图像分割项目页 |
| The Detection of Apparent Cracks in Bridges Using Computer Vision | 2021-08 至 2022-06；YOLOv5、裂缝检测、畸变校正、定量测量；提到 YOLOv5s-GTB 稿件 | 桥梁裂缝检测项目页；稿件状态待核对 |
| Automated Road Information Extraction Based on Laser Scanning Point Cloud | 2020-08 至 2021-08；道路点云数据、线性索引分割、噪声处理 | 点云道路信息提取项目页 |
| Vehicle Dispatching Considering User Preference Based on Reinforcement Learning | 2021-08 至 2022-05；纽约出租车数据、用户偏好、多智能体强化学习和深度 Q 网络 | 强化学习派单项目页 |

### 个人经历素材

简历还包含 HKUST、东南大学、NUS 的教育经历，香港建造业机器人中心实习、荣誉奖项、课程成绩，以及编程和研究技能。这些信息可以用于扩充 Biography 与经历时间线。

需要核对的差异包括：主页仍写在读及 `Present`，简历的硕士教育结束时间写 2023-11；主页的 HKCRC 实习结束时间为 2022-12，简历为 2023-01；两份简历的学位名称分别出现 Data Science 与 Data-driven Modeling。旧简历不宜直接删除，可先明确版本与引用来源。

## 可优先更新的内容

1. 用已有简历素材补完整个人简介，核对身份、学位名称、日期与研究方向。
2. 建立 GAEI-UNet 真实论文页，并从 5 项研究经历中选出要展示的项目。
3. 保留和完善 4 篇已有正文的笔记；为 3 个未完成条目决定补写、隐藏或归档。
4. 决定模板教程和示例页面是否继续用于参考，并统一摘要、作者信息和导航入口。
