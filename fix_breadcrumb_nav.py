#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 定义各书的章节结构
book_chapters = {
    'crumbs': [(1, None, 2), (2, 1, 3), (3, 2, 4), (4, 3, None)],
    'reflections': [(1, None, 2), (2, 1, None)],
    'spiritual-stories': [(1, None, 2), (2, 1, None)],
    'surpassing-love': [(1, None, 2), (2, 1, None)],
    'teachings': [(1, None, 2), (2, 1, None)],
    'timeless': [(1, None, 2), (2, 1, 3), (3, 2, 4), (4, 3, 5), (5, 4, 6), (6, 5, None)],
}

# 书籍标题映射
book_titles = {
    'crumbs': '桌边碎语',
    'reflections': '反思录',
    'spiritual-stories': '灵性故事',
    'surpassing-love': '超越爱与恩典',
    'teachings': '以言传意',
    'timeless': '时代中的永恒',
}

fixed_count = 0

for book, chapters in book_chapters.items():
    book_title = book_titles.get(book, book)
    
    for ch_num, prev_ch, next_ch in chapters:
        f = f'{book}-ch{ch_num}.html'
        
        if not os.path.exists(f):
            continue
            
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 检查是否有乱码
        if '\x01' not in content and '\x02' not in content and '\x03' not in content and '\x04' not in content:
            continue
        
        # 修复面包屑导航中的乱码
        # 模式: <span style="color:var(--text-muted);">\x01</span>
        content = re.sub(r'<span style="color:var\(--text-muted\);">\x01</span>', 
                        f'<span style="color:var(--text-muted);">{book_title}</span>', content)
        content = re.sub(r'<span style="color:var\(--text-muted\);">\x03</span>', 
                        f'<span style="color:var(--text-muted);">{book_title}</span>', content)
        
        # 修复章节导航链接中的乱码
        # 模式1: 第一章 (只有下一章)
        if prev_ch is None and next_ch:
            content = re.sub(
                r'<a href="\x02" class="btn-primary">\x03</a>',
                f'<a href="{book}-ch{next_ch}.html" class="btn-primary">下一章 →</a>',
                content
            )
        # 模式2: 最后一章 (只有上一章)
        elif prev_ch and next_ch is None:
            content = re.sub(
                r'<a href="\x01" class="btn-secondary">\x02</a>',
                f'<a href="{book}-ch{prev_ch}.html" class="btn-secondary">← 上一章</a>',
                content
            )
            content = re.sub(
                r'<span style="color:var\(--text-muted\);">\x03</span>',
                '<span></span>',
                content
            )
        # 模式3: 中间章节 (有上一章和下一章)
        elif prev_ch and next_ch:
            content = re.sub(
                r'<a href="\x01" class="btn-secondary">\x02</a>',
                f'<a href="{book}-ch{prev_ch}.html" class="btn-secondary">← 上一章</a>',
                content
            )
            content = re.sub(
                r'<a href="\x03" class="btn-primary">\x04</a>',
                f'<a href="{book}-ch{next_ch}.html" class="btn-primary">下一章 →</a>',
                content
            )
        
        # 保存
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f'已修复: {f}')
        fixed_count += 1

print(f'\n共修复 {fixed_count} 个文件')
