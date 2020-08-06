<template>
  <div class="infoOverlayWrapper">
    <div
      @click="$emit('close')"
      class="overlayBackground" />
    <div class="infoOverlay" ref="overlay" @click.stop>
      <header>
        <span>This verse was hidden because it&nbsp;contains</span>
      </header>
      <div
        v-for="label in target.labels"
        :key="label.id"
        class="score-display"
        :style="{ backgroundColor: label.color }">{{label.name}}</div>

      <p class="sharing">
        <ShareButton platformName="email"
          :url="`mailto:?subject=${shareTitle}&body=${shareText}%0D%0A${shareUrl}`">
          <emailIcon />
        </ShareButton>
        <ShareButton platformName="facebook"
          :url="`https://www.facebook.com/sharer.php?u=${shareUrl}`">
          <facebookIcon />
        </ShareButton>
        <ShareButton platformName="pinterest"
          :url="`https://pinterest.com/pin/create/bookmarklet?url=${shareUrl}&description=${shareText}`">
          <pinterestIcon />
        </ShareButton>
        <ShareButton platformName="reddit"
          :url="`http://www.reddit.com/submit?url=${shareUrl}&title=${shareText}`">
          <redditIcon />
        </ShareButton>
        <ShareButton platformName="twitter"
          :url="`https://twitter.com/intent/tweet?url=${shareUrl}&text=${shareText}`">
          <twitterIcon />
        </ShareButton>
      </p>
    </div>
  </div>
</template>

<script>
import ShareButton from '@/components/ShareButton.vue';
import emailIcon from '@/assets/icons/social/email.svg';
import facebookIcon from '@/assets/icons/social/facebook.svg';
import pinterestIcon from '@/assets/icons/social/pinterest.svg';
import redditIcon from '@/assets/icons/social/reddit.svg';
import twitterIcon from '@/assets/icons/social/twitter.svg';

export default {
  components: {
    emailIcon,
    facebookIcon,
    pinterestIcon,
    redditIcon,
    twitterIcon,
    ShareButton,
  },
  data() {
    return {
      shareTitle: '',
      shareText: '#safeBible #artImproved',
    };
  },
  computed: {
    shareUrl() {
      const verseId = `${this.$route.params.bookId}/${this.$route.params.chapterIdx}/${this.target.verseIdx}`;
      return encodeURIComponent(`https://${window.location.host}/?verse=${verseId}`);
    },
  },
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

  padding: 11px 13px 11px 21px;
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
  margin: 10px 0;
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

.sharing {
  line-height: 45px;
  margin-bottom: 0;
  margin-top: 20px;
}

.shareButton {
  margin: 0 3px;
}

</style>
