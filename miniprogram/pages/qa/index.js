// pages/qa/index.js
Page({
  data: { qaList: [] },
  onLoad() {
    const qa = require('../../data/qa.json')
    this.setData({ qaList: qa })
  },
  onQaTap(e) {
    wx.navigateTo({ url: `/pages/qa/detail?id=${e.currentTarget.dataset.id}` })
  }
})
