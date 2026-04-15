# -*- coding: utf-8 -*-
"""提取EPUB前20个章节的关键内容"""
import re

input_file = r"c:/Users/willp/WorkBuddy/20260410104230/epub_content/epub_full_text.txt"
output_file = r"c:/Users/willp/WorkBuddy/20260410104230/epub_content/key_chapters.txt"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 按章节分割
chapters = re.split(r'=== (text\d+\.html) ===', content)

print(f"总字符数: {len(content)}")
print(f"章节数: {len(chapters) // 2}")

# 提取前20个章节，每个取前4000字符
key_content = []
for i in range(1, min(41, len(chapters)), 2):  # 前20个
    filename = chapters[i]
    text = chapters[i+1] if i+1 < len(chapters) else ""
    if text and len(text) > 100:
        key_content.append(f"\n{'='*40}\n{filename}\n{'='*40}\n{text[:4000]}")

# 保存
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(key_content))

print(f"\n已提取 {len(key_content)} 个关键章节")
print(f"保存到: {output_file}")

# 打印每个章节的前200字符作为预览
print("\n" + "="*50)
print("章节预览:")
print("="*50)
for i in range(1, min(41, len(chapters)), 2):
    filename = chapters[i]
    text = chapters[i+1] if i+1 < len(chapters) else ""
    preview = text[:200].replace('\n', ' ').strip() if text else "(空)"
    print(f"\n{filename}:")
    print(f"  {preview}...")
