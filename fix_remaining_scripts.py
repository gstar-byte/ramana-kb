#!/usr/bin/env python3
"""修复剩余5个文件的内联脚本冲突"""
import os, re

files = [
    r"c:\Users\willp\Desktop\2026年4月\kb01\pages\graph.html",
    r"c:\Users\willp\Desktop\2026年4月\kb01\pages\index.html",
    r"c:\Users\willp\Desktop\2026年4月\kb01\pages\concepts\mind.html",
    r"c:\Users\willp\Desktop\2026年4月\kb01\pages\qa\index.html",
    r"c:\Users\willp\Desktop\2026年4月\kb01\pages\qa\index_fixed.html",
]

# 更宽松的匹配：<script> 块中只要含有 sidebar-section-title 就整个删掉
# 注意：匹配 <script> 到 </script>，但块中需要含目标字符串
BLOCK_PATTERN = re.compile(r'<script>(?:(?!</script>)[\s\S])*?sidebar-section-title[\s\S]*?</script>', re.DOTALL)

for fpath in files:
    if not os.path.exists(fpath):
        print(f"⚠ 不存在: {fpath}")
        continue
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    new_content, n = BLOCK_PATTERN.subn('', content)
    if n > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ 修复 {os.path.basename(fpath)} ({n}个块)")
    else:
        print(f"- 未匹配 {os.path.basename(fpath)}")
