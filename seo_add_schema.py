"""
SEO Fix Phase 4: 批量注入 JSON-LD 结构化数据（6种Schema）
根据页面类型自动选择合适的 Schema：
- 首页: WebSite + BreadcrumbList
- 书籍页面: Book + BreadcrumbList  
- 概念页面: Article + BreadcrumbList
- 人物页面: Person/Biography + BreadcrumbList
- 问答页面: FAQPage + BreadcrumbList
- 其他栏目页: BreadcrumbList
"""
import os
import re
import json

BASE_URL = "https://ramanamaharshi.space"
PAGES_DIR = "c:/Users/willp/WorkBuddy/20260410104230/pages"
EXCLUDE_FILES = {"_template.html", "sitemap.html"}


def get_url_path(filepath):
    """将文件路径转换为URL路径"""
    rel = os.path.relpath(filepath, PAGES_DIR).replace(os.sep, "/")
    if rel.endswith(".html"):
        rel = rel[:-5]
    if rel.endswith("/index"):
        rel = rel[:-6] or "/"
    if rel == "" or rel == "/":
        return "/"
    if not rel.startswith("/"):
        rel = "/" + rel
    return rel


def detect_page_type(filepath, rel_path):
    """
    返回 (page_type, page_name)
    page_type: homepage | books | book_chapter | concepts | concept_detail | 
               persons | person_detail | methods | qa | qa_page | graph | other
    """
    if rel_path == "index":
        return ("homepage", "首页")
    
    # Books
    if rel_path.startswith("books/"):
        name = rel_path[6:]  # 去掉 "books/"
        if "-" in name and any(name.startswith(x) for x in ["be-as-you-are-ch", "gems-ch", "back-to-heart-ch", 
            "talks-ch", "crumbs-ch", "timeless-ch", "reflections-ch", "surpassing-love-ch", 
            "spiritual-stories-ch"]):
            return ("book_chapter", name)
        elif name == "index":
            return ("books", "书籍总览")
        else:
            # 书籍详情/概览页
            book_titles = {
                "be-as-you-are": "走向静默，如你本来",
                "be-as-you-are": "Be As You Are",
                "gems": "宝钻集",
                "back-to-heart": "回到你心中",
                "talks": "对谈录",
                "teachings": "以言传意",
                "day-by-day": "日日与彼",
                "face-to-face": "面对面",
                "search-secret-india": "秘密印度",
                "maharshi-gospel": "马哈希福音",
                "maha-yoga": "大瑜伽",
                "guru-vachaka-kovai": "上师言颂",
                "timeless": "时代中的永恒",
                "reflections": "反思录",
                "spiritual-stories": "灵性故事",
                "surpassing-love": "超越爱与恩典",
                "crumbs": "桌边碎语",
                "collected-works": "全集",
                "saint-maugham": "圣者（毛姆）",
            }
            title = book_titles.get(name, name.replace("-", " ").title())
            return ("book_detail", title)
    
    # Concepts
    if rel_path.startswith("concepts/"):
        name = rel_path[9:]
        if name == "index":
            return ("concepts", "核心概念")
        concept_names = {
            "atman": "真我 (Atman)",
            "awareness": "觉知 (Awareness)",
            "bhakti": "虔信 (Bhakti)",
            "brahman": "梵 (Brahman)",
            "ego": "自我 (Ego/Ahamkara)",
            "enlightenment": "开悟 (Enlightenment)",
            "fate": "命运 (Fate)",
            "freewill": "自由意志 (Free Will)",
            "grace": "恩典 (Grace)",
            "guru": "上师 (Guru)",
            "heart": "本心 (Heart)",
            "japa": "念诵 (Japa)",
            "jnana": "智识 (Jnana)",
            "jnani": "觉者 (Jnani)",
            "karma": "业力 (Karma)",
            "maya": "摩耶 (Maya)",
            "mind": "心智 (Mind)",
            "moksha": "解脱 (Moksha)",
            "peace": "安宁 (Peace)",
            "sahaja": "自然状态 (Sahaja)",
            "samadhi": "三摩地 (Samadhi)",
            "samsara": "轮回 (Samsara)",
            "satchidananda": "存在-意识-喜悦 (Satchidananda)",
            "self-enquiry": "参究法 (Self-Enquiry)",
            "self": "自我 (Self)",
            "silence": "静默 (Silence)",
            "surrender": "归伏/臣服 (Surrender)",
            "svasthya": "安住本位 (Svasthya)",
            "thoughts": "念头 (Thoughts/Vrittis)",
            "whoami": "我是谁？(Who Am I?)",
            "world": "世界 (World)",
        }
        cname = concept_names.get(name, name.replace("-", " ").title())
        return ("concept_detail", cname)
    
    # Persons
    if rel_path.startswith("persons/"):
        name = rel_path[8:]
        if name == "index":
            return ("persons", "关键人物")
        person_names = {
            "ramana": "室利·拉玛那·马哈希",
            "venkataramana": "韦卡罗达·南达（母亲）",
            "david": "大卫·高德曼",
        }
        pname = person_names.get(name, name.replace("-", " ").title())
        return ("person_detail", pname)
    
    # Methods
    if rel_path.startswith("methods/"):
        return ("methods", "修行方法")
    
    # QA
    if rel_path.startswith("qa/"):
        name = rel_path[3:]
        if name == "index":
            return ("qa", "精选问答")
        else:
            return ("qa_page", f"问答 {name}")
    
    # Graph
    if rel_path == "graph":
        return ("graph", "知识图谱")
    
    return ("other", os.path.basename(filepath)[:-5])


