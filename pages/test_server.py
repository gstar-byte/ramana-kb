#!/usr/bin/env python3
"""
模拟 Vercel 的 cleanUrls 功能的本地测试服务器
- /path → /path.html
- /path/index → /path/index.html
- 自动重定向：/books → /books/ (301)
"""
import http.server
import os
import socketserver
import urllib.parse

PORT = 8004

class CleanURLRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 移除查询参数和锚点
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query = parsed_path.query
        fragment = parsed_path.fragment
        
        # 检查是否需要重定向添加末尾斜杠
        if (path != '/' and 
            not path.endswith('/') and
            not '.' in os.path.basename(path)):  # 不是带扩展名的文件
            # 检查对应的资源是否存在
            test_path1 = path + '.html'
            test_path2 = path + '/index.html'
            test_dir = path.rstrip('/')
            
            # 如果对应的内容存在，就重定向
            if (os.path.exists(self.translate_path(test_path1)) or 
                os.path.exists(self.translate_path(test_path2)) or
                os.path.isdir(self.translate_path(test_dir))):
                # 构建重定向 URL
                redirect_url = path + '/'
                if query:
                    redirect_url += '?' + query
                if fragment:
                    redirect_url += '#' + fragment
                
                # 发送 301 重定向
                self.send_response(301)
                self.send_header('Location', redirect_url)
                self.end_headers()
                return
        
        # 检查是否为根路径
        if path == '/' or path == '':
            path = '/index.html'
        
        # 检查路径是否已存在
        if not os.path.exists(self.translate_path(path)):
            # 尝试多种可能性
            possible_paths = []
            
            # 1. 去掉末尾斜杠，然后加 .html (处理 /graph/ → /graph.html)
            if path.endswith('/'):
                possible_paths.append(path.rstrip('/') + '.html')
            
            # 2. 直接加 .html (处理 /graph → /graph.html)
            possible_paths.append(path + '.html')
            
            # 3. 检查是否为目录，尝试 index.html (处理 /books/ → /books/index.html)
            possible_paths.append(path.rstrip('/') + '/index.html')
            
            # 4. 检查是否带有 index，尝试补充为 index.html (处理 /books/index → /books/index.html)
            if path.endswith('/index'):
                possible_paths.append(path + '.html')
            
            # 5. 检查是否带有 /index/ 的情况 (处理 /books/index/ → /books/index.html)
            if path.endswith('/index/'):
                possible_paths.append(path.rstrip('/') + '.html')
            
            # 尝试所有可能的路径
            for test_path in possible_paths:
                if os.path.exists(self.translate_path(test_path)):
                    path = test_path
                    break
        
        # 更新 self.path
        self.path = path
        return super().do_GET()

Handler = CleanURLRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'测试服务器运行在 http://localhost:{PORT}')
    print('模拟 Vercel 的 cleanUrls 功能 + 自动重定向添加斜杠')
    print('按 Ctrl+C 停止服务器')
    httpd.serve_forever()
