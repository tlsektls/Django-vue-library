<template>
	<div class="suggest">
		<Swiper3 :bookData="bookData"></Swiper3>
	</div>
</template>

<script>
import { getAPI } from '@/axios-api'
import Swiper3 from '@/components/inner/Swiper3'

export default {
  name: "Suggest",
  data() {
    return {
      bookData: [],
    }
  },
  components: {
    Swiper3,
  },
  created () {
      getAPI.get('/bookSuggest/?title=구름을%20키우는%20방법,아버지의%20해방일지,은하환담')
        .then(response => {
          console.log('suggest-book API has recieved data')
          console.log(response)
          console.log(response.data[0].author)
          this.bookData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  },
};
</script>
