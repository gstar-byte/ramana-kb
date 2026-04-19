import re
import os

# 读取 qa-19.html 看看原始内容
with open('pages/qa/qa-19.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 qa-container
container = re.search(r'<div class="qa-container">(.*?)<div class="pagination">', content, re.DOTALL)
if container:
    container_content = container.group(1)
    print("Container content length:", len(container_content))
    print()
    
    # 使用不同的方法提取 - 匹配整个 qa-item div
    # 先找到所有的 qa-item 开始位置
    starts = [m.start() for m in re.finditer(r'<div class="qa-item">', container_content)]
    print(f"Found {len(starts)} qa-item starts")
    
    # 手动提取每个 qa-item
    items = []
    for i, start in enumerate(starts):
        end = len(container_content)
        if i + 1 < len(starts):
            end = starts[i + 1]
        
        item = container_content[start:end]
        # 去掉结尾的 </div>
        item = item.rstrip()
        if item.endswith('</div>'):
            item = item[:-6]
        
        items.append(item.strip())
    
    print(f"Extracted {len(items)} items")
    print()
    print("First item:")
    print(items[0])
