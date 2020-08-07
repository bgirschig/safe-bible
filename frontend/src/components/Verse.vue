<template>
  <span class="verse">
    <sup :key="verse.verseIdx" :id="verse['verseId']">
      <a
        aria-label="more info about this verse"
        :href="verse.bibleHubLink"
        rel="noopener"
        target="_blank"
        class="verseNumber">
        {{verse.verseIdx}}
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
  },
};
</script>
