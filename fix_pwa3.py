# -*- coding: utf-8 -*-
"""修复所有子页面的PWA配置 - 正确版"""

import os
import re

def get_relative_prefix(filepath):
    """根据文件深度返回正确的相对路径前缀"""
    # filepath 格式: pages/books/be-as-you-are.html
    # 需要计算从当前文件到 pages 目录的深度
    parts = filepath.split(os.sep)
    # parts[0] = 'pages', parts[1] = 'books', parts[2] = 'file.html'
    # 目录深度 = len(parts) - 1 (去掉 'pages')
    depth = len(parts) - 1
    if depth <= 1:
        return ''  # 直接在 pages 目录下
    return '../' * (depth - 1)  # 子目录需要 ../

def fix_pwa_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = get_relative_prefix(filepath)
    
    # 清理旧的/错误的 PWA 标签
    # 移除所有 manifest 和 apple 相关 meta/link 标签
    content = re.sub(r'<link[^>]*rel="manifest"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*name="theme-color"[^>]*>', '', content)
    content = re.sub(r'<meta[^>]*name="apple-mobile-web-app[^"]*"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="apple-touch-icon"[^>]*>', '', content)
    content = re.sub(r'<link[^>]*rel="icon"[^>]*>', '', content)
    content = re.sub(r'<!-- PWA.*?-->', '', content, flags=re.DOTALL)
    
    # 清理重复的空行
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # 构建正确的 PWA 标签
    manifest_path = prefix + 'manifest.json'
    icon_path = prefix + 'icons/icon-192.png'
    sw_path = prefix + 'sw.js'
    
    pwa_block = f'''
    <!-- PWA 配置 -->
    <link rel="manifest" href="{manifest_path}">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="apple-touch-icon" href="{icon_path}">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🙏</text></svg>">
'''
    
    # 在 </head> 前插入 PWA 标签
    content = content.replace('</head>', pwa_block + '</head>')
    
    # 添加/更新 service worker 注册
    sw_script = f'''
    <!-- Service Worker -->
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
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed: {filepath}')

def main():
    pages_dir = 'pages'
    count = 0
    
    for root, dirs, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                fix_pwa_in_file(filepath)
                count += 1
    
    print(f'\n总计修复 {count} 个文件')

if __name__ == '__main__':
    main()
