#!/usr/bin/env python3
"""
KB01 性能优化脚本 - 压缩CSS、合并JS、减少HTTP请求
"""
import re
import os
from pathlib import Path

KB01 = Path("F:/26年4月/kb01/pages")

def minify_css(css_path):
    """压缩CSS：去除注释、空格、换行"""
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 去除注释
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # 去除多余空格（保留CSS属性之间的空格）
    content = re.sub(r'\s*([{}:;,])\s*', r'\1', content)
    content = re.sub(r';\s*}', '}', content)
    content = re.sub(r'\s+', ' ', content)

    # 去除首尾空白
    content = content.strip()

    return content

def minify_js(js_path):
    """压缩JS：去除注释和多余空格"""
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 去除单行注释
    content = re.sub(r'//[^\n]*', '', content)

    # 去除多行注释
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # 去除多余空格
    content = re.sub(r'\s+', ' ', content)
    content = re.sub(r'\s*([{}();,=+\-*/<>!&|.?:])\s*', r'\1', content)

    return content.strip() + '\n'

def create_bundle_js():
    """合并script.js和search.js为一个bundle"""
    script_path = KB01 / "script.js"
    search_path = KB01 / "search.js"

    bundle = ""

    if script_path.exists():
        bundle += minify_js(script_path) + "\n"

    if search_path.exists():
        bundle += minify_js(search_path) + "\n"

    return bundle

def update_html_references():
    """更新HTML文件中的JS/CSS引用"""
    html_files = list(KB01.glob("*.html")) + list(KB01.glob("**/*.html"))
    updated = 0

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # 替换 styles.css 为 styles.min.css
            content = content.replace('href="styles.css"', 'href="styles.min.css"')
            content = content.replace("href='styles.css'", "href='styles.min.css'")

            # 替换 script.js + search.js 为 bundle.min.js
            # 先移除旧的script标签
            content = re.sub(r'<script\s+[^>]*src=["\']script\.js["\'][^>]*></script>\s*', '', content)
            content = re.sub(r'<script\s+[^>]*src=["\']search\.js["\'][^>]*></script>\s*', '', content)

            # 添加bundle.min.js（在</body>前）
            if 'bundle.min.js' not in content and 'app.js' not in content:
                content = content.replace('</body>', '<script src="bundle.min.js" defer></script>\n</body>')

            # 对于使用app.js的页面，保持不变或改为bundle
            # 因为app.js已经包含了搜索功能

            if content != original:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated += 1

        except Exception as e:
            print(f"Error processing {html_file}: {e}")

    return updated

def main():
    print("🚀 KB01 性能优化开始...")

    # 1. 压缩CSS
    print("\n📦 压缩CSS...")
    css_path = KB01 / "styles.css"
    css_size_before = css_path.stat().st_size
    minified_css = minify_css(css_path)

    min_css_path = KB01 / "styles.min.css"
    with open(min_css_path, 'w', encoding='utf-8') as f:
        f.write(minified_css)

    css_size_after = min_css_path.stat().st_size
    print(f"   styles.css: {css_size_before:,} → {css_size_after:,} bytes ({100*css_size_after/css_size_before:.1f}%)")
    print(f"   节省: {css_size_before - css_size_after:,} bytes ({(1-css_size_after/css_size_before)*100:.1f}%)")

    # 2. 合并并压缩JS
    print("\n📦 合并并压缩JS...")
    bundle = create_bundle_js()

    bundle_path = KB01 / "bundle.min.js"
    with open(bundle_path, 'w', encoding='utf-8') as f:
        f.write(bundle)

    bundle_size = len(bundle.encode('utf-8'))
    print(f"   bundle.min.js: {bundle_size:,} bytes (script.js + search.js)")

    # 3. 更新HTML引用
    print("\n🔗 更新HTML引用...")
    updated = update_html_references()
    print(f"   更新了 {updated} 个HTML文件")

    print("\n✅ 优化完成!")
    print(f"   CSS: {css_size_before:,} → {css_size_after:,} bytes")
    print(f"   JS: {bundle_size:,} bytes (合并后)")
    print(f"\n📝 注意: 请检查页面是否正常工作，如有问题可恢复原文件。")

if __name__ == "__main__":
    main()
