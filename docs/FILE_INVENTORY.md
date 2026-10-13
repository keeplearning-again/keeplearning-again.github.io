# 网站全部文件索引

盘点日期：2026-10-13。基线为 `master` 分支提交 `b3fd8a2`。原仓库包含 **155 个普通文件**，合计 **7,770,779 字节（约 7.41 MiB）**；另有 **1 个 Git 子模块 `public`**。下列索引覆盖基线中的所有文件和子模块，不包含 `.git/` 内部数据。

本次新增的 5 个文件另列在文末，不计入原有 155 个文件。页面内容与完成情况见 [已有内容清单](CONTENT_INVENTORY.md)。

## 目录用途与数量

| 路径 | 普通文件数 | 用途 |
| --- | ---: | --- |
| 根目录 | 10 | 主页、索引、网站元数据、服务配套文件与子模块配置 |
| `admin/` | 2 | 内容管理后台静态入口与配置 |
| `authors/` | 2 | 作者原图与生成后的头像 |
| `categories/` | 3 | 分类总览与分页跳转 |
| `category/` | 6 | Demo、教程分类页、RSS 与分页跳转 |
| `css/` | 4 | 主题、依赖和代码高亮样式 |
| `en/` | 1 | 英文页面的主题脚本 |
| `event/` | 2 | 活动列表与 RSS |
| `js/` | 6 | 网站交互、主题、论文引用、数学和幻灯片脚本 |
| `media/` | 8 | 应用图标与机构标识 |
| `post/` | 37 | 10 个博客详情页、列表、RSS、图片与示例附件 |
| `project/` | 11 | 2 个示例项目、列表、RSS 与图片 |
| `public/` | 0 | Git 子模块，本地未初始化 |
| `publication-type/` | 9 | 论文类型页、RSS 与分页跳转 |
| `publication/` | 17 | 3 个示例论文、列表、RSS、图片、BibTeX 与示例 PDF |
| `publication_types/` | 3 | 论文类型总览与分页跳转 |
| `slides/` | 2 | 幻灯片列表 RSS 与示例演示 |
| `tag/` | 15 | 5 个标签的详情页、RSS 与分页跳转 |
| `tags/` | 3 | 标签总览与分页跳转 |
| `talk/` | 4 | 示例演讲详情与图片 |
| `uploads/` | 2 | 当前 CV 入口对应简历与旧版简历 |
| `webfonts/` | 8 | Font Awesome 字体及兼容字体 |

## 文件类型

| 类型 | 数量 |
| --- | ---: |
| `.bib` | 2 |
| `.css` | 4 |
| `.csv` | 1 |
| `.html` | 52 |
| `.jpg` | 10 |
| `.js` | 7 |
| `.json` | 2 |
| `.pdf` | 3 |
| `.png` | 10 |
| `.svg` | 4 |
| `.ttf` | 4 |
| `.txt` | 1 |
| `.webmanifest` | 1 |
| `.webp` | 26 |
| `.woff2` | 4 |
| `.xml` | 20 |
| `.yml` | 1 |
| 无扩展名 | 3 |

生成后的缩略图和封面图带有 `_hu` 标记，与原图同时保留。分页文件、搜索索引、RSS 和分类页参与网站导航；后续整理页面时，需要在同一次生成或修改中同步这些输出。

## 原有文件逐项索引

文件大小单位为字节。点击路径可查看本地文件。

### 根目录

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [.gitmodules](../.gitmodules) | 125 | public 子模块的来源和分支配置 |
| [404.html](../404.html) | 16079 | 找不到页面时显示的错误页 |
| [_headers](../_headers) | 545 | Netlify 响应头配置 |
| [_redirects](../_redirects) | 106 | Netlify 重定向配套文件，当前为注释 |
| [index.html](../index.html) | 31333 | 个人网站主页 |
| [index.json](../index.json) | 39839 | 全站搜索索引，18 个记录 |
| [index.xml](../index.xml) | 102249 | 全站 RSS |
| [manifest.webmanifest](../manifest.webmanifest) | 588 | Web 应用名称、主题与图标配置 |
| [public](../public) | 子模块 | Git 子模块 gitlink，目录为空，不计入普通文件 |
| [robots.txt](../robots.txt) | 73 | 爬虫入口与站点地图地址 |
| [sitemap.xml](../sitemap.xml) | 6482 | 网站 URL 地图 |

