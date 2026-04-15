#!/usr/bin/env python3
"""修复HTML文件中的链接路径问题"""

import os
import re

pages_dir = r"c:/Users/willp/WorkBuddy/20260410104230/pages"

# 需要检查和修复的文件模式
fixes = [
    # books/目录下的章节页，书籍链接应指向 ../index.html
    {
        "dir": "books",
        "pattern": r'href="index\.html" class="active">书籍',
        "replace": 'href="../index.html" class="active">书籍',
        "desc": "修复books子目录中书籍链接"
    },
    # concepts/目录下的页面，概念链接应指向 ../index.html
    {
        "dir": "concepts",
        "pattern": r'href="index\.html" class="active">概念',
        "replace": 'href="../index.html" class="active">概念',
        "desc": "修复concepts子目录中概念链接"
    },
    # methods/目录下的页面
    {
        "dir": "methods",
        "pattern": r'href="index\.html" class="active">方法',
        "replace": 'href="../index.html" class="active">方法',
        "desc": "修复methods子目录中方法链接"
    },
    # qa/目录下的页面
    {
        "dir": "qa",
        "pattern": r'href="index\.html" class="active">问答',
        "replace": 'href="../index.html" class="active">问答',
        "desc": "修复qa子目录中问答链接"
    },
    # persons/目录下的页面
    {
        "dir": "persons",
        "pattern": r'href="index\.html" class="active">人物',
        "replace": 'href="../index.html" class="active">人物',
        "desc": "修复persons子目录中人物链接"
    }
]

total_fixed = 0

for fix in fixes:
    dir_path = os.path.join(pages_dir, fix["dir"])
    if not os.path.exists(dir_path):
        print(f"跳过: {dir_path} 不存在")
        continue
    
    files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
    count = 0
    
    for filename in files:
        filepath = os.path.join(dir_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否需要修复
            if re.search(fix["pattern"], content):
                # 执行替换
                new_content = re.sub(fix["pattern"], fix["replace"], content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
        except Exception as e:
            print(f"  错误 {filename}: {e}")
    
    if count > 0:
        print(f"✓ {fix['desc']}: 修复了 {count} 个文件")
        total_fixed += count

print(f"\n总共修复: {total_fixed} 个文件")
