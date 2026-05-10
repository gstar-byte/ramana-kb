#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
繁体中文转换脚本 v3
使用 OpenCC 进行繁简转换，并按台湾习惯处理
"""

import os
import re
import shutil
from opencc import OpenCC

# 初始化 OpenCC
cc = OpenCC('s2twp')

def convert_text(text):
    """转换文本内容"""
    return cc.convert(text)

def copy_and_convert_html(src_path, dst_path):
    """复制并转换单个 HTML 文件"""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换语言属性
    content = content.replace('lang="zh-CN"', 'lang="zh-TW"')
    content = content.replace("lang='zh-CN'", "lang='zh-TW'")

    # 替换 og:locale
    content = content.replace('og:locale" content="zh_CN"', 'og:locale" content="zh_TW"')

    # 替换 JSON-LD 中的语言
    content = content.replace('"inLanguage": "zh-CN"', '"inLanguage": "zh-TW"')

    # 替换内部链接
    def replace_href_src(match):
        url = match.group(1)
        # 只处理相对路径的内部链接
        if url.startswith('/pages/') and not url.startswith('/pages/icons'):
            # books/index.html -> /zh-TW/pages/books/index.html
            url = '/zh-TW/' + url
        elif url.startswith('/') and not url.startswith('/zh-TW') and not url.startswith('/pages/icons') and not url.startswith('/styles') and not url.startswith('/app.js') and not url.startswith('/manifest') and not url.startswith('/sw.js') and not url.startswith('/search.js') and not url.startswith('/graph') and not url.startswith('/sitemap') and not url.startswith('/robots'):
            # /about.html -> /zh-TW/about.html
            url = '/zh-TW' + url
        return match.group(0).replace(match.group(1), url)

    content = re.sub(r'href="([^"]*)"', replace_href_src, content)
    content = re.sub(r"href='([^']*)'", replace_href_src, content)
    content = re.sub(r'src="([^"]*)"', replace_href_src, content)

    # 提取并转换可见文本
    result = []
    i = 0
    in_script = False
    in_style = False
    in_textarea = False

    while i < len(content):
        # 检查特殊标签
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

        if content[i] == '>':
            result.append(content[i])
            i += 1
            continue

        # 收集文本块
        text_chunk = content[i]
        while i + 1 < len(content) and content[i + 1] != '<':
            text_chunk += content[i + 1]
            i += 1

        result.append(convert_text(text_chunk))
        i += 1

    return ''.join(result)

def process_directory(src_dir, dst_dir, prefix=''):
    """递归处理目录"""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    count = 0

    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        if rel_path == '.':
            dst_subdir = dst_dir
        else:
            dst_subdir = os.path.join(dst_dir, rel_path)

        if not os.path.exists(dst_subdir):
            os.makedirs(dst_subdir)

        for filename in files:
            src_file = os.path.join(root, filename)

            if filename.endswith('.html') or filename.endswith('.htm'):
                dst_file = os.path.join(dst_subdir, filename)
                try:
                    converted = copy_and_convert_html(src_file, dst_file)
                    with open(dst_file, 'w', encoding='utf-8') as f:
                        f.write(converted)
                    count += 1
                    print(f"  ✓ {rel_path}/{filename}" if rel_path != '.' else f"  ✓ {filename}")
                except Exception as e:
                    print(f"  ✗ Error: {filename} - {e}")
            else:
                dst_file = os.path.join(dst_subdir, filename)
                shutil.copy2(src_file, dst_file)

    return count

def main():
    src_dir = '/workspace'
    zh_tw_dir = '/workspace/zh-TW'

    print("=" * 50)
    print("繁体中文转换 v3")
    print("=" * 50)

    # 测试转换
    test_text = "知识库系统整理灵性教示，包含经典著作完整导读"
    print(f"\n转换测试: {test_text}")
    print(f"  → {convert_text(test_text)}")

    # 复制静态文件到根目录
    print("\n[1] 复制静态文件...")
    static_files = [
        'styles.css', 'app.js', 'manifest.json', 'sw.js', 'pwa-analytics.js',
        'search.js', 'd3.min.js', 'robots.txt', 'sitemap.xml', 'graph.html', 'sitemap.html'
    ]

    for f in static_files:
        src = os.path.join(src_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(zh_tw_dir, f))

    print(f"  ✓ {len(static_files)} static files")

    # 复制 public 目录
    public_src = os.path.join(src_dir, 'public')
    public_dst = os.path.join(zh_tw_dir, 'public')
    if os.path.exists(public_src):
        shutil.copytree(public_src, public_dst, dirs_exist_ok=True)
        print("  ✓ public/")

    # 处理根目录的 index.html
    print("\n[2] 处理 index.html...")
    index_src = os.path.join(src_dir, 'index.html')
    index_dst = os.path.join(zh_tw_dir, 'index.html')
    if os.path.exists(index_src):
        converted = copy_and_convert_html(index_src, index_dst)
        with open(index_dst, 'w', encoding='utf-8') as f:
            f.write(converted)
        print("  ✓ index.html")

    # 处理 pages 目录
    print("\n[3] 转换页面文件...")
    pages_src = os.path.join(src_dir, 'pages')
    pages_dst = os.path.join(zh_tw_dir, 'pages')
    count = process_directory(pages_src, pages_dst)

    print(f"\n总计转换 {count} 个 HTML 文件")
    print("\n" + "=" * 50)
    print("转换完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
