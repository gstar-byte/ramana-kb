import re, glob

# 查找所有 viewport meta 标签被污染的文件
bad_files = []
for f in glob.glob('c:/Users/willp/WorkBuddy/20260410104230/pages/**/*.html', recursive=True):
    c = open(f, encoding='utf-8').read()
    # 找 viewport 中有多余内容的
    match = re.search(r'<meta name="viewport"[^>]+>', c)
    if match:
        tag = match.group(0)
        if '拉玛那' in tag or 'initial-scale' not in tag or len(tag) > 60:
            bad_files.append((f, tag))

print(f'发现 {len(bad_files)} 个文件 viewport 被污染:')
for f, tag in bad_files[:10]:
    print(f'  {f}')
    print(f'  当前: {tag}')
    print()
