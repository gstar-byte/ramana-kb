#!/usr/bin/env python3
"""
批量创建概念页面
"""
import os

# 概念数据
concepts = [
    {
        "filename": "chit-jada-granthi",
        "title": "意识-物质纽结 / Chit-Jada Granthi",
        "subtitle": "真我与身体之间的纽结，需要切断以证悟真我",
        "definition": "<strong>意识-物质纽结（Chit-Jada Granthi）</strong>，又称心结或自我纽结，是真我（纯意识）与身体（惰性物质）之间的纽结。这个纽结是自我（Ego）产生的根源，也是束缚个体于轮回的根本原因。马哈希指出：自我作为真我与物理身体之间的纽结，被称为chit-jada granthi。修行的目的就是解开这个纽结。当通过自我参究追溯我念的源头时，这个纽结就会被切断，真我自然显现。",
    },
    {
        "filename": "sadhana",
        "title": "修行 / Sadhana",
        "subtitle": "通往真我的灵性修习与实践",
        "definition": "<strong>修行（Sadhana）</strong>指通往真我证悟的灵性修习与实践。在马哈希的教示中，虽然所有修行方法最终都指向自我参究，但不同的修行者可能需要不同的入门方法。马哈希说：除了自我参究之外，所有种类的修行都只是像用药物控制疯狂一样。然而，他也承认其他修行方法可以作为辅助。修行的最终目的不是获得什么新东西，而是去除我尚未证悟的无明想法，认识本来就存在的真我。",
    },
    {
        "filename": "vasanas",
        "title": "习气 / Vasanas",
        "subtitle": "深层的心理印痕和倾向，是轮回的根源",
        "definition": "<strong>习气（Vasanas）</strong>，又称潜在倾向或心理印痕，是过去经历和业力的残留，储存在心智深处，驱动着个体的行为、思想和反应模式。马哈希指出：当习气被有效地摧毁时，证悟才有可能。习气是轮回的根本——正是因为习气的存在，个体灵魂（Jiva）才会不断转世。摧毁习气的方法不是压抑，而是通过自我参究追溯其源头。当心智融入真我时，习气自然消融。",
    },
    {
        "filename": "prarabdha",
        "title": "宿业 / Prarabdha",
        "subtitle": "今生必须体验的成熟业力",
        "definition": "<strong>宿业（Prarabdha）</strong>指已经成熟、必须在今生体验的业力。与潜在的未来业力（Sanchita）不同，宿业就像已经上箭的弓，必然会被射出。马哈希解释说：一个人的今生行为是由其宿业决定的。即使是觉者（Jnani），其身体也会经历宿业，直到宿业耗尽，身体才会死亡。然而，对于觉者来说，宿业的经历不再产生束缚，因为他们已经超越了对身体的认同。",
    },
    {
        "filename": "jiva",
        "title": "个体灵魂 / Jiva",
        "subtitle": "认同身体的个体存在，是束缚的状态",
        "definition": "<strong>个体灵魂（Jiva）</strong>指认同身体和心理活动的个体存在，是束缚于轮回的状态。Jiva由真我、精微身（包括心智、智性、ego）和粗身（物理身体）组成。马哈希指出：因为人们认为他们是Jivas，克里希纳说上帝居住在心中作为Jivas的操纵者。事实上，没有Jivas，也没有操纵者；真我包含一切。Jiva的状态是幻相（Maya）的产物。当通过自我参究认识到真我时，Jiva消融于其源头，只剩下真我。",
    },
    {
        "filename": "avidya",
        "title": "无明 / Avidya",
        "subtitle": "对真实本性的无知，是束缚的根源",
        "definition": "<strong>无明（Avidya）</strong>指对真实本性的无知，是束缚于轮回的根本原因。由于无明，众生将暂时的、变化的身心现象误认为永恒的、真实的自我。马哈希指出：无明是对真我的无知。这种无知不是缺乏知识，而是错误的认同——将真我与非真我（身体、心智、ego）混淆。去除无明的方法不是积累更多知识，而是直接认识真我。自我参究就是直接面对我是谁的问题，从而消融无明，认识真我。",
    },
]

# HTML模板
template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title}是拉玛那马哈希教示的核心概念。{subtitle}">
    <meta name="keywords" content="{keywords}">
    <title>{title} | 拉玛那马哈希核心概念详解 | 拉玛那马哈希知识库</title>
    <link rel="stylesheet" href="../styles.css">
    <meta name="theme-color" content="#1a1a2e">
    <link rel="manifest" href="../manifest.json">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://ramanamaharshi.space/concepts/{filename}">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-MYFWHFPSYB');
    </script>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
            </div>
            <div class="search-box">
                <input type="text" id="search-input" placeholder="搜索标题或内容..." autocomplete="off">
                <div id="search-results"></div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item"><span class="emoji">📖</span> 书籍总览 <span class="count">18</span></a>
                    <a href="index.html" class="sidebar-item active"><span class="emoji">🔮</span> 核心概念 <span class="count">30+</span></a>
                    <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> 修行方法 <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> 修行问答 <span class="count">340+</span></a>
                    <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> 知识图谱</a>
                </div>
            </div>
        </aside>

        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">{short_title}</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../books/index.html">书籍</a>
                    <a href="index.html" class="active">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>
            
            <div class="content-wrapper">
                <nav class="breadcrumb"><a href="../index.html">首页</a> / <a href="index.html">核心概念</a> / <span>{page_title}</span></nav>
                
                <header class="page-header">
                    <h1>{title}</h1>
                    <p class="subtitle">{subtitle}</p>
                </header>
                
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📖 核心定义</h2>
                    <p style="margin-bottom:1rem;">{definition}</p>
                </div>
                
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="atman.html" class="tag">🔮 真我/Atman</a>
                        <a href="whoami.html" class="tag">🔍 "我是谁？"</a>
                        <a href="self-enquiry.html" class="tag">🛤️ 自我参究</a>
                        <a href="moksha.html" class="tag">🕊️ 解脱/Moksha</a>
                    </div>
                </div>
                
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📚 相关书籍</h2>
                    <div class="concept-tags">
                        <a href="../books/maharshi-gospel.html" class="tag">📜 马哈希福音</a>
                        <a href="../books/gems.html" class="tag">💎 宝钻集</a>
                        <a href="../books/talks.html" class="tag">💬 对谈录</a>
                    </div>
                </div>
            </div>
            
            <footer class="site-footer">
                <p>拉玛那马哈希Space | <a href="index.html">← 返回核心概念</a></p>
            </footer>
        </main>
    </div>
    
    <script src="../script.js"></script>
    <script>
        if ('serviceWorker' in navigator) {{
            navigator.serviceWorker.register('../sw.js');
        }}
    </script>
    <script src="../pwa-analytics.js"></script>
</body>
</html>
'''

output_dir = "c:/Users/willp/Desktop/2026年4月/kb01/pages/concepts"

for concept in concepts:
    filename = concept["filename"]
    title = concept["title"]
    subtitle = concept["subtitle"]
    definition = concept["definition"]
    
    short_title = title.split("/")[0].strip()
    page_title = title.split("/")[0].strip().replace(" ", "")
    keywords = f"{short_title}, 拉玛那马哈希, 真我"
    
    content = template.format(
        filename=filename,
        title=title,
        short_title=short_title,
        page_title=page_title,
        subtitle=subtitle,
        definition=definition,
        keywords=keywords
    )
    
    filepath = os.path.join(output_dir, f"{filename}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已创建: {filename}.html")

print(f"\n共创建 {len(concepts)} 个概念页面")
