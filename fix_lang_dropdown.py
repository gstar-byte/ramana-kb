#!/usr/bin/env python3
"""
将三站多语言切换按钮改为下拉菜单
- 简体根目录 (pages/): 当前语言显示为 "简▾"，下拉有 繁体中文 / English
- en英文版 (pages/en/): 当前语言显示为 "EN▾"，下拉有 简体中文 / 繁體中文
- zh-TW繁中版 (pages/zh-TW/): 当前语言显示为 "繁▾"，下拉有 简体中文 / English
"""
import os
import re

# CSS + JS 注入到 </style> 前（如果没有style则注入到</head>前）
DROPDOWN_STYLE = """
/* ===== 语言下拉菜单 ===== */
.lang-dropdown{position:relative;display:inline-flex;align-items:center;border-left:1px solid rgba(255,255,255,.3);margin-left:0;}
.lang-dropdown-btn{background:rgba(255,255,255,.1);border:none;color:#e2e8f0;font-size:13px;font-weight:600;cursor:pointer;padding:5px 10px;border-radius:4px;white-space:nowrap;display:flex;align-items:center;gap:3px;transition:background .15s;}
.lang-dropdown-btn:hover{background:rgba(255,255,255,.2);}
.lang-dropdown-menu{display:none;position:absolute;top:calc(100% + 6px);right:0;min-width:120px;background:#1e293b;border:1px solid rgba(255,255,255,.15);border-radius:6px;box-shadow:0 8px 24px rgba(0,0,0,.4);z-index:9999;overflow:hidden;}
.lang-dropdown.open .lang-dropdown-menu{display:block;}
.lang-dropdown-menu a{display:block;padding:8px 16px;color:#cbd5e1;font-size:13px;text-decoration:none;white-space:nowrap;transition:background .1s;}
.lang-dropdown-menu a:hover{background:rgba(255,255,255,.1);color:#fff;}
.lang-dropdown-menu a.current{color:#f59e0b;pointer-events:none;}
/* ======================= */
"""

DROPDOWN_JS = """
<script>
(function(){
  document.addEventListener('click',function(e){
    var dd=e.target.closest('.lang-dropdown');
    document.querySelectorAll('.lang-dropdown.open').forEach(function(el){
      if(el!==dd) el.classList.remove('open');
    });
    if(dd) dd.classList.toggle('open');
  });
})();
</script>
"""

def inject_style_js(content, style_snippet, js_snippet):
    """注入CSS和JS"""
    if '/* ===== 语言下拉菜单 =====' not in content:
        if '</style>' in content:
            content = content.replace('</style>', style_snippet + '</style>', 1)
        elif '</head>' in content:
            content = content.replace('</head>', '<style>' + style_snippet + '</style></head>', 1)
    if '<script>\n(function(){\n  document.addEventListener' not in content:
        content = content.replace('</body>', js_snippet + '</body>', 1)
        if js_snippet not in content:
            content = content + js_snippet
    return content

# ==========================================
# 简体版：有两种模式
# 模式A（大多数页面）: 只有"繁"按钮（onclick跳转zh-TW）
# 模式B（首页等）: 有"EN"和"繁"两个按钮
# ==========================================

# 简体版下拉HTML生成
def make_zh_cn_dropdown(en_url, tw_url):
    return (
        '<div class="lang-dropdown">'
        '<button class="lang-dropdown-btn">简 ▾</button>'
        '<div class="lang-dropdown-menu">'
        f'<a href="{tw_url}">繁體中文</a>'
        f'<a href="{en_url}">English</a>'
        '</div></div>'
    )

# en版下拉HTML生成
def make_en_dropdown(cn_url, tw_url):
    return (
        '<div class="lang-dropdown">'
        '<button class="lang-dropdown-btn">EN ▾</button>'
        '<div class="lang-dropdown-menu">'
        f'<a href="{cn_url}">简体中文</a>'
        f'<a href="{tw_url}">繁體中文</a>'
        '</div></div>'
    )

# zh-TW版下拉HTML生成
def make_zh_tw_dropdown(cn_url, en_url):
    return (
        '<div class="lang-dropdown">'
        '<button class="lang-dropdown-btn">繁 ▾</button>'
        '<div class="lang-dropdown-menu">'
        f'<a href="{cn_url}">简体中文</a>'
        f'<a href="{en_url}">English</a>'
        '</div></div>'
    )

