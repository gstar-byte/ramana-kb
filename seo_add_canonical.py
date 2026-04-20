"""
SEO Fix Phase 3: 批量添加/更新 canonical 标签
统一使用 non-www 域名: https://ramanamaharshi.space
在 <head> 中 robots meta 标签后添加 <link rel="canonical">
"""
import os
import re

BASE_URL = "https://ramanamaharshi.space"
PAGES_DIR = "/workspace/pages"

EXCLUDE_FILES = {"_template.html", "sitemap.html"}


def get_url_path(filepath):
    """将文件路径转换为URL路径（保留.html后缀）"""
    rel = os.path.relpath(filepath, PAGES_DIR).replace(os.sep, "/")
    
    if rel == "index.html":
        return "/"
    elif rel.endswith("/index.html"):
        rel = rel[:-10] + "/"
    
    if not rel.startswith("/"):
        rel = "/" + rel
    
    return rel


def add_canonical():
    added = 0
    updated = 0
    skipped = 0
    
    for root, dirs, files in os.walk(PAGES_DIR):
        for fname in sorted(files):
            if not fname.endswith(".html"):
                continue
            if fname in EXCLUDE_FILES:
                continue
            
            fpath = os.path.join(root, fname)
            
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                url_path = get_url_path(fpath)
                full_url = BASE_URL + url_path
                new_canonical = f'<link rel="canonical" href="{full_url}">'
                
                # 检查是否已有 canonical
                has_canonical = bool(re.search(r'<link\s+rel=["\']canonical["\']', content))
                
                if has_canonical:
                    # 更新已有的 canonical
                    content = re.sub(
                        r'<link\s+rel=["\']canonical["\'][^>]*>',
                        new_canonical,
                        content,
                        flags=re.IGNORECASE
                    )
                    action = "updated"
                    updated += 1
                else:
                    # 在 robots meta 后插入 canonical（或 </title> 之后）
                    # 策略：找 <meta name="robots"，在其后插入
                    robots_match = re.search(r'(<meta[^>]*name=["\']robots["\'][^>]*>)', content)
                    if robots_match:
                        insert_pos = robots_match.end()
                        content = content[:insert_pos] + "\n    " + new_canonical + content[insert_pos:]
                        action = "added (after robots)"
                        added += 1
                    else:
                        # 备选：在 </title> 或第一个 meta 后插入
                        title_match = re.search(r'(</title>)', content)
                        if title_match:
                            insert_pos = title_match.end()
                            content = content[:insert_pos] + "\n    " + new_canonical + content[insert_pos:]
                            action = "added (after title)"
                            added += 1
                        else:
                            skipped += 1
                            continue
                
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                
                rel_path = os.path.relpath(fpath, PAGES_DIR)
                print(f"  [{action}] {rel_path} → {full_url}")
                    
            except Exception as e:
                print(f"  [ERR] {fname}: {e}")
    
    print(f"\n=== 完成！新增 {added}, 更新 {updated}, 跳过 {skipped} ===")


if __name__ == "__main__":
    add_canonical()
