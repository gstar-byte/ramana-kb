#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
繁体中文转换脚本
使用 OpenCC 进行繁简转换，并按台湾习惯处理特定术语和人名
"""

import os
import re
import shutil
from opencc import OpenCC

# 初始化 OpenCC (使用台湾繁体配置)
cc = OpenCC('s2twp')  # 简体到繁体（台湾习惯，含常用词转换）

# 台湾习惯用语替换（覆盖 OpenCC 默认转换）
# 这些是根据台湾出版习惯调整的
TAIWAN_TERMS = {
    # 书籍/出版相关
    '叢書': '叢書',
    '叢': '叢',

    # 灵性/宗教术语（保持原样或按台湾习惯）
    '解脫': '解脫',
    '真我': '真我',
    '心智': '心智',
    '上師': '上師',
    '靜默': '靜默',
    '臣服': '臣服',
    '恩典': '恩典',

    # 人名（保持原样，这些是专有名词）
    '拉瑪那': '拉瑪那',
    '馬哈希': '馬哈希',
    '大衛·高德曼': '大衛·高德曼',

    # 其他常见词
    '軟體': '軟體',
    '軟件': '軟體',
    '網站': '網站',
    '網頁': '網頁',
    '瀏覽器': '瀏覽器',
    '文檔': '文檔',
    '文檔': '文檔',

    # 标点符号
    '「': '「',
    '」': '」',
    '『': '『',
    '』': '』',
}

def convert_text(text):
    """转换文本内容"""
    # 首先使用 OpenCC 转换
    converted = cc.convert(text)

    # 按台湾习惯微调
    # 保持一些佛教/印度词汇的繁体原貌

    return converted

def should_preserve_text(tag, attrs):
    """判断是否应该保留原文（如代码、英文等）"""
    if tag in ['script', 'style', 'code', 'pre']:
        return True
    if tag == 'a' and any(k.lower() == 'hreflang' for k, v in attrs):
        return True
    if tag == 'meta':
        for k, v in attrs:
            if k in ['name', 'property', 'content']:
                if 'hreflang' in str(v).lower():
                    return True
    return False

def convert_html_file(input_path, output_path):
    """转换单个 HTML 文件"""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换 hreflang 标签中的 URL
    # 将 /books/ -> /zh-TW/books/
    # 将 https://ramanamaharshi.space/ -> https://ramanamaharshi.space/zh-TW/

    def replace_urls(match):
        url = match.group(1)
        # 只替换内部链接
        if url.startswith('/') and not url.startswith('/zh-TW'):
            url = '/zh-TW' + url
        elif url.startswith('https://ramanamaharshi.space/') and '/zh-TW' not in url:
            url = url.replace('https://ramanamaharshi.space/', 'https://ramanamaharshi.space/zh-TW/')
        return match.group(0).replace(match.group(1), url)

    # 替换内部链接
    content = re.sub(r'href="([^"]+)"', replace_urls, content)
    content = re.sub(r'src="([^"]+)"', replace_urls, content)
    content = re.sub(r"href='([^']+)'", replace_urls, content)

    # 替换语言标签中的 URL
    content = re.sub(
        r'(href=")(https://ramanamaharshi\.space/)([^"]*")',
        lambda m: m.group(1) + m.group(2) + 'zh-TW/' + m.group(3),
        content
    )

    # 转换 HTML lang 属性
    content = content.replace('lang="zh-CN"', 'lang="zh-TW"')

    # 替换 og:locale
    content = content.replace('og:locale" content="zh_CN"', 'og:locale" content="zh_TW"')

    # 替换 JSON-LD 中的语言
    content = content.replace('"inLanguage": "zh-CN"', '"inLanguage": "zh-TW"')

    # 替换 canonical 和其他链接
    def replace_canonical_url(match):
        url = match.group(1)
        if url.startswith('https://ramanamaharshi.space/') and '/zh-TW' not in url:
            url = url.replace('https://ramanamaharshi.space/', 'https://ramanamaharshi.space/zh-TW/')
        elif url.startswith('/') and not url.startswith('/zh-TW'):
            url = '/zh-TW' + url
        return match.group(0).replace(match.group(1), url)

    content = re.sub(r'(https://ramanamaharshi\.space/[^"]+)', replace_canonical_url, content)
    content = re.sub(r'(href=")(/[^"]+")', lambda m: m.group(1) + ('/zh-TW' + m.group(2)[1:] if not m.group(2).startswith('/zh-TW') else m.group(1) + m.group(2)), content)

    # 提取并转换可见文本内容
    result = []
    i = 0
    in_tag = False
    in_script = False
    in_style = False
    in_textarea = False

    while i < len(content):
        char = content[i]

        # 处理特殊标签
        if content[i:i+7].lower() == '<script':
            in_script = True
            result.append(content[i:i+7])
            i += 7
            continue
        elif content[i:i+8].lower() == '</script':
            in_script = False
            result.append(content[i:i+8])
            i += 8
            continue
        elif content[i:i+6].lower() == '<style':
            in_style = True
            result.append(content[i:i+6])
            i += 6
            continue
        elif content[i:i+7].lower() == '</style':
            in_style = False
            result.append(content[i:i+7])
            i += 7
            continue
        elif content[i:i+9].lower() == '<textarea':
            in_textarea = True
            result.append(content[i:i+9])
            i += 9
            continue
        elif content[i:i+10].lower() == '</textarea':
            in_textarea = False
            result.append(content[i:i+10])
            i += 10
            continue

        if in_script or in_style or in_textarea:
            result.append(char)
            i += 1
            continue

        # 处理 HTML 标签
        if char == '<':
            in_tag = True
            # 提取完整标签
            tag_end = content.find('>', i)
            if tag_end != -1:
                tag = content[i:tag_end+1]
                result.append(tag)
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

        # 收集纯文本
        text_chunk = char
        while i + 1 < len(content):
            next_char = content[i + 1]
            if next_char == '<':
                break
            text_chunk += next_char
            i += 1
        i += 1

        # 转换文本（保留空白和标点）
        converted_chunk = convert_text(text_chunk)
        result.append(converted_chunk)

    return ''.join(result)

def convert_directory(src_dir, dst_dir, base_src='pages', base_dst='zh-TW/pages'):
    """递归转换目录"""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    converted_count = 0

    for root, dirs, files in os.walk(src_dir):
        # 计算相对路径
        rel_path = os.path.relpath(root, src_dir)

        # 替换路径中的 pages 为 zh-TW/pages
        if rel_path.startswith('pages'):
            new_rel_path = rel_path.replace('pages', 'zh-TW/pages', 1)
        else:
            new_rel_path = rel_path

        dst_subdir = os.path.join(dst_dir, new_rel_path)

        if not os.path.exists(dst_subdir):
            os.makedirs(dst_subdir)

        for filename in files:
            if filename.endswith('.html') or filename.endswith('.htm'):
                src_file = os.path.join(root, filename)
                dst_file = os.path.join(dst_subdir, filename)

                try:
                    converted = convert_html_file(src_file, dst_file)
                    with open(dst_file, 'w', encoding='utf-8') as f:
                        f.write(converted)
                    converted_count += 1
                    print(f"✓ {src_file} -> {dst_file}")
                except Exception as e:
                    print(f"✗ Error converting {src_file}: {e}")

    return converted_count

def copy_static_files(src_dir, dst_dir):
    """复制静态文件"""
    static_files = ['styles.css', 'app.js', 'manifest.json', 'sw.js', 'pwa-analytics.js',
                   'search.js', 'graph.html', 'sitemap.html', 'robots.txt', 'sitemap.xml',
                   'favicon.ico', 'd3.min.js']

    # 也复制 icons 目录
    icons_src = os.path.join(src_dir, 'pages', 'icons')
    icons_dst = os.path.join(dst_dir, 'pages', 'icons')

    if os.path.exists(icons_src):
        if not os.path.exists(icons_dst):
            os.makedirs(icons_dst)
        for f in os.listdir(icons_src):
            src = os.path.join(icons_src, f)
            dst = os.path.join(icons_dst, f)
            shutil.copy2(src, dst)
            print(f"  Copied icon: {f}")

    # 复制根目录的静态文件
    for f in static_files:
        src = os.path.join(src_dir, f)
        dst = os.path.join(dst_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied: {f}")

def main():
    src_dir = '/workspace'
    dst_dir = '/workspace/zh-TW'

    print("=" * 50)
    print("繁体中文转换脚本")
    print("=" * 50)

    # 复制静态文件
    print("\n[1] 复制静态文件...")
    copy_static_files(src_dir, dst_dir)

    # 复制 public 目录（如果有）
    public_src = os.path.join(src_dir, 'public')
    public_dst = os.path.join(dst_dir, 'public')
    if os.path.exists(public_src):
        shutil.copytree(public_src, public_dst, dirs_exist_ok=True)
        print("  Copied public/")

    # 转换 pages 目录
    print("\n[2] 转换页面文件...")
    pages_src = os.path.join(src_dir, 'pages')
    pages_dst = os.path.join(dst_dir, 'pages')
    count = convert_directory(pages_src, pages_dst)
    print(f"\n总计转换 {count} 个 HTML 文件")

    print("\n" + "=" * 50)
    print("转换完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
