<template>
	<div class="suggest">
		<Swiper3 :bookData="bookData"></Swiper3>
	</div>
</template>

<script>
import { getAPI } from '@/axios-api'
import Swiper3 from '@/components/inner/Swiper3'

export default {
  name: "NewBook",
  data() {
    return {
      bookData: [],
    }
  },
  components: {
    Swiper3,
  },
  created () {
      getAPI.get('/bookNew/')
        .then(response => {
          this.bookData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  },
};
</script>