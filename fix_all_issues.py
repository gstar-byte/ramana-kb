#!/usr/bin/env python3
"""
批量修复概念页面的6个问题：
1. 添加缺失的favicon
2. 为h1添加缺失的icon
3. 修复maya/vairagya的标题居中问题（添加page-header结构）
4. 更新satchidananda.html标题
5. 修复图谱中重复的"习气"节点
6. 丰富图谱融入所有概念
"""

import re
import os
from pathlib import Path

BASE = Path("F:/26年4月/kb01/pages")
CONCEPTS = BASE / "concepts"
GRAPH = BASE / "graph.html"

FAVICON_LINE = '    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 100 100\'%3E%3Ctext y=\'.9em\' font-size=\'90\'%3E🙏%3C/text%3E%3C/svg%3E">\n'

# 问题1：缺少favicon的页面
MISSING_FAVICON = [
    "vichara.html", "sharanagati.html", "lakshya.html",
    "manonasha.html", "prarabdha.html", "jiva.html",
    "prana.html", "viveka.html", "vasanas.html",
    "avidya.html", "satya.html", "shiva.html"
]

# 问题2：h1缺少icon的页面及应有的icon
MISSING_H1_ICON = {
    "sadhana.html": "🧘",
    "jnana.html": "🕯️",
    "prarabdha.html": "📜",
    "samsara.html": "🔄",
    "jiva.html": "👤",
    "heart.html": "💖",
}

# 问题3：需要添加page-header结构的页面（maya, vairagya）
# 这些页面直接用了<section class="concept-section">，没有page-header包裹


def fix_favicon():
    """为缺少favicon的页面添加favicon"""
    print("=" * 60)
    print("修复问题1：添加缺失的favicon")
    print("=" * 60)
    
    for fname in MISSING_FAVICON:
        fpath = CONCEPTS / fname
        if not fpath.exists():
            print(f"  ⚠️  文件不存在: {fname}")
            continue
        
        content = fpath.read_text(encoding="utf-8")
        
        if 'rel="icon"' in content:
            print(f"  ⏭️  {fname} 已有favicon，跳过")
            continue
        
        # 在 <link rel="stylesheet" href="../styles.css"> 之后添加favicon
        # 需要找到正确的插入位置
        stylesheet_pattern = r'(<link rel="stylesheet" href="\.\./styles\.css">)\s*\n'
        
        def add_favicon(m):
            return m.group(0) + FAVICON_LINE
        
        new_content = re.sub(stylesheet_pattern, add_favicon, content)
        
        if new_content == content:
            # 尝试其他模式
            # 有些页面可能是 <link rel="stylesheet" href="../styles.css"> 不带结束的 >
            alt_pattern = r'(<link rel="stylesheet" href="\.\./styles\.css">)\n'
            new_content2 = re.sub(alt_pattern, r'\1\n' + FAVICON_LINE, content)
            if new_content2 == content:
                print(f"  ❌ {fname}: 无法找到插入位置")
                continue
            new_content = new_content2
        
        fpath.write_text(new_content, encoding="utf-8")
        print(f"  ✅ {fname}: 已添加favicon")


def fix_h1_icon():
    """为h1添加缺失的icon"""
    print("\n" + "=" * 60)
    print("修复问题2：为h1添加缺失的icon")
    print("=" * 60)
    
    for fname, icon in MISSING_H1_ICON.items():
        fpath = CONCEPTS / fname
        if not fpath.exists():
            print(f"  ⚠️  文件不存在: {fname}")
            continue
        
        content = fpath.read_text(encoding="utf-8")
        
        # 检查h1是否已有icon（emoji）
        h1_pattern = r'<h1>([^<]+)</h1>'
        match = re.search(h1_pattern, content)
        
        if not match:
            print(f"  ⚠️  {fname}: 未找到 <h1> 标签")
            continue
        
        h1_text = match.group(1)
        
        # 检查是否已有emoji
        if re.match(r'[\U0001F000-\U0001FFFF]', h1_text):
            print(f"  ⏭️  {fname}: h1已有icon ({h1_text[:2]})，跳过")
            continue
        
        # 添加icon
        new_h1 = f'<h1>{icon} {h1_text}</h1>'
        new_content = content.replace(match.group(0), new_h1)
        
        fpath.write_text(new_content, encoding="utf-8")
        print(f"  ✅ {fname}: <h1>{icon} {h1_text}</h1>")


