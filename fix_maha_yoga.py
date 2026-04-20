#!/usr/bin/env python3
"""修复 maha-yoga-ch1~5.html 的问题：
1. 删除重复面包屑（第一个错的）
2. 修正侧边栏链接路径
3. 补上 GA4 代码（从 be-as-you-are-ch1.html 复制）
"""
import os, re

BASE = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books'

# GA4代码块（从 be-as-you-are-ch1.html 复制）
GA4 = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MYFWHFPSYB');
</script>

'''

# JSON-LD
JSONLD = '''  <!-- SEO JSON-LD Structured Data -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "拉玛那马哈希知识库",
      "item": "https://ramanamaharshi.space/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "书籍",
      "item": "https://ramanamaharshi.space/books"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "大瑜伽",
      "item": "https://ramanamaharshi.space/books/maha-yoga"
    }
  ]
}
</script>
'''

chapters = [
    ('maha-yoga-ch1.html', '第一章：阿鲁那佳拉的圣者', 'maha-yoga-ch2.html', 'ch2'),
    ('maha-yoga-ch2.html', '第二章：我们幸福吗？', 'maha-yoga-ch3.html', 'ch3'),
    ('maha-yoga-ch3.html', '第三章：无明', 'maha-yoga-ch4.html', 'ch4'),
    ('maha-yoga-ch4.html', '第四章：哲学与证据', 'maha-yoga-ch5.html', 'ch5'),
    ('maha-yoga-ch5.html', '第五章：世界', 'maha-yoga.html', 'book'),
]

for fname, title, next_link, next_label in chapters:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. 修正第一个错误的面包屑（指向 be-as-you-are 的那个）
    old_crumb = '''                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> /
                    <a href="../books/index.html">书籍</a> /
                    <a href="be-as-you-are.html">走向静默，如你本来</a> /
                    <span>第一章：我是谁？</span>
                </nav>'''
    html = html.replace(old_crumb, '')

    # 2. 替换 GA4 代码块（如果有重复或缺失）
    old_ga4 = re.search(
        r'<!--\s*Google tag.*?</script>\s*',
        html, re.DOTALL
    )
    if old_ga4:
        # 检查是否包含 G-MYFWHFPSYB
        if 'G-MYFWHFPSYB' not in old_ga4.group():
            html = html[:old_ga4.start()] + GA4.rstrip() + '\n' + html[old_ga4.end():]
    else:
        # 插入 GA4 到 </head> 之前
        html = html.replace('</head>', GA4 + '</head>')

    # 3. 补 JSON-LD
    if 'G-MYFWHFPSYB' in html and 'BreadcrumbList' not in html:
        html = html.replace('</head>', JSONLD + '\n</head>')

    # 4. 修正侧边栏"其他书籍"中的路径错误
    html = html.replace(
        '<a href="index.html" class="sidebar-item">📚 书籍总览</a>',
        '<a href="../books/index.html" class="sidebar-item">📚 书籍总览</a>'
    )
    html = html.replace(
        '<a href="../books/be-as-you-are.html" class="sidebar-item">📖 大瑜伽</a>',
        '<a href="maha-yoga.html" class="sidebar-item">📖 大瑜伽</a>'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'✓ 修复: {fname}')

print('\n全部完成！')
