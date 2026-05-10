#!/usr/bin/env python3
import os
import re
from opencc import OpenCC

cc = OpenCC('s2tw')

def fix_zhtw_qa_meta():
    qa_dir = '/workspace/pages/zh-TW/qa'
    count = 0
    for fname in sorted(os.listdir(qa_dir)):
        if not fname.endswith('.html'):
            continue
        filepath = os.path.join(qa_dir, fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        head_close = content.find('</head>')
        if head_close == -1:
            continue
        head_section = content[:head_close]
        body_section = content[head_close:]
        converted_head = cc.convert(head_section)
        if converted_head != head_section:
            content = converted_head + body_section
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    print(f"Fixed QA meta tags in {count} zh-TW files")

def fix_zhtw_qa_index():
    filepath = '/workspace/pages/zh-TW/qa/index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    head_close = content.find('</head>')
    if head_close == -1:
        return
    head_section = content[:head_close]
    body_section = content[head_close:]
    converted_head = cc.convert(head_section)
    content = converted_head + body_section
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed qa/index.html meta tags")

def move_toggle_to_topbar():
    simplified_dir = '/workspace/pages'
    traditional_dir = '/workspace/pages/zh-TW'
    
    for lang_dir, is_zhtw in [(simplified_dir, False), (traditional_dir, True)]:
        count = 0
        for root, dirs, files in os.walk(lang_dir):
            for fname in files:
                if not fname.endswith('.html'):
                    continue
                filepath = os.path.join(root, fname)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                original = content
                
                content = re.sub(r'\s*<a\s+href="[^"]*"\s+class="lang-toggle"[^>]*>[繁簡简]</a>', '', content)
                
                if is_zhtw:
                    toggle_html = '<a href="#" class="lang-toggle" title="切換爲簡體中文" onclick="location.href=location.pathname.replace(\'/zh-TW/\',\'/\');return false;">簡</a>'
                else:
                    toggle_html = '<a href="#" class="lang-toggle" title="切换为繁体中文" onclick="location.href=\'/zh-TW/\'+location.pathname.substring(1);return false;">繁</a>'
                
                content = re.sub(
                    r'(<a\s+href="[^"]*graph\.html"[^>]*>圖譜</a>)',
                    r'\1' + toggle_html,
                    content
                )
                content = re.sub(
                    r'(<a\s+href="[^"]*graph\.html"[^>]*>图谱</a>)',
                    r'\1' + toggle_html,
                    content
                )
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
        print(f"Moved toggle to topbar in {count} {'zh-TW' if is_zhtw else 'simplified'} files")

def update_lang_toggle_css():
    for css_path in ['/workspace/pages/styles.css', '/workspace/pages/zh-TW/styles.css']:
        with open(css_path, 'r', encoding='utf-8') as f:
            css = f.read()
        
        css = re.sub(r'/\* Language Toggle Button \*/.*?@media\(max-width:768px\)\{\.lang-toggle\{[^}]+\}\}', '', css, flags=re.DOTALL)
        css = re.sub(r'/\* Language Toggle Button \*/.*?\.lang-toggle:hover\{[^}]+\}', '', css, flags=re.DOTALL)
        
        new_css = """/* Language Toggle in Topbar */
.lang-toggle{display:inline-flex;align-items:center;justify-content:center;padding:0 12px;font-size:13px;font-weight:600;color:#cbd5e1;text-decoration:none;transition:all .2s;border-left:1px solid rgba(255,255,255,.08);height:44px;line-height:44px;}
.lang-toggle:hover{color:var(--gold-light);background:rgba(184,134,11,.15);}"""
        
        css = css.rstrip() + '\n' + new_css + '\n'
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f"Updated lang-toggle CSS in {css_path}")

if __name__ == '__main__':
    print("=== Step 1: Fix zh-TW QA meta tags ===")
    fix_zhtw_qa_meta()
    fix_zhtw_qa_index()
    
    print("\n=== Step 2: Move toggle button to topbar ===")
    move_toggle_to_topbar()
    
    print("\n=== Step 3: Update lang-toggle CSS ===")
    update_lang_toggle_css()
    
    print("\n=== All done! ===")
