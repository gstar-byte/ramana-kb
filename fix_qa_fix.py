#!/usr/bin/env python3
INPUT = r"F:\26年4月\kb01\pages\zh-TW\qa\index.html"
with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(' 页，共 ', ' 頁，共 ')
with open(INPUT, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done - fixed 页，共')
