#!/usr/bin/env python3
"""
把所有书籍章节页的翻页导航统一替换为 page-nav 三栏风格（宝钻集风格）。
标准模板:
<div class="page-nav">
    <a href="书名-chN.html">
        <span class="nav-label">← 上一章</span>
        <span class="nav-title">第N章：章名</span>
    </a>
    <a href="书名.html">
        <span class="nav-label">返回书籍</span>
        <span class="nav-title">书名全书</span>
    </a>
    <a href="书名-chN.html">
        <span class="nav-label">下一章 →</span>
        <span class="nav-title">第N章：章名</span>
    </a>
</div>
"""
import re, os, glob

BOOKS_DIR = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books'

# 书籍元数据（书名->书籍文件名）
BOOKS = {
    'be-as-you-are':    {'title': '走向静默，如你本来', 'file': 'be-as-you-are.html'},
    'gems':             {'title': '宝钻集',            'file': 'gems.html'},
    'back-to-heart':    {'title': '回到你心中',          'file': 'back-to-heart.html'},
    'day-by-day':       {'title': '日日与彼',            'file': 'day-by-day.html'},
    'face-to-face':     {'title': '面对面',              'file': 'face-to-face.html'},
    'talks':            {'title': '对谈录',              'file': 'talks.html'},
    'maharshi-gospel':  {'title': '马哈希福音',          'file': 'maharshi-gospel.html'},
    'self-enquiry':     {'title': '自我参究',            'file': 'self-enquiry.html'},
    'crumbs':           {'title': '桌边碎语',            'file': 'crumbs.html'},
    'spiritual-stories': {'title': '灵性故事',           'file': 'spiritual-stories.html'},
    'surpassing-love':  {'title': '超越爱与恩典',        'file': 'surpassing-love.html'},
    'teachings':        {'title': '以言传意',            'file': 'teachings.html'},
    'timeless':         {'title': '时代中的永恒',        'file': 'timeless.html'},
    'search-secret':    {'title': '秘密印度',            'file': 'search-secret-india.html'},
}

def extract_chapter_num(filename):
    m = re.search(r'-ch(\d+)\.html', filename)
    return int(m.group(1)) if m else None

