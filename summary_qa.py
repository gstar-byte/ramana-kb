import os, re

qa_dir = 'pages/qa'

def get_page_summary(fname):
    fpath = os.path.join(qa_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    title_m = re.search(r'<h1[^>]*>(.*?)</h1>', content)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else fname
    sub_m = re.search(r'class="subtitle"[^>]*>(.*?)</p>', content)
    subtitle = re.sub(r'<[^>]+>', '', sub_m.group(1)).strip() if sub_m else ''
    items = re.findall(r'class="qa-q"[^>]*>(.*?)</div>', content, re.DOTALL)
    questions = [re.sub(r'<[^>]+>', '', q).strip() for q in items]
    return title, subtitle, questions

print('qa-1~28 主题总览')
print('='*70)
for i in range(1, 29):
    fname = f'qa-{i}.html'
    title, subtitle, questions = get_page_summary(fname)
    print(f'[{i:02d}] {title}')
    print(f'     来源：{subtitle}')
    print()

print()
print('散点重复详情（qa-1~28内）:')
print('='*70)
# qa-6 vs qa-25
for pg in ['qa-6.html', 'qa-25.html']:
    _, _, qs = get_page_summary(pg)
    print(f'{pg}: {[q for q in qs if "上师" in q and "恩典" in q]}')
print()
for pg in ['qa-9.html', 'qa-22.html']:
    _, _, qs = get_page_summary(pg)
    print(f'{pg}: {[q for q in qs if "工作" in q]}')
print()
for pg in ['qa-19.html', 'qa-27.html']:
    _, _, qs = get_page_summary(pg)
    print(f'{pg}: {[q for q in qs if "三摩地" in q]}')
print()
for pg in ['qa-23.html', 'qa-26.html']:
    _, _, qs = get_page_summary(pg)
    print(f'{pg}: {[q for q in qs if "一行三昧" in q]}')
