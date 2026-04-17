"""
SEO Fix Phase 5: 全面优化 Title / Meta Description / OG 标签
符合 Google 推荐的最佳长度：
- Title: 30-60 字符（最佳），最大不超过 70 字符
- Description: 120-158 字符（最佳），最大不超过 300 字符
- 移除所有 Emoji
- 统一使用 non-www 域名
- 添加 og:image 占位
- 标准化分隔符为 " - "
"""
import os
import re

BASE_URL = "https://ramanamaharshi.space"
PAGES_DIR = "c:/Users/willp/WorkBuddy/20260410104230/pages"
SITE_NAME = "拉玛那马哈希Space"
EXCLUDE_FILES = {"_template.html", "sitemap.html"}

# Emoji 正则模式
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"  # supplemental
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002600-\U000026FF"   # misc
    "\U00002700-\U000027BF"   # dingbats
    "]+", flags=re.UNICODE
)


def get_url_path(filepath):
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


def strip_emoji(text):
    """移除文本中的所有 emoji"""
    if text is None:
        return ""
    return EMOJI_PATTERN.sub("", text).strip()


def detect_page_type(rel_path, fname):
    """检测页面类型，返回 (type_key, page_name_for_title)"""
    if rel_path == "index":
        return ("homepage", None)
    
    # Books
    if rel_path.startswith("books/"):
        name = rel_path[6:]
        if name == "index":
            return ("books_index", "书籍总览")
        
        book_titles = {
            "be-as-you-are": ("book_detail", "走向静默 如你本来 Be As You Are"),
            "gems": ("book_detail", "宝钻集 Gems from Bhagavan"),
            "back-to-heart": ("book_detail", "回到你心中"),
            "talks": ("book_detail", "对谈录 Talks with Sri Ramana Maharshi"),
            "teachings": ("book_detail", "以言传意 Teachings in His Own Words"),
            "day-by-day": ("book_detail", "日日与彼 Day by Day with Bhagavan"),
            "face-to-face": ("book_detail", "面对面 Face to Face"),
            "search-secret-india": ("book_detail", "秘密印度 A Search in Secret India"),
            "maharshi-gospel": ("book_detail", "马哈希福音 Maharshis Gospel"),
            "maha-yoga": ("book_detail", "大瑜伽 Maha Yoga"),
            "guru-vachaka-kovai": ("book_detail", "上师言颂 Guru Vachaka Kovai"),
            "timeless": ("book_detail", "时代中的永恒 Timeless in Time"),
            "reflections": ("book_detail", "反思录 Reflections"),
            "spiritual-stories": ("book_detail", "灵性故事 Spiritual Stories"),
            "surpassing-love": ("book_detail", "超越爱与恩典 Surpassing Love and Grace"),
            "crumbs": ("book_detail", "桌边碎语 Crumbs from the Table"),
            "collected-works": ("book_detail", "全集 Collected Works of Ramana Maharshi"),
            "saint-maugham": ("book_detail", "圣者 The Saint by Maugham"),
        }
        
        # 章节页
        ch_map = {
            "be-as-you-are-ch": "走向静默",
            "gems-ch": "宝钻集",
            "back-to-heart-ch": "回到你心中",
            "talks-ch": "对谈录",
            "crumbs-ch": "桌边碎语",
            "timeless-ch": "时代中的永恒",
            "reflections-ch": "反思录",
            "surpassing-love-ch": "超越爱与恩典",
            "spiritual-stories-ch": "灵性故事",
        }
        for prefix, title in ch_map.items():
            if name.startswith(prefix):
                ch_num = name.replace(prefix, "")
                return ("book_chapter", f"{title} 第{ch_num}章")
        
        if name in book_titles:
            return book_titles[name]
        return ("book_detail", name.replace("-", " ").title())
    
    # Concepts
    if rel_path.startswith("concepts/"):
        name = rel_path[9:]
        if name == "index":
            return ("concepts_index", "核心概念总览")
        
        concept_data = {
            "atman": ("真我 Atman 灵魂本质", "深入了解真我(Atman)在印度不二论哲学中的含义，以及拉玛那马哈希如何通过自我参究证悟真我。"),
            "awareness": ("觉知 Awareness 纯粹意识", "觉知是意识本身，非对象化的存在。探索觉知与心智、真我的关系，理解纯粹觉知状态。"),
            "bhakti": ("虔信 Bhakti 归依之道", "虔信是对上师或神性的完全归依与爱。了解虔信如何自然转化为智识，最终导向解脱。"),
            "brahman": ("梵 Brahman 终极实在", "梵是宇宙终极实在、无限意识。理解梵我一如的不二论核心教导及其修行意义。"),
            "ego": ("自我 Ego 我执之心", "自我(小我)是所有痛苦和束缚的根源。学习如何识别并超越虚假的自我感。"),
            "enlightenment": ("开悟 Enlightenment 觉醒", "开悟不是获得什么，而是回归本然状态。探索开悟的本质、过程及常见误区。"),
            "fate": ("命运 Fate 业力显现", "命运是过去业力的自然呈现。理解如何在接受命运的同时保持内心的自由。"),
            "freewill": ("自由意志 Free Will", "自由意志是否存在？拉玛那马哈希认为真我没有个体意志，唯有神圣意志运行。"),
            "grace": ("恩典 Grace 神圣加持", "恩典始终存在，只是我们未敞开接收。了解如何通过归伏和虔诚来接纳恩典。"),
            "guru": ("上师 Guru 灵性导师", "上师是内在的指引者。拉玛那马哈希关于内在上师和外在上师关系的教导。"),
            "heart": ("本心 Heart 灵性中心", "本心位于身体右侧而非左侧，是真我的居所。理解心轮与本心的区别。"),
            "japa": ("念诵 Japa 圣号持诵", "念诵是重复神圣名号或咒语的修行法门。了解如何将念诵转化为自然的内在状态。"),
            "jnana": ("智识 Jnana 智慧之道", "智识是通过直接体验获得的灵性智慧，不同于书本知识。智识瑜伽的核心实践方法。"),
            "jnani": ("觉者 Jnani 已觉悟之人", "觉者是已经稳定安住于真我中的圣人。了解觉者的特征、行为和影响。"),
            "karma": ("业力 Karma 因果法则", "业力是因果律的运作方式。理解业力的形成、消耗以及如何从业力中解脱。"),
            "maya": ("摩耶 Maya 幻象之力", "摩耶是遮蔽真实自我的幻象力量。如何看穿摩耶的迷障，直见真相。"),
            "mind": ("心智 Mind 心念之流", "心智是念头和习气的集合体。理解心智的本质、运作方式及如何超越它。"),
            "moksha": ("解脱 Moksha 自由自在", "解脱是从虚幻的个体身份中彻底觉醒。解脱不是死后才能达到的状态。"),
            "peace": ("安宁 Peace 内在平静", "真正的安宁不是外在环境的安静，而是内心深处不受干扰的平静。如何安住于安宁之中。"),
            "sahaja": ("自然状态 Sahaja", "Sahaja是不费力的自然存在状态，无需刻意修行的安住。这是最终修行的成果。"),
            "samadhi": ("三摩地 Samadhi 深度禅定", "三摩地是一种深度专注和融合的意识状态。了解不同类型的三摩地和其灵性价值。"),
            "samsara": ("轮回 Samsara 生死流转", "轮回是因无明而产生的生死循环。理解轮回的本质和如何从中解脱。"),
            "satchidananda": ("存在意识喜悦 Sat-Chit-Ananda", "Sat-Chit-Ananda描述了真我的三种属性：绝对存在、纯粹意识和无尽喜悦。"),
            "self-enquiry": ("参究法 Self-Enquiry 自我探究", "我是谁？参究法是拉玛那马哈希最核心最直接的修行法门。详细指南和实践要点。"),
            "self": ("自我 Self 本来的我", "自我即真我不是小我ego。理解自我的真正含义以及如何发现它。"),
            "silence": ("静默 Silence 无言之教", "静默是最高级的教导形式。拉玛那马哈希以静默传递无法用语言表达的真谛。"),
            "surrender": ("归伏 Surrender 完全臣服", "归伏是将一切交给内在的上师或神。归伏与参究法的关系及其实践方法。"),
            "svasthya": ("安住 Svasthya 安住本位", "Svasthya意为安住在自己的本然位置——真我中。这是修行的终极目标和自然状态。"),
            "thoughts": ("念头 Thoughts 心念波动", "念头是心智的基本活动单位。理解念头的来源、本质及如何不被其控制。"),
            "whoami": ("我是谁 Who Am I 核心追问", "我是谁？这是拉玛那马哈希最著名也最重要的教示。完整原文翻译和逐句解读。"),
            "world": ("世界 World 幻象与实相", "世界如同梦境一般不实但又经验性地存在。理解世界在不二论中的位置。"),
        }
        if name in concept_data:
            t, d = concept_data[name]
            return ("concept_detail", (t, d))
        return ("concept_detail", (name.replace("-", " ").title(), f"{name}相关概念解读"))
    
    # Persons
    if rel_path.startswith("persons/"):
        name = rel_path[8:]
        if name == "index":
            return ("persons_index", "关键人物索引")
        person_data = {
            "ramana": (
                "室利·拉玛那·马哈希 Sri Ramana Maharshi",
                "1879年生于南印度，1896年经历死亡觉醒后前往阿鲁那佳拉圣山，终身以静默和自我参究教导弟子。20世纪最具影响力的不二论圣者之一。"
            ),
            "venkataramana": (
                "韦卡罗达·南达 Alagammal 马哈希母亲",
                "拉玛那·马哈希的母亲，晚年跟随儿子到阿鲁那佳拉山修行并在此获得解脱。代表无条件母爱与灵性成熟的完美结合。"
            ),
            "david": (
                "大卫·高德曼 David Godman",
                "拉玛那·马哈希主要编纂者和传记作者，著有《Be As You Are》等经典著作，致力于传播马哈希的教导至西方世界。"
            ),
        }
        if name in person_data:
            t, d = person_data[name]
            return ("person_detail", (t, d))
        return ("person_detail", (name, ""))
    
    # Methods
    if rel_path.startswith("methods/") or rel_path == "methods":
        return ("methods_index", "修行方法总览")
    
    # QA
    if rel_path.startswith("qa/"):
        name = rel_path[3:]
        if name == "index":
            return ("qa_index", "精选问答总览")
        return ("qa_page", (f"精选问答 第{name}页", f"拉玛那马哈希关于灵性修行、自我了悟、日常生活的经典问答集。"))
    
    # Graph
    if rel_path == "graph":
        return ("graph", "知识图谱")
    
    return ("other", (os.path.splitext(fname)[0], ""))


