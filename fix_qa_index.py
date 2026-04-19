#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""修复 index.html：删除分页导航后的游离 qa-item"""

import re

# 读取备份文件作为正确参考
with open('pages/qa/index.html.backup', 'r', encoding='utf-8') as f:
    backup = f.read()

# 查找正确的结构结束位置
# 在备份中，"        </main>" 之后是 "<script>"
# 我们需要保留分页前的最后一个 qa-item 后的内容

# 读取当前损坏的文件
with open('pages/qa/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到 "        </main>" 的位置
main_close = content.find('        </main>')
if main_close == -1:
    print("错误：找不到 </main>")
    exit(1)

# 在 </main> 之前，找到最后一个 </div> (关闭 qa-list)
before_main = content[:main_close]
last_div_before_main = before_main.rfind('</div>')
last_qa_item = before_main.rfind('</div>\n\n                <div class="qa-item"')

print(f"文件总长度: {len(content)}")
print(f"</main> 位置: {main_close}")

# 找到 <script> 开始的位置（分页前的 script）
script_start = content.find('<script>', main_close)
print(f"第一个 <script> 位置: {script_start}")

# 删除从 </main> 到 <script> 之间的所有游离内容
if script_start > main_close:
    # 提取正确部分
    correct_part = content[:main_close] + '\n' + content[main_close:].split('\n', 1)[0]  # 保留 </main>
    # 加上 </body> 和 </html> 前的 script 部分
    script_section = content[script_start:]
    
    # 重构文件
    # 正确的结构是: ... </main> [错误内容] <script> ... </body> </html>
    # 我们需要: ... </main> [正确内容] </body> </html>
    
    # 找到 </body> 和 </html>
    body_close = content.find('</body>')
    html_close = content.find('</html>')
    
    if body_close > main_close and html_close > body_close:
        # 保留 </main> 之前的所有内容
        # 加上 </body> 和 </html> 之前的内容（去除错误内容）
        result = content[:main_close]
        # 加上 </main> 本身
        result += '\n' + content[main_close:].split('\n', 1)[0]
        # 加上 </body> 和 </html> 前的 script 部分
        result += '\n' + content[script_start:]
        
        # 写入
        with open('pages/qa/index.html', 'w', encoding='utf-8') as f:
            f.write(result)
        
        print(f"清理完成！新文件长度: {len(result)}")
    else:
        print("错误：找不到 </body> 或 </html>")
        exit(1)
else:
    print("错误：找不到分页后的 <script>")
    exit(1)

# 验证
with open('pages/qa/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"新文件行数: {len(lines)}")
print(f"最后5行: {''.join(lines[-5:])}")
