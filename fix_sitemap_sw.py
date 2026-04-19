import re

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

for fname in ['sitemap.xml', 'sw.js']:
    path = f'{BASE}\\{fname}'
    with open(path, encoding='utf-8') as f:
        c = f.read()
    # 匹配 .html 链接（非协议开头）
    matches = re.findall(r'(https?://[^\s"\'<>]*\.html)', c)
    if matches:
        print(f'{fname}: 发现 {len(matches)} 个 .html 引用，需要更新 sitemap 生成脚本')
    else:
        print(f'{fname}: 无需修改 ✅')

# 检查 sw.js 中的预缓存列表
sw_path = f'{BASE}\\sw.js'
with open(sw_path, encoding='utf-8') as f:
    sw = f.read()
precache = re.findall(r'"([^"]+\.html)"', sw)
if precache:
    print(f'sw.js: 预缓存中有 {len(precache)} 个 .html 文件')
    # 需要把这些也改成无扩展名，Vercel cleanUrls 会自动处理
    # 但 service worker 预缓存是本地缓存，应该和实际文件对应
    # 由于文件名还是 .html，预缓存 URL 也应该是 .html
    print('sw.js: 预缓存 URL 保持 .html（文件名本身没变）')
