#!/usr/bin/env python3
import os

concepts = [
    {
        "filename": "ahamkara.html",
        "title": "我慢 / Ahamkara",
        "icon": "💀",
        "subtitle": "自我执着 · 个体身份的根源",
        "description": "我慢（Ahamkara）是吠檀多哲学中意指'我执'或'自我意识'的核心术语。它是导致个体与真我分离的根源，也是一切痛苦和束缚的源头。",
        "keywords": "我慢, Ahamkara, 自我意识, 我执, 吠檀多, 拉玛那马哈希",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是我慢？</h2>
                            <p><strong>我慢（Ahamkara）</strong>源自梵语，由"aham"（我）和"kara"（造作）组成，意指"我之造作"。它是个体对自己身份的执着——认为自己是一个独立的实体，与宇宙分离。</p>
                        </section>

                        <div class="quote-box">
                            "我慢是心智制造的'我'。它是虚假的自我意识，认为自己是独立的实体。当参究'我是谁？'时，我慢就会瓦解，真我就会显现。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>我慢的本质</h2>
                        <p>我慢是内具（Antahkarana）的四个组成部分之一，与：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>末那（Manas）</strong> - 心意/思考的器官</li>
                            <li><strong>觉（Buddhi）</strong> - 智/分辨的能力</li>
                            <li><strong>心（Chitta）</strong> - 识/记忆的仓库</li>
                        </ul>
                        <p>我慢是将这一切误认为"我"的那一个。</p>

                        <div class="quote-box">
                            "我慢像一根线，串起了所有的业力和身份认同。剪断这根线，所有的束縛就会解脱。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>如何超越我慢？</h2>
                        <p>马哈希教导说，超越我慢的唯一方法是：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li>参究"我是谁？"</li>
                            <li>发现我慢背后的那个纯粹意识</li>
                            <li>安住于真我之中，不再认同身份</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="ego.html" class="tag">🧠 自我/Ego</a>
                            <a href="antahkarana.html" class="tag">🧩 内具/Antahkarana</a>
                            <a href="whoami.html" class="tag">🔍 "我是谁？"</a>
                            <a href="atman.html" class="tag">🔮 真我/Atman</a>
                            <a href="maya.html" class="tag">🎭 摩耶/Maya</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "antahkarana.html",
        "title": "内具 / Antahkarana",
        "icon": "🧩",
        "subtitle": "心意四身 · 内在感知的工具",
        "description": "内具（Antahkarana）是吠檀多哲学中意指内在心意器官复合体的核心术语，包括末那（Manas）、觉（Buddhi）、我慢（Ahamkara）和心（Chitta）。",
        "keywords": "内具, Antahkarana, 心意四身, 末那, 觉, 我慢, 心, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是内具？</h2>
                            <p><strong>内具（Antahkarana）</strong>意指"内在的工具"或"内在的器官"。它是由四个部分组成的心意复合体，负责所有的感知、思考、记忆和身份认同。</p>
                        </section>

                        <div class="quote-box">
                            "内具就像一面镜子。当它安静时，能映照出真我；当它波动时，只会映照出自己的妄想。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>内具的四个组成部分</h2>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>末那（Manas）</strong> - 思考、犹豫的心意</li>
                            <li><strong>觉（Buddhi）</strong> - 分辨、判断的智</li>
                            <li><strong>我慢（Ahamkara）</strong> - 自我执着的身份认同</li>
                            <li><strong>心（Chitta）</strong> - 记忆、潜意识的仓库</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>内具与真我的关系</h2>
                        <p>内具本身不是真我，但它是真我之光的反射：</p>
                        <div class="quote-box">
                            "内具就像月亮，它本身不发光，只是反射太阳的光。当你参究'我是谁？'时，你会发现不是内具在觉知，而是真我在觉知。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="mind.html" class="tag">🧠 心智/Citta</a>
                            <a href="ahamkara.html" class="tag">💀 我慢/Ahamkara</a>
                            <a href="mano.html" class="tag">💭 意/Mano</a>
                            <a href="buddhi.html" class="tag">🧠 觉/Buddhi</a>
                            <a href="chit.html" class="tag">✨ 意识/Chit</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "buddhi.html",
        "title": "觉 / Buddhi",
        "icon": "🧠",
        "subtitle": "分辨的智 · 内在的智慧",
        "description": "觉（Buddhi）是吠檀多哲学中意指"智"或"分辨能力"的核心术语，是内具（Antahkarana）的四个组成部分之一，负责判断和决策。",
        "keywords": "觉, Buddhi, 智, 分辨能力, 智慧, 内具, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是觉？</h2>
                            <p><strong>觉（Buddhi）</strong>是"智"或"分辨的智慧"。它是内具（Antahkarana）的最高功能——分辨真假、对错、真实与虚幻的能力。</p>
                        </section>

                        <div class="quote-box">
                            "觉是心智中最高的部分，也是最接近真我的。当觉转向内，它就变成了参究的工具。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>觉的两种面向</h2>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>向外的觉</strong> - 分辨世俗事务的智，带来知识但不是智慧</li>
                            <li><strong>向内的觉</strong> - 分辨真我的智慧，带来解脱</li>
                        </ul>

                        <div class="quote-box">
                            "知识来自头脑，智慧来自心。觉是心的智慧。"
                            <div class="source">—《对谈录》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>如何发展觉？</h2>
                        <p>马哈希教导：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li>持续参究"我是谁？"</li>
                            <li>不认同身份，安住于觉知</li>
                            <li>在静默中让觉自然显现</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="antahkarana.html" class="tag">🧩 内具/Antahkarana</a>
                            <a href="viveka.html" class="tag">🔎 抉择/Viveka</a>
                            <a href="jnana.html" class="tag">🛤️ 参究法/Jnana</a>
                            <a href="mind.html" class="tag">🧠 心智/Citta</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "asat.html",
        "title": "非存在 / Asat",
        "icon": "❌",
        "subtitle": "虚幻的显现 · 与真相对的非实",
        "description": '非存在（Asat）是吠檀多哲学中意指"非实"或"虚幻"的核心术语，与"存在（Sat）"相对，用来描述世界和个体身份的本质。',
        "keywords": "非存在, Asat, 虚幻, 非实, 摩耶, 吠檀多, 拉玛那马哈希",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是非存在？</h2>
                            <p><strong>非存在（Asat）</strong>意指"不是真实的"、"不是存在"。吠檀多用它来描述世界——不是说世界不存在，而是说它不是真实的、永恒的存在。</p>
                        </section>

                        <div class="quote-box">
                            "世界像一场梦。梦时你认为它是真的，醒后才知道它是假的。证悟真我就是从世界之梦中醒来。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>Asat 与 Sat</h2>
                        <p>存在（Sat）与非存在（Asat）的区别：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>存在（Sat）</strong> - 永恒不变、不受时间空间限制的真实</li>
                            <li><strong>非存在（Asat）</strong> - 生灭变化、依赖于觉知而显现的虚幻</li>
                        </ul>

                        <div class="quote-box">
                            "世界如绳上之蛇，它只是你的想象。当你看清绳子，蛇就消失。当你看清真我，世界就消失。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="satya.html" class="tag">💎 真理/Satya</a>
                            <a href="brahman.html" class="tag">🌀 梵/Brahman</a>
                            <a href="maya.html" class="tag">🎭 摩耶/Maya</a>
                            <a href="world.html" class="tag">🌍 世界/World</a>
                            <a href="satchidananda.html" class="tag">✨ 存在-意识-喜悦</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "anubhava.html",
        "title": "亲证 / Anubhava",
        "icon": "💫",
        "subtitle": "直接体验 · 超越文字的证悟",
        "description": "亲证（Anubhava）是吠檀多哲学中意指"直接体验"或"亲身体证"的核心术语，它是超越思维和文字的真实证悟，是修行的最终目标。",
        "keywords": "亲证, Anubhava, 直接体验, 证悟, 体验, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是亲证？</h2>
                            <p><strong>亲证（Anubhava）</strong>意指"亲身体证"、"直接体验"。它不是从书本或他人处学来的知识，而是自己亲身经历的真实。</p>
                        </section>

                        <div class="quote-box">
                            "知识是二手的，亲证是一手的。书本上的水不能解渴，只有你自己喝到的水才能解渴。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>亲证 vs 知识</h2>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>知识（Jnana）</strong> - 概念、理论、理解</li>
                            <li><strong>亲证（Anubhava）</strong> - 直接经验、体证</li>
                        </ul>

                        <div class="quote-box">
                            "学习非二元是准备工作，参究是过程，亲证是结果。"
                            <div class="source">—《对谈录》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>如何获得亲证？</h2>
                        <p>马哈希教导：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li>参究"我是谁？"</li>
                            <li>安住于觉知之中</li>
                            <li>让亲证自然显现</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="jnana.html" class="tag">🛤️ 参究法/Jnana</a>
                            <a href="samadhi.html" class="tag">🧘 三摩地/Samadhi</a>
                            <a href="jivanmukti.html" class="tag">✨ 在生解脱/Jivanmukti</a>
                            <a href="silence.html" class="tag">🤫 静默/Silence</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "paramatma.html",
        "title": "超灵 / Paramatma",
        "icon": "🔆",
        "subtitle": "最高我 · 宇宙的自我",
        "description": "超灵（Paramatma）是吠檀多哲学中意指"最高我"或"宇宙自我"的核心术语，它是个体真我的终极本质，与梵（Brahman）同一。",
        "keywords": "超灵, Paramatma, 最高我, 宇宙自我, 真我, 梵, 拉玛那马哈希",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是超灵？</h2>
                            <p><strong>超灵（Paramatma）</strong>由"param"（最高）和"atma"（我）组成，意指"最高的我"或"宇宙的自我"。它是个体真我的终极本质——万物都是它的显现。</p>
                        </section>

                        <div class="quote-box">
                            "个体真我（Jivatma）如大海中的一滴水，超灵（Paramatma）是整个大海。两者在本质上没有区别——都是水。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>Jivatma vs Paramatma</h2>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>个体我（Jivatma）</strong> - 被我慢包裹的真我，认为自己是分离的</li>
                            <li><strong>超灵（Paramatma）</strong> - 真我未被污染的纯粹状态，与梵同一</li>
                        </ul>

                        <div class="quote-box">
                            "当你参究'我是谁？'，个体我就会消失，超灵就会显现。其实它们一直是一体的。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="atman.html" class="tag">🔮 真我/Atman</a>
                            <a href="brahman.html" class="tag">🌀 梵/Brahman</a>
                            <a href="jiva.html" class="tag">👤 个体灵魂/Jiva</a>
                            <a href="satchidananda.html" class="tag">✨ 存在-意识-喜悦</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "prakriti.html",
        "title": "自性 / Prakriti",
        "icon": "🌱",
        "subtitle": "原质 · 物质世界的源头",
        "description": "自性（Prakriti）是数论哲学和吠檀多哲学中意指"原质"或"自然"的核心术语，它是物质世界显现的源头，与神我（Purusha）相对。",
        "keywords": "自性, Prakriti, 原质, 自然, 神我, Purusha, 数论, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是自性？</h2>
                            <p><strong>自性（Prakriti）</strong>意指"原质"、"自然"、"物质世界的源头"。数论哲学用它来描述宇宙显现的能量——从它演化出所有的物质和心意世界。</p>
                        </section>

                        <div class="quote-box">
                            "自性是显现的能量，它创造了世界。但它本身不是真实的——它只是意识的投射。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>Prakriti 与 Purusha</h2>
                        <p>在数论哲学中，有两个终极原则：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>神我（Purusha）</strong> - 纯粹意识/见者，不活动但觉知</li>
                            <li><strong>自性（Prakriti）</strong> - 物质能量/所见，活跃但无觉知</li>
                        </ul>

                        <div class="quote-box">
                            "神我是看者，自性是被看者。当看者认出自己不是被看者时，就解脱了。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>三德</h2>
                        <p>自性由三德（Guna）组成：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>萨埵（Sattva）</strong> - 纯质/善德/光明</li>
                            <li><strong>剌闍（Rajas）</strong> - 激质/情德/活动</li>
                            <li><strong>多磨（Tamas）</strong> - 暗质/迷德/懒惰</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="purusha.html" class="tag">👁️ 神我/Purusha</a>
                            <a href="maya.html" class="tag">🎭 摩耶/Maya</a>
                            <a href="guna.html" class="tag">⚖️ 三德/Guna</a>
                            <a href="world.html" class="tag">🌍 世界/World</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "purusha.html",
        "title": "神我 / Purusha",
        "icon": "👁️",
        "subtitle": "原人 · 纯粹的觉知",
        "description": "神我（Purusha）是数论哲学和吠檀多哲学中意指"原人"或"纯粹意识"的核心术语，它是觉知者，与自性（Prakriti）相对。",
        "keywords": "神我, Purusha, 原人, 纯粹意识, 见者, 自性, 数论, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是神我？</h2>
                            <p><strong>神我（Purusha）</strong>意指"人"、"原人"、"纯粹意识"。在数论哲学中，它是唯一的觉知者——不活动、不变化、不被污染，但它的光是所有显现的源头。</p>
                        </section>

                        <div class="quote-box">
                            "神我就像太阳，自性就像云朵。云朵遮住太阳，但太阳从未被云朵污染。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>神我的特点</h2>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li>纯粹意识，不包含任何内容</li>
                            <li>见者，不是被见者</li>
                            <li>不活动，只是见证</li>
                            <li>永恒不变，不受任何影响</li>
                        </ul>

                        <div class="quote-box">
                            "你不是行为者，你是神我——见者。行为是自性的工作。"
                            <div class="source">—《对谈录》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="prakriti.html" class="tag">🌱 自性/Prakriti</a>
                            <a href="atman.html" class="tag">🔮 真我/Atman</a>
                            <a href="chit.html" class="tag">✨ 意识/Chit</a>
                            <a href="brahman.html" class="tag">🌀 梵/Brahman</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "nirguna.html",
        "title": "无德 / Nirguna",
        "icon": "🌌",
        "subtitle": "无属性 · 超越一切描述的梵",
        "description": "无德（Nirguna）是吠檀多哲学中意指"无属性"或"超越属性"的核心术语，用来描述梵（Brahman）的终极状态——超越一切语言和概念。",
        "keywords": "无德, Nirguna, 无属性, 有德, Saguna, 梵, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是无德？</h2>
                            <p><strong>无德（Nirguna）</strong>由"nir"（无）和"guna"（德/属性）组成，意指"没有任何属性"、"超越一切属性"。它是梵的终极状态——无法用任何语言、概念或形象来描述。</p>
                        </section>

                        <div class="quote-box">
                            "梵不是这，不是这。（Neti Neti）当你否定一切，剩下的就是梵。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>Nirguna vs Saguna</h2>
                        <p>对梵的两种描述方式：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>有德梵（Saguna Brahman）</strong> - 梵作为有属性的神，如湿婆、毗湿奴等</li>
                            <li><strong>无德梵（Nirguna Brahman）</strong> - 梵作为无属性的绝对存在</li>
                        </ul>

                        <div class="quote-box">
                            "有德梵是楼梯，无德梵是楼顶。楼梯帮助你上楼，但楼顶本身不是楼梯。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="saguna.html" class="tag">👑 有德/Saguna</a>
                            <a href="brahman.html" class="tag">🌀 梵/Brahman</a>
                            <a href="satchidananda.html" class="tag">✨ 存在-意识-喜悦</a>
                            <a href="silence.html" class="tag">🤫 静默/Silence</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "saguna.html",
        "title": "有德 / Saguna",
        "icon": "👑",
        "subtitle": "有属性 · 人格化的梵",
        "description": "有德（Saguna）是吠檀多哲学中意指"有属性"或"人格化"的核心术语，用来描述梵（Brahman）的另一种面向——作为有属性、可以被爱、被崇拜的神。",
        "keywords": "有德, Saguna, 有属性, 无德, Nirguna, 梵, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是有德？</h2>
                            <p><strong>有德（Saguna）</strong>由"sa"（有）和"guna"（德/属性）组成，意指"有属性"、"有特质"。它是梵的人格化面向——作为可以被崇拜、被爱、有慈悲和智慧的神。</p>
                        </section>

                        <div class="quote-box">
                            "有德梵是为有信仰的人准备的。无德梵是为有智慧的人准备的。两者最终会合一。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>奉爱之路</h2>
                        <p>对有德梵的奉爱是一条有力的解脱之路：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li>通过祈祷、咒语、礼拜</li>
                            <li>通过爱和臣服</li>
                            <li>最终"我"消失，与神合一</li>
                        </ul>

                        <div class="quote-box">
                            "奉爱就是记住神——或者说记住真实的自己。当你完全臣服，'我'就消失，神就显现。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="nirguna.html" class="tag">🌌 无德/Nirguna</a>
                            <a href="bhakti.html" class="tag">💖 奉爱/Bhakti</a>
                            <a href="surrender.html" class="tag">🙏 臣服/Surrender</a>
                            <a href="grace.html" class="tag">✨ 恩典/Grace</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "guna.html",
        "title": "三德 / Guna",
        "icon": "⚖️",
        "subtitle": "属性 · 构成自然的三种特质",
        "description": "三德（Guna）是数论哲学和吠檀多哲学中意指"属性"或"特质"的核心术语，它们是构成自性（Prakriti）的三种基本能量——萨埵（Sattva）、剌闍（Rajas）、多磨（Tamas）。",
        "keywords": "三德, Guna, 属性, 萨埵, 剌闍, 多磨, Sattva, Rajas, Tamas, 数论",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是三德？</h2>
                            <p><strong>三德（Guna）</strong>是构成自性（Prakriti）的三种基本能量或属性。它们总是混合在一起，不断变化，创造出所有的心理和物质现象。</p>
                        </section>

                        <div class="quote-box">
                            "三德像编织世界的三根线。当你看穿编织，就会看到背后的纯粹意识。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>三德详解</h2>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>萨埵（Sattva）</strong> - 纯质/善德/光明/平静/智慧/真实</li>
                            <li><strong>剌闍（Rajas）</strong> - 激质/情德/活动/激情/不安</li>
                            <li><strong>多磨（Tamas）</strong> - 暗质/迷德/懒惰/无知/沉重</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>三德与修行</h2>
                        <p>马哈希教导：</p>
                        <div class="quote-box">
                            "你不需要改变三德——你需要认识到你不是三德。三德属于自性，你是神我——见者。"
                            <div class="source">—《对谈录》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="prakriti.html" class="tag">🌱 自性/Prakriti</a>
                            <a href="purusha.html" class="tag">👁️ 神我/Purusha</a>
                            <a href="mind.html" class="tag">🧠 心智/Citta</a>
                            <a href="sadhana.html" class="tag">🧘 修行/Sadhana</a>
                        </div>
                    </div>
        """
    },
    {
        "filename": "vikalpa.html",
        "title": "分别 / Vikalpa",
        "icon": "🔀",
        "subtitle": "妄想 · 制造二元的思维",
        "description": "分别（Vikalpa）是瑜伽和吠檀多哲学中意指"妄想"或"分别心"的核心术语，它是制造二元对立的思维活动，是束缚的根源。",
        "keywords": "分别, Vikalpa, 妄想, 分别心, 二元对立, 瑜伽, 吠檀多",
        "content": """
                    <div class="card">
                        <section>
                            <h2>什么是分别？</h2>
                            <p><strong>分别（Vikalpa）</strong>意指"妄想"、"分别"、"想象"。它是心智制造二元对立的能力——好坏、对错、我/他、喜欢/不喜欢。</p>
                        </section>

                        <div class="quote-box">
                            "分别是绳索，它把你绑在轮回之中。当你停止分别，绳索就会松开。"
                            <div class="source">— 室利·拉玛那·马哈希</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>分别的五种形态</h2>
                        <p>根据瑜伽经，心的变化有五种：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li><strong>正知（Pramana）</strong> - 正确的知识</li>
                            <li><strong>不正知（Viparyaya）</strong> - 错误的知识</li>
                            <li><strong>分别（Vikalpa）</strong> - 想象/妄想</li>
                            <li><strong>睡眠（Nidra）</strong> - 深睡</li>
                            <li><strong>记忆（Smriti）</strong> - 回忆</li>
                        </ul>

                        <div class="quote-box">
                            "分别是最大的敌人。它把'一'变成'多'。参究'我是谁？'会融化所有的分别。"
                            <div class="source">—《走向静默，如你本来》</div>
                        </div>
                    </div>

                    <div class="card">
                        <h2>如何超越分别？</h2>
                        <p>马哈希教导：</p>
                        <ul style="margin-left:1.5rem;margin-bottom:1rem;">
                            <li>觉知分别，但不跟随它</li>
                            <li>参究"这个念头是谁的？"</li>
                            <li>安住于分别背后的那个纯粹意识</li>
                        </ul>
                    </div>

                    <div class="card">
                        <h2>相关概念</h2>
                        <div class="concept-tags">
                            <a href="advaita.html" class="tag">🕊️ 非二元/Advaita</a>
                            <a href="maya.html" class="tag">🎭 摩耶/Maya</a>
                            <a href="thoughts.html" class="tag">💭 念头/Thoughts</a>
                            <a href="viveka.html" class="tag">🔎 抉择/Viveka</a>
                        </div>
                    </div>
        """
    }
]

template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{DESCRIPTION}">
    <meta name="keywords" content="{KEYWORDS}, 拉玛那马哈希">
    <title>{TITLE} | 拉玛那马哈希核心概念详解指南修行智慧详解指南｜拉玛那马哈希灵性智慧完整指南 | 拉玛那马哈希知识库</title>
    <link rel="preload" href="../styles.css" as="style">
    <link rel="preload" href="../app.js" as="script">
    <link rel="dns-prefetch" href="https://www.googletagmanager.com">
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
    <link rel="preconnect" href="https://www.google-analytics.com" crossorigin>
    <link rel="stylesheet" href="../styles.css">
    <meta name="theme-color" content="#1a1a2e">
    <link rel="manifest" href="../manifest.json">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
    <meta name="robots" content="index, follow">
    <meta name="author" content="室利·拉玛那·马哈希 (Sri Ramana Maharshi)">
    <link rel="canonical" href="https://ramanamaharshi.space/concepts/{FILENAME}">

    <meta property="og:title" content="{TITLE} | 拉玛那马哈希核心概念详解指南修行智慧详解指南 | 拉玛那马哈希知识库">
    <meta property="og:description" content="{DESCRIPTION}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ramanamaharshi.space/concepts/{FILENAME}">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="拉玛那马哈希知识库">
    <meta name="publisher" content="拉玛那马哈希知识库">
    <meta property="og:image" content="https://ramanamaharshi.space/images/og-default.jpg">

    <link rel="preconnect" href="https://www.google-analytics.com" crossorigin>
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-MYFWHFPSYB');
</script>

  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{TITLE_ESCAPED} — 拉玛那马哈希核心概念详解",
  "description": "深入了解{SHORT_TITLE}在拉玛那马哈希教示中的含义、实践方法和相关引文。",
  "inLanguage": "zh-CN",
  "articleSection": "Philosophy",
  "about": {{
    "@type": "Thing",
    "name": "{SHORT_TITLE}"
  }},
  "author": {{
    "@type": "Organization",
    "name": "拉玛那马哈希知识库"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "拉玛那马哈希知识库",
    "url": "https://ramanamaharshi.space"
  }},
  "url": "https://ramanamaharshi.space/concepts/{FILENAME}"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "拉玛那马哈希知识库",
      "item": "https://ramanamaharshi.space/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "核心概念",
      "item": "https://ramanamaharshi.space/concepts/index.html"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{SHORT_TITLE}",
      "item": "https://ramanamaharshi.space/concepts/{FILENAME}"
    }}
  ]
}}
</script>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">

<aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
                <button class="sidebar-close-btn" title="收起侧边栏">◀</button>
            </div>

            <div class="search-box">
                <input type="text" id="search-input" placeholder="搜索标题或内容..." autocomplete="off">
                <div id="search-results"></div>
            </div>

            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item"><span class="emoji">📖</span> 书籍总览 <span class="count">18</span></a>
                    <a href="index.html" class="sidebar-item active"><span class="emoji">🔮</span> 核心概念 <span class="count">39+</span></a>
                    <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> 修行方法 <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> 修行问答 <span class="count">28</span></a>
                    <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> 知识图谱</a>
                </div>
            </div>

            <div class="sidebar-section">
                <div class="sidebar-section-title">🔮 核心概念</div>
                <div class="sidebar-items">
                    <a href="atman.html" class="sidebar-item">🔮 真我/Atman</a>
                    <a href="brahman.html" class="sidebar-item">🌀 梵/Brahman</a>
                    <a href="whoami.html" class="sidebar-item">🔍 "我是谁？"</a>
                    <a href="mind.html" class="sidebar-item">🧠 心智/Citta</a>
                    <a href="ego.html" class="sidebar-item">🧠 自我/Ego</a>
                    <a href="moksha.html" class="sidebar-item">🕊️ 解脱/Moksha</a>
                    <a href="karma.html" class="sidebar-item">☸️ 业力/Karma</a>
                    <a href="maya.html" class="sidebar-item">🎭 摩耶/Maya</a>
                    <a href="grace.html" class="sidebar-item">✨ 恩典/Grace</a>
                    <a href="silence.html" class="sidebar-item">🤫 静默/Silence</a>
                    <a href="surrender.html" class="sidebar-item">🙏 臣服/Surrender</a>
                    <a href="samadhi.html" class="sidebar-item">🧘 三摩地/Samadhi</a>
                </div>
            </div>

            <div class="sidebar-section">
                <div class="sidebar-section-title">🛤️ 修行方法</div>
                <div class="sidebar-items">
                    <a href="../methods/index.html#whoami" class="sidebar-item">🔍 参究"我是谁"</a>
                    <a href="../methods/index.html#surrender" class="sidebar-item">🙏 臣服上师</a>
                    <a href="../methods/index.html#japa" class="sidebar-item">🔮 念诵咒语</a>
                </div>
            </div>

            <div class="sidebar-section">
                <div class="sidebar-section-title">👤 关键人物</div>
                <div class="sidebar-items">
                    <a href="../persons/ramana.html" class="sidebar-item">🙏 室利·拉玛那·马哈希</a>
                    <a href="../persons/david.html" class="sidebar-item">📝 大卫·高德曼</a>
                    <a href="../persons/venkataramana.html" class="sidebar-item">👩 韦卡罗达·南达</a>
                </div>
            </div>
        </aside>

        <main class="main-content">
                        <header class="topbar">
                <button class="sidebar-open-btn" title="展开侧边栏">▶</button>
                <div class="topbar-left">
                    <span class="topbar-title">🔮 核心概念</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../books/index.html">书籍</a>
                    <a href="../index.html" class="active">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>

            <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> / <a href="index.html">核心概念</a> / <span>{SHORT_TITLE}</span>
                </nav>

                <article class="concept-detail">
                    <header class="page-header">
                        <h1>{ICON} {TITLE}</h1>
                        <p class="subtitle">{SUBTITLE}</p>
                    </header>

{CONTENT}

                </article>

            </div>

                        <footer class="site-footer">
                <p><a href="../index.html">拉玛那马哈希</a> | 传承自印度阿鲁那佳拉圣山</p>
                <p style="margin-top:0.5rem; font-size:0.9rem; color: var(--text-muted);">© 2026 拉玛那马哈希. 保留所有权利。</p>
                <p style="margin-top:1rem; font-size:0.9rem;"><a href="../sitemap.html" style="color: var(--text-muted); text-decoration: underline;">🌐 网站地图</a> <span style="margin: 0 1rem;">|</span> <a href="mailto:591611431@qq.com" style="color: var(--text-muted); text-decoration: underline;">联系我</a></p>
            </footer>
        </main>
    </div>

    <script>
    if ('serviceWorker' in navigator) {{
        window.addEventListener('load', function() {{
            navigator.serviceWorker.register('sw.js')
                .then(function(registration) {{
                    console.log('SW registered:', registration.scope);
                }})
                .catch(function(error) {{
                    console.log('SW registration failed:', error);
                }});
        }});
    }}
    </script>
<script src="pwa-analytics.js" defer></script>
    <script src="script.js" defer></script>
<script>document.addEventListener("click",function(e){{if(e.target.closest(".sidebar-close-btn,.sidebar-open-btn")){{e.preventDefault();var s=document.getElementById("sidebar"),m=document.querySelector(".main-content"),t=document.querySelector(".topbar"),b=document.querySelector(".sidebar-close-btn");if(!s)return;if(s.classList.contains("desktop-hidden")){{s.classList.remove("desktop-hidden");if(m)m.classList.remove("full-width");if(t)t.classList.remove("reading-mode");if(b){{b.textContent="◀";b.title="收起侧边栏";}}}}else{{s.classList.add("desktop-hidden");if(m)m.classList.add("full-width");if(t)t.classList.remove("reading-mode");if(b){{b.textContent="▶";b.title="展开侧边栏";}}}}}}}});</script>
</body>
</html>
"""

for concept in concepts:
    filepath = f"/workspace/pages/concepts/{concept['filename']}"
    content = template.format(
        FILENAME=concept["filename"],
        TITLE=concept["title"],
        TITLE_ESCAPED=concept["title"].replace('"', '\\"'),
        SHORT_TITLE=concept["title"],
        ICON=concept["icon"],
        SUBTITLE=concept["subtitle"],
        DESCRIPTION=concept["description"],
        KEYWORDS=concept["keywords"],
        CONTENT=concept["content"]
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created: {filepath}")

print(f"\nSuccessfully created {len(concepts)} concept pages!")
