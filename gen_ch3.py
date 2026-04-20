#!/usr/bin/env python3
"""gen_ch3.py - 大瑜伽第3章"""
BASE = r"c:/Users/willp/Desktop/2026年4月/kb01"
OUT = f"{BASE}/pages/books"
TPL = open(f"{OUT}/be-as-you-are-ch1.html", encoding='utf-8').read()

ch_nav = '''<a href="maha-yoga-ch1.html" class="sidebar-item">📖 第一章：阿鲁那佳拉的圣者</a>
                    <a href="maha-yoga-ch2.html" class="sidebar-item">📖 第二章：我们幸福吗？</a>
                    <a href="maha-yoga-ch3.html" class="sidebar-item active">📖 第三章：无明</a>
                    <a href="maha-yoga-ch4.html" class="sidebar-item">📖 第四章：哲学与证据</a>
                    <a href="maha-yoga-ch5.html" class="sidebar-item">📖 第五章：世界</a>'''

body = """
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="maha-yoga.html">大瑜伽</a> /
                    <span>第三章：无明</span>
                </nav>

                <header class="page-header">
                    <h1>第三章：无明</h1>
                    <p class="subtitle">Ignorance | 大瑜伽</p>
                </header>

                <div class="card">
                    <h2>📋 章节概要</h2>
                    <p>如果幸福就在我们之内，我们为什么无法触及它？本章给出了答案：是无明（Avidya）遮蔽了真正的幸福。无明不是简单的"不知道某件事"，而是一种根本的认知扭曲——我们把自己认同为某种非我的东西。</p>
                    <p>佛陀说："你们只是自己受苦，没有人强迫你们。"阿鲁那佳拉的圣者给出了同样的教导："世界本身没有错，错的是我们自己——因为我们的思维方式错了。我们需要做的是追溯内心最深处那个根本的错误，并将它拔除。"</p>
                    <p>作者强调：只有找到并拔除这个根本错误，才是彻底的治疗。所有其他方法——宗教仪式、祈祷、算命——都只是权宜之计，它们的最大价值仅限于把我们引向正确的治疗方法。</p>
                </div>

                <div class="quote-box">
                    <p>"找到并拔除我们根本的错误，这是唯一彻底的治疗。所有其他补救都只是姑息之剂；充其量只能说，它们以各自的方式帮助我们走上正确的治疗之路。"</p>
                    <cite>— Sri K. Lakshmana Sarma, 大瑜伽 第3章</cite>
                </div>

                <div class="card">
                    <h2>💡 核心教导</h2>
                    <p>本章深入探讨了信仰与怀疑的关系。一个真诚而认真的怀疑者，可能比一个偏执的信徒更接近真理——因为前者愿意追寻，而后者被信仰封闭了道路。那些把宗教信条当作绝对真理本身的人，不会进一步追问，从而错失真正了悟的机会。</p>
                    <p>真理的追寻者必须准备放下自己的信仰，不被任何教条所束缚。没有书本知识、心态开放的弟子，往往比满脑子教条的博学之人更处于有利位置。</p>
                    <p>真正的无知不是不知道某些事实，而是不知道自己是谁。"我们不知道自己"这一点，我们完全知道。我们以为自己在世间混得很好——但所有这些知识都是向外寻求的，从不向内。</p>
                </div>

                <div class="card">
                    <h2>🔑 核心洞见</h2>
                    <ul style="margin:1rem 0 1rem 1.5rem;line-height:1.8;">
                        <li><strong>一切苦难的原因在于自身</strong>：不是世界错了，而是我们"我"的根本认知错了——把非我当成了自我</li>
                        <li><strong>拔除根本错误是唯一彻底的治疗</strong>：所有宗教仪式、祈祷都只是姑息之剂，唯有认出无明才能解脱</li>
                        <li><strong>真诚的怀疑者优于偏执的信徒</strong>：后者把信仰当作真理本身，拒绝进一步的探寻</li>
                        <li><strong>真正的无知是不知自我</strong>：不是不知道某些知识，而是不知道自己是谁，把身体或心智当成了自我</li>
                        <li><strong>开悟者从不互相矛盾</strong>：所有圣哲的教导一致，因为他们已超越无明；其他修行者则众说纷纭</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/avidya.html" class="tag">🌑 无明/Avidya</a>
                        <a href="../concepts/knowledge.html" class="tag">📖 知识与智慧</a>
                        <a href="../concepts/faith.html" class="tag">🙏 信仰</a>
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 自我参究</a>
                        <a href="../concepts/truth.html" class="tag">💎 真理</a>
                    </div>
                </div>

                <div class="page-nav">
                    <a href="maha-yoga-ch2.html"><span class="nav-label">← 上一章</span><span class="nav-title">第二章</span></a>
                    <a href="maha-yoga.html"><span class="nav-label">返回书籍</span><span class="nav-title">大瑜伽全书</span></a>
                    <a href="maha-yoga-ch4.html"><span class="nav-label">下一章 →</span><span class="nav-title">第四章</span></a>
                </div>
"""

html = (TPL
    .replace('走向静默，如你本来 第一章：我是谁？自我参究精读修行智慧详解指南完整 | 拉玛那马哈希知识库', '第三章：无明 | 大瑜伽修行智慧 | 拉玛那马哈希知识库')
    .replace('走向静默，如你本来第1章详细内容和核心要义，包含原文摘要、关键段落解读和相关概念的交叉引用。走向静默，如你本来为拉玛那马哈希教示体系中的重要著作。本页面提供完整的章节内容与修行要点。', '无明 — 大瑜伽第3章。阐述苦恼的真正根源：不在外界，而在自身。唯有认出并拔除内心的根本错误——将非我当作自我——才能获得根本的治疗。')
    .replace('https://ramanamaharshi.space/books/be-as-you-are-ch1', 'https://ramanamaharshi.space/books/maha-yoga-ch3')
    .replace('data-chapter-mode="true"', 'data-chapter-mode="true"')
    .replace('📖 走向静默，如你本来', '📖 大瑜伽')
    .replace('<a href="be-as-you-are-ch1.html" class="sidebar-item active">📖 第一章：导论</a>\n                    <a href="be-as-you-are-ch2.html" class="sidebar-item">📖 第二章：真我</a>\n                    <a href="be-as-you-are-ch3.html" class="sidebar-item">📖 第三章：心智</a>\n                    <a href="be-as-you-are-ch4.html" class="sidebar-item">📖 第四章：静默</a>\n                    <a href="be-as-you-are-ch5.html" class="sidebar-item">📖 第五章：自我了悟</a>\n                    <a href="be-as-you-are-ch6.html" class="sidebar-item">📖 第六章：臣服</a>\n                    <a href="be-as-you-are-ch7.html" class="sidebar-item">📖 第七章：恩典</a>\n                    <a href="be-as-you-are-ch8.html" class="sidebar-item">📖 第八章：修行</a>\n                    <a href="be-as-you-are-ch9.html" class="sidebar-item">📖 第九章：解脱</a>', ch_nav)
    .replace('📖 第一章：我是谁？ - 走向静默，如你本来', '📖 第三章：无明 - 大瑜伽')
    .replace('<a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>', '<a href="index.html" class="sidebar-item">📚 书籍总览</a>')
)

import re
m = re.search(r'(<div class="card">.*?)(\s*<div class="page-nav">)', TPL, re.DOTALL)
if m:
    html = html.replace(m.group(0), body + '\n                <div class="page-nav">', 1)

with open(f"{OUT}/maha-yoga-ch3.html", 'w', encoding='utf-8') as f:
    f.write(html)
print("Done: maha-yoga-ch3.html")
