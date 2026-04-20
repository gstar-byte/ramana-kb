# -*- coding: utf-8 -*-
f = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/collected-works.html'
c = open(f, encoding='utf-8').read()
checks = [
    ('章节1可点击', 'href="collected-works-self-enquiry.html" class="chapter-card"' in c),
    ('章节2可点击', 'href="collected-works-whoami.html" class="chapter-card"' in c),
    ('章节3可点击', 'href="collected-works-upadesa-saram.html" class="chapter-card"' in c),
    ('章节4可点击', 'href="collected-works-upadesa-manjari.html" class="chapter-card"' in c),
    ('page-nav上一本', '上一本' in c),
    ('page-nav下一本', '下一本' in c),
    ('无重复footer', c.count('<footer class="site-footer">') == 1),
    ('html闭合', '</html>' in c),
    ('body闭合', c.rstrip().endswith('</html>')),
    ('无游离chapter-card', '<div class="chapter-card">' not in c),
]
for name, ok in checks:
    print(('OK ' if ok else 'FAIL') + name)
print('总长度:', len(c), '字符')
