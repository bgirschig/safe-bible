<template>
  <div id="contentsTable" class="">
    <h1>The <span class="highlight">safe</span> Holy Bible</h1>
    <h2>Annexes</h2>
    <div class="columns">
      <!-- This is done manually because it doesn't integrate well with 'regular' books -->
      <router-link class="bookLink onlyExact" :to="`/`">Home</router-link>
      <router-link class="bookLink" :to="`/highlights`">Highlights</router-link>
      <router-link class="bookLink" :to="`/annexes#translation`">A note on translation</router-link>
      <router-link class="bookLink" :to="`/annexes#details`">Technical details</router-link>
      <router-link class="bookLink" :to="`/annexes#contact`">Contact</router-link>
    </div>

    <h2>Old testament</h2>
    <div class="columns">
      <router-link
        v-for="book in oldTestament"
        :key="book.id"
        class="bookLink"
        :to="`/${book.id}`">
        {{ book.short }}
      </router-link>
    </div>

    <h2>New testament</h2>
    <div class="columns">
      <router-link
        v-for="book in newTestament"
        :key="book.id"
        class="bookLink"
        :to="`/${book.id}`">
        {{ book.short }}
      </router-link>
    </div>
  </div>
</template>

<script>
import appState from '@/appState.js';

export default {
  data() {
    return { appState };
  },
  computed: {
    annexes() {
      return appState.books.filter((book) => book.group === 'annexes');
    },
    newTestament() {
      return appState.books.filter((book) => book.group === 'new-testament');
    },
    oldTestament() {
      return appState.books.filter((book) => book.group === 'old-testament');
    },
  },
};
</script>

<style scoped>
#contentsTable {
  position: fixed;
  top: 0;
  left: 0;
  background-color: var(--bgColor);
  width: 100%;
  height: calc(100% - 63px);
  z-index: 3;
  padding: 15px;
  box-sizing: border-box;
  overflow-y: auto;
  max-width: 500px;
  border-right: 1px solid rgba(var(--fontColor), 0.15);
  font-size: 1em;
  text-align: center;
  font-family: 'Source Serif Pro', serif;
}

h1 {
  margin-top: 1.3em;
  font-weight: normal;
  text-align: center;
}
h1 .highlight {
  font-family: "Roboto";
  font-size: 0.8em;
  font-variant: small-caps;
}

.columns {
  line-height: 1.7em;
}

#contentsTable.open {
  left: 0;
}
.bookLink {
  margin-bottom: 0.7em;
  display: inline-block;
  display: block;
}

.books {
  display: flex;
  justify-content: space-between;
}
.books div {
  flex: 1 1;
}
.columns {
  column-count: 2;
}
.onlyExact.router-link-exact-active,
:not(.onlyExact).router-link-active {
  color: var(--accentColor);
  font-weight: bold;
}
</style>
