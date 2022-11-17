<template>
  <div class="index">
    <Header></Header>

    <div class="content">
      <div class="banner">
        <div class="container">
          <div class="news">
            <h3>최근 도서관 뉴스 <a href="">></a></h3>
            <News></News>
          </div>
        </div>
      </div>


        <div class="notice-row row">
          <div class="col-4">
            <h3>공지사항</h3>
            <div class="inner">
              
            </div>
          </div>

          <div class="col-4">
            <h3>도서관 일정</h3>
            <div class="inner">
              
            </div>
          </div>

          <div class="col-4">
            <h3>도서관 위치</h3>
            <div class="inner">
              <Map></Map>
            </div>
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
  import News from '../components/inner/News'
  import Map from '../components/inner/Map'
  export default {
    name: 'Index',
    data () {
      return {
        IndexData: [],
        NewsData: [],
        PublisherData: [],
      }
    },
    components: {
      Header, 
      Footer,
      News,
      Map,
    },
    created () {
      getAPI.get('/newsboard/',)
        .then(response => {
          console.log(response)
          console.log('newsboard API has recieved data')
          this.NewsData = response.data
        })
        .catch(err => {
          console.log(err)
        })
      getAPI.get('/publisher/',)
        .then(response => {
          console.log(response)
          console.log('publisher API has recieved data')
          this.PublisherData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
</script>

<style lang="scss">
@charset "utf-8";
@import "@/assets/scss/common.scss";
@import "@/assets/scss/body.scss";
</style>

