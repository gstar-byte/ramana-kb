"""
重构 collected-works.html：改名"权威合集" + 标准页面结构
"""
import os, re

BASE = r"c:/Users/willp/Desktop/2026年4月/kb01/pages/books"
path = os.path.join(BASE, "collected-works.html")

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# ===== 1. 侧边栏"全集" → "权威合集" =====
html = html.replace('📚 全集', '📚 权威合集')

# ===== 2. Topbar "全集" → "权威合集" =====
html = html.replace('topbar-title">📚 全集', 'topbar-title">📚 权威合集')

# ===== 3. 重构主体内容区域 =====
# 找到 <div class="content-wrapper"> 开始的位置
cw_start = html.find('<div class="content-wrapper">')

# 旧主体（从 book-detail 到 </div>）
old_body_start = html.find('<article class="book-detail">')
old_body_end = html.find('</div>\n\n                         \n    <!-- 上一本', cw_start)  # 找 content-wrapper 的闭合 </div>

if old_body_end == -1:
    old_body_end = html.find('</div>\n\n\n    <!-- 上一本', cw_start)

if old_body_end == -1:
    # 尝试找 footer 前的位置
    footer_pos = html.find('<footer class="site-footer">')
    old_body_end = html.rfind('</div>', 0, footer_pos)

print(f"cw_start={cw_start}, old_body_end={old_body_end}")

# 新主体
new_body = '''
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> / <a href="index.html">书籍</a> / <span>权威合集</span>
                </nav>

                <header class="page-header">
                    <h1>📚 权威合集</h1>
                    <p class="subtitle">Collected Works | Sri Ramana Maharshi 原著</p>
                </header>

                <!-- 书籍简介 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📚 书籍简介</h2>
                    <p style="margin-bottom:1rem;"><strong>《权威合集》</strong>（Collected Works）是马哈希全部文字作品的权威汇编，收录了他亲自撰写的所有著作，包括最核心的《本心十论》（Upadesa Saram）和《五我问》（Vichara Sutram）。</p>
                    <p style="margin-bottom:1rem;">这部著作是研究马哈希教法的最重要原始文献，让读者得以直接接触大师本人的文字。其中《本心十论》以简洁的诗体阐述了自我参究的精髓，被公认为马哈希教示的核心纲要。</p>
                    <div class="concept-tags" style="margin-top:1rem;">
                        <span class="tag">吠檀多</span>
                        <span class="tag">自我参究</span>
                        <span class="tag">哲学专著</span>
                    </div>
                </div>

                <!-- 核心内容 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1.5rem;">📑 核心内容</h2>

                    <div class="chapter-card">
                        <h4>《本心十论》Upadesa Saram <span class="chapter-arrow">→</span></h4>
                        <p class="summary">马哈希本人撰写的核心教义，以十节诗精炼阐述自我参究的精髓。每节诗都是通往证悟的指引，核心教导指向一点：消融自我，证悟真我。此论是马哈希教法的纲要性文献。</p>
                    </div>

                    <div class="chapter-card">
                        <h4>《五我问》Vichara Sutram <span class="chapter-arrow">→</span></h4>
                        <p class="summary">以箴言形式阐述自我参究的方法。五个问题层层深入，引导修行者通过"我是谁？"的参究，认出并消融心智活动，最终证悟真我。是《本心十论》的姊妹篇。</p>
                    </div>

                    <div class="chapter-card">
                        <h4>《自性警策》 <span class="chapter-arrow">→</span></h4>
                        <p class="summary">马哈希对弟子的警策开示，提醒修行者保持觉知，警惕心智的幻相游戏。文字简短有力，直指人心。</p>
                    </div>

                    <div class="chapter-card">
                        <h4>《十论偈》 <span class="chapter-arrow">→</span></h4>
                        <p class="summary">十首偈语诗，涵盖自我参究、静默、恩典等核心主题。配合《本心十论》阅读，可更全面理解马哈希的教法体系。</p>
                    </div>
                </div>

                <!-- 相关书籍 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📚 相关书籍</h2>
                    <div class="concept-tags">
                        <a href="be-as-you-are.html" class="tag">📖 走向静默，如你本来</a>
                        <a href="gems.html" class="tag">💎 宝钻集</a>
                        <a href="maharshi-gospel.html" class="tag">📜 马哈希福音</a>
                    </div>
                </div>

                <!-- 源文档 -->
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📥 源文档</h2>
                    <div class="concept-tags">
                        <a href="../pdf_content/collected_works.txt" class="tag" download>📄 Collected Works 原文 (TXT)</a>
                    </div>
                </div>

'''

# 替换
html = html[:cw_start + len('<div class="content-wrapper">')] + '\n' + new_body + html[old_body_end:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ collected-works.html 重构完成：书名→权威合集，结构→标准card布局")
