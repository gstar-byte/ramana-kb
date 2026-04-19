import re
import os

def extract_qa_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    items = []
    container = re.search(r'<div class="qa-container">(.*?)<div class="pagination">', content, re.DOTALL)
    if container:
        container_content = container.group(1)
        starts = [m.start() for m in re.finditer(r'<div class="qa-item">', container_content)]
        
        for i, start in enumerate(starts):
            end = len(container_content)
            if i + 1 < len(starts):
                end = starts[i + 1]
            
            item = container_content[start:end].rstrip()
            if item.endswith('</div>'):
                item = item[:-6]
            
            items.append(item.strip())
    
    return items

def convert_to_index_format(item_content):
    """将 qa-q 和 qa-a 转换为 index.html 格式"""
    q_match = re.search(r'class="qa-q">(.*?)<\/div>', item_content, re.DOTALL)
    a_match = re.search(r'class="qa-a">(.*?)<\/div>', item_content, re.DOTALL)
    
    if not q_match:
        print(f"  WARNING: No question found")
        return None
    if not a_match:
        print(f"  WARNING: No answer found")
        return None
    
    question = q_match.group(1).strip()
    answer = a_match.group(1).strip()
    
    return f'''                    <div class="qa-item" data-category="修行">
                        <div class="qa-question">
                            <span class="qa-icon">❓</span>
                            <div class="qa-content">
                                <h3>{question}</h3>
                                <p class="qa-meta">来源：精选问答 | 主题：修行</p>
                            </div>
                        </div>
                        <div class="qa-answer">
                            <span class="qa-icon">💡</span>
                            <div class="qa-content">
                                <p>{answer}</p>
                            </div>
                        </div>
                    </div>'''

# 主程序
print("Starting merge...")

# 提取所有新内容
all_new_items = []
for i in range(19, 24):
    filepath = f'pages/qa/qa-{i}.html'
    if os.path.exists(filepath):
        items = extract_qa_from_file(filepath)
        print(f"qa-{i}: {len(items)} items")
        for item in items:
            converted = convert_to_index_format(item)
            if converted:
                all_new_items.append(converted)

print(f"Total new items: {len(all_new_items)}")

# 恢复备份并重新读取
with open('pages/qa/index.html.backup', 'r', encoding='utf-8') as f:
    index_content = f.read()

# 找到插入位置
insert_marker = '✨ 更多问答正在整理中'
insert_pos = index_content.find(insert_marker)

if insert_pos != -1:
    insert_content = '\n\n'.join(all_new_items) + '\n\n                '
    new_content = index_content[:insert_pos] + insert_content + index_content[insert_pos:]
    
    with open('pages/qa/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully merged {len(all_new_items)} items into index.html")
else:
    print("ERROR: Could not find insert marker!")
