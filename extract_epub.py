# -*- coding: utf-8 -*-
"""批量提取EPUB所有章节文本"""
import os
import re

epub_dir = r"c:/Users/willp/WorkBuddy/20260410104230/epub_content/OEBPS"
output_file = r"c:/Users/willp/WorkBuddy/20260410104230/epub_content/epub_full_text.txt"

def extract_text_from_html(html_content):
    """从HTML提取纯文本"""
    # 提取body内容
    match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
    if match:
        body = match.group(1)
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', ' ', body)
        # 清理空白
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return ""

files = sorted([f for f in os.listdir(epub_dir) if f.startswith('text') and f.endswith('.html')])

all_content = []
for i, filename in enumerate(files):
    filepath = os.path.join(epub_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    text = extract_text_from_html(content)
    if text:
        all_content.append(f"=== {filename} ===\n{text}\n")
        print(f"[{i+1}/{len(files)}] {filename}")

# 保存完整内容
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n\n".join(all_content))

print(f"\n完成！共提取 {len(all_content)} 个章节")
print(f"保存到: {output_file}")
