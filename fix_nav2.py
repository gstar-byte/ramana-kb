#!/usr/bin/env python3
"""
统一书籍章节页翻页导航为 page-nav 风格。
处理以下所有模式：
  A. <div class="card"><div style="flex">prev/next</div></div>
  B. <div class="card"><div class="concept-tags">prev/next</div></div>
  C. <a class="tag" href="next">下一章 →</a>  (无div包裹)
  D. <a class="btn-primary/secondary">下一章 →</a>  (无div包裹)
  E. talks-ch2/ch3 无导航 → INSERT before </main>
  F. 章节导航 card (maharshi-gospel)
  G. <!-- 章节导航 --> 注释 + card
"""
import re, os, glob

BOOKS_DIR = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books'

# 书籍元数据
BOOKS = {
    'be-as-you-are':        {'title': '走向静默，如你本来', 'file': 'be-as-you-are.html'},
    'gems':                 {'title': '宝钻集',             'file': 'gems.html'},
    'back-to-heart':        {'title': '回到你心中',         'file': 'back-to-heart.html'},
    'day-by-day':           {'title': '日日与彼',           'file': 'day-by-day.html'},
    'face-to-face':         {'title': '面对面',             'file': 'face-to-face.html'},
    'talks':                {'title': '对谈录',             'file': 'talks.html'},
    'maharshi-gospel':      {'title': '马哈希福音',         'file': 'maharshi-gospel.html'},
    'self-enquiry':         {'title': '自我参究',           'file': 'self-enquiry.html'},
    'crumbs':               {'title': '桌边碎语',           'file': 'crumbs.html'},
    'spiritual-stories':    {'title': '灵性故事',           'file': 'spiritual-stories.html'},
    'surpassing-love':      {'title': '超越爱与恩典',       'file': 'surpassing-love.html'},
    'teachings':            {'title': '以言传意',           'file': 'teachings.html'},
    'timeless':             {'title': '时代中的永恒',       'file': 'timeless.html'},
    'search-secret-india':   {'title': '秘密印度',           'file': 'search-secret-india.html'},
    'reflections':          {'title': '反思录',             'file': 'reflections.html'},
    'maha-yoga':            {'title': '大瑜伽',             'file': 'maha-yoga.html'},
    'guru-vachaka':         {'title': '上师言颂',           'file': 'guru-vachaka-kovai.html'},
    'collected-works':      {'title': '全集',               'file': 'collected-works.html'},
    'gospel-of-bhagavan':   {'title': '马哈希福音',         'file': 'maharshi-gospel.html'},
    'reflections':          {'title': '反思录',             'file': 'reflections.html'},
}

def extract_ch_num(filename):
    m = re.search(r'-ch(\d+)\.html', filename)
    return int(m.group(1)) if m else None

def get_chapter_title(filepath, chapter_num):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
        if m:
            t = m.group(1).strip()
            for bp in ['走向静默，如你本来 ', '宝钻集 ', '回到你心中 ', '日日与彼 ',
                       '面对面 ', '对谈录 ', '马哈希福音 ', '自我参究 ',
                       '桌边碎语 ', '灵性故事 ', '超越爱与恩典 ', '以言传意 ',
                       '时代中的永恒 ', '秘密印度 ', '反思录 ', '大瑜伽 ',
                       '上师言颂 ', '全集 ']:
                if t.startswith(bp):
                    t = t[len(bp):]
                    break
            return t
    except:
        pass
    return f'第{chapter_num}章'

def build_nav(book_key, chapter_num, prev_file, next_file, prev_title, next_title):
    book_meta = BOOKS.get(book_key, {'title': book_key, 'file': book_key + '.html'})
    book_title = book_meta['title']
    book_file = book_meta['file']

    prev_html = (f'<a href="{prev_file}">'
                 f'<span class="nav-label">← 上一章</span>'
                 f'<span class="nav-title">{prev_title}</span>'
                 f'</a>') if prev_file else '<span></span>'

    book_html = (f'<a href="{book_file}">'
                 f'<span class="nav-label">返回书籍</span>'
                 f'<span class="nav-title">{book_title}全书</span>'
                 f'</a>')

    next_html = (f'<a href="{next_file}">'
                 f'<span class="nav-label">下一章 →</span>'
                 f'<span class="nav-title">{next_title}</span>'
                 f'</a>') if next_file else '<span></span>'

    return (f'\n                <div class="page-nav">\n                    {prev_html}\n                    {book_html}\n                    {next_html}\n                </div>\n')

