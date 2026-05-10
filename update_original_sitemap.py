#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新原始 sitemap.xml 添加 hreflang"""

import os
from datetime import datetime

def update_original_sitemap():
    sitemap_path = '/workspace/zh-TW/sitemap.xml'

    # 读取当前 sitemap
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换 zh-TW URL 为 zh-CN URL
    content = content.replace('https://ramanamaharshi.space/zh-TW/', 'https://ramanamaharshi.space/')

    # 交换 hreflang 标签
    content = content.replace('hreflang="zh-TW"', 'TMP').replace('hreflang="zh-CN"', 'hreflang="zh-TW"').replace('TMP', 'hreflang="zh-CN"')

    # 写入回原始 sitemap.xml
    original_path = '/workspace/pages/sitemap.xml'
    with open(original_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("更新了原始 sitemap.xml")

if __name__ == '__main__':
    update_original_sitemap()
