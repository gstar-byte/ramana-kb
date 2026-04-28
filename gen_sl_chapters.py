# -*- coding: utf-8 -*-
"""
Generate chapter HTML for Surpassing Love and Grace Ch 1-10.
Uses template file to avoid quote escaping issues.
"""

import json
import os
import re

CN_NUMS = {
    1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十',
    11:'十一',12:'十二',13:'十三',14:'十四',15:'十五',16:'十六',17:'十七',18:'十八',
    19:'十九',20:'二十',21:'二十一',22:'二十二',23:'二十三',24:'二十四',25:'二十五',
    26:'二十六',27:'二十七',28:'二十八',29:'二十九',30:'三十',31:'三十一',32:'三十二',
    33:'三十三',34:'三十四',35:'三十五',36:'三十六',37:'三十七',38:'三十八',
    39:'三十九',40:'四十',41:'四十一',42:'四十二',43:'四十三'
}

CHAPTERS = {
    1: {'cn_title': '回忆录 I', 'author': 'Viswanatha Swami',
        'concepts': ['grace','silence','guru','self-enquiry','arunachala'],
        'concept_labels': ['✨ 恩典','🤫 静默','👆 上师','🔍 自我了悟','🏔️ 阿鲁那佳拉']},
    2: {'cn_title': '早期岁月', 'author': 'Swami Omkar 等',
        'concepts': ['self-enquiry','samadhi','grace','meditation'],
        'concept_labels': ['🔍 自我了悟','🧘 三摩地','✨ 恩典','🧘 冥想']},
    3: {'cn_title': '拉玛那生平场景', 'author': 'B.V. Narasimha Swami',
        'concepts': ['self-enquiry','mind','self','samadhi'],
        'concept_labels': ['🔍 自我参究','💭 心智','🕉️ 真我','🧘 三摩地']},
    4: {'cn_title': '薄伽梵如何来到我身边', 'author': 'Sadhu Trivenigiri Swami 等',
        'concepts': ['grace','guru','surrender','awakening','self-enquiry'],
        'concept_labels': ['✨ 恩典','👆 上师','🕊️ 臣服','💫 觉醒','🔍 自我了悟']},
    5: {'cn_title': '薄伽梵生平的教训', 'author': 'M.V. Krishnan',
        'concepts': ['awakening','arunachala','grace','self'],
        'concept_labels': ['💫 觉醒','🏔️ 阿鲁那佳拉','✨ 恩典','🕉️ 真我']},
    6: {'cn_title': '薄伽梵生平的教训', 'author': 'K.R.K. Murthy',
        'concepts': ['equanimity','service','egolessness','simplicity'],
        'concept_labels': ['⚖️ 平等心','🤝 服务','🕊️ 无我','🌿 简朴']},
    7: {'cn_title': '爱的奉献', 'author': 'T.P.R.',
        'concepts': ['devotion','love','guru','grace','bhakti'],
        'concept_labels': ['🙏 奉献','💝 爱','👆 上师','✨ 恩典','🙏 虔诚']},
    8: {'cn_title': '与圣山智者的难忘日子', 'author': 'Swami Desikananda, Santi',
        'concepts': ['meditation','samadhi','bliss','self','silence'],
        'concept_labels': ['🧘 冥想','🧘 三摩地','😊 喜乐','🕉️ 真我','🤫 静默']},
    9: {'cn_title': '薄伽梵的问题答复', 'author': '综合记录',
        'concepts': ['self-enquiry','mind','self','liberation','karma'],
        'concept_labels': ['🔍 自我参究','💭 心智','🕉️ 真我','🔓 解脱','🔄 业力']},
    10: {'cn_title': '追忆拉马纳', 'author': 'Chagganlal Yogi',
        'concepts': ['grace','equanimity','silence','love','guru'],
        'concept_labels': ['✨ 恩典','⚖️ 平等心','🤫 静默','💝 爱','👆 上师']},
}

SIDEBAR_TITLES = {
    1: '回忆录 I', 2: '早期岁月', 3: '拉玛那生平场景',
    4: '薄伽梵的到来', 5: '薄伽梵生平的教训', 6: '生平的教训',
    7: '爱的奉献', 8: '难忘的日子', 9: '问题答复',
    10: '追忆拉马纳', 11: '回忆录 II', 12: '薄伽梵的幽默',
    13: '对话', 14: '梦境', 15: '勿忘', 16: '转折点',
    17: 'Sein', 18: '八颂与成就者', 19: '进入怀抱',
    20: '不止是梦？', 21: '我所认识的拉马纳', 22: '沉默的恩典',
    23: '室利·拉玛那·马哈希', 24: '什么是生命？', 25: '与圣山智者的相处',
    26: '超乎理解的平安', 27: '葡萄柚', 28: '拉马纳福音',
    29: '临终时刻的解脱', 30: '伟大事件', 31: '对话 II',
    32: '室利·薄伽梵·拉马纳', 33: '我是！我是！', 34: '手段与目的',
    35: '上师肖像', 36: '拉马纳活着', 37: '今日的拉马纳道场',
    38: '求道者与求道者', 39: '阿鲁纳查拉的玛哈希', 40: '未完成的游戏',
    41: '薄伽梵论轮回', 42: '照片的效果', 43: '常在',
}

