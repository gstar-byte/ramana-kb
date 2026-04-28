// pages/concepts/index.js
Page({
  data: { concepts: [] },
  onLoad() {
    const concepts = require('../../data/concepts.json')
    this.setData({ concepts })
  },
  onConceptTap(e) {
    wx.navigateTo({ url: `/pages/concepts/detail?id=${e.currentTarget.dataset.id}` })
  }
})
