#!/usr/bin/env python3
"""修复 concepts 目录下页面的侧边栏链接"""
import os
import re

concepts_dir = 'pages/concepts'

# 获取所有概念文件
concept_files = []
for f in os.listdir(concepts_dir):
    if f.endswith('.html') and f != 'index.html':
        concept_files.append(f)

print(f"找到 {len(concept_files)} 个概念页面")

# 修复每个文件中的侧边栏链接
fixed_count = 0
for filename in concept_files:
    filepath = os.path.join(concepts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 修复侧边栏中的相对链接 (mind.html -> concepts/mind.html)
    # 但要排除 index.html，因为它应该在当前目录
    content = re.sub(
        r'(<a href=")(?!index\.html|../)([a-z\-]+\.html)(")',
        r'\1concepts/\2\3',
        content
    )
    
    # 修复面包屑中的链接
    content = re.sub(
        r'(<a href=")(../index\.html|index\.html)(">核心概念</a>)',
        r'<a href="index.html">核心概念</a>',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1
        print(f"修复: {filename}")

print(f"\n总共修复了 {fixed_count} 个文件")
