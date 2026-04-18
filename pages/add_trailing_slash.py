"""
批量添加尾部斜杠
- href="books" → href="books/"
- href="concepts" → href="concepts/"
- 保持首页链接 href="/" 不变
- 保持带 # 锚点的链接不变
"""
import re
import os

BASE = '/workspace/pages'

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    # 替换不带斜杠的相对链接，排除：
    # - 已经带斜杠的
    # - 带 .html 的
    # - 首页 /
    # - 带 # 锚点的
    # - 带查询参数 ? 的
    # - 外部链接（http://, https://, //）
    
    new_content = content
    
    # 处理双引号的链接
    new_content = re.sub(
        r'href="(?![/#?]|https?://|//)([^"#?]+?)"',
        r'href="\1/"',
        new_content
    )
    
    # 处理单引号的链接
    new_content = re.sub(
        r"href='(?![/#?]|https?://|//)([^'#?]+?)'",
        r"href='\1/'",
        new_content
    )
    
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
