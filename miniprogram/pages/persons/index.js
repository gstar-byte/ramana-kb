// pages/persons/index.js
Page({
  data: { persons: [] },
  onLoad() {
    const persons = require('../../data/persons.json')
    this.setData({ persons })
  },
  onPersonTap(e) {
    wx.navigateTo({ url: `/pages/persons/detail?id=${e.currentTarget.dataset.id}` })
  }
})
