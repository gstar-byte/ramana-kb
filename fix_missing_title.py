#!/usr/bin/env python3
"""
修复缺失<title>标签的页面
"""
import re
from pathlib import Path

KB01 = Path("F:/26年4月/kb01/pages")

def add_missing_title(html_path):
    """为缺失title的页面添加"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 检查是否已有<title>
    if '<title>' in content:
        return False

    # 从og:title提取
    og_match = re.search(r'<meta property="og:title" content="([^"]+)"', content)
    if og_match:
        og_title = og_match.group(1)
        # 移除末尾的品牌名重复
        og_title = re.sub(r'\s*\|\s*拉玛那马哈希\s*\|\s*拉玛那马哈希', ' | 拉玛那马哈希', og_title)
        og_title = re.sub(r'\s*\|\s*拉玛那马哈希知识库\s*$', '', og_title)

        # 在</head>前插入<title>
        content = content.replace('</head>', f'<title>{og_title}</title>\n</head>')

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    print("🔧 添加缺失的<title>标签...")

    html_files = list(KB01.glob("**/*.html"))
    fixed = 0

    for html_file in html_files:
        try:
            if add_missing_title(html_file):
                fixed += 1
                print(f"  修复: {html_file.relative_to(KB01)}")
        except Exception as e:
            print(f"Error: {html_file}: {e}")

    print(f"\n✅ 共修复 {fixed} 个文件")

    # 验证
    still_missing = sum(1 for f in KB01.glob("**/*.html") if '<title>' not in open(f, 'r', encoding='utf-8').read())
    print(f"   仍缺失: {still_missing} 个")

if __name__ == "__main__":
    main()
