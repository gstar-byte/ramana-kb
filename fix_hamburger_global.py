#!/usr/bin/env python3
"""统一修复所有HTML文件的汉堡菜单结构"""

import os
import re

# 正确的结构
CORRECT_HAMBURGER = '''<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout\">'''

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<body>' not in content:
        return False
    
    # 检查是否已经有正确的结构
    if content.find('<button class="hamburger"') > 0 and content.find('<button class="hamburger"') < content.find('<body>') + 20:
        # 汉堡按钮在body标签附近，已经正确
        return False
    
    # 移除现有的错误汉堡按钮和覆盖层
    # 移除 <button class="hamburger"...>
    content = re.sub(r'\s*<button class="hamburger"[^>]*>☰</button>', '', content)
    # 移除 <div class="sidebar-overlay"...>
    content = re.sub(r'\s*<div class="sidebar-overlay"[^>]*></div>', '', content)
    
    # 在 <body> 后面插入正确的结构
    content = content.replace('<body>\n', CORRECT_HAMBURGER + '\n', 1)
    content = content.replace('<body>', CORRECT_HAMBURGER + '\n', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    pages_dir = 'pages'
    count = 0
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    print(f'Fixed: {filepath}')
                    count += 1
    
    print(f'\nTotal fixed: {count} files')

if __name__ == '__main__':
    main()
