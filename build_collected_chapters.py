# -*- coding: utf-8 -*-
"""
创建《权威合集》四个章节页面
"""
import os, re

BASE  = r'c:/Users/willp/Desktop/2026年4月/kb01'
BOOKS = os.path.join(BASE, 'pages', 'books')
SRC   = os.path.join(BASE, 'pdf_content', 'collected_works.txt')

with open(SRC, encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')

def segment(start, end=None):
    return '\n'.join(lines[start-1:end])

def clean(text):
    text = re.sub(r'\n--- 第\d+页 ---\n\d+\n', '\n', text)
    text = re.sub(r'\n--- 第\d+页 ---\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

SHARED_SIDEBAR = '''            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item active"><span class="emoji">📖</span> 书籍总览 <span class="count">18</span></a>
                    <a href="../concepts/index.html" class="sidebar-item"><span class="emoji">🔮</span> 核心概念 <span class="count">30+</span></a>
                    <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> 修行方法 <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> 修行问答 <span class="count">28</span></a>
                    <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> 知识图谱</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📖 经典著作</div>
                <div class="sidebar-items">
                    <a href="be-as-you-are.html" class="sidebar-item">📖 走向静默，如你本来</a>
                    <a href="gems.html" class="sidebar-item">💎 宝钻集</a>
                    <a href="talks.html" class="sidebar-item">💬 对谈录</a>
                    <a href="back-to-heart.html" class="sidebar-item">📕 回到你心中</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📅 对话与日记</div>
                <div class="sidebar-items">
                    <a href="day-by-day.html" class="sidebar-item">📅 日日与彼</a>
                    <a href="face-to-face.html" class="sidebar-item">👁️ 面对面</a>
                    <a href="maharshi-gospel.html" class="sidebar-item">📜 马哈希福音</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 哲学专著</div>
                <div class="sidebar-items">
                    <a href="collected-works.html" class="sidebar-item active">📚 权威合集</a>
                    <a href="spiritual-stories.html" class="sidebar-item">📖 灵性故事</a>
                    <a href="reflections.html" class="sidebar-item">💭 反思录</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📗 其他著作</div>
                <div class="sidebar-items">
                    <a href="teachings.html" class="sidebar-item">📝 以言传意</a>
                    <a href="surpassing-love.html" class="sidebar-item">💝 超越爱与恩典</a>
                    <a href="crumbs.html" class="sidebar-item">🍞 桌边碎语</a>
                    <a href="timeless.html" class="sidebar-item">⏳ 时代中的永恒</a>
                </div>
            </div>
'''

FOOTER_NAV = '''            <div class="page-nav">
                <a href="collected-works.html"><span class="nav-label">← 返回全书</span><span class="nav-title">📚 权威合集</span></a>
                <a href="{next_file}"><span class="nav-label">{next_label} →</span><span class="nav-title">{next_title}</span></a>
            </div>

            <footer class="site-footer">
                <p><a href="../index.html">拉玛那马哈希</a> | 传承自印度阿鲁那佳拉圣山</p>
                <p style="margin-top:0.5rem; font-size:0.9rem; color: var(--text-muted);">© 2026 拉玛那马哈希. 保留所有权利。</p>
                <p style="margin-top:1rem; font-size:0.9rem;"><a href="../sitemap.html" style="color: var(--text-muted); text-decoration: underline;">🌐 网站地图</a></p>
            </footer>
        </main>
    </div>
    <script>
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('../sw.js').catch(function() {});
    }
    </script>
</body>
</html>
'''

def make_page(title, desc, kw, canon, body_html, next_file, next_label, next_title):
    footer = FOOTER_NAV.replace('{next_file}', next_file) \
                        .replace('{next_label}', next_label) \
                        .replace('{next_title}', next_title)
    return '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="拉玛那,马哈希,灵性修行,自我了悟,阿鲁那佳拉,{kw}">
    <link rel="stylesheet" href="../styles.css">
    <link rel="manifest" href="../manifest.json">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://ramanamaharshi.space/books/{canon}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ramanamaharshi.space/books/{canon}">
    <meta property="og:locale" content="zh_CN">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
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
                <input type="text" id="search-input" placeholder="搜索..." autocomplete="off">
                <div id="search-results"></div>
            </div>
{sidebar}
        </aside>
        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">📚 权威合集</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../books/index.html" class="active">书籍</a>
                    <a href="../concepts/index.html">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>
{body}
{footer}
'''.format(title=title, desc=desc, kw=kw, canon=canon,
           sidebar=SHARED_SIDEBAR, body=body_html, footer=footer)

# ============================================================
# 章节1: Self-Enquiry
# ============================================================
ch1_body = '''
                <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="collected-works.html">权威合集</a> /
                    <span>自我参究</span>
                </nav>

                <header class="page-header">
                    <h1>自我参究</h1>
                    <p class="subtitle">Self-Enquiry (Vichara Sangraham) | Sri Ramana Maharshi 原著</p>
                </header>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📖 章节概要</h2>
                    <p><strong>《自我参究》</strong>是马哈希最早撰写的著作，写于1901年，当时他年约二十二岁，已是证悟真我的觉者。他住在阿鲁那佳拉山的维鲁帕克沙洞穴中，以文字答复早期弟子的问题。这部著作奠定了马哈希"参究自我"教法的根基。</p>
                    <p>开篇即问："有没有一种崇拜至上者的方法，超越一切，除了安住于彼？"——答案就是安住于真我之中。马哈希说："只有两条路：问自己'我是谁？'，或者归伏上师。"</p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">💬 核心问答</h2>
                    <div class="quote-box">
                        <strong>问：</strong>有没有一种崇拜至上者的方法，超越一切，除了安住于彼？<br><br>
                        <strong>答：</strong>除了坚定地安住于"我是彼"之外，没有其他方式能崇拜那超越一切的上帝。
                    </div>
                    <div class="quote-box">
                        <strong>问：</strong>如何参究"我是谁"？<br><br>
                        <strong>答：</strong>行走、归来、存在、行动等体验，人人会自然产生。"我"这个意识难道不是那些行为的主体吗？参究那个意识的真实本性，安住于自己——这就是理解"我是谁"的方法。
                    </div>
                    <div class="quote-box">
                        <strong>问：</strong>如何将心意引向"我是谁"？<br><br>
                        <strong>答：</strong>当其他念头升起时，不追随它们，而是问："这念头是谁起的？"答案是"我"。于是问："我是谁？"心意回到它自身，"我"这个念头便消融了。
                    </div>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">✨ 修行指引</h2>
                    <ul>
                        <li>当念头升起时，不追随它，而是问："这个念头是谁起的？" → 答案"我" → 问："我是谁？"</li>
                        <li>心意回到"我"的源头，念头消融</li>
                        <li>持续参究，直到念头不再升起</li>
                        <li>"我"的念头也消失时，便只剩下纯粹的觉知——真我</li>
                    </ul>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📜 原文节选（英译）</h2>
                    <p style="font-style:italic; color:var(--text-muted);">
                        "Is there any way of adoring the Supreme which is all, except by abiding firmly as That?"<br><br>
                        — Invocation, Self-Enquiry<br><br>
                        "How is one to enquire 'Who am I?'"<br><br>
                        "Actions such as 'going' and 'coming' belong only to the body. The 'I' which is the form of knowledge — that 'I' does not go or come. The body was not, when one was in sleep; it is not, when one is asleep; it is not the truth."
                    </p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 "我是谁？"</a>
                        <a href="../concepts/mind.html" class="tag">🧠 心智</a>
                        <a href="../concepts/awareness.html" class="tag">👁️ 觉知</a>
                        <a href="../concepts/samadhi.html" class="tag">🧘 三摩地</a>
                        <a href="../concepts/surrender.html" class="tag">🙏 归伏</a>
                    </div>
                </div>
                </div>
'''

page1 = make_page(
    '自我参究 Self-Enquiry | 权威合集',
    '《自我参究》(Vichara Sangraham) 是马哈希最早撰写的著作，奠定自我参究教法的根基，包含26组问答。',
    '自我参究,Vichara Sangraham',
    'collected-works-self-enquiry',
    ch1_body,
    'collected-works-whoami.html', '下一章', '我是谁？'
)
with open(os.path.join(BOOKS, 'collected-works-self-enquiry.html'), 'w', encoding='utf-8') as f:
    f.write(page1)
print('OK collected-works-self-enquiry.html')

# ============================================================
# 章节2: Who Am I?
# ============================================================
ch2_body = '''
                <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="collected-works.html">权威合集</a> /
                    <span>我是谁？</span>
                </nav>

                <header class="page-header">
                    <h1>我是谁？</h1>
                    <p class="subtitle">Nan Yar? (Who Am I?) | Sri Ramana Maharshi 原著</p>
                </header>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📖 章节概要</h2>
                    <p><strong>《我是谁？》</strong>（泰米尔语 Nan Yar?，意为"我是谁？"）是马哈希最广为人知的短文。最开始是锡伐普拉卡萨姆·皮莱问的一系列问答，后来整理成连贯的论述。</p>
                    <p>开篇指出：一切众生恒常想要快乐、无有痛苦；每个人对自己都有至高的爱——而幸福是爱的原因。要获得那本是自性的幸福，必须认识自我。而"我是谁？"这个形式的参究，是最主要的方法。</p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">💬 核心问答</h2>
                    <div class="quote-box">
                        <strong>1. 我是谁？</strong><br><br>
                        由七种液体所成的粗身，我不是；五种认知感官（耳、皮、眼、舌、鼻），我不是；五种行动感官（口、足、手、排泄、生殖），我不是；五种生命气（般那等），我不是；甚至连思考的心意，我也不是；那仅带有对象残余印象的无明，我也不是。
                    </div>
                    <div class="quote-box">
                        <strong>2. 如果我都不是这些，那我是什么？</strong><br><br>
                        "我是谁？"这个念头之后，所有其他念头都会消亡。"我是谁？"这个念头将其他念头摧毁后，它自身也会消亡。于是安住于"我就是那"——真我闪耀之处。
                    </div>
                    <div class="quote-box">
                        <strong>10. 何为解脱？</strong><br><br>
                        探究被困缚的自己之本性，证悟自己的真实本性，即是解脱。应当始终安住于真我，不受"我"这个错觉所染。
                    </div>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">✨ 修行指引</h2>
                    <ul>
                        <li><strong>否定层面：</strong>我不是身体、感官、心意、无明——它们都会消失</li>
                        <li><strong>肯定层面：</strong>剩下的那个"我"就是真我</li>
                        <li><strong>方法：</strong>"我是谁？"摧毁其他一切念头后，它自己也消亡</li>
                        <li><strong>结果：</strong>安住于"我就是那"——本自具足的存在-意识-喜悦</li>
                    </ul>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📜 原文节选（英译）</h2>
                    <p style="font-style:italic; color:var(--text-muted);">
                        "As all living beings desire to be happy always, without misery, as in the case of everyone there is observed supreme love for one's self, and as happiness alone is the cause for love, in order to gain that happiness which is one's nature and which is experienced in the state of deep sleep where there is no mind, one should know one's Self. For that, the path of knowledge, the enquiry of the form 'Who am I?', is the principal means."<br><br>
                        — Who Am I?, Introduction
                    </p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 "我是谁？"</a>
                        <a href="../concepts/atman.html" class="tag">🔮 真我</a>
                        <a href="../concepts/mind.html" class="tag">🧠 心智</a>
                        <a href="../concepts/awareness.html" class="tag">👁️ 觉知</a>
                        <a href="../concepts/world.html" class="tag">🌍 世界</a>
                    </div>
                </div>
                </div>
'''

page2 = make_page(
    '我是谁？ Nan Yar? | 权威合集',
    '《我是谁？》(Nan Yar?) 是马哈希最广为人知的短文，以10组问答精炼阐述自我参究的精髓。',
    '我是谁,自我参究',
    'collected-works-whoami',
    ch2_body,
    'collected-works-upadesa-saram.html', '下一章', '本心十论'
)
with open(os.path.join(BOOKS, 'collected-works-whoami.html'), 'w', encoding='utf-8') as f:
    f.write(page2)
print('OK collected-works-whoami.html')

# ============================================================
# 章节3: Upadesa Saram (本心十论)
# ============================================================
ch3_body = '''
                <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="collected-works.html">权威合集</a> /
                    <span>本心十论</span>
                </nav>

                <header class="page-header">
                    <h1>本心十论</h1>
                    <p class="subtitle">Upadesa Saram | Sri Ramana Maharshi 原著</p>
                </header>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📖 章节概要</h2>
                    <p><strong>《本心十论》</strong>（Upadesa Saram）是马哈希亲笔撰写的核心教义，以十节诗精炼阐述了自我参究的精髓。这部著作是马哈希教法的纲要性文献，每一颂都是通往证悟的指引。</p>
                    <p>马哈希在诗中指出：一切众生皆因无明而认身体为"我"；自我参究即是认出真我；真我即是"我在"的觉知本身；安住于此，则一切皆安住。</p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📜 原文十颂（英译）</h2>
                    <div class="quote-box">1. 世界遮蔽了心意；以"我是谁？"参究，世界被否定；而那心意——世界之芽的种子——熄灭了。</div>
                    <div class="quote-box">2. 参究即是：将心意保持在真我之中。</div>
                    <div class="quote-box">3. 冥想即是：思维自己的自性是梵，是存在-意识-喜悦。</div>
                    <div class="quote-box">4. 以参究，心意变得纯净；以冥想，心意变得稳定；以奉爱，心意消融；以静默，心意成为一。</div>
                    <div class="quote-box">5. 有两条路：问自己"我是谁？"或归伏上师。前者是智慧瑜伽，后者是奉爱瑜伽。两者皆摧毁自我。</div>
                    <div class="quote-box">6. 自我参究的修行随时可行；其他修行需要特定条件，因而困难。</div>
                    <div class="quote-box">7. 心意只是一捆念头；"我"是这捆念头的根本；因此自我参究即是参究心意的根本。</div>
                    <div class="quote-box">8. 当"我"的念头被摧毁，所有其他念头都被摧毁。如同砍树根，一切枝叶枯萎。</div>
                    <div class="quote-box">9. 何为解脱？探究被困缚的自己之本性，证悟自己的真实本性，即是解脱。</div>
                    <div class="quote-box">10. 自我参究的修行是通往证悟的直接道路；其他一切修行汇聚于此。</div>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">✨ 核心洞见</h2>
                    <ul>
                        <li><strong>唯一道路：</strong>自我参究是直接通往证悟的道路，其他一切修行最终都汇聚于此</li>
                        <li><strong>心意本质：</strong>心意只是一捆念头，"我"是这捆念头的根本</li>
                        <li><strong>方法：</strong>参究"我是谁"——即摧毁"我"这个念头</li>
                        <li><strong>两条路：</strong>参究自我（智慧之道）或归伏上师（奉爱之道）</li>
                    </ul>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 "我是谁？"</a>
                        <a href="../concepts/atman.html" class="tag">🔮 真我</a>
                        <a href="../concepts/surrender.html" class="tag">🙏 归伏</a>
                        <a href="../concepts/samadhi.html" class="tag">🧘 三摩地</a>
                        <a href="../concepts/jnana.html" class="tag">📖 智慧</a>
                    </div>
                </div>
                </div>
'''

page3 = make_page(
    '本心十论 Upadesa Saram | 权威合集',
    '《本心十论》(Upadesa Saram) 是马哈希亲笔撰写的核心教义，以十节诗精炼阐述自我参究的精髓，是马哈希教法的纲要性文献。',
    '本心十论,Upadesa Saram',
    'collected-works-upadesa-saram',
    ch3_body,
    'collected-works-upadesa-manjari.html', '下一章', '上师言颂'
)
with open(os.path.join(BOOKS, 'collected-works-upadesa-saram.html'), 'w', encoding='utf-8') as f:
    f.write(page3)
print('OK collected-works-upadesa-saram.html')

# ============================================================
# 章节4: Upadesa Manjari (上师言颂)
# ============================================================
ch4_body = '''
                <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="collected-works.html">权威合集</a> /
                    <span>上师言颂</span>
                </nav>

                <header class="page-header">
                    <h1>上师言颂</h1>
                    <p class="subtitle">Upadesa Manjari (Spiritual Instruction) | Sri Ramana Maharshi 原著</p>
                </header>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📖 章节概要</h2>
                    <p><strong>《上师言颂》</strong>（Upadesa Manjari，意为"上师教言的花束"）是最早的弟子之一室利·纳塔南达记录的一天中马哈希与弟子们的对话，经马哈希本人认可后出版。</p>
                    <p>此书是马哈希不朽言教的精华汇编，涵盖上师的标志、弟子的素质、什么是真正的"上师加持"、如何通过上师的恩典觉醒等核心主题。</p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">💬 核心问答节选</h2>
                    <div class="quote-box">
                        <strong>1. 真正上师的标志是什么？</strong><br><br>
                        持续安住于真我，以平等心看待一切，无论何时何地都毫无动摇的勇气。
                    </div>
                    <div class="quote-box">
                        <strong>4. 如果上师就是自己的真我，为何若无上师的恩典，都无法证悟？</strong><br><br>
                        虽然在绝对真理中，上师的状态就是真我，但对因无明而成为个体灵魂的真我来说，若无上师的恩典，很难认识自己的真实本性。所有世俗的观念都会在真正的上师面前瓦解。
                    </div>
                    <div class="quote-box">
                        <strong>6. 如何说弟子通过恩典认识了自己的真实状态？</strong><br><br>
                        这就像大象在梦中看到狮子而惊醒。上师恩典的一瞥，就足以让弟子从无明的沉睡中觉醒，证悟真实知识。
                    </div>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">✨ 核心洞见</h2>
                    <ul>
                        <li><strong>上师的本质：</strong>上师是真我以人形显现，为唤醒弟子而慈悲施教</li>
                        <li><strong>恩典的运作：</strong>上师的恩典超越言语，通过"上师加持的一瞥"发生——足以让弟子从无明的沉睡中觉醒</li>
                        <li><strong>弟子的资格：</strong>强烈的解脱愿望，以及对世间一切喜乐的厌离</li>
                        <li><strong>"upadesa"的含义：</strong>"指向近处"——上师让那被认为遥远的梵变得近在眼前</li>
                    </ul>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📜 原文节选（英译）</h2>
                    <p style="font-style:italic; color:var(--text-muted);">
                        "The word 'upadesa' means, 'near the place or seat' (upa - near, desa - place or seat). The Guru who is the embodiment of that which is indicated by the terms sat, chit, and ananda (existence, consciousness and bliss), establishes the disciple in his own real nature without differentiation."<br><br>
                        "Upadesa also means showing a distant object quite near. It is brought home to the disciple that Brahman which he believes to be distant and different from himself is near and not different from himself."<br><br>
                        — Upadesa Manjari, Chapter I
                    </p>
                </div>

                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/guru.html" class="tag">🙏 上师</a>
                        <a href="../concepts/grace.html" class="tag">✨ 恩典</a>
                        <a href="../concepts/surrender.html" class="tag">🙏 归伏</a>
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 "我是谁？"</a>
                        <a href="../concepts/awareness.html" class="tag">👁️ 觉知</a>
                    </div>
                </div>
                </div>
'''

page4 = make_page(
    '上师言颂 Upadesa Manjari | 权威合集',
    '《上师言颂》(Upadesa Manjari) 记录马哈希与弟子对话精华，涵盖上师恩典、自我参究、归伏等核心主题。',
    '上师言颂,Upadesa Manjari',
    'collected-works-upadesa-manjari',
    ch4_body,
    'collected-works.html', '返回全书', '权威合集'
)
with open(os.path.join(BOOKS, 'collected-works-upadesa-manjari.html'), 'w', encoding='utf-8') as f:
    f.write(page4)
print('OK collected-works-upadesa-manjari.html')

print('\nAll 4 chapter pages created!')
