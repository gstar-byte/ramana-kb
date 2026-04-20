"""
为4个缺少 footer 和 content-wrapper 闭合的书籍主页修复结构
"""
import os

BASE = r"c:/Users/willp/Desktop/2026年4月/kb01/pages/books"

# 书籍顺序
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

FOOTER = '''<footer class="site-footer">
                <p><a href="../index.html">拉玛那马哈希</a> | 传承自印度阿鲁那佳拉圣山</p>
                <p style="margin-top:0.5rem; font-size:0.9rem; color: var(--text-muted);">© 2026 拉玛那马哈希. 保留所有权利。</p>
                <p style="margin-top:1rem; font-size:0.9rem;"><a href="../sitemap.html" style="color: var(--text-muted); text-decoration: underline;">🌐 网站地图</a> <span style="margin: 0 1rem;">|</span> <a href="mailto:591611431@qq.com" style="color: var(--text-muted); text-decoration: underline;">联系我</a></p>
            </footer>'''

def get_nav(filename):
    if filename not in book_map:
        return ''
    idx = book_map[filename]
    prev = BOOKS[idx - 1] if idx > 0 else None
    next_b = BOOKS[idx + 1] if idx < len(BOOKS) - 1 else None
    nav = '<div class="page-nav">\n'
    if prev:
        nav += f'    <a href="{prev[0]}"><span class="nav-label">← 上一本</span><span class="nav-title">{prev[2]} {prev[1]}</span></a>\n'
    else:
        nav += '    <span></span>\n'
    if next_b:
        nav += f'    <a href="{next_b[0]}"><span class="nav-label">下一本 →</span><span class="nav-title">{next_b[2]} {next_b[1]}</span></a>\n'
    else:
        nav += '    <span></span>\n'
    nav += '</div>'
    return nav


# 需要修复的文件：它们缺少 content-wrapper 的闭合 div 和 footer
PROBLEMATIC = ['talks.html', 'back-to-heart.html', 'day-by-day.html', 'face-to-face.html']

for fname in PROBLEMATIC:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 替换 pattern: </div></main>  → 添加 content-wrapper闭合 + nav + footer + </main>
    old = '</div>\n        </main>'
    new = f'''</div>

            <!-- 上一本 下一本 -->
            {get_nav(fname)}

            {FOOTER}
        </main>'''

    if old in html:
        html = html.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'✓ 修复 {fname}')
    else:
        print(f'⚠ 结构不匹配 {fname}，尝试备用方案')
        # 备用：找 </main> 前的位置
        em = html.find('</main>')
        if em > 0:
            insert = f'\n\n            <!-- 上一本 下一本 -->\n            {get_nav(fname)}\n\n            {FOOTER}\n        '
            new_html = html[:em] + insert + html[em:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f'  ✓ 备用方案修复 {fname}')

print('\n完成！')
