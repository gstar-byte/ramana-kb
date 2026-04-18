#!/usr/bin/env python3
"""
模拟 Vercel 的 cleanUrls 功能的本地测试服务器
- /path → /path.html
- /path/index → /path/index.html
"""
import http.server
import os
import socketserver

PORT = 8002

class CleanURLRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 移除查询参数
        path = self.path.split('?')[0]
        
        # 检查是否为根路径
        if path == '/' or path == '':
            path = '/index.html'
        
        # 检查路径是否已存在
        if not os.path.exists(self.translate_path(path)):
            # 尝试添加 .html 扩展名
            path_with_html = path + '.html'
            if os.path.exists(self.translate_path(path_with_html)):
                path = path_with_html
            # 检查是否为目录，尝试 index.html
            elif os.path.isdir(self.translate_path(path.rstrip('/'))):
                index_path = path.rstrip('/') + '/index.html'
                if os.path.exists(self.translate_path(index_path)):
                    path = index_path
            # 检查是否已带有 index，尝试补充为 index.html
            elif path.endswith('/index'):
                path_with_html = path + '.html'
                if os.path.exists(self.translate_path(path_with_html)):
                    path = path_with_html
            # 检查是否带有 /index/ 的情况
            elif path.endswith('/index/'):
                path_with_html = path.rstrip('/') + '.html'
                if os.path.exists(self.translate_path(path_with_html)):
                    path = path_with_html
            # 检查是否只是目录路径
            elif not path.endswith('.html'):
                # 先尝试直接加 .html
                path_with_html = path + '.html'
                if os.path.exists(self.translate_path(path_with_html)):
                    path = path_with_html
                else:
                    # 再尝试加 /index.html
                    path_with_index = path.rstrip('/') + '/index.html'
                    if os.path.exists(self.translate_path(path_with_index)):
                        path = path_with_index
        
        # 更新 self.path
        self.path = path
        return super().do_GET()

Handler = CleanURLRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'测试服务器运行在 http://localhost:{PORT}')
    print('模拟 Vercel 的 cleanUrls 功能')
    print('按 Ctrl+C 停止服务器')
    httpd.serve_forever()