### admin

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [admin/config.yml](../admin/config.yml) | 18534 | 内容管理集合、分支和媒体目录配置 |
| [admin/index.html](../admin/index.html) | 423 | CMS 后台静态页面 |

### authors

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [authors/admin/avatar.jpg](../authors/admin/avatar.jpg) | 620242 | 作者头像原图 |
| [authors/admin/avatar_hu77d434e1653c7c85e21fab9a7004fc26_620242_270x270_fill_q75_lanczos_center.jpg](../authors/admin/avatar_hu77d434e1653c7c85e21fab9a7004fc26_620242_270x270_fill_q75_lanczos_center.jpg) | 6816 | 生成后的头像裁切图 |

### categories

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [categories/index.html](../categories/index.html) | 16220 | 栏目列表或分类总览 |
| [categories/index.xml](../categories/index.xml) | 868 | 所在栏目或分类的 RSS |
| [categories/page/1/index.html](../categories/page/1/index.html) | 382 | 第一页分页跳转 |

### category

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [category/demo/index.html](../category/demo/index.html) | 19806 | 标签、分类或论文类型详情页 |
| [category/demo/index.xml](../category/demo/index.xml) | 21900 | 所在栏目或分类的 RSS |
| [category/demo/page/1/index.html](../category/demo/page/1/index.html) | 391 | 第一页分页跳转 |
| [category/教程/index.html](../category/%E6%95%99%E7%A8%8B/index.html) | 16831 | 标签、分类或论文类型详情页 |
| [category/教程/index.xml](../category/%E6%95%99%E7%A8%8B/index.xml) | 11102 | 所在栏目或分类的 RSS |
| [category/教程/page/1/index.html](../category/%E6%95%99%E7%A8%8B/page/1/index.html) | 433 | 第一页分页跳转 |

### css

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [css/libs/chroma/dracula.min.css](../css/libs/chroma/dracula.min.css) | 2320 | 主题或依赖样式 |
| [css/libs/chroma/github-light.min.css](../css/libs/chroma/github-light.min.css) | 2599 | 主题或依赖样式 |
| [css/vendor-bundle.min.047268c6dd09ad74ba54a0ba71837064.css](../css/vendor-bundle.min.047268c6dd09ad74ba54a0ba71837064.css) | 101931 | 主题或依赖样式 |
| [css/wowchemy.042e26407c9e383d96a1f26d6787c686.css](../css/wowchemy.042e26407c9e383d96a1f26d6787c686.css) | 181758 | 主题或依赖样式 |

### en

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [en/js/wowchemy.min.3322c0d94f0e691b0b24c63f4c41064b.js](../en/js/wowchemy.min.3322c0d94f0e691b0b24c63f4c41064b.js) | 23294 | 主题或功能脚本 |

### event

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [event/index.html](../event/index.html) | 17047 | 栏目列表或分类总览 |
| [event/index.xml](../event/index.xml) | 2582 | 所在栏目或分类的 RSS |

### js

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [js/mathjax-config.js](../js/mathjax-config.js) | 653 | 主题或功能脚本 |
| [js/vendor-bundle.min.f64289d8217e08e3afcd597d60836062.js](../js/vendor-bundle.min.f64289d8217e08e3afcd597d60836062.js) | 175637 | 主题或功能脚本 |
| [js/wowchemy-headroom.db4755770454eb63685f8de785c0a172.js](../js/wowchemy-headroom.db4755770454eb63685f8de785c0a172.js) | 5365 | 主题或功能脚本 |
| [js/wowchemy-init.min.ec9d49ca50e4b80bdb08f0417a28ed84.js](../js/wowchemy-init.min.ec9d49ca50e4b80bdb08f0417a28ed84.js) | 1560 | 主题或功能脚本 |
| [js/wowchemy-publication.68f8d7090562ca65fc6d3cb3f8f2d2cb.js](../js/wowchemy-publication.68f8d7090562ca65fc6d3cb3f8f2d2cb.js) | 1614 | 主题或功能脚本 |
| [js/wowchemy-slides.js](../js/wowchemy-slides.js) | 2427 | 主题或功能脚本 |

