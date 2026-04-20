# -*- coding: utf-8 -*-
"""
创建《权威合集》四章章节页面，并更新主页卡片为可点击链接
"""
import os

BASE = r'c:/Users/willp/Desktop/2026年4月/kb01'
BOOKS = os.path.join(BASE, 'pages', 'books')
SRC = os.path.join(BASE, 'pdf_content', 'collected_works.txt')

# 读取原文
with open(SRC, encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')

def get_lines(start, end):
    """获取指定行范围的内容"""
    return '\n'.join(lines[start-1:end])

# ===== 章节内容提取 =====
# 根据分析，文件结构大致如下：
# 行1-~: Self-Enquiry
# 行988-~: Who Am I? 等

# 提取 Upadesa Saram (本心十论) - 约20节诗
# 从 collected_works 中找 Upadesa Saram 部分
# 行 ~1592 附近有 Reality in Forty Verses
# Upadesa Saram 通常在前面的部分

# 让我们找到确切位置
upadesa_start = None
vichara_start = None
for i, l in enumerate(lines):
    s = l.strip()
    if s == 'UPADESA SARAM' or s == 'Upadesa Saram':
        upadesa_start = i + 1
        print(f"Upadesa Saram starts at line {upadesa_start}: {s}")
    if s == 'VICHARA SUTRAM' or s == 'Vichara Sutram':
        vichara_start = i + 1
        print(f"Vichara Sutram starts at line {vichara_start}: {s}")

# 打印 upadesa_start 附近的内容
if upadesa_start:
    print("\n=== Upadesa Saram context ===")
    for i in range(upadesa_start-2, upadesa_start+20):
        if i < len(lines):
            print(f"{i+1}: {lines[i].strip()[:100]}")

# 检查已有的 Self-Enquiry 和 Who Am I 内容
# Who Am I 约在988行
print("\n=== Around line 988 (Who Am I?) ===")
for i in range(986, 1015):
    if i < len(lines):
        print(f"{i+1}: {lines[i].strip()[:100]}")
