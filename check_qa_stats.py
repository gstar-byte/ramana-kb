import os, re
from collections import defaultdict

qa_dir = 'pages/qa'
files = sorted([f for f in os.listdir(qa_dir) if re.match(r'qa-\d+\.html', f)], 
               key=lambda x: int(re.search(r'\d+', x).group()))

print(f'QA页面数量: {len(files)}')
print(f'页面范围: {files[0]} ~ {files[-1]}')
print()

all_questions = []
per_page = {}
duplicates = defaultdict(list)

for fname in files:
    fpath = os.path.join(qa_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 尝试多种提取方式
    questions = re.findall(r'class=["\']qa-question["\'][^>]*>(.*?)</div>', content, re.DOTALL)
    if not questions:
        # 尝试 h3
        questions = re.findall(r'<h3[^>]*class=["\'][^"\']*question[^"\']*["\'][^>]*>(.*?)</h3>', content, re.DOTALL)
    if not questions:
        # 尝试 data-q 或其他属性
        questions = re.findall(r'<div[^>]*class=["\'][^"\']*qa-q[^"\']*["\'][^>]*>(.*?)</div>', content, re.DOTALL)
    if not questions:
        # 通用 h3 提取
        questions = re.findall(r'<h3[^>]*>(.*?)</h3>', content, re.DOTALL)
    
    cleaned = []
    for q in questions:
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        q_clean = re.sub(r'\s+', ' ', q_clean)
        if q_clean and len(q_clean) > 5:
            cleaned.append(q_clean)
            all_questions.append((fname, q_clean))
            duplicates[q_clean].append(fname)
    
    per_page[fname] = len(cleaned)

print(f'总QA数量: {len(all_questions)}')
print()

print('每页QA数量:')
for fname, cnt in sorted(per_page.items(), key=lambda x: int(re.search(r'\d+', x[0]).group())):
    print(f'  {fname}: {cnt}条')

print()
dup_list = {q: flist for q, flist in duplicates.items() if len(flist) > 1}
if dup_list:
    print(f'发现重复QA: {len(dup_list)}个')
    for q, flist in list(dup_list.items())[:20]:
        print(f'  [{q[:60]}]')
        print(f'    -> {flist}')
else:
    print('未发现重复QA')
