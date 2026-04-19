with open('c:/Users/willp/WorkBuddy/20260410104230/pages/qa/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
    print(f'总行数: {len(c.splitlines())}')
    print(f'qa-item数量: {c.count("class=\"qa-item\"")}')
