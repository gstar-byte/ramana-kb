import re, glob

# 修复：给 SW script 块加上 </script> 闭合标签
files = [
    r'c:\Users\willp\WorkBuddy\20260410104230\pages\index.html',
    r'c:\Users\willp\WorkBuddy\20260410104230\pages\concepts\guru.html',
    r'c:\Users\willp\WorkBuddy\20260410104230\pages\concepts\maya.html',
]

for f in files:
    with open(f, encoding='utf-8') as fh:
        c = fh.read()
    
    # 在 </script> 后面是 pwa-analytics.js 的地方，确保 SW script 正确闭合
    # 当前: ...}</script>
    #     <script src="pwa-analytics.js"></script>
    # 错误: ...}
    #     <script src="pwa-analytics.js"></script>
    
    old = '''        }
    <script src="pwa-analytics.js"></script>'''
    
    new = '''    </script>
    <script src="pwa-analytics.js"></script>'''
    
    if old in c:
        c = c.replace(old, new, 1)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c)
        print(f'修复: {f}')
    else:
        # 可能已经修复过了，检查一下
        if '</script>' in c and 'pwa-analytics.js' in c:
            # 找 pwa-analytics 前的文本
            idx = c.find('pwa-analytics.js')
            before = c[max(0, idx-20):idx]
            if '</script>' in before:
                print(f'已正确 (跳过): {f}')
            else:
                print(f'未匹配，需要手动检查: {f}')
        else:
            print(f'未找到 pwa-analytics: {f}')

print('\n完成')
