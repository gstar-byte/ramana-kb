import os
import re

pages_dir = "c:/Users/willp/WorkBuddy/20260410104230/pages"
html_files = []

for root, dirs, files in os.walk(pages_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 添加覆盖层
    if 'sidebar-overlay' not in content:
        # 在 <body> 后添加覆盖层
        content = content.replace('<body>', '''<body>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
''')
    
    # 2. 更新 toggleSidebar 函数
    old_func = "function toggleSidebar() { document.getElementById('sidebar').classList.toggle('open'); }"
    new_func = """function toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('sidebarOverlay');
        sidebar.classList.toggle('open');
        if (overlay) overlay.classList.toggle('open');
    }"""
    content = content.replace(old_func, new_func)
    
    # 3. 添加移动端菜单点击关闭
    if 'sidebar-item' in content and 'onclick="toggleSidebar()"' not in content.split('sidebar-items')[-1][:500] if 'sidebar-items' in content else True:
        # 在 sidebar-items 结束后添加关闭逻辑（通过在每个 sidebar-item 的 onclick）
        pass  # 不太可靠，跳过
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    count += 1

print(f"已更新 {count} 个文件的侧边栏功能")
