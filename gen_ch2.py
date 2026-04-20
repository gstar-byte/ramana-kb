#!/usr/bin/env python3
"""gen_ch2.py - 大瑜伽第2章"""
BASE = r"c:/Users/willp/Desktop/2026年4月/kb01"
OUT = f"{BASE}/pages/books"
TPL = open(f"{OUT}/be-as-you-are-ch1.html", encoding='utf-8').read()

ch_nav = '''<a href="maha-yoga-ch1.html" class="sidebar-item">📖 第一章：阿鲁那佳拉的圣者</a>
                    <a href="maha-yoga-ch2.html" class="sidebar-item active">📖 第二章：我们幸福吗？</a>
                    <a href="maha-yoga-ch3.html" class="sidebar-item">📖 第三章：无明</a>
                    <a href="maha-yoga-ch4.html" class="sidebar-item">📖 第四章：哲学与证据</a>
                    <a href="maha-yoga-ch5.html" class="sidebar-item">📖 第五章：世界</a>'''

body = """
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="maha-yoga.html">大瑜伽</a> /
                    <span>第二章：我们幸福吗？</span>
                </nav>

                <header class="page-header">
                    <h1>第二章：我们幸福吗？</h1>
                    <p class="subtitle">Are We Happy? | 大瑜伽</p>
                </header>

                <div class="card">
                    <h2>📋 章节概要</h2>
                    <p>本章从一个最基本的问题开始：我们幸福吗？我们穷尽一生追求幸福，以为它藏在世界的某个角落——更多的金钱、更大的房子、更完美的关系。但 Sri K. Lakshmana Sarma 在本书中追问：这些追求真的让我们幸福了吗？</p>
                    <p>作者指出，大多数人从未停下来真正思考这个问题。我们被欲望推着往前走，从一次失望走向另一次希望，却从不追问：为什么幸福总是躲着我们？</p>
                    <p>更深层的洞见是：快乐（Happiness）与快感（Pleasure）是两件完全不同的事。我们以为快感就是幸福的质地——如果我们能持续地提供快感，就能保证幸福。但快感的天性就是无常的——它依赖外在条件，而外在条件永远不稳定。</p>
                </div>

                <div class="quote-box">
                    <p>"快乐与幸福是两件完全不同的事。快乐只是我们内在自然幸福的释放，被误认为来自外在事物。如同啃骨头的狗以为是骨头让它尝到血味，实际上那是它自己的血。"</p>
                    <cite>— Sri K. Lakshmana Sarma, 大瑜伽 第2章</cite>
                </div>

                <div class="card">
                    <h2>💡 核心教导</h2>
                    <p>作者引用阿鲁那佳拉圣者的话：快乐其实并非来自外在事物。如果快乐真的来自事物，那么拥有更多事物的人应该更快乐，一无所有的人应该彻底痛苦。但事实并非如此——富人不一定快乐，穷人也不一定痛苦；而在酣畅无梦的睡眠中，我们所有人都是幸福的。</p>
                    <p>这揭示了一个惊人的真相：真正的幸福属于我们内在的本性。当我们放下对事物的渴望与对恐惧的执取时，我们就会体验到它。而渴望与恐惧正是幸福的两大敌人。</p>
                    <p>欲望告诉我们："得到这个，你就会幸福。"我们深信不疑地去追求。但欲望如同无底的深渊，永远填不满。得到之后，它立刻发现新的目标，我们继续追逐。欲望欺骗我们一辈子。渴望无尽，恐惧亦无尽。</p>
                </div>

                <div class="card">
                    <h2>🔑 核心洞见</h2>
                    <ul style="margin:1rem 0 1rem 1.5rem;line-height:1.8;">
                        <li><strong>幸福与快感截然不同</strong>：快感依赖外在条件，天性无常；幸福是我们内在本性的自然状态，无关外在条件</li>
                        <li><strong>渴望与恐惧是幸福的两大敌人</strong>：只要我们仍受制于这两者，就永远无法真正幸福</li>
                        <li><strong>睡眠是幸福的无声证明</strong>：无梦的酣睡中我们最幸福，说明幸福就在我们之内，不需要任何外在条件</li>
                        <li><strong>欲望如同无底深渊</strong>：它许诺幸福，却永远无法兑现，每得到一样东西，就生出新的欲望</li>
                        <li><strong>真正的幸福是永恒的</strong>：常在、新鲜、纯粹，不受时空或条件影响——只有真我的觉醒才能触及</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/satchidananda.html" class="tag">💎 存在-意识-喜悦</a>
                        <a href="../concepts/self.html" class="tag">🔮 自我</a>
                        <a href="../concepts/desire.html" class="tag">🔥 欲望</a>
                        <a href="../concepts/fear.html" class="tag">😨 恐惧</a>
                        <a href="../concepts/pleasure.html" class="tag">💫 快乐</a>
                    </div>
                </div>

                <div class="page-nav">
                    <a href="maha-yoga-ch1.html"><span class="nav-label">← 上一章</span><span class="nav-title">第一章</span></a>
                    <a href="maha-yoga.html"><span class="nav-label">返回书籍</span><span class="nav-title">大瑜伽全书</span></a>
                    <a href="maha-yoga-ch3.html"><span class="nav-label">下一章 →</span><span class="nav-title">第三章</span></a>
                </div>
"""

