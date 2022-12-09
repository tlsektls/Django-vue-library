import router from '@/router';
import axios from 'axios';
import { createStore } from 'vuex'

export default createStore({
  
  globalInjection: true,
  state: {
    access: '',
    refresh: '',
  },
  getters: {
  },
  mutations: {
    initializerStore(state) {
      if (localStorage.getItem('access')) {
        state.access = localStorage.getItem('access')
        state.refresh = localStorage.getItem('refresh')
      } else {
        state.access = ''
        state.refresh = ''
      }
    },
    setAccess(state, access) {
      state.access = access
    },
    setRefresh(state, refresh) {
      state.refresh = refresh
    },
    removeToken(state) {
      state.access = ''
      state.refresh = ''
    },
  },
  actions: {
  },
  modules: {
  }
})
