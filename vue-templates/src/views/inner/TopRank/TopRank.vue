<template>
	<div class="top-rank">
    <div class="rank-btn-wrap">
      <button 
      class="rank-btn normal" 
      :class="{ active: isSelCheck.isSuggest }" 
      @click="[rankSelect($event), this.isSelCheck.isSuggest=true]">
        추천
      </button>

      <button 
      class="rank-btn normal" 
      :class="{ active: isSelCheck.isNew }" 
      @click="[rankSelect($event), this.isSelCheck.isNew=true]">
        신규
      </button>

      <button 
      class="rank-btn normal" 
      :class="{ active: isSelCheck.isPor }" 
      @click="[rankSelect($event), this.isSelCheck.isPor=true]">
        인기
      </button>

      <router-link :to="{name:'Books'}" class="ml-auto">
        더보기
        <font-awesome-icon icon="fa-solid fa-plus" />
      </router-link>
    </div>

    <SuggestSwiper :class="{ none: !isSelCheck.isSuggest }"></SuggestSwiper>
    <NewSwiper :class="{ none: !isSelCheck.isNew }"></NewSwiper>
    <PopularSwiper :class="{ none: !isSelCheck.isPor }"></PopularSwiper>
	</div>
</template>
 

<script>
  import { getAPI } from '@/axios-api'
  import SuggestSwiper from '@/views/inner/TopRank/SuggestSwiper'
  import PopularSwiper from '@/views/inner/TopRank/PopularSwiper'
  import NewSwiper from '@/views/inner/TopRank/NewSwiper'

// Import Swiper styles
import "swiper/css";

import "swiper/css/pagination";
import "swiper/css/navigation";


export default {
  name: 'TopRank',
  data () {
    return {
      bookData: [],
      offDayData: [],
      isSelCheck: {
        isSuggest: true,
        isNew: false,
        isPor: false,
      }
    }
  },
  components: {
    SuggestSwiper,
    PopularSwiper,
    NewSwiper,
  },
  created () {
    
  },
  methods: {
    rankSelect(e) {
      this.isSelCheck.isSuggest = false
      this.isSelCheck.isNew = false
      this.isSelCheck.isPor = false
      console.log(e.currentTarget)
    },
  }

}
</script>