def get_chapter_title(filepath, chapter_num):
    """从文件内容中提取章节标题"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # 找 <h1> 或第一个大标题
        m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
        if m:
            title = m.group(1).strip()
            # 去掉书名前缀
            for book_prefix in ['走向静默，如你本来 ', '宝钻集 ', '回到你心中 ', '日日与彼 ',
                                '面对面 ', '对谈录 ', '马哈希福音 ', '自我参究 ',
                                '桌边碎语 ', '灵性故事 ', '超越爱与恩典 ', '以言传意 ',
                                '时代中的永恒 ', '秘密印度 ']:
                if title.startswith(book_prefix):
                    title = title[len(book_prefix):]
                    break
            return title
    except:
        pass
    return f'第{chapter_num}章'

def build_nav(book_key, chapter_num, prev_file, next_file, book_html, prev_title, next_title):
    """生成 page-nav HTML"""
    book_meta = BOOKS.get(book_key, {})
    book_title = book_meta.get('title', book_key)
    book_file = book_meta.get('file', f'{book_key}.html')

    prev_html = ''
    if prev_file:
        prev_label = f'← 上一章'
        prev_html = f'''<a href="{prev_file}">
                        <span class="nav-label">{prev_label}</span>
                        <span class="nav-title">{prev_title}</span>
                    </a>'''
    else:
        prev_html = '<span></span>'

    book_html = f'''<a href="{book_file}">
                        <span class="nav-label">返回书籍</span>
                        <span class="nav-title">{book_title}全书</span>
                    </a>'''

    next_html = ''
    if next_file:
        next_label = f'下一章 →'
        next_html = f'''<a href="{next_file}">
                        <span class="nav-label">{next_label}</span>
                        <span class="nav-title">{next_title}</span>
                    </a>'''
    else:
        next_html = '<span></span>'

    return f'''
                <div class="page-nav">
                    {prev_html}
                    {book_html}
                    {next_html}
                </div>'''

def process_file(filepath):
    filename = os.path.basename(filepath)

    # 识别书籍key
    book_key = None
    for key in BOOKS:
        if filename.startswith(key + '-ch'):
            book_key = key
            break
    if not book_key:
        return False, 'unknown book'

    chapter_num = extract_chapter_num(filename)
    if not chapter_num:
        return False, 'no chapter number'

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已经是 page-nav
    if 'class="page-nav"' in content:
        return False, 'already page-nav'

    # 提取所有同书章节
    all_chapters = []
    for f in glob.glob(f'{BOOKS_DIR}/{book_key}-ch*.html'):
        n = extract_chapter_num(os.path.basename(f))
        if n:
            all_chapters.append((n, os.path.basename(f), f))

    all_chapters.sort(key=lambda x: x[0])
    chapter_nums = [c[0] for c in all_chapters]

    prev_info = None
    next_info = None
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

    # 查找并替换导航区块
    # 常见模式：<div class="card">...上一章...下一章...</div>
    # 或者只有上一章/只有下一章的情况
    patterns_to_try = [
        # 完整的两栏布局
        re.compile(
            r'<div class="card">\s*<div style="display:flex;justify-content:space-between;[^"]*">\s*'
            r'<a href="[^"]*" class="tag">[^<]*上一章[^<]*</a>\s*'
            r'<a href="[^"]*" class="tag">[^<]*下一章[^<]*</a>\s*'
            r'</div>\s*</div>',
            re.DOTALL
        ),
        # 只有下一章
        re.compile(
            r'<div class="card">\s*<div style="display:flex;justify-content:space-between;[^"]*">\s*'
            r'(?:<a href="[^"]*" class="tag">[^<]*</a>\s*)?'
            r'<a href="([^"]*)" class="tag">[^<]*下一章[^<]*</a>\s*'
            r'</div>\s*</div>',
            re.DOTALL
        ),
        # 只有上一章
        re.compile(
            r'<div class="card">\s*<div style="display:flex;justify-content:space-between;[^"]*">\s*'
            r'<a href="([^"]*)" class="tag">[^<]*上一章[^<]*</a>\s*'
            r'</div>\s*</div>',
            re.DOTALL
        ),
        # btn-primary / btn-secondary 风格
        re.compile(
            r'<div class="card">\s*<div style="display:flex;justify-content:space-between;[^"]*">\s*'
            r'<a href="([^"]*)" class="[^"]*btn-secondary[^"]*">[^<]*</a>\s*'
            r'<a href="([^"]*)" class="[^"]*btn-primary[^"]*">[^<]*下一章[^<]*</a>\s*'
            r'</div>\s*</div>',
            re.DOTALL
        ),
        # btn-primary 只有下一章
        re.compile(
            r'<div style="text-align:center;[^"]*">\s*'
            r'<a href="([^"]*)" class="btn-primary">[^<]*下一章[^<]*</a>\s*'
            r'</div>',
            re.DOTALL
        ),
        # 只有下一章 (tag风格，无card包裹)
        re.compile(
            r'<div style="[^"]*">\s*'
            r'<a href="([^"]*)" class="tag">[^<]*下一章[^<]*</a>\s*'
            r'</div>',
            re.DOTALL
        ),
    ]

    new_nav = build_nav(book_key, chapter_num, prev_file, next_file,
                       BOOKS.get(book_key, {}).get('file', ''),
                       prev_title, next_title)

    replaced = False
    for pat in patterns_to_try:
        new_content = pat.sub(new_nav, content)
        if new_content != content:
            content = new_content
            replaced = True
            break

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
    print(f'\n总计: {len(results)} 个文件, 修复 {fixed} 个')

if __name__ == '__main__':
    main()
