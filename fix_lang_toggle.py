import re

with open("F:/26年4月/kb01/pages/zh-TW/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# 找到并替换 lang-toggle 规则
old_pattern = r'\.lang-toggle\{display:inline-flex;align-items:center;justify-content:center;[^}]+\}'
new_rule = '.lang-toggle{display:inline-flex;align-items:center;justify-content:center;height:20px !important;line-height:20px !important;font-size:10px !important;padding:0 6px !important;border-radius:10px !important;background:var(--gold) !important;box-shadow:0 1px 4px rgba(184,134,11,0.2) !important;}'
css = re.sub(old_pattern, new_rule, css)

# 移除 :hover 规则
css = re.sub(r'\.lang-toggle:hover\{[^}]+\}', '', css)

with open("F:/26年4月/kb01/pages/zh-TW/styles.css", "w", encoding="utf-8", newline="") as f:
    f.write(css)

print("Done")
