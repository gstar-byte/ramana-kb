# -*- coding: utf-8 -*-
"""移除所有页面的 favicon"""

import os
import re

def fix_favicon(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 移除 favicon 相关标签
    if 'rel="icon"' in content:
        content = re.sub(r'    <link rel="icon"[^>]*>\n', '', content)
        modified = True
    if 'rel="apple-touch-icon"' in content:
        content = re.sub(r'    <link rel="apple-touch-icon"[^>]*>\n', '', content)
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {filepath}')

for root, dirs, files in os.walk('pages'):
    for f in files:
        if f.endswith('.html'):
            fix_favicon(os.path.join(root, f))
