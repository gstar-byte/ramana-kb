import re
BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'
with open(f'{BASE}\\index.html', encoding='utf-8') as f:
    content = f.read()
hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
anchor_links = [h for h in hrefs if '#' in h]
print('锚点链接:')
for h in anchor_links:
    print(f'  {h}')
