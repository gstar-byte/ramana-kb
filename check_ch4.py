for ch in ['be-as-you-are-ch2.html', 'be-as-you-are-ch4.html']:
    path = r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/' + ch
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'=== {ch} ===')
    for i, l in enumerate(lines):
        stripped = l.strip()
        if stripped.startswith(('<h2', '<h3')):
            print(f'  行{i+1:3d}: {stripped[:100]}')
    print()
