// pages/qa/detail.js
Page({
  data: { qa: null },
  onLoad(options) {
    const qa = require('../../data/qa.json')
    const item = qa.find(q => q.id === options.id)
    this.setData({ qa: item })
    wx.setNavigationBarTitle({ title: item.question.substring(0, 10) + '...' })
  }
})
