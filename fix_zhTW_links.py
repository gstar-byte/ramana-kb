#!/usr/bin/env python3
"""修复 zh-TW 内部链接路径"""

import os
import re

def fix_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 修复 href 和 src 中的路径
    # /zh-TW/books/ -> /zh-TW/books/ (保持不变，因为是相对路径)
    # href="lang-toggle.css" -> 正确
    # href="../styles.css" -> 需要检查

    # 修复相对路径引用
    if '/zh-TW/pages/' in content:
        content = content.replace('/zh-TW/pages/', '/pages/')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    zh_tw_dir = '/workspace/pages/zh-TW'
    count = 0

    for root, dirs, files in os.walk(zh_tw_dir):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if fix_links(filepath):
                    print(f"✓ Fixed: {os.path.relpath(filepath, zh_tw_dir)}")
                    count += 1

    print(f"\n修复了 {count} 个文件")

if __name__ == '__main__':
    main()
