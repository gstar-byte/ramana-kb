#!/usr/bin/env python3
"""给全站所有页面添加语言切换按钮"""

import os

def add_lang_toggle(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'lang-toggle' in content:
        return False

    is_zh_tw = '/zh-TW/' in filepath

    if is_zh_tw:
        toggle = '<a href="/" class="lang-toggle" title="切換為簡體中文">簡</a>'
    else:
        toggle = '<a href="/zh-TW/" class="lang-toggle" title="切換為繁體中文">繁</a>'

    content = content.replace('<body>', f'<body>\n    {toggle}')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    print("=== 添加语言切换按钮 ===")

    # 简体版
    zh_cn_count = 0
    for root, dirs, files in os.walk('/workspace/pages'):
        if 'zh-TW' in root:
            continue
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if add_lang_toggle(filepath):
                    zh_cn_count += 1
    print(f"简体版: 添加了 {zh_cn_count} 个按钮")

    # 繁体版
    zh_tw_count = 0
    for root, dirs, files in os.walk('/workspace/pages/zh-TW'):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if add_lang_toggle(filepath):
                    zh_tw_count += 1
    print(f"繁体版: 添加了 {zh_tw_count} 个按钮")

    print("\n完成！")

if __name__ == '__main__':
    main()
