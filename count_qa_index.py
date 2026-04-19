import re

with open('pages/qa/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 统计 qa-item 数量
qa_items = re.findall(r'class="qa-item"', content)
print(f'index.html qa-item count: {len(qa_items)}')

# 查找 itemsPerPage 设置
items_per_page = re.search(r'itemsPerPage\s*=\s*(\d+)', content)
if items_per_page:
    ipp = int(items_per_page.group(1))
    print(f'itemsPerPage: {ipp}')
    total_pages = len(qa_items) // ipp + (1 if len(qa_items) % ipp > 0 else 0)
    print(f'total pages: {total_pages}')
