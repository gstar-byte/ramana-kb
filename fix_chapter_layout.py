#!/usr/bin/env python3
"""
修复马哈希福音ch7-ch14的页面布局，使其与ch1-ch6保持一致
"""

import re
import os

# 文件列表
files = [
    "pages/books/maharshi-gospel-ch7.html",
    "pages/books/maharshi-gospel-ch8.html",
    "pages/books/maharshi-gospel-ch9.html",
    "pages/books/maharshi-gospel-ch10.html",
    "pages/books/maharshi-gospel-ch11.html",
    "pages/books/maharshi-gospel-ch12.html",
    "pages/books/maharshi-gospel-ch13.html",
    "pages/books/maharshi-gospel-ch14.html",
]

# 章节信息
chapters = {
    "ch7": {"title": "第七章：上师与恩典", "subtitle": "Guru and His Grace", "prev": "ch6", "prev_title": "自我了悟", "next": "ch8", "next_title": "平安与幸福"},
    "ch8": {"title": "第八章：平安与幸福", "subtitle": "Peace and Happiness", "prev": "ch7", "prev_title": "上师与恩典", "next": "ch9", "next_title": "自我参究"},
    "ch9": {"title": "第九章：自我参究", "subtitle": "Self-enquiry", "prev": "ch8", "prev_title": "平安与幸福", "next": "ch10", "next_title": "修行与恩典"},
    "ch10": {"title": "第十章：修行与恩典", "subtitle": "Sadhana and Grace", "prev": "ch9", "prev_title": "自我参究", "next": "ch11", "next_title": "觉者与世界"},
    "ch11": {"title": "第十一章：觉者与世界", "subtitle": "The Jnani and the World", "prev": "ch10", "prev_title": "修行与恩典", "next": "ch12", "next_title": "本心即真我"},
    "ch12": {"title": "第十二章：本心即真我", "subtitle": "The Heart is the Self", "prev": "ch11", "prev_title": "觉者与世界", "next": "ch13", "next_title": "本心的位置"},
    "ch13": {"title": "第十三章：本心的位置", "subtitle": "The Place of the Heart", "prev": "ch12", "prev_title": "本心即真我", "next": "ch14", "next_title": "\"我\"与\"我念\""},
    "ch14": {"title": "第十四章：\"我\"与\"我念\"", "subtitle": "Aham and Aham-Vritti", "prev": "ch13", "prev_title": "本心的位置", "next": "index", "next_title": "返回书籍首页"},
}

def fix_file(filepath, ch_key):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    ch_info = chapters[ch_key]
    
    # 1. 修复顶部导航栏
    old_topbar = '''    <header class="topbar">
        <button class="menu-btn" onclick="openSidebar()">☰</button>
        <nav class="topbar-nav">'''
    
    new_topbar = '''    <header class="topbar">
        <div class="topbar-left">
            <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
            <span class="topbar-title">📜 马哈希福音</span>
        </div>
        <nav class="topbar-nav topbar-full">'''
    
    content = content.replace(old_topbar, new_topbar)
    
    # 2. 修复面包屑和content-wrapper结构
    # 找到 <main class="main-content"> 后面的内容
    old_main_start = '''    <main class="main-content">
        <div class="breadcrumb">'''
    
    new_main_start = f'''        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">📜 马哈希福音</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="index.html" class="active">书籍</a>
                    <a href="../concepts/index.html">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>
            
            <div class="content-wrapper">
                <nav class="breadcrumb">'''
    
    content = content.replace(old_main_start, new_main_start)
    
    # 3. 修复面包屑中的链接
    content = content.replace('<a href="./index.html">书籍</a>', '<a href="index.html">书籍</a>')
    content = content.replace('<a href="./maharshi-gospel.html">马哈希福音</a>', '<a href="maharshi-gospel.html">马哈希福音</a>')
    
    # 4. 修复 article 标签为 div
    content = content.replace('<article class="page-content">', '<div class="page-content">')
    content = content.replace('</article>', '</div>')
    
    # 5. 在 </div> (page-content结束) 后添加 </div> (content-wrapper结束)
    # 这个需要找到正确的位置
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filepath}")

# 执行修复
base_path = "c:/Users/willp/Desktop/2026年4月/kb01"

for i, filename in enumerate(files, 7):
    ch_key = f"ch{i}"
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        fix_file(filepath, ch_key)
    else:
        print(f"File not found: {filepath}")

print("\nDone!")
