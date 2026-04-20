#!/usr/bin/env python3
"""
修复 ch7-ch14 的 ul 列表样式，添加内联样式以匹配 ch6
"""
import os
import re

def fix_ul_style(filepath):
    """修复文件中的 ul 样式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 查找所有 <ul> 标签（没有 style 属性的）
    # 替换为带样式的 <ul>
    pattern = r'<ul>(?!\s*style)'
    replacement = '<ul style="margin:1rem 0 1rem 1.5rem;line-height:1.8;">'
    
    content = re.sub(pattern, replacement, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 修复 ch7-ch14
files_to_fix = [
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch7.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch8.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch9.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch10.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch11.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch12.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch13.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch14.html',
]

fixed_count = 0
for filepath in files_to_fix:
    if os.path.exists(filepath):
        fixed = fix_ul_style(filepath)
        if fixed:
            print(f"✅ 已修复: {os.path.basename(filepath)}")
            fixed_count += 1
        else:
            print(f"⏭️ 无需修复: {os.path.basename(filepath)}")
    else:
        print(f"❌ 文件不存在: {filepath}")

print(f"\n共修复 {fixed_count} 个文件")
