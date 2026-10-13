# 个人主页升级说明

更新日期：2026-10-13。此版用于发布到 <https://keeplearning-again.github.io/>，GitHub Pages 使用 `master` 分支根目录。

## 当前展示

- 姓名：Ruiqiang Xiao（肖睿强）；保留 John 作为页面元数据中的别名，移除 `John.` 视觉标识。
- 身份：HKUST (Guangzhou) 博士二年级；导师为 Prof. Lei Zhu 与 Prof. Kaishun Wu；目前在 JD.com 实习。
- 研究方向：medical image analysis、video understanding、multimodal large models。
- 全英文内容，中文姓名按用户要求保留。
- 两项重点研究：EchoPilot 与 npj Digital Medicine 的实时手术解剖识别论文。
- News：基于已核实的论文发表、公开预印本与奖项记录整理。
- Publications：9 项成果，按年份与可确认的发表时间倒序；每项均有原始研究图、基本描述、作者和可用链接。点击缩略图可查看完整研究图。
- 主题筛选、年份分组、教育与实习经历，以及联系方式。

## 视觉方向

明亮、克制的电影感，以暖白、浅沙、石墨和铜色为基础。通过姓名的字重和尺度、真实肖像、研究图体量、非对称分栏与对齐建立视觉节奏。字体使用本地托管的 Manrope 无衬线字体；中文姓名使用系统中文无衬线字体。页面没有斜体或大型衬线标题。

首版经过美学 agent 独立评审，评分 72/100；第二版首屏评分 82/100。后续据此放大肖像、精简重复简介、提前展示研究图并扩大论文文字与缩略图。最终评审见 [美学评审记录](AESTHETIC_REVIEW.md)，分数属于该评审 agent 的设计判断。

## 可维护的源文件

| 文件 | 修改内容 |
| --- | --- |
| [templates/homepage.html](../templates/homepage.html) | 身份、导师、研究方向、News、教育经历、精选研究与页面结构 |
| [data/publications.json](../data/publications.json) | 论文题目、作者、年份、时间、venue、简述、图片、链接、来源与筛选主题 |
| [assets/homepage/homepage.css](../assets/homepage/homepage.css) | 字体、颜色、尺寸、间距与响应式布局 |
| [assets/homepage/homepage.js](../assets/homepage/homepage.js) | 论文主题筛选、计数与空年份隐藏 |
| [scripts/build-homepage.py](../scripts/build-homepage.py) | 使用标准库将模板与论文数据生成为根目录主页 |
| [index.html](../index.html) | 可直接部署的静态主页，由构建脚本生成 |
| [publication/index.html](../publication/index.html) | 原论文列表入口跳转到新版主页的 Publications 区域 |

修改源文件后，在仓库根目录运行：

```sh
python3 scripts/build-homepage.py
python3 -m http.server 8765 --bind 127.0.0.1
```

然后访问 <http://127.0.0.1:8765/>。无需安装 npm 依赖或使用 Hugo。此流程覆盖新版主页；历史博客、示例详情页和 RSS 仍是原有 Hugo 输出。

JavaScript 不可用时，9 项论文仍直接存在于 HTML 中；筛选控件会隐藏。页面包含可通过键盘聚焦的跳过导航入口、图片说明、可访问按钮状态与减少动画的样式。

## 论文核对

Google Scholar 中当时可见 8 项记录，另补用户指定的 npj 文章。作者顺序优先采用论文或会议的公开版本；未从姓氏、排序或主页内容推断共同一作标记。

