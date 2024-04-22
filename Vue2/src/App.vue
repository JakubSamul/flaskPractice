<template>
  <div :class="[{ flexStart: step === 1 }, 'wrapper']">
    <transition name="slide">
      <img src="./assets/logo.png" alt="description of image" class="logo" v-if="step === 1">
    </transition>
    <transition name="fode">
      <Background v-if="step === 0" />
    </transition>
    <Claim v-if="step === 0" />
    <SearchImput v-model="searchValue" @input="handleInput" :dark="step === 1" />
    <div class="results" v-if="results && !loading && step ===1">
      <Item v-for="item in results" :item="item" :key="item.data[0].
      nasa_id" @click.enter="handleModelOpen(item)" />
    </div>
    <div class="loader" v-if="step === 1 && loading" />
    <Model v-if="modelOpen" :item="modelItem" @closeModel="modelOpen = false" />
  </div>
</template>
<script>
import axios from 'axios';
import debounce from 'lodash.debounce';
import Claim from '@/components/Claim.vue';
import SearchImput from '@/components/SearchImput.vue';
import Background from '@/components/Background.vue';
import Item from '@/components/Item.vue';
import Model from '@/components/Model.vue';

const API = 'https://images-api.nasa.gov/search';

export default {
  name: 'App',
  components: {
    Background,
    Item,
    Model,
    Claim,
    SearchImput,
  },
  data() {
    return {
      modelOpen: false,
      modelItem: null,
      loading: false,
      step: 0,
      searchValue: '',
      results: [],
    };
  },
  methods: {
    handleModelOpen(item) {
      this.modelOpen = true;
      this.modelItem = item;
    },
    // eslint-disable-next-line
    handleInput: debounce(function () {
      this.loading = true;
      console.log(this.searchValue);
      axios.get(`${API}?q=${this.searchValue}&media_type=image`)
        .then((response) => {
          this.results = response.data.collection.items;
          this.loading = false;
          this.step = 1;
        })
        .catch((error) => {
          console.log(error);
        });
    }, 1000),
  },
};
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;400;600;800&display=swap');

* {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: 'Montserrat', sans-serif;
  margin: 0;
  padding: 0;
}

.fode-enter-active, .fode-leave-active {
  transition: opacity 1s ease;
}

.fode-enter, .fode-leave-to {
  opacity: 0;
}

.slide-enter-active, .slide-leave-active {
  transition: margin-top 1s ease;
}

.slide-enter, .slide-leave-to {
  margin-top: -50px;
}

.wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 30px;
  width: 100%;
  min-height: 100vh;
  justify-content: center;

  &.flexStart {
    justify-content: flex-start;
  }
}

.loader {
  margin-top: 100px;
  display: inline-block;
  width: 80px;
  height: 80px;

  @media (min-width: 768px) {
    width: 90px;
    height: 90px;
  }
}
.loader:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #1e3d4a;
  border-color: #1e3d4a transparent #1e3d4a transparent;
  animation: loader 1.2s linear infinite;

  @media (min-width: 768px) {
    width: 90px;
    height: 90px;
  }
}
@keyframes loader {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.logo {
  position: absolute;
  top: 40px;
}

.results {
  margin-top: 30px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 20px;

  @media (min-width: 768px) {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
</style>
