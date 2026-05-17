#!/usr/bin/env python3
"""
英文版PDF批量处理脚本
从英文PDF提取文本，生成英文版HTML
"""

import os
import re
import fitz  # PyMuPDF
from pathlib import Path

# 配置
SOURCE_DIR = Path("ebooks")
OUTPUT_DIR = Path("pages/en/books")
TEMPLATE_FILE = Path("pages/books/be-as-you-are-ch1.html")

# PDF与书籍slug映射（文件名关键字 -> slug）
PDF_SLUG_MAP = {
    "Be As You Are": "be-as-you-are",
    "Timeless in Time": "timeless",
    "A Search in Secret India": "search-secret-india",
    "Teachings of Ramana Maharshi in His Own Words": "teachings",
    "Maharshis Gospel": "maharshi-gospel",
    "Face to Face": "face-to-face",
    "Gems from": "gems",
    "Guru Vachaka Kovai": "guru-vachaka-kovai",
    "Maha Yoga": "maha-yoga",
    "Surpassing Love": "surpassing-love",
    "Crumbs from": "crumbs",
    "Reflections On Talks": "reflections",
    "S.S.Cohen-Guru Ramana": "guru-ramana",
    "S.S. Cohen-Reflections": "reflections",  # 这个先匹配
    "Spiritual stoires": "spiritual-stories",
    "Spiritual stories": "spiritual-stories",
    "Talks with": "talks",
    "Collected Works": "collected-works",
    "day by day": "day-by-day",
    "day-by-day": "day-by-day",
}


def extract_pdf_info(pdf_path):
    """从PDF文件名提取书名和slug"""
    filename = os.path.basename(pdf_path).lower()

    # 跳过中文PDF
    if any(ord(c) > 127 for c in os.path.basename(pdf_path)):
        return None, None

    # 按优先级匹配（更具体的先匹配）
    priority_keys = [
        "S.S. Cohen-Reflections",
        "S.S.Cohen-Guru Ramana",
        "Reflections On Talks",
        "Be As You Are",
        "Timeless in Time",
        "A Search in Secret India",
        "Teachings of Ramana Maharshi in His Own Words",
        "Maharshis Gospel",
        "Face to Face",
        "Gems from",
        "Guru Vachaka Kovai",
        "Maha Yoga",
        "Surpassing Love",
        "Crumbs from",
        "Spiritual stoires",
        "Spiritual stories",
        "Talks with",
        "Collected Works",
        "day by day",
        "day-by-day",
    ]

    for key in priority_keys:
        if key.lower() in filename:
            slug = PDF_SLUG_MAP.get(key)
            if slug:
                # 返回标准书名
                book_names = {
                    "be-as-you-are": "Be As You Are",
                    "timeless": "Timeless in Time",
                    "search-secret-india": "A Search in Secret India",
                    "teachings": "Teachings of Ramana Maharshi",
                    "maharshi-gospel": "Maharshi's Gospel",
                    "face-to-face": "Face to Face with Sri Ramana Maharshi",
                    "gems": "Gems from Bhagavan",
                    "guru-vachaka-kovai": "Guru Vachaka Kovai",
                    "maha-yoga": "Maha Yoga",
                    "surpassing-love": "Surpassing Love and Grace",
                    "crumbs": "Crumbs from His Table",
                    "reflections": "Reflections On Talks",
                    "guru-ramana": "Guru Ramana",
                    "spiritual-stories": "Spiritual Stories",
                    "talks": "Talks with Sri Ramana Maharshi",
                    "collected-works": "Collected Works",
                    "day-by-day": "Day by Day with Bhagavan",
                }
                return book_names.get(slug, key), slug

    return None, None

    # 从文件名提取
    basename = os.path.basename(pdf_path)
    for name in PDF_BOOK_MAP.keys():
        if name.lower().replace(" ", "") in basename.lower().replace(" ", ""):
            return name

    return None


def extract_chapters(text):
    """按章节分割文本"""
    # 常见的章节标题模式
    chapter_patterns = [
        r'\n([A-Z][A-Z\s]+)\n',  # 全大写标题
        r'\n([IVX]+\.?\s+[^\n]+)\n',  # 罗马数字 + 标题
        r'\n(\d+\.?\s+[^\n]+)\n',  # 数字 + 标题
    ]

    chapters = []
    lines = text.split('\n')

    current_chapter = {"title": "Introduction", "content": []}
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 检测是否为章节标题
        is_chapter = False
        for pattern in chapter_patterns:
            if re.match(pattern, f'\n{line}\n'):
                # 保存上一章节
                if current_chapter["content"]:
                    chapters.append(current_chapter)
                current_chapter = {"title": line.strip(), "content": []}
                is_chapter = True
                break

        if not is_chapter:
            current_chapter["content"].append(line)

    # 保存最后一章
    if current_chapter["content"]:
        chapters.append(current_chapter)

    return chapters


def clean_text(text):
    """清理文本"""
    # 移除多余空白
    text = re.sub(r'\n{3,}', '\n\n', text)
    # 移除页码（常见格式）
    text = re.sub(r'\n\d+\n', '\n', text)
    return text.strip()


def extract_pdf_text(pdf_path):
    """从PDF提取完整文本"""
    doc = fitz.open(pdf_path)
    pages_text = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        # 清理页面文本
        text = clean_text(text)
        if text:
            pages_text.append({
                'page_num': page_num + 1,
                'text': text
            })

    doc.close()
    return pages_text


