import json, re, glob

# 读取现有qa-data.json
with open(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\qa\qa-data.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)
print(f'Existing items: {len(existing)}')

# 读取新QA文件并提取问答对
new_items = []
for i in range(52, 62):
    fpath = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\qa\qa-%d.html' % i
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    # 提取页面标题
    title_match = re.search(r'<h1>(.*?)</h1>', c)
    title = title_match.group(1).replace('\u4fee\u884c\u95ee\u7b54 ', '').strip() if title_match else 'QA-%d' % i
    # 提取问题 - 在qa-q div中
    q_divs = re.findall(r'class="qa-q"[^>]*>(.*?)</div>', c, re.DOTALL)
    # 提取答案 - 在qa-a div中
    a_divs = re.findall(r'class="qa-a"[^>]*>(.*?)</div>', c, re.DOTALL)
    
    for qi, ai in zip(q_divs, a_divs):
        q_clean = re.sub(r'<[^>]+>', '', qi).strip()
        a_clean = re.sub(r'<[^>]+>', '', ai).strip()
        if q_clean and a_clean and len(q_clean) > 3:
            new_items.append({
                'question': q_clean,
                'answer': a_clean,
                'meta': title,
                'category': '\u65e5\u5e38',
                'link': 'qa-%d.html' % i
            })
    
    print(f'  qa-{i}: {len(q_divs)} QAs extracted ({title[:30]})')

print(f'New QA pairs extracted: {len(new_items)}')
combined = existing + new_items
print(f'Combined total: {len(combined)}')

with open(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\qa\qa-data.json', 'w', encoding='utf-8') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)
print('qa-data.json updated!')
