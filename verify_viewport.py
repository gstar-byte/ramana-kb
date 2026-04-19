import re
c = open(r'c:\Users\willp\WorkBuddy\20260410104230\pages\index.html', encoding='utf-8').read()
vp = re.search(r'<meta name="viewport"[^>]+>', c)
print('viewport:', vp.group(0) if vp else 'NOT FOUND')
