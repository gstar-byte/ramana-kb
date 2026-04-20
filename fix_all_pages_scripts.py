#!/usr/bin/env python3
"""
批量删除 pages/ 所有子目录 .html 中与 script.js 冲突的内联 <script> 块
（仅删除含 querySelectorAll('.sidebar-section-title') 的内联块）
"""
import os
import re

base_dir = r"c:\Users\willp\Desktop\2026年4月\kb01\pages"

# 匹配含 sidebar-section-title 的内联 script 块
INLINE_SCRIPT_PATTERN = re.compile(
    r'\s*<script>\s*(?:function toggleSidebar\(\)[\s\S]*?)?document\.querySelectorAll\([\'"]\.sidebar-section-title[\'"]\)[\s\S]*?</script>',
    re.DOTALL
)

fixed = 0
skipped = 0

for root, dirs, files in os.walk(base_dir):
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, encoding='utf-8') as f:
            content = f.read()
        
        new_content, n = INLINE_SCRIPT_PATTERN.subn('', content)
        if n > 0:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            rel = fpath.replace(base_dir, '').lstrip('/\\')
            print(f"✓ {rel}")
            fixed += 1
        else:
            skipped += 1

print(f"\n完成：{fixed} 个文件修复，{skipped} 个文件无需修改")
