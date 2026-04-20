# -*- coding: utf-8 -*-
c = open(r'c:/Users/willp/Desktop/2026年4月/kb01/pdf_content/collected_works.txt', encoding='utf-8').read()
lines = c.split('\n')

# Find page markers
pages = []
for i, l in enumerate(lines):
    stripped = l.strip()
    if stripped.startswith('---') and '第' in stripped and '页' in stripped:
        pages.append((i, stripped))

print(f'Total lines: {len(lines)}')
print(f'Page markers found: {len(pages)}')
for idx, (line_num, marker) in enumerate(pages):
    print(f'  {marker}: line {line_num+1}')
    # Show next 3 lines after page marker
    for j in range(1, 4):
        if line_num+j < len(lines):
            next_line = lines[line_num+j].strip()
            if next_line:
                print(f'    -> {next_line[:80]}')

# Find sections
print('\n=== Key Sections ===')
for i, l in enumerate(lines):
    stripped = l.strip()
    # Look for major section headers
    if stripped.isupper() and len(stripped) > 3 and len(stripped) < 60:
        if not stripped.startswith('---'):
            print(f'Line {i+1}: {stripped}')
