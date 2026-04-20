#!/usr/bin/env python3
"""gen_ch45.py - 大瑜伽第4章和第5章"""
BASE = r"c:/Users/willp/Desktop/2026年4月/kb01"
OUT = f"{BASE}/pages/books"
TPL = open(f"{OUT}/be-as-you-are-ch1.html", encoding='utf-8').read()

# ====== 第4章 ======
ch4_nav = '''<a href="maha-yoga-ch1.html" class="sidebar-item">📖 第一章：阿鲁那佳拉的圣者</a>
                    <a href="maha-yoga-ch2.html" class="sidebar-item">📖 第二章：我们幸福吗？</a>
                    <a href="maha-yoga-ch3.html" class="sidebar-item">📖 第三章：无明</a>
                    <a href="maha-yoga-ch4.html" class="sidebar-item active">📖 第四章：哲学与证据</a>
                    <a href="maha-yoga-ch5.html" class="sidebar-item">📖 第五章：世界</a>'''

body4 = """
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="maha-yoga.html">大瑜伽</a> /
                    <span>第四章：哲学与证据</span>
                </nav>

                <header class="page-header">
                    <h1>第四章：哲学与证据</h1>
                    <p class="subtitle">Philosophy and Evidence | 大瑜伽</p>
                </header>

                <div class="card">
                    <h2>📋 章节概要</h2>
                    <p>本章探讨了如何正确地做"哲学"——即在真正参究自我之前，对我们的观念进行审查和修正。作者指出，大多数哲学之所以失败，是因为它们使用 了错误的证据——即普通人的共同经验，而这种经验本身就是无明的产物。</p>
                    <p>可靠的证据必须来自已经超越无明的觉悟者——即圣哲。只有在圣哲经验的基础上，我们才能建立起真正有助于参究的哲学。而普通人、甚至瑜伽士和圣者的经验都不可靠，因为他们在某种程度上仍受无明的制约。</p>
                    <p>作者进一步区分了三类修行者的层次：瑜伽士（Yogis）、圣者（Soul）和圣哲（Sage）。瑜伽士将心智当作自我；圣者崇拜人格神；而圣哲已彻底超越无明，证得了真我。三者中唯有圣哲的证言是始终一致、不相互矛盾的。</p>
                </div>

                <div class="quote-box">
                    <p>"可靠的证据不是无知者的经验，而是已完全超越无明的圣哲的经验。只有在他们的经验基础上，我们才能建立起有助于参究的哲学。"</p>
                    <cite>— Sri K. Lakshmana Sarma, 大瑜伽 第4章</cite>
                </div>

                <div class="card">
                    <h2>💡 核心教导</h2>
                    <p>哲学应当成为参究的准备，而不是目的本身。正确的哲学是对我们关于世界、灵魂和上帝的所有现有观念进行公正的批评。那些试图确证这些观念的哲学，只会加深无明，有害于参究。</p>
                    <p>真正的哲学必须从承认无明的存在开始。这意味着我们所有的观念都值得怀疑。瑜伽士将高级心智当作自我，声称它是不死的灵魂；圣者相信人格化的上帝；而圣哲则超越了一切二元对立，证得绝对的一真我。</p>
                    <p>作者借Sri Sankara的话指出：非圣哲所获得的真理视角，会因为心智的干扰而失真。只有圣哲才能如实地宣说真理——因为在他们的境界中，心智已经消融于真我之中。</p>
                </div>

                <div class="card">
                    <h2>🔑 核心洞见</h2>
                    <ul style="margin:1rem 0 1rem 1.5rem;line-height:1.8;">
                        <li><strong>正确的证据来自圣哲</strong>：只有已超越无明的觉悟者的经验，才能作为可靠的哲学基础</li>
                        <li><strong>普通人的共同经验是无明的产物</strong>：以此为基础的哲学只会确证无明，阻碍解脱</li>
                        <li><strong>瑜伽士、圣者、圣哲三层次</strong>：瑜伽士将心智当自我；圣者崇拜人格神；唯有圣哲超越一切二元</li>
                        <li><strong>瑜伽士的目标并非最高</strong>：他们追求的是在无明境界内的荣耀状态，而非彻底的觉醒</li>
                        <li><strong>哲学只是手段而非目的</strong>：哲学是对观念的审查修正，真正的目标是参究真我</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/jnana.html" class="tag">🛤️ 智慧瑜伽</a>
                        <a href="../concepts/yoga.html" class="tag">🧘 瑜伽</a>
                        <a href="../concepts/sage.html" class="tag">🧘 圣哲</a>
                        <a href="../concepts/authority.html" class="tag">📜 权威</a>
                        <a href="../concepts/reason.html" class="tag">⚖️ 理性</a>
                    </div>
                </div>

                <div class="page-nav">
                    <a href="maha-yoga-ch3.html"><span class="nav-label">← 上一章</span><span class="nav-title">第三章</span></a>
                    <a href="maha-yoga.html"><span class="nav-label">返回书籍</span><span class="nav-title">大瑜伽全书</span></a>
                    <a href="maha-yoga-ch5.html"><span class="nav-label">下一章 →</span><span class="nav-title">第五章</span></a>
                </div>
"""

