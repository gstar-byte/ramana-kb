"""
最简单、最精确的添加斜杠脚本
"""
import re
import os

BASE = '/workspace/pages'

def is_content_link(url):
    """判断是否是我们的内容链接需要加斜杠"""
    # 排除的情况
    if (url == '/' or  # 根路径
        url.endswith('/') or  # 已经有斜杠
        url.startswith('http://') or 
        url.startswith('https://') or 
        url.startswith('//') or
        url.startswith('data:') or
        '#' in url or 
        '?' in url or
        # 检查是否有扩展名（资源文件）
        '.' in url and not url.startswith('./') and not url.startswith('../')):
        return False
    return True

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # 处理双引号的 href
    def replace_double(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        if is_content_link(url):
            return f'{prefix}{url}/{suffix}'
        return match.group(0)
    
    new_content = re.sub(r'(href=")([^"]+)(")', replace_double, new_content)
    
    # 处理单引号的 href
    def replace_single(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        if is_content_link(url):
            return f"{prefix}{url}/{suffix}"
        return match.group(0)
    
    new_content = re.sub(r"(href=')([^']+)(')", replace_single, new_content)
    
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
