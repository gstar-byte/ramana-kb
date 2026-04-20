import re

txt = open(r'c:/Users/willp/Desktop/2026年4月/kb01/pdf_content/maha_yoga.txt', 'r', encoding='utf-8').read()
lines = txt.split('\n')

# 找所有页码标记的位置和紧跟其后的内容
chapters = []

for i, l in enumerate(lines):
    s = l.strip()
    m = re.match(r'^--- 第(\d+)页 ---$', s)
    if m:
        pg = int(m.group(1))
        # 找紧跟的章节标题行（下一行）
        title = ''
        for j in range(1, 5):
            if i+j < len(lines):
                ns = lines[i+j].strip()
                if ns and len(ns) < 100 and not ns.startswith('*'):
                    title = ns
                    break
        chapters.append((pg, title, i+1))  # (页码, 标题, 行号)

print('=== 书籍结构 ===')
for c in chapters:
    print('Page %3d | Line %5d | %s' % (c[0], c[1], c[2][:80]))

# 提取每章内容
print('\n=== 每章内容长度 ===')
for idx in range(len(chapters) - 1):
    pg1, title1, ln1 = chapters[idx]
    pg2, title2, ln2 = chapters[idx+1]
    content = '\n'.join(lines[ln1:ln2])
    # 清理
    content = re.sub(r'\n--- 第\d+页 ---\n', '', content)
    content = re.sub(r'\n\d+\n---', '\n', content)
    print('Ch %d (%s): %d chars, %d lines' % (idx+1, title1[:40], len(content), ln2-ln1))
    print('  前100字: ' + content[:100].replace('\n', ' '))
    print()
