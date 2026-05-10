#!/usr/bin/env python3
"""全面修复 zh-TW 页面"""

import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. 修复 canonical URL（移除多余的 >）
    content = re.sub(r'<link rel="canonical" href="([^"]+)">>', r'<link rel="canonical" href="\1">', content)

    # 2. 修复 og:url 指向 zh-TW 版本
    content = re.sub(
        r'<meta property="og:url" content="https://ramanamaharshi\.space/([^"]*)">',
        r'<meta property="og:url" content="https://ramanamaharshi.space/zh-TW/\1">',
        content
    )

    # 3. 修复人名
    content = re.sub(r'馬雜湊', '馬哈希', content)

    # 4. 修复 hreflang 中的 canonical URL
    def fix_hreflang_canonical(match):
        url = match.group(1)
        if '/zh-TW' not in url and 'ramanamaharshi' in url:
            if url.startswith('/'):
                url = '/zh-TW' + url
            else:
                url = url.replace('ramanamaharshi.space/', 'ramanamaharshi.space/zh-TW/')
        return f'<link rel="canonical" href="{url}">'

    content = re.sub(r'<link rel="canonical" href="([^"]+)"', fix_hreflang_canonical, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    zh_tw_dir = '/workspace/pages/zh-TW'
    count = 0

    for root, dirs, files in os.walk(zh_tw_dir):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if fix_file(filepath):
                    rel_path = os.path.relpath(filepath, zh_tw_dir)
                    print(f"✓ Fixed: {rel_path}")
                    count += 1

    print(f"\n修复了 {count} 个文件")

if __name__ == '__main__':
    main()
