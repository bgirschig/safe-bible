<template>
  <span v-if="sentences.length > 0" class="verse">
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
      v-for="(sentence, sentenceIdx) in sentences"
      :key="`${verse.verseIdx}-${sentenceIdx}`"
      :text="sentence.text"
      :labelIds="sentence.labels"
      :verseId="verse.verseId"
    />
  </span>
</template>

<script>
import Sentence from '@/components/Sentence.vue';
import appState from '@/appState';
import { Filth } from '@/enums.js';

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
    sentences() {
      return this.verse.sentences.filter((sentence) => {
        switch (appState.settings.filthAmount) {
          case Filth.KEEP_EVERYTHING:
            return true;
          case Filth.NO_FILTH:
            return sentence.labels.length === 0;
          case Filth.ONLY_FILTH:
            return sentence.labels.length > 0;
          default:
            throw new Error(`unexpected filth setting: ${appState.settings.filthAmount}`);
        }
      });
    },
  },
};
</script>
