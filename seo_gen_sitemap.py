"""
SEO Fix Phase 2: 生成完整 sitemap.xml
扫描 pages/ 下所有 HTML 文件，排除 _template.html 等模板文件
输出到 pages/sitemap.xml
"""
import os

BASE_URL = "https://ramanamaharshi.space"
PAGES_DIR = "c:/Users/willp/WorkBuddy/20260410104230/pages"

# 排除的文件（模板、非页面）
EXCLUDE_FILES = {
    "_template.html",
    "sitemap.html",
}

# 排除的目录
EXCLUDE_DIRS = set()

def get_url_path(filepath):
    """将文件路径转换为URL路径（去掉 .html 后缀，处理 index.html）"""
    rel = os.path.relpath(filepath, PAGES_DIR).replace(os.sep, "/")
    
    # 去掉 .html 后缀（Vercel cleanUrls）
    if rel.endswith(".html"):
        rel = rel[:-5]
    
    # index.html → 目录根路径
    if rel.endswith("/index"):
        rel = rel[:-6] or "/"
    
    # 根目录 index.html → /
    if rel == "" or rel == "/":
        return "/"
    
    # 确保以 / 开头
    if not rel.startswith("/"):
        rel = "/" + rel
    
    return rel


def gen_sitemap():
    urls = []
    
    for root, dirs, files in os.walk(PAGES_DIR):
        # 排除不需要的目录
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for fname in sorted(files):
            if not fname.endswith(".html"):
                continue
            if fname in EXCLUDE_FILES:
                continue
            
            fpath = os.path.join(root, fname)
            url_path = get_url_path(fpath)
            urls.append(url_path)
    
    # 生成 XML
    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for url_path in sorted(urls):
        full_url = BASE_URL + url_path
        xml_lines.append(f'  <url>')
        xml_lines.append(f'    <loc>{full_url}</loc>')
        xml_lines.append(f'  </url>')
    
    xml_lines.append('</urlset>')
    
    output = os.path.join(PAGES_DIR, "sitemap.xml")
    with open(output, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    
    print(f"✅ Sitemap 生成完成！共 {len(urls)} 个 URL")
    print(f"   输出文件: {output}")
    print(f"\n前20个URL:")
    for u in sorted(urls)[:20]:
        print(f"   {BASE_URL}{u}")
    if len(urls) > 20:
        print(f"   ... 还有 {len(urls) - 20} 个")


if __name__ == "__main__":
    gen_sitemap()
