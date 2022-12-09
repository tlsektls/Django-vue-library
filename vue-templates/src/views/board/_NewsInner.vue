<template>
  <div class="NoticeBoard">
    <Header></Header> 
		
      <div class="container">
				<h1> id: {{ this.$route.params.id }}  </h1>
        
				<h3>news_title: {{this.newsData.news_title}}</h3>
        <div class="new-date">{{this.newsData.news_date}}</div>
        <div class="img-wrap"><img :src="this.newsData.news_poster"></div>
        <div class="content">{{this.newsData.news_content}}</div>
      </div>

    <Footer></Footer>
  </div>
</template>

<script>
  import { getAPI } from '@/axios-api'
  import { useRoute } from 'vue-router'
  import Header from '@/components/Header'
  import Footer from '@/components/Footer'
  export default {
    name: 'News-inner',
    data () {
      return {
        newsData: [],
      }
    },
    components: {
      Header,
      Footer,
    },
    methods : {
    },
    mounted() {
      console.log(this.$route)
    },
    created () {
      const route = useRoute();
      const id = route.params.id;
      //const formData = new FormData();
      //formData.append('id', 2);

      getAPI.get(`/newsboard/news/${id}/`)
        .then(response => {
          console.log(response)
          console.log('newsboard API has recieved data')
          this.newsData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
</script>

<style scoped>

</style>

