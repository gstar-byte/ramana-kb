#!/usr/bin/env python3
"""
增强版 sitemap.xml 生成器
- 添加 lastmod (今日日期)
- 添加 priority (按页面层级)
- 添加 changefreq
- 确保所有 URL 与实际可访问的页面一致（保留 .html 后缀）
- 每条 URL 添加 xhtml:link hreflang（zh-CN / zh-TW）；整站仅此一份 XML 站点地图（含 /zh-TW 下页面）
"""
import os
import re
import glob
from datetime import date

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://ramanamaharshi.space"
ZH_TW_ROOT = "/zh-TW"
TODAY = date.today().strftime("%Y-%m-%d")


def hreflang_urls(url_path):
    """
    根据站点路径返回 (zh-CN 完整 URL, zh-TW 完整 URL)。
    url_path 形如 /、/books/x.html、/zh-TW/...（与 get_url_and_priority 输出一致）。
    """
    if url_path.startswith(f"{ZH_TW_ROOT}/"):
        rest = url_path[len(f"{ZH_TW_ROOT}/") :]
        if rest in ("", "index.html"):
            cn_path = "/"
        else:
            cn_path = f"/{rest}"
        cn_full = f"{BASE_URL}/" if cn_path == "/" else f"{BASE_URL}{cn_path}"
        # 繁體首頁 hreflang 使用 /zh-TW/（與站內慣例一致）
        if rest in ("", "index.html"):
            tw_full = f"{BASE_URL}{ZH_TW_ROOT}/"
        else:
            tw_full = f"{BASE_URL}{url_path}"
        return cn_full, tw_full

    if url_path in ("/", "/index.html"):
        cn_full = f"{BASE_URL}/"
        tw_full = f"{BASE_URL}{ZH_TW_ROOT}/"
        return cn_full, tw_full

    cn_full = f"{BASE_URL}{url_path}"
    tw_full = f"{BASE_URL}{ZH_TW_ROOT}{url_path}"
    return cn_full, tw_full

def get_url_and_priority(rel_path):
    """从相对路径生成 URL 和优先级（保留 .html 后缀）"""
    # 统一使用正斜杠
    p = rel_path.replace('\\', '/')
    
    # 修正 index.html 页面
    if p == 'index.html':
        return '/', 1.0, 'weekly'
    
    # 计算优先级
    depth = p.count('/')
    basename = os.path.basename(p)
    
    if depth == 0:  # 顶级页面（graph.html等）
        priority = 0.8
        freq = 'monthly'
    elif depth == 1:  # 二级页面
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
        'index_fixed.html',  # 临时修复文件不需要
        'index.html.backup',  # 备份文件不需要
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
    lines.append(
        "<!-- 供搜索引擎抓取。人类可读、带版式的索引页："
        f"{BASE_URL}/sitemap.html（简体）与 {BASE_URL}/zh-TW/sitemap.html（繁体） -->"
    )
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
    lines.append('        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
    lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml"')
    lines.append('        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9')
    lines.append('        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">')
    
    for url_path, priority, freq in urls:
        full_url = f"{BASE_URL}{url_path}"
        cn_href, tw_href = hreflang_urls(url_path)
        lines.append('  <url>')
        lines.append(f'    <loc>{full_url}</loc>')
        lines.append(f'    <lastmod>{TODAY}</lastmod>')
        lines.append(f'    <changefreq>{freq}</changefreq>')
        lines.append(f'    <priority>{priority:.1f}</priority>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="zh-CN" href="{cn_href}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="zh-TW" href="{tw_href}"/>')
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
