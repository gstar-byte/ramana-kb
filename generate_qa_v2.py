#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 qa-29 到 qa-43（共15页）新内容 - v2
基于 pdf_content 原文素材，智能提取段落并转换为问答
"""

import os
import re
import random

qa_dir = 'pages/qa'
os.makedirs(qa_dir, exist_ok=True)

def load_text(fname):
    try:
        with open(f'pdf_content/{fname}', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

def extract_paragraphs(text, min_len=80, max_len=500):
    """提取合适的段落"""
    # 清理文本
    text = re.sub(r'\n{3,}', '\n\n', text)
    paragraphs = text.split('\n\n')
    
    valid = []
    for p in paragraphs:
        p = p.strip()
        # 过滤太短的
        if len(p) < min_len:
            continue
        # 过滤太长的（尝试分割）
        if len(p) > max_len:
            # 按句子分割
            sentences = re.split(r'(?<=[。！？.!?])\s+', p)
            current = ""
            for s in sentences:
                if len(current) + len(s) < max_len:
                    current += s
                else:
                    if len(current) >= min_len:
                        valid.append(current.strip())
                    current = s
            if len(current) >= min_len:
                valid.append(current.strip())
        else:
            valid.append(p)
    
    return valid

def para_to_qa(para, theme_keywords, index):
    """将段落转换为问答"""
    # 清理段落
    para = para.replace('\n', ' ').strip()
    
    # 尝试找到问句
    question_patterns = [
        r'([^。]*(?:什么|如何|为什么|是否|怎么|哪里|谁|何时)[^。]*[？?])',
        r'([^。]*(?:问|问道|询问)[^。]*[：:])',
    ]
    
    question = None
    answer = para
    
    for pattern in question_patterns:
        match = re.search(pattern, para)
        if match:
            question = match.group(1).strip()
            answer = para.replace(question, '').strip()
            # 清理开头的标点
            answer = re.sub(r'^[：:\s]+', '', answer)
            break
    
    if not question or len(question) < 5:
        # 生成问题
        generic_questions = [
            "马哈希对此有何教导？",
            "这在修行中意味着什么？",
            "我们应该如何理解这一点？",
            "这对日常生活有什么启示？",
            "这与真我有什么关系？",
            "如何在实践中应用这个教导？",
            "马哈希是如何解释这个问题的？",
            "这个教导的核心是什么？",
        ]
        question = generic_questions[index % len(generic_questions)]
    
    # 确保答案不太短
    if len(answer) < 30:
        answer = para
    
    # 限制长度
    if len(answer) > 400:
        answer = answer[:397] + "..."
    
    return question, answer

# 15页主题规划
pages_plan = [
    {"num": 29, "title": "归伏与臣服之道", "subtitle": "《宝钻集》第十二章：完全的降服", "source": "gems_from_bhagavan.txt", 
     "keywords": ["臣服", "归伏", "投降", "surrender", "降服", "奉献", "devotion", "bhakti"]},
    {"num": 30, "title": "念诵与持名", "subtitle": "《上师言颂》：名号的力量", "source": "guru_vachaka_kovai.txt",
     "keywords": ["念诵", "持名", "japa", "咒语", "名号", "重复", "name", "mantra"]},
    {"num": 31, "title": "苦行与自律", "subtitle": "《对谈录》：关于苦行的问答", "source": "talks_with_ramana_1.txt",
     "keywords": ["苦行", "自律", "禁欲", "饮食", "节制", "discipline", "austerity"]},
    {"num": 32, "title": "情绪与欲望", "subtitle": "《日日与彼》：面对内心的波动", "source": "day_by_day.txt",
     "keywords": ["情绪", "欲望", "愤怒", "恐惧", "贪爱", "emotion", "desire", "anger", "fear"]},
    {"num": 33, "title": "关系与爱", "subtitle": "《超越爱与恩典》：在关系中修行", "source": "surpassing_love.txt",
     "keywords": ["爱", "关系", "家庭", "伴侣", "亲情", "love", "relationship", "family"]},
    {"num": 34, "title": "疾病与痛苦", "subtitle": "《面对面》：身体病痛中的觉知", "source": "face_to_face.txt",
     "keywords": ["疾病", "痛苦", "病痛", "健康", "身体", "illness", "pain", "suffering", "disease"]},
    {"num": 35, "title": "金钱与物质", "subtitle": "《桌边碎语》：超越贫富的分别", "source": "crumbs_table.txt",
     "keywords": ["金钱", "财富", "贫穷", "物质", "拥有", "money", "wealth", "possession", "rich", "poor"]},
    {"num": 36, "title": "食物与饮食", "subtitle": "《马哈希福音》：关于饮食的教导", "source": "maharshi_gospel.txt",
     "keywords": ["食物", "饮食", "素食", "进食", "饥饿", "food", "diet", "eat", "vegetarian"]},
    {"num": 37, "title": "睡眠与无梦", "subtitle": "《大瑜伽》：深睡中的真我", "source": "maha_yoga.txt",
     "keywords": ["睡眠", "无梦", "深睡", "休息", "清醒", "sleep", "dream", "deep sleep", "waking"]},
    {"num": 38, "title": "神通与奇迹", "subtitle": "《秘密印度》：关于神秘现象", "source": "search_secret_india.txt",
     "keywords": ["神通", "奇迹", "siddhi", "神秘", "超自然", "power", "miracle", "supernatural", "occult"]},
    {"num": 39, "title": "经典与经文", "subtitle": "《以言传意》：如何看待经典", "source": "teachings_in_own_words.txt",
     "keywords": ["经典", "经文", "吠陀", "奥义书", "圣经", "scripture", "veda", "upanishad", "bible", "text"]},
    {"num": 40, "title": "其他修行法门", "subtitle": "《对谈录》：瑜伽、禅定与参究的比较", "source": "talks_with_ramana_1.txt",
     "keywords": ["瑜伽", "禅定", "冥想", "哈达瑜伽", "呼吸", "yoga", "meditation", "pranayama", "hatha", "kundalini"]},
    {"num": 41, "title": "马哈希的生平", "subtitle": "《时代中的永恒》：大师的一生", "source": "timeless_in_time.txt",
     "keywords": ["生平", "童年", "觉醒", "阿鲁那佳拉", "山", "life", "childhood", "awakening", "arunachala", "tiruvannamalai"]},
    {"num": 42, "title": "静修院生活", "subtitle": "《日日与彼》：在道场的日子", "source": "day_by_day.txt",
     "keywords": ["静修院", "道场", "ashram", "生活", "日常", "ashram", "hermitage", "daily life", "routine"]},
    {"num": 43, "title": "弟子与传承", "subtitle": "《灵性故事》：马哈希的弟子们", "source": "spiritual_stories.txt",
     "keywords": ["弟子", "传承", "devotee", "奉献者", "故事", "disciple", "devotee", "follower", "story"]},
]

def score_paragraph(para, keywords):
    """给段落打分，越高越相关"""
    score = 0
    para_lower = para.lower()
    for kw in keywords:
        if kw.lower() in para_lower:
            score += 2
        # 中文分词匹配
        if kw in para:
            score += 3
    # 偏好包含问答特征的段落
    if any(w in para for w in ['问', '？', '?', '答', '说', '道']):
        score += 1
    return score

def generate_qa_page(plan, qa_list):
    """生成单个QA页面的HTML"""
    num = plan["num"]
    title = plan["title"]
    subtitle = plan["subtitle"]
    
    qa_items = ""
    for q, a in qa_list[:8]:
        qa_items += f'''
                        <div class="qa-item">
                            <div class="qa-q">❓ {q}</div>
                            <div class="qa-a">{a}</div>
                        </div>'''
    
    prev_link = f"qa-{num-1}.html" if num > 29 else "qa-28.html"
    next_link = f"qa-{num+1}.html" if num < 43 else "index.html"
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - {subtitle}。精选自拉玛那马哈希的教导，包含原汁原味的灵性问答与修行指引。">
    <meta name="keywords" content="马哈希, 问答, 修行, 灵性, {plan['keywords'][0]}">
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

def main():
    print("开始生成 qa-29 到 qa-43 (v2)...\n")
    
    # 预加载所有文本
    texts = {}
    for plan in pages_plan:
        src = plan["source"]
        if src not in texts:
            texts[src] = load_text(src)
            print(f"加载: {src} ({len(texts[src])} 字符)")
    
    print()
    
    # 生成每一页
    for plan in pages_plan:
        num = plan["num"]
        src = plan["source"]
        text = texts.get(src, "")
        
        if not text:
            print(f"⚠️  {num}: 无文本内容")
            continue
        
        # 提取所有段落
        paragraphs = extract_paragraphs(text)
        print(f"{num}: 提取到 {len(paragraphs)} 个段落")
        
        # 按相关性排序
        scored = [(p, score_paragraph(p, plan["keywords"])) for p in paragraphs]
        scored.sort(key=lambda x: x[1], reverse=True)
        
        # 取前8个
        top_paras = [p for p, s in scored[:12]]
        random.shuffle(top_paras)  # 随机打乱，增加多样性
        
        # 转换为问答
        qa_list = []
        for i, para in enumerate(top_paras[:8]):
            q, a = para_to_qa(para, plan["keywords"], i)
            qa_list.append((q, a))
        
        # 生成HTML
        html = generate_qa_page(plan, qa_list)
        
        # 保存
        fpath = os.path.join(qa_dir, f'qa-{num}.html')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"  ✓ qa-{num}.html: {plan['title']} ({len(qa_list)}条QA)")
    
    print("\n✅ 完成！已生成 qa-29 到 qa-43")

if __name__ == '__main__':
    main()
