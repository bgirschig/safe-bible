<template>
  <div id="settings" class="">
    <h1>Settings</h1>

    <p>
      <button
        @click="appState.settings.nightMode = !appState.settings.nightMode"
        class="nightmodeToggle">
        Dark Mode
      </button>
    </p>

    <FilthSelector />

    <h2>Text size</h2>
    <p id="fontSizeSelector">
      <span @click="appState.settings.fontSize = 'compact'"
        class="compact" data-value="compact">Compact</span>
      <span @click="appState.settings.fontSize = 'medium'"
        class="medium" data-value="medium">Medium</span>
      <span @click="appState.settings.fontSize = 'large'"
        class="large" data-value="large">Large</span>
    </p>
  </div>
</template>

<script>
import FilthSelector from '@/components/FilthSelector.vue';
import appState from '@/appState.js';

export default {
  data() {
    return { appState };
  },
  components: { FilthSelector },
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
  z-index: 2;
  padding: 15px;
  box-sizing: border-box;
  overflow-y: auto;
  max-width: 500px;
  border-left: 1px solid rgba(var(--fontColor), 0.15);
  font-size: 1rem;
  text-align: center;
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
