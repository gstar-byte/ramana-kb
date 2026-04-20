import re
import os

count = 0
pages_dir = 'pages'

for root, dirs, files in os.walk(pages_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            content = open(path, 'r', encoding='utf-8').read()

            # 移除 canonical 标签（单行）
            new_content = re.sub(r'<link[^>]*rel=["\']canonical"[^>]*>', '', content)

            if new_content != content:
                open(path, 'w', encoding='utf-8').write(new_content)
                count += 1
                print(f'修复: {path}')

print(f'\\n共移除 {count} 个文件的 canonical 标签')
