#!/usr/bin/env python3
"""
修复移动端汉堡菜单问题：
1. 找出所有引用 script.js 但目录下没有该文件的 HTML 页面
2. 将 script.js 引用修正为 ../script.js（适用于一级子目录）
3. 同时处理 zh-TW 目录
"""
import os, re, shutil

def fix_script_refs(base_dir, report_only=False):
    issues = []
    fixed = []
    
    for root, dirs, files in os.walk(base_dir):
        # 跳过根目录本身（script.js 在那里）
        if os.path.normpath(root) == os.path.normpath(base_dir):
            continue
        
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, base_dir)
            
            with open(path, encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            # 检查是否引用了不带路径的 script.js
            has_issue = ('src="script.js"' in content or "src='script.js'" in content)
            local_script_exists = os.path.exists(os.path.join(root, 'script.js'))
            
            if has_issue and not local_script_exists:
                issues.append(rel)
                if not report_only:
                    # 计算相对路径深度
                    depth = len(rel.replace('\\', '/').split('/')) - 1
                    prefix = '../' * depth
                    # 替换引用
                    new_content = content.replace('src="script.js"', f'src="{prefix}script.js"')
                    new_content = new_content.replace("src='script.js'", f"src='{prefix}script.js'")
                    with open(path, 'w', encoding='utf-8') as fp:
                        fp.write(new_content)
                    fixed.append(rel)
    
    return issues, fixed

print("=== 检查 pages/ ===")
issues, fixed = fix_script_refs('F:/26年4月/kb01/pages', report_only=False)
print(f"问题页面: {len(issues)}, 已修复: {len(fixed)}")
for p in issues[:10]:
    print(f"  {p}")

print("\n=== 检查 zh-TW/ ===")
issues2, fixed2 = fix_script_refs('F:/26年4月/kb01/zh-TW', report_only=False)
print(f"问题页面: {len(issues2)}, 已修复: {len(fixed2)}")
for p in issues2[:10]:
    print(f"  {p}")

print("\n完成！")
