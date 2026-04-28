// pages/persons/detail.js
Page({
  data: { person: null },
  onLoad(options) {
    const persons = require('../../data/persons.json')
    const person = persons.find(p => p.id === options.id)
    this.setData({ person })
    wx.setNavigationBarTitle({ title: person.name })
  }
})
