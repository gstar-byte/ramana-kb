#!/usr/bin/env python3
"""gen_maha_yoga_ch1.py - 生成大瑜伽第1章"""
BASE = r"c:/Users/willp/Desktop/2026年4月/kb01"
OUT = f"{BASE}/pages/books"
TPL = open(f"{OUT}/be-as-you-are-ch1.html", encoding='utf-8').read()

ch_nav = '''<a href="maha-yoga-ch1.html" class="sidebar-item active">📖 第一章：阿鲁那佳拉的圣者</a>
                    <a href="maha-yoga-ch2.html" class="sidebar-item">📖 第二章：我们幸福吗？</a>
                    <a href="maha-yoga-ch3.html" class="sidebar-item">📖 第三章：无明</a>
                    <a href="maha-yoga-ch4.html" class="sidebar-item">📖 第四章：哲学与证据</a>
                    <a href="maha-yoga-ch5.html" class="sidebar-item">📖 第五章：世界</a>'''

prev_nav = '<span></span>'
next_nav = '<a href="maha-yoga-ch2.html"><span class="nav-label">下一章 →</span><span class="nav-title">第二章</span></a>'

body = """
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="maha-yoga.html">大瑜伽</a> /
                    <span>第一章：阿鲁那佳拉的圣者</span>
                </nav>

                <header class="page-header">
                    <h1>第一章：阿鲁那佳拉的圣者</h1>
                    <p class="subtitle">The Sage of Arunachala | 大瑜伽</p>
                </header>

                <div class="card">
                    <h2>📋 章节概要</h2>
                    <p>本章是全书的开篇，以印度古籍《奥义书》的智慧开篇，阐明了一个核心真理：真正的自由只能来自对"真实自我"的直接了悟，而非书本知识。</p>
                    <p>作者 Sri K. Lakshmana Sarma 是马哈希的弟子，详细讲述了马哈希的生平——这位出生在Tiruchuzhi村庄的少年，十六岁时经历了深刻的死亡觉醒，最终徒步走向阿鲁那佳拉圣山，再未离开。</p>
                    <p>作者区分了两类觉悟者：有使命的天生圣者（如马哈希）和需要漫长修行的普通人。前者从出生就超越世间欲望，较早获得解脱；而后者需经历持续的、有方向的修行努力。马哈希正是前者的典范——他无需努力，真我参究自然发生。</p>
                </div>

                <div class="quote-box">
                    <p>"真理就在我们自身之中——我们真正的自我的实相知识，它能带来真正的自由。寻求自由的人，必须恭敬地向那已得自由的人请教。"</p>
                    <cite>— Sri K. Lakshmana Sarma, 大瑜伽 第1章</cite>
                </div>

                <div class="card">
                    <h2>💡 核心教导</h2>
                    <p>本章的核心洞见在于揭示马哈希作为"天生圣者"的非凡品质。他不同于普通的宗教导师，不是通过学习或苦修获得觉醒，而是自性流露。他的证悟是"无为之悟"——不是通过努力达到某个境界，而是安住于本来如是。</p>
                    <p>作者借用Sri Ramakrishna Paramahamsa的教导，区分了圣者（Soul）与圣哲（Sage）的层次。圣哲（梵）为"已熟透之果"，代表真正的圆满。Sri Ramakrishna说："你们要完全，正如你们的天父是完全的"——这里指的正是圣哲的境界，而非仅仅圣者的境界。</p>
                    <p>书中描述了马哈希少年时期对死亡的觉醒。十六岁那年，他经历了一次深刻的死亡恐惧，但这恐惧促使他向内参究，直到他发现："死亡之后，我难道也会死吗？"正是对这个问题的参究，令他彻底觉醒，踏上前往阿鲁那佳拉的旅程。</p>
                </div>

                <div class="card">
                    <h2>🔑 核心洞见</h2>
                    <ul style="margin:1rem 0 1rem 1.5rem;line-height:1.8;">
                        <li><strong>马哈希是天生圣者</strong>：从出生就超越世间欲望，无需努力便自然达到解脱状态，是"已熟之果"</li>
                        <li><strong>少年觉醒发生于十六岁</strong>：死亡恐惧促使他向内参究，发现"我"的存在本质，从而彻底觉醒</li>
                        <li><strong>真我参究无需求助书本</strong>：活生生的上师的静默比一辈子的书本研读更能让我们接近真相</li>
                        <li><strong>真正的教育是内在的</strong>：少年马哈希对世间学业漠不关心，因为他的灵魂早已熟透，只等待觉醒</li>
                        <li><strong>圣哲之境超越一切</strong>：圣者（Soul）与圣哲（Sage）的区别，如同花朵与果实——圣哲是圆满的实现</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 自我参究</a>
                        <a href="../concepts/sage.html" class="tag">🧘 圣哲</a>
                        <a href="../concepts/arunachala.html" class="tag">⛰️ 阿鲁那佳拉</a>
                        <a href="../concepts/samadhi.html" class="tag">🧘 三摩地</a>
                        <a href="../concepts/jnana.html" class="tag">🛤️ 智慧瑜伽</a>
                    </div>
                </div>

                <div class="page-nav">
                    """ + prev_nav + """
                    <a href="maha-yoga.html"><span class="nav-label">返回书籍</span><span class="nav-title">大瑜伽全书</span></a>
                    """ + next_nav + """
                </div>
"""

