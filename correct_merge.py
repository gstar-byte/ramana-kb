#!/usr/bin/env python3
"""正确合并49个新QA到index.html"""

import os
import re

# 读取主文件
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    main_lines = f.readlines()

print(f"主文件行数: {len(main_lines)}")

# 找到 </div> 关闭 qa-list 的行（在分页导航之前）
close_div_line = None
for i, line in enumerate(main_lines):
    if 'id="pagination"' in line:
        close_div_line = i - 2  # 往前两行找 </div>
        break

print(f"</div> 在第 {close_div_line + 1} 行")

# 读取要插入的内容
new_items = []
files_to_read = [
    'c:/Users/willp/WorkBuddy/20260410104230/pages/qa/qa-19.html',
    'c:/Users/willp/WorkBuddy/20260410104230/pages/qa/qa-20.html',
    'c:/Users/willp/WorkBuddy/20260410104230/pages/qa/qa-21.html',
    'c:/Users/willp/WorkBuddy/20260410104230/pages/qa/qa-22.html',
    'c:/Users/willp/WorkBuddy/20260410104230/pages/qa/qa-23.html',
]

for filepath in files_to_read:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 qa-item
        items = re.findall(r'<div class="qa-item"[^>]*>.*?</div>\s*</div>', content, re.DOTALL)
        new_items.extend(items)
        print(f"从 {os.path.basename(filepath)} 读取了 {len(items)} 个问答")

print(f"\n总共读取了 {len(new_items)} 个新问答")

# 转换旧格式为新格式
def convert_to_new_format(html):
    """转换旧格式 qa-item 为新格式"""
    # 提取问题和答案
    q_match = re.search(r'<div class="qa-question">.*?<h3>([^<]+)</h3>', html, re.DOTALL)
    a_match = re.search(r'<div class="qa-answer">.*?<p>([^<]+)</p>', html, re.DOTALL)
    
    if q_match and a_match:
        return html  # 已经是新格式
    
    # 处理旧格式
    q_match = re.search(r'<div class="qa-q">([^<]+)</div>', html)
    a_match = re.search(r'<div class="qa-a">([^<]+)</div>', html)
    
    if q_match and a_match:
        q = q_match.group(1).strip()
        a = a_match.group(1).strip()
        return f'''<div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>{q}</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>{a}</p>
                            </div>
                        </div>
                    </div>'''
    return None

converted_items = []
for item in new_items:
    converted = convert_to_new_format(item)
    if converted:
        converted_items.append(converted)

print(f"转换了 {len(converted_items)} 个问答为新格式")

# 重建文件
# 在 </div> 之前插入新内容
new_lines = []
new_lines.extend(main_lines[:close_div_line])  # 到 </div> 之前
new_lines.extend(converted_items)  # 新格式的内容
new_lines.append(main_lines[close_div_line])  # </div>
new_lines.extend(main_lines[close_div_line+1:])  # 剩余内容

# 写回文件
new_content = ''.join(new_lines)
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\n新文件行数: {len(new_lines)}")

# 验证
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    final_content = f.read()
    qa_count = final_content.count('class="qa-item"')
    print(f"qa-item 总数: {qa_count}")
    
# 计算页数
pages = (qa_count + 14) // 15
print(f"预计页数: {pages}")
