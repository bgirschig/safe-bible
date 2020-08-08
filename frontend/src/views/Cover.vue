<template>
  <div id="cover" class="cover">
    <div class="topHalf">
      <Logo class="logo"/>
    </div>
    <div class="bottomHalf">
      <SharingOnboarding
        class="fitWidth"
        v-if="sharedVerseInfo"
        :verse="sharedVerseInfo"
        @cta="$emit('cta', 'share-onboarding')"/>
      <div v-else class="crossWrapper">
        <Cross class="fitWidth"/>
        <div class="buttonWrapper">
          <button aria-label="start" @click="$emit('cta', 'cover')" class="scrollButton">
            <ArrowDown />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ArrowDown from '@/assets/icons/arrow_down.svg';
import Cross from '@/assets/cover/cross.svg';
import Logo from '@/assets/cover-logo.svg';
import SharingOnboarding from '@/components/SharingOnboarding.vue';

export default {
  components: {
    ArrowDown,
    Cross,
    SharingOnboarding,
    Logo,
  },
  data() {
    return {
      sharedVerseInfo: window.sharedVerseInfo,
    };
  },
};
</script>

<style scoped>
.cover {
  background-color: var(--accentColor);
  width: 100%;
  height: 100vh;
  z-index: 3;
  position: relative;

  background-image: url("~@/assets/cover/background.jpeg");
  background-position: center;
  background-size: cover;
  background-attachment: fixed;

  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-items: stretch;
}

.cover>div {
  flex-grow: 1;
  flex-shrink: 1;
  position: relative;
  flex-basis: 100%;
  box-sizing: border-box;
  text-align: center;
}
.bottomHalf {
  padding: 10px 10px 70px 10px;
}
.topHalf {
  padding: 30px 0 30px 0;
  max-height: 40vh;
}
.lower {
  padding: 20px 0 70px 0;
}
.logo {
  height: 100%;
max-width: 100%;
}
.logo path {
  fill: white;
}

.crossWrapper {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-items: stretch;
  max-height: 550px;
}
.crossWrapper svg {
  height: 100%;
  max-width: 100%;
  margin: auto;
}

.scrollButton {
  padding: 6px 6px 6px 6px;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 100%;
  color: white;
  font-size: 0;
}

.signature {
  display: flex;
  align-items: center;
  color: white;
  position: absolute;
  bottom: 20px;
  right: 20px;
  font-size: 17px;
  font-variant: small-caps;
}
.signature img {
  margin-left: 10px;
  height: 1.5em;
}
</style>
