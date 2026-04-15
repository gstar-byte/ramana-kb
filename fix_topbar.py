# -*- coding: utf-8 -*-
"""修复CSS中的topbar和main-content样式"""

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
    }
    
    /* 顶部导航 - 显示全部7项 */
    .topbar-nav a { display: flex !important; }
}'''

content = content.replace(old_1025_1200, new_1025_1200)

with open('pages/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS已修复！")
