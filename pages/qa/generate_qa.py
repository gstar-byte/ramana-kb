#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 读取现有的qa-1.html作为模板
with open('qa-1.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# 生成qa-29.html 到 qa-58.html
for i in range(29, 59):
    filename = f'qa-{i}.html'
    
    # 替换文件名和页码
    content = template_content.replace('qa-1.html', filename)
    content = content.replace('第 1 页 / 共 28 页', f'第 {i} 页 / 共 58 页')
    
    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已生成 {filename}')

print('完成！共生成30个QA文件（qa-29.html 到 qa-58.html）')
