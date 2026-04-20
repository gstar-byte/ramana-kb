import os, glob, re

kb = r'c:/Users/willp/Desktop/2026年4月/kb01/pages'

# 完整 footer 模板（subdir 页面用 ../）
FOOTER_FULL = '''            <footer class="site-footer">
                <p><a href="../index.html">拉玛那马哈希</a> | 传承自印度阿鲁那佳拉圣山</p>
                <p style="margin-top:0.5rem; font-size:0.9rem; color: var(--text-muted);">© 2026 拉玛那马哈希. 保留所有权利。</p>
                <p style="margin-top:1rem; font-size:0.9rem;"><a href="../sitemap.html" style="color: var(--text-muted); text-decoration: underline;">🌐 网站地图</a> <span style="margin: 0 1rem;">|</span> <a href="mailto:591611431@qq.com" style="color: var(--text-muted); text-decoration: underline;">联系我</a></p>
            </footer>'''

fixed = []

# 找到所有书籍/人物/概念/方法子目录的页面
subdirs = ['books', 'concepts', 'persons', 'methods']
for subdir in subdirs:
    files = glob.glob(f'{kb}/{subdir}/*.html')
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()

        if '保留所有权利' in content and '网站地图' in content:
            continue  # 已有完整 footer

        # 替换旧的简陋 footer
        old_pattern = r'<footer class="site-footer">.*?</footer>'
        new_content = re.sub(old_pattern, FOOTER_FULL, content, flags=re.DOTALL)

        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            rel = f.replace(kb+'\\', '').replace(kb+'/', '')
            fixed.append(rel)
            print(f'Fixed footer: {rel}')

print(f'\n共修复 {len(fixed)} 个 footer')
