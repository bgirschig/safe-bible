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
      verses: null,
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
    let response;
    try {
      response = await fetch(`/chapter/${this.$route.params.bookId}/${this.$route.params.chapterIdx}`);
    } catch (e) {
      console.error(e);
      this.error = 'Sorry, an unexpected error happened. Please try again';
      return;
    }
    const data = await response.json();
    if (response.ok) {
      this.verses = data;
      this.error = null;
    } else {
      this.verses = null;
      switch (data.error) {
        case 'BOOK_NOT_FOUND':
          this.$router.push('/404');
          break;
        case 'CHAPTER_NOT_FOUND':
          this.$router.push('/404');
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
