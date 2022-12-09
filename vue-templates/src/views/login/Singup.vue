<template>
  <div class="login">
    <Header></Header>

    <div class="content">
      <div class="container">
				<h1>회원가입폼</h1>
 
				<form @submit.prevent="submitForm">
          <label for="username">username</label>
          <input type="test" name="username" v-model="username"><br>
          <label for="email">email</label>
          <input type="email" name="email" v-model="email"><br>
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
  import Header from '../../components/Header'
  import Footer from '../../components/Footer'
  export default {
    name: 'Login',
    data () {
      return {
        username: null,
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
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email,
        }

        getAPI.post('api/v1/users/', formData)
        .then(response => {
          console.log(response)
          console.log('login API has recieved data')
          this.$router.push('/Login')
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

