# 拉玛那马哈希知识库 - 微信小程序

## 项目结构

```
miniprogram/
├── app.js                  # 小程序入口
├── app.json                # 全局配置
├── app.wxss                # 全局样式
├── sitemap.json            # 站点地图
├── project.config.json     # 项目配置
├── data/                   # JSON数据文件
│   ├── books.json          # 18本书籍数据
│   ├── concepts.json       # 13个核心概念
│   ├── qa.json             # 10条精选问答
│   ├── persons.json        # 3个人物传记
│   └── methods.json        # 4种修行方法
├── pages/                  # 页面
│   ├── index/              # 首页
│   ├── books/              # 书籍列表和详情
│   ├── concepts/           # 概念列表和详情
│   ├── qa/                 # 问答列表和详情
│   ├── persons/            # 人物列表和详情
│   ├── methods/            # 修行方法
│   └── search/             # 搜索页面
└── assets/
    └── icons/              # tabBar图标
```

## 如何使用

1. 下载并安装 [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)
2. 打开微信开发者工具，选择"导入项目"
3. 选择 `miniprogram` 目录
4. 填入你的 AppID（或选择测试号）
5. 点击"导入"

## 功能特性

- ✅ 首页：统计卡片、快速入口、热门书籍、概念标签、每日一读
- ✅ 书籍：18本书籍列表和章节导航
- ✅ 概念：13个核心概念详解
- ✅ 问答：精选问答浏览
- ✅ 人物：关键人物传记
- ✅ 方法：修行方法指南
- ✅ 搜索：全文搜索功能
- ✅ 分享：支持分享给好友和朋友圈
- ✅ TabBar：底部导航栏

## 后续扩展

- 导入完整HTML内容到JSON
- 添加收藏功能
- 添加阅读历史记录
- 添加夜间模式
- 添加字体大小调节
- 分包加载优化
