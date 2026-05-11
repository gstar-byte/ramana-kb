#!/usr/bin/env python3
"""批量修复概念页面缺少favicon的问题"""

import re
from pathlib import Path

BASE = Path("F:/26年4月/kb01/pages/concepts")

# 需要添加favicon的页面
MISSING = [
    "vichara.html", "sharanagati.html", "lakshya.html",
    "manonasha.html", "prarabdha.html", "jiva.html",
    "prana.html", "viveka.html", "vasanas.html",
    "avidya.html", "satya.html", "shiva.html"
]

FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'%3E%3Ctext y=\'.9em\' font-size=\'90\'%3E🙏%3C/text%3E%3C/svg%3E">'

for fname in MISSING:
    fpath = BASE / fname
    if not fpath.exists():
        print(f"  ❌ 文件不存在: {fname}")
        continue
    
    content = fpath.read_text(encoding="utf-8")
    
    if 'rel="icon"' in content:
        print(f"  ⏭️  {fname} 已有favicon，跳过")
        continue
    
    # 在 <link rel="stylesheet" href="../styles.css"> 之后添加favicon
    # 匹配：<link rel="stylesheet" href="../styles.css"> 可选空白换行
    pattern = r'(<link rel="stylesheet" href="\.\./styles\.css">)\s*\n'
    
    def replacer(m):
        return m.group(0) + "\n" + FAVICON + "\n"
    
    new_content = re.sub(pattern, replacer, content)
    
    if new_content == content:
        print(f"  ⚠️  {fname}: 无法找到插入位置")
        continue
    
    fpath.write_text(new_content, encoding="utf-8")
    print(f"  ✅ {fname}: 已添加favicon")
