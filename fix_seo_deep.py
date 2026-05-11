#!/usr/bin/env python3
"""
SEO深度修复 - 修复所有双竖线和格式问题
"""
import re
from pathlib import Path

KB01 = Path("F:/26年4月/kb01/pages")
BRAND = "拉玛那马哈希"

def deep_fix(html_path):
    """深度修复所有SEO问题"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. 修复双竖线 ||
    content = re.sub(r'\|\s*\|', '|', content)
    content = re.sub(r'\s*\|\s*\|', ' | ', content)

    # 2. 修复 title 标签中的重复品牌名
    # 移除连续重复的品牌名
    pattern = rf'({BRAND}[^|]*)\s*\|\s*{BRAND}([^|]*\|\s*{BRAND})'
    content = re.sub(pattern, rf'\1 | {BRAND}', content)

    # 3. 移除title末尾的连续重复
    # 如 "... | 拉玛那马哈希 | 拉玛那马哈希"
    content = re.sub(rf'\s*\|\s*{BRAND}\s*\|\s*{BRAND}\s*$', f' | {BRAND}', content)

    # 4. 同步 og:title 和 twitter:title
    title_match = re.search(r'<title>([^<]+)</title>', content)
    if title_match:
        title = title_match.group(1)

        # og:title 同步
        content = re.sub(
            r'<meta property="og:title" content="[^"]*"',
            f'<meta property="og:title" content="{title}"',
            content
        )

        # twitter:title 使用主标题（避免太长）
        short_title = title.split('|')[0].strip()
        content = re.sub(
            r'<meta name="twitter:title" content="[^"]*"',
            f'<meta name="twitter:title" content="{short_title}"',
            content
        )

    # 5. 修复 meta description 中的重复
    content = re.sub(rf'{BRAND}知识库\s*\|\s*{BRAND}知识库', f'{BRAND}知识库', content)

    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("🔧 深度修复SEO问题...")

    html_files = list(KB01.glob("**/*.html"))
    fixed = 0

    for html_file in html_files:
        try:
            if deep_fix(html_file):
                fixed += 1
        except Exception as e:
            print(f"Error: {html_file}: {e}")

    print(f"✅ 修复了 {fixed} 个文件")

    # 验证
    print("\n📋 验证样本:")
    samples = ["index.html", "books/be-as-you-are.html", "concepts/whoami.html"]
    for s in samples:
        path = KB01 / s
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            title = re.search(r'<title>([^<]+)</title>', content)
            if title:
                print(f"  {s}: {title.group(1)[:70]}...")

    # 检查双竖线
    double_pipe = sum(1 for f in KB01.glob("**/*.html") if '||' in open(f, 'r', encoding='utf-8').read())
    print(f"\n  仍有双竖线: {double_pipe} 个文件")

if __name__ == "__main__":
    main()
