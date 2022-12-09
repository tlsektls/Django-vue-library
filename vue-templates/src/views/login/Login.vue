<template>
  <div class="login">
    <Header></Header>

    <div class="content">
      <div class="container">
				<h1>로그인폼</h1>
 
				<form @submit.prevent="submitForm">
          <label for="eamil">eamil</label>
          <input type="test" name="eamil" v-model="email"><br>
          <label for="password">password</label>
          <input type="password" name="password" v-model="password"><br>
          <button type="submit">Sign up</button>
				</form>
      </div>
      <div> check user </div>
      <div> {{this.username}} </div>
    </div>


    <Footer></Footer>

  </div>
</template>

<script>
  import { getAPI } from '../../axios-api'
  import axios from 'axios'
  import Header from '../../components/Header'
  import Footer from '../../components/Footer'
  export default {
    name: 'Login',
    data () {
      return {
        email: null,
        password: null,
      }
    },
    components: {
      Header, 
      Footer,
    },
    methods: {
      submitForm(e) {
        axios.defaults.headers.common['Authentication'] = ''
        localStorage.removeItem("access")

        const formData = {
          username: this.email,
          password: this.password,
        }

        console.log(formData)

        getAPI.post('/api/v1/jwt/create', formData)
        .then(response => {
          
          console.log(response)

          const access = response.data.access
          const refresh = response.data.refresh

          this.$store.commit('setAccess', access)
          this.$store.commit('setRefresh', refresh)

          axios.defaults.headers.common['Authentication'] = "JWT " + access

          localStorage.setItem("access", access)
          localStorage.setItem("refresh", refresh)

          let username = this.email
          localStorage.setItem("loginUser", username)

          this.$router.push("/")
        }).catch(error => {
          console.log(error)
        })
      }
    },
  }
</script>

<style lang="scss">
@charset "utf-8";
@import "@/assets/scss/body.scss";
</style>

