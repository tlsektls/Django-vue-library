import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import Index from '../views/Index'
import Books from '../views/books/Books'
import BookInner from '../views/books/_BookInner'
import Author from '../views/books/Author'
import NewsBoard from '../views/board/NewsBoard'
import NewsInner from '../views/board/_NewsInner'
import Login from '../views/login/Login'
import Singup from '../views/login/Singup'
import Join from '../views/login/Join'
import User from '../views/user/User'

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
    path: '/Books/book',
    name: 'BookInner',
    component: BookInner
  },
  {
    path: '/Author/:id',
    name: 'Author',
    props: true,
    component: Author
  },
  {
    path: '/NewsBoard',
    name: 'NewsBoard',
    component: NewsBoard
  },
  {
    path: '/NewsBoard/news/:id',
    name: 'NewsInner',
    props: true,
    component: NewsInner
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Singup',
    name: 'Singup',
    component: Singup
  },
  {
    path: '/Join',
    name: 'Join',
    component: Join
  },
  {
    path: '/User',
    name: 'User',
    component: User,
    auth: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(function (to, from, next) {
  const refresh = localStorage.getItem("refresh")
  console.log('beforeEach' + to.path + refresh)
  if((to.path == '/user' || to.path == '/User') && refresh == '') {
    next({ path: '/Login' })
  } else {
    next()
  }
})


export default router
