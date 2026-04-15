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
- 路径: `c:/Users/willp/WorkBuddy/20260410104230/`
- 主文件: `拉玛那马哈希知识库.html`（交互式单页面应用）
- Skill: `~/.workbuddy/skills/拉玛那知识库/SKILL.md`
- 架构: 三层节点（概念/书籍/人物）+ 可点击跳转
- 已整合书籍（14本）：
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

### 知识库多HTML重构（20260412-0413 - 重大升级）
- 新目录: `c:/Users/willp/WorkBuddy/20260410104230/pages/`
- 创建了90+个独立HTML文件 + 1个CSS文件（参考巴菲特知识库的多页结构）
- **20260414重大修复（导航栏全站统一）**：
  - 修复了全部90+HTML文件的左侧sidebar和顶部topbar不一致问题
  - sidebar标准结构：☰汉堡按钮 + 🙏logo + 搜索框 + 5大板块（核心索引含150+/经典著作/核心概念/修行方法/关键人物）
  - topbar标准结构：首页/书籍/概念/方法/问答/人物/图谱（共7项）
  - 修复：双层`<main>`嵌套、重复面包屑、多余首页链接、404链接
  - 修行问答计数统一为150+
- **章节聚焦模式（be-as-you-are + gems两本书22章节页）**：
  - 侧边栏自动折叠无关板块，只显示当前书的章节目录
  - 删除了章节导航栏（chapter-nav-bar）
  - 顶部topbar始终保持标准7项不变
- **QA页面扩充**：第11-12页，新增30条问答，新分类（世界/死亡/轮回/幸福）
- **概念页面完善**：创建了20+个概念详情页（bhakti/japa/world/enlightenment/sahaja/peace/fate/freewill/awareness/heart/jnana/jnani/samsara/satchidananda/self-enquiry/svasthya等）
- 文件结构：
  - pages/index.html - 首页
  - pages/graph.html - 知识图谱（D3.js）
  - pages/styles.css - 共享样式
  - pages/books/ - 书籍页面（含be-as-you-are-ch1~9.html、gems-ch1~13.html等章节页）
  - pages/concepts/ - 30+概念详情页
  - pages/persons/ - 人物页面
  - pages/methods/ - 方法页面
  - pages/qa/ - 问答页面（150+条，12分类，12页）
- 每个页面都有完整的meta标签（description, keywords）利于SEO
- **GitHub + Vercel部署**：
  - GitHub：gstar-byte/ramana-kb
  - Vercel：ramana-kb（rootDirectory=pages）
  - 域名：ramanamaharshi.space（A记录→216.198.79.1）
  - PWA：manifest.json + sw.js + 8种尺寸图标
- **未来方向**：
  - 按前两本书（走向静默/宝钻集）的模式继续丰富其他书籍
  - 完善每个概念，把所有概念都放到知识图谱中
  - 知识图谱要包含：人物、概念、书籍、方法等全面关联

## 用户偏好
- 中文交流
- 绝对路径优先
- 知识图谱需要清晰的节点标签显示

## 重要书籍说明
- pdf_content目录包含19本PDF提取的txt文件
- 《秘密印度》有完整中文翻译版本
- 《圣者》(毛姆) 已有完整中文翻译
- 所有书籍都需要翻译、理解并整合到知识库中
