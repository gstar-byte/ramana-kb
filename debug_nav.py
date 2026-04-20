import re
c = open(r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/be-as-you-are.html', encoding='utf-8').read()
# 找所有 page-nav div
matches = list(re.finditer(r'<div class="page-nav">(.*?)</div>', c, re.DOTALL))
print(f'Found {len(matches)} page-nav divs')
for i, m in enumerate(matches):
    links = re.findall(r'href="([^"]+)"', m.group(1))
    print(f'  Nav {i+1}: links={links}')
    print(f'  Content: {repr(m.group(1)[:200])}')
