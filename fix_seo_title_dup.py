#!/usr/bin/env python3
"""
SEO修复脚本 - 修复Title重复、品牌名重复等问题
"""
import re
from pathlib import Path

KB01 = Path("F:/26年4月/kb01/pages")

BRAND = "拉玛那马哈希"

def fix_title_duplication(html_path):
    """修复Title中的重复问题"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. 修复 <title> 标签中的重复
    # 匹配 <title>...</title> 并修复
    def fix_title_tag(match):
        title = match.group(1)
        # 移除末尾的品牌名重复（如 "... | 拉玛那马哈希 | 拉玛那马哈希"）
        title = re.sub(rf'\s*\|\s*{BRAND}\s*\|\s*{BRAND}', f' | {BRAND}', title)
        title = re.sub(rf'\s*\|\s*{BRAND}\s*$', f' | {BRAND}', title)
        return f'<title>{title}</title>'

    content = re.sub(r'<title>([^<]+)</title>', fix_title_tag, content)

    # 2. 修复 og:title 和 twitter:title
    # og:title 应该和 title 保持一致
    def fix_meta_title(match):
        full = match.group(0)
        # 提取现有title
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            new_title = title_match.group(1)
            return f'<meta property="og:title" content="{new_title}">'
        return full

    content = re.sub(r'<meta property="og:title"[^>]+>', fix_meta_title, content)

    # twitter:title
    def fix_twitter_title(match):
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            new_title = title_match.group(1)
            # Twitter title 可以稍短，避免截断
            short_title = new_title.split('|')[0].strip()
            return f'<meta name="twitter:title" content="{short_title}">'
        return match.group(0)

    content = re.sub(r'<meta name="twitter:title"[^>]+>', fix_twitter_title, content)

    # 3. 修复 meta description 中的品牌名重复
    content = re.sub(rf'\s*\|{BRAND}知识库\s*\|{BRAND}知识库', f' | {BRAND}知识库', content)

    if content != original:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_all():
    html_files = list(KB01.glob("**/*.html"))
    fixed = 0

    for html_file in html_files:
        try:
            if fix_title_duplication(html_file):
                fixed += 1
        except Exception as e:
            print(f"Error: {html_file}: {e}")

    return fixed

def main():
    print("🔧 修复SEO Title重复问题...")

    fixed = fix_all()

    print(f"✅ 修复了 {fixed} 个文件")

    # 验证
    sample = KB01 / "index.html"
    with open(sample, 'r', encoding='utf-8') as f:
        content = f.read()

    title = re.search(r'<title>([^<]+)</title>', content)
    og_title = re.search(r'<meta property="og:title"[^>]+>', content)
    tw_title = re.search(r'<meta name="twitter:title"[^>]+>', content)

    print(f"\n📋 验证 (index.html):")
    print(f"   Title: {title.group(1) if title else '未找到'}")
    if og_title:
        print(f"   og:title: {og_title.group(0)[:80]}...")
    if tw_title:
        print(f"   twitter:title: {tw_title.group(0)[:80]}...")

if __name__ == "__main__":
    main()
