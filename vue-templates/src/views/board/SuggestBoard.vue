<template>
  <div class="">
    <Header></Header>

    <h3>도서관 뉴스</h3>
		
    <!--<SearchBar></SearchBar>-->
  <div class="search d-block">
    <input type="search" v-model="boardSearch">
    <button type="submit"><i class="xi-search"></i></button>
  </div>

  {{checkData}}

    <table>
      <tr>
        <th>뉴스 제목</th>
        <th>뉴스 날짜</th>
      </tr>
      <tr v-for="news in newsData" :key="news">
        <td><router-link :to="{ name:'NewsInner', params:{id:news.id}}">{{ news.news_title }}</router-link></td>
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
  import { getAPI } from '@/axios-api'
  import Header from '@/components/Header'
  import Footer from '@/components/Footer'
  import SearchBar from '@/views/inner/SearchBar'
  import NewsList from '@/views/board/_News'

export default {
  name: 'Suggest-board',
  data () {
    return {
      newsData: [],
      paramsData: null,
      boardSearch: "",
      pageNum: 0,
      checkData: "",
    }
  },
  props: {
    pageSize: {
      type: Number,
      required: false,
      default: 5
    }
  },
	components: {
    Header,
    Footer,
    SearchBar,
    NewsList
  },
  created () {
    getAPI.get('/newsboard/')
      .then(response => {
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
    movePage(e) {
      this.pageNum = e;
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

			return this.newsData.filter((val) => {
        var searchVal = val.news_title.toUpperCase().indexOf(this.boardSearch.toUpperCase()) >= 0;
        return searchVal
      }).slice(start, end);
    }
    //boardSearch(val){},
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