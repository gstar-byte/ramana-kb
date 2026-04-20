#!/usr/bin/env python3
"""扫描所有书籍章节页的翻页导航样式"""
import os, glob

books_dir = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books'
files = sorted(glob.glob(f'{books_dir}/*-ch*.html'))

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    has_pagenav = 'class="page-nav"' in content
    has_card_nav = '<div class="card">' in content and ('上一章' in content or '下一章' in content)

    # 提取翻页文字
    prev_line, next_line = '', ''
    for line in content.split('\n'):
        if '上一章' in line:
            prev_line = line.strip()[:80]
        if '下一章' in line:
            next_line = line.strip()[:80]

    style = '✅ page-nav' if has_pagenav else ('⚠️ card-nav' if has_card_nav else '❓ unknown')
    print(f'{style} | {name} | 上一章:{prev_line[:50]} | 下一章:{next_line[:50]}')
