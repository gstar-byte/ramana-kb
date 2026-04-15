# -*- coding: utf-8 -*-
"""统一修复所有断点的汉堡菜单和顶部导航"""

with open('pages/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复 768px-900px 断点
old_768_900 = '''/* Tablet 小平板 (768px - 900px) - 显示首页、书籍、概念、问答、图谱 */
@media (min-width: 768px) and (max-width: 900px) {
    html { font-size: 15px; }
    
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .quick-entry { grid-template-columns: repeat(2, 1fr); gap: 8px; }
    
    .stat-card .number { font-size: 30px; }
    .card h2 { font-size: 18px; }
    
    main { padding: 20px 20px 60px; }
    
    /* 侧边栏隐藏，主内容无左边距 */
    .main-content { margin-left: 0; }
    
    /* 侧边栏 - 隐藏，用汉堡菜单 */
    .sidebar { 
        transform: translateX(-100%); 
        transition: transform .3s ease; 
    }
    .sidebar.open { transform: translateX(0); }
    
    .hamburger {
        display: flex !important;
    }
    
    .page-header h1 { font-size: 26px; }
    
    /* 顶部导航 - 固定在顶部，从44px开始（避开汉堡菜单） */
    .topbar {
        position: fixed !important;
        top: 0 !important;
        left: 44px !important;
        right: 0 !important;
        height: 44px;
        z-index: 100;
        justify-content: flex-start !important;
    }
    
    /* 顶部导航 - 显示首页、书籍、概念、问答、图谱，隐藏方法、人物 */
    .topbar-nav a:nth-child(4)   /* 方法 */
    { display: none !important; }
    .topbar-nav a:nth-child(6)   /* 人物 */
    { display: none !important; }
    
    /* 缩小字体和间距，让菜单更紧凑 */
    .topbar-nav a {
        padding: 10px 12px;
        font-size: 13px;
    }
}'''

new_768_900 = '''/* Tablet 小平板 (768px - 900px) - 显示首页、书籍、概念、问答、图谱 */
@media (min-width: 768px) and (max-width: 900px) {
    html { font-size: 15px; }
    
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .quick-entry { grid-template-columns: repeat(2, 1fr); gap: 8px; }
    
    .stat-card .number { font-size: 30px; }
    .card h2 { font-size: 18px; }
    
    main { padding: 20px 20px 60px; }
    
    /* 侧边栏隐藏，主内容无左边距 */
    .main-content { margin-left: 0; margin-top: 44px; }
    
    /* 侧边栏 - 隐藏，用汉堡菜单 */
    .sidebar { 
        transform: translateX(-100%); 
        transition: transform .3s ease; 
    }
    .sidebar.open { transform: translateX(0); }
    
    /* 汉堡菜单 - 固定在左上角，与顶部导航对齐 */
    .hamburger {
        display: flex !important;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1001;
        background: var(--navy);
        color: #fff;
        border: none;
        border-right: 1px solid rgba(255,255,255,.1);
        font-size: 20px;
        padding: 0;
        cursor: pointer;
    }
    
    .page-header h1 { font-size: 26px; }
    
    /* 顶部导航 - 固定在顶部，从44px开始 */
    .topbar {
        position: fixed !important;
        top: 0 !important;
        left: 44px !important;
        right: 0 !important;
        height: 44px;
        z-index: 100;
        justify-content: flex-start !important;
    }
    
    /* 顶部导航 - 显示首页、书籍、概念、问答、图谱，隐藏方法、人物 */
    .topbar-nav a:nth-child(4)   /* 方法 */
    { display: none !important; }
    .topbar-nav a:nth-child(6)   /* 人物 */
    { display: none !important; }
    
    /* 缩小字体和间距，让菜单更紧凑 */
    .topbar-nav a {
        padding: 10px 12px;
        font-size: 13px;
    }
}'''

content = content.replace(old_768_900, new_768_900)

# 2. 修复 1025px-1200px 断点
old_1025_1200 = '''/* 1024px - 1200px：显示完整7项 */
@media (min-width: 1025px) and (max-width: 1200px) {
    html { font-size: 15px; }
    
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .quick-entry { grid-template-columns: repeat(2, 1fr); gap: 8px; }
    
    .stat-card .number { font-size: 30px; }
    .card h2 { font-size: 18px; }
    
    main { padding: 20px 20px 60px; }
    
    /* 侧边栏隐藏，主内容无左边距 */
    .main-content { 
        margin-left: 0 !important; 
        margin-top: 44px;
    }
    
    /* 侧边栏 - 隐藏，用汉堡菜单 */
    .sidebar { 
        transform: translateX(-100%); 
        transition: transform .3s ease; 
    }
    .sidebar.open { transform: translateX(0); }
    
    .hamburger {
        display: flex !important;
        position: fixed;
        top: 2px;
        left: 2px;
        z-index: 1001;
    }
    
    .page-header h1 { font-size: 26px; }
    
    /* 顶部导航 - 固定在顶部，从左边0开始 */
    .topbar {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 44px;
        width: 100%;
        z-index: 100;
        justify-content: flex-start !important;
    }
    
    /* 顶部导航 - 显示全部7项 */
    .topbar-nav a { display: flex !important; }
}'''

new_1025_1200 = '''/* 1024px - 1200px：显示完整7项 */
@media (min-width: 1025px) and (max-width: 1200px) {
    html { font-size: 15px; }
    
    .stats-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
    .quick-entry { grid-template-columns: repeat(2, 1fr); gap: 8px; }
    
    .stat-card .number { font-size: 30px; }
    .card h2 { font-size: 18px; }
    
    main { padding: 20px 20px 60px; }
    
    /* 侧边栏隐藏，主内容无左边距 */
    .main-content { margin-left: 0 !important; margin-top: 44px; }
    
    /* 侧边栏 - 隐藏，用汉堡菜单 */
    .sidebar { 
        transform: translateX(-100%); 
        transition: transform .3s ease; 
    }
    .sidebar.open { transform: translateX(0); }
    
    /* 汉堡菜单 - 固定在左上角，与顶部导航对齐 */
    .hamburger {
        display: flex !important;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1001;
        background: var(--navy);
        color: #fff;
        border: none;
        border-right: 1px solid rgba(255,255,255,.1);
        font-size: 20px;
        padding: 0;
        cursor: pointer;
    }
    
    .page-header h1 { font-size: 26px; }
    
    /* 顶部导航 - 固定在顶部，从44px开始 */
    .topbar {
        position: fixed !important;
        top: 0 !important;
        left: 44px !important;
        right: 0 !important;
        height: 44px;
        z-index: 100;
        justify-content: flex-start !important;
    }
    
    /* 顶部导航 - 显示全部7项 */
    .topbar-nav a { display: flex !important; }
}'''

content = content.replace(old_1025_1200, new_1025_1200)

# 3. 修复 <768px 手机断点
old_mobile = '''@media (max-width: 767px) {
    /* 侧边栏 - 隐藏，用汉堡菜单 */
    .sidebar { 
        transform: translateX(-100%); 
        transition: transform .3s ease; 
        width: 280px;
    }
    .sidebar.open { transform: translateX(0); }
    
    /* 汉堡菜单 - 固定在左上角 */
    .hamburger {
        display: flex !important;
        align-items: center;
        justify-content: center;
        width: 40px;
        height: 40px;
        position: fixed;
        top: 2px;
        left: 2px;
        z-index: 1001;
        background: var(--navy);
        color: #fff;
        border: none;
        font-size: 18px;
        padding: 0;
        border-radius: 8px;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,.3);
    }
    .hamburger:hover { background: var(--navy-light); }
    
    /* 主内容区 - 无边栏偏移 */
    .main-content { 
        margin-left: 0; 
        margin-top: 88px;
    }
    
    /* 顶部导航 - 固定在顶部，从44px开始（避开汉堡菜单） */
    .topbar {
        position: fixed;
        top: 0;
        left: 44px;
        right: 0;
        height: 44px;
        padding: 0;
        background: var(--navy);
        border-bottom: 2px solid var(--gold);
        z-index: 100;
        display: flex;
        justify-content: flex-start;
        overflow: hidden;
    }'''

new_mobile = '''@media (max-width: 767px) {
    /* 侧边栏 - 隐藏，用汉堡菜单 */
    .sidebar { 
        transform: translateX(-100%); 
        transition: transform .3s ease; 
        width: 280px;
    }
    .sidebar.open { transform: translateX(0); }
    
    /* 汉堡菜单 - 固定在左上角，与顶部导航对齐 */
    .hamburger {
        display: flex !important;
        align-items: center;
        justify-content: center;
        width: 44px;
        height: 44px;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1001;
        background: var(--navy);
        color: #fff;
        border: none;
        border-right: 1px solid rgba(255,255,255,.1);
        font-size: 20px;
        padding: 0;
        cursor: pointer;
    }
    .hamburger:hover { background: var(--navy-light); }
    
    /* 主内容区 - 无边栏偏移 */
    .main-content { 
        margin-left: 0; 
        margin-top: 44px;
    }
    
    /* 顶部导航 - 固定在顶部，从44px开始 */
    .topbar {
        position: fixed;
        top: 0;
        left: 44px;
        right: 0;
        height: 44px;
        padding: 0;
        background: var(--navy);
        border-bottom: 2px solid var(--gold);
        z-index: 100;
        display: flex;
        justify-content: flex-start;
        overflow: hidden;
    }'''

content = content.replace(old_mobile, new_mobile)

with open('pages/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS已统一修复！")
