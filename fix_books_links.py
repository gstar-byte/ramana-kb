#!/usr/bin/env python3
"""修复 books/ 目录下的链接"""
import os
import re

def fix_books_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_content = content
    
    # 书籍名称列表
    books = [
        'be-as-you-are', 'gems', 'talks', 'back-to-heart', 'day-by-day',
        'face-to-face', 'search-secret-india', 'maharshi-gospel', 'maha-yoga',
        'guru-vachaka', 'timeless', 'teachings', 'surpassing-love', 'crumbs',
        'reflections', 'spiritual-stories', 'collected-works'
    ]
    books_pattern = '|'.join(books)
    
    # 修复 sidebar-item 中的书籍链接
    content = re.sub(
        rf'<a href="({books_pattern})\.html" class="sidebar-item',
        r'<a href="books/\1.html" class="sidebar-item',
        content
    )
    
    # 修复 tag 链接
    content = re.sub(
        rf'<a href="({books_pattern})\.html" class="tag"',
        r'<a href="books/\1.html" class="tag"',
        content
    )
    
    # 修复 breadcrumb 中的链接
    content = re.sub(
        rf'(href=")({books_pattern})\.html"',
        r'\1books/\2.html"',
        content
    )
    
    # 修复页脚中的链接
    content = re.sub(
        rf'(← 返回.*?<a href=")({books_pattern})\.html"',
        r'\1books/\2.html"',
        content,
        flags=re.DOTALL
    )
    
    if content != old_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    return False

# 修复 books/ 目录下的所有页面
fixed_count = 0
for root, dirs, files in os.walk('pages/books'):
    for f in files:
        if f.endswith('.html'):
            if fix_books_page(os.path.join(root, f)):
                fixed_count += 1

print(f"修复了 {fixed_count} 个书籍页面")
