<template>
  <div id="cover" class="cover">
    <div class="titleZone">
      <div class="title">
        <div class="big">THE</div>
        <div class="small highlight">safe</div><br>
        <div class="big" style="left: 26px;">HOLY</div><br>
        <div class="big" style="left: -8px;">BIBLE</div>
      </div>
    </div>
    <div class="crossZone">
      <Cross />
    </div>
    <div class="buttonZone">
      <a href="#main" class="scrollButton">
        <ArrowDown />
      </a>
    </div>
  </div>
</template>

<script>
import ArrowDown from '@/assets/icons/arrow_down.svg';
import Cross from '@/assets/cover/cross.svg';

export default {
  components: { ArrowDown, Cross },
};
</script>

<style scoped>
.cover {
  background-color: var(--accentColor);
  color: #DEA000;
  width: 100%;
  height: 100vh;
  z-index: 3;
  position: relative;

  background-image: url("~@/assets/cover/background.jpeg");
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
}
.title {
  line-height: 2.5rem;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: bold;
}
.title div {
  position: relative;
  display: inline-block;
  top: 8px;
}
.title .big {
  font-size: 64px;
}
.title .small {
  font-size: 24px;
}
.title .highlight {
  line-height: normal;
  color: var(--accentColor);
  background-color: #DEA000;
  padding: 2px 6px;
  top: unset;
  left: 5px;
}

.cross {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 50vw;
  height: 70vw;
}
.cross div {
  background-color: #DEA000;
  position: absolute;
}
.cross .horizontal {
  transform: translate(0, -50%);
  top: 25%;
  width: 100%;
  height: 2vw;
}
.cross .vertical {
  left: 50%;
  transform: translate(-50%, 0);
  width: 2vw;
  height: 100%;
}

.titleZone {
  height: 40vh;
  text-align: center;
}
.crossZone {
  height: 40vh;
  text-align: center;
}
.crossZone svg {
  width: 100%;
  height: 100%;
}

.buttonZone {
  height: 20vh;
  position: relative;
}
.scrollButton {
  position: absolute;
  padding: 6px 6px 6px 6px;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 100%;
  color: white;
  left: 50%;
  top: 10%;
  transform: translate(-50%, -50%);
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