html4 = (TPL
    .replace('走向静默，如你本来 第一章：我是谁？自我参究精读修行智慧详解指南完整 | 拉玛那马哈希知识库', '第四章：哲学与证据 | 大瑜伽修行智慧 | 拉玛那马哈希知识库')
    .replace('走向静默，如你本来第1章详细内容和核心要义，包含原文摘要、关键段落解读和相关概念的交叉引用。走向静默，如你本来为拉玛那马哈希教示体系中的重要著作。本页面提供完整的章节内容与修行要点。', '哲学与证据 — 大瑜伽第4章。探讨正确哲学的角色：如何用圣哲的证言审查我们的观念，为自我参究做好准备。')
    .replace('https://ramanamaharshi.space/books/be-as-you-are-ch1', 'https://ramanamaharshi.space/books/maha-yoga-ch4')
    .replace('data-chapter-mode="true"', 'data-chapter-mode="true"')
    .replace('📖 走向静默，如你本来', '📖 大瑜伽')
    .replace('<a href="be-as-you-are-ch1.html" class="sidebar-item active">📖 第一章：导论</a>\n                    <a href="be-as-you-are-ch2.html" class="sidebar-item">📖 第二章：真我</a>\n                    <a href="be-as-you-are-ch3.html" class="sidebar-item">📖 第三章：心智</a>\n                    <a href="be-as-you-are-ch4.html" class="sidebar-item">📖 第四章：静默</a>\n                    <a href="be-as-you-are-ch5.html" class="sidebar-item">📖 第五章：自我了悟</a>\n                    <a href="be-as-you-are-ch6.html" class="sidebar-item">📖 第六章：臣服</a>\n                    <a href="be-as-you-are-ch7.html" class="sidebar-item">📖 第七章：恩典</a>\n                    <a href="be-as-you-are-ch8.html" class="sidebar-item">📖 第八章：修行</a>\n                    <a href="be-as-you-are-ch9.html" class="sidebar-item">📖 第九章：解脱</a>', ch4_nav)
    .replace('📖 第一章：我是谁？ - 走向静默，如你本来', '📖 第四章：哲学与证据 - 大瑜伽')
    .replace('<a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>', '<a href="index.html" class="sidebar-item">📚 书籍总览</a>')
)

import re
m = re.search(r'(<div class="card">.*?)(\s*<div class="page-nav">)', TPL, re.DOTALL)
if m:
    html4 = html4.replace(m.group(0), body4 + '\n                <div class="page-nav">', 1)

with open(f"{OUT}/maha-yoga-ch4.html", 'w', encoding='utf-8') as f:
    f.write(html4)
