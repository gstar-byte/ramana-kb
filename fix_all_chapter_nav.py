#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 定义各书的章节结构
book_chapters = {
    'be-as-you-are': [(1, None, 2), (2, 1, 3), (3, 2, 4), (4, 3, 5), (5, 4, 6), (6, 5, 7), (7, 6, 8), (8, 7, 9), (9, 8, None)],
    'crumbs': [(1, None, 2), (2, 1, 3), (3, 2, 4), (4, 3, None)],
    'face-to-face': [(1, None, 2), (2, 1, 3), (3, 2, 4), (4, 3, 5), (5, 4, None)],
    'reflections': [(1, None, 2), (2, 1, None)],
    'spiritual-stories': [(1, None, 2), (2, 1, None)],
    'surpassing-love': [(1, None, 2), (2, 1, None)],
    'teachings': [(1, None, 2), (2, 1, None)],
    'timeless': [(1, None, 2), (2, 1, 3), (3, 2, 4), (4, 3, 5), (5, 4, 6), (6, 5, None)],
}

fixed_count = 0

for book, chapters in book_chapters.items():
    for ch_num, prev_ch, next_ch in chapters:
        f = f'{book}-ch{ch_num}.html'
        
        if not os.path.exists(f):
            continue
            
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 检查是否有乱码
        if '\x01' not in content and '\x02' not in content and '\x03' not in content and '\x04' not in content:
            continue
        
        # 构建新的导航HTML
        nav_parts = []
        if prev_ch:
            nav_parts.append(f'<a href="{book}-ch{prev_ch}.html" class="tag">🔹 上一章</a>')
        else:
            nav_parts.append('<span></span>')
        
        if next_ch:
            nav_parts.append(f'<a href="{book}-ch{next_ch}.html" class="tag">🔹 下一章</a>')
        else:
            nav_parts.append('<span></span>')
        
        new_nav = f'''<div style="display:flex;justify-content:space-between;align-items:center;">
                        {nav_parts[0]}
                        {nav_parts[1]}
                    </div>'''
        
        # 替换乱码导航 - 匹配各种可能的乱码模式
        # 模式1: \x01 ... \x02
        pattern1 = r'\x01\s*(<div style="display:flex;justify-content:space-between;align-items:center;">.*?<a href="[^"]*" class="tag">.*?</a>.*?</div>)\s*\x02'
        # 模式2: 直接替换整个导航区域
        pattern2 = r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="[^"]*" class="tag">[^<]*</a>\s*<a href="[^"]*" class="tag">[^<]*</a>\s*</div>'
        
        new_content = re.sub(pattern1, new_nav, content, flags=re.DOTALL)
        if new_content == content:
            new_content = re.sub(pattern2, new_nav, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'已修复: {f}')
            fixed_count += 1
        else:
            print(f'未修复: {f}')

print(f'\n共修复 {fixed_count} 个文件')
