<template>
  <span
    @click="toggleVisibility"
    :class="{censored, clean, sentence: true, visible}">
    {{text}}
  </span>
</template>

<script>
import appState from '@/appState.js';

// TODO: get this from server to avoid discrepancies with share images
const labelMap = {
  SPAM: { id: 'SPAM', color: '#228BEB', name: 'spam' },
  FLIRTATION: { id: 'FLIRTATION', color: '#F66FD9', name: 'flirtation' },
  PROFANITY: { id: 'PROFANITY', color: '#10803D', name: 'profanity' },
  IDENTITY_ATTACK: { id: 'IDENTITY_ATTACK', color: '#000000', name: 'identity attack' },
  THREAT: { id: 'THREAT', color: '#EF2A2A', name: 'threat' },
  // Provocation is a (sort of) substantive for inflammatory
  INFLAMMATORY: { id: 'INFLAMMATORY', color: '#EF2A2A', name: 'provocation' },
  TOXICITY: { id: 'TOXICITY', color: '#6F32D3', name: 'toxicity' },
  SEVERE_TOXICITY: { id: 'SEVERE_TOXICITY', color: '#6F32D3', name: 'severe toxicity' },
  SEXUALLY_EXPLICIT: { id: 'SEXUALLY_EXPLICIT', color: '#F66FD9', name: 'sexually explicit' },
  INSULT: { id: 'INSULT', color: '#F3890C', name: 'insult' },
  OBSCENE: { id: 'OBSCENE', color: '#F66FD9', name: 'obscenity' },
};

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
      return this.labelIds.map((key) => labelMap[key]);
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
    },
  },
};
</script>