print("Done: maha-yoga-ch4.html")

# ====== 第5章 ======
ch5_nav = '''<a href="maha-yoga-ch1.html" class="sidebar-item">📖 第一章：阿鲁那佳拉的圣者</a>
                    <a href="maha-yoga-ch2.html" class="sidebar-item">📖 第二章：我们幸福吗？</a>
                    <a href="maha-yoga-ch3.html" class="sidebar-item">📖 第三章：无明</a>
                    <a href="maha-yoga-ch4.html" class="sidebar-item">📖 第四章：哲学与证据</a>
                    <a href="maha-yoga-ch5.html" class="sidebar-item active">📖 第五章：世界</a>'''

body5 = """
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="index.html">书籍</a> /
                    <a href="maha-yoga.html">大瑜伽</a> /
                    <span>第五章：世界</span>
                </nav>

                <header class="page-header">
                    <h1>第五章：世界</h1>
                    <p class="subtitle">The World | 大瑜伽</p>
                </header>

                <div class="card">
                    <h2>📋 章节概要</h2>
                    <p>本章深入探讨了"世界"这一概念的本质。作者引用阿鲁那佳拉圣者的教导：世界与真我之间的关系，如同绳子与蛇的关系——当我们在黑暗中把绳子误认为蛇时，蛇就遮蔽了绳子；同样，世界遮蔽了真我。</p>
                    <p>圣者说："如果不是因为我们相信世界是真实的，要得到真我的启示就很容易了。"最神奇的是——我们本身就是真我，却还在努力要与它合一。我们不是要成为真我——我们本就是真我。</p>
                    <p>作者进一步阐明：世界既真实又不真实。从一方面说，世界是真实的，因为呈现为世界的就是那唯一的实在——真我本身；另一方面，世界是不真实的，因为作为"世界"它只是一种幻相（摩耶），离开实在本身便无存在可言。这不是自相矛盾，而是实在的双重面向。</p>
                </div>

                <div class="quote-box">
                    <p>"最神奇的是——我们本身就是真我，却还在努力要与它合一。我们不是要成为真我——我们本就是真我。那将在某一天被认识到的东西，此刻就已作为真相存在着。"</p>
                    <cite>— Sri K. Lakshmana Sarma, 大瑜伽 第5章</cite>
                </div>

                <div class="card">
                    <h2>💡 核心教导</h2>
                    <p>马哈希指出：我们都热爱无我状态（Egoless State），只是我们自己不知道这一点。我们对无梦睡眠的热爱正是证明——在无梦睡眠中，我们没有"我"的执着，我们是幸福的。圣者说：热爱睡眠的人不可能说不热爱无我状态。</p>
                    <p>当我们把世界当作真实的，我们就必须把自我安放在世界之中——只能是身体或心智。而这正是无明的根源：真我不是身体，不是心智，而是超越两者的绝对存在。不放弃"世界是真实的"这一信念，我们永远无法了悟真我。</p>
                    <p>心的自然流向是朝向世界，而非真我。即使我们成功地将心从世界转向真我，它也会挣脱束缚，重新游移到世界。为什么会这样？圣哲说：是因为我们相信世界是真实的。真正的事物有无可置疑的进入心灵的权利。</p>
                </div>

                <div class="card">
                    <h2>🔑 核心洞见</h2>
                    <ul style="margin:1rem 0 1rem 1.5rem;line-height:1.8;">
                        <li><strong>世界如同绳子上的蛇</strong>：当绳子被误认为蛇时，蛇遮蔽了绳子；同样，世界遮蔽了真我</li>
                        <li><strong>我们本就已是真我</strong>：无需成为，只需认识到；最神奇的是我们本就是，却还在努力要与它合一</li>
                        <li><strong>无梦睡眠是无我状态的世俗证明</strong>：我们热爱睡眠，是因为它在世间最近似无我状态</li>
                        <li><strong>相信世界真实是念头入侵的根源</strong>：不放弃这个信念，心智就无法持续安住于真我</li>
                        <li><strong>世界既真实又不真实</strong>：它是真我的显现（故真实），但作为"世界"它只是幻相（故不真实）</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>🔗 相关概念</h2>
                    <div class="concept-tags">
                        <a href="../concepts/world.html" class="tag">🌍 世界</a>
                        <a href="../concepts/maya.html" class="tag">💫 摩耶/Maya</a>
                        <a href="../concepts/reality.html" class="tag">💎 实在</a>
                        <a href="../concepts/self-enquiry.html" class="tag">🔮 自我参究</a>
                        <a href="../concepts/satchidananda.html" class="tag">💎 存在-意识-喜悦</a>
                    </div>
                </div>

                <div class="page-nav">
                    <a href="maha-yoga-ch4.html"><span class="nav-label">← 上一章</span><span class="nav-title">第四章</span></a>
                    <a href="maha-yoga.html"><span class="nav-label">返回书籍</span><span class="nav-title">大瑜伽全书</span></a>
                    <span></span>
                </div>
"""

