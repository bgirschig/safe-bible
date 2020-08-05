<template>
  <div class="infoOverlayWrapper">
    <div
      @click="$emit('close')"
      class="overlayBackground" />
    <div class="infoOverlay" ref="overlay" @click.stop>
      <header>
        <span>This verse was hidden because it&nbsp;contains</span>
        <button class="share"><ShareIcon /></button>
      </header>
      <div
        v-for="label in target.labels"
        :key="label.id"
        class="score-display"
        :style="{ backgroundColor: label.color }">{{label.name}}</div>
    </div>
  </div>
</template>

<script>
import ShareIcon from '@/assets/icons/share.svg';

export default {
  components: { ShareIcon },
  props: {
    target: { type: Object },
  },
  watch: {
    target() {
      this.updatePosition();
    },
  },
  methods: {
    updatePosition() {
      const targetSencence = this.target.$el;
      const overlay = this.$refs.overlay;

      let left;
      const overlayWidth = overlay.getBoundingClientRect().width;
      if (window.innerWidth < overlayWidth + 25) {
        left = (window.innerWidth - overlayWidth) / 2;
      } else {
        left = Math.min(targetSencence.offsetLeft, window.innerWidth - overlayWidth - 25);
      }

      overlay.style.top = `${targetSencence.offsetTop}px`;
      overlay.style.left = `${left}px`;
    },
  },
  mounted() {
    this.updatePosition();
  },
};
</script>

<style scoped>
.infoOverlay {
  top: 0;
  left: 0;
  /* The 5px offset here is to account for the trick we're using to
  have padding on the backgrounds of individual lines (solid box
  shadows, 5px on each side). This ensures the overlay is aligned
  with the box visible to the user */
  transform: translate(-5px, calc(-100% - 10px));
  position: absolute;
  z-index: 2;
  overflow: hidden;
  box-sizing: border-box;
  width: calc(100vw - 40px);
  max-width: 380px;

  padding: 8px 18px;
  font-size: 1rem;

  background-color: var(--bgColor);
  box-shadow: rgba(0, 0, 0, 0.7) 0 0 10px;
  border-radius: 4px;
  font-family: "Roboto", sans-serif;

}
.infoOverlay button {
  border: none;
}
.infoOverlay header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.infoOverlay header button {
  padding: 5px 5px 2px 5px;
}
.infoOverlay h2 {
  font-weight: normal;
  text-align: left;
}
.score-display {
  padding: 7px 9px;
  font-family: "Roboto", sans-serif;
  color: white;
  border-radius: 100px;
  display: inline-block;
  padding: 4px 14px;
  font-size: 0.8em;
  margin: 5px 3px;
}
.overlayBackground {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(var(--fontColor), 0.8);
}
</style>