def get_nav_info(book_key, chapter_num, all_chapters):
    prev_info = next_info = None
    for i, (n, fname, fpath) in enumerate(all_chapters):
        if n == chapter_num:
            if i > 0:
                prev_info = all_chapters[i-1]
            if i < len(all_chapters) - 1:
                next_info = all_chapters[i+1]
            break
    prev_file = os.path.basename(prev_info[2]) if prev_info else None
    next_file = os.path.basename(next_info[2]) if next_info else None
    prev_title = get_chapter_title(prev_info[2], prev_info[0]) if prev_info else ''
    next_title = get_chapter_title(next_info[2], next_info[0]) if next_info else ''
    return prev_file, next_file, prev_title, next_title

def process_file(filepath):
    filename = os.path.basename(filepath)

    book_key = None
    for key in BOOKS:
        if filename.startswith(key + '-ch'):
            book_key = key
            break
    if not book_key:
        return False, 'unknown book'

    chapter_num = extract_ch_num(filename)
    if not chapter_num:
        return False, 'no chapter num'

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'class="page-nav"' in content:
        return False, 'already page-nav'

    # 收集同书所有章节
    all_chapters = []
    for f in glob.glob(f'{BOOKS_DIR}/{book_key}-ch*.html'):
        n = extract_ch_num(os.path.basename(f))
        if n:
            all_chapters.append((n, os.path.basename(f), f))
    all_chapters.sort(key=lambda x: x[0])

    prev_file, next_file, prev_title, next_title = get_nav_info(book_key, chapter_num, all_chapters)
    new_nav = build_nav(book_key, chapter_num, prev_file, next_file, prev_title, next_title)

    original = content
    replaced = False

    # ===== 模式A: flex div inside card =====
    # 上一章+下一章
    patA_full = re.compile(
        r'<div class="card">\s*'
        r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*'
        r'<a href="([^"]*)" class="tag">[^<]*上一章[^<]*</a>\s*'
        r'<a href="([^"]*)" class="tag">[^<]*下一章[^<]*</a>\s*'
        r'</div>\s*'
        r'</div>',
        re.DOTALL)
    # 上一章+空span
    patA_prev = re.compile(
        r'<div class="card">\s*'
        r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*'
        r'<a href="([^"]*)" class="tag">[^<]*上一章[^<]*</a>\s*'
        r'<span></span>\s*'
        r'</div>\s*'
        r'</div>',
        re.DOTALL)
    # 空span+下一章
    patA_next = re.compile(
        r'<div class="card">\s*'
        r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*'
        r'<span></span>\s*'
        r'<a href="([^"]*)" class="tag">[^<]*下一章[^<]*</a>\s*'
        r'</div>\s*'
        r'</div>',
        re.DOTALL)

    for pat in [patA_full, patA_prev, patA_next]:
        m = pat.search(content)
        if m:
            content = pat.sub(new_nav, content)
            replaced = True
            break

    # ===== 模式A2: flex + text span + btn-primary next =====
    if not replaced:
        patA2 = re.compile(
            r'<div class="card">\s*'
            r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*'
            r'(?:<span style="[^"]*">[^<]*</span>\s*)?'
            r'<a href="([^"]*)" class="[^"]*btn-primary[^"]*">[^<]*下一章[^<]*</a>\s*'
            r'</div>\s*'
            r'</div>',
            re.DOTALL)
        m = patA2.search(content)
        if m:
            content = patA2.sub(new_nav, content)
            replaced = True

    # ===== 模式B: maharshi-gospel 章节导航 card =====
    if not replaced:
        patB = re.compile(
            r'(<!-- 章节导航 -->\s*)?'
            r'<div class="card">\s*'
            r'(?:<h2[^>]*>📚 章节导航</h2>\s*)?'
            r'(?:<div class="concept-tags">)?\s*'
            r'(?:<a href="([^"]*)" class="tag">← 上一章[^<]*</a>\s*)?'
            r'(?:<a href="([^"]*)" class="tag">[^<]*书籍首页[^<]*</a>\s*)?'
            r'(?:<a href="([^"]*)" class="tag">[^<]*返回书籍[^<]*</a>\s*)?'
            r'(?:<a href="([^"]*)" class="tag">[^<]*下一章[^<]*</a>\s*)?'
            r'(?:</div>\s*)?'
            r'</div>',
            re.DOTALL)
        m = patB.search(content)
        if m:
            content = patB.sub(new_nav, content)
            replaced = True

    # ===== 模式C: 无包裹的 <a class="tag">下一章 → =====
    if not replaced:
        # 只有下一章，无包裹
        patC_next = re.compile(
            r'<a href="([^"]*)" class="tag">[^<]*下一章[^<]*</a>\s*(?=\s*</div>\s*</main>)')
        m = patC_next.search(content)
        if m:
            content = patC_next.sub(new_nav, content)
            replaced = True

    # ===== 模式D: btn-primary/secondary =====
    if not replaced:
        # 上一章+下一章
        patD_full = re.compile(
            r'<a href="([^"]*)" class="[^"]*btn-secondary[^"]*">[^<]*</a>\s*'
            r'<a href="([^"]*)" class="[^"]*btn-primary[^"]*">[^<]*下一章[^<]*</a>')
        m = patD_full.search(content)
        if m:
            content = patD_full.sub(new_nav, content)
            replaced = True

    if not replaced:
        # 只有下一章 (btn-primary)
        patD_next = re.compile(
            r'<a href="([^"]*)" class="[^"]*btn-primary[^"]*">[^<]*下一章[^<]*</a>\s*(?=\s*</div>\s*</main>)')
        m = patD_next.search(content)
        if m:
            content = patD_next.sub(new_nav, content)
            replaced = True

    # ===== 模式E: talks-ch2/ch3 无导航，直接在 </main> 前插入 =====
    if not replaced:
        # 找 </main> 前一个 </div> 并在其前插入
        patE = re.compile(r'(\s*</div>\s*\n\s*</main>)')
        m = patE.search(content)
        if m:
            # 确认这个文件真的没有导航
            if '上一章' not in content and '下一章' not in content:
                content = patE.sub(new_nav + r'\1', content)
                replaced = True

    # ===== 模式F: btn-primary + text span (无包裹 prev+next) =====
    # <span>书名</span><a btn-primary>下一章 →
    if not replaced:
        patF_next = re.compile(
            r'<div class="card">\s*'
            r'(?:<span style="[^"]*">[^<]*</span>\s*)?'
            r'<a href="([^"]*)" class="[^"]*btn-primary[^"]*">[^<]*下一章[^<]*</a>\s*'
            r'</div>')
        m = patF_next.search(content)
        if m:
            content = patF_next.sub(new_nav, content)
            replaced = True

    # ===== 模式G: btn-secondary prev + text span (无flex) =====
    # <div class="card"><a btn-secondary>← 上一章</a><span>书名</span></div>
    if not replaced:
        patG_prev = re.compile(
            r'<div class="card">\s*'
            r'<a href="([^"]*)" class="[^"]*btn-secondary[^"]*">[^<]*上一章[^<]*</a>\s*'
            r'(?:<span style="[^"]*">[^<]*</span>\s*)?'
            r'</div>')
        m = patG_prev.search(content)
        if m:
            content = patG_prev.sub(new_nav, content)
            replaced = True

    # ===== 模式H: crumbs-ch4 flex prev-only =====
    # <div class="card"><div style="flex"><a btn-secondary>← 上一章</a><span>书名</span></div></div>
    if not replaced:
        patH = re.compile(
            r'<div class="card">\s*'
            r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*'
            r'<a href="([^"]*)" class="[^"]*btn-secondary[^"]*">[^<]*上一章[^<]*</a>\s*'
            r'(?:<span style="[^"]*">[^<]*</span>\s*)?'
            r'</div>\s*'
            r'</div>',
            re.DOTALL)
        m = patH.search(content)
        if m:
            content = patH.sub(new_nav, content)
            replaced = True

    if not replaced:
        return False, f'pattern not matched (ch{chapter_num})'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, f'ch{chapter_num} prev={prev_file} next={next_file}'

def main():
    files = sorted(glob.glob(f'{BOOKS_DIR}/*-ch*.html'))
    results = []
    for f in files:
        ok, msg = process_file(f)
        results.append((os.path.basename(f), ok, msg))

    for fname, ok, msg in results:
        status = '✅' if ok else '⏭️ '
        print(f'{status} {fname}: {msg}')

    fixed = sum(1 for _, ok, _ in results if ok)
    skipped = sum(1 for _, ok, _ in results if not ok)
    print(f'\n总计: {len(results)} 个, 修复 {fixed} 个, 跳过 {skipped} 个')

if __name__ == '__main__':
    main()
