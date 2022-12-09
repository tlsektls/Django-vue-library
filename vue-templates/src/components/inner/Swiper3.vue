<template>
  <div class="swiper-container">
    <swiper
      :slidesPerView="3"
      :spaceBetween="36"
      :loop="true"
      :pagination="{
        clickable: true,
      }"
      ref="mySwiperRef"
      @swiper="onSwiper"
    >
      <swiper-slide v-for="book in bookData" :key="book">
        <router-link :to="{ name:'', params:{}}">
          <div class="img-wrap"><img :src="'http://127.0.0.1:8000'+book.image" alt="book-img"/></div>
          <p>{{ book.title }}</p>
        </router-link>
      </swiper-slide>
    </swiper>

    <div class="swiper-navigation">
      <button class="swiper-button-prev normal" @click="this.swiper.slidePrev()"></button>
      <button class="swiper-button-next normal" @click="this.swiper.slideNext()"></button>
    </div>
  </div>
</template>

<script>
  import { Pagination, A11y } from "swiper";
  import { Swiper, SwiperSlide } from "swiper/vue";


// Import Swiper styles
import "swiper/css";

import "swiper/css/pagination";
import "swiper/css/navigation";


export default {
  name: "Swiper3",
  props: {
    bookData: {}
  },
  data() {
    return {
      swiper: null,
    };
  },
  components: {
    Swiper,
    SwiperSlide,
    
  },
  methods: {
    onSwiper(swiper) {
      console.log(swiper);
      this.swiper = swiper;
    },
  },
  setup() {
    return {
      modules: [Pagination, A11y],
    };
  },
};
</script>

