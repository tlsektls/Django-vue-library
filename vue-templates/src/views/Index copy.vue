<template>
  <div class="index">
    <Header></Header>

    <main class="layout-main content" id="content">

      <!-- banner -->
      <div class="banner">
        <!--<img src="@/assets/images/library-banner.jpeg">-->
        <div class="container">
          <h2>책나무 작은 도서관</h2>
          <p>책으로 둘러싸인 작은 미로에서 혼자만의 지적 모험을...</p>

          <div class="search-wrap">
            <input type="search" >
            <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
          </div>
        </div>
      </div>

      <!--  -->
      <div class="container">

        <div class="row">
          <div class="col-10">
            <!-- 추천 / 신규 / 인기 도서 top3 slider -->
            <TopRank></TopRank>

          </div>
          <div class="col-2">
            <h3>도서관 일정</h3>
            <div class="inner">
              <datepicker inline="true" :highlighted="{
                dates: getOffDay}"
              >
              </datepicker>
            </div></div>
        </div>


        <!--search-->
          <SearchBar></SearchBar>

          <div class="news">
            <h3>최근 도서관 뉴스 <a href="">></a></h3>
            <News></News>
          </div>


        <!-- 공지사항 / 일정 / 위치 -->
        <div class="notice-row row">
          <div class="col-4">
            <h3>공지사항</h3>
            <div class="inner">
              
            </div>
          </div>

          <div class="col-4">
          </div>

          <div class="col-4">
            <h3>도서관 위치</h3>
            <div class="inner">
              <Map></Map>
            </div>
          </div>
        </div>


      </div>

    </main>

    <Footer></Footer>

  </div>
</template>

<script>
  import { getAPI } from '@/axios-api'
  import Header from '@/components/Header'
  import Footer from '@/components/Footer'
  import News from '@/components/inner/News'
  import Map from '@/components/inner/Map'
  import TopRank from '@/views/inner/TopRank/TopRank'
  import SearchBar from '@/views/inner/SearchBar'
  import Datepicker from 'vuejs3-datepicker';

// Import Swiper styles
import "swiper/css";

import "swiper/css/pagination";
import "swiper/css/navigation";


  export default {
    name: 'Index',
    data () {
      return {
        bookData: [],
        offDayData: [],
      }
    },
    components: {
      Header, 
      Footer,
      News,
      Map,
      TopRank,
      SearchBar,
      Datepicker,
    },
    beforeCreate() {
      this.$store.commit('initializerStore')
      const access = this.$store.state.access
      if(access) {
        getAPI.defaults.headers.common['Authorization'] = "JWT " + access
      } else {
        getAPI.defaults.headers.common['Authorization'] = ''
      }
    },
    created () {
      getAPI.get('/book/')
        .then(response => {
          console.log('book API has recieved data')
          console.log(response)
          this.IndexData = response.data
        })
        .catch(err => {
          console.log(err)
        })
      getAPI.get('/offday/')
        .then(response => {
          console.log('offday API has recieved data')
          console.log(response)
          this.offDayData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    mounted() {
      setInterval(() => {
        this.getAccess()
      }, 6000000) //6000000
    },
    methods: {
      getAccess(e) {
        const accessData = {
          refresh: this.$store.state.refresh
        }
        getAPI.post('api/v1/jwt/refresh', accessData)
        .then(response => {
          const access = response.data.access
          localStorage.setItem("access", access)
          this.$store.commit('setAccess', access)
        })
        .catch(error => {
          console.log("refresh", error)
        })
      },
      logout() {
        this.getAccess()
        console.log("LOGOUT")
        localStorage.setItem("access", '')
        localStorage.setItem("refresh", '')
        this.$store.commit('removeToken')
      },
    },
    computed: {
      getOffDay() {
        const dateArr = []
        for(let i=0; i<this.offDayData.length; i++) {
          let date = this.offDayData[i]['offday']
          dateArr.push(new Date(date))
        }
        return dateArr
      }
    },
  }
</script>

<style lang="css">
/*@charset "utf-8";*/
@import "@/assets/fonts/CookieRun/cookie.css";
@import "@/assets/fonts/pretendard/pretendard.css";
</style>

<style lang="scss">
@charset "utf-8";
//@import "@/assets/scss/common.scss";
@import "@/assets/scss/index.scss";



.vuejs3-datepicker__calendar-topbar {
  display: none;
}
</style>

