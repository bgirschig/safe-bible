<template>
  <div class="controlBar">
    <button
      aria-label="toggle book browser"
      @click="$emit('toggleIndex')"
      :class="['imageBtn', {selected: appState.currentPanel === 'bookBrowser'}]">
      <BookIcon />
    </button>
    <div class="navigation">
      <router-link
        aria-label="go to previous page"
        v-visible="appState.prevPageUrl"
        :to="appState.prevPageUrl || ''">
        <ArrowLeft />
        </router-link>
      <span class="currentChapter">{{ appState.pageTitle }}</span>
      <router-link
        aria-label="go to next page"
        v-visible="appState.nextPageUrl"
        :to="appState.nextPageUrl || ''">
        <ArrowRight />
        </router-link>
    </div>
    <button
      aria-label="toggle settings panel"
      @click="$emit('toggleSettings')"
      :class="['imageBtn', {selected: appState.currentPanel === 'settings'}]">
      <SettingsIcon />
    </button>
  </div>
</template>

<script>
import ArrowLeft from '@/assets/icons/arrow_left.svg';
import ArrowRight from '@/assets/icons/arrow_right.svg';
import BookIcon from '@/assets/icons/book.svg';
import SettingsIcon from '@/assets/icons/settings.svg';
import appState from '@/appState.js';

export default {
  components: {
    ArrowLeft,
    ArrowRight,
    BookIcon,
    SettingsIcon,
  },
  data() {
    return {
      appState,
    };
  },
};
</script>

<style scoped>
.controlBar {
  position: fixed;
  display: flex;
  justify-content: space-between;
  border-top: 1px solid rgba(var(--fontColor), 0.15);
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
  background-color: var(--bgColor);
  z-index: 3;
}

.controlBar .navigation {
  display: flex;
  align-items: center;
}
.controlBar .navigation .currentChapter {
  position: relative;
  bottom: 2px;
  font-size: clamp(9px, 1rem, 5vw);
  white-space: nowrap;
}

.controlBar .navigation a,
.controlBar .navigation button {
  margin: 0 10px;
}

.controlBar .navigation a[href=""] {
  visibility: hidden;
}

.controlBar .imageBtn {
  padding: 18px;
  margin: 0;
}
.imageBtn.selected {
  background-color: var(--accentColor);
}
.imageBtn.selected svg {
  fill: white;
}
button {
  border: none;
}
</style>
