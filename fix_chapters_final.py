import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 概念icon映射
concept_icons = {
    '真我': '🔮', 'atman': '🔮', 'self': '🔮',
    '梵': '🕉️', 'brahman': '🕉️',
    '本心': '💖', 'heart': '💖',
    '存在-意识-喜悦': '✨', 'satchidananda': '✨',
    '摩耶': '🌫️', 'maya': '🌫️',
    '世界': '🌍', 'world': '🌍',
    '心智': '🧠', 'mind': '🧠', 'citta': '🧠',
    '自我': '👤', 'ego': '👤',
    '念头': '💭', 'thought': '💭',
    '习气': '🌀', 'vasana': '🌀',
    '我念': '❓', 'i-am': '❓',
    '觉知': '👁️', 'awareness': '👁️',
    '无明': '🌑', 'ignorance': '🌑',
    '意识-物质纽结': '🔗', 'knot': '🔗',
    '自性': '☀️', 'svasthya': '☀️',
    '个体灵魂': '👤', 'jiva': '👤',
    '我是谁': '🔍', 'whoami': '🔍', 'who am i': '🔍',
    '静默': '🤫', 'silence': '🤫',
    '三摩地': '🧘', 'samadhi': '🧘',
    '臣服': '🙏', 'surrender': '🙏',
    '奉爱': '💗', 'bhakti': '💗',
    '念诵': '📿', 'japa': '📿',
    '禅定': '☸️', 'dhyana': '☸️',
    '参究': '🛤️', 'self-enquiry': '🛤️', 'enquiry': '🛤️', '参究法': '🛤️',
    '修行': '🌱', 'sadhana': '🌱', 'practice': '🌱',
    '解脱': '🕊️', 'moksha': '🕊️', 'liberation': '🕊️',
    '恩典': '✨', 'grace': '✨',
    '上师': '👆', 'guru': '👆',
    '业力': '⚖️', 'karma': '⚖️',
    '觉者': '👑', 'jnani': '👑',
    '开悟': '💡', 'enlightenment': '💡',
    '自然安住': '🌿', 'sahaja': '🌿',
    '命运': '📜', 'fate': '📜',
    '自由意志': '🕊️', 'freewill': '🕊️',
    '在生解脱': '🌟', 'jivanmukti': '🌟',
    '宿业': '📜', 'prarabdha': '📜',
    '安宁': '🕊️', 'peace': '🕊️',
    '智慧': '💡', 'jnana': '💡',
    '轮回': '🔄', 'samsara': '🔄',
    '马哈希': '🙏', 'ramana': '🙏',
    '南达': '👵', 'nanda': '👵',
    '大卫': '📚', 'david': '📚',
    '临在': '✨', 'presence': '✨',
    '方法': '📖', 'method': '📖',
}

def get_icon(text, href):
    """根据文本和链接获取icon"""
    text_lower = text.lower()
    href_lower = href.lower()
    
    for key, icon in concept_icons.items():
        if key in text_lower or key in href_lower:
            return icon
    return '🔹'

def add_icon_to_tag(match):
    """给tag添加icon"""
    href = match.group(1)
    text = match.group(2).strip()
    
    # 如果已经有icon，跳过
    if any(ord(c) > 255 for c in text[:2]):
        return match.group(0)
    
    icon = get_icon(text, href)
    return f'<a href="{href}" class="tag">{icon} {text}</a>'

def fix_chapter_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modified = False
    
    # 1. 修复相关概念的tag，添加icon
    # 查找 concept-tags 或 flex-wrap 中的 tag
    content = re.sub(r'<a href="([^"]+)" class="tag">([^<]+)</a>', add_icon_to_tag, content)
    
    # 2. 检查并修复翻页导航
    # 检查是否有乱码导航（包含特殊字符）
    if re.search(r'<a href="[^"]*[\x00-\x08][^"]*" class="tag">[\x00-\x08]</a>', content):
        # 删除乱码导航
        content = re.sub(r'\s*<div class="card">\s*<div style="display:flex;justify-content:space-between;align-items:center;">\s*<a href="[^"]*[\x00-\x08][^"]*" class="tag">[\x00-\x08]</a>\s*<a href="[^"]*[\x00-\x08][^"]*" class="tag">[\x00-\x08]</a>\s*</div>\s*</div>', '', content)
        modified = True
    
    # 3. 检查是否有翻页导航，如果没有则添加
    # 从文件名提取书籍名和章节号
    match = re.match(r'(.+)-ch(\d+)\.html', filename)
    if match:
        book_name = match.group(1)
        chapter_num = int(match.group(2))
        
        # 检查是否已有导航
        has_nav = '上一章' in content or '下一章' in content
        
        if not has_nav:
            # 构建导航HTML
            prev_ch = chapter_num - 1
            next_ch = chapter_num + 1
            
            nav_html = '\n                <div class="card">\n                    <div style="display:flex;justify-content:space-between;align-items:center;">\n'
            
            if prev_ch >= 1:
                nav_html += f'                        <a href="{book_name}-ch{prev_ch}.html" class="tag">← 上一章</a>\n'
            else:
                nav_html += '                        <span></span>\n'
            
            # 检查下一章是否存在
            next_file = f'{book_name}-ch{next_ch}.html'
            if os.path.exists(next_file):
                nav_html += f'                        <a href="{next_file}" class="tag">下一章 →</a>\n'
            else:
                nav_html += '                        <span></span>\n'
            
            nav_html += '                    </div>\n                </div>'
            
            # 在 </div>\n            </div>\n        </main> 之前插入
            content = re.sub(r'(\s*</div>\s*</div>\s*</div>\s*)(</main>)', r'\1' + nav_html + r'\n            \2', content)
            modified = True
    
    if content != original or modified:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# 处理所有章节文件
chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]
chapter_files.sort()

fixed_count = 0
for f in chapter_files:
    if fix_chapter_file(f):
        print(f"修复: {f}")
        fixed_count += 1

print(f"\n共修复 {fixed_count} 个文件")
