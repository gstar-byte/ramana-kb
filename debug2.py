import re
import os

def extract_qa_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    items = []
    # 找到 qa-container
    container = re.search(r'<div class="qa-container">(.*?)<div class="pagination">', content, re.DOTALL)
    if container:
        container_content = container.group(1)
        # 提取每个 qa-item
        pattern = r'<div class="qa-item">(.*?)</div>\s*</div>'
        matches = re.findall(pattern, container_content, re.DOTALL)
        for m in matches:
            items.append(m.strip())
    return items

# 测试
items = extract_qa_from_file('pages/qa/qa-19.html')
print(f'qa-19 items: {len(items)}')
if items:
    print(f'First item:')
    print(repr(items[0][:200]))
    print()
    
    # 尝试提取问题
    q_match = re.search(r'class="qa-q">(.*?)<\/div>', items[0], re.DOTALL)
    print(f"q_match: {q_match}")
