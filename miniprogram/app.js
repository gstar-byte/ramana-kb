// app.js
App({
  globalData: {
    searchIndex: []
  },
  
  onLaunch() {
    // 初始化搜索数据
    this.initSearchData()
  },
  
  initSearchData() {
    const books = require('./data/books.json')
    const concepts = require('./data/concepts.json')
    const qa = require('./data/qa.json')
    const persons = require('./data/persons.json')
    const methods = require('./data/methods.json')
    
    let index = []
    
    books.forEach(book => {
      index.push({
        type: 'book',
        title: book.title,
        url: `/pages/books/detail?id=${book.id}`,
        excerpt: book.description || ''
      })
    })
    
    concepts.forEach(concept => {
      index.push({
        type: 'concept',
        title: concept.title,
        url: `/pages/concepts/detail?id=${concept.id}`,
        excerpt: concept.description || ''
      })
    })
    
    qa.forEach(item => {
      index.push({
        type: 'qa',
        title: item.question,
        url: `/pages/qa/detail?id=${item.id}`,
        excerpt: item.answer ? item.answer.substring(0, 50) + '...' : ''
      })
    })
    
    persons.forEach(person => {
      index.push({
        type: 'person',
        title: person.name,
        url: `/pages/persons/detail?id=${person.id}`,
        excerpt: person.bio ? person.bio.substring(0, 50) + '...' : ''
      })
    })
    
    methods.forEach(method => {
      index.push({
        type: 'method',
        title: method.title,
        url: `/pages/methods/index`,
        excerpt: method.description || ''
      })
    })
    
    this.globalData.searchIndex = index
  }
})
