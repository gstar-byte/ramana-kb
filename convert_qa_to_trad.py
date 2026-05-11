#!/usr/bin/env python3
"""转换 zh-TW QA 数据文件为繁体中文"""
import json
import opencc

converter = opencc.OpenCC('s2t')

INPUT = r"F:\26年4月\kb01\pages\zh-TW\qa\qa-data.json"
OUTPUT = r"F:\26年4月\kb01\pages\zh-TW\qa\qa-data.json"

with open(INPUT, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for item in data:
    if 'question' in item:
        item['question'] = converter.convert(item['question'])
    if 'answer' in item:
        item['answer'] = converter.convert(item['answer'])
    if 'meta' in item:
        item['meta'] = converter.convert(item['meta'])
    if 'category' in item:
        item['category'] = converter.convert(item['category'])
    count += 1

with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"已转换 {count} 个 QA 条目为繁体中文")
