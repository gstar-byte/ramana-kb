"""
批量修复 index/ 链接为目录链接
- books/index/ → books/
- concepts/index/ → concepts/
- 仅处理内部链接，不改外部 URL
"""
import re
import os

BASE = '/workspace/pages'

# 正则：匹配 href="xxx/index/" 或 href='xxx/index/'
INDEX_LINK_RE = re.compile(r'(href=["\'])([^\"\']+\/index\/)(["\'])')
# 正则：匹配 href="xxx/index#..." 或 href='xxx/index#...'
INDEX_HASH_RE = re.compile(r'(href=["\'])([^\"\']+\/index)(#.*?)(["\'])')


def fix_url(url):
    """将 index/ 转换为目录链接"""
    if url.endswith('/index/'):
        return url[:-6] + '/'  # 变成 books/ 而不是 books/index/
    return url


def fix_url_with_hash(url_with_hash):
    """处理带锚点的 index 链接"""
    # URL 格式是 path/index#hash
    if url_with_hash and '/index' in url_with_hash:
        # 分割路径和锚点
        if '#' in url_with_hash:
            path_part, hash_part = url_with_hash.split('#', 1)
            if path_part.endswith('/index'):
                path_part = path_part[:-5] + '/'
                return path_part + '#' + hash_part
    return url_with_hash


def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # 先修复带哈希的链接
    def fix_hash_replacer(m):
        prefix = m.group(1)
        url = m.group(2)
        hash_part = m.group(3)
        suffix = m.group(4)
        fixed = fix_url_with_hash(url + hash_part)
        return prefix + fixed + suffix

    new_content = INDEX_HASH_RE.sub(fix_hash_replacer, content)
    
    # 再修复普通的 index/ 链接
    def fix_index_replacer(m):
        prefix = m.group(1)
        url = m.group(2)
        suffix = m.group(3)
        return prefix + fix_url(url) + suffix

    new_content = INDEX_LINK_RE.sub(fix_index_replacer, new_content)

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
