<template>
  <div id="sharingTarget">
    <h2>{{verse.title}}</h2>
    <p>{{verse.text}}</p>
    <p>This verse was detected as</p>
    <p>
      <span
        v-for="label in labels"
        :key="label['id']"
        class="score-display"
        :style="{ backgroundColor: label.color }">
        {{label.name}}
      </span>
    </p>
    <button @click="$emit('cta')" class="accent">learn more</button>
  </div>
</template>

<script>
import appState from '@/appState.js';

export default {
  props: {
    verse: { type: Object },
  },
  computed: {
    labels() {
      if (!appState.labelMap) return [];
      return this.verse.labels.map((key) => appState.labelMap[key]);
    },
  },
};
</script>

<style scoped>
#sharingTarget {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  color: rgb(var(--fontColor));
  background-color: var(--bgColor);
  padding: 20px;
  border-radius: 3px;
  text-align: center;
  box-sizing: border-box;
  max-width: calc(100% - 20px);
  width: 450px;
}
</style>
