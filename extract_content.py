#!/usr/bin/env python3
import re

def extract_from_gospel():
    """从Maharshi's Gospel中提取相关内容"""
    with open('/workspace/pdf_content/maharshi_gospel.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取关于mind, surrender, guru, heart等的内容
    extracts = {
        'mind': [],
        'surrender': [],
        'guru': [],
        'heart': [],
        'self_realization': [],
        'renunciation': [],
        'jnani': [],
        'three_states': [],
        'fate_freewill': []
    }
    
    # 简单提取一些段落
    lines = content.split('\\n')
    
    # 查找关于mind的内容
    for i, line in enumerate(lines):
        if 'mind' in line.lower() and len(line) > 50:
            context = ' '.join(lines[max(0, i-2):i+3])
            if len(context) > 100:
                extracts['mind'].append(context)
        
        if 'surrender' in line.lower() and len(line) > 50:
            context = ' '.join(lines[max(0, i-2):i+3])
            if len(context) > 100:
                extracts['surrender'].append(context)
        
        if 'guru' in line.lower() or 'grace' in line.lower() and len(line) > 50:
            context = ' '.join(lines[max(0, i-2):i+3])
            if len(context) > 100:
                extracts['guru'].append(context)
        
        if 'heart' in line.lower() and len(line) > 50:
            context = ' '.join(lines[max(0, i-2):i+3])
            if len(context) > 100:
                extracts['heart'].append(context)
    
    return extracts

def extract_from_talks():
    """从Talks with Ramana中提取相关内容"""
    with open('/workspace/pdf_content/talks_with_ramana_1.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    extracts = {
        'mind': [],
        'surrender': [],
        'guru': [],
        'heart': [],
        'self_realization': [],
        'renunciation': [],
        'jnani': [],
        'three_states': [],
        'fate_freewill': []
    }
    
    lines = content.split('\\n')
    
    for i, line in enumerate(lines):
        # 提取一些有用的内容
        keywords = ['who am i', 'self-inquiry', 'mind', 'ego', 'surrender', 'guru', 'heart', 'samadhi', 'jnani']
        for kw in keywords:
            if kw in line.lower() and len(line) > 30:
                context = ' '.join(lines[max(0, i-3):i+4])
                if len(context) > 150:
                    extracts[keywords.index(kw) % len(extracts)].append(context)
    
    return extracts

def extract_from_day_by_day():
    """从Day by Day中提取内容"""
    extracts = {}
    try:
        with open('/workspace/pdf_content/day_by_day.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            # 简单返回一些内容片段
            extracts['general'] = content[:5000]
    except:
        pass
    return extracts

def main():
    print("从Maharshi's Gospel提取内容...")
    gospel_extracts = extract_from_gospel()
    
    print("从Talks with Ramana提取内容...")
    talks_extracts = extract_from_talks()
    
    # 合并所有提取内容
    all_extracts = {}
    for key in gospel_extracts:
        all_extracts[key] = gospel_extracts.get(key, []) + talks_extracts.get(key, [])
    
    print("\n=== 提取结果统计 ===")
    for key, items in all_extracts.items():
        print(f"{key}: {len(items)} 条")
    
    # 保存提取内容
    import json
    with open('/workspace/extracted_content.json', 'w', encoding='utf-8') as f:
        json.dump(all_extracts, f, ensure_ascii=False, indent=2)
    
    print("\n提取内容已保存到 /workspace/extracted_content.json")

if __name__ == "__main__":
    main()