# ==============================
# 处理简体版（根目录）
# ==============================
def process_zhcn_file(filepath, content):
    # 模式B: 有两个lang-toggle按钮 (EN + 繁)
    # <a href="/en/" class="lang-toggle"...>EN</a><a href="/zh-TW/" class="lang-toggle"...>繁</a>
    pat_b = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*href="(/en/)"[^>]*>EN</a>'
        r'\s*<a [^>]*class="lang-toggle"[^>]*href="(/zh-TW/)"[^>]*>繁</a>'
    )
    # 反向顺序版
    pat_b2 = re.compile(
        r'<a [^>]*href="(/en/)"[^>]*class="lang-toggle"[^>]*>EN</a>'
        r'\s*<a [^>]*href="(/zh-TW/)"[^>]*class="lang-toggle"[^>]*>繁</a>'
    )
    
    replaced = False
    
    # 尝试模式B (EN在前)
    m = pat_b.search(content)
    if m:
        dropdown = make_zh_cn_dropdown(m.group(1), m.group(2))
        content = content[:m.start()] + dropdown + content[m.end():]
        replaced = True
    
    if not replaced:
        m = pat_b2.search(content)
        if m:
            dropdown = make_zh_cn_dropdown(m.group(1), m.group(2))
            content = content[:m.start()] + dropdown + content[m.end():]
            replaced = True
    
    # 模式A: 只有"繁"按钮
    # <a href="#" class="lang-toggle"... onclick="location.href='/zh-TW/'+...">繁</a>
    pat_a = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*onclick="[^"]*location\.href\s*=\s*[^"]*zh-TW[^"]*"[^>]*>繁</a>'
    )
    if not replaced:
        m = pat_a.search(content)
        if m:
            # 从onclick中提取路径模式
            onclick = m.group(0)
            # 用动态URL
            dropdown = make_zh_cn_dropdown(
                "javascript:void(0)' onclick=\"location.href=location.pathname.replace(/^\\/en\\//,'/').replace(/^\\/zh-TW\\//,'/')+location.pathname.replace(/^.*\\//,'')&&(location.href='/en/'+location.pathname.replace(/^\\/zh-TW\\//,'').replace(/^\\/en\\//,'')),false",
                "javascript:void(0)"
            )
            # 简单处理：生成动态版本
            dropdown = (
                '<div class="lang-dropdown">'
                '<button class="lang-dropdown-btn">简 ▾</button>'
                '<div class="lang-dropdown-menu">'
                '<a href="#" onclick="location.href=\'/zh-TW/\'+location.pathname.substring(1);return false;">繁體中文</a>'
                '<a href="#" onclick="location.href=\'/en/\'+location.pathname.substring(1);return false;">English</a>'
                '</div></div>'
            )
            content = content[:m.start()] + dropdown + content[m.end():]
            replaced = True
    
    # 还有 "繁" 在前，"EN" 在后的模式
    # <a href="/zh-TW/" class="lang-toggle"...>繁</a>...<a href="/en/" class="lang-toggle"...>EN</a>
    pat_tw_en = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*href="(/zh-TW/)"[^>]*>[繁繁]</a>'
        r'.*?'
        r'<a [^>]*class="lang-toggle"[^>]*href="(/en/)"[^>]*>EN</a>',
        re.DOTALL
    )
    if not replaced:
        m = pat_tw_en.search(content)
        if m:
            dropdown = make_zh_cn_dropdown(m.group(2), m.group(1))
            content = content[:m.start()] + dropdown + content[m.end():]
            replaced = True
    
    return content, replaced