def make_breadcrumb(url_path, items):
    """生成 BreadcrumbList JSON-LD"""
    breadcrumbs = []
    for i, (name, url) in enumerate(items):
        breadcrumbs.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": name,
            "item": BASE_URL + url
        })
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumbs
    }


def make_schema(page_type, page_name, url_path):
    """根据页面类型生成对应的 JSON-LD Schema"""
    schemas = []
    
    # BreadcrumbList - 所有页面都有
    breadcrumb_items = [("拉玛那马哈希Space", "/")]
    
    if page_type == "homepage":
        pass  # 首页只有一项
    elif page_type in ("book_detail", "book_chapter"):
        breadcrumb_items.append(("书籍", "/books"))
        if page_type == "book_chapter":
            # 从章节名推断书籍名
            parts = page_name.rsplit(" ", 1)
            if len(parts) > 1 and parts[1].startswith("第"):
                breadcrumb_items.append((parts[0], f"/books/{url_path.split('/')[-2] if '/' in url_path else ''}"))
        else:
            breadcrumb_items.append((page_name, url_path))
    elif page_type == "concept_detail":
        breadcrumb_items.append(("核心概念", "/concepts"))
        breadcrumb_items.append((page_name, url_path))
    elif page_type == "person_detail":
        breadcrumb_items.append(("关键人物", "/persons"))
        breadcrumb_items.append((page_name, url_path))
    elif page_type in ("qa_page",):
        breadcrumb_items.append(("精选问答", "/qa"))
    elif page_type in ("books",):
        breadcrumb_items.append(("书籍总览", url_path))
    elif page_type in ("concepts",):
        breadcrumb_items.append(("核心概念", url_path))
    elif page_type in ("persons",):
        breadcrumb_items.append(("关键人物", url_path))
    elif page_type in ("methods",):
        breadcrumb_items.append(("修行方法", url_path))
    elif page_type in ("qa",):
        breadcrumb_items.append(("精选问答", url_path))
    elif page_type == "graph":
        breadcrumb_items.append(("知识图谱", url_path))
    
    schemas.append(make_breadcrumb(url_path, breadcrumb_items))
    
    # 页面特定 Schema
    if page_type == "homepage":
        schemas.insert(0, {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "拉玛那马哈希Space",
            "url": BASE_URL,
            'description': "\u5ba4\u5229\u00b7\u62c9\u739b\u90a3\u00b7\u9a6c\u54c8\u5e0c\u7075\u6027\u6559\u793a\u4e2d\u6587\u77e5\u8bc6\u5e93\uff1a18\u90e8\u7ecf\u5178\u4f5c\u300130+\u6838\u5fc3\u6982\u5ff5\u3001150+\u7cbe\u9009\u95ee\u7b54\u30013\u4f4d\u5173\u952e\u4eba\u7269\u4f20\u8bb0",
            'inLanguage': "zh-CN",
            'potentialAction': {
                '@type': 'SearchAction',
                'target': {'@type': 'EntryPoint', 'urlTemplate': f'{BASE_URL}/?q={{search_term_string}}'},
                'query-input': 'required name=search_term_string'
            }
        })
    
    elif page_type == "person_detail" and "马哈希" in page_name:
        schemas.insert(0, {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": "室利·拉玛那·马哈希",
            "alternateName": ["Sri Ramana Maharshi", "Bhagavan"],
            'jobTitle': "灵性导师 / 圣者",
            'description': "印度20世纪最具影响力的不二论（Advaita Vedanta）圣者之一。1879年生于南印度Tiruchuli，1896年在Madurai经历死亡体验后觉醒，随后前往阿鲁那佳拉圣山，终身在山脚下静默教导，以'参究自我'（Who am I?）为核心法门影响无数求道者。",
            'birthDate': "1879-12-30",
            'deathDate': "1950-04-14",
            'birthPlace': {"@type": "Place", "name": "Tiruchuli, Tamil Nadu, India"},
            'deathPlace': {"@type": "Place", "name": "阿鲁那佳拉圣山脚下的Ramana Ashramam, Tiruvannamalai"},
            'knowsAbout': ["不二论 Advaita Vedanta", "自我参究 Self-Enquiry", "静默教导 Silent Teachings", "归伏 Surrender"],
            'sameAs': [
                "https://en.wikipedia.org/wiki/Ramana_Maharshi"
            ],
            'image': f"{BASE_URL}/images/ramana.jpg",
            'url': f"{BASE_URL}{url_path}"
        })
    
    elif page_type == "book_detail":
        schemas.insert(0, {
            "@context": "https://schema.org",
            "@type": "Book",
            "name": page_name,
            "inLanguage": "zh-CN",
            "bookFormat": "https://schema.org/EBook",
            'genre': "Spirituality, Philosophy, Advaita Vedanta",
            'description': f"{page_name} — 拉玛那马哈希教示经典著作，涵盖其核心教导：自我参究、静默、归伏等修行法门。",
            'author': [{"@type": "Person", "name": "室利·拉玛那·马哈希"}],
            'url': f"{BASE_URL}{url_path}"
        })
    
    elif page_type == "concept_detail":
        schemas.insert(0, {
            "@context": "https://schema.org",
            "@type": "Article",
            'headline': f'{page_name} — 拉玛那马哈希核心概念详解',
            'description': f'深入了解{page_name}在拉玛那马哈希教示中的含义、实践方法和相关引文。',
            'inLanguage': "zh-CN",
            'articleSection': "Philosophy",
            'about': {'@type': 'Thing', 'name': page_name},
            'author': {'@type': 'Organization', 'name': '拉玛那马哈希Space'},
            'publisher': {'@type': 'Organization', 'name': '拉玛那马哈希Space', 'url': BASE_URL},
            'url': f"{BASE_URL}{url_path}"
        })
    
    elif page_type == "qa_page":
        schemas.insert(0, {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            'name': f'拉玛那马哈希 {page_name}',
            'description': '关于拉玛那马哈希灵性教导的问答精选',
            'mainEntity': []  # 实际FAQ项需要从HTML中提取，这里先放框架
        })
    
    return schemas


