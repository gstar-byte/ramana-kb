#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 检查所有章节文件
chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]

for f in sorted(chapter_files):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 查找乱码
    garbage_chars = []
    for i, c in enumerate(content):
        if ord(c) < 32 and c not in '\n\r\t':
            garbage_chars.append((i, repr(c), ord(c)))
    
    if garbage_chars:
        print(f'{f}: {len(garbage_chars)} 个乱码字符')
        for pos, char_repr, ord_val in garbage_chars[:3]:  # 只显示前3个
            context = content[max(0,pos-30):pos+30]
            print(f'  位置{pos}: {char_repr} -> {repr(context)}')
        print()
