import re
lines = open(r'c:/Users/willp/Desktop/2026年4月/kb01/pdf_content/collected_works.txt', encoding='utf-8').read().split('\n')

# 找 Who Am I? 部分
in_who = False
for i, l in enumerate(lines):
    if 'NAN YAR' in l or 'Who Am I' in l:
        in_who = True
    if in_who and l.strip():
        print(f'{i+1}: {l.strip()[:120]}')
    if in_who and i > 300:
        break
