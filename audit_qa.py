import os, re

qa_dir = 'pages/qa'

def extract_qa(fname):
    fpath = os.path.join(qa_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取标题
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else fname
    
    # 提取subtitle
    sub_m = re.search(r'class="subtitle"[^>]*>(.*?)</p>', content)
    subtitle = re.sub(r'<[^>]+>', '', sub_m.group(1)).strip() if sub_m else ''
    
    # 提取所有QA对
    items = re.findall(r'class="qa-q"[^>]*>(.*?)</div>\s*<div[^>]*class="qa-a"[^>]*>(.*?)</div>', content, re.DOTALL)
    pairs = []
    for q, a in items:
        q = re.sub(r'<[^>]+>', '', q).strip()
        a = re.sub(r'<[^>]+>', '', a).strip()
        pairs.append((q, a))
    
    return title, subtitle, pairs

print('='*80)
print('QA页面内容审计（qa-1 ~ qa-28）')
print('='*80)

all_qa_set = {}  # question -> first_seen_page

for i in range(1, 29):
    fname = f'qa-{i}.html'
    title, subtitle, pairs = extract_qa(fname)
    
    dups_in_page = []
    for q, a in pairs:
        if q in all_qa_set:
            dups_in_page.append(f'  ⚠️  重复: [{q[:40]}] (首见于 {all_qa_set[q]})')
        else:
            all_qa_set[q] = fname
    
    print(f'\n【{fname}】{title}')
    print(f'  来源: {subtitle}')
    print(f'  QA数: {len(pairs)}条')
    for q, a in pairs:
        a_preview = a[:60] + '...' if len(a) > 60 else a
        print(f'  Q: {q[:55]}')
        print(f'  A: {a_preview}')
        print()
    if dups_in_page:
        for d in dups_in_page:
            print(d)
    print('-'*60)

print(f'\n总计: qa-1~28 共 {len(all_qa_set)} 个不重复问题')
