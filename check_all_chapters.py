#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 检查所有章节文件
chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]

broken_nav = []
no_icon_concepts = []

for f in sorted(chapter_files):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查损坏的footer结构
    if '</div> class="site-footer">' in content:
        broken_nav.append(f)
    
    # 检查相关概念中是否有不带icon的tag
    # 查找 class="tag"> 后面直接跟文字而不是emoji的
    concept_section = re.search(r'相关概念.*?</div>\s*</div>', content, re.DOTALL)
    if concept_section:
        section = concept_section.group(0)
        # 查找没有emoji的tag
        tags = re.findall(r'class="tag">([^<]+)</a>', section)
        for tag in tags:
            # 检查是否以emoji开头（emoji的unicode范围）
            if tag and not any(ord(c) > 127 for c in tag[:2]):
                no_icon_concepts.append((f, tag))

print(f'损坏的导航: {len(broken_nav)} 个文件')
for f in broken_nav[:10]:
    print(f'  - {f}')

print(f'\n缺少icon的概念标签: {len(no_icon_concepts)} 个')
for f, tag in no_icon_concepts[:20]:
    print(f'  - {f}: {tag}')
