<template>
  <div>
    <Cover @cta="handleCta"/>
    <main id="main">
      <div class="text">
        <h1 id="foreword">Foreword</h1>

        <div class="columns">
          <p>The Bible is one of the most popular books in the world, but is it safe to read ?</p>
          <p>
            This question has been tormenting since time immemorial. Across the years, attempts
            have been made to create create a version of the holy book that was safe to read for
            everybody, but they always faced the same problem: Humans, with all their biases and
            interpretations, are required to do the hard, time-consuming work.</p>
          <p>
            However, thanks to recent progress in Artificial Intelligence, tools are now available
            to do this in a rational and effortless way. Every sentence from the old and new
            testament has been rated by this tool, on multiple criteria: <i>spam</i>,
            <i>flirtation</i>, <i>profanity</i>, <i>identity attack</i>, <i>threat</i>,
            <i>inflammatory</i>, <i>toxicity</i>, <i>severe toxicity</i>, <i>sexually explicit</i>,
            <i>insult</i> and <i>obscene</i>.
          </p>
          <p>
            If you believe a verse was censored by mistake, you are probably wrong: The tool that
            was used to rate the sentences is trained on a vast amount of data, and is currently in
            use by leading tech companies around the world to make the web a better place.
          </p>
          <p>
            If you believe a verse should have been censored, you are probably wrong: The Bible is
            the infallible word of God, who is by definition good and righteous. It is therefore
            impossible to find a questionable verse there.
          </p>
        </div>

        <h1 id="howto">How to use</h1>
        <div class="columns">
          <p>
            While reading, some verses will be blacked out. This is for your own good. We advise
            you not to click on those, as this would reveal the censored text, and possibly
            traumatize you
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
            <Verse :verse="{
              verseIdx: 10,
              verseId: 'GEN/22/10',
              bibleHubLink: 'https://biblehub.com/genesis/22-10.htm',
              sentences: [
                {
                  text: 'Abraham stretched out his hand, and took the knife to kill his son.',
                  labels: ['THREAT', 'INFLAMMATORY'],
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
}
</style>
