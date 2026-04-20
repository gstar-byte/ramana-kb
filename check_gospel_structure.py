import os

files = [
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch9.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch10.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch11.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch12.html',
    r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maharshi-gospel-ch13.html',
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    name = os.path.basename(f)
    body = content.count('</body>')
    html_end = content.count('</html>')
    cw_open = content.count('content-wrapper')
    # check if footer is inside or outside content-wrapper
    cw_idx = content.rfind('content-wrapper')
    footer_idx = content.rfind('site-footer')
    print(name, '| </body>:', body, '</html>:', html_end,
          '| content-wrapper mentions:', cw_open,
          '| footer after last cw:', footer_idx > cw_idx)
