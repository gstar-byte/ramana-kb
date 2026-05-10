#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
繁体中文转换脚本 v2
使用 OpenCC 进行繁简转换，并按台湾习惯处理
"""

import os
import re
import shutil
from opencc import OpenCC

# 初始化 OpenCC (使用台湾繁体配置)
cc = OpenCC('s2twp')  # 简体到繁体（台湾习惯，含常用词转换）

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

    # 替换 canonical URL - 简体版指向繁体版
    def replace_canonical_src(match):
        url = match.group(1)
        if 'ramanamaharshi.space' in url and '/zh-TW' not in url:
            url = url.replace('ramanamaharshi.space/', 'ramanamaharshi.space/zh-TW/')
        elif url.startswith('/') and not url.startswith('/zh-TW'):
            url = '/zh-TW' + url
        return match.group(0).replace(match.group(1), url)

    # 替换 href 和 src 中的内部链接
    def replace_href_src(match):
        url = match.group(1)
        # 内部相对链接（以 / 开头，但不是 /zh-TW/）
        if url.startswith('/') and not url.startswith('/zh-TW') and not url.startswith('/pages/icons'):
            # 替换为 /zh-TW/ 路径
            if url.startswith('/pages/'):
                url = '/zh-TW/' + url[7:]  # 去掉 /pages/ 加上 /zh-TW/pages/
            elif url.startswith('/styles') or url.startswith('/app.js') or \
                 url.startswith('/manifest') or url.startswith('/sw.js') or \
                 url.startswith('/search.js') or url.startswith('/graph.html') or \
                 url.startswith('/sitemap') or url.startswith('/robots.txt'):
                # 根目录文件，保持原样
                pass
            else:
                url = '/zh-TW' + url
        return match.group(0).replace(match.group(1), url)

    # 处理 href 属性
    content = re.sub(r'href="([^"]*)"', replace_href_src, content)
    content = re.sub(r"href='([^']*)'", replace_href_src, content)

    # 处理 src 属性
    content = re.sub(r'src="([^"]*)"', replace_href_src, content)

    # 提取并转换可见文本
    result = []
    i = 0
    in_tag = False
    in_script = False
    in_style = False
    in_textarea = False
    in_preserve = False

    while i < len(content):
        char = content[i]

        # 检查特殊标签开始
        if i + 1 < len(content):
            next5 = content[i:i+8].lower()

            if next5.startswith('<script'):
                in_script = True
                result.append(content[i:i+7])
                i += 7
                continue
            elif next5.startswith('</script'):
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
            result.append(char)
            i += 1
            continue

        # 处理标签
        if char == '<':
            in_tag = True
            tag_end = content.find('>', i)
            if tag_end != -1:
                result.append(content[i:tag_end+1])
                i = tag_end + 1
                continue
        elif char == '>':
            in_tag = False
            result.append(char)
            i += 1
            continue

        if in_tag:
            result.append(char)
            i += 1
            continue

        # 收集文本块
        text_chunk = char
        while i + 1 < len(content) and content[i + 1] != '<':
            text_chunk += content[i + 1]
            i += 1
        i += 1

        # 转换文本
        converted = convert_text(text_chunk)
        result.append(converted)

    return ''.join(result)

def process_directory(src_dir, dst_dir):
    """处理整个目录"""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    count = 0

    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
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
                    print(f"✓ {filename}")
                except Exception as e:
                    print(f"✗ Error: {filename} - {e}")
            else:
                # 非 HTML 文件，直接复制
                dst_file = os.path.join(dst_subdir, filename)
                shutil.copy2(src_file, dst_file)

    return count

def main():
    src_dir = '/workspace'
    zh_tw_dir = '/workspace/zh-TW'

    print("=" * 50)
    print("繁体中文转换 v2")
    print("=" * 50)

    # 测试转换
    test_text = "知识库系统整理灵性教示，包含经典著作完整导读、核心概念详解、修行方法指南"
    print(f"\n转换测试: {test_text}")
    print(f"  → {convert_text(test_text)}")

    # 复制静态文件到根目录
    print("\n[1] 复制静态文件...")
    static_files = [
        'styles.css', 'app.js', 'manifest.json', 'sw.js', 'pwa-analytics.js',
        'search.js', 'd3.min.js', 'robots.txt', 'sitemap.xml'
    ]

    for f in static_files:
        src = os.path.join(src_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(zh_tw_dir, f))
            print(f"  ✓ {f}")

    # 复制 pages 目录下的文件
    print("\n[2] 转换页面文件...")

    # 创建必要目录
    os.makedirs(os.path.join(zh_tw_dir, 'pages', 'icons'), exist_ok=True)
    os.makedirs(os.path.join(zh_tw_dir, 'pages', 'books'), exist_ok=True)
    os.makedirs(os.path.join(zh_tw_dir, 'pages', 'concepts'), exist_ok=True)
    os.makedirs(os.path.join(zh_tw_dir, 'pages', 'qa'), exist_ok=True)
    os.makedirs(os.path.join(zh_tw_dir, 'pages', 'methods'), exist_ok=True)
    os.makedirs(os.path.join(zh_tw_dir, 'pages', 'persons'), exist_ok=True)

    # 复制 icons
    icons_src = os.path.join(src_dir, 'pages', 'icons')
    if os.path.exists(icons_src):
        for f in os.listdir(icons_src):
            shutil.copy2(os.path.join(icons_src, f), os.path.join(zh_tw_dir, 'pages', 'icons', f))

    # 处理首页
    print("\n[3] 处理 index.html...")
    index_src = os.path.join(src_dir, 'index.html')
    index_dst = os.path.join(zh_tw_dir, 'index.html')
    converted = copy_and_convert_html(index_src, index_dst)
    with open(index_dst, 'w', encoding='utf-8') as f:
        f.write(converted)
    print("  ✓ index.html")

    # 处理 graph.html
    graph_src = os.path.join(src_dir, 'graph.html')
    if os.path.exists(graph_src):
        graph_dst = os.path.join(zh_tw_dir, 'graph.html')
        shutil.copy2(graph_src, graph_dst)
        print("  ✓ graph.html")

    # 处理 sitemap.html
    sitemap_src = os.path.join(src_dir, 'sitemap.html')
    if os.path.exists(sitemap_src):
        sitemap_dst = os.path.join(zh_tw_dir, 'sitemap.html')
        shutil.copy2(sitemap_src, sitemap_dst)
        print("  ✓ sitemap.html")

    # 处理 pages 子目录
    pages_src = os.path.join(src_dir, 'pages')
    pages_dst = os.path.join(zh_tw_dir, 'pages')
    count = process_directory(pages_src, pages_dst)

    print(f"\n总计转换 {count} 个 HTML 文件")
    print("\n" + "=" * 50)
    print("转换完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
