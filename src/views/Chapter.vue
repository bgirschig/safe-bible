<template>
  <main id="main">
    <div v-if="error" class="errorDisplay">{{error}}</div>
    <div v-if="verses" class="text">
      <h1>{{appState.bookInfo.full}}</h1>
      <h2 class="current">{{$route.params.chapterIdx}}</h2>

      <div class="columns">
        <template v-for="verse in verses">
          <sup :key="verse.verseIdx" :id="verse['verseId']">
            <a :href="verse.bibleHubLink" target="_blank" class="verseNumber">{{verse.verseIdx}}</a>
          </sup>&nbsp;<!--
       --><span
            v-for="(sentence, sentenceIdx) in verse.sentences"
            :key="`${verse.verseIdx}-${sentenceIdx}`"
            :class="{censored: sentence.labels.length>0}">
            &nbsp;&nbsp;&nbsp;&nbsp;{{sentence.text}}
          </span>
        </template>
      </div>
    </div>
  </main>
</template>

<script>
import appState from '@/appState.js';

export default {
  data() {
    return {
      verses: null,
      error: null,
      appState,
    };
  },
  async created() {
    const response = await fetch(`/chapter/${this.$route.params.bookId}/${this.$route.params.chapterIdx}`);
    const data = await response.json();
    if (response.ok) {
      this.verses = data;
      this.error = null;
    } else {
      this.verses = null;
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