html = (TPL
    .replace('走向静默，如你本来 第一章：我是谁？自我参究精读修行智慧详解指南完整 | 拉玛那马哈希知识库', '第二章：我们幸福吗？ | 大瑜伽修行智慧 | 拉玛那马哈希知识库')
    .replace('走向静默，如你本来第1章详细内容和核心要义，包含原文摘要、关键段落解读和相关概念的交叉引用。走向静默，如你本来为拉玛那马哈希教示体系中的重要著作。本页面提供完整的章节内容与修行要点。', '我们幸福吗？ — 大瑜伽第2章。追问人类存在的核心问题：幸福究竟来自何方？通过对欲望、恐惧与快乐的深刻分析，揭示外在世界无法给予真正的幸福，唯有回归内在真我。')
    .replace('https://ramanamaharshi.space/books/be-as-you-are-ch1', 'https://ramanamaharshi.space/books/maha-yoga-ch2')
    .replace('data-chapter-mode="true"', 'data-chapter-mode="true"')
    .replace('📖 走向静默，如你本来', '📖 大瑜伽')
    .replace('<a href="be-as-you-are-ch1.html" class="sidebar-item active">📖 第一章：导论</a>\n                    <a href="be-as-you-are-ch2.html" class="sidebar-item">📖 第二章：真我</a>\n                    <a href="be-as-you-are-ch3.html" class="sidebar-item">📖 第三章：心智</a>\n                    <a href="be-as-you-are-ch4.html" class="sidebar-item">📖 第四章：静默</a>\n                    <a href="be-as-you-are-ch5.html" class="sidebar-item">📖 第五章：自我了悟</a>\n                    <a href="be-as-you-are-ch6.html" class="sidebar-item">📖 第六章：臣服</a>\n                    <a href="be-as-you-are-ch7.html" class="sidebar-item">📖 第七章：恩典</a>\n                    <a href="be-as-you-are-ch8.html" class="sidebar-item">📖 第八章：修行</a>\n                    <a href="be-as-you-are-ch9.html" class="sidebar-item">📖 第九章：解脱</a>', ch_nav)
    .replace('📖 第一章：我是谁？ - 走向静默，如你本来', '📖 第二章：我们幸福吗？ - 大瑜伽')
    .replace('<a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>', '<a href="index.html" class="sidebar-item">📚 书籍总览</a>')
)

import re
m = re.search(r'(<div class="card">.*?)(\s*<div class="page-nav">)', TPL, re.DOTALL)
if m:
    html = html.replace(m.group(0), body + '\n                <div class="page-nav">', 1)

with open(f"{OUT}/maha-yoga-ch2.html", 'w', encoding='utf-8') as f:
    f.write(html)
print("Done: maha-yoga-ch2.html")
