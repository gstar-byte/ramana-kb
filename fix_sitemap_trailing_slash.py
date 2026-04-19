import re, glob

# 更新 sitemap.xml 中的 URL，加上 trailing slash
sitemap = r'c:\Users\willp\WorkBuddy\20260410104230\pages\sitemap.xml'
with open(sitemap, encoding='utf-8') as f:
    content = f.read()

# 找所有 loc 中的 URL，给非首页、非锚点的 URL 加上斜杠
# 但首页 / 和其他分类索引页（如 /books、/persons）不加斜杠
def add_trailing_slash(match):
    loc = match.group(1)
    # 首页、索引页不加斜杠
    no_slash_endings = ['/books', '/concepts', '/persons', '/methods', '/qa', '/graph', '/sitemap', '/index']
    if any(loc.endswith(x) for x in no_slash_endings):
        return f'<loc>{loc}</loc>'
    # 其他页面加斜杠
    if not loc.endswith('/'):
        return f'<loc>{loc}/</loc>'
    return match.group(0)

new_content = re.sub(r'<loc>(https?://[^<]+)</loc>', add_trailing_slash, content)

with open(sitemap, 'w', encoding='utf-8') as f:
    f.write(new_content)

# 验证
with open(sitemap, encoding='utf-8') as f:
    c = f.read()

# 检查几个关键 URL
samples = re.findall(r'<loc>([^<]+)</loc>', c)
for s in samples[:20]:
    print(s)
print(f'\n共 {len(samples)} 个URL')
