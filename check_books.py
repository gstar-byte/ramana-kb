import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')
files = [f for f in os.listdir('.') if f.endswith('.html') and '-ch' not in f and f != 'index.html']
files.sort()

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    has_related_books = '有' if '相关书籍' in content else '无'
    
    if 'class="tag"' in content:
        tag_type = 'tag(有icon)'
    elif 'class="concept-tag"' in content:
        tag_type = 'concept-tag(无icon)'
    else:
        tag_type = '未知'
    
    print(f'{f}: 相关书籍={has_related_books}, 标签={tag_type}')
