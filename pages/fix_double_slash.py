"""
批量修复链接中的双斜杠问题
- books// → books/
- concepts// → concepts/
- 仅处理内部链接，不改外部 URL
"""
import re
import os

BASE = '/workspace/pages'

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    # 替换 href="xxx//" 为 href="xxx/"
    # 分两步：先匹配模式，再替换
    new_content = content
    new_content = re.sub(r'href="([^"]+)//"', r'href="\1/"', new_content)
    new_content = re.sub(r"href='([^']+)//'", r"href='\1/'", new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# 扫描所有 .html 文件
changed = 0
total = 0
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            total += 1
            fpath = os.path.join(root, fname)
            if process_file(fpath):
                rel = os.path.relpath(fpath, BASE)
                print(f'  ✓ {rel}')
                changed += 1

print(f'\n完成：{changed}/{total} 个文件已修改')
