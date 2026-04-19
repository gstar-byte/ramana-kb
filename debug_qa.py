import re

# 测试一个 item
item = '''<div class="qa-q">❓ 什么是自我探究？</div>
                        <div class="qa-a">自我探究是问"我是谁"的过程。不是用心智去找答案，而是将注意力从外物不断收回到"我是谁"这个根本问题。答案不在语言中，而在于探究本身。</div>
                    '''

print("Original item:")
print(item)
print()

# 提取问题
q_match = re.search(r'class="qa-q">(.*?)<\/div>', item, re.DOTALL)
print(f"q_match: {q_match}")

if q_match:
    question = q_match.group(1).strip()
    print(f"question: {question}")