### media

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [media/icon_hud72a807ca50d008ad851764b48a793ed_213136_180x180_fill_lanczos_center_3.png](../media/icon_hud72a807ca50d008ad851764b48a793ed_213136_180x180_fill_lanczos_center_3.png) | 49482 | 生成后的应用图标 |
| [media/icon_hud72a807ca50d008ad851764b48a793ed_213136_192x192_fill_lanczos_center_3.png](../media/icon_hud72a807ca50d008ad851764b48a793ed_213136_192x192_fill_lanczos_center_3.png) | 55044 | 生成后的应用图标 |
| [media/icon_hud72a807ca50d008ad851764b48a793ed_213136_32x32_fill_lanczos_center_3.png](../media/icon_hud72a807ca50d008ad851764b48a793ed_213136_32x32_fill_lanczos_center_3.png) | 2610 | 生成后的应用图标 |
| [media/icon_hud72a807ca50d008ad851764b48a793ed_213136_512x512_fill_lanczos_center_3.png](../media/icon_hud72a807ca50d008ad851764b48a793ed_213136_512x512_fill_lanczos_center_3.png) | 267308 | 生成后的应用图标 |
| [media/icons/brands/HKUST.svg](../media/icons/brands/HKUST.svg) | 88330 | 学校或机构 SVG 标识 |
| [media/icons/brands/SEU.svg](../media/icons/brands/SEU.svg) | 51760 | 学校或机构 SVG 标识 |
| [media/icons/brands/hkcrc.svg](../media/icons/brands/hkcrc.svg) | 57181 | 学校或机构 SVG 标识 |
| [media/icons/brands/nus.svg](../media/icons/brands/nus.svg) | 28155 | 学校或机构 SVG 标识 |

