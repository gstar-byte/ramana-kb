import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 书籍信息映射
book_relations = {
    'be-as-you-are.html': ['gems.html', 'talks.html', 'teachings.html'],
    'gems.html': ['be-as-you-are.html', 'talks.html', 'day-by-day.html'],
    'back-to-heart.html': ['be-as-you-are.html', 'reflections.html', 'crumbs.html'],
    'day-by-day.html': ['gems.html', 'talks.html', 'face-to-face.html'],
    'face-to-face.html': ['day-by-day.html', 'talks.html', 'gems.html'],
    'talks.html': ['gems.html', 'day-by-day.html', 'be-as-you-are.html'],
    'teachings.html': ['be-as-you-are.html', 'gems.html', 'crumbs.html'],
    'crumbs.html': ['teachings.html', 'gems.html', 'back-to-heart.html'],
    'timeless.html': ['be-as-you-are.html', 'reflections.html', 'surpassing-love.html'],
    'reflections.html': ['timeless.html', 'surpassing-love.html', 'back-to-heart.html'],
    'surpassing-love.html': ['timeless.html', 'reflections.html', 'search-secret-india.html'],
    'search-secret-india.html': ['be-as-you-are.html', 'surpassing-love.html', 'gems.html'],
    'spiritual-stories.html': ['gems.html', 'crumbs.html', 'teachings.html'],
    'collected-works.html': ['teachings.html', 'gems.html', 'talks.html'],
    'maha-yoga.html': ['be-as-you-are.html', 'gems.html', 'teachings.html'],
    'maharshi-gospel.html': ['be-as-you-are.html', 'gems.html', 'talks.html'],
}

book_titles = {
    'be-as-you-are.html': '📖 走向静默，如你本来',
    'gems.html': '💎 宝钻集',
    'back-to-heart.html': '📕 回到你心中',
    'day-by-day.html': '📅 日日与彼',
    'face-to-face.html': '👁️ 面对面',
    'talks.html': '💬 对谈录',
    'teachings.html': '📗 以言传意',
    'crumbs.html': '🍞 桌边碎语',
    'timeless.html': '⏳ 时代中的永恒',
    'reflections.html': '💭 反思录',
    'surpassing-love.html': '💝 超越爱与恩典',
    'search-secret-india.html': '🔍 秘密印度',
    'spiritual-stories.html': '📖 灵性故事',
    'collected-works.html': '📚 全集',
    'maha-yoga.html': '🧘 大瑜伽',
    'maharshi-gospel.html': '📜 马哈希福音',
}

def fix_chapter_page(filename):
    """修复章节页面的flex导航问题"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复flex导航为普通卡片样式
    old_pattern = r'<div class="card" style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="([^"]+)" class="tag">([^<]+)</a>\s*<a href="([^"]+)" class="tag">([^<]+)</a>\s*</div>'
    new_html = '''<div class="card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <a href="\1" class="tag">\2</a>
                        <a href="\3" class="tag">\4</a>
                    </div>
                </div>'''
    
    content_new = re.sub(old_pattern, new_html, content)
    
    if content_new != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content_new)
        return True
    return False

def fix_book_main_page(filename):
    """修复书籍主页面：移除相关概念，确保有相关书籍"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. 移除相关概念区域（保留章节页面的，只移除书籍主页面的）
    # 查找 <!-- 核心概念 --> 或 <h2>🔗 相关概念</h2> 所在的card
    concept_pattern = r'<div class="card">\s*<h2[^>]*>🔗 相关概念</h2>.*?</div>\s*</div>'
    if re.search(concept_pattern, content, re.DOTALL):
        content = re.sub(concept_pattern, '', content, flags=re.DOTALL)
        modified = True
    
    # 2. 检查是否有相关书籍
    has_related_books = '相关书籍' in content
    
    if not has_related_books and filename in book_relations:
        # 在源文档区域之前添加相关书籍
        related = book_relations[filename]
        related_html = '''                <!-- 相关书籍 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📚 相关书籍</h2>
                    <div class="concept-tags">
'''
        for rel_file in related:
            if rel_file in book_titles:
                related_html += f'                        <a href="{rel_file}" class="tag">{book_titles[rel_file]}</a>\n'
        related_html += '''                    </div>
                </div>
                
'''
        
        # 在 <!-- 下载链接 --> 或 <!-- 源文档 --> 之前插入
        content = re.sub(r'(\s+)(<!-- 下载链接 -->|<!-- 源文档 -->)', r'\1' + related_html + r'\1\2', content)
        modified = True
    
    if modified:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return modified

# 处理所有文件
chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]
book_files = [f for f in os.listdir('.') if '-ch' not in f and f.endswith('.html') and f != 'index.html']

print("=== 修复章节页面 ===")
for f in chapter_files:
    if fix_chapter_page(f):
        print(f"修复: {f}")

print("\n=== 修复书籍主页面 ===")
for f in book_files:
    if fix_book_main_page(f):
        print(f"修复: {f}")

print("\n完成!")
