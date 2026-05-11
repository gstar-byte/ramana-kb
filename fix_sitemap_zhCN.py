#!/usr/bin/env python3
"""修复简体 sitemap，移除 zh-TW URL"""

sitemap_path = r"F:\26年4月\kb01\pages\sitemap.xml"

with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找出所有 url 条目
import re

# 匹配整个 <url>...</url> 块
url_pattern = re.compile(r'<url>.*?</url>', re.DOTALL)

urls = url_pattern.findall(content)

# 过滤掉 zh-TW 的 URL
zhTW_urls = []
zhCN_urls = []

for url in urls:
    if '/zh-TW/' in url:
        zhTW_urls.append(url)
    else:
        zhCN_urls.append(url)

print(f"总 URL 数: {len(urls)}")
print(f"简体 URL: {len(zhCN_urls)}")
print(f"繁体 URL (将被移除): {len(zhTW_urls)}")

# 重新组装
header = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
'''

footer = '</urlset>'

new_content = header + '\n'.join(zhCN_urls) + '\n' + footer

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\n已修复！简体 sitemap 现在只包含 {len(zhCN_urls)} 个 URL")
