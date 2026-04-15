#!/usr/bin/env python3
"""修复 concepts/ 目录下的概念链接"""
import os

def fix_concepts_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 概念列表中的链接（sidebar 和 相关概念标签）
    # 修复类似 href="atman.html" 为 href="concepts/atman.html"
    import re
    
    # 在 sidebar-items 和 .tag 链接中
    # 需要添加 concepts/ 前缀
    
    old_content = content
    
    # 修复 sidebar-item 和 tag 链接中的概念链接
    # 这些链接应该在同一个目录下，但需要正确的目录前缀
    
    # 修复模式：href="xxx.html" 在 sidebar-items 或 tag class 后面
    # 需要变成 href="concepts/xxx.html"
    
    # 修复 sidebar 中的概念链接
    content = re.sub(
        r'(<div class="sidebar-items">.*?)<a href="(atman|brahman|whoami|mind|ego|moksha|self|self-enquiry|silence|surrender|bhakti|japa|samadhi|jnana|jnani|karm|thoughts|maya|satchidananda|samsara|svasthya|awareness|heart|grace|guru|enlightenment|peace|fate|freewill|world)\.html"',
        r'\1<a href="concepts/\2.html"',
        content,
        flags=re.DOTALL
    )
    
    # 修复 tag 链接
    content = re.sub(
        r'<a href="(atman|brahman|whoami|mind|ego|moksha|self|self-enquiry|silence|surrender|bhakti|japa|samadhi|jnana|jnani|karm|thoughts|maya|satchidananda|samsara|svasthya|awareness|heart|grace|guru|enlightenment|peace|fate|freewill|world)\.html" class="tag"',
        r'<a href="concepts/\1.html" class="tag"',
        content
    )
    
    # 修复 breadcrumb 中的概念链接
    content = re.sub(
        r'(核心概念.*?)href="(atman|brahman|whoami|mind|ego|moksha|self|self-enquiry|silence|surrender|bhakti|japa|samadhi|jnana|jnani|karm|thoughts|maya|satchidananda|samsara|svasthya|awareness|heart|grace|guru|enlightenment|peace|fate|freewill|world)\.html"',
        r'\1href="concepts/\2.html"',
        content,
        flags=re.DOTALL
    )
    
    if content != old_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    return False

# 修复 concepts/ 目录下的所有页面
fixed_count = 0
for f in os.listdir('pages/concepts'):
    if f.endswith('.html'):
        if fix_concepts_page(f'pages/concepts/{f}'):
            fixed_count += 1

print(f"修复了 {fixed_count} 个概念页面")
