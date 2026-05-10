#!/usr/bin/env python3
import os
import re
from opencc import OpenCC

cc = OpenCC('s2tw')

LANG_TOGGLE_CSS = """/* Language Toggle Button */
.lang-toggle{position:fixed;top:56px;right:16px;z-index:1000;display:inline-flex;align-items:center;justify-content:center;padding:6px 14px;background:rgba(255,255,255,0.9);border:1px solid var(--border);border-radius:20px;font-size:13px;font-weight:600;color:var(--text);text-decoration:none;transition:all .2s ease;box-shadow:0 2px 8px rgba(0,0,0,0.08);}
.lang-toggle:hover{background:var(--gold);border-color:var(--gold);color:white;transform:translateY(-1px);box-shadow:0 4px 12px rgba(184,134,11,0.25);}
@media(max-width:768px){.lang-toggle{top:52px;right:8px;padding:5px 10px;font-size:12px;}}"""

ZHTW_TOGGLE_HTML = '<a href="#" class="lang-toggle" title="\u5207\u63db\u7232\u7c21\u9ad4\u4e2d\u6587" onclick="location.href=location.pathname.replace(\'/zh-TW/\',\'/\');return false;">\u7c21</a>'
SIMPLIFIED_TOGGLE_HTML = '<a href="#" class="lang-toggle" title="\u5207\u6362\u4e3a\u7e41\u4f53\u4e2d\u6587" onclick="location.href=\'/zh-TW/\'+location.pathname.substring(1);return false;">\u7e41</a>'

def fix_graph_html():
    path = '/workspace/zh-TW/graph.html'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = cc.convert(content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed graph.html: converted JS data to traditional Chinese")

def add_css_to_styles(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    if '.lang-toggle' in css:
        css = re.sub(r'/\* Language Toggle Button \*/.*?\.lang-toggle:hover\{[^}]+\}', '', css, flags=re.DOTALL)
        css = re.sub(r'@media\(max-width:768px\)\{\.lang-toggle\{[^}]+\}\}', '', css)
    css = css.rstrip() + '\n' + LANG_TOGGLE_CSS + '\n'
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print(f"Added lang-toggle CSS to {css_path}")

def fix_zhtw_toggle_buttons():
    zhtw_dir = '/workspace/zh-TW'
    count = 0
    for root, dirs, files in os.walk(zhtw_dir):
        for fname in files:
            if not fname.endswith('.html'):
                continue
            filepath = os.path.join(root, fname)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            original = content
            content = content.replace('<link rel="stylesheet" href="lang-toggle.css">\n', '')
            content = content.replace('<link rel="stylesheet" href="lang-toggle.css">', '')
            content = re.sub(
                r'<a\s+href="[^"]*"\s+class="lang-toggle"[^>]*>[简簡]</a>',
                ZHTW_TOGGLE_HTML,
                content
            )
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
    print(f"Fixed toggle buttons in {count} zh-TW HTML files")

def add_toggle_to_simplified_pages():
    pages_dir = '/workspace/pages'
    count = 0
    for root, dirs, files in os.walk(pages_dir):
        if 'zh-TW' in root:
            continue
        for fname in files:
            if not fname.endswith('.html'):
                continue
            filepath = os.path.join(root, fname)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'lang-toggle' in content:
                continue
            body_match = re.search(r'(<body[^>]*>)', content)
            if not body_match:
                continue
            insert_pos = body_match.end()
            toggle_line = '\n    ' + SIMPLIFIED_TOGGLE_HTML
            content = content[:insert_pos] + toggle_line + content[insert_pos:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    print(f"Added toggle buttons to {count} simplified HTML files")

def add_hreflang_to_simplified():
    pages_dir = '/workspace/pages'
    count = 0
    for root, dirs, files in os.walk(pages_dir):
        if 'zh-TW' in root:
            continue
        for fname in files:
            if not fname.endswith('.html'):
                continue
            filepath = os.path.join(root, fname)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'hreflang="zh-TW"' in content:
                continue
            head_close = content.find('</head>')
            if head_close == -1:
                continue
            hreflang_tags = '\n    <link rel="alternate" hreflang="zh-TW" href="https://ramanamaharshi.space/zh-TW/">\n    <link rel="alternate" hreflang="zh-CN" href="https://ramanamaharshi.space/">'
            content = content[:head_close] + hreflang_tags + content[head_close:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    print(f"Added hreflang tags to {count} simplified HTML files")

def copy_zhtw_to_pages():
    src = '/workspace/zh-TW'
    dst = '/workspace/pages/zh-TW'
    if os.path.exists(dst):
        os.system(f'rm -rf {dst}')
    os.system(f'cp -r {src} {dst}')
    file_count = sum(len(files) for _, _, files in os.walk(dst))
    print(f"Copied zh-TW to pages/zh-TW/ ({file_count} files)")

if __name__ == '__main__':
    print("=== Step 1: Fix graph.html JS data ===")
    fix_graph_html()
    
    print("\n=== Step 2: Add lang-toggle CSS to styles.css ===")
    add_css_to_styles('/workspace/pages/styles.css')
    add_css_to_styles('/workspace/zh-TW/styles.css')
    
    print("\n=== Step 3: Fix zh-TW toggle buttons ===")
    fix_zhtw_toggle_buttons()
    
    print("\n=== Step 4: Add toggle to simplified pages ===")
    add_toggle_to_simplified_pages()
    
    print("\n=== Step 5: Add hreflang to simplified pages ===")
    add_hreflang_to_simplified()
    
    print("\n=== Step 6: Copy zh-TW to pages/zh-TW/ ===")
    copy_zhtw_to_pages()
    
    print("\n=== All done! ===")
