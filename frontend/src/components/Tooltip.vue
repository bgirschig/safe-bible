<template>
  <div class="hoverTooltip">
    <slot />
  </div>
</template>

<script>
import { computeOverlayPosition } from '@/js/layout';

export default {
  props: {
    target: { type: Object },
  },
  watch: {
    target() {
      this.updatePosition();
    },
  },
  mounted() {
    this.updatePosition();
  },
  methods: {
    updatePosition() {
      const { left, top } = computeOverlayPosition(this.target.$el, this.$el);

      this.$el.style.top = `${top}px`;
      this.$el.style.left = `${left}px`;
    },
  },
};
</script>

<style scoped>
.hoverTooltip {
  position: absolute;
  padding: 5px;
  box-sizing: border-box;
  background-color: var(--bgColor);
  border: 1px solid rgba(0,0,0, 0.9);
  white-space: nowrap;
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
  border-radius: 3px;
  z-index: 3;
  transform: translate(0, -100%);
}
</style>
