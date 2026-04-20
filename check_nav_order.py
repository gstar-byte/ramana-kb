"""
检查所有书籍页的上一本/下一本导航是否正确
"""
import re, os

BASE = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books'

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
    'be-as-you-are.html': '走向静默',
    'gems.html': '宝钻集',
    'talks.html': '对谈录',
    'back-to-heart.html': '回到你心中',
    'day-by-day.html': '日日与彼',
    'face-to-face.html': '面对面',
    'maharshi-gospel.html': '马哈希福音',
    'search-secret-india.html': '印度探秘',
    'maha-yoga.html': '大瑜伽',
    'collected-works.html': '权威合集',
    'spiritual-stories.html': '灵性故事',
    'reflections.html': '反思录',
    'teachings.html': '以言传意',
    'surpassing-love.html': '超越爱与恩典',
    'crumbs.html': '桌边碎语',
    'timeless.html': '时代中的永恒',
}

for f in ORDER:
    path = os.path.join(BASE, f)
    if not os.path.exists(path):
        print(f'MISSING: {f}')
        continue
    c = open(path, encoding='utf-8').read()
    i = ORDER.index(f)
    prev = ORDER[i - 1] if i > 0 else None
    nxt = ORDER[i + 1] if i < len(ORDER) - 1 else None

    nav_m = re.search(r'<div class="page-nav">(.*?)</div>', c, re.DOTALL)
    if not nav_m:
        print(f'{TITLE[f]:12s}: [无导航]')
        continue

    nav_text = nav_m.group(1)
    links = re.findall(r'href="([^"]+)"', nav_text)
    prev_link = links[0] if len(links) > 0 else None
    nxt_link = links[1] if len(links) > 1 else None

    # nav只有一个<a>时，prev_link就是nxt；有两个时，prev_link=prev, nxt_link=nxt
    if prev is not None:
        prev_ok = prev_link == prev
        nxt_ok = nxt_link == nxt
    else:
        # 第一本书：nav只有一个链接（prev_link实际是next）
        prev_ok = True  # 无prev链接，正确
        nxt_ok = prev_link == nxt  # prev_link实际是nxt

    prev_label = TITLE.get(prev, '') if prev else ''
    nxt_label = TITLE.get(nxt, '') if nxt else ''

    status = 'OK' if (prev_ok and nxt_ok) else 'ERR'
    print(f'{status} {TITLE[f]:12s}: prev={prev_link}({prev_label}) / nxt={nxt_link}({nxt_label})')
