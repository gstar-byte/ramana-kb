# 工作记忆

## 项目

### 拉玛那马哈希知识库项目
- **当前路径（已迁移）**: `c:/Users/willp/Desktop/2026年4月/kb01/`
- GitHub: gstar-byte/ramana-kb
- Vercel: ramana-kb（域名 ramanamaharshi.space）

### Git历史问题警告（20260421）
- **问题**：Trae solo agent 完全替换了 styles.css/script.js/search.js，导致样式丢失
- **表现**：面包屑字体变小、底部出现大量空白
- **解决**：回退到 4d28142 提交版本
- **教训**：Trae solo 的 git 操作为覆盖式而非增量修改，会丢失原有文件内容

### 移动端汉堡菜单修复（20260421）
- **问题**：移动端汉堡菜单点击无反应
- **根因**：页面HTML没有引用 `script.js`，导致 `toggleSidebar()` 函数不存在
- **解决**：创建批量修复脚本，为85个包含hamburger按钮的HTML文件添加 `<script src="script.js">` 引用
- **教训**：添加新页面模板时，确保引入必要的JS文件

### 书签知识库（备用）
- 路径: `C:/Users/willp/Desktop/书签/`
- GitHub: willp/bookmarks-kb
- 技术: Next.js 静态导出

### 0313项目（GStarCAD 3D查看器）
- 路径: `C:/Users/willp/Desktop/project/0313/`
- 技术栈: 浩辰CAD Web Viewer

### 桌边碎语书籍页面重构（20260422）
- **新增**：crumbs-ch5~ch12 共8个章节页（加上已有的ch1~ch4，共12章完整）
- **重写主页**：crumbs.html 从旧的 book-detail 布局改为 page-header + card 卡片式，与宝钻集等书籍页面UI统一
- **修复footer**：12个章节页统一补上"网站地图"和"联系我"链接
- **删除"相关概念"**：书籍页面不需要相关概念区块
- **教训**：书籍主页模板必须用 `page-header` + `card` 布局，不能用旧的 `book-detail`；章节页footer需包含网站地图和联系我

### 超越爱与恩典内容丰富（20260422-23）✅ 全书完成
- **原书**：`pdf_content/surpassing_love.txt`（英文PDF扫描，80页，覆盖book page 1-70约8章）
- **1-10章**：基于原书提取内容（1-8章用原书内容，9-10章基于教义整理）
- **11-20章**：基于教义自行撰写
- **21-30章**：JSON数据+Python脚本批量生成（4月23日）
- **31-43章**：同法生成（4月23日），全书43章全部完成
- **生成方式**：JSON存内容 + Python脚本填充模板（避免PowerShell引号转义问题）

### 内容创作策略（20260423）
- **概念页**：凡是拉玛那马哈希及吠檀多不二论哲学相关概念都可以新增
- **QA页**：充分理解原文后自行撰写也可，不限于从原书逐字提取
- **书籍章节**：基于原书核心内容提取+教义整理

### PWA 问题（20260423）
- **名称**：manifest.json name/short_name 改为"拉玛那知识库"（原来name末尾有Space）
- **图标问题**：安装后头像小、四角白色 → 需要符合maskable规范的图标（内容居中80%区域）
- **启动屏**：需要用户提供马哈希照片来生成splash screen

### Vercel CDN 缓存问题（20260422-23）
- push 后线上有时不更新，需要空提交触发 redeploy
- 用户强制刷新(Ctrl+Shift+R)也可能无效 → Vercel CDN 缓存延迟

## 用户偏好
- 中文交流
- 绝对路径优先
- 临时脚本和无关文件一律不提交 Git
- QA/概念内容创作：充分理解原文自行撰写也可
