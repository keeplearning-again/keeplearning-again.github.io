# 仓库现状与维护记录

以下记录为升级前的仓库快照；当前主页实现与验证见 [升级说明](HOMEPAGE_UPGRADE.md)。

盘点日期：2026-10-13。基线：本地 `master` 分支，提交 `b3fd8a2be4acf8151dc7de7c3e4161a8a8a6e2d1`，提交说明为 `20240109 updated CV`，提交日期为 2024-01-09。开始盘点时工作区干净。

仓库已有的静态页面、搜索索引、RSS 和附件组织可以继续沿用。当前最大的维护问题是生成这些页面的源码缺失；内容上的主要缺口是简历里的真实论文和项目尚未进入网站展示。

## 已有的运行和管理方式

| 项目 | 实际情况 |
| --- | --- |
| 版本管理 | 当前本地分支为 `master`；remote 为 `keeplearning-again/keeplearning-again.github.io` |
| 页面生成 | HTML 标明 `Wowchemy 5.7.0 for Hugo`；仓库保存的是 HTML、RSS、索引和处理后的资源 |
| 内容编辑 | `admin/config.yml` 配置了 `git-gateway`、目标分支 `main`，引用 `content/home`、`content/post`、`content/publication` 等目录；这些源码目录不在当前检出中 |
| 子模块 | `.gitmodules` 的 `public` 指向同一个 GitHub 仓库的 `main` 分支；gitlink 为 `c7f5f17a698f0aaf25b7a3dac7a3dfc22f4d0355`；本地目录为空、尚未初始化 |
| 部署配套文件 | 有 `_headers` 和 `_redirects`（Netlify 注释），站点 URL 为 GitHub Pages 域名；当前检出没有 CI 工作流或部署脚本，实际发布设置需另行查看 |
| 文档与约定 | 盘点前没有 README、仓库内 AGENTS、贡献说明或维护任务记录 |

配置文件证明已有配置文本，不能据此确认后台、子模块或部署流程当前可正常运行。`master` 与配置中的 `main` 差异需要在找回源码、确认发布流程时核对。

## 已确认的问题

| 问题 | 文件证据 | 影响 |
| --- | --- | --- |
| 缺少网站源码和构建配置 | 没有 `content/`、`config/`、`layouts/`、`assets/`、`hugo.toml`、`go.mod`；后台配置引用不存在的源码目录 | 无法从当前检出复现 Hugo 构建；直接编辑输出文件可能在未来生成时被覆盖 |
| 真实成果未展示 | `publication/`、`project/` 为示例；两份简历包含真实论文和研究经历 | 访客看到的成果页与实际材料不匹配 |
| 主页简介和博客未完成 | Biography 未完成句子；差分隐私和车道线文章为空；注意力溯源文章只有一句正文 | 主页与文章内容需要补全或调整展示 |
| 论文与项目导航无目标 | 主页导航 `href="/#projects"`；主页只有 5 个区块，没有 `id="projects"` | 导航无法定位到目标区块 |
| NUS 链接被当成本地路径 | `index.html` 中两处 `href="nus.edu.sg"` | 缺少协议，浏览器会将链接解析为站内路径 |
| 社交入口残留模板值 | `https://twitter.com/GeorgeCushen`、`https://www.linkedin.com/` | 个人链接需要核对 |
| 作者与研究方向不一致 | 示例论文页作者和 `cite.bib` 不同；文章页作者介绍仍写 distributed robotics 等方向 | 需要统一作者和简介数据源 |
| 简历与页面、简历版本之间不一致 | [内容清单的简历部分](CONTENT_INVENTORY.md)列出作者、学位名称和日期差异 | 更新时需要核对最终信息，不能直接选取其中一个版本当作现状 |

## 后续任务

这些任务为待办事项，本次完成的是盘点与索引整理。

| 优先级 | 目标 | 交付物与验收条件 | 状态 | 下一步 |
| --- | --- | --- | --- | --- |
| 1 | 找回网站源码并明确发布入口 | 定位原始内容、主题与配置；记录源码分支、输出分支和构建命令；能复现静态输出 | 待处理 | 先检查其他分支、历史与本机备份，并核对 `public` 子模块的用途 |
| 2 | 展示真实个人与研究内容 | 更新 Biography 和时间线；建立真实论文及选定项目页；作者、链接与日期经核对 | 待处理 | 以简历材料为起点，确认最新身份、论文版本和项目状态 |
| 3 | 修复内容入口 | 论文和项目导航有目标；NUS、社交、CV 链接正确 | 待处理 | 源码找回后在源码中修正；如先改静态文件，记录需同步的修改 |
| 4 | 整理示例与未完成内容 | 为每个模板和空条目决定保留、隐藏、归档或补写；列表、搜索、RSS 与实际页面一致 | 待处理 | 按 [内容清单](CONTENT_INVENTORY.md) 逐项处理 |

## 本次整理结果

| 目标 | 交付物 | 验收条件 | 状态 | 证据 |
| --- | --- | --- | --- | --- |
| 梳理全部原有文件 | [文件索引](FILE_INVENTORY.md) | 覆盖 155 个普通文件与 1 个子模块；各路径用途可查 | 已完成 | Git 文件列表、路径与大小核对 |
| 说明已有内容 | [内容清单](CONTENT_INVENTORY.md) | 覆盖主页、10 篇博客、3 个论文页、2 个项目页、演讲、幻灯片和 2 份简历 | 已完成 | HTML、搜索索引和 PDF 文字核对 |
| 引入可参考的管理方法 | [skill 本地副本](../skills/repo-management/SKILL.md) | 保留来源原文，记录版本 | 已完成 | 下方来源信息与 Git blob SHA |

本次新增 README、3 份盘点文档和 1 份 skill 副本，原有页面及附件保持原路径与内容。整理结果保留在本地工作区，尚未提交、推送或发布。

## 验证范围

- 用 `git status`、`git log`、`git ls-files --stage`、`git submodule status` 核对基线、跟踪文件和子模块状态。
- 解析 52 个原有 HTML 文件的 `href`、`src`，校验指向本网站的文件路径。发现缺失目标 `nus.edu.sg`；另核对主页区块，发现 `/#projects` 无目标。此项为静态路径检查，不包含 JavaScript 动态请求或所有页内锚点。
- 核对 `index.json` 的 18 个记录：17 个详情页与 1 个作者记录；所有详情页的本地 HTML 均存在。
- 使用 `pdftotext -layout` 提取两份简历和示例论文 PDF，并使用 `pdfinfo` 核对页数。仅用于确认文字内容，未做 PDF 排版评审。
- 核对新增文档中的本地文件链接、文件索引覆盖范围和 skill 原文 SHA，并确认原有跟踪文件未改动。

本次没有运行 Hugo 构建、浏览器交互测试或部署验证；结果说明本地文件与内容现状。

## Skill 来源

来源：[3D_Segmentation 的 repo-management/SKILL.md](https://github.com/keeplearning-again/3D_Segmentation/blob/main/skills/repo-management/SKILL.md)，分支 `main`，读取日期 2026-10-13，Git blob SHA 为 `24752e15d334186d1d9062c5900876df867c5e4c`。来源目录当时仅包含 `SKILL.md`。

本地保存位置为 `skills/repo-management/SKILL.md`，供本仓库参考与显式调用。它是仓库内副本，不是全局安装；以后需要更新时，应先对比来源内容与版本，再决定是否同步。
