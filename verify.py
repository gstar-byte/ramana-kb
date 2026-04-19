with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
print('总行数:', len(content.splitlines()))
qa_count = content.count('class="qa-item"')
print('qa-item数量:', qa_count)