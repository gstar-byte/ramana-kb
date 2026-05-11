#!/usr/bin/env python3
"""
为问答页面添加 icon
- qa/index.html: <h1>修行问答</h1> -> <h1>💬 修行问答</h1>
- qa/qa-*.html: <h1>💬 修行问答X：标题</h1> (已有icon，检查是否缺失)
"""
import os
import re
from pathlib import Path

def fix_qa_index():
    """修复问答首页"""
    file_path = Path("c:/Users/willp/Desktop/2026年4月/kb01/pages/qa/index.html")
    if not file_path.exists():
        print(f"❌ 文件不存在: {file_path}")
        return False

    content = file_path.read_text(encoding='utf-8')

    # 检查是否已经有 icon
    if '<h1>💬 修行问答</h1>' in content:
        print("✅ qa/index.html 已有 icon，跳过")
        return True

    # 添加 icon
    if '<h1>修行问答</h1>' in content:
        content = content.replace('<h1>修行问答</h1>', '<h1>💬 修行问答</h1>')
        file_path.write_text(content, encoding='utf-8')
        print("✅ 已修复 qa/index.html")
        return True
    else:
        print("⚠️ qa/index.html 未找到目标标题")
        return False

def fix_qa_pages():
    """修复各个问答详情页"""
    qa_dir = Path("c:/Users/willp/Desktop/2026年4月/kb01/pages/qa")
    qa_files = sorted(qa_dir.glob("qa-*.html"))

    fixed_count = 0
    skipped_count = 0
    error_count = 0

    for file_path in qa_files:
        try:
            content = file_path.read_text(encoding='utf-8')

            # 检查 page-header 中的 h1
            # 目标模式: <h1>💬 修行问答X：标题</h1>
            # 问题模式: <h1>修行问答X：标题</h1> (缺少icon)

            # 查找 page-header 中的 h1
            match = re.search(r'<header class="page-header">\s*<h1>(.*?)</h1>', content, re.DOTALL)
            if not match:
                print(f"⚠️ {file_path.name}: 未找到 page-header h1")
                error_count += 1
                continue

            h1_content = match.group(1)

            # 检查是否已经有 icon
            if h1_content.startswith('💬'):
                skipped_count += 1
                continue

            # 添加 icon
            new_h1 = f'💬 {h1_content}'
            new_content = content.replace(f'<h1>{h1_content}</h1>', f'<h1>{new_h1}</h1>', 1)

            if new_content != content:
                file_path.write_text(new_content, encoding='utf-8')
                print(f"✅ {file_path.name}: 已添加 icon")
                fixed_count += 1
            else:
                print(f"⚠️ {file_path.name}: 替换失败")
                error_count += 1

        except Exception as e:
            print(f"❌ {file_path.name}: 错误 - {e}")
            error_count += 1

    print(f"\n📊 问答详情页统计:")
    print(f"   修复: {fixed_count}")
    print(f"   跳过(已有icon): {skipped_count}")
    print(f"   错误: {error_count}")
    print(f"   总计: {len(qa_files)}")

if __name__ == "__main__":
    print("📝 开始为问答页面添加 icon...\n")

    # 修复首页
    print("📄 修复问答首页...")
    fix_qa_index()

    print("\n📄 修复问答详情页...")
    fix_qa_pages()

    print("\n✅ 完成!")
