#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# be-as-you-are 章节修复
chapters = [
    (1, None, 2),      # ch1: 无上一章, 下一章=ch2
    (2, 1, 3),
    (3, 2, 4),
    (4, 3, 5),
    (5, 4, 6),
    (6, 5, 7),
    (7, 6, 8),
    (8, 7, 9),
    (9, 8, None),      # ch9: 上一章=ch8, 无下一章
]

for ch_num, prev_ch, next_ch in chapters:
    f = f'be-as-you-are-ch{ch_num}.html'
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 构建新的导航HTML
    nav_parts = []
    if prev_ch:
        nav_parts.append(f'<a href="be-as-you-are-ch{prev_ch}.html" class="tag">🔹 上一章</a>')
    else:
        nav_parts.append('<span></span>')  # 占位
    
    if next_ch:
        nav_parts.append(f'<a href="be-as-you-are-ch{next_ch}.html" class="tag">🔹 下一章</a>')
    else:
        nav_parts.append('<span></span>')  # 占位
    
    new_nav = f'''<div style="display:flex;justify-content:space-between;align-items:center;">
                        {nav_parts[0]}
                        {nav_parts[1]}
                    </div>'''
    
    # 匹配没有 <!-- 章节导航 --> 注释的导航
    pattern = r'(<div class="card">)\s*<div style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="[^"]*" class="tag">[^<]*</a>\s*<a href="[^"]*" class="tag">[^<]*</a>\s*</div>\s*(</div>\s*</div>\s*<footer)'
    
    replacement = f'\1\n                    {new_nav}\n                \2'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'已修复: {f}')
    else:
        print(f'未匹配: {f}')

print('\n修复完成!')
