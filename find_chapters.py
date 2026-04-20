# -*- coding: utf-8 -*-
"""Find the four key sections in collected_works.txt"""
with open(r'c:/Users/willp/Desktop/2026年4月/kb01\pdf_content\collected_works.txt', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find Upadesa Saram and Vichara Sutram
targets = ['UPADESA SARAM', 'Upadesa Saram', 'VICHARA SUTRAM', 'Vichara Sutram',
           'Self-Enquiry', 'Self-enquiry', 'WHO AM I', 'Who am I?',
           'Reality in Forty', 'Forty Verses', 'Ulladu Narpadu', 'ELEVEN VERSES',
           'Upadesa Manjari', 'Maharshi\'s', 'ORIGINAL WORKS']

for target in targets:
    for i, l in enumerate(lines):
        if target.lower() in l.lower() and not l.strip().startswith('---'):
            print(f"[{target}] Line {i+1}: {l.strip()[:80]}")
