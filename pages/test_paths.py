#!/usr/bin/env python3
"""
测试路径处理
"""
import os

# 测试不同路径
paths = [
    '/graph/',
    '/graph',
    '/books/',
    '/books/be-as-you-are/',
    '/books/be-as-you-are'
]

print("测试路径处理：")
print("当前目录:", os.getcwd())
print()

for path in paths:
    # 模拟 http.server 处理路径的方式
    # http.server 会把 / 映射到当前目录
    if path.startswith('/'):
        local_path = path[1:]  # 去掉开头的 /
    else:
        local_path = path
    
    # 规范化路径
    local_path = os.path.normpath(local_path)
    
    print(f"请求路径: {path}")
    print(f"本地路径: {local_path}")
    
    # 检查文件是否存在
    if os.path.exists(local_path):
        print(f"✓ 存在: {local_path}")
    else:
        print(f"✗ 不存在: {local_path}")
        
        # 尝试去掉末尾斜杠加 .html
        if local_path.endswith('/'):
            test_path = local_path.rstrip('/') + '.html'
        else:
            test_path = local_path + '.html'
        
        if os.path.exists(test_path):
            print(f"✓ 尝试成功: {test_path}")
        else:
            print(f"✗ 尝试失败: {test_path}")
    
    print()

print("\n当前目录的 HTML 文件:")
for f in os.listdir('.'):
    if f.endswith('.html'):
        print(f"  - {f}")

print("\nbooks 目录的 HTML 文件:")
if os.path.exists('books'):
    for f in os.listdir('books'):
        if f.endswith('.html'):
            print(f"  - {f}")
