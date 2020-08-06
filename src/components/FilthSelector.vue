<template>
  <div id="filthSelector" class="card">
    <p>What do you want to read?</p>

    <FilthSelectorSVG />
  </div>
</template>

<script>
import FilthSelectorSVG from '@/assets/ui/filthSelector.svg';

export default {
  components: { FilthSelectorSVG },
};
</script>

<style scoped>
#filthSelector {
  user-select: none;
  width: 80%;
  max-width: 250px;

  border: 1px solid rgba(var(--fontColor), 0.15);
  background-color: var(--bgColor);
  display: inline-block;
  padding: 10px 20px;
  border-radius: 4px;
  margin: 10px;
  box-sizing: border-box;
}

#filthSelector p {
  margin-top: 0;
}

#filthSelector .dial {
  width: 15vw;
  height: 15vw;
  background-color: var(--accentColor);
  border-radius: 100%;
  position: relative;
}
#filthSelector .dial::after {
  content: "";
  width: 75%;
  height: 75%;
  border: 3px solid white;
  border-radius: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
#filthSelector .indicator {
  width: 30%;
  height: 3px;
  background-color: white;
  position: absolute;
  top: 50%;
  right: 13%;
  transform: translate(0, -50%);
}

.dial.up {
  transform: rotate(-40deg);
}
.dial.middle {
  transform: rotate(0);
}
.dial.down {
  transform: rotate(40deg);
}
</style>
