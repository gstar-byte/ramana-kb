import re

# 测试
item = '<div class="qa-q">❓ 什么是自我探究？</div>\n                        <div class="qa-a">自我探究是问"我是谁"的过程。不是用心智去找答案，而是将注意力从外物不断收回到"我是谁"这个根本问题。答案不在语言中，而在于探究本身。'

print("Item:")
print(item)
print()

# 尝试不同的模式
patterns = [
    (r'class="qa-q">(.*?)<\/div>', "qa-q pattern"),
    (r'class="qa-a">(.*?)<\/div>', "qa-a pattern"),
    (r'class=.{1}qa-q{1}>(.*?)<\/div>', "qa-q pattern relaxed"),
    (r'class=.{1}qa-a{1}>(.*?)<\/div>', "qa-a pattern relaxed"),
]

for pattern, name in patterns:
    m = re.search(pattern, item, re.DOTALL)
    print(f"{name}: {m}")
