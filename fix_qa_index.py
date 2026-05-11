#!/usr/bin/env python3
"""转换 zh-TW/qa/index.html 中剩余的简体 JS 文字"""
import re

INPUT = r"F:\26年4月\kb01\pages\zh-TW\qa\index.html"

with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix page info text
content = content.replace(
    "`第 ${page} / ${totalPages} 页，共 ${filteredItems.length} 条`",
    "`第 ${page} / ${totalPages} 頁，共 ${filteredItems.length} 條`"
)

# Check what remains
import re
# Find all JS string literals (single or double quoted)
strings = re.findall(r'["\`]([^`\n]*?(?:问|答|页|条|加载|精选)[^`\n]*?)["\`]', content)
for s in strings[:20]:
    print(repr(s[:80]))

with open(INPUT, 'w', encoding='utf-8') as f:
    f.write(content)
