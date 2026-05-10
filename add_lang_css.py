#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""添加语言切换按钮 CSS 到所有页面"""

import os
import re

def add_css_link(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    css_link = '<link rel="stylesheet" href="lang-toggle.css">'

    if 'lang-toggle.css' not in content:
        if '<link rel="stylesheet" href="styles.css">' in content:
            content = content.replace(
                '<link rel="stylesheet" href="styles.css">',
                '<link rel="stylesheet" href="styles.css">\n    ' + css_link
            )
        elif '<link rel="stylesheet" href="../styles.css">' in content:
            content = content.replace(
                '<link rel="stylesheet" href="../styles.css">',
                '<link rel="stylesheet" href="../styles.css">\n    ' + css_link
            )

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
                    add_css_link(filepath)
                    count += 1
                except Exception as e:
                    print(f"✗ Error: {filename} - {e}")

    print(f"添加 CSS 链接到 {count} 个文件")

if __name__ == '__main__':
    main()
