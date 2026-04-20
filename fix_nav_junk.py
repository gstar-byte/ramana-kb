#!/usr/bin/env python3
"""删除所有 maha-yoga-ch*.html 中残留的第二个 page-nav（指向 be-as-you-are 的垃圾导航）"""
import os, re

BASE = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books'

for i in range(1, 6):
    path = os.path.join(BASE, f'maha-yoga-ch{i}.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 找第二个 page-nav（指向 be-as-you-are 的）
    first = content.find('<div class="page-nav">')
    if first == -1:
        print(f'maha-yoga-ch{i}: 没有 page-nav')
        continue

    second = content.find('<div class="page-nav">', first + 1)
    if second == -1:
        print(f'maha-yoga-ch{i}: 只有一个 page-nav，无需清理')
        continue

    # 确认第二个指向 be-as-you-are
    snippet = content[second:second+200]
    if 'be-as-you-are' not in snippet:
        print(f'maha-yoga-ch{i}: 第二个 page-nav 不是垃圾，跳过')
        continue

    # 找到第二个 page-nav 的结束 </div>
    end = content.find('</div>', second)
    # 还要包含后面紧跟的 whitespace/newline
    after = end + 6  # </div> 长度
    # 往后找 content-wrapper 的结束
    tail = content[after:after+50].lstrip()
    if not tail.startswith('<div class="page-nav">'):
        # 可能后面就是 content-wrapper
        pass

    # 删除从 second 到下一个 </div> 为止的整个 block
    # 更安全的方式：用正则找所有 page-nav，删掉包含 be-as-you-are 的
    def remove_be_nav(m):
        if 'be-as-you-are' in m.group(0):
            return ''
        return m.group(0)

    content2 = re.sub(
        r'<div class="page-nav">.*?</div>',
        remove_be_nav, content, flags=re.DOTALL
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content2)

    count = content2.count('page-nav')
    print(f'✓ 清理 maha-yoga-ch{i}.html，剩余 {count} 个 page-nav')
print('全部完成')