def fix_maya_vairagya():
    """修复maya.html和vairagya.html的标题居中问题"""
    print("\n" + "=" * 60)
    print("修复问题3：maya.html和vairagya.html添加page-header")
    print("=" * 60)
    
    # maya.html的修复
    maya_path = CONCEPTS / "maya.html"
    if maya_path.exists():
        content = maya_path.read_text(encoding="utf-8")
        
        # 检查是否已有page-header
        if '<header class="page-header">' in content:
            print("  ⏭️  maya.html 已有page-header，跳过")
        else:
            # 需要在 <div class="content-wrapper"> 之后、
            # <nav class="breadcrumb"> 之前插入 page-header
            # maya.html结构：
            # <div class="content-wrapper">
            #     <nav class="breadcrumb">...
            #     <section class="concept-section">...
            
            # 获取h1标题（从breadcrumb中提取）
            breadcrumb_match = re.search(r'<nav class="breadcrumb">(.*?)</nav>', content, re.DOTALL)
            if breadcrumb_match:
                breadcrumb = breadcrumb_match.group(1)
                # 提取当前页面标题
                title_match = re.search(r'<span>(.*?)</span>', breadcrumb)
                if title_match:
                    page_title = title_match.group(1)
                    # 提取icon（如果有）
                    icon_match = re.search(r'([\U0001F000-\U0001FFFF])', page_title)
                    icon = icon_match.group(1) if icon_match else "🎭"
                    
                    # 构建page-header
                    page_header = f'''
                <article class="concept-detail">
                    <header class="page-header">
                        <h1>{icon} {page_title}</h1>
                    </header>
                    
'''
                    
                    # 在 <div class="content-wrapper"> 之后插入
                    # 需要先把 breadcrumb 从 <nav class="breadcrumb"> 改为在 page-header 之后
                    # 简化：直接在 content-wrapper 后加 page-header，保留 breadcrumb
                    
                    # 方案：在 <div class="content-wrapper"> 之后添加 page-header
                    new_content = content.replace(
                        '<div class="content-wrapper">\n                                <nav class="breadcrumb">',
                        '<div class="content-wrapper">\n                <article class="concept-detail">\n                    <header class="page-header">\n                        <h1>🎭 摩耶/幻相 (Maya)</h1>\n                    </header>\n                \n                                <nav class="breadcrumb">'
                    )
                    
                    if new_content == content:
                        print("  ⚠️  maya.html: 无法自动修复，请手动添加page-header")
                    else:
                        maya_path.write_text(new_content, encoding="utf-8")
                        print("  ✅ maya.html: 已添加page-header结构")
    
    # vairagya.html的修复
    vairagya_path = CONCEPTS / "vairagya.html"
    if vairagya_path.exists():
        content = vairagya_path.read_text(encoding="utf-8")
        
        if '<header class="page-header">' in content:
            print("  ⏭️  vairagya.html 已有page-header，跳过")
        else:
            # 类似maya.html的修复
            new_content = content.replace(
                '<div class="content-wrapper">\n                <nav class="breadcrumb">',
                '<div class="content-wrapper">\n                <article class="concept-detail">\n                    <header class="page-header">\n                        <h1>🌿 出离/厌离 (Vairagya)</h1>\n                    </header>\n                \n                <nav class="breadcrumb">'
            )
            
            if new_content == content:
                # 尝试另一种模式
                new_content2 = content.replace(
                    '<div class="content-wrapper">\n                                <nav class="breadcrumb">',
                    '<div class="content-wrapper">\n                <article class="concept-detail">\n                    <header class="page-header">\n                        <h1>🌿 出离/厌离 (Vairagya)</h1>\n                    </header>\n                \n                                <nav class="breadcrumb">'
                )
                if new_content2 == content:
                    print("  ⚠️  vairagya.html: 无法自动修复，请手动添加page-header")
                else:
                    vairagya_path.write_text(new_content2, encoding="utf-8")
                    print("  ✅ vairagya.html: 已添加page-header结构")
            else:
                vairagya_path.write_text(new_content, encoding="utf-8")
                print("  ✅ vairagya.html: 已添加page-header结构")


