"""
修复第三批：9个面包屑页面的 sidebar 和 topbar
"""
import re

pages_dir = "c:/Users/willp/WorkBuddy/20260410104230/pages"

# 9个目标文件及其对应的「当前激活书籍」链接名
FILES = {
    "books/crumbs.html":           ("crumbs.html", "🍞 桌边碎语"),
    "books/day-by-day.html":       ("day-by-day.html", "📅 日日与彼"),
    "books/face-to-face.html":     ("face-to-face.html", "👁️ 面对面"),
    "books/maha-yoga.html":        ("maha-yoga.html", "🧘 大瑜伽"),
    "books/collected-works.html":  ("collected-works.html", "📚 全集"),
    "books/spiritual-stories.html":("spiritual-stories.html", "📖 灵性故事"),
    "books/reflections.html":      ("reflections.html", "💭 反思录"),
    "books/surpassing-love.html":  ("surpassing-love.html", "💝 超越爱与恩典"),
    "books/teachings.html":        ("teachings.html", "📝 以言传意"),
}

# 大书籍列表用于 sidebar（书籍分类板块）
def make_sidebar(active_file, title):
    """生成标准 sidebar，active_file 是当前页对应的文件名，用于标记 active"""

    def ai(f):
        return ' active' if f == active_file else ''

    return f'''        <!-- 左侧边栏 -->
        <aside class="sidebar" id="sidebar">
            <button class="hamburger" onclick="toggleSidebar()">☰</button>
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
            </div>
            
            <!-- 核心索引 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item active"><span class="emoji">📖</span> 书籍总览 <span class="count">18</span></a>
                    <a href="../concepts/index.html" class="sidebar-item"><span class="emoji">🔮</span> 核心概念 <span class="count">30+</span></a>
                    <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> 修行方法 <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> 修行问答 <span class="count">120+</span></a>
                    <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> 知识图谱</a>
                </div>
            </div>
            
            <!-- 经典著作 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">📖 经典著作</div>
                <div class="sidebar-items">
                    <a href="be-as-you-are.html" class="sidebar-item{ai('be-as-you-are.html')}">📖 走向静默，如你本来</a>
                    <a href="gems.html" class="sidebar-item{ai('gems.html')}">💎 宝钻集</a>
                    <a href="talks.html" class="sidebar-item{ai('talks.html')}">💬 对谈录</a>
                    <a href="back-to-heart.html" class="sidebar-item{ai('back-to-heart.html')}">📕 回到你心中</a>
                </div>
            </div>
            
            <!-- 对话与日记 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">📅 对话与日记</div>
                <div class="sidebar-items">
                    <a href="day-by-day.html" class="sidebar-item{ai('day-by-day.html')}">📅 日日与彼</a>
                    <a href="face-to-face.html" class="sidebar-item{ai('face-to-face.html')}">👁️ 面对面</a>
                    <a href="maharshi-gospel.html" class="sidebar-item{ai('maharshi-gospel.html')}">📜 马哈希福音</a>
                </div>
            </div>
            
            <!-- 哲学专著 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 哲学专著</div>
                <div class="sidebar-items">
                    <a href="collected-works.html" class="sidebar-item{ai('collected-works.html')}">📚 全集</a>
                    <a href="spiritual-stories.html" class="sidebar-item{ai('spiritual-stories.html')}">📖 灵性故事</a>
                    <a href="reflections.html" class="sidebar-item{ai('reflections.html')}">💭 反思录</a>
                </div>
            </div>
            
            <!-- 其他著作 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">📗 其他著作</div>
                <div class="sidebar-items">
                    <a href="teachings.html" class="sidebar-item{ai('teachings.html')}">📝 以言传意</a>
                    <a href="surpassing-love.html" class="sidebar-item{ai('surpassing-love.html')}">💝 超越爱与恩典</a>
                    <a href="crumbs.html" class="sidebar-item{ai('crumbs.html')}">🍞 桌边碎语</a>
                    <a href="timeless.html" class="sidebar-item{ai('timeless.html')}">⏳ 时代中的永恒</a>
                </div>
            </div>
        </aside>'''


def make_topbar(title):
    return f'''            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">{title}</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="index.html" class="active">书籍</a>
                    <a href="../concepts/index.html">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>'''


def fix_file(rel_path, active_file, title):
    filepath = f"{pages_dir}/{rel_path}"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # ── 1. 替换整个 <aside class="sidebar"...>...</aside> ──
    sidebar_pattern = re.compile(
        r'[ \t]*<!-- (?:侧边栏|左侧边栏) -->\s*<aside class="sidebar"[^>]*>.*?</aside>',
        re.DOTALL
    )
    new_sidebar = make_sidebar(active_file, title)
    content, n1 = sidebar_pattern.subn(new_sidebar, content)
    if n1 == 0:
        # 尝试不带注释的版本
        sidebar_pattern2 = re.compile(r'[ \t]*<aside class="sidebar"[^>]*>.*?</aside>', re.DOTALL)
        content, n1 = sidebar_pattern2.subn(new_sidebar, content)

    # ── 2. 替换顶部导航栏（面包屑式 header.topbar）──
    topbar_pattern = re.compile(
        r'[ \t]*<!-- 主内容区 -->\s*<main class="main-content">\s*<!-- 顶部导航栏 -->\s*<header class="topbar">.*?</header>',
        re.DOTALL
    )
    # 构造替换后的版本（保留外层 <main> 开启标签和注释）
    new_topbar_block = f'''        <!-- 主内容区 -->
        <main class="main-content">
{make_topbar(title)}'''
    content, n2 = topbar_pattern.subn(new_topbar_block, content)

    if n1 == 0 and n2 == 0:
        print(f"  ⚠️  {rel_path}: 未找到需要替换的内容，跳过")
        return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✅  {rel_path}: sidebar({'已替换' if n1 else '未变'}) topbar({'已替换' if n2 else '未变'})")


print("开始修复第三批（面包屑页面）...")
for rel_path, (active_file, title) in FILES.items():
    fix_file(rel_path, active_file, title)
print("\n全部完成！")
