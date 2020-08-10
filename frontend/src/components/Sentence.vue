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

<style scoped>
.censored {
  cursor: pointer;
}

@media (hover: hover) {
  .censored:not(.visible):before {
    content: "Stay safe, Don't click";
    position: absolute;
    bottom: calc(100% + 6px);
    padding: 0 10px;
    box-sizing: border-box;
    background-color: rgb(var(--fontColor));
    border: 0.1px solid rgba(var(--bgColorValues), 0.3);
    color: var(--bgColor);
    white-space: nowrap;
    font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
    border-radius: 3px;
    z-index: 3;

    /*
      This trick is to avoid flickering when going from one line to the next in the same sentence
      we can't do a real transition because
    */
    transition: visibility 0.2s;
    visibility: hidden;
  }
  .censored:hover::before {
    visibility: visible;
  }
}
</style>
