import router from '@/router';
import axios from 'axios';
import { createStore } from 'vuex'

export default createStore({

  //import Vue from "vue";
  //import Vuex from "vuex";
  
  //Vue.use(Vuex);
  
  //export const store = new Vuex.Store({
    
  globalInjection: true,
  state: {
    userInfo: null,
    isLogin: false,
    isLoginError: false
  },
  getters: {
  },
  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
  },
  actions: {
    login(dispatch, loginObj) {
      console.log(loginObj)
      axios
      .post('http://127.0.0.1:8000/rest-auth/login/', loginObj)
      // loginObj = {email, password}
      .then(res => {
        // 접근 성공시, 토근 값이 반환된다. (실제로는 토근과 함께 유저 id를 받아온다.)
        // 토근을 헤더 정보에 포함시켜서 유저정보를 요청
        let token = res.data.token;

        localStorage.setItem('access_token', token);
        this.dispatch('getUserInfo');
        router.push({name: "home"});
        console.log(res);
      })
      .catch(() => {
        alert('이메일과 비밀번호를 확인하세요.');
      });
    },
    logout({ commit }) {
      router.push({ name: "home" });
    },
    signup(dispatch, loginObj) {
      axios
      .post('http://127.0.0.1:8000/rest-auth/signup/', loginObj)
      // loginObj = {email, password}
      .then(res => {
        alert('회원가입이 성공적으로 이뤄졌습니다.')
        router.push({name: "login"});
        console.log(res);
      })
      .catch(() => {
        alert('이메일과 비밀번호를 확인하세요.');
      });
    },
    logogetUserInfo({ commit }) {
      let token = localStorage.getItem("access_token");
      let config = {
        headers: {
          "access-token": token
        }
      };
      axios
      .post('http://127.0.0.1:8000/user/login/', config)
      // loginObj = {email, password}
      .then(response => {
        let userInfo = {
          pk: response.data.data.pk,
          username: response.data.data.username,
          email: response.data.data.email,
        }
        commit("loginSuccess", userInfo);
      })
      .catch(() => {
        alert('이메일과 비밀번호를 확인하세요.');
      });
    },
  },
  modules: {
  }
})
