#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 generate_search_india_chapters.py 中数据字符串里嵌套的ASCII双引号
策略：找到长中文内容行中的 "词" 模式（双引号包裹的短词），替换为「词」
"""
import re

filepath = 'c:/Users/willp/Desktop/2026年4月/kb01/generate_search_india_chapters.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
fixed_lines = []
changes = []

for i, line in enumerate(lines, 1):
    # 只处理前240行（数据区域）
    if i > 240:
        fixed_lines.append(line)
        continue

    # 检测：行中是否有 "短词" 模式（双引号包裹2-8个中文字符）
    # 这种情况是内容字符串中引用专有名词
    # 匹配：中文字符 + " + 1-8个字符 + " + 中文字符 or ：
    pattern = r'(?<=[^\s])"([^"]{1,12})"(?=[^\s])'
    
    if re.search(pattern, line):
        new_line = re.sub(pattern, r'「\1」', line)
        if new_line != line:
            changes.append((i, line.strip()[:100], new_line.strip()[:100]))
        fixed_lines.append(new_line)
    else:
        fixed_lines.append(line)

print(f"共修改 {len(changes)} 行:")
for ln, old, new in changes:
    print(f"  Line {ln}:")
    print(f"    OLD: {old}")
    print(f"    NEW: {new}")

# 写回文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(fixed_lines))

print("\n已写回文件，验证语法...")
import ast
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        src = f.read()
    ast.parse(src)
    print("语法检查通过！")
except SyntaxError as e:
    print(f"仍有语法错误: {e}")
