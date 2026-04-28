// pages/books/index.js
Page({
  data: {
    books: []
  },

  onLoad() {
    const books = require('../../data/books.json')
    this.setData({ books })
  },

  onBookTap(e) {
    const id = e.currentTarget.dataset.id
    wx.navigateTo({
      url: `/pages/books/detail?id=${id}`
    })
  }
})
