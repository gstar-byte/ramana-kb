#!/usr/bin/env python3
"""
批量删除 pages/books/*.html 中与 script.js 冲突的内联 <script> 块
保留 <script src="../script.js"> 不变
"""
import os
import re

books_dir = r"c:\Users\willp\Desktop\2026年4月\kb01\pages\books"

# 匹配内联 script 块（含 sidebar-section-title 的那个）
# 模式：<script> ... querySelectorAll('.sidebar-section-title') ... </script>
INLINE_SCRIPT_PATTERN = re.compile(
    r'\s*<script>\s*(?:function toggleSidebar\(\)[\s\S]*?)?document\.querySelectorAll\([\'"]\.sidebar-section-title[\'"]\)[\s\S]*?</script>',
    re.DOTALL
)

fixed = 0
skipped = 0

for fname in os.listdir(books_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(books_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    new_content, n = INLINE_SCRIPT_PATTERN.subn('', content)
    if n > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ 修复 {fname}（删除 {n} 个内联脚本块）")
        fixed += 1
    else:
        skipped += 1

print(f"\n完成：{fixed} 个文件修复，{skipped} 个文件无需修改")
