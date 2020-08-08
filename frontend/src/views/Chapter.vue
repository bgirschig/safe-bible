<template>
  <main id="main">
    <div v-if="error" class="text errorDisplay">{{error}}</div>
    <div v-if="verses" class="text">
      <h1>{{appState.bookInfo.full}}</h1>

      <div class="chapterSelector">
        <div class="before">
          <router-link
            :aria-label="`go to chapter ${current-idx}`"
            v-for="idx in current-1"
            :key="idx"
            :to="`/${$route.params.bookId}/${current-idx}`">
            {{current-idx}}
          </router-link>
        </div>
        <h2 class="current">{{current}}</h2>
        <div class="next">
          <router-link
            :aria-label="`go to chapter ${current + idx}`"
            v-for="idx in nextChaptersCount"
            :key="idx"
            :to="`/${$route.params.bookId}/${current + idx}`">
            {{current + idx}}
          </router-link>
        </div>
      </div>

      <div v-if="verses.length > 0" class="columns">
        <Verse v-for="verse in verses" :key="verse.id" :verse="verse" />
      </div>
      <div v-else class="emptyMessage">{{ emptyMessage }}</div>
    </div>
  </main>
</template>

<script>
import appState from '@/appState.js';
import Verse from '@/components/Verse.vue';
import { Filth } from '@/enums';

export default {
  components: { Verse },
  data() {
    return {
      rawVerses: null,
      error: null,
      appState,
    };
  },
  computed: {
    current() {
      return parseInt(this.$route.params.chapterIdx, 10);
    },
    nextChaptersCount() {
      if (!appState.bookInfo.chapterCount) return 0;
      return appState.bookInfo.chapterCount - this.current;
    },
    verses() {
      if (!this.rawVerses) return null;

      // Make a copy: we're going to modify the contents
      const verses = JSON.parse(JSON.stringify(this.rawVerses));

      switch (appState.settings.filthAmount) {
        case Filth.KEEP_EVERYTHING:
          return verses;
        case Filth.NO_FILTH:
          /* eslint-disable no-param-reassign */
          return verses.filter((verse) => {
            verse.sentences = verse.sentences.filter((sentence) => sentence.labels.length === 0);
            return verse.sentences.length > 0;
          });
          /* eslint-enable no-param-reassign */
        default:
          /* eslint-disable no-param-reassign */
          return verses.filter((verse) => {
            verse.sentences = verse.sentences.filter((sentence) => sentence.labels.length > 0);
            return verse.sentences.length > 0;
          });
          /* eslint-enable no-param-reassign */
      }
    },
    emptyMessage() {
      switch (appState.settings.filthAmount) {
        case Filth.NO_FILTH:
          return 'Sorry, everything here was detected as offensive';
        case Filth.ONLY_FILTH:
          return 'Sorry, no filth was found in this chapter';
        case Filth.KEEP_EVERYTHING:
        default:
          return 'Sorry, there is nothing to display here';
      }
    },
  },
  async created() {
    const response = await fetch(`/chapter/${this.$route.params.bookId}/${this.$route.params.chapterIdx}`);
    const data = await response.json();
    if (response.ok) {
      this.rawVerses = data;
      this.error = null;
    } else {
      this.rawVerses = null;
      switch (data.error) {
        case 'BOOK_NOT_FOUND':
          this.error = 'Sorry, the book you\'re looking for was not found';
          break;
        case 'CHAPTER_NOT_FOUND':
          this.error = `Sorry, there is no chapter ${this.$route.params.chapterIdx} in ${this.$route.params.bookId}`;
          break;
        default:
          this.error = 'Sorry, an unexpected error happened. Please try again';
          break;
      }
    }
  },
};
</script>

<style scoped>
.emptyMessage {
  text-align: center;
}
.errorDisplay {
  text-align: center;
  font-size: 1.2em;
  padding-top: 3em;
}

.chapterSelector {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 -1.5em 40px -1.5em;
}
h2 {
  margin: 0;
}
.current {
  margin: 0 0.6em;
  flex: 0 0;
}
.before {
  text-align: right;
  direction: rtl;
}
.next, .before {
  width: 50%;
  flex: 1 1;
  white-space: nowrap;
  overflow: hidden;
}
.next a, .before a {
  margin: 0 0.2em;
  font-size: 1.2em;
  color: rgba(var(--fontColor), 0.25);
}
</style>
