#!/usr/bin/env python3
"""修复 persons/ 目录下的链接"""
import os
import re

def fix_persons_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_content = content
    
    # 修复 sidebar 中的链接
    content = re.sub(
        r'<a href="(ramana|david|venkataramana)\.html" class="sidebar-item',
        r'<a href="persons/\1.html" class="sidebar-item',
        content
    )
    
    # 修复 tag 链接
    content = re.sub(
        r'<a href="(ramana|david|venkataramana)\.html" class="tag"',
        r'<a href="persons/\1.html" class="tag"',
        content
    )
    
    # 修复 breadcrumb 中的链接
    content = re.sub(
        r'(人物索引.*?)href="(ramana|david|venkataramana)\.html"',
        r'\1href="persons/\2.html"',
        content,
        flags=re.DOTALL
    )
    
    if content != old_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    return False

# 修复 persons/ 目录下的所有页面
fixed_count = 0
for f in os.listdir('pages/persons'):
    if f.endswith('.html'):
        if fix_persons_page(f'pages/persons/{f}'):
            fixed_count += 1

print(f"修复了 {fixed_count} 个人物页面")