# ==============================
# 处理en版
# ==============================
def process_en_file(filepath, content):
    # en版首页: <a href="/" class="lang-toggle"...>简</a><a href="/zh-TW/" class="lang-toggle"...>繁</a>
    pat_index = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*href="(/)"[^>]*>简</a>'
        r'\s*<a [^>]*class="lang-toggle"[^>]*href="(/zh-TW/)"[^>]*>繁</a>'
    )
    # en版书籍页: onclick跳转 ../../books/xxx.html
    pat_onclick = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*onclick="[^"]*"[^>]*>[中中]</a>'
    )
    
    replaced = False
    m = pat_index.search(content)
    if m:
        dropdown = make_en_dropdown(m.group(1), m.group(2))
        content = content[:m.start()] + dropdown + content[m.end():]
        replaced = True
    
    if not replaced:
        m = pat_onclick.search(content)
        if m:
            onclick_text = m.group(0)
            # 提取目标路径
            href_match = re.search(r"location\.href='([^']+)'", onclick_text)
            if href_match:
                cn_path = href_match.group(1)
                # 构造zh-TW路径: 从en路径推断
                # en页面通常在 en/books/xxx.html，cn在 books/xxx.html，TW在 zh-TW/books/xxx.html
                tw_path = cn_path.replace('../../', '/zh-TW/').replace('../', '/zh-TW/')
                dropdown = (
                    '<div class="lang-dropdown">'
                    '<button class="lang-dropdown-btn">EN ▾</button>'
                    '<div class="lang-dropdown-menu">'
                    f'<a href="#" onclick="location.href=\'{cn_path}\';return false;">简体中文</a>'
                    f'<a href="#" onclick="location.href=\'{tw_path}\';return false;">繁體中文</a>'
                    '</div></div>'
                )
            else:
                dropdown = make_en_dropdown('/', '/zh-TW/')
            content = content[:m.start()] + dropdown + content[m.end():]
            replaced = True
    
    return content, replaced


# ==============================
# 处理zh-TW版
# ==============================
def process_zhtw_file(filepath, content):
    # zh-TW首页: <a href="/" class="lang-toggle"...>簡</a><a href="/en/" class="lang-toggle"...>EN</a>
    pat_index = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*href="(/)"[^>]*>[简簡]</a>'
        r'\s*<a [^>]*class="lang-toggle"[^>]*href="(/en/)"[^>]*>EN</a>'
    )
    # zh-TW书籍页: onclick跳转，替换路径中的 /zh-TW/ -> /
    pat_onclick = re.compile(
        r'<a [^>]*class="lang-toggle"[^>]*onclick="[^"]*zh-TW[^"]*"[^>]*>[簡简]</a>'
    )
    
    replaced = False
    m = pat_index.search(content)
    if m:
        dropdown = make_zh_tw_dropdown(m.group(1), m.group(2))
        content = content[:m.start()] + dropdown + content[m.end():]
        replaced = True
    
    if not replaced:
        m = pat_onclick.search(content)
        if m:
            dropdown = (
                '<div class="lang-dropdown">'
                '<button class="lang-dropdown-btn">繁 ▾</button>'
                '<div class="lang-dropdown-menu">'
                '<a href="#" onclick="location.href=location.pathname.replace(\'/zh-TW/\',\'/\');return false;">简体中文</a>'
                '<a href="#" onclick="location.href=location.pathname.replace(\'/zh-TW/\',\'/en/\');return false;">English</a>'
                '</div></div>'
            )
            content = content[:m.start()] + dropdown + content[m.end():]
            replaced = True
    
    return content, replaced


# ==============================
# 主处理逻辑
# ==============================
def process_directory(base_dir, mode):
    """
    mode: 'zhcn' | 'en' | 'zhtw'
    """
    total = 0
    changed = 0
    skipped = 0
    
    for root, dirs, files in os.walk(base_dir):
        # 简体版时跳过 en/ 和 zh-TW/ 子目录
        if mode == 'zhcn':
            dirs[:] = [d for d in dirs if d not in ('en', 'zh-TW', 'node_modules', '.workbuddy')]
        
        for fname in files:
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            if 'lang-toggle' not in content:
                continue
            
            total += 1
            
            if mode == 'zhcn':
                new_content, ok = process_zhcn_file(fpath, content)
            elif mode == 'en':
                new_content, ok = process_en_file(fpath, content)
            else:  # zhtw
                new_content, ok = process_zhtw_file(fpath, content)
            
            if ok and new_content != content:
                new_content = inject_style_js(new_content, DROPDOWN_STYLE, DROPDOWN_JS)
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                changed += 1
            else:
                skipped += 1
    
    return total, changed, skipped


BASE = 'F:/26年4月/kb01/pages'

print("=== 处理简体版（根目录）===")
t, c, s = process_directory(BASE, 'zhcn')
print(f"  扫描: {t}, 修改: {c}, 跳过: {s}")

print("=== 处理英文版（en/）===")
t, c, s = process_directory(os.path.join(BASE, 'en'), 'en')
print(f"  扫描: {t}, 修改: {c}, 跳过: {s}")

print("=== 处理繁中版（zh-TW/）===")
t, c, s = process_directory(os.path.join(BASE, 'zh-TW'), 'zhtw')
print(f"  扫描: {t}, 修改: {c}, 跳过: {s}")

print("\n✅ 全部完成！")
