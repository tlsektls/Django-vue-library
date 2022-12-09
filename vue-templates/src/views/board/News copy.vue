<template>
  <div class="">
    <Header></Header> 
		
    <h3>도서관 뉴스</h3>
				
    <div class="container">
<!--
			<ul v-for="news in newsData" :key="news.id" class="col-md-4">
        <li>{{ news }}</li>
      </ul>-->

      <div class="board">
        <div class="board-head">
          <p>뉴스 제목</p>
          <p>뉴스 날짜</p>
        </div>
        <ul class="board-body">

          <li v-for="news in newsData" :key="news.id" class="col-md-4">
            <router-link :to="{ name:'NewsInner', params:{id:news.id}}">{{ news.news_title }}</router-link>
            <p>{{ news.news_date }}</p>
          </li>
        </ul>
      </div>



    </div>

    <Footer></Footer>
  </div>
</template>

<script>
  import { getAPI } from '../../axios-api'
  import Header from '../../components/Header'
  import Footer from '../../components/Footer'
  export default {
    name: 'News',
    data () {
      return {
        newsData: [],
        paramsData: null
      }
    },
    //props: {
    //  data: {
    //    type: String,
    //    default: ""
    //  }
    //},
    components: {
      Header,
      Footer
    },
    created () {
      getAPI.get('/newsboard/')
        .then(response => {
          console.log(response)
          console.log('newsboard API has recieved data')
          this.newsData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    mounted() {
      this.paramsData = this.data /* this.$route.params.data 로도 사용가능 */
    },

  }

</script>

<style scoped>

</style>

