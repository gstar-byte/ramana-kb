#!/usr/bin/env python3
"""修复子页面链接路径问题"""
import os
import re

def fix_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取当前文件相对于 pages 目录的路径
    rel_path = os.path.relpath(filepath, 'pages')
    depth = rel_path.count(os.sep) - 1  # 距离 pages 目录的深度
    
    # 基础前缀
    prefix = '../' * depth if depth > 0 else ''
    
    # 概念页面中的链接（同级目录下的 .html）
    # 例如在 concepts/whoami.html 中，核心概念的链接应该加 concepts/
    if '/concepts/' in filepath:
        # 核心概念列表链接
        content = re.sub(
            r'href="(atman|brahman|whoami|mind|ego|moksha|self|self-enquiry|silence|surrender|bhakti|japa|samadhi|jnana|jnani|karm|thoughts|maya|satchidananda|samsara|svasthya|awareness|heart|grace|guru|enlightenment|peace|fate|freewill|world)\.html"',
            r'href="concepts/\1.html"',
            content
        )
    
    # 人物页面中的链接
    if '/persons/' in filepath:
        content = re.sub(
            r'href="(ramana|david|venkataramana)\.html"',
            r'href="persons/\1.html"',
            content
        )
    
    # 书籍页面中的链接（章节页面中的书籍链接）
    if '/books/' in filepath:
        # 修复面包屑和页脚中的书籍链接
        content = re.sub(
            r'href="(be-as-you-are|gems|talks|back-to-heart|day-by-day|face-to-face|search-secret-india|maharshi-gospel|maha-yoga|guru-vachaka|timeless|teachings|surpassing-love|crumbs|reflections|spiritual-stories|collected-works)\.html"',
            r'href="books/\1.html"',
            content
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 遍历所有 HTML 文件
for root, dirs, files in os.walk('pages'):
    for f in files:
        if f.endswith('.html'):
            fix_links(os.path.join(root, f))

print("链接路径修复完成！")
