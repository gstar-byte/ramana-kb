import re, glob

# 找所有文件里 serviceWorker.register 前的 <script> 标签
bad_files = []
for f in glob.glob('c:/Users/willp/WorkBuddy/20260410104230/pages/**/*.html', recursive=True):
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    # 找 serviceWorker.register 的上下文
    if 'serviceWorker.register' in c:
        # 检查前面100个字符内有没有 <script
        idx = c.find('serviceWorker.register')
        before = c[max(0, idx-200):idx]
        if '<script' not in before and '<script>' not in before:
            bad_files.append(f)

print(f'发现 {len(bad_files)} 个文件 SW 代码缺少 <script> 标签:')
for f in bad_files[:10]:
    print(f'  {f}')
