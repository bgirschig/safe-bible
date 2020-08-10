<template>
  <div id="app"
    @keydown.esc="closeEverything"
    :class="[
      appState.settings.fontSize,
      filthClass,
      {
        nightMode: appState.settings.nightMode,
        zIndexBugFix: enableZindexFix,
      },
    ]">
    <transition name="slidefromleft">
      <BookBrowser v-if="showBookBrowser"/>
    </transition>
    <transition name="slidefromright">
      <SettingsEditor v-if="showSettings"/>
    </transition>

    <Controlbar
      v-if="appState.books.length>0"
      @toggleIndex="toggleBrowser"
      @toggleSettings="toggleSettings"/>

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

    <Tooltip v-if="showCensorTooltip" :target="appState.hoveredSentence">
      Stay safe, Don't click
    </Tooltip>
  </div>
</template>

<script>
import WebFont from 'webfontloader';

import { matomoCustomVariables, Filth, getEnumValueName } from '@/enums.js';
import Controlbar from '@/components/Controlbar.vue';
import appState from '@/appState.js';
import SwipeDetector from '@/js/swipeDetector';
import InfoOverlay from '@/components/InfoOverlay.vue';
import BookBrowser from '@/components/BookBrowser.vue';
import SettingsEditor from '@/components/SettingsEditor.vue';
import Tooltip from '@/components/Tooltip.vue';
import '@/css/common.css';
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
    enableZindexFix() {
      // The bug this adresses has been detected on chrome and safari. firefox works fine
      const isFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;
      return !isFirefox;
    },
    filthClass() {
      return getEnumValueName(Filth, appState.settings.filthAmount)
        .toLowerCase()
        .replace(/_/g, '-');
    },
    showCensorTooltip() {
      return appState.hoveredSentence
        && !appState.currentSentence
        && appState.hoveredSentence.censored;
    },
  },
  async mounted() {
    this.loadFonts();
    this.loadSettings();
    this.loadBooks();

    this.swipeDetector = new SwipeDetector({
      el: document.body,
      callback: (direction) => {
        if (direction === 'left' && appState.nextPageUrl) {
          this.$router.push(appState.nextPageUrl);
          window._paq.push(['trackEvent', 'swipeNav', 'next']);
        } else if (direction === 'right' && appState.prevPageUrl) {
          this.$router.push(appState.prevPageUrl);
          window._paq.push(['trackEvent', 'swipeNav', 'prev']);
        }
      },
    });
  },
  components: {
    Controlbar,
    InfoOverlay,
    BookBrowser,
    SettingsEditor,
    Tooltip,
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
      if (this.$route.params.chapterIdx) {
        appState.chapterIdx = parseInt(this.$route.params.chapterIdx, 10) - 1;
      } else {
        appState.chapterIdx = 0;
      }

      if (this.$route.name === 'Chapter') {
        appState.bookId = this.$route.params.bookId;
        appState.pageTitle = `${appState.bookInfo.short} ${this.$route.params.chapterIdx || 1}`;
        document.title = `safe bible | ${appState.bookInfo.short} ${this.$route.params.chapterIdx || 1}`;
      } else {
        appState.bookId = this.$route.name;
        appState.pageTitle = this.$route.meta.title;
      }
      document.title = `safe bible | ${appState.pageTitle}`;

      // eslint-disable-next-line no-underscore-dangle
      window._paq.push(['setDocumentTitle', document.title]);
    },
    async loadBooks() {
      const response = await fetch('/books');
      const data = await response.json();
      appState.books = data.books;
      appState.highlights = data.highlights;
      appState.labelMap = data.labelMap;
      this.updateAppState();
    },
    loadFonts() {
      WebFont.load({
        google: {
          families: ['Roboto:wght@400;700&display=swap', 'Source+Serif+Pro&display=swap'],
        },
      });
    },
    loadSettings() {
      try {
        const savedSettings = JSON.parse(localStorage.getItem('settings'));
        if (savedSettings) {
          Object.assign(appState.settings, savedSettings);
        } else {
          console.warn('There were no settings to load. Using default values');
        }

        // setup visit's settings for analytics
        const filthName = getEnumValueName(Filth, appState.settings.filthAmount);
        window._paq.push(['setCustomVariable',
          matomoCustomVariables.FONT_SIZE, 'font-size', appState.settings.fontSize]);
        window._paq.push(['setCustomVariable',
          matomoCustomVariables.DARK_MODE, 'dark-mode', appState.settings.nightMode]);
        window._paq.push(['setCustomVariable',
          matomoCustomVariables.FILTH_SELECT, 'filth-amount', filthName]);
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
  margin: 0;
}

#app {
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  --bgColorValues: 255, 255, 255;
  --bgColor: rgb(var(--bgColorValues));
  --fontColor: 0, 0, 0;
  --linkColor: rgb(0, 101, 255);
  --accentColor: #297176;

  color: RGB(var(--fontColor));
  background-color: rgb(240, 240, 240);
}

svg {
  fill: RGB(var(--fontColor));
}
a {
  color: var(--linkColor);
  text-decoration: none;
}
.center {
  text-align: center;
}

#app.nightMode {
  background-color: rgb(25, 25, 25);

  --bgColorValues: 0, 0, 0;
  --bgColor: black;
  --fontColor: 150, 150, 150;
  --linkColor: rgb(117 164 234);
}

main {
  min-height: 100vh;
  box-sizing: border-box;
  padding-bottom: 63px;
}

button, .btnLink {
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
  background-color: transparent;
  border-radius: 2px;
  border: none;
  font-size: inherit;
  padding: 10px 20px;
  color: inherit;
  display: inline-block;
  line-height: 1em;
  border: 1px solid RGBA(var(--fontColor), 0.15);
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
