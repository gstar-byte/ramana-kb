#!/usr/bin/env python3
"""批量添加 PWA Analytics 脚本到所有 HTML 文件"""

import os
import re

PWA_ANALYTICS = '<script src="pwa-analytics.js"></script>\n'

def add_pwa_analytics_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有 pwa-analytics.js
    if 'pwa-analytics.js' in content:
        print(f"  ⏭️  已有: {filepath}")
        return False
    
    # 在 </body> 前添加
    if '</body>' in content.lower():
        match = re.search(r'</body>', content, re.IGNORECASE)
        if match:
            pos = match.start()
            new_content = content[:pos] + PWA_ANALYTICS + content[pos:]
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
                try:
                    if add_pwa_analytics_to_file(filepath):
                        print(f"  ✅ 添加成功: {os.path.relpath(filepath, base_dir)}")
                        count += 1
                    else:
                        print(f"  ⏭️  跳过: {os.path.relpath(filepath, base_dir)}")
                except Exception as e:
                    print(f"  ❌ 错误: {filepath} - {e}")
    
    return count

if __name__ == '__main__':
    base_dir = 'pages'
    print(f'📊 开始为 {base_dir} 目录下的所有 HTML 文件添加 PWA Analytics...\n')
    
    count = process_directory(base_dir)
    
    print(f'\n✅ 完成！共添加 {count} 个文件。')
