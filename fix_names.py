#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复繁体版本中的问题"""

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 修复人名
    content = re.sub(r'馬雜湊', '馬哈希', content)
    content = re.sub(r'馬杂湊', '馬哈希', content)

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

    print(f"修复了 {count} 个文件")

if __name__ == '__main__':
    main()
