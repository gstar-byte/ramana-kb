#!/usr/bin/env python3
"""
站点性能优化脚本
批量更新所有HTML文件，替换 script.js + search.js 为 app.js
"""

import os
import re
from pathlib import Path

def optimize_html_file(filepath):
    """优化单个HTML文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # 1. 替换 script.js + search.js 为 app.js
    # 处理各种变体：带 defer、不带 defer、不同顺序
    patterns = [
        # 标准情况：两个script标签分开
        (r'<script src="[^"]*script\.js"[^>]*></script>\s*<script src="[^"]*search\.js"[^>]*></script>',
         '<script src="app.js" defer></script>'),
        (r'<script src="[^"]*search\.js"[^>]*></script>\s*<script src="[^"]*script\.js"[^>]*></script>',
         '<script src="app.js" defer></script>'),
        # 子目录情况
        (r'<script src="\.\./script\.js"[^>]*></script>\s*<script src="\.\./search\.js"[^>]*></script>',
         '<script src="../app.js" defer></script>'),
        (r'<script src="\.\./search\.js"[^>]*></script>\s*<script src="\.\./script\.js"[^>]*></script>',
         '<script src="../app.js" defer></script>'),
        # 三级目录
        (r'<script src="\.\./\.\./script\.js"[^>]*></script>\s*<script src="\.\./\.\./search\.js"[^>]*></script>',
         '<script src="../../app.js" defer></script>'),
        (r'<script src="\.\./\.\./search\.js"[^>]*></script>\s*<script src="\.\./\.\./script\.js"[^>]*></script>',
         '<script src="../../app.js" defer></script>'),
    ]

    for pattern, replacement in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"合并JS: {filepath.name}")
            break

    # 2. 添加关键资源预加载（如果还没有）
    if 'rel="preload"' not in content and '<head>' in content:
        # 计算相对路径
        try:
            rel_path = filepath.parent.relative_to(Path('pages'))
            depth = len(rel_path.parts) if rel_path.parts else 0
        except ValueError:
            depth = 0
        if depth == 0:
            css_path, js_path = 'styles.css', 'app.js'
        else:
            prefix = '../' * depth
            css_path, js_path = prefix + 'styles.css', prefix + 'app.js'

        preload_html = f'''    <!-- 预加载关键资源 -->
    <link rel="preload" href="{css_path}" as="style">
    <link rel="preload" href="{js_path}" as="script">

    <!-- DNS 预解析 -->
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
    <link rel="preconnect" href="https://www.google-analytics.com" crossorigin>

'''
        # 在 <link rel="stylesheet" 之前插入
        content = re.sub(r'(<link rel="stylesheet"[^>]*>)', preload_html + r'\1', content, count=1)
        changes.append(f"添加预加载: {filepath.name}")

    # 3. 优化 GA 代码（如果存在旧的同步加载方式）
    if 'gtag(' in content and 'send_page_view: false' not in content:
        # 已经是异步的，不需要修改
        pass

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

def main():
    pages_dir = Path('pages')
    html_files = list(pages_dir.rglob('*.html'))

    print(f"找到 {len(html_files)} 个HTML文件")
    print("=" * 50)

    total_changes = []
    for html_file in html_files:
        changes = optimize_html_file(html_file)
        total_changes.extend(changes)
        if changes:
            print(f"✅ {html_file.relative_to(pages_dir)}")
            for c in changes:
                print(f"   - {c}")

    print("=" * 50)
    print(f"优化完成！共修改 {len(total_changes)} 处")

if __name__ == '__main__':
    main()
