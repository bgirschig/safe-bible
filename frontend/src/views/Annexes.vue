<template>
  <main id="main">
    <div class="text">
      <h1>Safe Bible Annexes</h1>

      <h2 id="translation" :class="{anchorTarget: $route.hash==='#translation'}">
        A note on translation</h2>
      <div class="columns">
        <p>
          While very powerful, the current tools don’t work very well with ancient hebrew, so a
          choice had to be made about what translation to work with
        </p>
        <p>
          The New International Version (NIV) was a logical first choice, as it is the most popular
          one, but its licencing terms don’t allow reproducing the text in full. Instead, I decided
          to use the <a href="https://worldenglish.bible/">World English Bible</a>, a Public Domain,
          modern English bible
        </p>
        <p>
          If you want to compare translations while reading, click on the verse number. That verse
          will be opened on <a href="https://biblehub.com/">biblehub.com</a>, where you can compare
          a verse between 27 different translations, including the NIV, King James version, etc...
        </p>
      </div>

      <h2 id="details" :class="{anchorTarget: $route.hash==='#details'}">Technical details</h2>
      <div class="columns">
        <p>
          Every sencence in the book was sent to <a href="http://www.perspectiveapi.com">Perspective
          API</a> to determine the likelihood that it contains things like <i>violence</i>,
          <i>identity attacks</i>, <i>flirtation</i>, etc...
        </p>
        <p>
          Any verse where the likelihood for one of those higher than <strong>75%</strong> was
          labelled as 'offensive', and censored.
        </p>
        <p>
          Perspective API started at Google's <a href="https://jigsaw.google.com/">jigsaw</a> (a
          team dedicated to research and technology to keep our world safer), but has now been open
          sourced.
        </p>
        <p>
          The frontend was created using <a href="https://vuejs.org/">VueJS</a> and is hosted
          on <a href="https://cloud.google.com/appengine">appengine</a>
        </p>
        <p>
          To avoid sharing your data with advertisers, analytics are collected with
          <a href="https://matomo.org/">matomo</a>. They are only used to improve the website, and
          make sure everything is working as expected.
        </p>
      </div>

      <h2 id="contact" :class="{anchorTarget: $route.hash==='#contact'}">Contact</h2>
      <p class="center">
        If you have a question or a comment, feel free to send an email<br>
        I'll do my best to answer them.
      </p>
      <p class="center">
        <a href="mailto:bible@artimproved.com">bible@artimproved.com</a>
      </p>
    </div>
  </main>
</template>

<style scoped>
/* :target does not work with vue-router */
.anchorTarget {
  color: var(--accentColor);
  font-weight: bold;
}
.anchorTarget::before {
  content: '→ ';
}
</style>