### post

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [post/20230326_differencial_privacy/index.html](../post/20230326_differencial_privacy/index.html) | 22202 | 博客详情页，状态见内容清单 |
| [post/attention机制溯源/index.html](../post/attention%E6%9C%BA%E5%88%B6%E6%BA%AF%E6%BA%90/index.html) | 24786 | 博客详情页，状态见内容清单 |
| [post/chatgpt总结/featured.png](../post/chatgpt%E6%80%BB%E7%BB%93/featured.png) | 275271 | 页面封面原图 |
| [post/chatgpt总结/featured_hu0e9d00357b0799bed7e004e3dde62db9_275271_1200x2500_fit_q75_h2_lanczos_3.webp](../post/chatgpt%E6%80%BB%E7%BB%93/featured_hu0e9d00357b0799bed7e004e3dde62db9_275271_1200x2500_fit_q75_h2_lanczos_3.webp) | 38934 | 生成后的详情封面图 |
| [post/chatgpt总结/featured_hu0e9d00357b0799bed7e004e3dde62db9_275271_150x0_resize_q75_h2_lanczos_3.webp](../post/chatgpt%E6%80%BB%E7%BB%93/featured_hu0e9d00357b0799bed7e004e3dde62db9_275271_150x0_resize_q75_h2_lanczos_3.webp) | 1602 | 生成后的封面缩略图 |
| [post/chatgpt总结/index.html](../post/chatgpt%E6%80%BB%E7%BB%93/index.html) | 27501 | 博客详情页，状态见内容清单 |
| [post/getting-started/featured.jpg](../post/getting-started/featured.jpg) | 241861 | 页面封面原图 |
| [post/getting-started/featured_hub9ee31969f44a6711206a2baf9f065b4_241861_1200x2500_fit_q75_h2_lanczos.webp](../post/getting-started/featured_hub9ee31969f44a6711206a2baf9f065b4_241861_1200x2500_fit_q75_h2_lanczos.webp) | 50320 | 生成后的详情封面图 |
| [post/getting-started/featured_hub9ee31969f44a6711206a2baf9f065b4_241861_150x0_resize_q75_h2_lanczos.webp](../post/getting-started/featured_hub9ee31969f44a6711206a2baf9f065b4_241861_150x0_resize_q75_h2_lanczos.webp) | 2736 | 生成后的封面缩略图 |
| [post/getting-started/index.html](../post/getting-started/index.html) | 30130 | 博客详情页，状态见内容清单 |
| [post/index.html](../post/index.html) | 28755 | 栏目列表或分类总览 |
| [post/index.xml](../post/index.xml) | 83021 | 所在栏目或分类的 RSS |
| [post/jupyter/featured.png](../post/jupyter/featured.png) | 71549 | 页面封面原图 |
| [post/jupyter/featured_hub1daa031c2af6888ff37bd93eb033a1a_71549_150x0_resize_q75_h2_lanczos_3.webp](../post/jupyter/featured_hub1daa031c2af6888ff37bd93eb033a1a_71549_150x0_resize_q75_h2_lanczos_3.webp) | 1114 | 生成后的封面缩略图 |
| [post/jupyter/featured_hub1daa031c2af6888ff37bd93eb033a1a_71549_720x2500_fit_q75_h2_lanczos_3.webp](../post/jupyter/featured_hub1daa031c2af6888ff37bd93eb033a1a_71549_720x2500_fit_q75_h2_lanczos_3.webp) | 11008 | 生成后的详情封面图 |
| [post/jupyter/index.html](../post/jupyter/index.html) | 26030 | 博客详情页，状态见内容清单 |
| [post/jupyter/index_1_0.png](../post/jupyter/index_1_0.png) | 11155 | Jupyter 模板示例的输出图片 |
| [post/markdown+typora/featured.png](../post/markdown%2Btypora/featured.png) | 33304 | 页面封面原图 |
| [post/markdown+typora/featured_hued96563dbbad43bb3972c6c520bd98ca_33304_1200x2500_fit_q75_h2_lanczos_3.webp](../post/markdown%2Btypora/featured_hued96563dbbad43bb3972c6c520bd98ca_33304_1200x2500_fit_q75_h2_lanczos_3.webp) | 11208 | 生成后的详情封面图 |
| [post/markdown+typora/featured_hued96563dbbad43bb3972c6c520bd98ca_33304_150x0_resize_q75_h2_lanczos_3.webp](../post/markdown%2Btypora/featured_hued96563dbbad43bb3972c6c520bd98ca_33304_150x0_resize_q75_h2_lanczos_3.webp) | 1410 | 生成后的封面缩略图 |
| [post/markdown+typora/index.html](../post/markdown%2Btypora/index.html) | 25458 | 博客详情页，状态见内容清单 |
| [post/page/1/index.html](../post/page/1/index.html) | 364 | 第一页分页跳转 |
| [post/transformer/featured.png](../post/transformer/featured.png) | 172075 | 页面封面原图 |
| [post/transformer/featured_hu55e335c73174c518587033d1e6843012_172075_1200x2500_fit_q75_h2_lanczos_3.webp](../post/transformer/featured_hu55e335c73174c518587033d1e6843012_172075_1200x2500_fit_q75_h2_lanczos_3.webp) | 24176 | 生成后的详情封面图 |
| [post/transformer/featured_hu55e335c73174c518587033d1e6843012_172075_150x0_resize_q75_h2_lanczos_3.webp](../post/transformer/featured_hu55e335c73174c518587033d1e6843012_172075_150x0_resize_q75_h2_lanczos_3.webp) | 2726 | 生成后的封面缩略图 |
| [post/transformer/index.html](../post/transformer/index.html) | 36108 | 博客详情页，状态见内容清单 |
| [post/writing-technical-content/featured.jpg](../post/writing-technical-content/featured.jpg) | 266353 | 页面封面原图 |
| [post/writing-technical-content/featured_huc72159e0fc0d14b85f60d34436a630f0_266353_1200x2500_fit_q75_h2_lanczos.webp](../post/writing-technical-content/featured_huc72159e0fc0d14b85f60d34436a630f0_266353_1200x2500_fit_q75_h2_lanczos.webp) | 114044 | 生成后的详情封面图 |
| [post/writing-technical-content/featured_huc72159e0fc0d14b85f60d34436a630f0_266353_150x0_resize_q75_h2_lanczos.webp](../post/writing-technical-content/featured_huc72159e0fc0d14b85f60d34436a630f0_266353_150x0_resize_q75_h2_lanczos.webp) | 7422 | 生成后的封面缩略图 |
| [post/writing-technical-content/index.html](../post/writing-technical-content/index.html) | 42273 | 博客详情页，状态见内容清单 |
| [post/writing-technical-content/line-chart.json](../post/writing-technical-content/line-chart.json) | 1569 | 模板图表演示配置 |
| [post/writing-technical-content/results.csv](../post/writing-technical-content/results.csv) | 33 | 模板图表演示数据 |
| [post/计算机视觉任务/featured.png](../post/%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89%E4%BB%BB%E5%8A%A1/featured.png) | 272624 | 页面封面原图 |
| [post/计算机视觉任务/featured_hu96baab7cf28786bfd50ebeaa04cbc0eb_272624_1200x2500_fit_q75_h2_lanczos_3.webp](../post/%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89%E4%BB%BB%E5%8A%A1/featured_hu96baab7cf28786bfd50ebeaa04cbc0eb_272624_1200x2500_fit_q75_h2_lanczos_3.webp) | 29920 | 生成后的详情封面图 |
| [post/计算机视觉任务/featured_hu96baab7cf28786bfd50ebeaa04cbc0eb_272624_150x0_resize_q75_h2_lanczos_3.webp](../post/%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89%E4%BB%BB%E5%8A%A1/featured_hu96baab7cf28786bfd50ebeaa04cbc0eb_272624_150x0_resize_q75_h2_lanczos_3.webp) | 2578 | 生成后的封面缩略图 |
| [post/计算机视觉任务/index.html](../post/%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89%E4%BB%BB%E5%8A%A1/index.html) | 25898 | 博客详情页，状态见内容清单 |
| [post/车道线论文大合集/index.html](../post/%E8%BD%A6%E9%81%93%E7%BA%BF%E8%AE%BA%E6%96%87%E5%A4%A7%E5%90%88%E9%9B%86/index.html) | 20918 | 博客详情页，状态见内容清单 |

