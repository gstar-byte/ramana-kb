#!/usr/bin/env python3
"""修复 lang-toggle 竖条问题：批量给没有 border-left 的 lang-toggle 添加分隔线"""
import os
import re

BASE = r"F:\26年4月\kb01\pages"

# Pattern: class="lang-toggle" followed by style= OR just class="lang-toggle"
# We want to add style="border-left:1px solid rgba(255,255,255,.3);" to those without it
pattern_no_style = re.compile(
    r'<a (href="#") class="lang-toggle"( style="border-left:[^"]*")?([^>]*)>繁</a>'
)
# But we only want to fix those WITHOUT the style

pattern = re.compile(
    r'<a href="#" class="lang-toggle"(?! style="border-left)([^>]*)>繁</a>'
)
pattern_trad = re.compile(
    r'<a href="#" class="lang-toggle"(?! style="border-left)([^>]*)>簡</a>'
)

count = 0
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        original = content
        changed = False

        # Fix 繁 (simplified)
        def add_border_simp(m):
            attrs = m.group(1)
            return f'<a href="#" class="lang-toggle" style="border-left:1px solid rgba(255,255,255,.3);"{attrs}>繁</a>'

        new_content = pattern.sub(add_border_simp, content)
        if new_content != content:
            changed = True
            content = new_content

        # Fix 簡 (traditional)
        def add_border_trad(m):
            attrs = m.group(1)
            return f'<a href="#" class="lang-toggle" style="border-left:1px solid rgba(255,255,255,.3);"{attrs}>簡</a>'

        new_content = pattern_trad.sub(add_border_trad, content)
        if new_content != content:
            changed = True
            content = new_content

        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            rel = os.path.relpath(fpath, BASE)
            print(f"[FIXED] {rel}")
            count += 1

print(f"\n总计修复 {count} 个文件")
