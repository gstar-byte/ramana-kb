import re, glob, os

kb = r'c:/Users/willp/Desktop/2026年4月/kb01/pages'

samples = [
    'books/be-as-you-are-ch2.html',
    'books/maharshi-gospel-ch1.html',
    'concepts/silence.html',
    'methods/index.html',
    'persons/ramana.html',
    'qa/index.html',
]

for rel in samples:
    path = os.path.join(kb, rel)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'<footer[^>]*>(.*?)</footer>', content, re.DOTALL)
    if m:
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = re.sub(r'\s+', ' ', text)
        print(f'{rel}:')
        print(f'  {text[:150]}')
        print()
