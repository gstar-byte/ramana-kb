#!/usr/bin/env python3
"""转换 zh-TW/qa/index.html 中的简体 JS 文字为繁体"""
import re
import opencc

converter = opencc.OpenCC('s2t')

INPUT = r"F:\26年4月\kb01\pages\zh-TW\qa\index.html"

with open(INPUT, 'r', encoding='utf-8') as f:
    content = f.read()

# 需要转换的 JS 字符串模式
# 这些是 JS 中嵌入的简体字符串，需要整体转繁体

# 1. 第X页
content = content.replace('`第${page}页`', '`第${page}頁`')

# 2. title 和 desc 相关
content = content.replace(
    "'精选问答600则 | 拉玛那马哈希灵性对话精编指南详解 | 拉玛那马哈希知识库'",
    "'精選問答600則 | 拉瑪那馬哈希靈性對話精編指南詳解 | 拉瑪那馬哈希知識庫'"
)

content = content.replace(
    "'拉玛那马哈希精选问答600则，涵盖真我、心智、参究、奉爱、静默、恩典、三摩地、梦境修行、圣人传记，自然灵性、艺术修行、饮食健康、人际关系、深层哲学、现代修行等核心主题，助您深入理解这位伟大灵性导师的教示精髓与修行智慧。'",
    "'拉瑪那馬哈希精選問答600則，涵蓋真我、心智、參究、奉愛、靜默、恩典、三摩地、夢境修行、聖人傳記，自然靈性、藝術修行、飲食健康、人際關係、深層哲學、現代修行等核心主題，助您深入理解這位偉大靈性導師的教示精髓與修行智慧。'"
)

# 3. filterNames
content = content.replace("'全部'", "'全部'")
content = content.replace("'主题问答'", "'主題問答'")
content = content.replace("'探索拉玛那马哈希关于'", "'探索拉瑪那馬哈希關於'")

# 4. 正在加载
content = content.replace("'正在加载问答内容...'", "'正在載入問答內容...'")

# 5. 更多问答
content = content.replace("'✨ 更多问答正在整理中……'", "'✨ 更多問答正在整理中……'")

# 6. 分类选项
content = content.replace("'全部问答'", "'全部問答'")
content = content.replace("'按主题筛选'", "'按主題篩選'")
content = content.replace("'按书籍筛选'", "'按書籍篩選'")

# 7. 加载所有
content = content.replace("'加载所有'", "'載入所有'")

# 8. 加载失败
content = content.replace("'加载失败'", "'載入失敗'")
content = content.replace("'点击重试'", "'點擊重試'")

with open(INPUT, 'w', encoding='utf-8') as f:
    f.write(content)

print("zh-TW/qa/index.html JS 文字转换完成")