html = (TPL
    .replace('走向静默，如你本来 第一章：我是谁？自我参究精读修行智慧详解指南完整 | 拉玛那马哈希知识库', '第一章：阿鲁那佳拉的圣者 | 大瑜伽修行智慧 | 拉玛那马哈希知识库')
    .replace('走向静默，如你本来第1章详细内容和核心要义，包含原文摘要、关键段落解读和相关概念的交叉引用。走向静默，如你本来为拉玛那马哈希教示体系中的重要著作。本页面提供完整的章节内容与修行要点。', '阿鲁那佳拉的圣者 — 大瑜伽第1章。Sri K. Lakshmana Sarma讲述马哈希的生平传记：他的出身、少年觉醒、阿鲁那佳拉山之旅，以及他如何以无言之教照亮了千万弟子的心灵。')
    .replace('https://ramanamaharshi.space/books/be-as-you-are-ch1', 'https://ramanamaharshi.space/books/maha-yoga-ch1')
    .replace('data-chapter-mode="true"', 'data-chapter-mode="true"')
    .replace('📖 走向静默，如你本来', '📖 大瑜伽')
    .replace('<a href="be-as-you-are-ch1.html" class="sidebar-item active">📖 第一章：导论</a>\n                    <a href="be-as-you-are-ch2.html" class="sidebar-item">📖 第二章：真我</a>\n                    <a href="be-as-you-are-ch3.html" class="sidebar-item">📖 第三章：心智</a>\n                    <a href="be-as-you-are-ch4.html" class="sidebar-item">📖 第四章：静默</a>\n                    <a href="be-as-you-are-ch5.html" class="sidebar-item">📖 第五章：自我了悟</a>\n                    <a href="be-as-you-are-ch6.html" class="sidebar-item">📖 第六章：臣服</a>\n                    <a href="be-as-you-are-ch7.html" class="sidebar-item">📖 第七章：恩典</a>\n                    <a href="be-as-you-are-ch8.html" class="sidebar-item">📖 第八章：修行</a>\n                    <a href="be-as-you-are-ch9.html" class="sidebar-item">📖 第九章：解脱</a>', ch_nav)
    .replace('📖 第一章：我是谁？ - 走向静默，如你本来', '📖 第一章：阿鲁那佳拉的圣者 - 大瑜伽')
    .replace('<a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>', '<a href="index.html" class="sidebar-item">📚 书籍总览</a>')
)

# 替换正文内容
import re
# 找到 <div class="card"> 开始到 page-nav 结束的部分并替换
m = re.search(r'(<div class="card">.*?)(\s*<div class="page-nav">)', TPL, re.DOTALL)
if m:
    html = html.replace(m.group(0), body + '\n                <div class="page-nav">', 1)

out_path = f"{OUT}/maha-yoga-ch1.html"
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"生成: {out_path}")
