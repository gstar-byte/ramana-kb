#!/usr/bin/env python3
import re

def read_and_analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有章节标题
    print("=== 章节分析 ===")
    
    # 第一章：HAPPINESS (第4页开始)
    print("\n第一章（HAPPINESS）的内容范围：")
    # 找到第一章开始和第二章开始
    chapter1_start = content.find("HAPPINESS")
    chapter2_start = content.find("THE SELF AND NON-SELF")
    
    if chapter1_start != -1 and chapter2_start != -1:
        chapter1_content = content[chapter1_start:chapter2_start]
        print(f"长度：{len(chapter1_content)} 字符")
        print(f"行数：{chapter1_content.count('\\n')}")
        print(f"\n第一章内容预览（前500字符）：")
        print(chapter1_content[:500])
    
    # 分析各章节长度
    print("\n=== 各章节内容长度对比 ===")
    
    chapters = [
        ("HAPPINESS", "THE SELF AND NON-SELF"),
        ("THE SELF AND NON-SELF", "MIND"),
        ("MIND", "WHO AM I?"),
        ("WHO AM I?", "SURRENDER"),
        ("SURRENDER", "THE THREE STATES"),
        ("THE THREE STATES", "GRACE AND GURU"),
        ("GRACE AND GURU", "SELF-REALIZATION"),
        ("SELF-REALIZATION", "HEART"),
        ("HEART", "RENUNCIATION"),
        ("RENUNCIATION", "FATE AND FREEWILL"),
        ("FATE AND FREEWILL", "JNANI"),
        ("JNANI", "MISCELLANEOUS"),
        ("MISCELLANEOUS", None)
    ]
    
    for i, (start_title, end_title) in enumerate(chapters, 1):
        start_idx = content.find(start_title)
        if start_idx == -1:
            continue
            
        if end_title:
            end_idx = content.find(end_title, start_idx)
        else:
            end_idx = len(content)
            
        chapter_content = content[start_idx:end_idx]
        print(f"第{i}章 ({start_title[:30]}): {len(chapter_content)} 字符, {chapter_content.count('\\n')} 行")
    
    return content

if __name__ == "__main__":
    file_path = "/workspace/pdf_content/gems_from_bhagavan.txt"
    content = read_and_analyze_file(file_path)
