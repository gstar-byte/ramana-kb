#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复繁体转换脚本
1. 修复人名转换错误
2. 添加 hreflang 标签
3. 修复 canonical URL
4. 添加语言切换按钮
"""

import os
import re
from opencc import OpenCC

cc = OpenCC('s2twp')

# 需要保留原样或特殊转换的人名/术语
PRESERVE_TERMS = {
    # 核心人名
    '馬雜湊': '馬哈希',
    '馬哈希': '馬哈希',
    '拉瑪那': '拉瑪那',
    '室利·拉瑪那·馬哈希': '室利·拉瑪那·馬哈希',
    '室利·拉瑪那·馬雜湊': '室利·拉瑪那·馬哈希',
    '拉瑪那·馬哈希': '拉瑪那·馬哈希',
    '拉瑪那·馬雜湊': '拉瑪那·馬哈希',

    # 大卫·高德曼
    '大衛·高德曼': '大衛·高德曼',
    '大衛 高德曼': '大衛·高德曼',

    # 韦卡罗达·南达
    '韋卡羅達·南達': '韋卡羅達·南達',
    '韦卡罗达·南达': '韋卡羅達·南達',

    # 书名中的马哈希
    '《馬雜湊福音》': '《馬哈希福音》',
    '《马哈希福音》': '《馬哈希福音》',
}

def fix_content(content):
    """修复转换后的内容"""

    # 1. 修复人名错误
    for wrong, correct in PRESERVE_TERMS.items():
        content = content.replace(wrong, correct)

    # 2. 修复马哈希相关
    content = re.sub(r'馬雜湊', '馬哈希', content)
    content = re.sub(r'馬杂湊', '馬哈希', content)

    return content

def add_hreflang_and_toggle(content, is_zh_tw=True):
    """添加 hreflang 标签和语言切换按钮"""

    lang_code = 'zh-TW' if is_zh_tw else 'zh-CN'
    alt_lang = 'zh-CN' if is_zh_tw else 'zh-TW'
    alt_url_prefix = '' if is_zh_tw else '/zh-TW'
    current_url_prefix = '/zh-TW' if is_zh_tw else ''

    # hreflang 标签
    hreflang_self = f'<link rel="alternate" hreflang="{lang_code}" href="https://ramanamaharshi.space{current_url_prefix}/">'
    hreflang_alt = f'<link rel="alternate" hreflang="{alt_lang}" href="https://ramanamaharshi.space{alt_url_prefix}/">'

    # 提取当前页面的相对路径
    canonical_match = re.search(r'<link rel="canonical" href="https://ramanamaharshi\.space([^"]+)"', content)
    if canonical_match:
        current_path = canonical_match.group(1)
        alt_path = '/zh-TW' + current_path if not is_zh_tw else current_path.replace('/zh-TW', '')
        if not is_zh_tw and not alt_path.startswith('/'):
            alt_path = '/' + alt_path

        hreflang_self = f'<link rel="alternate" hreflang="{lang_code}" href="https://ramanamaharshi.space{current_path}">'
        hreflang_alt = f'<link rel="alternate" hreflang="{alt_lang}" href="https://ramanamaharshi.space{alt_path}">'

    # 语言切换按钮 HTML
    toggle_html = f'''
    <a href="{alt_path if 'alt_path' in dir() else '/zh-TW/'}" class="lang-toggle" title="切換為{alt_lang}版本">{alt_lang.split('-')[1]}</a>
    '''

    # 添加到 </head> 之前
    if '<link rel="alternate" hreflang' not in content:
        content = content.replace('</head>', f'{hreflang_self}\n    {hreflang_alt}\n</head>')

    # 添加语言切换按钮到 body 开头
    if 'lang-toggle' not in content:
        content = content.replace('<body>', f'<body>\n    {toggle_html}')

    return content

def fix_canonical_url(content, is_zh_tw=True):
    """修复 canonical URL"""

    prefix = '/zh-TW' if is_zh_tw else ''

    # 替换 canonical URL
    def replace_canonical(match):
        url = match.group(1)
        if is_zh_tw:
            # zh-TW 版本的 canonical 应该指向 zh-TW 版本
            if '/zh-TW' not in url:
                if url.startswith('/'):
                    url = '/zh-TW' + url
                else:
                    url = url.replace('ramanamaharshi.space/', 'ramanamaharshi.space/zh-TW/')
        return match.group(0).replace(match.group(1), url)

    content = re.sub(r'<link rel="canonical" href="([^"]+)"', replace_canonical, content)

    return content

def process_file(filepath):
    """处理单个 HTML 文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否是 zh-TW 版本
    is_zh_tw = '/zh-TW/' in filepath or filepath.endswith('/zh-TW/index.html')

    # 1. 修复内容
    content = fix_content(content)

    # 2. 修复 canonical URL
    content = fix_canonical_url(content, is_zh_tw)

    # 3. 添加 hreflang 和语言切换按钮
    content = add_hreflang_and_toggle(content, is_zh_tw)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    zh_tw_dir = '/workspace/zh-TW'

    print("=" * 50)
    print("修复繁体版本")
    print("=" * 50)

    count = 0

    for root, dirs, files in os.walk(zh_tw_dir):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                try:
                    process_file(filepath)
                    count += 1
                    print(f"✓ {os.path.relpath(filepath, zh_tw_dir)}")
                except Exception as e:
                    print(f"✗ Error: {filename} - {e}")

    print(f"\n总计修复 {count} 个文件")
    print("\n" + "=" * 50)
    print("修复完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
