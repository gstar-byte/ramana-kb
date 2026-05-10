#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 canonical URL 格式问题"""

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 修复多余的 >
    content = re.sub(r'href="https://ramanamaharshi\.space/zh-TW/([^"]+)">>', r'href="https://ramanamaharshi.space/zh-TW/\1">', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    zh_tw = '/workspace/zh-TW'
    count = 0

    for root, dirs, files in os.walk(zh_tw):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                try:
                    fix_file(filepath)
                    count += 1
                except Exception as e:
                    print(f"✗ Error: {filename} - {e}")

    print(f"修复了 {count} 个文件的 canonical URL")

if __name__ == '__main__':
    main()