def get_all_pdf_files():
    """获取所有PDF文件"""
    pdf_files = []
    for f in os.listdir(SOURCE_DIR):
        if f.lower().endswith('.pdf'):
            pdf_files.append(SOURCE_DIR / f)
    return sorted(pdf_files)


def process_all_pdfs():
    """处理所有PDF"""
    pdf_files = get_all_pdf_files()
    print(f"找到 {len(pdf_files)} 个PDF文件\n")

    results = []
    for pdf_path in pdf_files:
        print(f"处理: {pdf_path.name}")
        book_name, book_slug = extract_pdf_info(str(pdf_path))
        if book_name and book_slug:
            print(f"  -> 书名: {book_name}")
            print(f"  -> Slug: {book_slug}")

            # 提取文本
            pages = extract_pdf_text(str(pdf_path))
            print(f"  -> 页数: {len(pages)}")

            if len(pages) == 0:
                print(f"  -> 警告: 无文本内容（可能是扫描版）")
                continue

            # 生成HTML
            output_path = OUTPUT_DIR / f"{book_slug}.html"
            generate_book_html(book_slug, book_name, pages, output_path)
            print(f"  -> 输出: {output_path}\n")

            results.append({
                'pdf': pdf_path.name,
                'book': book_name,
                'slug': book_slug,
                'pages': len(pages),
                'output': str(output_path)
            })
        else:
            print(f"  -> 无法识别书名，跳过\n")

    return results


def generate_book_html(slug, title, pages, output_path):
    """生成书籍HTML"""
    # 合并所有页面文本
    full_text = "\n\n".join([p['text'] for p in pages])

    # 创建HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} by Sri Ramana Maharshi - Complete teachings and wisdom from the great sage of Arunachala.">
    <meta name="keywords" content="Ramana Maharshi, Arunachala, Self-realization, Advaita Vedanta, spiritual teachings">
    <title>{title} | Sri Ramana Maharshi</title>

    <link rel="canonical" href="https://ramanamaharshi.space/en/books/{slug}.html">
    <link rel="alternate" hreflang="zh-CN" href="https://ramanamaharshi.space/books/{slug}.html">
    <link rel="alternate" hreflang="zh-TW" href="https://ramanamaharshi.space/zh-TW/books/{slug}.html">
    <link rel="alternate" hreflang="en" href="https://ramanamaharshi.space/en/books/{slug}.html">

    <link rel="preconnect" href="https://www.google-analytics.com" crossorigin>
    <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-MYFWHFPSYB');
    </script>
    <link rel="stylesheet" href="../styles.min.css">
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">

    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <a href="../index.html" class="logo">🙏 Sri Ramana KB</a>
            <button class="sidebar-close-btn" title="Close sidebar">◀</button>
        </div>

        <div class="search-box">
            <input type="text" id="search-input" placeholder="Search..." autocomplete="off">
            <div id="search-results"></div>
        </div>

        <div class="sidebar-section">
            <div class="sidebar-section-title">📚 Core Index</div>
            <div class="sidebar-items">
                <a href="index.html" class="sidebar-item"><span class="emoji">📖</span> Books <span class="count">17</span></a>
                <a href="../concepts/index.html" class="sidebar-item"><span class="emoji">🔮</span> Concepts</a>
                <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> Methods</a>
                <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> Q&A</a>
                <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> Persons</a>
                <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> Knowledge Graph</a>
            </div>
        </div>

        <div class="sidebar-section">
            <div class="sidebar-section-title">📖 Current Book</div>
            <div class="sidebar-items">
                <a href="{slug}.html" class="sidebar-item active">📖 {title}</a>
            </div>
        </div>
    </aside>

    <main class="main-content">
        <header class="topbar">
            <button class="sidebar-open-btn" title="Expand sidebar">▶</button>
            <div class="topbar-left">
                <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                <span class="topbar-title">📖 {title}</span>
            </div>
            <nav class="topbar-nav topbar-full">
                <a href="../index.html">Home</a>
                <a href="index.html" class="active">Books</a>
                <a href="../concepts/index.html">Concepts</a>
                <a href="../methods/index.html">Methods</a>
                <a href="../qa/index.html">Q&A</a>
                <a href="../persons/index.html">Persons</a>
                <a href="../graph.html">Graph</a>
                <a href="#" class="lang-toggle" style="border-left:1px solid rgba(255,255,255,.3);" title="Switch to Chinese" onclick="location.href='../../books/{slug}.html';return false;">中</a>
            </nav>
        </header>

        <div class="content-wrapper">
            <header class="page-header">
                <h1>📖 {title}</h1>
                <p style="color:var(--text-muted);margin-top:0.5rem;">Teachings of Sri Ramana Maharshi</p>
            </header>

            <article class="content book-content">
                <div class="book-text">
'''

    # 添加文本内容
    for para in full_text.split('\n\n'):
        para = para.strip()
        if para:
            # 处理引号
            para = para.replace('"', '"').replace('"', '"').replace(''', "'").replace(''', "'")
            html += f'<p>{para}</p>\n\n'

    html += '''                </div>
            </article>
        </div>
    </main>

    <script src="../bundle.min.js"></script>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"    生成HTML完成: {output_path}")


if __name__ == "__main__":
    print("=" * 60)
    print("Ramana Knowledge Base - English PDF Processor")
    print("=" * 60)
    print()

    results = process_all_pdfs()

    print("\n" + "=" * 60)
    print(f"处理完成! 共处理 {len(results)} 本书")
    print("=" * 60)

    for r in results:
        print(f"  {r['book']}: {r['pages']} pages")
