"""
安全地添加尾部斜杠，只处理我们的内容页面，不影响资源文件
"""
import re
import os

BASE = '/workspace/pages'

# 资源文件扩展名列表，这些不要处理
RESOURCE_EXTENSIONS = [
    '.css', '.js', '.json', '.png', '.jpg', '.jpeg', '.gif',
    '.svg', '.ico', '.webp', '.woff', '.woff2', '.ttf', '.eot',
    '.pdf', '.txt', '.xml'
]

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    
    # 处理双引号的链接
    def replace_double_quote(match):
        url = match.group(1)
        # 检查是否是资源文件
        is_resource = any(url.endswith(ext) for ext in RESOURCE_EXTENSIONS)
        # 检查是否已经带斜杠、是根路径、带锚点或查询参数
        if (not is_resource and 
            not url.endswith('/') and 
            url != '/' and 
            '#' not in url and 
            '?' not in url and
            not url.startswith('http://') and
            not url.startswith('https://') and
            not url.startswith('//')):
            return f'href="{url}/"'
        return match.group(0)
    
    new_content = re.sub(r'href="([^"]+?)"', replace_double_quote, new_content)
    
    # 处理单引号的链接
    def replace_single_quote(match):
        url = match.group(1)
        is_resource = any(url.endswith(ext) for ext in RESOURCE_EXTENSIONS)
        if (not is_resource and 
            not url.endswith('/') and 
            url != '/' and 
            '#' not in url and 
            '?' not in url and
            not url.startswith('http://') and
            not url.startswith('https://') and
            not url.startswith('//')):
            return f"href='{url}/'"
        return match.group(0)
    
    new_content = re.sub(r"href='([^']+?)'", replace_single_quote, new_content)
    
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
