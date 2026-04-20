"""
给所有书籍主页底部添加"上一本/下一本"导航
"""
import os, re

BASE = r"c:/Users/willp/Desktop/2026年4月/kb01/pages/books"

# 书籍顺序（从 books/index.html 的 book-card 顺序提取）
BOOKS = [
    ("be-as-you-are.html",      "走向静默，如你本来",  "📖"),
    ("gems.html",                "宝钻集",              "💎"),
    ("talks.html",               "对谈录",              "💬"),
    ("back-to-heart.html",       "回到你心中",           "📕"),
    ("day-by-day.html",          "日日与彼",             "📅"),
    ("face-to-face.html",        "面对面",               "👁️"),
    ("maharshi-gospel.html",     "马哈希福音",           "📜"),
    ("search-secret-india.html", "秘密印度",             "🔍"),
    ("maha-yoga.html",           "大瑜伽",               "🧘"),
    ("collected-works.html",     "全集",                 "📚"),
    ("spiritual-stories.html",   "灵性故事",             "📖"),
    ("reflections.html",        "反思录",               "💭"),
    ("teachings.html",           "以言传意",             "📗"),
    ("surpassing-love.html",     "超越爱与恩典",          "💝"),
    ("crumbs.html",              "桌边碎语",             "🍞"),
    ("timeless.html",            "时代中的永恒",          "⏳"),
]

# 建立 filename -> index 映射
book_map = {b[0]: i for i, b in enumerate(BOOKS)}

def get_nav_html(filename):
    """生成上一本/下一本 HTML"""
    if filename not in book_map:
        return None
    idx = book_map[filename]
    prev_book = BOOKS[idx - 1] if idx > 0 else None
    next_book = BOOKS[idx + 1] if idx < len(BOOKS) - 1 else None

    nav = '<div class="page-nav">\n'

    if prev_book:
        prev_file, prev_title, prev_emoji = prev_book
        nav += f'    <a href="{prev_file}"><span class="nav-label">← 上一本</span><span class="nav-title">{prev_emoji} {prev_title}</span></a>\n'
    else:
        nav += '    <span></span>\n'

    if next_book:
        next_file, next_title, next_emoji = next_book
        nav += f'    <a href="{next_file}"><span class="nav-label">下一本 →</span><span class="nav-title">{next_emoji} {next_title}</span></a>\n'
    else:
        nav += '    <span></span>\n'

    nav += '</div>'
    return nav


def add_book_nav(filename):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"  ⚠ 文件不存在: {filename}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 检查是否已有 page-nav（books 专用）
    if 'book-nav' in html or '<!-- 上一本 下一本 -->' in html:
        print(f"  ✓ 已处理过: {filename}")
        return

    nav_html = get_nav_html(filename)
    if not nav_html:
        print(f"  ⚠ 无法生成导航: {filename}")
        return

    # 找到 </div>（content-wrapper 结束）后、<footer 开始前的位置插入
    content_end = html.find('</div>', html.find('content-wrapper'))
    footer_start = html.find('<footer', content_end)

    if content_end == -1 or footer_start == -1:
        print(f"  ⚠ 结构异常: {filename}")
        return

    insert_pos = content_end + len('</div>')
    new_html = html[:insert_pos] + '\n\n    <!-- 上一本 下一本 -->\n    ' + nav_html + '\n' + html[insert_pos:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"  ✓ {filename}: 上一本 ←{BOOKS[book_map[filename]][1]}→ 下一本 {BOOKS[book_map[filename]+1][1] if book_map[filename] < len(BOOKS)-1 else ''}")


print("=== 为所有书籍主页添加上一本/下一本导航 ===")
for filename, _, _ in BOOKS:
    add_book_nav(filename)

print("\n完成！")
