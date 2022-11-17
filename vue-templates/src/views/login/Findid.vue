<template>
  <div class="login">
    <Header></Header>

    <div class="content">
      <div class="container">
				<h1>비밀번호 찾기</h1>
 
				<form name="f1" method="post">

				</form>
				
				<button type="button" onclick="memReg()">비밀번호 찾기</button>

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
    name: 'Login',
    data () {
      return {
        LoginData: [],
      }
    },
    components: {
      Header, 
      Footer,
    },
    created () {
      //getAPI.get('/login/',)
      //  .then(response => {
      //    console.log(response)
      //    console.log('login API has recieved data')
      //    this.LoginData = response.data
      //  })
      //  .catch(err => {
      //    console.log(err)
      //  })
    }
  }
</script>

<style lang="scss">
@charset "utf-8";
@import "@/assets/scss/body.scss";
</style>

