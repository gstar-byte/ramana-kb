import re, os

base = r'c:\Users\willp\WorkBuddy\20260410104230\pages'
files = ['index.html', 'books/be-as-you-are.html', 'persons/ramana.html']
for fp in files:
    c = open(os.path.join(base, fp), encoding='utf-8').read()
    links = re.findall(r'href=["\']([^"\']*\.html)', c)
    print(f'{fp}: {len(links)} 个 .html 链接')
    if links[:3]:
        print('  示例:', links[:3])
