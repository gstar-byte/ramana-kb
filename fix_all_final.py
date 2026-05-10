#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全面修复：添加语言切换按钮 + 修复图谱节点"""

import os
import re
from opencc import OpenCC

cc = OpenCC('s2twp')

# 繁体图谱节点映射
GRAPH_NODES = {
    # 中心
    "🙏 拉玛那": "🙏 拉瑪那",

    # 本体论
    "🔮 真我": "🔮 真我",
    "梵": "梵",
    "🌊 摩耶": "🌊 摩耶",
    "💎 本我": "💎 本我",

    # 心智与自我
    "🧠 心智": "🧠 心智",
    "🧠 自我": "🧠 自我",
    "💭 念头": "💭 念頭",

    # 修行法门
    '🔍 "我是谁？"': '🔍 "我是誰？"',
    "🤫 静默": "🤫 靜默",
    "🧘 三摩地": "🧘 三摩地",
    "🙏 臣服": "🙏 臣服",

    # 解脱与境界
    "🕊️ 解脱": "🕊️ 解脫",
    "✨ 恩典": "✨ 恩典",
    "👆 上师": "👆 上師",
    "🔄 业力": "🔄 業力",

    # 书籍
    "📖 走向静默": "📖 走向靜默",
    "💎 宝钻集": "💎 寶鑽集",
    "💬 对谈录": "💬 對談錄",
    "📕 回到心中": "📕 回到心中",
    "📅 日日与彼": "📅 日日與彼",
    "👁️ 面对面": "👁️ 面對面",

    # 人物
    "📝 高德曼": "📝 高德曼",
    "👩 南达": "👩 南達",

    # 修行相关
    "💖 本心": "💖 本心",
    "🏔️ 阿鲁那佳拉": "🏔️ 阿魯那佳拉",
    "🧘 禅定": "🧘 禪定",
    "🔮 念诵": "🔮 念誦",
    "🌿 出离": "🌿 出離",
    "🕯️ 智慧": "🕯️ 智慧",
    "🌫️ 无明": "🌫️ 無明",
    "✨ 存在-意识-喜悦": "✨ 存在-意識-喜悅",
    "🔄 熏习": "🔄 薰習",
}

def add_lang_toggle_to_file(filepath):
    """添加语言切换按钮"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 检查是否已经是繁体版
    is_zh_tw = 'lang="zh-TW"' in content

    # 如果没有语言切换按钮，添加它
    if 'lang-toggle' not in content:
        if is_zh_tw:
            toggle = '<a href="/zh-TW/" class="lang-toggle" title="切換為簡體中文">簡</a>'
            # 替换为简体版链接
            href_toggle = '<a href="/" class="lang-toggle" title="切換為簡體中文">簡</a>'
        else:
            # 简体版添加繁体切换
            href_toggle = '<a href="/zh-TW/" class="lang-toggle" title="切換為繁體中文">繁</a>'

        content = content.replace('<body>', f'<body>\n    {href_toggle}')

    return content != original

def fix_graph_nodes(filepath):
    """修复图谱节点"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 替换节点名称
    for zh_cn, zh_tw in GRAPH_NODES.items():
        content = content.replace(f'name: "{zh_cn}"', f'name: "{zh_tw}"')

    # 替换描述中的简体词
    replacements = [
        ("伟大", "偉大"),
        ("导师", "導師"),
        ("永恒", "永恆"),
        ("实相", "實相"),
        ("存在", "存在"),
        ("幻相", "幻相"),
        ("工具", "工具"),
        ("感知", "感知"),
        ("产物", "產物"),
        ("障碍", "障礙"),
        ("直接", "直接"),
        ("了悟", "了悟"),
        ("核心", "核心"),
        ("教法", "教法"),
        ("标志", "標誌"),
        ("言语", "言語"),
        ("教导", "教導"),
        ("禅定", "禪定"),
        ("高级", "高級"),
        ("专注", "專注"),
        ("完全", "完全"),
        ("交托", "交託"),
        ("意志", "意志"),
        ("轮回", "輪迴"),
        ("无明", "無明"),
        ("解脱", "解脫"),
        ("证悟", "證悟"),
        ("加持", "加持"),
        ("觉醒", "覺醒"),
        ("关键", "關鍵"),
        ("因素", "因素"),
        ("导师", "導師"),
        ("引导", "引導"),
        ("学生", "學生"),
        ("走向", "走向"),
        ("行动", "行動"),
        ("果报", "果報"),
        ("法则", "法則"),
        ("精华", "精華"),
        ("记录", "記錄"),
        ("弟子", "弟子"),
        ("日常", "日常"),
        ("对话", "對話"),
        ("文献", "文獻"),
        ("权威", "權威"),
        ("编纂", "編纂"),
        ("守护", "守護"),
        ("阿鲁那", "阿魯那"),
        ("佳拉", "佳拉"),
        ("圣山", "聖山"),
        ("修行", "修行"),
        ("圆寂", "圓寂"),
        ("之地", "之地"),
        ("专注", "專注"),
        ("寂静", "寂靜"),
        ("持诵", "持誦"),
        ("神圣", "神聖"),
        ("音节", "音節"),
        ("圣名", "聖名"),
        ("出离", "出離"),
        ("世俗", "世俗"),
        ("超越", "超越"),
        ("放下", "放下"),
        ("知识", "知識"),
        ("究竟", "究竟"),
        ("无知", "無知"),
        ("属性", "屬性"),
        ("熏习", "薰習"),
        ("根深", "根深"),
        ("蒂固", "蒂固"),
        ("心理", "心理"),
        ("印记", "印記"),
        ("来源", "來源"),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    return content != original

def main():
    print("=" * 50)
    print("全面修复脚本")
    print("=" * 50)

    # 1. 修复 zh-TW/graph.html 的节点
    print("\n[1] 修复图谱节点...")
    graph_file = '/workspace/pages/zh-TW/graph.html'
    if fix_graph_nodes(graph_file):
        with open(graph_file, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(graph_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed: graph.html")
    else:
        print(f"  - No changes: graph.html")

    # 2. 添加语言切换按钮到 zh-TW 所有页面
    print("\n[2] 添加语言切换按钮到 zh-TW...")
    zh_tw_count = 0
    for root, dirs, files in os.walk('/workspace/pages/zh-TW'):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if add_lang_toggle_to_file(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    zh_tw_count += 1
    print(f"  ✓ Added toggle to {zh_tw_count} zh-TW pages")

    # 3. 添加语言切换按钮到简体版所有页面
    print("\n[3] 添加语言切换按钮到简体版...")
    zh_cn_count = 0
    for root, dirs, files in os.walk('/workspace/pages'):
        # 跳过 zh-TW 目录
        if 'zh-TW' in root:
            continue
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                if add_lang_toggle_to_file(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    zh_cn_count += 1
    print(f"  ✓ Added toggle to {zh_cn_count} zh-CN pages")

    print("\n" + "=" * 50)
    print("修复完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
