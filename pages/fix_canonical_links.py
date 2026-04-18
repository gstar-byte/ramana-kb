"""
修复所有HTML文件中的canonical链接，添加.html扩展名
"""
import re
import os

BASE = '/workspace/pages'

# 正则：匹配 canonical 链接
CANONICAL_RE = re.compile(r'(rel=["\']canonical["\'] href=["\'])([^"\']+)(["\'])')

def fix_canonical_url(url):
    """修复 canonical URL，添加 .html 扩展名"""
    # 跳过根路径和已有的 .html 链接
    if url == 'https://ramanamaharshi.space/':
        return url
    
    # 跳过包含文件扩展名的链接
    if any(ext in url for ext in ['.html', '.xml', '.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg']):
        return url
    
    # 为非根路径添加 .html 扩展名
    return url + '.html'

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # 替换 canonical 链接
    def replacer(m):
        prefix = m.group(1)
        url = m.group(2)
        suffix = m.group(3)
        return prefix + fix_canonical_url(url) + suffix

    new_content = CANONICAL_RE.sub(replacer, content)

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
