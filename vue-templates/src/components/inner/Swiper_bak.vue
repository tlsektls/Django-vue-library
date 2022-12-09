<template>
  <div>
                <swiper
                  :slidesPerView="3"
                  :spaceBetween="30"
                  :slidesPerGroup="3"
                  :loop="true"
                  :loopFillGroupWithBlank="true"
                  :pagination="{
                    clickable: true,
                  }"
                  :navigation="true"
                  :modules="modules"
                  class="mySwiper"
                >

      <swiper-slide v-for="book in bookData" :key="book">
        <router-link :to="{ name:'', params:{}}">
          <img :src="'http://127.0.0.1:8000'+book.image" alt="book-img"/>
          <p>{{ book.title }}</p>
        </router-link>
      </swiper-slide>
                  <!--<swiper-slide>Slide 1</swiper-slide>
                  <swiper-slide>Slide 2</swiper-slide>
                  <swiper-slide>Slide 2</swiper-slide>
                  <swiper-slide>Slide 2</swiper-slide>
                  <swiper-slide>Slide 2</swiper-slide>-->
                </swiper>
  </div>
</template>

<script>
  import Swiper3 from '@/components/inner/Swiper3'
  import { Pagination, Navigation } from "swiper";
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
  },
  components: {
    Swiper,
    SwiperSlide,
  },
  created () {

  },
  setup() {
    return {
      modules: [Pagination, Navigation],
    };
  },
};
</script>

