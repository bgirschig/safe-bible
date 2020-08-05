<template>
  <div id="app">
    <div class="debug">Vuejs</div>
    <Controlbar v-if="appState.books.length>0" @toggleIndex="toggleIndex" :navState="appState.nav"/>
    <router-view :key="$route.path"/>
  </div>
</template>

<script>
import Controlbar from '@/components/Controlbar.vue';
import appState from '@/appState.js';

export default {
  data() {
    return {
      appState,
    };
  },
  async mounted() {
    const response = await fetch('http://localhost:8080/books');
    const data = await response.json();
    appState.books = data;
    this.updateAppState();
  },
  components: { Controlbar },
  watch: {
    $route() {
      this.updateAppState();
    },
  },
  methods: {
    toggleIndex() {
      console.log('toggleIndex');
    },
    updateAppState() {
      appState.bookId = this.$route.params.bookId;
    },
  },
};
</script>

<style lang="scss">
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
  padding: 20px 25px;
}

.debug {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 999;
  background-color: red;
  padding: 5px;
  display: none;
}
.debug:hover {
}
</style>
