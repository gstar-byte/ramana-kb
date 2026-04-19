import re, glob

# 给缺少 <script> 标签的 SW 注册代码添加 <script> 标签
files = [
    r'c:\Users\willp\WorkBuddy\20260410104230\pages\index.html',
    r'c:\Users\willp\WorkBuddy\20260410104230\pages\concepts\guru.html',
    r'c:\Users\willp\WorkBuddy\20260410104230\pages\concepts\maya.html',
]

for f in files:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    
    # 找 serviceWorker.register 前的注释行，加上 <script> 标签
    # 匹配 "    // Service Worker 注册" 前面加上 "<script>"
    old = '        // Service Worker 注册 (PWA离线支持)'
    new = '    <script>\n        // Service Worker 注册 (PWA离线支持)'
    c = c.replace(old, new, 1)
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    print(f'修复: {f}')

print('\n完成')
