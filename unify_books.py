import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

# 书籍信息映射（用于相关书籍推荐）
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
    '我是谁？': '🔍', 'whoami': '🔍', 'who am i': '🔍',
    '静默': '🤫', 'silence': '🤫',
    '三摩地': '🧘', 'samadhi': '🧘',
    '臣服': '🙏', 'surrender': '🙏',
    '奉爱': '💗', 'bhakti': '💗',
    '念诵': '📿', 'japa': '📿',
    '禅定': '☸️', 'dhyana': '☸️',
    '参究': '🛤️', 'self-enquiry': '🛤️', 'enquiry': '🛤️',
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
}

def get_icon_for_concept(text, href):
    """根据概念文本和链接确定icon"""
    text_lower = text.lower()
    href_lower = href.lower()
    
    for key, icon in concept_icons.items():
        if key in text_lower or key in href_lower:
            return icon
    return '🔹'  # 默认icon

def add_icon_to_concept_tag(match):
    """给concept-tag添加icon"""
    full_tag = match.group(0)
    href = re.search(r'href="([^"]+)"', full_tag)
    text = re.search(r'>([^<]+)</a>', full_tag)
    
    if href and text:
        href_val = href.group(1)
        text_val = text.group(1)
        icon = get_icon_for_concept(text_val, href_val)
        # 替换为带icon的tag样式
        new_tag = full_tag.replace('class="concept-tag"', 'class="tag"')
        new_tag = new_tag.replace(f'>{text_val}</a>', f'>{icon} {text_val}</a>')
        return new_tag
    return full_tag

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 转换 concept-tag 为 tag（添加icon）
    content = re.sub(r'<a[^>]*class="concept-tag"[^>]*>[^<]*</a>', add_icon_to_concept_tag, content)
    
    # 2. 检查是否有相关书籍区域
    has_related_books = '相关书籍' in content
    
    if not has_related_books and filename in book_relations:
        # 在源文档区域之前添加相关书籍
        related = book_relations[filename]
        related_html = '                <!-- 相关书籍 -->\n                <div class="card">\n                    <h2 style="color:var(--primary);margin-bottom:1rem;">📚 相关书籍</h2>\n                    <div class="concept-tags">\n'
        for rel_file in related:
            if rel_file in book_titles:
                related_html += f'                        <a href="{rel_file}" class="tag">{book_titles[rel_file]}</a>\n'
        related_html += '                    </div>\n                </div>\n                \n'
        
        # 在 <!-- 源文档 --> 之前插入
        content = content.replace('                <!-- 源文档 -->', related_html + '                <!-- 源文档 -->')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename, has_related_books

# 处理所有书籍页面
files = [f for f in os.listdir('.') if f.endswith('.html') and '-ch' not in f and f != 'index.html']
files.sort()

for f in files:
    result = process_file(f)
    print(f"处理: {result[0]} (原有相关书籍: {'是' if result[1] else '否'})")

print("\n完成!")
