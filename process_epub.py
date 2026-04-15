# -*- coding: utf-8 -*-
"""处理EPUB内容，提取关键章节"""
import re

input_file = r"c:/Users/willp/WorkBuddy/20260410104230/epub_content/epub_full_text.txt"
output_file = r"c:/Users/willp/WorkBuddy/20260410104230/epub_content/key_chapters.txt"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 按章节分割
chapters = re.split(r'=== (text\d+\.html) ===', content)

print(f"总字符数: {len(content)}")
print(f"章节数: {len(chapters) // 2}")

# 提取关键章节内容
key_chapters = {
    '走向静默_简介': [],
    '核心教义': [],
    '参究自我': [],
    '心智本质': [],
    '三摩地': [],
    '问答精选': [],
    '其他精华': []
}

current_section = '其他精华'

# 分析每个章节的内容
for i in range(1, len(chapters), 2):
    filename = chapters[i]
    text = chapters[i+1] if i+1 < len(chapters) else ""
    
    # 检测章节类型
    text_lower = text.lower()
    
    if '作者' in text and len(text) < 3000:
        current_section = '走向静默_简介'
        key_chapters[current_section].append(f"\n--- {filename} ---\n{text[:3000]}")
    elif '我是谁' in text or '自我' in text or '参究' in text:
        if len(text) > 500:
            current_section = '核心教义'
            key_chapters[current_section].append(f"\n--- {filename} ---\n{text[:5000]}")
    elif '心智' in text and len(text) > 1000:
        current_section = '心智本质'
        key_chapters[current_section].append(f"\n--- {filename} ---\n{text[:5000]}")
    elif '三摩地' in text or '禅定' in text:
        if len(text) > 500:
            current_section = '三摩地'
            key_chapters[current_section].append(f"\n--- {filename} ---\n{text[:5000]}")
    elif '问：' in text and '答：' in text:
        current_section = '问答精选'
        key_chapters[current_section].append(f"\n--- {filename} ---\n{text[:8000]}")
    else:
        if len(text) > 2000 and len(text) < 10000:
            key_chapters[current_section].append(f"\n--- {filename} ---\n{text[:3000]}")

# 保存关键内容
with open(output_file, 'w', encoding='utf-8') as f:
    for section, contents in key_chapters.items():
        if contents:
            f.write(f"\n\n{'='*50}\n{section}\n{'='*50}\n")
            f.write("\n".join(contents))

print(f"\n关键章节已保存到: {output_file}")
print("\n各部分字符数:")
for section, contents in key_chapters.items():
    total = sum(len(c) for c in contents)
    print(f"  {section}: {total} 字符")