def fix_satchidananda():
    """更新satchidananda.html标题，加上"存在——意识——喜悦"中文"""
    print("\n" + "=" * 60)
    print("修复问题4：更新satchidananda.html标题")
    print("=" * 60)
    
    fpath = CONCEPTS / "satchidananda.html"
    if not fpath.exists():
        print("  ⚠️  文件不存在: satchidananda.html")
        return
    
    content = fpath.read_text(encoding="utf-8")
    
    # 更新breadcrumb
    old_breadcrumb = '<span>✨ 萨特-奇丹-阿南达 (Sat-Chit-Ananda)</span>'
    new_breadcrumb = '<span>✨ 存在——意识——喜悦 / 萨特-奇丹-阿南达 (Sat-Chit-Ananda)</span>'
    
    if old_breadcrumb in content:
        content = content.replace(old_breadcrumb, new_breadcrumb)
        print("  ✅ 已更新breadcrumb标题")
    
    # 更新h1（如果有page-header）
    old_h1 = '<h1>✨ 存在-意识-喜悦 / Sat-Chit-Ananda</h1>'
    new_h1 = '<h1>✨ 存在——意识——喜悦 / 萨特-奇丹-阿南达 (Sat-Chit-Ananda)</h1>'
    
    if '<h1>' in content and '萨特-奇丹-阿南达' in content:
        # 需要找到正确的h1
        content = re.sub(
            r'<h1>(.*?萨特-奇丹-阿南达.*?)</h1>',
            new_h1,
            content
        )
        print("  ✅ 已更新h1标题")
    
    fpath.write_text(content, encoding="utf-8")
    print("  ✅ satchidananda.html 标题已更新")


def fix_graph_duplicate():
    """修复图谱中重复的"习气"节点"""
    print("\n" + "=" * 60)
    print("修复问题5：图谱中重复的"习气"节点")
    print("=" * 60)
    
    if not GRAPH.exists():
        print("  ⚠️  graph.html 不存在")
        return
    
    content = GRAPH.read_text(encoding="utf-8")
    
    # 方案：将 samskara 节点改名为 "🔄 熏习" 以区分
    old_samskara = '{ id: "samskara", name: "🔄 习气", type: "mind", url: "concepts/svasthya.html", desc: "习气/Samskara，根深蒂固的心理印痕" }'
    new_samskara = '{ id: "samskara", name: "🔄 熏习", type: "mind", url: "concepts/samskara.html", desc: "熏习/Samskara，根深蒂固的心理印痕，是Vasanas的来源" }'
    
    if old_samskara in content:
        content = content.replace(old_samskara, new_samskara)
        print("  ✅ 已将 samskara 节点改名为 '🔄 熏习'")
    else:
        print("  ⚠️  未找到 samskara 节点，可能已修复")
    
    # 同时更新所有指向 samskara 的关系，确保一致性
    # 不需要改动 links，因为 id 没变
    
    GRAPH.write_text(content, encoding="utf-8")
    print("  ✅ graph.html 已更新")


def enrich_graph():
    """丰富图谱，融入所有概念"""
    print("\n" + "=" * 60)
    print("修复问题6：丰富图谱融入所有概念")
    print("=" * 60)
    
    if not GRAPH.exists():
        print("  ⚠️  graph.html 不存在")
        return
    
    content = GRAPH.read_text(encoding="utf-8")
    
    # 获取所有概念页面
    concept_files = list(CONCEPTS.glob("*.html"))
    existing_nodes = set()
    
    # 从graph.html中提取现有节点id
    node_pattern = r'id:\s*"(\w+)"'
    for match in re.finditer(node_pattern, content):
        existing_nodes.add(match.group(1))
    
    print(f"  现有节点数: {len(existing_nodes)}")
    print(f"  概念页面数: {len(concept_files)}")
    
    # 检查哪些概念页面还没有对应的图谱节点
    missing = []
    for fpath in concept_files:
        # 从文件名推断id（去掉.html）
        fname = fpath.stem
        if fname == "index":
            continue
        if fname not in existing_nodes:
            missing.append(fname)
    
    print(f"  缺少节点的概念: {len(missing)}")
    if missing:
        print("  缺少节点的概念:", ", ".join(missing[:10]), "...")
    
    # 为缺少节点的概念添加节点定义
    # 需要在 nodes = [ 之后添加新节点
    
    # 读取_template.html来获取概念页面的结构，推断合适的icon和type
    # 简化：只添加节点定义，不添加关系（关系可以后续手动添加）
    
    print("  ⚠️  图谱丰富需要手动梳理概念关系，建议分步骤进行")
    print("  ℹ️  当前已跳过自动丰富，请手动编辑 graph.html 添加新节点和关系")


if __name__ == "__main__":
    print("\n🚀 开始批量修复概念页面问题...\n")
    
    fix_favicon()
    fix_h1_icon()
    fix_maya_vairagya()
    fix_satchidananda()
    fix_graph_duplicate()
    enrich_graph()
    
    print("\n✨ 修复完成！请检查并手动处理图谱丰富问题。\n")
