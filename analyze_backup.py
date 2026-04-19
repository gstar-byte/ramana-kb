#!/usr/bin/env python3
"""分析备份文件，找到正确的结构"""

with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"总行数: {len(lines)}")

# 找到 qa-list 容器
for i, line in enumerate(lines):
    if 'id="qaList"' in line:
        print(f'qaList 开始于第 {i+1} 行')

# 找到 </div> 关闭 qa-list 容器（在分页导航之前）
# 分页导航前通常有一个 </div> 来关闭 qa-list
for i, line in enumerate(lines):
    if 'id="pagination"' in line:
        print(f'分页导航在第 {i+1} 行')
        # 显示前几行
        for j in range(max(0, i-3), i+1):
            print(f'{j+1}: {lines[j][:100]}')
        break

# 找到 footer 之前的最后一个 qa-item
for i in range(len(lines)-1, 0, -1):
    if 'class="qa-item"' in lines[i]:
        print(f'最后一个 qa-item 在第 {i+1} 行: {lines[i][:80]}')
        break

# 统计 qa-item 数量
count = sum(1 for line in lines if 'class="qa-item"' in line)
print(f'\nqa-item 总数: {count}')
