"""Debug: find book page numbers in PDF pages"""
import re

with open('pdf_content/surpassing_love.txt', 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('--- 第')
pages = {}
for part in parts[1:]:
    m = re.match(r'(\d+)页 ---(.*)', part, re.DOTALL)
    if m:
        pages[int(m.group(1))] = m.group(2)

def clean(t):
    return re.sub(r'(.)\1{4,}', r'\1', t)

# Show first line of PDF pages 11-80
for pn in sorted(pages.keys()):
    text = clean(pages[pn])
    lines = [l.strip() for l in text.split('\r\n') if l.strip()]
    if lines:
        first = lines[0][:100]
        # Check if it's a standalone number (book page)
        is_book_page = re.match(r'^\d{1,3}$', first)
        marker = ' [BOOK PAGE]' if is_book_page else ''
        print(f'PDF P{pn}: {first}{marker}')
    else:
        print(f'PDF P{pn}: [EMPTY]')
