<template>
<header class="layout-header">
  <div class="container">

    <nav class="navbar desktop">
      <h1>
        <router-link :to = "{ name:'index' }" exact class="navbar-brand">
          <img src="@/assets/images/logo.png" width="" height="27" class="d-inline-block align-top" alt="" loading="lazy">
        </router-link>
      </h1>
			<div class="collapse navbar-collapse">
        <ul class="navbar-nav desktop">
          <li class="nav-item active-only dropdown">
            <router-link :to="{ name:'Login' }" exact class="nav-link px-20" >blank1</router-link>
          </li>
          <li class="nav-item dropdown">
            <router-link :to="{ name:'Login' }" class="nav-link px-20" >blank1</router-link>
          </li>
          <li class="nav-item dropdown">
            <router-link :to="{ name:'Login' }" class="nav-link px-20" >blank1</router-link>
          </li>
          
          <!-- 비 로그인 -->
          <li class="nav-item">
            <router-link :to = "{ name:'Login' }">
              <!--<font-awesome-icon icon="fa-solid fa-circle-user" />-->
              Login
              </router-link> 
          </li>
          <li> | </li>
          <li class="nav-item">
            <router-link :to = "{ name:'Singup' }">
              <!--<font-awesome-icon icon="fa-solid fa-user-plus" />-->
              Singup
            </router-link>
          </li>
          <li class="nav-item">
            <button @click="logout()">Logout</button>
          </li>
          <li class="nav-item">
            <router-link :to = "{ name:'User' }">
              <font-awesome-icon icon="fa-solid fa-circle-user" />
              내 도서
            </router-link>
          </li>
          <!-- 로그인 -->
          <!--<li class="nav-item line-none dropdown">
            <a href="javascript:void(0)" class="btn login nav-link" role="button">
              <i class="xi-user mr-6"><span class="sr-only">유저 아이콘</span></i>
              <span class="mr-6">홍길동님</span>
              <i class="xi-angle-down"><span class="sr-only">화살표 아이콘</span></i>
            </a>
            <div class="dropdown-menu pt-50">
              <div class="dropdown-wrap">
                <a href="javascript:void(0)" class="dropdown-item">내정보 메뉴1</a>
                <a href="javascript:void(0)" class="dropdown-item">내정보 메뉴1</a>
                <a href="javascript:void(0)" class="dropdown-item">내정보 메뉴2</a>
                <a href="javascript:void(0)" class="dropdown-item">로그아웃</a>
              </div>
            </div>
          </li>-->
          
        </ul>
        <ul class="navbar-nav mobile">
          <li class="nav-item">
            <a href="javascript:void(0)">
              <i class="xi-bars"><span class="sr-only">메뉴 아이콘</span></i>
            </a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
  <!--<nav class="navbar mobile">
    <div class="container">
      
      <ul class="navbar-nav">
        <li class="nav-item d-flex align-items-center justify-content-between mb-30">
          <h3>title</h3>
          <button type="button" class="btn-navbar-close">
            <i class="xi-close"><span class="sr-only">메뉴 닫기</span></i>
          </button>
        </li>
        <li class="nav-item">
          <a href="">menu 01</a>
        </li>
      </ul>
    </div>
  </nav>-->
</header>
</template>

<script>
import { getAPI } from '@/axios-api'

export default {
  name: 'Header',

  data () {
    return {
      login: [],
    }
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
      this.$router.push("/")
    },
  },
}

</script>

//<style lang="scss">
//@import "@/assets/scss/common.scss";
//@import "@/assets/scss/header.scss";
//</style>