import os, re
base = r'c:\Users\willp\Desktop\2026年4月\kb01\pages'
pat = re.compile(r"querySelectorAll\(['\"]\.sidebar-section-title")
results = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            content = open(fp, encoding='utf-8').read()
            if pat.search(content):
                rel = fp.replace(base, '').lstrip('/\\')
                results.append(rel)
for r in results:
    print(r)
print(f'Total: {len(results)}')
