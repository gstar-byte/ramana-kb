#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 qa-29 到 qa-43（共15页）新内容
基于 pdf_content 原文素材，每页8条真实问答
"""

import os
import re

qa_dir = 'pages/qa'
os.makedirs(qa_dir, exist_ok=True)

# 读取原文素材
def load_text(fname):
    try:
        with open(f'pdf_content/{fname}', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

# 15页主题规划（避开qa-1~28已覆盖的主题）
pages_plan = [
    {
        "num": 29,
        "title": "归伏与臣服之道",
        "subtitle": "《宝钻集》第十二章：完全的降服",
        "source": "gems_from_bhagavan.txt",
        "keywords": ["臣服", "归伏", "投降", "surrender", "降服"]
    },
    {
        "num": 30,
        "title": "念诵与持名",
        "subtitle": "《上师言颂》：名号的力量",
        "source": "guru_vachaka_kovai.txt",
        "keywords": ["念诵", "持名", "japa", "咒语", "名号"]
    },
    {
        "num": 31,
        "title": "苦行与自律",
        "subtitle": "《对谈录》：关于苦行的问答",
        "source": "talks_with_ramana_1.txt",
        "keywords": ["苦行", "自律", "禁欲", "饮食", "节制"]
    },
    {
        "num": 32,
        "title": "情绪与欲望",
        "subtitle": "《日日与彼》：面对内心的波动",
        "source": "day_by_day.txt",
        "keywords": ["情绪", "欲望", "愤怒", "恐惧", "贪爱"]
    },
    {
        "num": 33,
        "title": "关系与爱",
        "subtitle": "《超越爱与恩典》：在关系中修行",
        "source": "surpassing_love.txt",
        "keywords": ["爱", "关系", "家庭", "伴侣", "亲情"]
    },
    {
        "num": 34,
        "title": "疾病与痛苦",
        "subtitle": "《面对面》：身体病痛中的觉知",
        "source": "face_to_face.txt",
        "keywords": ["疾病", "痛苦", "病痛", "健康", "身体"]
    },
    {
        "num": 35,
        "title": "金钱与物质",
        "subtitle": "《桌边碎语》：超越贫富的分别",
        "source": "crumbs_table.txt",
        "keywords": ["金钱", "财富", "贫穷", "物质", "拥有"]
    },
    {
        "num": 36,
        "title": "食物与饮食",
        "subtitle": "《马哈希福音》：关于饮食的教导",
        "source": "maharshi_gospel.txt",
        "keywords": ["食物", "饮食", "素食", "进食", "饥饿"]
    },
    {
        "num": 37,
        "title": "睡眠与无梦",
        "subtitle": "《大瑜伽》：深睡中的真我",
        "source": "maha_yoga.txt",
        "keywords": ["睡眠", "无梦", "深睡", "休息", "清醒"]
    },
    {
        "num": 38,
        "title": "神通与奇迹",
        "subtitle": "《秘密印度》：关于神秘现象",
        "source": "search_secret_india.txt",
        "keywords": ["神通", "奇迹", "siddhi", "神秘", "超自然"]
    },
    {
        "num": 39,
        "title": "经典与经文",
        "subtitle": "《以言传意》：如何看待经典",
        "source": "teachings_in_own_words.txt",
        "keywords": ["经典", "经文", "吠陀", "奥义书", "圣经"]
    },
    {
        "num": 40,
        "title": "其他修行法门",
        "subtitle": "《对谈录》：瑜伽、禅定与参究的比较",
        "source": "talks_with_ramana_1.txt",
        "keywords": ["瑜伽", "禅定", "冥想", "哈达瑜伽", "呼吸"]
    },
    {
        "num": 41,
        "title": "马哈希的生平",
        "subtitle": "《时代中的永恒》：大师的一生",
        "source": "timeless_in_time.txt",
        "keywords": ["生平", "童年", "觉醒", "阿鲁那佳拉", "山"]
    },
    {
        "num": 42,
        "title": "静修院生活",
        "subtitle": "《日日与彼》：在道场的日子",
        "source": "day_by_day.txt",
        "keywords": ["静修院", "道场", "ashram", "生活", "日常"]
    },
    {
        "num": 43,
        "title": "弟子与传承",
        "subtitle": "《灵性故事》：马哈希的弟子们",
        "source": "spiritual_stories.txt",
        "keywords": ["弟子", "传承", "devotee", "奉献者", "故事"]
    }
]

# 从文本中提取相关段落
def extract_relevant_qa(text, keywords, max_qa=8):
    """从文本中提取与关键词相关的问答段落"""
    paragraphs = text.split('\n\n')
    relevant = []
    
    for para in paragraphs:
        para = para.strip()
        if len(para) < 50 or len(para) > 800:
            continue
        # 检查是否包含关键词
        if any(kw in para for kw in keywords):
            relevant.append(para)
    
    # 如果没有找到足够内容，返回一些通用段落
    if len(relevant) < max_qa:
        for para in paragraphs:
            para = para.strip()
            if len(para) >= 100 and len(para) <= 600 and para not in relevant:
                relevant.append(para)
            if len(relevant) >= max_qa * 2:
                break
    
    return relevant[:max_qa * 2]

# 将段落转换为问答格式
def para_to_qa(para, index):
    """将段落转换为问答格式"""
    # 尝试从段落中提取问题和答案
    lines = para.split('\n')
    
    # 如果段落很短，直接作为答案，生成问题
    if len(para) < 200:
        questions = [
            "马哈希对此有何教导？",
            "这在修行中意味着什么？",
            "我们应该如何理解这一点？",
            "这对日常生活有什么启示？",
            "这与真我有什么关系？",
            "如何在实践中应用？",
            "这与其他修行方法有何不同？",
            "马哈希是如何解释这个问题的？"
        ]
        q = questions[index % len(questions)]
        a = para
    else:
        # 尝试分割成问答
        # 第一句作为问题，其余作为答案
        sentences = re.split(r'(?<=[。！？])', para)
        if len(sentences) >= 2:
            q = sentences[0].strip()
            a = ''.join(sentences[1:]).strip()
            if len(q) > 100:
                q = q[:100] + "..."
        else:
            q = "关于这个主题，马哈希怎么说？"
            a = para
    
    return q, a

# 生成HTML页面
def generate_qa_page(plan, qa_list):
    """生成单个QA页面的HTML"""
    num = plan["num"]
    title = plan["title"]
    subtitle = plan["subtitle"]
    
    qa_items = ""
    for i, (q, a) in enumerate(qa_list[:8]):
        qa_items += f'''
                        <div class="qa-item">
                            <div class="qa-q">❓ {q}</div>
                            <div class="qa-a">{a}</div>
                        </div>'''
    
    prev_num = num - 1 if num > 1 else "index"
    next_num = num + 1 if num < 58 else "index"
    prev_link = f"qa-{prev_num}.html" if prev_num != "index" else "index.html"
    next_link = f"qa-{next_num}.html" if next_num != "index" else "index.html"
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - {subtitle}。精选自拉玛那马哈希的教导，包含原汁原味的灵性问答与修行指引。">
    <meta name="keywords" content="马哈希, 问答, 修行, 灵性, {plan['keywords'][0] if plan['keywords'] else '真我'}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://ramanamaharshi.space/qa/qa-{num}">
    <meta property="og:title" content="{title} | 拉玛那马哈希知识库">
    <meta property="og:description" content="{title} - {subtitle}。精选自拉玛那马哈希的教导。">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ramanamaharshi.space/qa/qa-{num}">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="拉玛那马哈希知识库">
    <title>{title} | 拉玛那马哈希知识库</title>
    <link rel="stylesheet" href="../styles.css">
    <meta name="theme-color" content="#1a1a2e">
    <link rel="manifest" href="../manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-MYFWHFPSYB');
    </script>
</head>
<body>
    <div class="app-container">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                <a href="../index.html" class="logo">🙏 拉玛那马哈希知识库</a>
            </div>
            <div class="sidebar-content">
                <input type="text" class="sidebar-search" placeholder="搜索..." onkeyup="filterSidebar(this.value)">
                <div class="nav-section">
                    <div class="nav-header" onclick="toggleSection(this)">💬 修行问答</div>
                    <div class="nav-content">
                        <a href="index.html">问答目录</a>
                        <a href="qa-1.html">真我与自我</a>
                        <a href="qa-2.html">心智的本质</a>
                        <a href="qa-3.html">参究我是谁</a>
                    </div>
                </div>
            </div>
        </aside>
        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">💬 修行问答</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../books/index.html">书籍</a>
                    <a href="../concepts/index.html">概念</a>
                    <a href="index.html" class="active">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>
            <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> / <a href="index.html">修行问答</a> / <span>{title.replace('💬 ', '')}</span>
                </nav>
                <div class="page-header">
                    <h1>{title}</h1>
                    <p class="subtitle">{subtitle}</p>
                </div>
                <div class="qa-container">{qa_items}
                </div>
                <div class="pagination">
                    <a href="index.html" class="page-link">目录</a>
                    <a href="{prev_link}" class="page-link">上一页</a>
                    <a href="{next_link}" class="page-link">下一页</a>
                </div>
            </div>
        </main>
    </div>
    <script src="../script.js"></script>
    <script>
    if ('serviceWorker' in navigator) {{
        window.addEventListener('load', function() {{
            navigator.serviceWorker.register('../sw.js')
                .then(function(reg) {{ console.log('SW registered:', reg.scope); }})
                .catch(function(err) {{ console.log('SW failed:', err); }});
        }});
    }}
    </script>
</body>
</html>'''
    
    return html

# 主函数
def main():
    print("开始生成 qa-29 到 qa-43...")
    
    # 预加载所有文本
    texts = {}
    for plan in pages_plan:
        src = plan["source"]
        if src not in texts:
            texts[src] = load_text(src)
            print(f"  加载: {src} ({len(texts[src])} 字符)")
    
    # 生成每一页
    for plan in pages_plan:
        num = plan["num"]
        src = plan["source"]
        text = texts.get(src, "")
        
        if not text:
            print(f"  ⚠️  {num}: 无文本内容，跳过")
            continue
        
        # 提取相关段落
        relevant = extract_relevant_qa(text, plan["keywords"])
        
        # 转换为问答
        qa_list = []
        for i, para in enumerate(relevant[:8]):
            q, a = para_to_qa(para, i)
            qa_list.append((q, a))
        
        # 生成HTML
        html = generate_qa_page(plan, qa_list)
        
        # 保存
        fpath = os.path.join(qa_dir, f'qa-{num}.html')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"  ✓ qa-{num}.html: {plan['title']} ({len(qa_list)}条QA)")
    
    print("\n完成！已生成 qa-29 到 qa-43")

if __name__ == '__main__':
    main()
