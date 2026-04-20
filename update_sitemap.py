"""更新 sitemap.xml 添加新页面"""
import re

sitemap = open('pages/sitemap.xml', encoding='utf-8').read()

# 1. spiritual-stories-ch3.html 插入到 ch2 之后
ch3_entry = """  <url>
    <loc>https://ramanamaharshi.space/books/spiritual-stories-ch3.html</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>"""

sitemap = sitemap.replace(
    """  <url>
    <loc>https://ramanamaharshi.space/books/spiritual-stories-ch2.html</loc>
    <lastmod>2026-04-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://ramanamaharshi.space/books/surpassing-love-ch1.html</loc>""",
    """  <url>
    <loc>https://ramanamaharshi.space/books/spiritual-stories-ch2.html</loc>
    <lastmod>2026-04-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
""" + ch3_entry + """
  <url>
    <loc>https://ramanamaharshi.space/books/surpassing-love-ch1.html</loc>"""
)

# 2. 添加新概念页（找到现有概念附近）
new_concepts = [
    ('<loc>https://ramanamaharshi.space/concepts/viveka.html',
     '<loc>https://ramanamaharshi.space/concepts/vairagya.html'),
    ('<loc>https://ramanamaharshi.space/concepts/vairagya.html',
     '<loc>https://ramanamaharshi.space/concepts/dhyana.html'),
    ('<loc>https://ramanamaharshi.space/concepts/dhyana.html',
     '<loc>https://ramanamaharshi.space/concepts/advaita.html'),
    ('<loc>https://ramanamaharshi.space/concepts/advaita.html',
     '<loc>https://ramanamaharshi.space/concepts/shiva.html'),
    ('<loc>https://ramanamaharshi.space/concepts/shiva.html',
     '<loc>https://ramanamaharshi.space/concepts/shakti.html'),
    ('<loc>https://ramanamaharshi.space/concepts/shakti.html',
     '<loc>https://ramanamaharshi.space/concepts/mano.html'),
    ('<loc>https://ramanamaharshi.space/concepts/mano.html',
     '<loc>https://ramanamaharshi.space/concepts/nishtha.html'),
    ('<loc>https://ramanamaharshi.space/concepts/nishtha.html',
     '<loc>https://ramanamaharshi.space/concepts/sharanagati.html'),
    ('<loc>https://ramanamaharshi.space/concepts/sharanagati.html',
     '<loc>https://ramanamaharshi.space/concepts/viveka.html'),
    ('<loc>https://ramanamaharshi.space/concepts/viveka.html',
     '<loc>https://ramanamaharshi.space/concepts/prana.html'),
]

concept_entry_template = """  <url>
    <loc>{url}</loc>
    <lastmod>2026-04-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""

# Insert after the URL of the previous concept
# But the previous ones don't exist yet, so we need to find a reference point
# Let's find the last existing concept in sitemap
existing_concepts = re.findall(r'concepts/([a-z0-9-]+)\.html', sitemap)
print('现有概念:', existing_concepts[:5], '...')

# Find the last entry - insert after the last concept
# Let's find a known existing URL to insert before
insert_point = sitemap.find('</url>\n  <url>\n    <loc>https://ramanamaharshi.space/books/crumbs-ch1.html</loc>')

if insert_point > 0:
    concept_insert = ''
    for url in [
        'https://ramanamaharshi.space/concepts/vairagya.html',
        'https://ramanamaharshi.space/concepts/dhyana.html',
        'https://ramanamaharshi.space/concepts/advaita.html',
        'https://ramanamaharshi.space/concepts/shiva.html',
        'https://ramanamaharshi.space/concepts/shakti.html',
        'https://ramanamaharshi.space/concepts/mano.html',
        'https://ramanamaharshi.space/concepts/nishtha.html',
        'https://ramanamaharshi.space/concepts/sharanagati.html',
        'https://ramanamaharshi.space/concepts/viveka.html',
        'https://ramanamaharshi.space/concepts/prana.html',
    ]:
        concept_insert += concept_entry_template.format(url=url) + '\n'

    sitemap = sitemap[:insert_point] + concept_insert + sitemap[insert_point:]
    print('已添加10个新概念到sitemap.xml')
else:
    print('未找到插入点 crumbs-ch1')

# 更新sitemap最后修改时间
sitemap = sitemap.replace('  <lastmod>2026-04-17</lastmod>', '  <lastmod>2026-04-20</lastmod>')

open('pages/sitemap.xml', 'w', encoding='utf-8').write(sitemap)
print('sitemap.xml 更新完成')
