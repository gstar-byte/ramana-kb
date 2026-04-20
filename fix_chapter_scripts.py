import os
import re

pages_books = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books'

# 目标：search-secret-india-ch1 ~ ch17
files = [f for f in os.listdir(pages_books) if re.match(r'search-secret-india-ch\d+\.html', f)]
files.sort()

print(f'找到 {len(files)} 个章节文件')

# 要删除的内联脚本块（从 <script> 到 </script>，不含 script.js 那行）
inline_script = '''    <script>
        function toggleSidebar() {
            const s = document.getElementById('sidebar');
            const o = document.getElementById('sidebarOverlay');
            s.classList.toggle('open');
            if (o) o.classList.toggle('open');
        }
        document.querySelectorAll('.sidebar-section-title').forEach(title => {
            title.addEventListener('click', () => title.parentElement.classList.toggle('collapsed'));
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') document.getElementById('sidebar').classList.remove('open');
        });
    </script>
'''

fixed = 0
for fname in files:
    fpath = os.path.join(pages_books, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if inline_script in content:
        new_content = content.replace(inline_script, '')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  ✓ 已修复: {fname}')
        fixed += 1
    else:
        # 也尝试更宽松的正则匹配（内联script块）
        pattern = r'\n    <script>\n        function toggleSidebar\(\).*?</script>\n'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            new_content = content[:match.start()] + '\n' + content[match.end():]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'  ✓ 已修复(正则): {fname}')
            fixed += 1
        else:
            print(f'  - 未找到内联脚本: {fname}')

print(f'\n完成：共修复 {fixed} 个文件')
