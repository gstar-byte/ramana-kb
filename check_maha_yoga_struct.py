#!/usr/bin/env python3
with open(r'c:/Users/willp/Desktop/2026年4月/kb01/pages/books/maha-yoga.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ('article tag (should NOT exist)', 'article' not in html),
    ('book-detail (should NOT exist)', 'book-detail' not in html),
    ('book-header (should NOT exist)', 'book-header' not in html),
    ('book-icon-large (should NOT exist)', 'book-icon-large' not in html),
    ('book-intro (should NOT exist)', 'book-intro' not in html),
    ('book-related (should NOT exist)', 'book-related' not in html),
    ('breadcrumb (should exist)', 'breadcrumb' in html),
    ('page-header (should exist)', 'page-header' in html),
    ('card class (should exist)', 'card' in html),
    ('chapter-card (should exist)', 'chapter-card' in html),
]

for name, ok in checks:
    print(f"{'✓' if ok else '✗'} {name}")
