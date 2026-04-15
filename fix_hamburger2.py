import os
import re

pages_dir = 'pages'
html_files = [os.path.join(r,f) for r,ds,fs in os.walk(pages_dir) for f in fs if f.endswith('.html')]

# 修复：把汉堡按钮从 sidebar 内部移到 body 直接子元素
count = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # 模式：sidebar 开始标签后紧跟汉堡按钮
    old = '<aside class="sidebar" id="sidebar">\n            <button class="hamburger" onclick="toggleSidebar()">☰</button>'
    new = '<aside class="sidebar" id="sidebar">'
    
    if old in c:
        # 先在 body 后加汉堡按钮（如果还没有）
        if '<button class="hamburger"' not in c.split('<aside')[0]:
            c = c.replace('<body>', '<body>\n    <button class="hamburger" onclick="toggleSidebar()">☰</button>')
        # 移除 sidebar 内的汉堡按钮
        c = c.replace(old, new)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1

print(f'Fixed {count} files')
