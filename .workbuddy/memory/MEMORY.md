# 工作记忆

## 项目

### GStarCAD 3D查看器 (0313项目)
- 路径: `C:/Users/willp/Desktop/project/0313/`
- 技术栈: 浩辰CAD Web Viewer (hoops-web-viewer-monolith.umd.js + WebCAD.js)
- 后端服务: `http://127.0.0.1:8081` (需要运行才能转换文件)
- 本地服务器: `python -m http.server 8080` (需要启动才能访问页面)
- 新标签打开逻辑: URL参数 `?openNewTab=true` 触发文件选择
- Recent Drawings: localStorage Base64缓存 + 24小时过期 (ID: 29642493)

### 拉玛那马哈希知识库项目
- **当前路径（已迁移）**: `c:/Users/willp/Desktop/2026年4月/kb01/`
- 旧路径（已废弃）: `c:/Users/willp/WorkBuddy/20260410104230/`
- Skill: `~/.workbuddy/skills/拉玛那知识库/SKILL.md`
- 架构: 三层节点（概念/书籍/人物）+ 可点击跳转
- 已整合书籍（18本）：
  1. 📖 走向静默，如你本来 (Be As You Are)
  2. 📕 回到你心中
  3. 📗 以言传意 (Teachings in His Own Words)
  4. 💎 宝钻集 (Gems from Bhagavan)
  5. 💬 对谈录 (Talks with Sri Ramana Maharshi)
  6. 📅 日日与彼 (Day by Day with Bhagavan)
  7. 👁️ 面对面 (Face to Face)
  8. 🔍 秘密印度 (A Search in Secret India)
  9. 📖 圣者（毛姆）- 亲历记录
  10. 📜 马哈希福音 (Maharshi's Gospel)
  11. 🧘 大瑜伽 (Maha Yoga)
  12. 📿 上师言颂 (Guru Vachaka Kovai)
  13. ⏳ 时代中的永恒 (Timeless in Time)
  14. 💭 反思录 (Reflections)
  15. 📖 灵性故事 (Spiritual Stories)
  16. 💝 超越爱与恩典 (Surpassing Love and Grace)
  17. 🍞 桌边碎语 (Crumbs from the Table)
  18. 📚 全集 (Collected Works)

### 知识图谱项目
- 知识图谱已整合到主知识库中（拉玛那马哈希知识库.html）
- 使用点击节点弹出详情框的方式展示概念关系
- 图谱包含：本体（真我、本心、心智、自我）、修行法门、世界本质、书籍等节点
- 已删除独立知识图谱文件（整合到主知识库）

### 知识库改进（20260410 - 大幅增强）
- 主文件: `拉玛那马哈希知识库.html`（约160KB）
- 修复HTML结构错误（删除游离的重复标签）
- 新增功能：
  - 章节详情弹窗：点击章节可查看概要
  - 知识图谱视图：整合的概念关系图
  - 主页标记：右上角显示"📖 主页"
  - 左侧导航栏增强：分类显示19本书，添加数量标注
- 已删除多余文件：`拉玛那知识库.html`、`拉玛那马哈希知识图谱.html`、`合规知识图谱.html`
- 章节详情弹窗函数: `showChapterDetail(chapterId, bookTitle, chapterTitle, content)`

### 知识库增强（20260410下午 - 第二次大规模增强）
- 主文件: `拉玛那马哈希知识库.html`（约200KB+）
- 首页大幅重构（参考巴菲特知识库）：
  - 添加统计信息卡片：18本著作、30+概念、100+精选问答、3位人物
  - 添加五大入口卡片：书籍总览、核心思想、修行方法、人物索引、知识图谱
  - 添加核心概念TOP 15标签云
  - 添加TOP书籍推荐卡片
  - 添加关键人物展示卡片
  - 添加经典引言展示区
- 左侧导航栏重构：
  - 添加搜索框（filterSidebar函数）
  - 折叠式分类导航（toggleSection函数）
  - 索引分类：书籍总览、核心思想、修行方法、精选问答、语录、人物索引、知识图谱
  - 18本书分为6个分类：经典著作(4)、对话与日记(3)、朝圣记录(2)、哲学专著(3)、参考著作(6)
  - 修行与生活分类：生平、静修院、阿鲁那佳拉
- 核心概念扩展至30+个：
  - 本体论(5)：真我、梵、本心、存在-意识-喜悦、摩耶
  - 心智与自我(6)：心智、自我、念头、习气、觉知、醒时如梦
  - 修行法门(10)：参究法、"我是谁？"、归伏、臣服、念诵、三摩地、禅定、修行、努力、出离
  - 上师与恩典(3)：上师、恩典、静默
  - 业力与轮回(5)：业力、轮回、命运、自由意志、世界
  - 解脱与境界(8)：解脱、觉者、在家解脱、证悟、开悟、无住、安住、安宁
- 新增页面：
  - 书籍总览页(page-books)：展示所有18本书的分类和简介
  - 修行方法索引页(page-methods)：展示各种修行方法
  - 人物索引页(page-persons)：展示关键人物传记
- 顶部导航栏更新：添加书籍、方法、人物标签页
- 知识图谱侧边栏扩展至50+节点，点击可直接跳转到概念详情
- 概念详情动态生成：showConcept函数重构，支持30+概念的详细数据和原文引用
- 相关书籍说明：
  - pdf_content目录包含19本PDF提取的txt文件
  - 《秘密印度》有完整中文翻译版本
  - 《圣者》(毛姆) 已有完整中文翻译
  - 所有书籍都需要翻译、理解并整合到知识库中

### 知识库多HTML重构（20260412-0415 - 重大升级）
- 目录: `c:/Users/willp/Desktop/2026年4月/kb01/pages/`（已迁移，旧路径 `c:/Users/willp/WorkBuddy/20260410104230/pages/`）
- 创建了90+个独立HTML文件 + 1个CSS文件（参考巴菲特知识库的多页结构）
- **导航栏全站统一（20260414修复）**：
  - 修复了全部90+HTML文件的左侧sidebar和顶部topbar不一致问题
  - sidebar标准结构：☰汉堡按钮 + 🙏logo + 搜索框 + 5大板块（核心索引含150+/经典著作/核心概念/修行方法/关键人物）
  - topbar标准结构：首页/书籍/概念/方法/问答/人物/图谱（共7项）
  - 修复：双层`<main>`嵌套、重复面包屑、多余首页链接、404链接
  - 修行问答计数统一为340+
- **章节聚焦模式（be-as-you-are + gems两本书22章节页）**：
  - 侧边栏自动折叠无关板块，只显示当前书的章节目录
  - 删除了章节导航栏（chapter-nav-bar）
  - 顶部topbar始终保持标准7项不变
- **QA页面扩充**：第11-12页，新增30条问答，新分类（世界/死亡/轮回/幸福）
- **书籍页面结构规范（20260420总结）**：
  - 模板基准文件: `be-as-you-are.html`
  - 书籍主页: `<div class="card">` 而非 `<section>` + `<a class="chapter-card">` 整块可点击
  - 章节页: `<header class="page-header">` + 多个 `<div class="card">`
  - 底部: page-nav（上一本/下一本）在 footer 之前
  - ⚠️ 旧模板残留: `article.book-detail`、`header.book-header`、`section.book-intro/book-content`、`chapter-toggle` 折叠
- **《全集》已更名为《权威合集》**（20260420）
- **概念页面完善**：创建了20+个概念详情页（bhakti/japa/world/enlightenment/sahaja/peace/fate/freewill/awareness/heart/jnana/jnani/samsara/satchidananda/self-enquiry/svasthya等）
- 文件结构：
  - pages/index.html - 首页
  - pages/graph.html - 知识图谱（D3.js）
  - pages/sitemap.html - 网站地图
  - pages/styles.css - 共享样式
  - pages/books/ - 书籍页面（含be-as-you-are-ch1~9.html、gems-ch1~13.html等章节页）
  - pages/concepts/ - 30+概念详情页
  - pages/persons/ - 人物页面
  - pages/methods/ - 方法页面
  - pages/qa/ - 问答页面（340+条，15主题，43页）
- 每个页面都有完整的meta标签（description, keywords, robots）利于SEO
- **GitHub + Vercel部署**：
  - GitHub：gstar-byte/ramana-kb
  - Vercel：ramana-kb（rootDirectory=pages）
  - 域名：ramanamaharshi.space（A记录→216.198.79.1）
  - PWA：manifest.json + sw.js（v5，预缓存130+页面）
- **响应式导航优化（20260415）**：
  - 所有断点统一高度48px
  - 汉堡菜单和顶部导航完美对齐
  - 移除黄色竖线，保留底部金色边框
  - 4档断点适配（<768px/768-900px/900-1024px/1025-1200px）

### PWA 和 Analytics（20260416）
- GA4: G-MYFWHFPSYB，已添加到132个页面
- PWA Analytics: pwa-analytics.js，跟踪3个事件
- Service Worker: sw.js v5，预缓存全部130+页面
- SEO: 所有页面添加 noindex,nofollow
- 辅助脚本：
  - add_ga4.py - 幂等性添加GA4代码
  - add_pwa_analytics.py - 添加PWA Analytics

### QA页面重构（20260419）
- **问题发现**：qa-29~58（30页）内容为批量脚本Bug导致的重复垃圾内容
- **修复方案**：删除qa-44~58，重写qa-29~43为15页真实内容
- **新增15页主题**：归伏/念诵/苦行/情绪/关系/疾病/金钱/食物/睡眠/神通/经典/其他法门/生平/静修院/弟子
- **当前状态**：43页，353条QA，7处重复（4处为原有，3处已修复）
- **脚本**：generate_qa_v2.py / fix_qa_questions.py

### SEO字符长度优化（20260417）
- **title**: 45-55字符（最佳），pages/目录下有seo_title_final.py批量处理
- **description**: 140-155字符（最佳），pages/目录下有seo_desc_auto.py批量处理
- 全部130个页面已完成优化
- 关键脚本：verify_titles.py / verify_desc.py 验证，seo_fill_remaining.py补充遗漏

### 书籍页面UI统一修复（20260419）
- **问题**：《面对面》首页使用旧CSS类，与《宝钻集》不一致
- **修复**：重写face-to-face.html主体内容，统一为标准类（page-header/card/chapter-card）
- **受影响文件**：face-to-face.html

### 章节页面面包屑修复（20260419）
- **问题**：5个《面对面》章节页面面包屑缺少"书籍"层
- **修复**：添加 `<a href="../books/index.html">书籍</a>` 层
- **受影响文件**：face-to-face-ch1.html ~ ch5.html

### 侧边栏折叠按钮修复（20260419）
- **问题**：16个章节页面侧边栏折叠按钮无法点击
- **根因**：事件绑定冲突（内联脚本与script.js重复绑定）
- **修复**：批量移除内联脚本中的重复绑定代码
- **受影响文件**：
  - face-to-face-ch1~5.html（5个）
  - be-as-you-are-ch1~3.html（3个）
  - day-by-day-ch1~8.html（8个）
- **验证**：浏览器F12检查Event Listeners应只有一个click监听器

### 《马哈希福音》14章完整页面（20260419-20）
- **新增**：ch1-ch14 完整章节页面
- **每章结构**：
  - 章节概要（3段落）
  - 核心教导（quote-box）
  - 经典比喻/深意
  - 修行指引
  - 核心洞见（ul列表）
  - 相关概念（concept-tags）
  - 章节导航
- **修复问题**：
  1. 内容区域宽度（移除page-content包裹）
  2. HTML残留代码清理
  3. 列表样式统一（ul内联样式）
- **部署**：已推送到 ramanamaharshi.space

### 概念页面丰富（20260420）
- **新增39个概念详情页**（pages/concepts/目录，不含index.html和_template.html）
- **页面结构标准**：
  - 概念定义（quote-box 金色边框）
  - 核心教导/原文引用
  - 修行指引
  - 相关概念链接（concept-tags）
  - 面包屑导航
- **概念分类体系**：
  - 本体论(6)：真我、梵、本心、存在-意识-喜悦、摩耶、世界
  - 心智与自我(10)：心智、自我、念头、习气、我念、觉知、无明、意识-物质纽结、自性、个体灵魂
  - 修行法门(9)："我是谁？"、静默、三摩地、臣服、奉爱、念诵、禅定、参究、修行
  - 解脱与境界(11)：解脱、恩典、上师、业力、觉者、开悟、自然安住、命运、自由意志、在生解脱、宿业、安宁
- **与书籍/QA丰富工作的关系**：
  - 书籍丰富：章节概要+核心教导+经典比喻+修行指引+核心洞见+相关概念
  - QA丰富：问题+回答+分类标签+相关概念
  - 概念丰富：定义+原文引用+修行指引+相关概念
- **文件**：pages/concepts/*.html（39个文件）

## 用户偏好
- 中文交流
- 绝对路径优先
- 知识图谱需要清晰的节点标签显示
- **重要工作流**：新增页面时必须同步完成SEO（title/description）+ 更新sitemap.xml + 更新sitemap.html

## 重要书籍说明
- pdf_content目录包含19本PDF提取的txt文件
- 《秘密印度》有完整中文翻译版本
- 《圣者》(毛姆) 已有完整中文翻译
- 所有书籍都需要翻译、理解并整合到知识库中