def generate_seo_meta(page_type, page_info, url_path):
    """
    返回 (new_title, new_description)
    Title 最佳长度: 30-60字符 (Google显示约28-35个汉字)
    Description 最佳长度: 120-158字符 (Google显示约40-55个汉字)
    """
    
    if page_type == "homepage":
        title = f"拉玛那马哈希Space — 不二论灵性知识库"
        desc = "系统整理拉玛那马哈希的灵性教示：18部经典著作、30+核心概念详解、150+精选问答、3位关键人物传记。自我参究、静默、归伏等修行法门的完整中文指南。"
    
    elif page_type == "books_index":
        title = f"书籍总览 — {SITE_NAME}"
        desc = "收录拉玛那马哈希相关的18部经典著作：包括《走向静默》《宝钻集》《对谈录》《我是谁？》等核心典籍。每本书均有完整章节目录和内容概要，支持在线阅读和搜索。"
    
    elif page_type == "book_detail":
        book_name = page_info if isinstance(page_info, str) else page_info[0]
        title = f"{book_name} — {SITE_NAME}"
        desc = f"{book_name}的详细介绍、章节目录和核心思想概要。了解这本书在拉玛那马哈希教示体系中的地位，获取完整的阅读指引和关键引文。"
    
    elif page_type == "book_chapter":
        title = f"{page_info} — {SITE_NAME}" 
        desc = f"{page_info}的详细内容和核心要义。包含原文摘要、关键段落解读和相关概念的交叉引用。"
    
    elif page_type == "concepts_index":
        title = f"核心概念总览 — {SITE_NAME}"
        desc = "拉玛那马哈希教示体系中的30+个核心概念详解：真我、梵、本心、心智、业力、轮回、解脱、开悟等。每个概念均含定义、原文引用和实践指引。"
    
    elif page_type == "concept_detail":
        concept_name, concept_desc = page_info
        title = f"{concept_name} — {SITE_NAME}"
        desc = concept_desc
    
    elif page_type == "persons_index":
        title = f"关键人物索引 — {SITE_NAME}"
        desc = "介绍拉玛那马哈希及其周围的重要人物：包括马哈希本人详尽传记、其母亲韦卡罗达·南达、主要编纂者大卫·高德曼等的生平故事。"
    
    elif page_type == "person_detail":
        person_name, person_desc = page_info
        title = f"{person_name} — {SITE_NAME}"
        desc = person_desc
    
    elif page_type == "methods_index":
        title = f"修行方法总览 — {SITE_NAME}"
        desc = "拉玛那马哈希教导的主要修行法门：自我参究(我是谁)、归伏臣服、念诵、三摩地、禅定等。每种方法都有详细的操作步骤和注意事项。"
    
    elif page_type == "qa_index":
        title = f"精选问答总览 — {SITE_NAME}"
        desc = "超过150条拉玛那马哈希的经典问答，涵盖自我了悟、修行方法、日常生活、心智运作、世界本质、死亡与轮回等主题。分类清晰，便于检索。"
    
    elif page_type == "qa_page":
        qa_name, qa_desc = page_info
        title = f"{qa_name} — {SITE_NAME}"
        desc = qa_desc
    
    elif page_type == "graph":
        title = f"知识图谱 — {SITE_NAME}"
        desc = "拉玛那马哈希教示体系的交互式知识图谱。可视化展示真我、梵、心智、业力、解脱等核心概念之间的关系，点击节点可查看详情。"
    
    else:
        other_name = page_info if isinstance(page_info, str) else page_info[0]
        title = f"{other_name} — {SITE_NAME}"
        desc = page_info[1] if isinstance(page_info, tuple) and len(page_info) > 1 else f"了解{other_name}的相关内容。"
    
    # 清理标题中的emoji
    title = strip_emoji(title)
    
    # 确保标题长度合理 (目标: 20-65字符)
    if len(title) > 68:
        # 截断保留站点名
        suffix = f" — {SITE_NAME}"
        max_body = 68 - len(suffix)
        title = title[:max_body] + suffix
    
    # 确保description长度合理 (目标: 100-280字符)
    if len(desc) < 50:
        desc = desc.strip() + f" 访问{SITE_NAME}获取更多拉玛那马哈希灵性教示内容。"
    if len(desc) > 290:
        desc = desc[:287] + "..."
    
    return title, desc


