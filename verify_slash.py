import re, os

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'
with open(f'{BASE}\\index.html', encoding='utf-8') as f:
    content = f.read()

hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
print('index.html 前25个链接:')
for h in hrefs[:25]:
    print(f'  {h}')
print()
# 检查异常
no_slash_html = [h for h in hrefs if '.html' in h]
no_slash_no_ext = [h for h in hrefs if not h.endswith('/') and not '.' in h.split('/')[-1] and not h.startswith('http') and not h.startswith('//') and not h.startswith('#')]
print(f'含.html的链接: {len(no_slash_html)} 个')
print(f'无斜杠无扩展名内部链接: {no_slash_no_ext}')
