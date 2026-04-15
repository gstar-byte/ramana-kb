import os

pages_dir = 'pages'
html_files = [os.path.join(r,f) for r,ds,fs in os.walk(pages_dir) for f in fs if f.endswith('.html')]

old_pattern = '''<body>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <!-- 左侧边栏 -->
        <aside class="sidebar" id="sidebar">
            <button class="hamburger" onclick="toggleSidebar()">☰</button>'''

new_pattern = '''<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <!-- 左侧边栏 -->
        <aside class="sidebar" id="sidebar">'''

count = 0
for fp in html_files:
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if old_pattern in c:
        c = c.replace(old_pattern, new_pattern)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1

print(f'Updated {count} files')
