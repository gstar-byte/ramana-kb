import os
import re

os.chdir(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\books')

chapter_files = [f for f in os.listdir('.') if '-ch' in f and f.endswith('.html')]
chapter_files.sort()

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

no_nav = []
no_icon = []

for f in chapter_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查是否有翻页导航（检查是否有上一章/下一章链接）
    has_nav = '上一章' in content or '下一章' in content or 'href="' + f.replace('.html', '-ch') in content
    
    # 检查相关概念的tag是否有icon
    # 查找所有 concept-tags 或 flex-wrap 中的 tag
    tags_without_icon = []
    tag_pattern = r'<a href="([^"]+)" class="tag">([^<]+)</a>'
    for match in re.finditer(tag_pattern, content):
        href = match.group(1)
        text = match.group(2).strip()
        # 检查是否已经有icon
        if not any(ord(c) > 255 for c in text[:2]):  # 简单检查前两个字符是否包含emoji
            tags_without_icon.append(text)
    
    if not has_nav:
        no_nav.append(f)
    
    if tags_without_icon:
        no_icon.append((f, tags_without_icon))

print("=== 没有翻页导航的章节 ===")
for f in no_nav:
    print(f"  - {f}")

print(f"\n=== 相关概念缺少icon的章节 ===")
for f, tags in no_icon:
    print(f"  - {f}: {tags}")

print(f"\n总计: {len(no_nav)}个没有导航, {len(no_icon)}个缺少icon")
