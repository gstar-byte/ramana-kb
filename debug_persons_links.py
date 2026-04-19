import re

# 检查首页里和人物相关的所有链接
c = open(r'c:\Users\willp\WorkBuddy\20260410104230\pages\index.html', encoding='utf-8').read()

# 找所有 href
hrefs = re.findall(r'href=["\']([^"\']+)["\']', c)
david_related = [h for h in hrefs if 'david' in h.lower() or 'persons' in h.lower() or 'person' in h.lower()]
print("所有 david/persons 相关链接:")
for h in david_related:
    print(f"  {h}")

# 也看看导航里有什么
nav_section = re.search(r'(关键人物|key.persons|keyPersons)[^<]*</div', c, re.DOTALL)
if nav_section:
    print("\n导航人物区域:")
    print(nav_section.group(0)[:500])
