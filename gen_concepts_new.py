# -*- coding: utf-8 -*-
import os

CONCEPTS_DIR = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\concepts'

concepts = [
    {
        'slug': 'antaryamin',
        'emoji': '👁️',
        'zh': '内在指引者',
        'en': 'Antaryamin',
        'subtitle': '居住在每个人心中的神圣指引',
        'desc_meta': '内在指引者（Antaryamin）是居住在每个生命心中的神圣存在，它以直觉和内在声音的形式指引求道者走向真我。拉玛那马哈希知识库。',
        'og_desc': '内在指引者是居住在每个人心中的神圣存在，以直觉形式指引求道者。',
        'cards': [
            ('📖 核心定义', '<p><strong>Antaryamin</strong>（梵文：अन्तर्यामिन्），意为"内在的控制者"或"内在指引者"。在印度灵性传统中，Antaryamin是指居住在每个生命心中的神圣存在——它不是外在的神，而是你内在最深处那个永恒的觉知。</p><div class="quote-box">"上师不在外面。真正的上师在你心中。那个告诉你\u2018我在\u2019的，就是上师。追随那个声音。"<div class="source">— 室利·拉玛那·马哈希</div></div><p>马哈希强调，Antaryamin不是什么神秘的存在，它就是你自己的真我——那个纯粹的觉知。当你安静下来、停止追逐外在的认可时，你就会听到它的声音。</p>'),
            ('💡 详解', '<p>如何辨别Antaryamin的指引和心智的噪音？马哈希给出了几个标准：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>安静</strong>：真正的内在指引是安静的，不带有强烈的情绪色彩</li><li><strong>确定</strong>：它带来一种不需要理由的确定感</li><li><strong>持久</strong>：它不会反复摇摆，一旦出现就保持稳定</li><li><strong>无私</strong>：真正的指引服务于更高的善，而非个人欲望</li></ul><p>马哈希说，最可靠的"内在指引"就是"我是谁？"这个问题本身。当你持续地问这个问题时，Antaryamin自然会引导你走向答案。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="atman.html" class="tag">🔮 真我/Atman</a><a href="guru.html" class="tag">👆 上师/Guru</a><a href="self-enquiry.html" class="tag">🔍 自我参究</a><a href="grace.html" class="tag">✨ 恩典/Grace</a></div>')
        ]
    },
    {
        'slug': 'upadesha',
        'emoji': '📜',
        'zh': '灵性教导',
        'en': 'Upadesha',
        'subtitle': '直指真我的灵性传授',
        'desc_meta': '灵性教导（Upadesha）是上师直指真我的灵性传授，马哈希的教导核心是"我是谁"的自我参究。拉玛那马哈希知识库。',
        'og_desc': '灵性教导是上师直指真我的传授，马哈希的核心教导是自我参究。',
        'cards': [
            ('📖 核心定义', '<p><strong>Upadesha</strong>（梵文：उपदेश），意为"教导"、"指示"或"传授"。在灵性传统中，Upadesha不是普通的知识传授，而是上师直接将弟子引向真理的力量——它通过言语、沉默、眼神甚至仅仅是临在来传递。</p><div class="quote-box">"真正的Upadesha不需要语言。我的沉默就是最好的教导。但在沉默中无法理解的人，我用语言来帮助他们。语言是指向月亮的手指——不要把手指当成月亮。"<div class="source">— 室利·拉玛那·马哈希</div></div>'),
            ('💡 马哈希的教导方式', '<p>马哈希的Upadesha有几个层次：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>沉默（Mauna）</strong>：最高形式的教导，直接传递真知的振动</li><li><strong>"我是谁？"</strong>：核心的言语教导，一句话概括了整个灵性道路</li><li><strong>经典引用</strong>：引用奥义书、薄伽梵歌等来解释和佐证</li><li><strong>具体回答</strong>：针对弟子个人的具体问题给予精准的回应</li></ul><p>马哈希认为，最好的Upadesha是让弟子自己去体验，而不是依赖上师的话语。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="guru.html" class="tag">👆 上师/Guru</a><a href="silence.html" class="tag">🤫 静默/Silence</a><a href="jnana.html" class="tag">🕯️ 智慧/Jnana</a><a href="self-enquiry.html" class="tag">🔍 自我参究</a></div>')
        ]
    },
    {
        'slug': 'satya',
        'emoji': '⚖️',
        'zh': '真理',
        'en': 'Satya',
        'subtitle': '不变的实在——超越言语的终极真理',
        'desc_meta': '真理（Satya）是吠檀多哲学中不变的真实存在，超越所有相对层面的描述。拉玛那马哈希知识库。',
        'og_desc': '真理是吠檀多中不变的真实存在，超越所有相对层面的描述。',
        'cards': [
            ('📖 核心定义', '<p><strong>Satya</strong>（梵文：सत्य），意为"真理"、"真实"或"实在"。在印度哲学中，Satya不是一种观点或信念，而是那个永恒不变的存在本身——它是所有描述指向的对象，却永远无法被任何描述完全捕捉。</p><div class="quote-box">"Satya不是你能说的任何东西。当你停止所有的言语和思想，剩下的那个——就是Satya。但即使这样说也不完全准确，因为\u2018剩下\u2019意味着有什么被移除了，而Satya从来不在也不离开。"<div class="source">— 室利·拉玛那·马哈希</div></div><p>马哈希指出，追求Satya不意味着你需要找到某个"终极答案"，而是认出那个一直在那里的——你的真我。</p>'),
            ('💡 详解', '<p>Satya在吠檀多中有三个层面：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>相对真理（Vyavaharika Satya）</strong>：日常生活中的实用真理——水能解渴、火会燃烧</li><li><strong>经验真理（Pratibhasika Satya）</strong>：个人的主观体验——梦境、幻觉</li><li><strong>终极真理（Paramarthika Satya）</strong>：唯一不变的实在——真我/梵</li></ul><p>马哈希说：真正的Satya追求者最终会发现，真理不是一个"东西"，而是那个让所有"东西"得以被感知的觉知本身。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="brahman.html" class="tag">🕉️ 梵/Brahman</a><a href="atman.html" class="tag">🔮 真我/Atman</a><a href="advaita.html" class="tag">🔯 非二元/Advaita</a><a href="satchidananda.html" class="tag">✨ 存-知-乐</a></div>')
        ]
    },
    {
        'slug': 'samskara',
        'emoji': '🌀',
        'zh': '心理印记',
        'en': 'Samskara',
        'subtitle': '深藏于潜意识中的印象与倾向',
        'desc_meta': '心理印记（Samskara）是深藏于潜意识中的印象和倾向，它们驱动着我们的习惯反应和行为模式。拉玛那马哈希知识库。',
        'og_desc': '心理印记是深藏于潜意识中的印象和倾向，驱动着习惯反应和行为模式。',
        'cards': [
            ('📖 核心定义', '<p><strong>Samskara</strong>（梵文：संस्कार），意为"印象"、"倾向"或"潜能"。它是过去所有经历——包括今生和前世——在心智中留下的深层印记。Samskara不像普通的记忆那样可以被回忆，而是以一种隐性的方式影响我们的反应模式、偏好和恐惧。</p><div class="quote-box">"你的所有习惯反应都是Samskara。当有人批评你时你生气，当有人赞美你时你高兴——这些都是储存已久的印象在自动运作。修行不是去压制这些反应，而是去认识那个反应的\u2018我\u2019是谁。"<div class="source">— 室利·拉玛那·马哈希</div></div>'),
            ('💡 Samskara与修行', '<p>Samskara与Vasana（习气）密切相关，但有所不同：Vasana是活跃的倾向，Samskara是潜在的印记。马哈希说：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>它们如何形成</strong>：每一次有执着的行为都会加深Samskara</li><li><strong>它们如何运作</strong>：当外在条件匹配时，Samskara被激活成为Vasana</li><li><strong>如何消除</strong>：不是对抗它们，而是通过自我参究让注意力离开心智层面</li></ul><p>马哈希强调：当你在自我参究中深入到真我的层面时，Samskara就像影子——它还在那里，但因为你站在了光中，影子不再能影响你。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="vasanas.html" class="tag">🌀 习气/Vasanas</a><a href="karma.html" class="tag">🔄 业力/Karma</a><a href="mind.html" class="tag">🧠 心智/Mind</a><a href="self-enquiry.html" class="tag">🔍 自我参究</a></div>')
        ]
    },
    {
        'slug': 'vichara',
        'emoji': '🔎',
        'zh': '参究',
        'en': 'Vichara',
        'subtitle': '深入探究事物本质的灵性方法',
        'desc_meta': '参究（Vichara）是深入探究事物本质的灵性方法，马哈希教导的核心就是"我是谁"的参究。拉玛那马哈希知识库。',
        'og_desc': '参究是深入探究事物本质的方法，马哈希教导的核心是自我参究。',
        'cards': [
            ('📖 核心定义', '<p><strong>Vichara</strong>（梵文：विचार），意为"探究"、"思考"或"参究"。与普通的思考不同，Vichara不是概念性的分析，而是将注意力深入到事物的源头。在马哈希的教导中，Vichara特指"自我参究"（Atma-Vichara）——追踪"我"的感觉，直到发现它的源头。</p><div class="quote-box">"Vichara不是去想\u2018我是谁\u2019这个问题。Vichara是让注意力转向那个提出问题的\u2018我\u2019。不是分析答案，而是找到提问者。当你找到那个\u2018我\u2019的源头时，所有的疑问都会消失。"<div class="source">— 室利·拉玛那·马哈希</div></div>'),
            ('💡 Vichara的实践', '<p>Vichara与其他冥想方法的根本区别在于方向：大多数冥想方法是向外的（观呼吸、念佛号、观想），而Vichara是向内的——向着自己的源头。</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>第一步</strong>：当任何念头升起时，问"这个念头出现在谁的心中？"</li><li><strong>第二步</strong>：回答"在我心中"后，继续问"这个\u2018我\u2019是什么？"</li><li><strong>第三步</strong>：注意力转向那个"我"的感觉，停留在那里</li><li><strong>第四步</strong>：念头会消失，"我"的感觉会消融于真我之中</li></ul><p>马哈希说：Vichara不需要特殊的技巧，只需要诚实地、持续地将注意力转向内在。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="atma-vichara.html" class="tag">🕯️ 阿特玛·维查拉</a><a href="self-enquiry.html" class="tag">🔍 自我参究</a><a href="jnana.html" class="tag">📖 智慧/Jnana</a><a href="dhyana.html" class="tag">🧘 冥想/Dhyana</a></div>')
        ]
    },
    {
        'slug': 'manonasha',
        'emoji': '💥',
        'zh': '心智消融',
        'en': 'Manonasha',
        'subtitle': '心智在真我面前的彻底消融',
        'desc_meta': '心智消融（Manonasha）是心智在真我面前彻底消融的状态，是证悟的关键时刻。拉玛那马哈希知识库。',
        'og_desc': '心智消融是心智在真我面前彻底消融的状态，是证悟的关键时刻。',
        'cards': [
            ('📖 核心定义', '<p><strong>Manonasha</strong>（梵文：मनोनाश），意为"心智的毁灭"或"心智的消融"。这不是物理意义上大脑的损伤，而是指个体ego认同的心智在遇到真我之光时彻底消散——就像黑暗遇到阳光时自然消失。</p><div class="quote-box">"Manonasha不是你努力去消灭心智。它是当你的注意力完全停留在真我上时，心智因为失去了滋养而自然枯萎。就像火焰在油尽时自然熄灭一样——不需要你去吹灭它。"<div class="source">— 室利·拉玛那·马哈希</div></div><p>马哈希强调，Manonasha不是修行的"结果"，而是当你真正深入自我参究时必然发生的事情。</p>'),
            ('💡 消融的过程', '<p>心智消融不是一瞬间的事件，而是一个渐进的过程：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>第一阶段</strong>：念头变少，内心变得比较安静</li><li><strong>第二阶段</strong>：即使在日常生活中，也能保持一定的觉知距离</li><li><strong>第三阶段</strong>：在深度参究中，心智暂时停止运作</li><li><strong>最终阶段</strong>：个体认同完全消融，只剩下纯粹的觉知</li></ul><p>马哈希说：不要追求Manonasha。追求"我是谁"，Manonasha会作为副产品自然到来。就像不要追求黑暗消失——追求光明就好。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="mind.html" class="tag">🧠 心智/Mind</a><a href="ego.html" class="tag">🎭 自我(ego)</a><a href="samadhi.html" class="tag">🧘 三摩地</a><a href="turiya.html" class="tag">🌌 第四境</a></div>')
        ]
    },
    {
        'slug': 'lakshya',
        'emoji': '🎯',
        'zh': '灵性目标',
        'en': 'Lakshya',
        'subtitle': '修行者应当聚焦的终极目标',
        'desc_meta': '灵性目标（Lakshya）是修行者应当聚焦的终极目标——认识真我。拉玛那马哈希知识库。',
        'og_desc': '灵性目标是修行者应当聚焦的终极目标——认识真我。',
        'cards': [
            ('📖 核心定义', '<p><strong>Lakshya</strong>（梵文：लक्ष्य），意为"目标"、"标的"或"焦点"。在灵性修行中，Lakshya是修行者应当始终聚焦的终极目标——不是获得神通、不是追求特殊体验、不是达到某个境界，而是认识自己的真实本性。</p><div class="quote-box">"很多人把修行目标弄错了。他们追求 visions、追求和平、追求力量。这些都会来，但它们不是Lakshya。你的Lakshya只有一个：找到那个提出所有追求的\u2018我\u2019。当你找到它，所有其他的追求都会显得毫无意义。"<div class="source">— 室利·拉玛那·马哈希</div></div>'),
            ('💡 识别和保持焦点', '<p>马哈希教导了如何识别和保持Lakshya：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>简化目标</strong>：不追求多重目标，只专注于"我是谁"</li><li><strong>不执着副产品</strong>：冥想中的平静、光明等体验都是副产品，不要执着</li><li><strong>回归核心</strong>：当注意力散乱时，温柔地带回"我是谁"</li><li><strong>信任过程</strong>：即使看不到进度，持续坚持就是最大的进步</li></ul><p>马哈希说：射箭的人不会同时看着弓、箭、风和目标——他只看目标。修行者也是一样，只看Lakshya。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="self-enquiry.html" class="tag">🔍 自我参究</a><a href="jnana.html" class="tag">🕯️ 智慧/Jnana</a><a href="abhyasa.html" class="tag">🔁 持续练习</a><a href="nishtha.html" class="tag">🎯 坚定/Nishtha</a></div>')
        ]
    },
    {
        'slug': 'satsang',
        'emoji': '🤝',
        'zh': '圣者相聚',
        'en': 'Satsang',
        'subtitle': '与真理和求道者的联结',
        'desc_meta': '圣者相聚（Satsang）是与真理和求道者的联结，是灵性成长的重要助力。拉玛那马哈希知识库。',
        'og_desc': '圣者相聚是与真理和求道者的联结，是灵性成长的重要助力。',
        'cards': [
            ('📖 核心定义', '<p><strong>Satsang</strong>（梵文：सत्सङ्ग），由"Sat"（真理）和"Sangha"（联结/群体）组成，意为"与真理的联结"或"与圣者的聚会"。传统上，Satsang是指弟子们聚集在上师身边聆听教导的场合。但马哈希对Satsang有更深的理解。</p><div class="quote-box">"Satsang不一定要面对面地坐在一起。当你读一本真正的灵性书籍时，那是Satsang。当你在心中默念上师的名字时，那是Satsang。当你安静地坐着、保持觉知时，你和真我的在一起就是最好的Satsang。"<div class="source">— 室利·拉玛那·马哈希</div></div>'),
            ('💡 Satsang的力量', '<p>Satsang之所以重要，是因为它提供了几个关键的支持：</p><ul style="margin-left:1.5rem;line-height:2;"><li><strong>共振</strong>：与同样追求真理的人在一起，会产生灵性的共振效应</li><li><strong>榜样</strong>：看到别人在修行中前进，会激励自己继续</li><li><strong>纠偏</strong>：在困惑时，上师或同修可以帮助你回到正确的方向</li><li><strong>恩典</strong>：在上师的临在中，灵性转化会加速</li></ul><p>马哈希说：最内在的Satsang是与真我的在一起。当你安住在真我中时，整个宇宙都是你的Satsang。</p>'),
            ('🔗 相关概念', '<div class="concept-tags"><a href="guru.html" class="tag">👆 上师/Guru</a><a href="grace.html" class="tag">✨ 恩典/Grace</a><a href="sadhana.html" class="tag">🛤️ 修行/Sadhana</a><a href="bhakti.html" class="tag">❤️ 虔诚/Bhakti</a></div>')
        ]
    }
]

