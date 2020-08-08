<template>
  <span class="verse">
    <sup :id="verse['verseId']">
      <a
        v-if="verseLabel"
        aria-label="more info about this verse"
        :href="verse.bibleHubLink"
        rel="noopener"
        target="_blank"
        class="verseNumber">
        {{verseLabel}}
      </a>
    </sup>&nbsp;<Sentence
      v-for="(sentence, sentenceIdx) in verse.sentences"
      :key="`${verse.verseIdx}-${sentenceIdx}`"
      :text="sentence.text"
      :labelIds="sentence.labels"
      :verseId="verse.verseId"
    />
  </span>
</template>

<script>
import Sentence from '@/components/Sentence.vue';

export default {
  components: { Sentence },
  props: {
    verse: { type: Object, default: null },
    chapter: { type: String, default: null },
  },
  computed: {
    verseLabel() {
      if (!this.verse) return null;

      if (this.chapter !== null) {
        return `${this.chapter}:${this.verse.verseIdx}`;
      } else {
        return this.verse.verseIdx;
      }
    },
  },
};
</script>
