<template>
  <div id="settings" class="">
    <h1>Settings</h1>

    <p>
      <button
        @click="setDarkMode(!appState.settings.nightMode)"
        class="nightmodeToggle">
        Dark Mode
      </button>
    </p>

    <FilthSelector @change="setFilthAmount" :value="appState.settings.filthAmount"/>

    <h2>Text size</h2>
    <p id="fontSizeSelector" class="textFont">
      <span @click="setFontSize('compact')"
        class="compact" data-value="compact">Compact</span>
      <span @click="setFontSize('medium')"
        class="medium" data-value="medium">Medium</span>
      <span @click="setFontSize('large')"
        class="large" data-value="large">Large</span>
    </p>
  </div>
</template>

<script>
import FilthSelector from '@/components/FilthSelector.vue';
import appState from '@/appState.js';
import { matomoCustomVariables, Filth, getEnumValueName } from '@/enums.js';

export default {
  data() {
    return { appState };
  },
  components: { FilthSelector },
  methods: {
    setFontSize(size) {
      if (size === appState.settings.fontSize) return;
      appState.settings.fontSize = size;
      this.$matomo.setCustomVariable(matomoCustomVariables.FONT_SIZE, 'font-size', size);
    },
    setDarkMode(value) {
      if (value === appState.settings.nightMode) return;
      appState.settings.nightMode = value;
      this.$matomo.setCustomVariable(matomoCustomVariables.DARK_MODE, 'dark-mode', value);
    },
    setFilthAmount(value) {
      if (value === appState.settings.filthAmount) return;
      else appState.settings.filthAmount = value;

      const name = getEnumValueName(Filth, value);
      this.$matomo.setCustomVariable(matomoCustomVariables.FILTH_SELECT, 'filth-amount', name);
    },
  },
};
</script>

<style scoped>
#settings {
  position: fixed;
  top: 0;
  right: 0;
  background-color: var(--bgColor);
  width: 100%;
  height: calc(100% - 63px);
  z-index: 3;
  padding: 15px;
  box-sizing: border-box;
  overflow-y: auto;
  max-width: 500px;
  border-left: 1px solid rgba(var(--fontColor), 0.15);
  font-size: 1rem;
  text-align: center;
}

h1, h2 {
  line-height: 2em;
}

#settings button {
  padding: 15px 20px;
}

#fontSizeSelector {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
#fontSizeSelector span {
  margin: 5px;
  width: 120px;
  height: 60px;
  border: 1px solid rgba(var(--fontColor), 0.15);
  display: inline-block;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 2px;
}
#fontSizeSelector span:hover {
  cursor: pointer;
  background-color: rgba(var(--fontColor), 0.15);
}

.compact #fontSizeSelector .compact,
.medium #fontSizeSelector .medium,
.large #fontSizeSelector .large {
  background-color: var(--accentColor);
  color: white;
}

.nightMode #settings .nightmodeToggle {
  background-color: var(--accentColor);
  color: white;
}

@media (min-width: 400px) {
  #fontSizeSelector {
    flex-direction: row;
  }
}
</style>
