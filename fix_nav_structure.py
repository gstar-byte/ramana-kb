#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 修复 be-as-you-are 章节
for i in range(1, 10):
    f = f'be-as-you-are-ch{i}.html'
    
    if not os.path.exists(f):
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查是否有损坏的结构：</div> class="site-footer">
    if '</div> class="site-footer">' in content:
        print(f'{f}: 发现损坏的footer结构')
        
        # 修复：添加 <div class="card"> 包裹导航
        # 找到模式：<div style="display:flex;...">...</div> class="site-footer">
        pattern = r'(<div style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="[^"]*" class="tag">[^<]*</a>\s*<a href="[^"]*" class="tag">[^<]*</a>\s*</div>) class="site-footer">'
        replacement = r'<!-- 章节导航 -->\n                <div class="card">\n                    \1\n                </div>\n            </div>\n\n            <footer class="site-footer">'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'  -> 已修复')
        else:
            print(f'  -> 修复失败')
    else:
        # 检查是否有正确的章节导航结构
        if '<!-- 章节导航 -->' not in content and '<div style="display:flex;justify-content:space-between;align-items:center;">' in content:
            print(f'{f}: 缺少章节导航注释和card包裹')
            
            # 修复：添加注释和card包裹
            pattern = r'(<div style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="[^"]*" class="tag">[^<]*</a>\s*<a href="[^"]*" class="tag">[^<]*</a>\s*</div>)\s*</div>\s*<footer'
            replacement = r'<!-- 章节导航 -->\n                <div class="card">\n                    \1\n                </div>\n            </div>\n\n            <footer'
            
            new_content = re.sub(pattern, replacement, content)
            
            if new_content != content:
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'  -> 已修复')
            else:
                print(f'  -> 修复失败')

print('\n检查完成!')
