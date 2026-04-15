# -*- coding: utf-8 -*-
"""统一修复所有断点的导航栏样式"""

with open('pages/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复 900px-1024px 断点（缺失完整样式）
old_900_1024 = '''/* 900px - 1024px (Nest Hub 等设备)：显示5项 */
@media (min-width: 900px) and (max-width: 1024px) {
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

new_900_1024 = '''/* 900px - 1024px (Nest Hub 等设备)：显示5项 */
@media (min-width: 900px) and (max-width: 1024px) {
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

    /* 汉堡菜单 - 固定在左上角，与顶部导航完美对齐 */
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
        border-right: 1px solid var(--gold);
        border-bottom: 2px solid var(--gold);
        font-size: 20px;
        padding: 0;
        margin: 0;
        cursor: pointer;
        box-sizing: border-box;
    }

    .page-header h1 { font-size: 26px; }

    /* 顶部导航 - 固定在顶部，从44px开始 */
    .topbar {
        position: fixed !important;
        top: 0 !important;
        left: 44px !important;
        right: 0 !important;
        height: 44px !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 100;
        justify-content: flex-start !important;
        border-bottom: 2px solid var(--gold);
        box-sizing: border-box;
    }

    .topbar-nav {
        height: 42px;
        align-items: center;
        margin: 0;
        padding: 0;
    }

    .topbar-nav a {
        height: 42px;
        line-height: 42px;
        padding: 0 12px;
        font-size: 13px;
        margin: 0;
        border: none;
        border-right: 1px solid rgba(255,255,255,.1);
    }

    /* 顶部导航 - 显示首页、书籍、概念、问答、图谱，隐藏方法、人物 */
    .topbar-nav a:nth-child(4)   /* 方法 */
    { display: none !important; }
    .topbar-nav a:nth-child(6)   /* 人物 */
    { display: none !important; }
}'''

content = content.replace(old_900_1024, new_900_1024)

with open('pages/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS已完整修复！")
