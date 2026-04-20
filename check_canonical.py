import re
import os

pages_dir = 'c:/Users/willp/Desktop/2026年4月/kb01/pages'

patterns = {
    '带.html': [],
    '带/index.html': [],
    '不带后缀': [],
}

for root, dirs, files in os.walk(pages_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            content = open(path, 'r', encoding='utf-8').read()
            m = re.search(r'canonical.*?href="([^"]+)"', content)
            if m:
                url = m.group(1)
                rel_path = os.path.relpath(path, pages_dir)
                if url.endswith('.html') and '/index.html' not in url:
                    patterns['带.html'].append(f'{rel_path} -> {url}')
                elif '/index.html' in url:
                    patterns['带/index.html'].append(f'{rel_path} -> {url}')
                elif not url.endswith('/'):
                    patterns['不带后缀'].append(f'{rel_path} -> {url}')

print('=== 格式1: xxx.html (如 qa-1.html) ===')
for p in patterns['带.html'][:10]:
    print(p)
print(f'... 共 {len(patterns["带.html"])} 个')

print()
print('=== 格式2: /index.html ===')
for p in patterns['带/index.html'][:10]:
    print(p)
print(f'... 共 {len(patterns["带/index.html"])} 个')

print()
print('=== 格式3: 无后缀 ===')
for p in patterns['不带后缀'][:10]:
    print(p)
print(f'... 共 {len(patterns["不带后缀"])} 个')
