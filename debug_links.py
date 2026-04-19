import re, glob

# 检查所有页面中指向 david 的链接
files_with_david = []
for f in glob.glob('c:/Users/willp/WorkBuddy/20260410104230/pages/**/*.html', recursive=True):
    c = open(f, encoding='utf-8').read()
    # 找所有包含 david 的 href
    links = re.findall(r'href=["\']([^"\']*david[^"\']*)["\']', c)
    if links:
        files_with_david.append((f, links))

print(f'找到 {len(files_with_david)} 个文件包含 david 链接:')
for f, links in files_with_david[:20]:
    print(f'  {f}:')
    for l in links:
        print(f'    -> {l}')
