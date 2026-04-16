#!/usr/bin/env python3
"""
批量添加 GA4 代码到所有 HTML 文件
幂等性：已添加的不重复添加
用法：python add_ga4.py
"""

import os
import re

GA4_CODE = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MYFWHFPSYB');
</script>

'''

GA4_SKIP_PATTERNS = ['_template.html', 'new_qa_content.html']

def add_ga4_to_file(filepath):
    # 跳过模板文件
    if any(skip in filepath for skip in GA4_SKIP_PATTERNS):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 GA4 代码
    if 'G-MYFWHFPSYB' in content:
        return False
    
    # 检查是否已有 gtag
    if "gtag('config'" in content:
        return False
    
    # 找到 </head> 或 </HEAD> 标签
    if '</head>' in content.lower():
        match = re.search(r'</head>', content, re.IGNORECASE)
        if match:
            pos = match.start()
            new_content = content[:pos] + GA4_CODE + content[pos:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    
    return False

def process_directory(base_dir):
    count = 0
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root:
            continue
        
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, base_dir)
                try:
                    if add_ga4_to_file(filepath):
                        print(f"  ✅ 添加成功: {rel_path}")
                        count += 1
                    else:
                        print(f"  ⏭️  跳过: {rel_path}")
                except Exception as e:
                    print(f"  ❌ 错误: {rel_path} - {e}")
    
    return count

if __name__ == '__main__':
    base_dir = 'pages'
    print(f'📊 批量添加 GA4 代码\n')
    print(f'配置文件: G-MYFWHFPSYB\n')
    
    count = process_directory(base_dir)
    
    print(f'\n✅ 完成！共添加 {count} 个文件。')
    print(f'💡 提示：添加新 HTML 页面后，再次运行此脚本即可自动添加 GA4')
