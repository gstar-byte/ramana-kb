import os

files = [
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch9.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch10.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch12.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch13.html',
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    idx = content.find('</html>')
    if idx != -1:
        clean = content[:idx + len('</html>')]
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(clean)
        name = os.path.basename(f)
        print('Fixed:', name)
    else:
        print('No </html> found:', f)
