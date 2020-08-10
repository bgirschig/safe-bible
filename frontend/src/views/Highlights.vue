<template>
  <main>
    <div class="text">
      <h1>Highlights</h1>
      <div v-for="(book, bookId) in appState.highlights" :key="bookId" class="book">
        <h2>{{appState.highlights[bookId]["bookTitle"]}}</h2>
        <div class="columns">
          <p v-for="(chapter, chapterIdx) in book.chapters" :key="chapterIdx">
            <span class="chapterIdx">{{ chapterIdx }}</span>
            <Verse
              v-for="(verse, verseIdx) in chapter"
              :key="verseIdx"
              :verse="verse" />
          </p>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import appState from '@/appState.js';
import Verse from '@/components/Verse.vue';

export default {
  components: { Verse },
  data() {
    return {
      appState,
    };
  },
};
</script>

<style scoped>
.chapterIdx {
  font-size: 1.4em;
  margin-right: 0.5em;
}
</style>
