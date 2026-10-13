# Ruiqiang Xiao 个人主页

新版主页面向学术同行，展示 HKUST (Guangzhou) 博士二年级身份、导师、JD.com 实习、研究方向、News，以及 9 项带图片和简述的论文。视觉采用暖白、浅沙、石墨与铜色，使用圆润无衬线字体。发布地址：<https://keeplearning-again.github.io/>，GitHub Pages 使用 `master` 分支根目录。

## 查看与维护

| 入口 | 用途 |
| --- | --- |
| [升级说明](docs/HOMEPAGE_UPGRADE.md) | 新版结构、源文件、数据来源、图片与肖像处理、验证记录 |
| [美学评审](docs/AESTHETIC_REVIEW.md) | 独立美学 agent 的最终评审 |
| [桌面预览](docs/previews/homepage-desktop-final.jpg) | 新版首屏 |
| [手机预览](docs/previews/homepage-mobile-final.jpg) | 手机布局 |
| [论文数据](data/publications.json) | 9 项成果的内容、图片、链接与来源 |
| [主页模板](templates/homepage.html) | 个人信息、News、教育和整体结构 |
| [repo-management skill](skills/repo-management/SKILL.md) | 仓库管理参考副本 |

## 构建与预览

在仓库根目录运行：

```sh
python3 scripts/build-homepage.py
python3 -m http.server 8765 --bind 127.0.0.1
```

打开 <http://127.0.0.1:8765/>。修改主页模板或论文数据后，重新运行构建命令；样式和脚本修改后刷新浏览器即可。

新版主页为可直接部署的静态 HTML/CSS/JS，Python 脚本仅使用标准库。Manrope 字体与研究图片本地托管，不依赖页面加载时请求 Google Fonts。`publication/` 列表入口已指向新版 Publications。

## 升级前盘点

以下文档记录本地 `master` 分支提交 `b3fd8a2`（2024-01-09）的升级前快照，保留作为历史依据：

- [内容清单](docs/CONTENT_INVENTORY.md)
- [155 个原有文件及子模块索引](docs/FILE_INVENTORY.md)
- [仓库维护记录](docs/REPO_STATUS.md)

历史博客、示例详情页、RSS 和主题资源保留原路径；它们属于先前 Hugo/Wowchemy 输出。当前新构建流程覆盖主页，不代表已经找回历史 Hugo 工程。
