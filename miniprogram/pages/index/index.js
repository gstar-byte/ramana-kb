// pages/index/index.js
Page({
  data: {},

  onLoad() {
    // 设置分享
    wx.showShareMenu({
      withShareTicket: true,
      menus: ['shareAppMessage', 'shareTimeline']
    })
  },

  navigateTo(e) {
    const url = e.currentTarget.dataset.url
    wx.navigateTo({ url })
  },

  onShareAppMessage() {
    return {
      title: '拉玛那马哈希知识库 - 灵性教示完整指南',
      path: '/pages/index/index'
    }
  },

  onShareTimeline() {
    return {
      title: '拉玛那马哈希知识库 - 灵性教示完整指南'
    }
  }
})
