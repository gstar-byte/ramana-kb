#!/usr/bin/env python3
"""修复 qa/index.html - 删除错误插入的49个问答，用正确格式重新插入"""

import re

# 读取文件
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.splitlines()

# 找到第4488行（</div> 关闭 qa-list）之后到分页导航之前的所有旧格式 qa-item
# 这些是新插入的错误内容（4490-4686行）
# 找到 </div> 关闭 qa-list 的行（在分页导航之前）
close_div_line = None
pagination_start = None

for i, line in enumerate(lines):
    if i >= 4485 and 'qa-q' in line:
        continue
    if '</div>' in line and close_div_line is None:
        close_div_line = i
    if 'pagination' in line and 'id="pagination"' in line:
        pagination_start = i
        break

print(f"找到 </div> 在第 {close_div_line + 1} 行")
print(f"找到分页在第 {pagination_start + 1} 行")

# 提取错误的内容（4490行到分页开始之前）
error_content_lines = lines[4489:pagination_start]
error_content = '\n'.join(error_content_lines)
print(f"错误内容行数: {len(error_content_lines)}")

# 提取旧格式的问答
old_items = re.findall(r'<div class="qa-item">\s*<div class="qa-q">([^<]+)</div>\s*<div class="qa-a">([^<]+)</div>\s*</div>', error_content)
print(f"找到 {len(old_items)} 个旧格式问答")

# 转换旧格式为新格式
new_items_html = []
for q, a in old_items:
    q_clean = q.strip()
    a_clean = a.strip()
    new_item = f'''                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>❓ {q_clean}</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>{a_clean}</p>
                            </div>
                        </div>
                    </div>'''
    new_items_html.append(new_item)

print(f"转换了 {len(new_items_html)} 个问答")

# 重建文件内容
# 保留 1-4489 行（到 </div> 为止，包括这个 div）
# 然后插入新格式的内容
# 然后是分页导航和之后的内容

# 找到 </div> 那一行的缩进
close_div_indent = lines[close_div_line].count(' ') - len(lines[close_div_line].lstrip())
close_div_indent = max(0, close_div_indent)

# 在 </div> 之前插入新内容（保持相同缩进）
new_content_lines = []
new_content_lines.extend(lines[:close_div_line])  # 到 </div> 之前
new_content_lines.extend(new_items_html)  # 新格式的内容
new_content_lines.append(lines[close_div_line])  # </div>
new_content_lines.extend(lines[pagination_start:])  # 分页和之后的内容

# 写回文件
new_content = '\n'.join(new_content_lines)
with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("修复完成！")
print(f"新文件总行数: {len(new_content_lines)}")
