# -*- coding: utf-8 -*-
"""修复所有子页面的PWA配置"""

import os
import re

def fix_pwa(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 计算相对路径前缀
    depth = filepath.count('/') - 1  # 减去 'pages/'
    prefix = '../' * depth if depth > 0 else ''
    
    manifest = prefix + 'manifest.json'
    icon = prefix + 'icons/icon-192.png'
    sw = prefix + 'sw.js'
    
    modified = False
    
    # 1. 修复 manifest.json 路径
    if 'href="manifest.json"' in content:
        content = content.replace('href="manifest.json"', f'href="{manifest}"')
        modified = True
    
    # 2. 修复 icons 路径
    if 'href="icons/icon-' in content:
        content = re.sub(r'href="icons/icon-\d+\.png"', f'href="{icon}"', content)
        modified = True
    
    # 3. 修复 styles.css 路径
    if depth > 0 and 'href="styles.css"' in content:
        content = content.replace('href="styles.css"', f'href="{prefix}styles.css"')
        modified = True
    
    # 4. 修复损坏的 meta 标签（多个属性合并在一行）
    # 匹配: <meta name="xxx" content="yyy" name="zzz" ...>
    bad_pattern = r'<meta\s+name="apple-mobile-web-app-capable"\s+content="yes"\s+name="apple-mobile-web-app-status-bar-style"\s+content="[^"]*"\s+name="apple-mobile-web-app-title"\s+content="[^"]*"\s+name="theme-color"\s+content="[^"]*">'
    good_block = f'''    <link rel="manifest" href="{manifest}">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="apple-touch-icon" href="{icon}">
'''
    
    if re.search(bad_pattern, content):
        content = re.sub(bad_pattern, good_block, content)
        modified = True
    
    # 5. 如果没有 PWA 标签，添加它们
    if 'name="theme-color"' not in content:
        # 在 </head> 前添加 PWA 标签
        pwa_block = f'''    <link rel="manifest" href="{manifest}">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="apple-touch-icon" href="{icon}">
'''
        content = content.replace('</head>', pwa_block + '</head>')
        modified = True
    
    # 6. 添加 service worker 注册
    if 'serviceWorker' not in content:
        sw_script = f'''
    <script>
    if ('serviceWorker' in navigator) {{
        window.addEventListener('load', function() {{
            navigator.serviceWorker.register('{sw}').then(function(reg) {{
                console.log('SW registered');
            }}).catch(function(err) {{
                console.log('SW failed:', err);
            }});
        }});
    }}
    </script>
'''
        content = content.replace('</body>', sw_script + '</body>')
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {filepath}')

def main():
    for root, dirs, files in os.walk('pages'):
        for f in files:
            if f.endswith('.html'):
                fix_pwa(os.path.join(root, f))

if __name__ == '__main__':
    main()
