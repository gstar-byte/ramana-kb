#!/usr/bin/env python3
"""使用正则修复图谱节点"""

import re

with open('/workspace/pages/zh-TW/graph.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式匹配并替换
patterns = [
    # 拉玛那
    (r'"name": "🙏 拉玛那"', '"name": "🙏 拉瑪那"'),
    (r'"name": "🏔️ 阿鲁那佳拉"', '"name": "🏔️ 阿魯那佳拉"'),
    (r'"name": "🔍 谁在问？"', '"name": "🔍 誰在問？"'),
    (r'"name": "💫 觉知"', '"name": "💫 覺知"'),
    (r'"name": "🔮 参究"', '"name": "🔮 參究"'),
    (r'"name": "👩 南达妈"', '"name": "👩 南達媽"'),
]

for pattern, replacement in patterns:
    content = re.sub(pattern, replacement, content)

# 简单的字符串替换
simple_replacements = [
    ("拉玛那", "拉瑪那"),
    ("阿鲁那", "阿魯那"),
]

for old, new in simple_replacements:
    content = content.replace(old, new)

with open('/workspace/pages/zh-TW/graph.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("修复完成！")

# 验证
with open('/workspace/pages/zh-TW/graph.html', 'r', encoding='utf-8') as f:
    content = f.read()

if "拉瑪那" in content:
    print("✓ 拉瑪那 替换成功")
if "阿魯那" in content:
    print("✓ 阿魯那 替换成功")
