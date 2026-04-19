import re
c = open(r'c:\Users\willp\WorkBuddy\20260410104230\pages\concepts\maya.html', encoding='utf-8').read()
# 找 serviceWorker.register 的上下文
idx = c.find('serviceWorker.register')
print('SW code附近:')
print(c[max(0,idx-80):idx+250])
