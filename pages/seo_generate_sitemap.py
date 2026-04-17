#!/usr/bin/env python3
"""
增强版 sitemap.xml 生成器
- 添加 lastmod (今日日期)
- 添加 priority (按页面层级)
- 添加 changefreq
- 修复 /index → /
- 确保所有 HTML 页面都包含
"""
import os
import re
import glob
from datetime import date

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://ramanamaharshi.space"
TODAY = date.today().strftime("%Y-%m-%d")

def get_url_and_priority(rel_path):
    """从相对路径生成 URL 和优先级"""
    # 统一使用正斜杠
    p = rel_path.replace('\\', '/')
    
    # 去掉 .html 后缀
    p = re.sub(r'\.html$', '', p)
    
    # 修正 index 页面
    if p == 'index':
        return '/', 1.0, 'weekly'
    if p.endswith('/index'):
        p = p[:-6]  # 去掉 /index
    
    # 计算优先级
    depth = p.count('/')
    if depth == 0:  # 顶级页面（graph, methods等）
        priority = 0.8
        freq = 'monthly'
    elif depth == 1:  # 二级页面（books/index, concepts/index 等）
        basename = os.path.basename(p)
        if 'ch' in basename or re.match(r'qa-\d+', basename):
            priority = 0.6  # 章节页面
            freq = 'monthly'
        else:
            priority = 0.8  # 列表/详情页面
            freq = 'monthly'
    else:
        priority = 0.5
        freq = 'monthly'
    
    return f'/{p}', priority, freq

def main():
    # 收集所有 HTML 文件
    html_files = glob.glob(os.path.join(PAGES_DIR, '**', '*.html'), recursive=True)
    
    # 排除不需要在 sitemap 中的文件
    exclude_patterns = {
        '_template.html',
        'sitemap.html',  # sitemap HTML 版本不需要
    }
    
    urls = []
    for fp in sorted(html_files):
        bn = os.path.basename(fp)
        if bn in exclude_patterns:
            continue
        
        rel = os.path.relpath(fp, PAGES_DIR)
        url_path, priority, freq = get_url_and_priority(rel)
        
        urls.append((url_path, priority, freq))
    
    # 排序：首页第一，然后按优先级降序，同优先级按路径排序
    urls.sort(key=lambda x: (-x[1], x[0]))
    
    # 生成 sitemap.xml
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
    lines.append('        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
    lines.append('        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9')
    lines.append('        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">')
    
    for url_path, priority, freq in urls:
        full_url = f"{BASE_URL}{url_path}"
        lines.append('  <url>')
        lines.append(f'    <loc>{full_url}</loc>')
        lines.append(f'    <lastmod>{TODAY}</lastmod>')
        lines.append(f'    <changefreq>{freq}</changefreq>')
        lines.append(f'    <priority>{priority:.1f}</priority>')
        lines.append('  </url>')
    
    lines.append('</urlset>')
    
    sitemap_content = '\n'.join(lines) + '\n'
    
    sitemap_path = os.path.join(PAGES_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print(f'✅ 生成 sitemap.xml: {len(urls)} 个 URL')
    print(f'   日期: {TODAY}')
    print(f'   路径: {sitemap_path}')

if __name__ == '__main__':
    main()
