import re
books = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books'
files = ['crumbs-ch4.html', 'reflections-ch2.html', 'teachings-ch2.html',
         'spiritual-stories-ch2.html', 'surpassing-love-ch2.html', 'timeless-ch6.html']

patG = re.compile(
    r'<div class="card">\s*'
    r'<div style="display:flex;justify-content:space-between;align-items:center;">\s*'
    r'<a href="([^"]*)" class="[^"]*btn-secondary[^"]*">[^<]*上一章[^<]*</a>\s*'
    r'(?:<span style="[^"]*">[^<]*</span>\s*)?'
    r'</div>\s*'
    r'</div>',
    re.DOTALL)

for fname in files:
    with open(books + '/' + fname, 'r', encoding='utf-8') as f:
        content = f.read()
    m = patG.search(content)
    if m:
        print(f'YES {fname}: matched prev={m.group(1)}')
    else:
        print(f'NO {fname}: NOT matched')
        lines = content.split('\n')
        for i, l in enumerate(lines):
            if '上一章' in l or ('card' in l and i > 155):
                print(f'  line {i+1}: {l.strip()[:100]}')
