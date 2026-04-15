# -*- coding: utf-8 -*-
"""修复所有子页面的PWA配置 - 改进版"""

import os
import re

def fix_pwa_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 判断文件深度（相对于 pages 目录）
    if filepath.count('/') > 1:  # 在子目录中
        rel_prefix = '../'
    else:
        rel_prefix = ''
    
    manifest_path = rel_prefix + 'manifest.json'
    icon_path = rel_prefix + 'icons/icon-192.png'
    sw_path = rel_prefix + 'sw.js'
    styles_path = rel_prefix + 'styles.css'
    
    modified = False
    
    # 1. 修复 manifest.json 路径
    if 'href="manifest.json"' in content:
        content = content.replace('href="manifest.json"', f'href="{manifest_path}"')
        modified = True
    
    # 2. 修复 styles.css 路径
    if filepath.count('/') > 1 and 'href="styles.css"' in content:
        content = content.replace('href="styles.css"', f'href="{styles_path}"')
        modified = True
    
    # 3. 修复 icons 路径
    if 'href="icons/icon-' in content:
        content = re.sub(r'href="icons/icon-\d+\.png"', f'href="{icon_path}"', content)
        modified = True
    
    # 4. 添加缺失的 PWA meta 标签
    pwa_meta_block = f'''    <link rel="manifest" href="{manifest_path}">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="apple-touch-icon" href="{icon_path}">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🙏</text></svg>">
'''
    
    # 检查是否需要添加 PWA meta
    if 'name="theme-color"' not in content and 'rel="manifest"' not in content:
        # 在 </head> 前插入完整的 PWA 标签
        content = content.replace('</head>', pwa_meta_block + '</head>')
        modified = True
    else:
        # 确保每个标签都存在
        if 'name="theme-color"' not in content:
            content = content.replace('</head>', f'    <meta name="theme-color" content="#1a1a2e">\n</head>')
            modified = True
        if 'name="apple-mobile-web-app-capable"' not in content:
            content = content.replace('</head>', f'    <meta name="apple-mobile-web-app-capable" content="yes">\n</head>')
            modified = True
        if 'name="apple-mobile-web-app-status-bar-style"' not in content:
            content = content.replace('</head>', f'    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n</head>')
            modified = True
        if 'name="apple-mobile-web-app-title"' not in content:
            content = content.replace('</head>', f'    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">\n</head>')
            modified = True
        if 'link rel="apple-touch-icon"' not in content:
            content = content.replace('</head>', f'    <link rel="apple-touch-icon" href="{icon_path}">\n</head>')
            modified = True
        if 'link rel="icon"' not in content:
            content = content.replace('</head>', f'    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'><text y=\'.9em\' font-size=\'90\'>🙏</text></svg>">\n</head>')
            modified = True
    
    # 5. 添加 service worker 注册
    sw_script = f'''
    <script>
    if ('serviceWorker' in navigator) {{
        window.addEventListener('load', function() {{
            navigator.serviceWorker.register('{sw_path}')
                .then(function(registration) {{
                    console.log('SW registered:', registration.scope);
                }})
                .catch(function(error) {{
                    console.log('SW registration failed:', error);
                }});
        }});
    }}
    </script>
'''
    
    if 'serviceWorker' not in content:
        content = content.replace('</body>', sw_script + '</body>')
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {filepath}')
    else:
        print(f'Skip : {filepath}')

def main():
    pages_dir = 'pages'
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                fix_pwa_in_file(filepath)

if __name__ == '__main__':
    main()
