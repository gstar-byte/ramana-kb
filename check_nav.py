import re

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'
with open(f'{BASE}\\index.html', encoding='utf-8') as f:
    c = f.read()

hrefs = re.findall(r'href=["\']([^"\']+)["\']', c)

# 检查所有链接
for h in hrefs:
    # 排除外部/特殊
    if h.startswith('http') or h.startswith('//') or h.startswith('#') or '.' in h:
        continue
    # 打印看起来有问题的（顶级目录但可能漏了子目录）
    print(h)