### project

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [project/example/featured.jpg](../project/example/featured.jpg) | 224363 | 页面封面原图 |
| [project/example/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_224363_150x0_resize_q75_h2_lanczos.webp](../project/example/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_224363_150x0_resize_q75_h2_lanczos.webp) | 2152 | 生成后的封面缩略图 |
| [project/example/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_224363_720x2500_fit_q75_h2_lanczos.webp](../project/example/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_224363_720x2500_fit_q75_h2_lanczos.webp) | 17126 | 生成后的详情封面图 |
| [project/example/index.html](../project/example/index.html) | 28980 | 模板项目详情页 |
| [project/external-project/featured.jpg](../project/external-project/featured.jpg) | 329522 | 页面封面原图 |
| [project/external-project/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_329522_150x0_resize_q75_h2_lanczos.webp](../project/external-project/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_329522_150x0_resize_q75_h2_lanczos.webp) | 1592 | 生成后的封面缩略图 |
| [project/external-project/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_329522_720x2500_fit_q75_h2_lanczos.webp](../project/external-project/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_329522_720x2500_fit_q75_h2_lanczos.webp) | 10922 | 生成后的详情封面图 |
| [project/external-project/index.html](../project/external-project/index.html) | 21531 | 模板项目详情页 |
| [project/index.html](../project/index.html) | 17306 | 栏目列表或分类总览 |
| [project/index.xml](../project/index.xml) | 4717 | 所在栏目或分类的 RSS |
| [project/page/1/index.html](../project/page/1/index.html) | 373 | 第一页分页跳转 |

### publication-type

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [publication-type/1/index.html](../publication-type/1/index.html) | 17771 | 标签、分类或论文类型详情页 |
| [publication-type/1/index.xml](../publication-type/1/index.xml) | 1875 | 所在栏目或分类的 RSS |
| [publication-type/1/page/1/index.html](../publication-type/1/page/1/index.html) | 406 | 第一页分页跳转 |
| [publication-type/2/index.html](../publication-type/2/index.html) | 17137 | 标签、分类或论文类型详情页 |
| [publication-type/2/index.xml](../publication-type/2/index.xml) | 1872 | 所在栏目或分类的 RSS |
| [publication-type/2/page/1/index.html](../publication-type/2/page/1/index.html) | 406 | 第一页分页跳转 |
| [publication-type/3/index.html](../publication-type/3/index.html) | 17458 | 标签、分类或论文类型详情页 |
| [publication-type/3/index.xml](../publication-type/3/index.xml) | 1615 | 所在栏目或分类的 RSS |
| [publication-type/3/page/1/index.html](../publication-type/3/page/1/index.html) | 406 | 第一页分页跳转 |

