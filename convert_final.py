#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
繁体中文转换脚本 - 最终版
"""

import os
import re
import shutil
from opencc import OpenCC

cc = OpenCC('s2twp')

PRESERVE_TERMS = {
    '馬雜湊': '馬哈希',
    '馬哈希': '馬哈希',
    '馬杂湊': '馬哈希',
}

def convert_text(text):
    return cc.convert(text)

def copy_and_convert_html(src_path, dst_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('lang="zh-CN"', 'lang="zh-TW"')
    content = content.replace("lang='zh-CN'", "lang='zh-TW'")
    content = content.replace('og:locale" content="zh_CN"', 'og:locale" content="zh_TW"')
    content = content.replace('"inLanguage": "zh-CN"', '"inLanguage": "zh-TW"')

    def replace_href_src(match):
        url = match.group(1)
        if url.startswith('/pages/') and not url.startswith('/pages/icons'):
            url = '/zh-TW/' + url[7:]
        elif url.startswith('/') and not url.startswith('/zh-TW') and not url.startswith('/pages/icons'):
            url = '/zh-TW' + url
        return match.group(0).replace(match.group(1), url)

    content = re.sub(r'href="([^"]*)"', replace_href_src, content)
    content = re.sub(r"href='([^']*)'", replace_href_src, content)
    content = re.sub(r'src="([^"]*)"', replace_href_src, content)

    result = []
    i = 0
    in_script = False
    in_style = False
    in_textarea = False

    while i < len(content):
        if i + 1 < len(content):
            snippet = content[i:i+8].lower()
            if snippet.startswith('<script'):
                in_script = True
                result.append(content[i:i+7])
                i += 7
                continue
            elif snippet.startswith('</script'):
                in_script = False
                result.append(content[i:i+9])
                i += 9
                continue
            elif content[i:i+6].lower() == '<style':
                in_style = True
                result.append(content[i:i+6])
                i += 6
                continue
            elif content[i:i+7].lower() == '</style':
                in_style = False
                result.append(content[i:i+8])
                i += 8
                continue
            elif content[i:i+9].lower() == '<textarea':
                in_textarea = True
                result.append(content[i:i+9])
                i += 9
                continue
            elif content[i:i+10].lower() == '</textarea':
                in_textarea = False
                result.append(content[i:i+11])
                i += 11
                continue

        if in_script or in_style or in_textarea:
            result.append(content[i])
            i += 1
            continue

        if content[i] == '<':
            tag_end = content.find('>', i)
            if tag_end != -1:
                result.append(content[i:tag_end+1])
                i = tag_end + 1
                continue

        text_chunk = content[i]
        while i + 1 < len(content) and content[i + 1] != '<':
            text_chunk += content[i + 1]
            i += 1

        result.append(convert_text(text_chunk))
        i += 1

    content = ''.join(result)

    for wrong, correct in PRESERVE_TERMS.items():
        content = content.replace(wrong, correct)

    return content

def add_seo_tags(content, filepath):
    """添加 hreflang 和语言切换按钮"""

    is_zh_tw = '/zh-TW/' in filepath

    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    if canonical_match:
        current_url = canonical_match.group(1)
        if is_zh_tw and '/zh-TW' not in current_url:
            if current_url.startswith('/'):
                current_url = '/zh-TW' + current_url
            else:
                current_url = current_url.replace('ramanamaharshi.space/', 'ramanamaharshi.space/zh-TW/')
            content = content.replace(
                canonical_match.group(0),
                f'<link rel="canonical" href="{current_url}">'
            )

    if '<link rel="alternate" hreflang' not in content:
        zh_tw_url = 'https://ramanamaharshi.space/zh-TW/'
        zh_cn_url = 'https://ramanamaharshi.space/'

        if is_zh_tw:
            hreflang_tags = f'''
    <link rel="alternate" hreflang="zh-TW" href="{zh_tw_url}">
    <link rel="alternate" hreflang="zh-CN" href="{zh_cn_url}">'''
        else:
            hreflang_tags = f'''
    <link rel="alternate" hreflang="zh-CN" href="{zh_cn_url}">
    <link rel="alternate" hreflang="zh-TW" href="{zh_tw_url}">'''

        content = content.replace('</head>', hreflang_tags + '\n</head>')

    if 'lang-toggle' not in content:
        if is_zh_tw:
            toggle_html = '<a href="/" class="lang-toggle" title="切换为简体中文">简</a>'
        else:
            toggle_html = '<a href="/zh-TW/" class="lang-toggle" title="切換為繁體中文">繁</a>'

        content = content.replace('<body>', f'<body>\n    {toggle_html}')

    return content

def process_file(src_file, dst_file):
    converted = copy_and_convert_html(src_file, dst_file)
    converted = add_seo_tags(converted, dst_file)
    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(converted)

def main():
    src_pages = '/workspace/pages'
    zh_tw_pages = '/workspace/zh-TW'

    print("=" * 50)
    print("繁体中文转换 - 最终版")
    print("=" * 50)

    test = convert_text("马哈希知识库")
    print(f"\n转换测试: 马哈希知识库 → {test}")

    print("\n[1] 复制静态文件...")
    static_files = [
        'styles.css', 'app.js', 'manifest.json', 'sw.js', 'pwa-analytics.js',
        'search.js', 'd3.min.js', 'robots.txt', 'sitemap.xml', 'graph.html',
        'sitemap.html', 'vercel.json'
    ]
    for f in static_files:
        src = os.path.join(src_pages, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(zh_tw_pages, f))

    print(f"  ✓ {len(static_files)} files")

    print("\n[2] 转换页面...")

    count = 0
    for root, dirs, files in os.walk(src_pages):
        rel_path = os.path.relpath(root, src_pages)
        dst_dir = os.path.join(zh_tw_pages, rel_path) if rel_path != '.' else zh_tw_pages

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for filename in files:
            src_file = os.path.join(root, filename)

            if filename.endswith('.html') or filename.endswith('.htm'):
                dst_file = os.path.join(dst_dir, filename)
                try:
                    process_file(src_file, dst_file)
                    count += 1
                except Exception as e:
                    print(f"  ✗ Error: {filename} - {e}")
            else:
                dst_file = os.path.join(dst_dir, filename)
                shutil.copy2(src_file, dst_file)

    print(f"\n总计转换 {count} 个文件")
    print("\n" + "=" * 50)
    print("转换完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
