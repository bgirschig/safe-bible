import Vue from 'vue';
import { Filth } from '@/enums';

export default new Vue({
  data() {
    return {
      books: [],
      highlights: [],
      bookId: null,
      currentSentence: null,
      currentPanel: null,
      settings: {
        filthAmount: Filth.KEEP_EVERYTHING,
        fontSize: 'medium',
        nightMode: false,
      },
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