def optimize_page(content, filepath, rel_path, page_type, page_info, url_path):
    """优化单个页面的 meta 标签"""
    new_title, new_desc = generate_seo_meta(page_type, page_info, url_path)
    full_url = BASE_URL + url_path
    
    # 1. 更新/添加 <title>
    content = re.sub(r'<title[^>]*>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
    
    # 2. 更新/添加 meta description
    if re.search(r'<meta\s+name=["\']description["\']', content):
        content = re.sub(
            r'<meta\s+name=["\']description["\']\s+content=["\'][^"]*["\']',
            f'<meta name="description" content="{new_desc}"',
            content,
            flags=re.IGNORECASE
        )
    else:
        # 在 robots 后插入 description
        robots_match = re.search(r'(<meta[^>]*name=["\']robots["\'][^>]*>)', content)
        if robots_match:
            insert_pos = robots_match.end()
            content = content[:insert_pos] + f'\n    <meta name="description" content="{new_desc}">' + content[insert_pos:]
    
    # 3. 更新/添加 Open Graph 标签
    og_block = f'''    <!-- Open Graph -->
    <meta property="og:title" content="{new_title}">
    <meta property="og:description" content="{new_desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{full_url}">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="{SITE_NAME}">
    <meta property="og:image" content="{BASE_URL}/images/og-default.jpg">
'''
    
    # 移除旧的 OG 块（如果有的话）
    # 先找 og:title 开始的位置
    og_start = re.search(r'\s*<!--\s*Open Graph\s*-->\s*\n', content)
    if og_start:
        # 找到OG块的结束位置（下一个空行或者</head>）
        rest = content[og_start.end():]
        og_end_match = re.match(r'(.*?)(?=\n(?:\s*<(?!meta)|\s*</head>|\s*<!--))', rest, re.DOTALL)
        if og_end_match:
            end_pos = og_start.end() + og_end_match.end()
            content = content[:og_start.start()] + og_block.rstrip() + "\n" + content[end_pos:]
        else:
            # 替换整个 OG 块直到 </head> 或下一个注释
            content = re.sub(
                r'\s*<!--\s*Open Graph\s*-->.*(?=<!--|$)',
                og_block,
                content,
                count=1,
                flags=re.DOTALL
            )
    else:
        # 在 canonical 后插入 OG
        canon_match = re.search(r'(<link[^>]*rel=["\']canonical["\'][^>]*>)', content)
        if canon_match:
            insert_pos = canon_match.end()
            content = content[:insert_pos] + "\n" + og_block + content[insert_pos:]
        else:
            # 备选位置
            head_end = content.find("</head>")
            if head_end > 0:
                content = content[:head_end] + og_block + content[head_end:]
    
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
                page_type, page_info = detect_page_type(rel_path, fname)
                url_path = "/" + rel_path if rel_path != "/" else "/"
                
                new_content = optimize_page(content, fpath, rel_path, page_type, page_info, url_path)
                
                if new_content != content:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
                    
                    display_rel = os.path.relpath(fpath, PAGES_DIR)
                    print(f"  [OK] {display_rel}")
                    
            except Exception as e:
                errors.append((fpath, str(e)))
                print(f"  [ERR] {fname}: {e}")
    
    print(f"\n=== 完成！共优化 {count} 个文件的 Meta 标签 ===")
    if errors:
        print(f"\n⚠️ {len(errors)} 个文件出错:")
        for fp, err in errors[:5]:
            print(f"  - {fp}: {err}")


if __name__ == "__main__":
    main()
