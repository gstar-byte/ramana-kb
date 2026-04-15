#!/usr/bin/env python3
"""修复汉堡菜单高度，所有断点统一增加2px"""

import re

with open('pages/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义需要修改的断点及其汉堡菜单样式
# 查找所有 @media 块中的 .hamburger 定义

# 断点 900-1024px
content = re.sub(
    r'@media \(min-width: 900px\) and \(max-width: 1024px\) \{[\s\S]*?/\* 汉堡菜单[\s\S]*?\.hamburger \{[\s\S]*?height: 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

# 断点 1025-1200px
content = re.sub(
    r'@media \(min-width: 1025px\) and \(max-width: 1200px\) \{[\s\S]*?/\* 汉堡菜单[\s\S]*?\.hamburger \{[\s\S]*?height: 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

# 断点 768-900px
content = re.sub(
    r'@media \(min-width: 768px\) and \(max-width: 900px\) \{[\s\S]*?\.hamburger \{[\s\S]*?height: 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

# 断点 <768px
content = re.sub(
    r'@media \(max-width: 767px\) \{[\s\S]*?\.hamburger \{[\s\S]*?height: 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

# 同时修改 topbar-nav a 的高度也要增加2px
content = re.sub(
    r'(\.topbar-nav a \{[\s\S]*?height:) 42px;',
    r'\g<1> 42px;  /* 保持不变 */',
    content
)

# 修改顶部导航高度也要增加2px（保持对齐）
content = re.sub(
    r'(@media \(min-width: 768px\) and \(max-width: 900px\) \{[\s\S]*?\.topbar \{[\s\S]*?height:) 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

content = re.sub(
    r'(@media \(min-width: 900px\) and \(max-width: 1024px\) \{[\s\S]*?\.topbar \{[\s\S]*?height:) 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

content = re.sub(
    r'(@media \(min-width: 1025px\) and \(max-width: 1200px\) \{[\s\S]*?\.topbar \{[\s\S]*?height:) 44px;',
    lambda m: m.group(0).replace('height: 44px;', 'height: 46px;'),
    content
)

# 修改 .main-content 的 margin-top
content = re.sub(
    r'(\.main-content \{[\s\S]*?margin-top:) 44px;',
    lambda m: m.group(0).replace('margin-top: 44px;', 'margin-top: 46px;'),
    content
)

with open('pages/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("汉堡菜单和顶部导航高度已统一增加到 46px")
