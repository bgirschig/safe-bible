<template>
  <div id="app"
    @keydown.esc="closeEverything"
    :class="[appState.settings.fontSize, {nightMode: appState.settings.nightMode}]">
    <transition name="slidefromleft">
      <BookBrowser v-if="showBookBrowser"/>
    </transition>
    <transition name="slidefromright">
      <SettingsEditor v-if="showSettings"/>
    </transition>

    <Controlbar
      v-if="appState.books.length>0"
      @toggleIndex="toggleBrowser"
      @toggleSettings="toggleSettings"
      :navState="appState.nav"/>

    <router-view :key="$route.path"/>

    <transition name="fade">
      <div
        v-if="appState.currentPanel"
        @click="appState.currentPanel=null"
        class="sidepanelOverlay" />
    </transition>

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
    this.loadSettings();
    this.loadBooks();
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
      this.closeEverything();
    },
    'appState.settings': {
      deep: true,
      handler() {
        // save settings when they get changed
        const settingsStr = JSON.stringify(appState.settings);
        localStorage.setItem('settings', settingsStr);
      },
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
    async loadBooks() {
      const response = await fetch('http://localhost:8080/books');
      const data = await response.json();
      appState.books = data;
      this.updateAppState();
    },
    loadSettings() {
      try {
        const savedSettings = JSON.parse(localStorage.getItem('settings'));
        if (savedSettings) {
          Object.assign(appState.settings, savedSettings);
        } else {
          console.warn('There were no settings to load. Using default values');
        }
      } catch {
        console.warn('Could not load previous settings. Using default values');
      }
    },
    closeEverything() {
      appState.currentPanel = null;
      appState.currentSentence = null;
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
body {
  // TODO: import fonts
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  --bgColor: white;
  --fontColor: 0, 0, 0;
  --linkColor: rgb(0, 101, 255);
  --accentColor: #297176;

  color: RGB(var(--fontColor));
  background-color: var(--bgColor);
}

svg {
  fill: RGB(var(--fontColor));
}
a {
  color: var(--linkColor);
  text-decoration: none;
}

#app.nightMode {
  background-color: rgb(25, 25, 25);

  --bgColor: black;
  --fontColor: 150, 150, 150;
  --linkColor: rgb(117 164 234);
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

.sidepanelOverlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 2;
  background-color: RGBA(var(--fontColor), 0.2);
}
</style>