| 成果 | 年份与来源 |
| --- | --- |
| EchoPilot | MICCAI 2026，[会议页面](https://papers.miccai.org/miccai-2026/0332-Paper1265.html)、[项目主页](https://keeplearning-again.github.io/EchoPilot/) |
| DSTD | MICCAI 2026，[会议页面](https://papers.miccai.org/miccai-2026/0288-Paper1074.html) |
| Real-time anatomy recognition in laparoscopic liver resection using video segmentation AI model | npj Digital Medicine，2026-07-10；[论文](https://www.nature.com/articles/s41746-026-02989-5)、[PubMed](https://pubmed.ncbi.nlm.nih.gov/42432115/)、[Crossref 元数据](https://api.crossref.org/works/10.1038/s41746-026-02989-5) |
| Cardio-mmFlow | ICML 2026，[PMLR](https://proceedings.mlr.press/v306/liu26ey.html) |
| HyperCBM | 2026-06-01 公开预印本，[arXiv](https://arxiv.org/abs/2606.01698) |
| OsmT | Scholar 记录的 venue 为 ICDE 2026；[arXiv](https://arxiv.org/abs/2512.04738) 预印本提交于 2025-12-04 |
| HRVVS | MICCAI 2025，[arXiv](https://arxiv.org/abs/2507.22530)、[会议程序](https://conferences.miccai.org/2025/files/downloads/MICCAI2025-Program-Book.pdf) |
| MatchSeg | IEEE BIBM 2024，[arXiv](https://arxiv.org/abs/2403.15901)；作者顺序按当前公开版本，Jiayu Huo 在 Ruiqiang Xiao 前 |
| IRFusionFormer | BMVC 2024 DIFA Workshop，[会议页面](https://bmvc2024.org/proceedings/workshop-proceedings/)、[arXiv](https://arxiv.org/abs/2409.20474)；Best Paper Award 来自 arXiv 备注及 Scholar 记录 |

排序以正式展示 venue 的年份为准，再使用已知日期。仅确认年份的 OsmT 没有补造月份或日，排在当年有明确日期的条目之后。HyperCBM 明确显示为 Preprint。会议类条目采用会议月份；同月且无具体日的论文保留稳定顺序。

## 图片与字体来源

全部论文图片均从项目主页、arXiv HTML 或正式论文 PDF 获取；没有生成、重绘或改写科学图中的实验结果。完整图片来源逐项记录在 `data/publications.json` 的 `image_source` 字段。

- EchoPilot：项目主页的 `assets/teaser.png`。
- npj：论文 PDF 第 37 页嵌入的模型图，直接提取 JPEG。论文按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 开放；来源为 Tao et al., 2026, DOI `10.1038/s41746-026-02989-5`。
- DSTD：会议 PDF 第 3 页模型图，通过 Poppler 渲染并截取图区域。
- Cardio-mmFlow：PMLR PDF 第 4 页模型图，通过 Poppler 渲染并截取图区域。
- 其他论文：arXiv HTML 公开的模型图原文件。
- Manrope：Google Fonts 提供的字体文件；[OFL 许可](../assets/homepage/fonts/OFL.txt) 保存在字体目录。

## 肖像高清化

原始肖像来自用户指定的 [Google Scholar](https://scholar.google.com/citations?user=C8e74qIAAAAJ&hl=en)，下载时尺寸为 128×128。原图保存在 [profile-scholar.jpg](../assets/homepage/images/profile-scholar.jpg)。

按用户要求，使用内置 imagegen 对原图进行保守的 AI 高清化，得到 1254×1254 的 [profile-scholar-hd.png](../assets/homepage/images/profile-scholar-hd.png)，并用于主页。处理保留黑白色调、背景和构图；新增高频细节属于模型重建，并非从低分辨率图中无损恢复。

完整提示词：

> Use case: identity-preserve. Edit target: the attached 128x128 Google Scholar portrait of Ruiqiang Xiao. Primary request: conservative photographic super-resolution and deblurring for a personal academic website, producing a sharp 1024x1024 square version. Restore clarity and reduce compression/blurring only. Preserve the EXACT person's identity, facial geometry, expression, slightly angled head, eye shape, nose, mouth, jaw, hairstyle and hairline, existing clothing, monochrome warm-gray photographic palette, soft lighting, background, crop and camera angle. Faithfully reconstruct details only where supported by the input; prefer restraint over inventing texture. Keep the original grayscale tonality and natural skin. Do not beautify, reshape, age, stylize, colorize, change pose, add accessories, replace background, change framing, add text or watermark. This is an upscale of the original portrait, not a newly designed portrait.

## 验证与预览

- Python 构建成功，9 条论文均在静态 HTML 中。
- 本地文件链接、页内导航、图片路径、图片说明和唯一 ID 检查通过。
- JavaScript 语法检查通过；实际浏览器验证主题筛选结果为 Medical imaging 6、Video 4、Multimodal AI 4、Language models 1、All work 9。
- 320、390、768、1470 px 四档宽度无水平溢出；修复平板精选研究图的宽度约束。9 张论文图路径有效；浏览器已确认论文缩略图加载及 News 历史条目展开。
- 最终预览：[桌面首屏](previews/homepage-desktop-final.jpg)、[手机首屏](previews/homepage-mobile-final.jpg)、[桌面论文区](previews/homepage-desktop-publications-final.jpg)、[手机论文区](previews/homepage-mobile-publications-final.jpg)。

教育经历起止年月、JD 实习部门和新版 CV 尚未提供，页面使用已确认的学位与当前身份，不添加推测日期或职位。
