<template>
  <span
    @click="toggleVisibility"
    :class="{censored, clean, sentence: true, visible}">
    {{text}}
  </span>
</template>

<script>
import appState from '@/appState.js';

export default {
  props: {
    text: { type: String, default: '' },
    labelIds: {},
    verseId: { type: String, default: '' },
  },
  computed: {
    censored() {
      return this.labelIds.length > 0;
    },
    clean() {
      return this.labelIds.length === 0;
    },
    labels() {
      if (!appState.labelMap) return [];
      return this.labelIds.map((key) => appState.labelMap[key]);
    },
    visible() {
      return appState.currentSentence === this;
    },
  },
  methods: {
    toggleVisibility() {
      if (appState.currentSentence === this) appState.currentSentence = null;
      else this.reveal();
    },
    async reveal() {
      if (!this.censored) return;
      appState.currentSentence = this;
      window._paq.push(['trackEvent', 'revealVerse', this.verseId]);
    },
  },
};
</script>
