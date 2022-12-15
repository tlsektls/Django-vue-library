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

        <div class="row g-4">
          <div class="col-xl-9 col-lg-12">
            <!-- 추천 / 신규 / 인기 도서 top3 slider -->
            <TopRank></TopRank>
          </div>

          <div class="col-xl-3 col-lg-6">
            <div class="schedule">
              <h3>도서관 일정</h3>
              <div class="inner">
                <datepicker inline="true" :highlighted="{
                  dates: getOffDay}"
                >
                </datepicker>
              </div>
            </div>
          </div>

          <div class="col-xl-4 col-lg-6">
            <div class="news">
              <h3>최근 도서관 뉴스 <router-link :to="{name:'NewsBoard'}" class="ml-auto"><font-awesome-icon icon="fa-solid fa-plus" /></router-link></h3>
              <NewsList></NewsList>
            </div>
          </div>
          <div class="col-xl-4 col-lg-6">
            <div class="suggest">
              <h3>건의 게시판 <router-link :to="{name:'NewsBoard'}" class="ml-auto"><font-awesome-icon icon="fa-solid fa-plus" /></router-link></h3>
              <div class="inner">
                
              </div>
            </div>
          </div>

          <div class="col-xl-4 col-lg-6">
            <div class="map">
              <h3>도서관 위치</h3>
              <div class="inner">
                <Map></Map>
              </div>
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
  import NewsList from '@/views/board/_News'

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
      NewsList
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
      getAPI.get('/offday/')
        .then(response => {
          this.offDayData = response.data
        })
        .catch(err => {
          console.log(err)
        })
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

			.top-rank {
				background-color: pink;
				.swiper {
					.img-wrap {
						width: 100%;
						img {
							display: block;
							width: 100%;
						}
					}
				}
			}

.vuejs3-datepicker__calendar-topbar {
  display: none;
}
</style>

