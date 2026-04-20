"""
统一书籍导航位置到页面底部（footer 之前）
"""
import os, re

BASE = r"c:/Users/willp/Desktop/2026年4月/kb01/pages/books"

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
    ("reflections.html",         "反思录",               "💭"),
    ("teachings.html",           "以言传意",             "📗"),
    ("surpassing-love.html",     "超越爱与恩典",          "💝"),
    ("crumbs.html",              "桌边碎语",             "🍞"),
    ("timeless.html",            "时代中的永恒",          "⏳"),
]
book_map = {b[0]: i for i, b in enumerate(BOOKS)}

def get_nav_html(filename):
    if filename not in book_map:
        return None
    idx = book_map[filename]
    prev_book = BOOKS[idx - 1] if idx > 0 else None
    next_book = BOOKS[idx + 1] if idx < len(BOOKS) - 1 else None

    nav = '<!-- 上一本 下一本 -->\n    <div class="page-nav">\n'
    if prev_book:
        nav += f'    <a href="{prev_book[0]}"><span class="nav-label">← 上一本</span><span class="nav-title">{prev_book[2]} {prev_book[1]}</span></a>\n'
    else:
        nav += '    <span></span>\n'
    if next_book:
        nav += f'    <a href="{next_book[0]}"><span class="nav-label">下一本 →</span><span class="nav-title">{next_book[2]} {next_book[1]}</span></a>\n'
    else:
        nav += '    <span></span>\n'
    nav += '</div>'
    return nav


for fname, title, emoji in BOOKS:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. 先删除现有的导航（如果有）
    # 匹配 <!-- 上一本 下一本 --> 到 </div> 的块
    pattern = r'\s*<!-- 上一本 下一本 -->\s*<div class="page-nav">.*?</div>\s*'
    html_clean = re.sub(pattern, '\n', html, flags=re.DOTALL)
    
    # 2. 在 <footer class="site-footer"> 之前插入新导航
    nav_html = get_nav_html(fname)
    footer_pos = html_clean.find('<footer class="site-footer">')
    
    if footer_pos == -1:
        print(f"⚠ {fname}: 找不到 footer")
        continue
    
    # 在 footer 前插入导航
    new_html = html_clean[:footer_pos] + '\n    ' + nav_html + '\n\n    ' + html_clean[footer_pos:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"✓ {fname}: 导航已移到 footer 前")

print("\n完成！")