### publication

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [publication/conference-paper/cite.bib](../publication/conference-paper/cite.bib) | 205 | 示例会议论文 BibTeX |
| [publication/conference-paper/conference-paper.pdf](../publication/conference-paper/conference-paper.pdf) | 15043 | 1 页占位示例 PDF |
| [publication/conference-paper/featured.jpg](../publication/conference-paper/featured.jpg) | 312700 | 页面封面原图 |
| [publication/conference-paper/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_312700_150x0_resize_q75_h2_lanczos.webp](../publication/conference-paper/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_312700_150x0_resize_q75_h2_lanczos.webp) | 2426 | 生成后的封面缩略图 |
| [publication/conference-paper/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_312700_720x2500_fit_q75_h2_lanczos.webp](../publication/conference-paper/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_312700_720x2500_fit_q75_h2_lanczos.webp) | 20356 | 生成后的详情封面图 |
| [publication/conference-paper/index.html](../publication/conference-paper/index.html) | 25186 | 模板论文详情页 |
| [publication/index.html](../publication/index.html) | 22414 | 栏目列表或分类总览 |
| [publication/index.xml](../publication/index.xml) | 3644 | 所在栏目或分类的 RSS |
| [publication/journal-article/cite.bib](../publication/journal-article/cite.bib) | 194 | 示例期刊论文 BibTeX |
| [publication/journal-article/featured.jpg](../publication/journal-article/featured.jpg) | 214168 | 页面封面原图 |
| [publication/journal-article/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_214168_150x0_resize_q75_h2_lanczos.webp](../publication/journal-article/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_214168_150x0_resize_q75_h2_lanczos.webp) | 2184 | 生成后的封面缩略图 |
| [publication/journal-article/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_214168_720x2500_fit_q75_h2_lanczos.webp](../publication/journal-article/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_214168_720x2500_fit_q75_h2_lanczos.webp) | 13068 | 生成后的详情封面图 |
| [publication/journal-article/index.html](../publication/journal-article/index.html) | 24692 | 模板论文详情页 |
| [publication/preprint/featured.jpg](../publication/preprint/featured.jpg) | 220813 | 页面封面原图 |
| [publication/preprint/featured_hu559a5add5185b02575aa8333502ab2cc_220813_150x0_resize_q75_h2_lanczos.webp](../publication/preprint/featured_hu559a5add5185b02575aa8333502ab2cc_220813_150x0_resize_q75_h2_lanczos.webp) | 2454 | 生成后的封面缩略图 |
| [publication/preprint/featured_hu559a5add5185b02575aa8333502ab2cc_220813_720x2500_fit_q75_h2_lanczos.webp](../publication/preprint/featured_hu559a5add5185b02575aa8333502ab2cc_220813_720x2500_fit_q75_h2_lanczos.webp) | 19560 | 生成后的详情封面图 |
| [publication/preprint/index.html](../publication/preprint/index.html) | 24415 | 模板论文详情页 |

### publication_types

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [publication_types/index.html](../publication_types/index.html) | 16789 | 栏目列表或分类总览 |
| [publication_types/index.xml](../publication_types/index.xml) | 910 | 所在栏目或分类的 RSS |
| [publication_types/page/1/index.html](../publication_types/page/1/index.html) | 403 | 第一页分页跳转 |

### slides

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [slides/example/index.html](../slides/example/index.html) | 9969 | 模板幻灯片页面 |
| [slides/index.xml](../slides/index.xml) | 11174 | 所在栏目或分类的 RSS |

