"""
批量检查并修复所有书籍页的"上一本/下一本"导航
以 books/index.html 的书籍顺序为准
"""
import re, os

BASE = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books'

# books/index.html 中的书籍顺序（不含章节页）
ORDER = [
    'be-as-you-are.html',
    'gems.html',
    'talks.html',
    'back-to-heart.html',
    'day-by-day.html',
    'face-to-face.html',
    'maharshi-gospel.html',
    'search-secret-india.html',
    'maha-yoga.html',
    'collected-works.html',
    'spiritual-stories.html',
    'reflections.html',
    'teachings.html',
    'surpassing-love.html',
    'crumbs.html',
    'timeless.html',
]

TITLE = {
    'be-as-you-are.html': '📖 走向静默，如你本来',
    'gems.html': '💎 宝钻集',
    'talks.html': '💬 对谈录',
    'back-to-heart.html': '📕 回到你心中',
    'day-by-day.html': '📅 日日与彼',
    'face-to-face.html': '👁️ 面对面',
    'maharshi-gospel.html': '📜 马哈希福音',
    'search-secret-india.html': '🔍 印度探秘',
    'maha-yoga.html': '🧘 大瑜伽',
    'collected-works.html': '📚 权威合集',
    'spiritual-stories.html': '📖 灵性故事',
    'reflections.html': '💭 反思录',
    'teachings.html': '📝 以言传意',
    'surpassing-love.html': '💝 超越爱与恩典',
    'crumbs.html': '🍞 桌边碎语',
    'timeless.html': '⏳ 时代中的永恒',
}

def get_nav_html(filename):
    i = ORDER.index(filename)
    prev = ORDER[i - 1] if i > 0 else None
    nxt = ORDER[i + 1] if i < len(ORDER) - 1 else None
    parts = []
    if prev:
        parts.append(
            f'<a href="{prev}"><span class="nav-label">← 上一本</span>'
            f'<span class="nav-title">{TITLE[prev]}</span></a>'
        )
    if nxt:
        parts.append(
            f'<a href="{nxt}"><span class="nav-label">下一本 →</span>'
            f'<span class="nav-title">{TITLE[nxt]}</span></a>'
        )
    return '<!-- 上一本 下一本 -->\n            <div class="page-nav">\n                ' + '\n                '.join(parts) + '\n            </div>'

def fix_file(filepath):
    c = open(filepath, encoding='utf-8').read()
    fname = os.path.basename(filepath)

    if fname not in ORDER:
        return False  # 跳过章节页等

    new_nav = get_nav_html(fname)

    # 找 page-nav 区域并替换
    pattern = r'(<!-- 上一本 下一本 -->.*?<div class="page-nav">.*?</div>\s*)'
    m = re.search(pattern, c, re.DOTALL)
    if m:
        old = m.group(1)
        c = c.replace(old, new_nav + '\n            ')
        open(filepath, 'w', encoding='utf-8').write(c)
        return True
    else:
        return False  # 没找到，暂不处理

fixed = []
for f in ORDER:
    path = os.path.join(BASE, f)
    if os.path.exists(path):
        ok = fix_file(path)
        if ok:
            fixed.append(f)

print('已修复:')
for f in fixed:
    i = ORDER.index(f)
    prev = ORDER[i-1] if i > 0 else None
    nxt = ORDER[i+1] if i < len(ORDER)-1 else None
    print(f'  {f}: ← {prev} / {nxt} →')
print(f'\n共 {len(fixed)} 个文件')
