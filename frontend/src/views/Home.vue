<template>
  <div>
    <Cover @cta="handleCta"/>
    <main id="main">
      <div class="text">
        <h1 id="foreword">Foreword</h1>
        <p class="center"><i>Read the bible without the hard parts, thanks to AI</i></p>
        <div class="columns">
          <p>
            The Bible is one of the most popular books in the world, but is it safe to read ?
          </p>
          <p>
            Many attempts have been made to create safer versions of the holy book, but they always
            faced the same problem: Humans, with all their biases and limitations, are required to
            do the hard, time-consuming work.
          </p>
          <p>
            However, thanks to recent advances in Artificial Intelligence, this can now be done
            in an effortless and rational way.
          </p>
          <p>
            If you believe a verse was censored by mistake, <strong>You are probably wrong</strong>:
            The tool is trained on a vast amount of data, and is currently in use by tech companies 
            around the world to make the web a better place.
          </p>
          <p>
            If you believe a verse should have been censored, <strong>You are probably wrong</strong>:
            The Bible is the infallible word of God. It is therefore impossible to find a questionable
            verse there.
          </p>
        </div>

        <h1 id="howto">How to use</h1>
        <div class="columns">
          <p>
            While reading, some verses will be blacked out. This is for your own good. We advise
            you not to click on those, as this would reveal the offending text.
          </p>
          <p>
            <Verse :verse="{
              verseIdx: 14,
              verseId: 'GEN/17/14',
              bibleHubLink: 'https://biblehub.com/genesis/17-14.htm',
              sentences: [
                {
                  text: 'The uncircumcised male who is not circumcised in the flesh of his'+
                    'foreskin, that soul shall be cut off from his people.',
                  labels: ['THREAT', 'INFLAMMATORY', 'SEXUALLY_EXPLICIT', 'OBSCENE'],
                }
              ]
            }" />
          </p>
        </div>

        <h1 id="howto">Let's go!</h1>
        <p class="center">
          <router-link
            v-on:click.native="$window._paq.push(['trackEvent', 'cta', 'best-bits'])"
            class="cta btnLink accent"
            to="/highlights">
            Read the best bits
          </router-link>
          <router-link
            v-on:click.native="$window._paq.push(['trackEvent', 'cta', 'from-start'])"
            class="cta btnLink"
            to="/GEN/1">
            Read from the start
          </router-link>
        </p>
      </div>
    </main>
  </div>
</template>

<script>
import Cover from '@/views/Cover.vue';
import Verse from '@/components/Verse.vue';
import appState from '@/appState';

export default {
  components: { Cover, Verse },
  data() {
    return { appState };
  },
  watch: {
    'appState.currentPanel': {
      handler() {
        console.log('oadfafj');
        if (appState.currentPanel) document.querySelector('#main').scrollIntoView({ behavior: 'smooth' });
      },
    },
  },
  methods: {
    handleCta(name = null) {
      document.querySelector('#main').scrollIntoView({ behavior: 'smooth' });
      this.$matomo.trackEvent('cta', name);
    },
  },
};
</script>

<style>
.cta {
  margin: 4px;
  padding: 10px;
  font-size: 0.8em;
  padding: 1em;
}
h1#foreword {
  margin-bottom: 0.5em;
}
strong {
  text-decoration: underline;
}
</style>
