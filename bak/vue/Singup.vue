<template>
 <div class="formContainer">
  <form class="login-box">
   <p>아이디</p>
   <input type="text" v-model="username" name="username" label="가입할 ID를 입력하세요" />
   <p>이메일</p>
   <input type="text" v-model="email" name="email" label="가입할 이메일을 입력하세요" />
   <p>비밀번호</p>
   <input type="password" v-model="password1" name="userpassword" label="비밀번호를 입력하세요" />
   <p>비밀번호 확인</p>
   <input type="password" v-model="password2" name="userpassword2" label="비밀번호 확인을 위해 다시 한번 입력하세요" />
   <br />
  </form>
  <div class="login-btn">
    <input
    type="submit"
    class="button"
    name="submit"
    @click="singup({username, email, password1, password2})"
    value="회원가입"
    />
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