### tag

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [tag/academic/index.html](../tag/academic/index.html) | 25260 | 标签、分类或论文类型详情页 |
| [tag/academic/index.xml](../tag/academic/index.xml) | 48046 | 所在栏目或分类的 RSS |
| [tag/academic/page/1/index.html](../tag/academic/page/1/index.html) | 388 | 第一页分页跳转 |
| [tag/deep-learning/index.html](../tag/deep-learning/index.html) | 16399 | 标签、分类或论文类型详情页 |
| [tag/deep-learning/index.xml](../tag/deep-learning/index.xml) | 4441 | 所在栏目或分类的 RSS |
| [tag/deep-learning/page/1/index.html](../tag/deep-learning/page/1/index.html) | 403 | 第一页分页跳转 |
| [tag/demo/index.html](../tag/demo/index.html) | 16074 | 标签、分类或论文类型详情页 |
| [tag/demo/index.xml](../tag/demo/index.xml) | 1165 | 所在栏目或分类的 RSS |
| [tag/demo/page/1/index.html](../tag/demo/page/1/index.html) | 376 | 第一页分页跳转 |
| [tag/source-themes/index.html](../tag/source-themes/index.html) | 19484 | 标签、分类或论文类型详情页 |
| [tag/source-themes/index.xml](../tag/source-themes/index.xml) | 2655 | 所在栏目或分类的 RSS |
| [tag/source-themes/page/1/index.html](../tag/source-themes/page/1/index.html) | 403 | 第一页分页跳转 |
| [tag/开源/index.html](../tag/%E5%BC%80%E6%BA%90/index.html) | 16811 | 标签、分类或论文类型详情页 |
| [tag/开源/index.xml](../tag/%E5%BC%80%E6%BA%90/index.xml) | 11087 | 所在栏目或分类的 RSS |
| [tag/开源/page/1/index.html](../tag/%E5%BC%80%E6%BA%90/page/1/index.html) | 418 | 第一页分页跳转 |

### tags

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [tags/index.html](../tags/index.html) | 17795 | 栏目列表或分类总览 |
| [tags/index.xml](../tags/index.xml) | 832 | 所在栏目或分类的 RSS |
| [tags/page/1/index.html](../tags/page/1/index.html) | 364 | 第一页分页跳转 |

### talk

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [talk/example-talk/featured.jpg](../talk/example-talk/featured.jpg) | 620088 | 页面封面原图 |
| [talk/example-talk/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_620088_150x0_resize_q75_h2_lanczos.webp](../talk/example-talk/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_620088_150x0_resize_q75_h2_lanczos.webp) | 2628 | 生成后的封面缩略图 |
| [talk/example-talk/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_620088_720x2500_fit_q75_h2_lanczos.webp](../talk/example-talk/featured_hu3d03a01dcc18bc5be0e67db3d8d209a6_620088_720x2500_fit_q75_h2_lanczos.webp) | 32614 | 生成后的详情封面图 |
| [talk/example-talk/index.html](../talk/example-talk/index.html) | 24229 | 模板演讲详情页 |

### uploads

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [uploads/resume.pdf](../uploads/resume.pdf) | 98195 | 网站 CV 入口，2 页简历 |
| [uploads/resume_old.pdf](../uploads/resume_old.pdf) | 98251 | 保留的旧版简历，2 页 |

### webfonts

| 文件 | 大小 | 用途 |
| --- | ---: | --- |
| [webfonts/fa-brands-400.ttf](../webfonts/fa-brands-400.ttf) | 187208 | Font Awesome 图标字体 |
| [webfonts/fa-brands-400.woff2](../webfonts/fa-brands-400.woff2) | 108020 | Font Awesome 图标字体 |
| [webfonts/fa-regular-400.ttf](../webfonts/fa-regular-400.ttf) | 63952 | Font Awesome 图标字体 |
| [webfonts/fa-regular-400.woff2](../webfonts/fa-regular-400.woff2) | 24948 | Font Awesome 图标字体 |
| [webfonts/fa-solid-900.ttf](../webfonts/fa-solid-900.ttf) | 394628 | Font Awesome 图标字体 |
| [webfonts/fa-solid-900.woff2](../webfonts/fa-solid-900.woff2) | 150124 | Font Awesome 图标字体 |
| [webfonts/fa-v4compatibility.ttf](../webfonts/fa-v4compatibility.ttf) | 10172 | Font Awesome 图标字体 |
| [webfonts/fa-v4compatibility.woff2](../webfonts/fa-v4compatibility.woff2) | 4564 | Font Awesome 图标字体 |

## 本次新增文件

| 文件 | 用途 |
| --- | --- |
| [README.md](../README.md) | 仓库入口、内容概览、目录用途与预览命令 |
| [docs/CONTENT_INVENTORY.md](CONTENT_INVENTORY.md) | 全部页面及简历内容清单 |
| [docs/FILE_INVENTORY.md](FILE_INVENTORY.md) | 本文件，原有文件的完整索引 |
| [docs/REPO_STATUS.md](REPO_STATUS.md) | 当前维护方式、问题、后续任务与验证范围 |
| [skills/repo-management/SKILL.md](../skills/repo-management/SKILL.md) | 从指定仓库保存的 skill 原文参考副本 |
