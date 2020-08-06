<template>
  <div id="app" class="medium">
    <Controlbar
      v-if="appState.books.length>0"
      @toggleIndex="toggleBrowser"
      @toggleSettings="toggleSettings"
      :navState="appState.nav"/>

    <router-view :key="$route.path"/>

    <InfoOverlay
      v-if="appState.currentSentence"
      ref="overlay"
      @close="appState.currentSentence=null"
      :target="appState.currentSentence" />

    <transition name="slidefromleft">
      <BookBrowser v-if="showBookBrowser"/>
    </transition>
    <transition name="slidefromright">
      <SettingsEditor v-if="showSettings"/>
    </transition>
  </div>
</template>

<script>
import Controlbar from '@/components/Controlbar.vue';
import appState from '@/appState.js';
import InfoOverlay from '@/components/InfoOverlay.vue';
import BookBrowser from '@/components/BookBrowser.vue';
import SettingsEditor from '@/components/SettingsEditor.vue';
import '@/css/text.css';
import '@/css/transitions.css';

export default {
  data() {
    return {
      appState,
    };
  },
  computed: {
    showBookBrowser() {
      return appState.currentPanel === 'bookBrowser';
    },
    showSettings() {
      return appState.currentPanel === 'settings';
    },
  },
  async mounted() {
    const response = await fetch('http://localhost:8080/books');
    const data = await response.json();
    appState.books = data;
    this.updateAppState();
  },
  components: {
    Controlbar,
    InfoOverlay,
    BookBrowser,
    SettingsEditor,
  },
  watch: {
    $route() {
      this.updateAppState();
      appState.currentPanel = null;
    },
  },
  methods: {
    toggleBrowser() {
      appState.currentPanel = this.showBookBrowser ? null : 'bookBrowser';
    },
    toggleSettings() {
      appState.currentPanel = this.showSettings ? null : 'settings';
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

button, .btnLink {
  background-color: transparent;
  border-radius: 2px;
  border: 1px solid RGBA(var(--fontColor), 0.15);
  font-size: inherit;
  padding: 10px 20px;
  color: inherit;
  display: inline-block;
  line-height: 1em;
}
button:hover, .btnLink:hover {
  cursor: pointer;
  background-color: RGBA(var(--fontColor), 0.15);
  color: RGB(var(--fontColor));
}
button.imageBtn {
  padding: 5px;
  margin: 5px;
}
.accent {
  background-color: var(--accentColor);
  color: white;
}
</style>
