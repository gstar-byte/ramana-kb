// pages/concepts/detail.js
Page({
  data: { concept: null },
  onLoad(options) {
    const concepts = require('../../data/concepts.json')
    const concept = concepts.find(c => c.id === options.id)
    this.setData({ concept })
    wx.setNavigationBarTitle({ title: concept.title })
  }
})
