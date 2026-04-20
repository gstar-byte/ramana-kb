import re

txt = open(r'c:/Users/willp/Desktop/2026年4月/kb01/pdf_content/maha_yoga.txt', 'r', encoding='utf-8').read()
lines = txt.split('\n')

with open(r'c:/Users/willp/Desktop/2026年4月/kb01/maha_yoga_pages.txt', 'w', encoding='utf-8') as out:
    for i, l in enumerate(lines):
        s = l.strip()
        m = re.match(r'^--- 第(\d+)页 ---$', s)
        if m:
            pg = int(m.group(1))
            next_lines = []
            for j in range(1, 6):
                if i+j < len(lines):
                    ns = lines[i+j].strip()
                    if ns:
                        next_lines.append(ns[:80])
            joined = ' | '.join(next_lines[:3])
            out.write('Page %d | %s\n' % (pg, joined))

print('Done')
