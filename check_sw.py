import re

sw = open(r'c:\Users\willp\WorkBuddy\20260410104230\pages\sw.js', encoding='utf-8').read()

# 找预缓存列表
precache = re.findall(r'"([^"]+\.html)"', sw)
print(f'sw.js 预缓存 .html 文件: {len(precache)} 个')
for p in precache[:10]:
    print(f'  {p}')
print('...')

# 找 install 事件中的缓存URL
install_block = re.search(r'install.*?\{(.*?)\}', sw, re.DOTALL)
if install_block:
    print('\ninstall 事件中的内容:')
    print(install_block.group(0)[:500])
