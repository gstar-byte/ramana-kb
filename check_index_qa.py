import re
from collections import defaultdict

with open('pages/qa/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 提取所有问题
questions = re.findall(r'<h3>问：(.*?)</h3>', content)
print(f'总问题数: {len(questions)}')

# 检查重复
duplicates = defaultdict(list)
for i, q in enumerate(questions):
    q_clean = q.strip()
    duplicates[q_clean].append(i+1)

dups = {q: lines for q, lines in duplicates.items() if len(lines) > 1}
print(f'重复问题数: {len(dups)}')

if dups:
    print('\n重复的问题:')
    for q, lines in list(dups.items())[:10]:
        print(f'  "{q[:40]}..." 出现在第 {lines} 个')
