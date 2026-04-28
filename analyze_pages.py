"""Analyze page structure of surpassing_love.txt"""
import re

with open('pdf_content/surpassing_love.txt', 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('--- 第')

with open('page_analysis.txt', 'w', encoding='utf-8') as out:
    for i, part in enumerate(parts[1:], 1):
        m = re.match(r'(\d+)页 ---(.*)', part)
        if m:
            page_num = int(m.group(1))
            # Lines are separated by \r\n in the file, and also literal \n
            # Clean up: replace literal \n with space, then split by \r\n
            cleaned = part.replace('\\n', ' ')
            lines = [l.strip() for l in cleaned.split('\r\n') if l.strip()][:3]
            preview = ' | '.join(lines)
            out.write('P%s: %s\n' % (page_num, preview[:200]))

print("Done.")
