<template>
  <div class="">
    <Header></Header> 
      <div class="album py-5 bg-light">
        <h3>newsboard</h3>
        <!--<div>{{APIData}}</div>-->
        <div class="container">
          <div class="row">

          <ol>
            <li v-for="news in NewsBoardData" :key="news.id">
              <!--<a :href="news.id">{{ news.news_title }}</a>-->
              <!--<router-link v-bind:to="`/NewsBoard/News/${news.id}`">{{ news.news_title }}</router-link>-->
              <router-link v-bind:to="{ name: 'News', params: { title: news.news_title, id: news.id, text:news.news_content }}">{{ news.news_title }}</router-link>
            </li>
          </ol>

          </div>
        </div>                                     
      </div>

    <Footer></Footer>
  </div>
</template>

<script>
  import { getAPI } from '../axios-api'
  import Header from '../components/Header'
  import Footer from '../components/Footer'
  export default {
    name: 'Books',
    data () {
      return {
          NewsBoardData: [],
        }
    },
    components: {
      Header,
      Footer
    },
    //created () {
    //    getAPI.get('/newsboard/',)
    //      .then(response => {
    //        console.log(response)
    //        console.log('newsboard API has recieved data')
    //        this.NewsBoardData = response.data
    //      })
    //      .catch(err => {
    //        console.log(err)
    //      });

    //}
  }
</script>

<style scoped>

</style>