def cn(n):
    return CN_NUMS.get(n, str(n))

def build_sidebar(active):
    lines = []
    for i in range(1, 44):
        active_cls = ' active' if i == active else ''
        title = SIDEBAR_TITLES.get(i, f'第{cn(i)}章')
        lines.append(f'            <a href="surpassing-love-ch{i}.html" class="sidebar-item{active_cls}">第{cn(i)}章：{title}</a>')
    return '\n'.join(lines)

def build_concepts(meta):
    tags = []
    for label, url in zip(meta['concept_labels'], meta['concepts']):
        tags.append(f'                <a href="../concepts/{url}.html" class="tag">{label}</a>')
    return '\n'.join(tags)

def build_nav(ch_num):
    prev = ''
    if ch_num > 1:
        prev_meta = CHAPTERS[ch_num - 1]
        prev = f'            <a href="surpassing-love-ch{ch_num-1}.html"><span class="nav-label">\u2190 \u4e0a\u4e00\u7ae0</span><span class="nav-title">\u7b2c{cn(ch_num-1)}\u7ae0\uff1a{prev_meta["cn_title"]}</span></a>'
    else:
        prev = '            <span></span>'
    
    nxt = ''
    if ch_num < 43:
        next_meta = CHAPTERS.get(ch_num + 1, {'cn_title': f'\u7b2c{cn(ch_num+1)}\u7ae0'})
        nxt = f'            <a href="surpassing-love-ch{ch_num+1}.html"><span class="nav-label">\u4e0b\u4e00\u7ae0 \u2192</span><span class="nav-title">\u7b2c{cn(ch_num+1)}\u7ae0\uff1a{next_meta["cn_title"]}</span></a>'
    
    return prev, nxt

# Read content files for each chapter
CONTENT_FILES = {
    1: 'content_sl_ch1.html',
    2: 'content_sl_ch2.html',
    3: 'content_sl_ch3.html',
    4: 'content_sl_ch4.html',
    5: 'content_sl_ch5.html',
    6: 'content_sl_ch6.html',
    7: 'content_sl_ch7.html',
    8: 'content_sl_ch8.html',
    9: 'content_sl_ch9.html',
    10: 'content_sl_ch10.html',
}

# Read template
with open('template_sl_chapter.html', 'r', encoding='utf-8') as f:
    template = f.read()

count = 0
for ch_num in range(1, 11):
    meta = CHAPTERS[ch_num]
    prev_nav, next_nav = build_nav(ch_num)
    sidebar = build_sidebar(ch_num)
    concepts = build_concepts(meta)
    
    # Read chapter content
    content_file = CONTENT_FILES[ch_num]
    with open(content_file, 'r', encoding='utf-8') as f:
        chapter_content = f.read()
    
    # Source note
    source_note = ''
    if ch_num >= 9:
        source_note = '        <div class="card">\n            <p style="color:var(--text-muted);font-size:0.9rem;">\u672c\u7ae0\u5185\u5bb9\u57fa\u4e8e\u62c9\u739b\u90a3\u9a6c\u54c8\u5e0c\u6559\u4e49\u4f53\u7cfb\u6574\u7406\u3002\u5b8c\u6574\u539f\u6587\u8bf7\u53c2\u9605\u539f\u4e66\u300aSurpassing Love and Grace\u300b\u3002</p>\n        </div>'
    
    html = template
    html = html.replace('{{CH_NUM}}', str(ch_num))
    html = html.replace('{{CN_NUM}}', cn(ch_num))
    html = html.replace('{{CN_TITLE}}', meta['cn_title'])
    html = html.replace('{{AUTHOR}}', meta['author'])
    html = html.replace('{{SIDEBAR}}', sidebar)
    html = html.replace('{{PREV_NAV}}', prev_nav)
    html = html.replace('{{NEXT_NAV}}', next_nav)
    html = html.replace('{{CONCEPTS}}', concepts)
    html = html.replace('{{CHAPTER_CONTENT}}', chapter_content)
    html = html.replace('{{SOURCE_NOTE}}', source_note)
    
    filepath = os.path.join('pages/books', f'surpassing-love-ch{ch_num}.html')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1
    print(f'Generated: surpassing-love-ch{ch_num}.html ({len(html)} chars)')

print(f'\nDone! Generated {count} chapter pages.')
