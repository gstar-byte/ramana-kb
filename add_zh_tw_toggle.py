#!/usr/bin/env python3
"""给 zh-TW 所有页面添加语言切换按钮"""

import os

def add_lang_toggle_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'lang-toggle' in content:
        return False

    toggle = '<a href="/" class="lang-toggle" title="切換為簡體中文">簡</a>'
    content = content.replace('<body>', f'<body>\n    {toggle}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    count = 0
    for root, dirs, files in os.walk('/workspace/zh-TW'):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if add_lang_toggle_to_file(filepath):
                    count += 1
    print(f"✅ 给 {count} 个繁体页面添加了语言切换按钮")

if __name__ == '__main__':
    main()
