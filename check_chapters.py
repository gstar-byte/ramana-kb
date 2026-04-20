import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 检查所有章节页面的flex导航
chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]

needs_fix = []
for f in chapter_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查是否有旧的flex导航
    if 'display:flex;justify-content:space-between' in content and '<div class="card" style="display:flex' in content:
        needs_fix.append(f)

print(f'需要修复的章节页面: {len(needs_fix)}个')
for f in needs_fix[:20]:
    print(f'  - {f}')
