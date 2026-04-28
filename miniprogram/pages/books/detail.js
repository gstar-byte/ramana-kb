// pages/books/detail.js
Page({
  data: { book: null },

  onLoad(options) {
    const books = require('../../data/books.json')
    const book = books.find(b => b.id === options.id)
    this.setData({ book })
    wx.setNavigationBarTitle({ title: book.title })
  },

  onChapterTap(e) {
    const bookId = e.currentTarget.dataset.book
    const chapterId = e.currentTarget.dataset.chapter
    wx.showToast({ title: '章节详情开发中', icon: 'none' })
  }
})
