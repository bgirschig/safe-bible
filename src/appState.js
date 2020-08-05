import Vue from 'vue';

export default new Vue({
  data() {
    return {
      books: [],
      bookId: null,
      currentSentence: null,
    };
  },
  computed: {
    bookMap() {
      const bookMap = {};
      this.books.forEach((book) => {
        bookMap[book.id] = book;
      });
      return bookMap;
    },
    bookInfo() {
      if (this.bookMap && this.bookId in this.bookMap) return this.bookMap[this.bookId];
      return {};
    },
  },
});
