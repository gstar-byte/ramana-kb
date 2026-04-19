#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""正确合并 qa-19~23 内容到 index.html"""

import re

def extract_qa_items(filepath):
    """从 HTML 文件提取所有 qa-item 内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 qa-container 开始
    container_match = re.search(r'<div class="qa-container">(.*?)</div>\s*<div class="pagination">', content, re.DOTALL)
    if not container_match:
        print(f"警告：{filepath} 找不到 qa-container")
        return ''
    
    return container_match.group(1).strip()

def main():
    # 读取 index.html
    with open('pages/qa/index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 读取 qa-19~23
    qa_files = ['pages/qa/qa-19.html', 'pages/qa/qa-20.html', 
                'pages/qa/qa-21.html', 'pages/qa/qa-22.html', 'pages/qa/qa-23.html']
    
    new_items = ''
    total_added = 0
    for qa_file in qa_files:
        items = extract_qa_items(qa_file)
        if items:
            # 统计 qa-item 数量
            count = len(re.findall(r'<div class="qa-item"', items))
            total_added += count
            print(f"从 {qa_file} 提取了 {count} 个问答")
            new_items += '\n' + items
    
    print(f"\n总共提取了 {total_added} 个新问答")
    
    # 在 index.html 中找到正确的插入位置
    # 找到 "</div>" (关闭 qa-list) 后面紧接着分页导航的位置
    # 备份结构: ... </div> (qa-list) \n\n <!-- 分页导航 -->
    
    # 查找 qa-list 关闭 div 后的空行和分页导航
    pattern = r'(</div>\s*\n\s*\n\s*<!-- 分页导航 -->)'
    match = re.search(pattern, index_content)
    
    if match:
        # 在 qa-list 关闭 div 和分页导航之间插入新内容
        insert_pos = match.end()
        new_content = index_content[:insert_pos] + new_items + '\n' + index_content[insert_pos:]
        
        # 写入
        with open('pages/qa/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"\n成功合并到 index.html！")
        print(f"插入位置: 第 {len(index_content[:insert_pos].splitlines())} 行之后")
    else:
        print("错误：找不到正确的插入位置")
        print("尝试备用方案...")
        
        # 备用：查找最后一个 </div> 后面跟着分页导航
        lines = index_content.split('\n')
        insert_line = -1
        for i, line in enumerate(lines):
            if '<!-- 分页导航 -->' in line:
                insert_line = i - 1
                break
        
        if insert_line > 0:
            # 在这行后面插入新内容
            new_lines = lines[:insert_line] + new_items.split('\n') + lines[insert_line:]
            with open('pages/qa/index.html', 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f"备用方案成功！插入位置: 第 {insert_line} 行之后")

if __name__ == '__main__':
    main()
