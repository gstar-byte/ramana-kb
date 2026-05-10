#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为 zh-TW 版本生成 sitemap.xml"""

import os
import re
from datetime import datetime

def generate_sitemap():
    zh_tw_dir = '/workspace/zh-TW'

    urls = []

    for root, dirs, files in os.walk(zh_tw_dir):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, zh_tw_dir)

                # 构建 URL
                url_path = rel_path.replace('\\', '/')
                if url_path == 'index.html':
                    url = 'https://ramanamaharshi.space/zh-TW/'
                else:
                    url = f'https://ramanamaharshi.space/zh-TW/{url_path}'

                # 确定优先级
                if url_path == 'index.html':
                    priority = '1.0'
                elif 'index.html' in url_path:
                    priority = '0.9'
                elif '-ch' not in url_path and '-qa' not in url_path:
                    priority = '0.8'
                else:
                    priority = '0.6'

                urls.append((url, priority))

    # 生成 XML
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''

    today = datetime.now().strftime('%Y-%m-%d')

    for url, priority in sorted(urls):
        # 获取对应的 zh-CN URL
        zh_cn_url = url.replace('/zh-TW/', '/')

        xml += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
    <xhtml:link rel="alternate" hreflang="zh-TW" href="{url}"/>
    <xhtml:link rel="alternate" hreflang="zh-CN" href="{zh_cn_url}"/>
  </url>
'''

    xml += '</urlset>'

    # 写入文件
    with open(os.path.join(zh_tw_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(xml)

    print(f"生成了包含 {len(urls)} 个 URL 的 sitemap.xml")

if __name__ == '__main__':
    generate_sitemap()
