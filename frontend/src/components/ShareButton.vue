<template>
  <button class="shareButton" @click="open" :aria-label="`Share via ${platformName}`">
    <slot />
  </button>
</template>

<script>
export default {
  props: {
    url: { type: String },
    platformName: { type: String },
    popupSize: { type: Array, default: () => [520, 400] },
  },
  methods: {
    open() {
      const [width, height] = this.popupSize;
      const left = Math.floor((window.innerWidth - width) * 0.5);
      const top = Math.floor((window.innerHeight - height) * 0.5);
      window.open(this.url, '', `top=${top},left=${left},width=${width},height=${height},menubar=no,scrollbars=no,statusbar=no'`);
      this.$matomo.trackEvent('shareVerse', this.platformName);
    },
  },
};
</script>

<style scoped>
  .shareButton {
    padding: 5px;
    filter: saturate(0);
  }
  .shareButton:hover {
    filter: none;
    background-color: transparent;
  }
  svg {
    width: 40px;
    height: 40px;
  }
</style>
