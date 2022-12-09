<template>
 <div class="formContainer">
  <form class="login-box">
   <p>아이디</p>
   <input type="text" v-model="username" name="username" label="ID를 입력하세요" />
   <p>비밀번호</p>
   <input type="password" v-model="password" name="userpassword" label="비밀번호를 입력하세요" />
   <br />
  </form>
 <div class="login-btn">
  <input
   type="submit"
   class="button"
   name="submit"
   @click="login({username, password})"
   value="로그인"
  />
 <div class="login-btn-txt">
  <a>아이디/비밀번호 찾기 |</a>
  <a class="bold">
  <router-link :to="{ name: 'signup' }">&nbsp;&nbsp;회원가입</router-link>
  </a>
 </div>
 </div>
 </div>
</template>

<script>
import {mapState, mapActions} from 'vuex';

export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>