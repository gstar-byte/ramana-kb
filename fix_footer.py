# 批量修复 footer
# 1. 所有 "拉玛那马哈希Space" → "拉玛那马哈希"
# 2. 书籍章节页 footer 替换为完整版（带版权+地图+联系）
# 3. 概念页/methods/index.html 等 footer 替换为完整版

import os, glob, re

kb = r'c:/Users/willp/Desktop/2026年4月/kb01/pages'

# 完整 footer 模板（用于书籍章节页/概念页/methods等）
FOOTER_FULL = '''
                <footer class="site-footer">
                    <p><a href="../index.html">拉玛那马哈希</a> | 传承自印度阿鲁那佳拉圣山</p>
                    <p style="margin-top:0.5rem; font-size:0.9rem; color: var(--text-muted);">© 2026 拉玛那马哈希. 保留所有权利。</p>
                    <p style="margin-top:1rem; font-size:0.9rem;"><a href="../sitemap.html" style="color: var(--text-muted); text-decoration: underline;">🌐 网站地图</a> <span style="margin: 0 1rem;">|</span> <a href="mailto:591611431@qq.com" style="color: var(--text-muted); text-decoration: underline;">联系我</a></p>
                </footer>'''

FOOTER_QA = FOOTER_FULL  # qa/ 子目录下链接和上面一致

fixed_count = 0
space_count = 0

# ========== 1. 修复所有 "Space" 替换为无 Space ==========
files = glob.glob(f'{kb}/**/*.html', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    if '拉玛那马哈希Space' not in content:
        continue

    space_count += 1
    # 替换 "拉玛那马哈希Space" → "拉玛那马哈希"
    content = content.replace('拉玛那马哈希Space', '拉玛那马哈希')

    # 判断是否是书籍章节页（位于 books/ 目录且文件名含 -ch 或是书主页）
    rel = f.replace(kb+'\\', '').replace(kb+'/', '')
    is_book = rel.startswith('books/')
    is_qa = rel.startswith('qa/')
    is_book_chapter = is_book and ('-ch' in rel or rel.endswith('.html'))

    if is_qa:
        # QA页 footer 在 </main> 之后，先找到旧 footer 替换
        content = re.sub(
            r'<footer class="site-footer">.*?</footer>',
            FOOTER_QA.strip(),
            content, flags=re.DOTALL
        )
    elif is_book_chapter:
        # 书籍章节页：找到旧的简陋 footer 替换
        content = re.sub(
            r'<footer class="site-footer">.*?</footer>',
            FOOTER_FULL.strip(),
            content, flags=re.DOTALL
        )
    # 非书籍章节页（如 persons/, concepts/, methods/）：只替换 Space，保留原有 footer 结构

    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)

    fixed_count += 1
    print(f'Fixed: {rel}')

# ========== 2. 书籍章节页/概念页/方法页：统一 footer ==========
# 这些页面可能没有简陋 footer，需要插入在 </main></div> 之前
patterns = [
    (r'books/', FOOTER_FULL),
    (r'concepts/', FOOTER_FULL),
    (r'methods/', FOOTER_FULL),
    (r'persons/', FOOTER_FULL),
    (r'qa/', FOOTER_QA),
]

for pat, footer_tpl in patterns:
    files = glob.glob(f'{kb}/**/*.html', recursive=True)
    for f in files:
        rel = f.replace(kb+'\\', '').replace(kb+'/', '')
        if not re.search(pat, rel):
            continue
        with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
            content = fh.read()

        # 检查是否已有完整 footer（有 copyright 和 sitemap）
        if '保留所有权利' in content and 'site-footer' in content:
            continue  # 已有完整 footer，跳过

        # 检查是否有任何 footer
        has_footer = '<footer' in content
        if has_footer:
            continue  # 已有 footer，不重复添加

        # 插入 footer：在 </main> 和 </div> 之间
        new_content = re.sub(
            r'(</main>\s*</div>\s*(?:<!-- .*? -->)?\s*)$',
            '\n    ' + footer_tpl.strip() + '\n\\1',
            content
        )
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            print(f'Inserted footer: {rel}')

print(f'\n完成！共修复 {space_count} 个含 Space 的文件')