def inject_json_ld(content, filepath, page_type, page_name, url_path):
    """将 JSON-LD 注入到 HTML 的 </head> 前"""
    schemas = make_schema(page_type, page_name, url_path)
    
    if not schemas:
        return content
    
    json_ld_blocks = []
    for schema in schemas:
        json_str = json.dumps(schema, ensure_ascii=False, indent=2)
        block = f'<script type="application/ld+json">\n{json_str}\n</script>'
        json_ld_blocks.append(block)
    
    combined = "\n".join(json_ld_blocks)
    injection = f"\n  <!-- SEO JSON-LD Structured Data -->\n  {combined}\n"
    
    # 在 </head> 前注入
    if "</head>" in content:
        content = content.replace("</head>", injection + "</head>")
    else:
        # 备选：在 <body> 后或文件末尾
        content = injection + content
    
    return content


def main():
    count = 0
    errors = []
    
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
                
                rel_path = get_url_path(fpath).lstrip("/")
                page_type, page_name = detect_page_type(fpath, rel_path)
                url_path = "/" + rel_path if rel_path != "/" else "/"
                
                new_content = inject_json_ld(content, fpath, page_type, page_name, url_path)
                
                if new_content != content:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
                    
                    display_rel = os.path.relpath(fpath, PAGES_DIR)
                    print(f"  [OK] {display_rel} → type={page_type}, name={page_name}")
                    
            except Exception as e:
                errors.append((fpath, str(e)))
                print(f"  [ERR] {fname}: {e}")
    
    print(f"\n=== 完成！共为 {count} 个文件注入了 JSON-LD 结构化数据 ===")
    if errors:
        print(f"\n⚠️ {len(errors)} 个文件出错:")
        for fp, err in errors[:5]:
            print(f"  - {fp}: {err}")


if __name__ == "__main__":
    main()
