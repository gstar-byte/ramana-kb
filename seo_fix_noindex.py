"""
SEO Fix Phase 1: 批量移除 noindex, 改为 index, follow
对 pages/ 目录下所有 HTML 文件执行替换
"""
import os
import re

PAGES_DIR = "c:/Users/willp/WorkBuddy/20260410104230/pages"

def fix_noindex():
    count = 0
    errors = []
    
    for root, dirs, files in os.walk(PAGES_DIR):
        for fname in files:
            if not fname.endswith(".html"):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original = content
                # 替换 noindex,nofollow 为 index,follow
                content = re.sub(
                    r'<meta\s+name=["\']robots["\']\s+content=["\']noindex,\s*nofollow["\']\s*/?>',
                    '<meta name="robots" content="index, follow">',
                    content,
                    flags=re.IGNORECASE
                )
                
                if content != original:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)
                    count += 1
                    rel_path = os.path.relpath(fpath, PAGES_DIR)
                    print(f"  [OK] {rel_path}")
                    
            except Exception as e:
                errors.append((fpath, str(e)))
                print(f"  [ERR] {fname}: {e}")
    
    print(f"\n=== 完成！共修改 {count} 个文件 ===")
    if errors:
        print(f"\n⚠️ {len(errors)} 个文件出错:")
        for fp, err in errors:
            print(f"  - {fp}: {err}")

if __name__ == "__main__":
    fix_noindex()
