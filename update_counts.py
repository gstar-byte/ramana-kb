import os

base = 'c:/Users/willp/Desktop/2026年4月/kb01/pages'
count = 0
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            c = open(path, encoding='utf-8').read()
            if 'count">30+' in c:
                c2 = c.replace('count">30+', 'count">39+', 1)
                open(path, 'w', encoding='utf-8').write(c2)
                count += 1
                print('Updated:', path)
print('Total:', count)
