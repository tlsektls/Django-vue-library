<template>
  <div class="">
    <Header></Header> 
		
    <table>
      <tr>
        <th>뉴스 제목</th>
        <th>뉴스 날짜</th>
      </tr>
      <tr v-for="news in newsData" :key="news">
        <td>{{ news.news_title }}</td>
        <td>{{ news.news_date }}</td>
      </tr>
    </table>
		
    <div class="btn-cover">
      <button v-if="pageNum === 0 ?false:true" @click="prevPage" class="page-btn">
        이전
      </button>

      <button v-if="pageNum < 2 ?false:true" @click="movePage(pageNum-2)" class="page-btn">
        {{ pageNum -1 }}
      </button>
      <button v-if="pageNum < 1 ?false:true" @click="movePage(pageNum-1)" class="page-btn">
        {{ pageNum }}
      </button>
      <button @click="prevPage" class="page-btn active">
        {{ pageNum +1 }}
      </button>
      <button v-if="pageNum >= pageCount - 1 ?false:true" @click="movePage(pageNum+1)" class="page-btn">
        {{ pageNum +2 }}
      </button>
      <button v-if="pageNum >= pageCount - 2 ?false:true" @click="movePage(pageNum+2)" class="page-btn">
        {{ pageNum +3 }}
      </button>

      <!--<span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>-->
      <button v-if="pageNum >= pageCount - 1 ?false:true" @click="nextPage" class="page-btn">
        다음
      </button>
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
  import { getAPI } from '../../axios-api'
  import Header from '../../components/Header'
  import Footer from '../../components/Footer'

export default {
  name: 'News-list',
  data () {
    return {
      newsData: [],
      paramsData: null,
      pageNum: 0
    }
  },
  props: {
    //listArray: {
    //  type: Array,
    //  required: true
    //},
    pageSize: {
      type: Number,
      required: false,
      default: 5
    }
  },
	components: {
    Header,
    Footer
  },
  created () {
    getAPI.get('/newsboard/')
      .then(response => {
        console.log(response)
        console.log('newsboard API has recieved data')
        this.newsData = response.data
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.newsData.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      page = Math.floor((listLeng - 1) / listSize) + 1
      return page;
    },
    newsData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.newsData.slice(start, end);
    }
  }
}
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}
table th {
  font-size: 1.2rem;
}
table tr {
  height: 2rem;
  text-align: center;
  border-bottom: 1px solid #505050;
}
table tr:first-of-type {
  border-top: 2px solid #404040;
}
table tr td {
  padding: 1rem 0;
  font-size: 1.1rem;
}
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
</style>