#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books\be-as-you-are-ch1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到并替换乱码部分 - 使用简单字符串替换
old_str = '''                
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span></span>
                        <a href="be-as-you-are-ch2.html" class="tag">🔹 下一章</a>
                    </div>
                
            </div>'''

new_str = '''                <!-- 章节导航 -->
                <div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span></span>
                        <a href="be-as-you-are-ch2.html" class="tag">🔹 下一章</a>
                    </div>
                </div>
            </div>'''

# 尝试找到实际的乱码字符
if '\x01' in content and '\x02' in content:
    # 使用正则替换
    pattern = r'\x01\s*(<div style="display:flex;justify-content:space-between;align-items:center;">\s*<span></span>\s*<a href="be-as-you-are-ch2\.html" class="tag">🔹 下一章</a>\s*</div>)\s*\x02'
    replacement = r'<!-- 章节导航 -->\n                <div class="card">\n                    \1\n                </div>'
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books\be-as-you-are-ch1.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print('已修复 be-as-you-are-ch1.html (使用正则)')
    else:
        print('正则未匹配到')
else:
    print('未找到乱码字符')
