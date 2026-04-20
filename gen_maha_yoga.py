"""大瑜伽章节生成器"""
import re, os

SRC = r'c:/Users/willp/Desktop/2026年4月/kb01/pdf_content/maha_yoga.txt'
OUT = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books'

txt = open(SRC, 'r', encoding='utf-8').read()
lines = txt.split('\n')

# 找页码边界
pages = []
for i, l in enumerate(lines):
    m = re.match(r'^--- 第(\d+)页 ---$', l.strip())
    if m:
        pages.append((int(m.group(1)), i+1))

# 提取5章内容
chapters = []
for idx in range(5):
    pg1, ln1 = pages[idx]
    pg2, ln2 = pages[idx+1]
    raw = '\n'.join(lines[ln1:ln2])
    raw = re.sub(r'\n---\s*第\d+\s*页\s*---\n', '\n', raw)
    raw = re.sub(r'\n\d{1,3}\n', '\n', raw)
    raw = re.sub(r'\n{3,}', '\n\n', raw).strip()
    
    # 第一行是章节标题
    first_lines = raw.split('\n', 3)
    title = first_lines[1] if len(first_lines) > 1 else ''
    content = '\n'.join(first_lines[2:]) if len(first_lines) > 2 else raw
    
    # 提取段落
    paras = [p.strip() for p in content.split('\n\n') if p.strip() and len(p.strip()) > 20]
    
    chapters.append({
        'num': idx + 1,
        'title': title,
        'page': pg1,
        'content': content,
        'paras': paras,
    })

# 打印摘要
for c in chapters:
    print('Ch%d: %s (p.%d, %d paras)' % (c['num'], c['title'][:40], c['page'], len(c['paras'])))
    print('  First para:', c['paras'][0][:100] if c['paras'] else 'N/A')

print('\n准备就绪，将生成5个章节页')
