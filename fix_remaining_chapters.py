import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 检查所有章节页面的flex导航
chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]

fixed_count = 0
for f in chapter_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original = content
    
    # 模式1: 带align-items:center的flex导航
    pattern1 = r'<div class="card" style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="([^"]+)" class="tag">([^<]+)</a>\s*<a href="([^"]+)" class="tag">([^<]+)</a>\s*</div>'
    replacement1 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <a href="\1" class="tag">\2</a>
                        <a href="\3" class="tag">\4</a>
                    </div>
                </div>'''
    content = re.sub(pattern1, replacement1, content)
    
    # 模式2: 不带align-items:center的flex导航（如crumbs-ch1.html）
    pattern2 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<span[^>]*>([^<]+)</span>\s*<a href="([^"]+)" class="btn-primary">([^<]+)</a>\s*</div>'
    replacement2 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span style="color:var(--text-muted);">\1</span>
                        <a href="\2" class="btn-primary">\3</a>
                    </div>
                </div>'''
    content = re.sub(pattern2, replacement2, content)
    
    # 模式3: 两个都是span的情况
    pattern3 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<span[^>]*>([^<]+)</span>\s*<span[^>]*>([^<]+)</span>\s*</div>'
    replacement3 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span style="color:var(--text-muted);">\1</span>
                        <span style="color:var(--text-muted);">\2</span>
                    </div>
                </div>'''
    content = re.sub(pattern3, replacement3, content)
    
    # 模式4: span + a.tag 的情况
    pattern4 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<span[^>]*>([^<]+)</span>\s*<a href="([^"]+)" class="tag">([^<]+)</a>\s*</div>'
    replacement4 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span style="color:var(--text-muted);">\1</span>
                        <a href="\2" class="tag">\3</a>
                    </div>
                </div>'''
    content = re.sub(pattern4, replacement4, content)
    
    # 模式5: a.tag + span 的情况
    pattern5 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<a href="([^"]+)" class="tag">([^<]+)</a>\s*<span[^>]*>([^<]+)</span>\s*</div>'
    replacement5 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <a href="\1" class="tag">\2</a>
                        <span style="color:var(--text-muted);">\3</span>
                    </div>
                </div>'''
    content = re.sub(pattern5, replacement5, content)
    
    # 模式6: a.btn-secondary + a.btn-primary 的情况
    pattern6 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<a href="([^"]+)" class="btn-secondary">([^<]+)</a>\s*<a href="([^"]+)" class="btn-primary">([^<]+)</a>\s*</div>'
    replacement6 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <a href="\1" class="btn-secondary">\2</a>
                        <a href="\3" class="btn-primary">\4</a>
                    </div>
                </div>'''
    content = re.sub(pattern6, replacement6, content)
    
    # 模式7: a.btn-primary + a.btn-primary 的情况
    pattern7 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<a href="([^"]+)" class="btn-primary">([^<]+)</a>\s*<a href="([^"]+)" class="btn-primary">([^<]+)</a>\s*</div>'
    replacement7 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <a href="\1" class="btn-primary">\2</a>
                        <a href="\3" class="btn-primary">\4</a>
                    </div>
                </div>'''
    content = re.sub(pattern7, replacement7, content)
    
    # 模式8: a.btn-secondary + span 的情况
    pattern8 = r'<div class="card" style="display:flex;justify-content:space-between;">\s*<a href="([^"]+)" class="btn-secondary">([^<]+)</a>\s*<span[^>]*>([^<]+)</span>\s*</div>'
    replacement8 = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <a href="\1" class="btn-secondary">\2</a>
                        <span style="color:var(--text-muted);">\3</span>
                    </div>
                </div>'''
    content = re.sub(pattern8, replacement8, content)
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"修复: {f}")
        fixed_count += 1

print(f"\n共修复 {fixed_count} 个文件")
