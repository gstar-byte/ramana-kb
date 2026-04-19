import re, os

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

# 检查首页的链接是否已去除 .html
with open(f'{BASE}\\index.html', encoding='utf-8') as f:
    content = f.read()

# 找所有 href
hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)

print('index.html 前20个链接:')
for h in hrefs[:20]:
    print(f'  {h}')
print()

# 检查是否还有 .html
html_links = [h for h in hrefs if '.html' in h]
print(f'仍有 .html 的链接: {len(html_links)} 个')
if html_links:
    print('示例:', html_links[:5])
