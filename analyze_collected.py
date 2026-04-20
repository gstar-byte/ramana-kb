# -*- coding: utf-8 -*-
c = open(r'c:/Users/willp/Desktop/2026年4月/kb01/pdf_content/collected_works.txt', encoding='utf-8').read()
lines = c.split('\n')

print(f'Total lines: {len(lines)}')

# Print every 50 lines to understand structure
for i in range(0, min(len(lines), 2217), 50):
    line = lines[i].strip()
    if line:
        print(f'{i+1:4d}: {line[:100]}')
