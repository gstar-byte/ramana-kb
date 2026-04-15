"""
修复第三批剩余6个文件的 topbar（没有 <!-- 主内容区 --> 注释的版本）
"""
import re

pages_dir = "c:/Users/willp/WorkBuddy/20260410104230/pages"

FILES = {
    "books/day-by-day.html":       ("day-by-day.html", "📅 日日与彼"),
    "books/face-to-face.html":     ("face-to-face.html", "👁️ 面对面"),
    "books/maha-yoga.html":        ("maha-yoga.html", "🧘 大瑜伽"),
    "books/collected-works.html":  ("collected-works.html", "📚 全集"),
    "books/spiritual-stories.html":("spiritual-stories.html", "📖 灵性故事"),
    "books/reflections.html":      ("reflections.html", "💭 反思录"),
}

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


for rel_path, (active_file, title) in FILES.items():
    filepath = f"{pages_dir}/{rel_path}"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配：<main class="main-content"> 后紧跟的 <header class="topbar">...</header>
    pattern = re.compile(
        r'(<main class="main-content">\s*)(<header class="topbar">.*?</header>)',
        re.DOTALL
    )
    replacement = r'\1' + make_topbar(title)
    new_content, n = pattern.subn(replacement, content)

    if n == 0:
        print(f"  ⚠️  {rel_path}: 未找到 topbar，跳过")
        continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  ✅  {rel_path}: topbar 已替换")

print("\n全部完成！")