html5 = (TPL
    .replace('走向静默，如你本来 第一章：我是谁？自我参究精读修行智慧详解指南完整 | 拉玛那马哈希知识库', '第五章：世界 | 大瑜伽修行智慧 | 拉玛那马哈希知识库')
    .replace('走向静默，如你本来第1章详细内容和核心要义，包含原文摘要、关键段落解读和相关概念的交叉引用。走向静默，如你本来为拉玛那马哈希教示体系中的重要著作。本页面提供完整的章节内容与修行要点。', '世界 — 大瑜伽第5章。探讨世界与真我的关系：世界如同绳子上的蛇遮蔽了真我，唯有认识到世界的不真实性，真我才能显现。我们本就已是真我，无需再成为。')
    .replace('https://ramanamaharshi.space/books/be-as-you-are-ch1', 'https://ramanamaharshi.space/books/maha-yoga-ch5')
    .replace('data-chapter-mode="true"', 'data-chapter-mode="true"')
    .replace('📖 走向静默，如你本来', '📖 大瑜伽')
    .replace('<a href="be-as-you-are-ch1.html" class="sidebar-item active">📖 第一章：导论</a>\n                    <a href="be-as-you-are-ch2.html" class="sidebar-item">📖 第二章：真我</a>\n                    <a href="be-as-you-are-ch3.html" class="sidebar-item">📖 第三章：心智</a>\n                    <a href="be-as-you-are-ch4.html" class="sidebar-item">📖 第四章：静默</a>\n                    <a href="be-as-you-are-ch5.html" class="sidebar-item">📖 第五章：自我了悟</a>\n                    <a href="be-as-you-are-ch6.html" class="sidebar-item">📖 第六章：臣服</a>\n                    <a href="be-as-you-are-ch7.html" class="sidebar-item">📖 第七章：恩典</a>\n                    <a href="be-as-you-are-ch8.html" class="sidebar-item">📖 第八章：修行</a>\n                    <a href="be-as-you-are-ch9.html" class="sidebar-item">📖 第九章：解脱</a>', ch5_nav)
    .replace('📖 第一章：我是谁？ - 走向静默，如你本来', '📖 第五章：世界 - 大瑜伽')
    .replace('<a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>', '<a href="index.html" class="sidebar-item">📚 书籍总览</a>')
)

m = re.search(r'(<div class="card">.*?)(\s*<div class="page-nav">)', TPL, re.DOTALL)
if m:
    html5 = html5.replace(m.group(0), body5 + '\n                <div class="page-nav">', 1)

with open(f"{OUT}/maha-yoga-ch5.html", 'w', encoding='utf-8') as f:
    f.write(html5)
print("Done: maha-yoga-ch5.html")
