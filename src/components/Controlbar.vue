<template>
  <div class="controlBar">
    <button @click="$emit('toggleIndex')" class="imageBtn index">
      <BookIcon />
    </button>
    <div class="navigation">
      <router-link v-visible="prev" :to="prev || ''"><ArrowLeft /></router-link>
      <span class="currentChapter">{{title}}</span>
      <router-link v-visible="next" :to="next || ''"><ArrowRight /></router-link>
    </div>
    <button @click="$emit('toggleSettings')" class="imageBtn settings">
      <SettingsIcon />
    </button>
  </div>
</template>

<script>
import ArrowLeft from '@/assets/icons/arrow_left.svg';
import ArrowRight from '@/assets/icons/arrow_right.svg';
import BookIcon from '@/assets/icons/book.svg';
import SettingsIcon from '@/assets/icons/settings.svg';
import appState from '@/appState.js';

export default {
  props: {
    navState: { type: Object, default: null },
  },
  components: {
    ArrowLeft,
    ArrowRight,
    BookIcon,
    SettingsIcon,
  },
  computed: {
    bookInfo() {
      return appState.bookMap[this.bookId];
    },
    chapterIdx() {
      if (this.$route.params.chapterIdx) return (parseInt(this.$route.params.chapterIdx, 10) - 1);
      return 0;
    },
    verseIdx() {
      if (this.$route.params.verseIdx) return (parseInt(this.$route.params.verseIdx, 10) - 1);
      return 0;
    },
    bookId() {
      return this.$route.params.bookId || this.$route.name || 'FOR';
    },
    title() {
      if (this.bookInfo.chapterCount > 0) {
        return `${this.bookInfo.short} ${this.chapterIdx + 1}`;
      } else {
        return this.bookInfo.short;
      }
    },
    prev() {
      let linkBookId = this.bookId;
      let linkChapter = this.chapterIdx - 1;

      if (linkChapter < 0) {
        if (!this.bookInfo.prev) return null;
        linkBookId = this.bookInfo.prev;
        linkChapter = appState.bookMap[linkBookId].chapterCount - 1;
      }
      if (appState.bookMap[linkBookId].chapterCount > 0) {
        return `/${linkBookId}/${linkChapter + 1}`;
      } else {
        return `/${linkBookId}#main`;
      }
    },
    next() {
      let linkBookId = this.bookId;
      let linkChapter = this.chapterIdx + 1;

      if (linkChapter >= this.bookInfo.chapterCount) {
        if (!this.bookInfo.next) return null;
        linkBookId = this.bookInfo.next;
        linkChapter = 0;
      }

      if (appState.bookMap[linkBookId].chapterCount > 0) {
        return `/${linkBookId}/${linkChapter + 1}`;
      } else {
        return `/${linkBookId}#main`;
      }
    },
  },
};
</script>

<style scoped>
.controlBar {
  position: fixed;
  display: flex;
  justify-content: space-between;
  font-family: 'Roboto', sans-serif;
  border-top: 1px solid rgba(var(--fontColor), 0.15);
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
  background-color: var(--bgColor);
  z-index: 2;
}

.controlBar .navigation {
  display: flex;
  align-items: center;
}
.controlBar .navigation .currentChapter {
  position: relative;
  bottom: 2px;
  font-size: clamp(9px, 1rem, 5vw);
}

.controlBar .navigation a,
.controlBar .navigation button {
  margin: 0 10px;
}

.controlBar .navigation a[href=""] {
  visibility: hidden;
}

.controlBar .imageBtn {
  padding: 18px;
  margin: 0;
}
.settingsOpen .imageBtn.settings,
.indexOpen .imageBtn.index {
  background-color: var(--accentColor);
}
.settingsOpen .imageBtn.settings svg,
.indexOpen .imageBtn.index svg {
  fill: white;
}
</style>
