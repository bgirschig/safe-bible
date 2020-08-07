<template>
  <div id="filthSelector" class="card">
    <p>What do you want to read?</p>

    <!-- eslint-disable -->
    <svg version="1.1" viewBox="0 0 212 94" xmlns="http://www.w3.org/2000/svg">
      <path d="m65.544 48.375h34.543" fill="none" stroke="rgb(var(--fontColor))" stroke-width="1.1906"/>
      <path d="m53.632 22.171 11.613-11.911h34.84" fill="none" stroke="rgb(var(--fontColor))" stroke-width="1.1906"/>
      <path d="m53.632 73.39 11.613 11.911h34.84" fill="none" stroke="rgb(var(--fontColor))" stroke-width="1.1906"/>
      <g transform="translate(33.347 47.653)">
        <g class="dial" @click="selectNext()" :style="{transform: `rotate(${dialAngle}deg)`}">
          <circle cx="-9.4237e-5" cy="0" r="26.205" fill="var(--accentColor)" stroke-width="1.1911"/>
          <circle cx="-9.4237e-5" cy="0" r="21.44" fill="var(--accentColor)" stroke="#fff" stroke-width="2.3822"/>
          <line x1="4.7644" x2="21.44" y1="0" y2="0" stroke="#fff" stroke-width="2.3822"/>
        </g>
      </g>
      <text @click="select(0)" :class="{selected: value === 0}" x="105.84525" y="54.501022" letter-spacing="0px" stroke-width=".35832" word-spacing="0px" style="line-height:1.25" xml:space="preserve">
        <tspan x="105.84525" y="14.501022" stroke-width=".35832">None of the filth</tspan>
      </text>
      <text @click="select(1)" :class="{selected: value === 1}" x="105.33807" y="92.982712" letter-spacing="0px" stroke-width=".35832" word-spacing="0px" style="line-height:1.25" xml:space="preserve">
        <tspan x="105.33807" y="52.982712" stroke-width=".35832">Keep everything</tspan>
      </text>
      <text @click="select(2)" :class="{selected: value === 2}" x="105.26369" y="129.52921" letter-spacing="0px" stroke-width=".35832" word-spacing="0px" style="line-height:1.25" xml:space="preserve">
        <tspan x="105.26369" y="89.52921" stroke-width=".35832">Only the filth</tspan>
      </text>
    </svg>
    <!-- eslint enable -->
  </div>
</template>

<script>
export default {
  props: {
    value: { type: Number, default: 1 },
  },
  computed: {
    dialAngle() {
      return (this.value - 1) * 40;
    },
  },
  methods: {
    selectNext() {
      this.select((this.value + 1) % 3);
    },
    select(value) {
      this.$emit('change', value);
    },
  },
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
  line-height: 2em;
}

#filthSelector p {
  margin-top: 0;
  line-height: 2em;
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
#filthSelector svg text {
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
  fill: rgb(var(--fontColor));
  font-size: 14.333px;

  font-feature-settings:normal;
  font-variant-caps:normal;
  font-variant-ligatures:normal;
  font-variant-numeric:normal;
}
text.selected {
  font-weight: bold;
}
text, .dial {
  cursor: pointer;
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
