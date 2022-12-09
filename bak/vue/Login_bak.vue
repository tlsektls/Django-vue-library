<template>
  <div class="login">
    <Header></Header>

    <div class="content">
      <div class="container">
				<h1>로그인폼</h1>
 
				<form name="f1" method="post">
          

						<table width="300" border="1" cellpadding="2" cellspacing="0">
						<tbody>
						<tr>
								<td>아이디 : </td>
								<td><input type="text" name="member_id"></td>
						</tr>
						<tr>
								<td>비밀번호 : </td>
								<td><input type="password" name="passwd"></td>
						</tr>
						<tr>
								<td>이름 : </td>
								<td><input type="text" name="name"></td>
						</tr>
						<tr>
								<td>이메일 : </td>
								<td><input type="text" name="email"></td>
						</tr>
						</tbody>
						</table>
				</form>
				
				<button type="button" onclick="memReg()">로그인</button>

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
      getAPI.get('/user/login/',)
        .then(response => {
          console.log(response)
          console.log('login API has recieved data')
          this.LoginData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
</script>

<style lang="scss">
@charset "utf-8";
@import "@/assets/scss/body.scss";
</style>

