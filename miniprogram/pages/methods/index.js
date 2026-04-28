// pages/methods/index.js
Page({
  data: { methods: [] },
  onLoad() {
    const methods = require('../../data/methods.json')
    this.setData({ methods })
  }
})
