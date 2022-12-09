<template>
  <div class="swiper-wrap">

  <swiper class="swiper" :options="swiperOptions">
    <swiper-slide v-for="book in bookData" :key="book">
      <router-link :to="{ name:'', params:{}}">
        <div class="img-wrap"><img :src="'http://127.0.0.1:8000'+ book.image" alt="book-img"></div>
        <p>{{ book.title }}</p>
      </router-link>
    </swiper-slide>

  </swiper>

    <!-- pagination -->
		<div class="swiper-pagination" slot="pagination"></div>
        
		<!-- navigation -->
		<div class="swiper-button-prev swiper-btn-prev" slot="button-prev"></div>
		<div class="swiper-button-next swiper-btn-next" slot="button-next"></div>

  </div>
</template>

<script>
  //import { Pagination, Navigation } from "swiper";
  //import { Swiper, SwiperSlide } from "swiper/vue";
  import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

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
			swiperOptions: {
        slidesPerView: "3",
        spaceBetween: "30",
        slidesPerGroup: "3",
        loop: "true",
				pagination: {
					el: '.swiper-pagination',
          clickable: true
				},
				navigation: {
					nextEl: '.swiper-button-next',
					prevEl: '.swiper-button-prev',
				},                    
			},
		}
  },
  components: {
    Swiper,
    SwiperSlide,
  },
  		computed: {
			swiper() {
				return this.mySwiper.$swiper;
			}
		},
  created () {

  },
  //setup() {
  //  return {
  //    modules: [Pagination, Navigation],
  //  };
  //},
};
</script>