def gen_concept_html(c):
    slug = c['slug']
    cards_html = '\n'.join(
        '<div class="card">\n'
        '    <h2>{title}</h2>\n'
        '    {content}\n'
        '</div>'.format(title=title, content=content)
        for title, content in c['cards']
    )
    
    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{zh} {en} | 拉玛那马哈希知识库</title>
    <meta name="description" content="{desc_meta}">
    <link rel="stylesheet" href="../styles.css">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://ramanamaharshi.space/concepts/{slug}.html">
    <meta property="og:title" content="{zh} {en} | 拉玛那马哈希知识库">
    <meta property="og:description" content="{og_desc}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="zh_CN">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-MYFWHFPSYB');</script>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header"><a href="../index.html" class="logo">🙏 拉玛那知识库</a></div>
            <div class="search-box"><input type="text" id="search-input" placeholder="搜索..." autocomplete="off"><div id="search-results"></div></div>
            <div class="sidebar-section"><div class="sidebar-section-title">📚 核心索引</div><div class="sidebar-items"><a href="../index.html" class="sidebar-item">🏠 首页</a><a href="../books/index.html" class="sidebar-item">📖 书籍</a><a href="index.html" class="sidebar-item active">🔮 核心概念</a><a href="../methods/index.html" class="sidebar-item">🛤️ 方法</a><a href="../qa/index.html" class="sidebar-item">💬 问答</a><a href="../persons/index.html" class="sidebar-item">👤 人物</a><a href="../graph.html" class="sidebar-item">🕸️ 图谱</a></div></div>
        </aside>
        <main class="main-content">
            <header class="topbar"><div class="topbar-left"><button class="menu-toggle" onclick="toggleSidebar()">☰</button><span class="topbar-title">🔮 {zh}</span></div><nav class="topbar-nav topbar-full"><a href="../index.html">首页</a><a href="../books/index.html">书籍</a><a href="index.html" class="active">概念</a><a href="../methods/index.html">方法</a><a href="../qa/index.html">问答</a><a href="../persons/index.html">人物</a><a href="../graph.html">图谱</a></nav></header>
            <div class="content-wrapper">
                <nav class="breadcrumb"><a href="../index.html">首页</a> / <a href="index.html">核心概念</a> / <span>{emoji} {zh} {en}</span></nav>
                <article class="concept-detail">
                    <header class="page-header">
                        <h1>{emoji} {zh} / {en}</h1>
                        <p class="subtitle">{subtitle}</p>
                    </header>
                    {cards_html}
                </article>
            </div>
            <footer class="site-footer">
                <p><a href="../index.html">拉玛那马哈希</a> | 传承自印度阿鲁那佳拉圣山</p>
                <p style="margin-top:0.5rem; font-size:0.9rem; color: var(--text-muted);">© 2026 拉玛那马哈希. 保留所有权利。</p>
                <p style="margin-top:1rem; font-size:0.9rem;"><a href="../sitemap.html" style="color: var(--text-muted); text-decoration: underline;">🌐 网站地图</a> <span style="margin: 0 1rem;">|</span> <a href="mailto:591611431@qq.com" style="color: var(--text-muted); text-decoration: underline;">联系我</a></p>
            </footer>
        </main>
    </div>
    <script src="../script.js"></script>
    <script>if ('serviceWorker' in navigator) {{ navigator.serviceWorker.register('../sw.js'); }}</script>
    <script src="../pwa-analytics.js"></script>
</body>
</html>'''.format(
        slug=slug, emoji=c['emoji'], zh=c['zh'], en=c['en'],
        subtitle=c['subtitle'], desc_meta=c['desc_meta'], og_desc=c['og_desc'],
        cards_html=cards_html
    )
    return html

for c in concepts:
    html = gen_concept_html(c)
    path = os.path.join(CONCEPTS_DIR, c['slug'] + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Created {}: {} ({})'.format(c['slug'], c['zh'], c['en']))

print('\nDone! 8 concept pages created.')
