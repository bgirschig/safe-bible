import Vue from 'vue';
import { Filth } from '@/enums';

export default new Vue({
  data() {
    return {
      books: [],
      highlights: [],
      bookId: null,
      chapterIdx: 0,
      pageTitle: null,
      currentSentence: null,
      currentPanel: null,
      labelMap: null,
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
    prevPageUrl() {
      if (!this.bookInfo.id) return null;
      let linkBookId = this.bookId;
      let linkChapter = this.chapterIdx - 1;

      if (linkChapter < 0) {
        if (!this.bookInfo.prev) return null;
        linkBookId = this.bookInfo.prev;
        linkChapter = this.bookMap[linkBookId].chapterCount - 1;
      }
      if (this.bookMap[linkBookId].chapterCount > 0) {
        return `/${linkBookId}/${linkChapter + 1}`;
      } else if (linkBookId === 'home') {
        return '/#main'; // skip the cover, go directly to the foreword
      } else {
        return `/${linkBookId}`;
      }
    },
    nextPageUrl() {
      if (!this.bookInfo.id) return null;
      let linkBookId = this.bookId;
      let linkChapter = this.chapterIdx + 1;

      if (linkChapter >= this.bookInfo.chapterCount) {
        if (!this.bookInfo.next) return null;
        linkBookId = this.bookInfo.next;
        linkChapter = 0;
      }

      if (this.bookMap[linkBookId].chapterCount > 0) {
        return `/${linkBookId}/${linkChapter + 1}`;
      } else if (linkBookId === 'home') {
        return '/';
      } else {
        return `/${linkBookId}`;
      }
    },
  },
});
