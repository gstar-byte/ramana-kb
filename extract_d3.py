#!/usr/bin/env python3
"""从git历史中提取D3.js代码并插入到当前graph.html"""

import subprocess
import re

# 获取历史版本的完整内容
result = subprocess.run(
    ['git', 'show', '3e370d2:pages/graph.html'],
    cwd=r'c:\Users\willp\Desktop\2026年4月\kb01',
    capture_output=True, text=True, encoding='utf-8'
)
hist_content = result.stdout

# 读取当前文件
with open(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\graph.html', 'r', encoding='utf-8') as f:
    curr_content = f.read()

# 从历史版本提取D3.js代码块
# 找到 // ========== D3.js 知识图谱 ========== 开始
# 到 </script> 结束（在zoom函数之后）
start_marker = '// ========== D3.js 知识图谱 =========='
end_marker = '</script>'

start_idx = hist_content.find(start_marker)
if start_idx == -1:
    print("ERROR: Start marker not found in history")
    exit(1)

# 找到zoom相关函数之后的位置
zoom_pattern = r'function zoomIn\(\)|function zoomOut\(\)|function resetZoom\(\)'
zoom_matches = list(re.finditer(zoom_pattern, hist_content[start_idx:]))
if zoom_matches:
    # 找到最后一个zoom函数之后的</script>
    last_zoom_end = zoom_matches[-1].end()
    # 从这个位置往后找</script>
    script_end = hist_content.find(end_marker, start_idx + last_zoom_end)
    if script_end != -1:
        d3_code = hist_content[start_idx:script_end + len(end_marker)]
    else:
        print("ERROR: Could not find </script> after zoom functions")
        exit(1)
else:
    print("ERROR: Zoom functions not found")
    exit(1)

print(f"Extracted D3 code length: {len(d3_code)} chars")

# 在当前文件中找到插入位置
# 在 </footer> 之后，</main> 之前插入
insert_marker = '</footer>'
insert_idx = curr_content.rfind(insert_marker)
if insert_idx == -1:
    print("ERROR: Insert marker not found in current file")
    exit(1)

# 在 </footer> 之后插入 <script> 块
insert_pos = insert_idx + len(insert_marker)

# 构建要插入的代码
script_block = '\n    <script>\n        ' + d3_code + '\n    </script>'

# 插入
new_content = curr_content[:insert_pos] + script_block + curr_content[insert_pos:]

# 保存
with open(r'c:\Users\willp\Desktop\2026年4月\kb01\pages\graph.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("D3.js code inserted successfully!")
