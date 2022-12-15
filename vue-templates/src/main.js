import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

//import VueAwesomeSwiper from 'vue-awesome-swiper'

//import 'bootstrap/dist/css/bootstrap.min.css'
//import "bootstrap/dist/js/bootstrap.min.js"
//import 'bootstrap'


// font-awesome과 관련된 import를 정의
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus, faCalendar, faCircleUser, faUserPlus, faMagnifyingGlass, faChevronRight, faChevronLeft} from '@fortawesome/free-solid-svg-icons'
import { faLeanpub } from '@fortawesome/free-brands-svg-icons'
import { faCircleXmark } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(faPlus, faCalendar, faCircleUser, faUserPlus, faMagnifyingGlass, faChevronRight, faChevronLeft, faLeanpub, faCircleXmark)
// 위에 createApp을 통해 생성한 Vue Application 인스턴스의 component API 활용
const app = createApp(App);

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(store)
  .use(router)
  //.use(VueAwesomeSwiper)
  .mount('#app')


//createApp(App).use(store).use(router).mount('#app')

//App.config.productionTip = false

