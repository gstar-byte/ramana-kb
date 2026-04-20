#!/usr/bin/env python3
"""
清理章节页面末尾的多余代码残留
"""
import os
import re

def clean_file(filepath):
    """清理文件末尾的多余代码"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # 查找正确的结束位置（</body></html>）
    # 模式：找到最后一个 </body></html>，删除之后的所有内容
    pattern = r'(</body>\s*</html>)(.*?)$'
    match = re.search(pattern, content, re.DOTALL)
    
    if match and match.group(2).strip():
        # 有额外的内容需要删除
        content = content[:match.start(2)]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, original_len - len(content)
    
    return False, 0

# 修复 ch7 和 ch14
files_to_fix = [
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch7.html',
    'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch14.html',
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        fixed, removed = clean_file(filepath)
        if fixed:
            print(f"✅ 已清理: {os.path.basename(filepath)} (删除 {removed} 字符)")
        else:
            print(f"⏭️ 无需清理: {os.path.basename(filepath)}")
    else:
        print(f"❌ 文件不存在: {filepath}")

print("\n清理完成！")
