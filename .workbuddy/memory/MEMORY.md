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

## 用户偏好
- 中文交流
- 绝对路径优先
