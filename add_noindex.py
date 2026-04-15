import os
import re

count = 0
for root, dirs, files in os.walk('pages'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 检查是否已有noindex/nofollow
            if 'name="robots"' not in content:
                # 在</head>前添加meta标签
                meta = '    <meta name="robots" content="noindex, nofollow">\n'
                content = content.replace('</head>', meta + '</head>')
                
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                count += 1
                print(f'Added: {filepath}')

print(f'\nTotal: {count} files updated')
