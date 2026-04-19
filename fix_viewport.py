import re, glob

CORRECT_VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
BAD_VIEWPORT_RE = re.compile(r'<meta name="viewport" content="width=device-width, initial-scale=1\.0[^"]*"[^>]*>')

count = 0
for f in glob.glob('c:/Users/willp/WorkBuddy/20260410104230/pages/**/*.html', recursive=True):
    with open(f, encoding='utf-8') as fh:
        content = fh.read()

    if BAD_VIEWPORT_RE.search(content):
        new_content = BAD_VIEWPORT_RE.sub(CORRECT_VIEWPORT, content)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        count += 1
        print(f'修复: {f}')

print(f'\n共修复 {count} 个文件')
