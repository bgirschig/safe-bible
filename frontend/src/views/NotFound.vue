<template>
  <main id="main">
    <div class="text">
      <p>Sorry, we couldn't find the page you're looking for</p>
      <p>
        <router-link
          class="btnLink"
          to="/#main">
          Back to Home
        </router-link>
        <button @click="appState.currentPanel = 'bookBrowser'">
          Open Books browser
        </button>
      </p>
    </div>
  </main>  
</template>

<script>
import appState from '@/appState.js';

export default {
  data() {
    return { appState };
  },
}
</script>

<style scoped>
#main {
  text-align: center;
  font-size: 1.2em;
}
.btnLink, button {
  margin: 5px;
}
</style>
