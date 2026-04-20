#!/usr/bin/env python3
"""
为缺少源文档区域的书籍页面添加 📥 源文档 部分
"""

import os
import re

# 书籍与对应txt文件映射
BOOKS_TO_ADD = {
    'back-to-heart.html': {
        'file': 'back_to_heart.txt',
        'title': 'Back to the Heart 原文 (TXT)'
    },
    'day-by-day.html': {
        'file': 'day_by_day.txt',
        'title': 'Day by Day with Bhagavan 原文 (TXT)'
    },
    'face-to-face.html': {
        'file': 'face_to_face.txt',
        'title': 'Face to Face with Sri Ramana Maharshi 原文 (TXT)'
    },
    'maha-yoga.html': {
        'file': 'maha_yoga.txt',
        'title': 'Maha Yoga 原文 (TXT)'
    },
    'collected-works.html': {
        'file': 'collected_works.txt',
        'title': 'Collected Works 原文 (TXT)'
    },
    'spiritual-stories.html': {
        'file': 'spiritual_stories.txt',
        'title': 'Spiritual Stories 原文 (TXT)'
    },
    'reflections.html': {
        'file': 'reflections.txt',
        'title': 'Reflections 原文 (TXT)'
    },
    'talks.html': {
        'file': 'talks_with_ramana_1.txt',
        'title': 'Talks with Sri Ramana Maharshi 原文 (TXT)'
    },
}

BASE_DIR = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books'

def add_source_section(file_path, txt_file, title):
    """在content-wrapper结束前添加源文档区域"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有源文档
    if '📥 源文档' in content or '源文档' in content:
        print(f"  跳过 (已有源文档): {os.path.basename(file_path)}")
        return False
    
    # 构建源文档HTML
    source_html = f'''
                
                <!-- 源文档 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📥 源文档</h2>
                    <div class="concept-tags">
                        <a href="../pdf_content/{txt_file}" class="tag" download>📄 {title}</a>
                    </div>
                </div>'''
    
    # 找到 content-wrapper 结束前的位置（在 </div>\n        </main> 之前）
    # 模式：查找最后一个相关概念或经典语录卡片后的 </div>\n        </main>
    pattern = r'(</div>\s*</main>)'
    
    # 尝试在相关概念卡片后插入
    if '相关概念' in content:
        # 在相关概念卡片的 </div> 后插入
        pattern = r'(<!-- 相关概念 -->\s*<div class="card">.*?</div>\s*)(</div>\s*</main>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            new_content = content[:match.end(1)] + source_html + content[match.end(1):]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  已添加: {os.path.basename(file_path)}")
            return True
    
    # 备用方案：在 </div>\n        </main> 前插入
    pattern = r'(</div>)(\s*</main>)'
    # 找到最后一个匹配
    matches = list(re.finditer(pattern, content))
    if matches:
        last_match = matches[-1]
        pos = last_match.start(2)
        new_content = content[:pos] + source_html + content[pos:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  已添加 (备用): {os.path.basename(file_path)}")
        return True
    
    print(f"  失败: 未找到插入点 - {os.path.basename(file_path)}")
    return False

def main():
    print("开始添加源文档区域...\n")
    
    success = 0
    skip = 0
    fail = 0
    
    for html_file, info in BOOKS_TO_ADD.items():
        file_path = os.path.join(BASE_DIR, html_file)
        if not os.path.exists(file_path):
            print(f"  文件不存在: {html_file}")
            fail += 1
            continue
        
        result = add_source_section(file_path, info['file'], info['title'])
        if result:
            success += 1
        else:
            skip += 1
    
    print(f"\n完成: 成功 {success}, 跳过 {skip}, 失败 {fail}")

if __name__ == '__main__':
    main()
