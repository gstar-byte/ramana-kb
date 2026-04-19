#!/usr/bin/env python3
"""修复 qa/index.html - 删除错误插入的49个问答，用正确格式重新插入"""

import re

# 读取文件
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到分页导航之前的所有 qa-item
pagination_line = None
for i, line in enumerate(lines):
    if 'id="pagination"' in line:
        pagination_line = i
        print(f'分页导航在第 {i+1} 行')
        for j in range(max(0, i-5), i):
            print(f'{j+1}: {lines[j][:100]}')
        break

if pagination_line is None:
    print("没找到分页导航！")
    exit(1)

# 找到 4480-4488 行之间是否是旧的 qa-item 格式
print("\n检查 4485-4490 行的格式：")
for i in range(4485, min(4490, len(lines))):
    print(f"{i+1}: {lines[i][:100]}")
