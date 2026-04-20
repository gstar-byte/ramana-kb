import re
import os

pages_dir = 'c:/Users/willp/Desktop/2026年4月/kb01/pages'
count = 0

for root, dirs, files in os.walk(pages_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            content = open(path, 'r', encoding='utf-8').read()
            
            # 查找 canonical 并修复：添加 .html 后缀
            # 匹配不带 .html 的 canonical
            pattern = r'(<link rel="canonical" href="https://ramanamaharshi\.space)(?!\.html)([^"]+)"'
            
            def fix_canonical(m):
                global count
                url = m.group(2)
                # 如果没有 .html 后缀，添加它
                if not url.endswith('.html'):
                    url = url + '.html'
                    count += 1
                    return f'{m.group(1)}{url}"'
                return m.group(0)
            
            new_content = re.sub(pattern, fix_canonical, content)
            
            if new_content != content:
                open(path, 'w', encoding='utf-8').write(new_content)
                print(f'修复: {os.path.relpath(path, pages_dir)}')

print(f'\n总共修复 {count} 个文件')
