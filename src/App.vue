<template>
  <div id="app">
    <Controlbar v-if="appState.books.length>0" @toggleIndex="toggleIndex" :navState="appState.nav"/>
    <router-view :key="$route.path"/>
    <InfoOverlay
      v-if="appState.currentSentence"
      ref="overlay"
      @close="appState.currentSentence=null"
      :target="appState.currentSentence" />
  </div>
</template>

<script>
import Controlbar from '@/components/Controlbar.vue';
import appState from '@/appState.js';
import InfoOverlay from '@/components/InfoOverlay.vue';
import '@/css/text.css';

export default {
  data() {
    return {
      appState,
    };
  },
  async mounted() {
    const response = await fetch('http://localhost:8080/books');
    const data = await response.json();
    appState.books = data;
    this.updateAppState();
  },
  components: { Controlbar, InfoOverlay },
  watch: {
    $route() {
      this.updateAppState();
    },
  },
  methods: {
    toggleIndex() {
      console.log('toggleIndex');
    },
    updateAppState() {
      appState.bookId = this.$route.params.bookId;
    },
  },
};
</script>

<style lang="scss">
html {
  overflow-x: hidden;
  /** Always show the scrollbar, to avoid changing viewport width */
  overflow-y: scroll;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  // TODO: import fonts
  margin: 0;
  --bgColor: white;
  --fontColor: 0, 0, 0;
  --linkColor: rgb(0, 101, 255);
  --accentColor: #297176;
}

main {
  min-height: 100vh;
  box-sizing: border-box;
  padding-bottom: 68px;
}
</style>
