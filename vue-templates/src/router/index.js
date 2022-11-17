import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import Index from '../views/Index'
import Books from '../views/Books'
import NewsBoard from '../views/NewsBoard'
import News from '../views/inner/News'
import Login from '../views/login/Login'

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/Books',
    name: 'Books',
    component: Books
  },
  {
    path: '/NewsBoard',
    name: 'NewsBoard',
    component: NewsBoard
  },
  {
    path: '/NewsBoard/news/:id',
    name: 'News',
    component: News
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
