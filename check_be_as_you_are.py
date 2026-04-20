#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 检查 be-as-you-are 章节
for i in range(1, 10):
    f = f'be-as-you-are-ch{i}.html'
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 检查导航链接
        nav_match = re.search(r'<a href="([^"]+)" class="tag">🔹 ([^<]+)</a>', content)
        if nav_match:
            print(f'{f}: href={repr(nav_match.group(1))}, text={repr(nav_match.group(2))}')
        else:
            # 尝试找乱码链接
            bad_nav = re.search(r'<a href="([^"]+)" class="tag">', content)
            if bad_nav:
                print(f'{f}: 乱码链接={repr(bad_nav.group(1))}')
            else:
                print(f'{f}: 未找到导航链接')
