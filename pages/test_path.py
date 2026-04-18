#!/usr/bin/env python3
"""
测试路径处理
"""
import os
import http.server

class TestHandler(http.server.SimpleHTTPRequestHandler):
    pass

# 创建一个临时处理器实例
handler = TestHandler(None, ('', 0), None)

# 测试不同路径
paths = [
    '/graph/',
    '/graph',
    '/books/',
    '/books/be-as-you-are/',
    '/books/be-as-you-are'
]

print("测试路径转换：")
for path in paths:
    translated = handler.translate_path(path)
    exists = os.path.exists(translated)
    print(f"{path:30} → {translated:60} 存在: {exists}")
    
    # 测试可能的转换
    if not exists:
        if path.endswith('/'):
            test_path = path.rstrip('/') + '.html'
            test_translated = handler.translate_path(test_path)
            test_exists = os.path.exists(test_translated)
            print(f"  尝试: {test_path:26} → {test_translated:60} 存在: {test_exists}")

print("\n当前目录文件:")
for f in os.listdir('.'):
    if f.endswith('.html'):
        print(f"  {f}")
