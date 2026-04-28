// pages/search/search.js
const app = getApp()

Page({
  data: {
    query: '',
    results: [],
    searched: false
  },

  onInput(e) {
    this.setData({ query: e.detail.value })
  },

  onSearch() {
    const query = this.data.query.toLowerCase()
    if (!query.trim()) return

    const index = app.globalData.searchIndex
    const results = index.filter(item => 
      item.title.toLowerCase().includes(query) || 
      item.excerpt.toLowerCase().includes(query)
    ).map(item => {
      const typeMap = {
        book: '书籍',
        concept: '概念',
        qa: '问答',
        person: '人物',
        method: '方法'
      }
      return {
        ...item,
        typeText: typeMap[item.type] || item.type
      }
    })

    this.setData({ results, searched: true })
  },

  onResultTap(e) {
    const url = e.currentTarget.dataset.url
    wx.navigateTo({ url })
  }
})
