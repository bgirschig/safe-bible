<template>
  <div class="infoOverlayWrapper">
    <div
      @click="$emit('close')"
      class="overlayBackground" />
    <div class="infoOverlay" ref="overlay" @click.stop>
      <header>
        <span>This verse was hidden because it&nbsp;contains</span>
      </header>
      <span
        v-for="label in target.labels"
        :key="label.id"
        class="score-display"
        :style="{ backgroundColor: label.color }">{{label.name}}</span>

      <p class="sharing">
        <ShareButton platformName="email"
          :sharedInfo=target.verseId
          :url="`mailto:?subject=${shareTitle}&body=${shareText}%0D%0A${shareUrl}`">
          <emailIcon />
        </ShareButton>
        <ShareButton platformName="facebook"
          :sharedInfo=target.verseId
          :url="`https://www.facebook.com/sharer.php?u=${shareUrl}`">
          <facebookIcon />
        </ShareButton>
        <ShareButton platformName="pinterest"
          :sharedInfo=target.verseId
          :url="`https://pinterest.com/pin/create/bookmarklet?url=${shareUrl}&description=${shareText}`"
          :popupSize="[660, 400]">
          <pinterestIcon />
        </ShareButton>
        <ShareButton platformName="reddit"
          :sharedInfo=target.verseId
          :url="`http://www.reddit.com/submit?url=${shareUrl}&title=${shareText}`"
          :popupSize="[660, 400]">
          <redditIcon />
        </ShareButton>
        <ShareButton platformName="twitter"
          :sharedInfo=target.verseId
          :url="`https://twitter.com/intent/tweet?url=${shareUrl}&text=${shareText}&hashtags=${hashtags.join(',')}&via=ImprovedArt`">
          <twitterIcon />
        </ShareButton>
      </p>
    </div>
  </div>
</template>

<script>
import appState from '@/appState';
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
      hashtags: ['safeBible', 'ArtImproved'],
    };
  },
  computed: {
    shareUrl() {
      return encodeURIComponent(`https://${window.location.host}/?verse=${this.target.verseId}`);
    },
    shareText() {
      let [bookId, chapterIdx, verseIdx] = this.target.verseId.split('/');
      chapterIdx = parseInt(chapterIdx, 10) - 1;
      verseIdx = parseInt(verseIdx, 10) - 1;
      const book = appState.bookMap[bookId];
      if (!book) return '';

      const verseTitle = `${book.short} ${chapterIdx + 1}:${verseIdx + 1}`;
      return `I was saved from reading ${verseTitle} thanks to ArtImproved`;
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
  z-index: 1;
  overflow: hidden;
  box-sizing: border-box;
  width: calc(100vw - 40px);
  max-width: 380px;

  padding: 11px 13px 11px 21px;
  font-size: 1rem;

  background-color: var(--bgColor);
  box-shadow: rgba(0, 0, 0, 0.7) 0 0 10px;
  border-radius: 4px;
}
.infoOverlay button {
  border: none;
}
.infoOverlay header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: 1.3em;
}
.infoOverlay header button {
  padding: 5px 5px 2px 5px;
}
.infoOverlay h2 {
  font-weight: normal;
  text-align: left;
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
  margin-bottom: 0;
  margin-top: 8px;
}

.shareButton {
  margin: 0;
}
.shareButton svg {
  width: 33px;
  height: 33px;
}
</style>
