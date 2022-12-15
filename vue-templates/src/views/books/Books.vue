<template>
<div class="">
  <Header></Header> 

  <div class="content"><div class="container"> 
    <h3>도서 리스트</h3>
		
    <!--<SearchBar></SearchBar>-->
    <!--<div class="search d-block">
      <input type="search" v-model="boardSearch">
      <button type="submit"><i class="xi-search"></i></button>
    </div>-->

    <div class="search">
      <div class="d-flex search-bar">
        <div class="btn-group">
          <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" :value="this.searchCategory.value" >
            {{this.searchCategory.text}}
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
            <li><a class="dropdown-item" href="#" @click="selCategory($event)" value="title">제목</a></li>
            <li><a class="dropdown-item" href="#" @click="selCategory($event)" value="author">저자</a></li>
            <li><a class="dropdown-item" href="#" @click="selCategory($event)" value="publisher">출판사</a></li>
          </ul>
        </div>
      <input type="search" v-model="bookSearch">
      <button type="submit" class="normal"><font-awesome-icon icon="fa-solid fa-magnifying-glass" /></button>
      </div>

      <div class="gerne-sel">
        <div class="d-inline">장르: </div>

        <div class="btn-group d-inline">
          <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            장르 선택
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
            <li v-for="gerne in gerneData" :key="gerne">
              <button class="dropdown-item" :id="gerne.id" @click="selectG($event)" :value=gerne.name>
                {{gerne.name}}
              </button>
            </li>
          </ul>
        </div>

        <ul class="gerne-selected d-flex" ref="sek_G">
          <li v-for="sekG in selectedG" :key="sekG" class="sel">
            <span class="gerne">{{sekG.gerne}}</span>
            <button v-on:click="deletG(sekG)" class="normal">
              <font-awesome-icon icon="fa-regular fa-circle-xmark" />
            </button>
          </li>
          
        </ul>
      </div>
    </div>


  <div class="book-list">
    <div class="book-card" v-for="book in bookData" :key="book">

      <div class="d-flex">
        <div class="img-wrap">
          <img :src="'http://127.0.0.1:8000'+book.image" alt="book-img">
        </div>
        <div class="book-info">
          <div class="d-flex justify-content-between">
            <div class="book-title">{{book.title}}</div>
            <div class="book-loan">
              <font-awesome-icon icon="fa-brands fa-leanpub" />
              일단은 대출가능</div>
          </div>
          <div class="d-flex info-detail">
            <div class="book-author">  
              <span class="type">저자: </span>
              <span v-for="(thisAuthor,index) in book.author" :key="thisAuthor">
                <router-link :to="{ name:'Author', params:{id:thisAuthor.id}}">{{thisAuthor.name}}</router-link>
                <span v-if="index < book.author.length-1">, </span>
              </span>
            </div>
            <div class="book-publisher">
              <span class="type">퍼블리셔: </span>{{book.publisher}}
              </div>
            <div class="book-genre">
              <span class="type">장르: </span>
              <span v-for="(thisGenre,index) in book.genre" :key="thisGenre">
                {{thisGenre.name}}<span v-if="index < book.genre.length-1">, </span>
              </span>
            </div>
          </div>
          <div class="book-summary">{{book.summary}}</div>
          <button class="normal ml-auto innerBook">자세히 보기</button>
        </div>
      </div>

      <!--<bookInnerModal></bookInnerModal>-->
      
      <!--<router-link :to="{ name:'BookInner', params:{id:book.id}}">{{ book.title }}</router-link>-->
    </div>
  </div>

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

    </div></div>

    <Footer></Footer>
</div>
</template>

<script>
  import { getAPI } from '@/axios-api'
  import Header from '@/components/Header'
  import Footer from '@/components/Footer'
  import SearchBar from '@/views/inner/SearchBar'

export default {
  name: 'News-list',
  data () {
    return {
      bookData: [],
      gerneData: [],
      bookSearch: "",
      searchCategory: {text: '제목', value: 'title'},
      pageNum: 0,
      selectedG: [],
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
    SearchBar
  },
  created () {
    getAPI.get('/books/')
      .then(response => {
        this.bookData = response.data
        console.log(this.bookData)
      })
      .catch(err => {
        console.log(err)
      })
    getAPI.get('/genre/')
      .then(response => {
        this.gerneData = response.data
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
    },

    selectG(event) {
      const value = event.currentTarget.value
      const inner = {'gerne': value}

      this.selectedG.push(inner)
    },
    deletG(item) {
      for(let i = 0; i < this.selectedG.length; i++) {
        if(this.selectedG[i] === item)  {
          this.selectedG.splice(i, 1);
          i--;
        }
      }
    },
    selCategory(event) {
      this.searchCategory.text = event.target.text
      this.searchCategory.value = event.srcElement.attributes.value.value
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.bookData.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      page = Math.floor((listLeng - 1) / listSize) + 1
      return page;
    },
    bookData () {
      const start = this.pageNum * this.pageSize,
        end = start + this.pageSize;

			return this.bookData.filter((val) => {
        if(this.searchCategory.value == "title") {
          var searchVal = val.title.toUpperCase().indexOf(this.bookSearch.toUpperCase()) >= 0;
          return searchVal

        } else if(this.searchCategory.value == "author") {
          // 나중에 다시. 저자 2번째부터 잘 못 읽음
          for(let i=0; i<val.author.length; i++) {
            console.log(val.author[i].name.toUpperCase().indexOf(this.bookSearch.toUpperCase()))

            var searchVal = val.author[i].name.toUpperCase().indexOf(this.bookSearch.toUpperCase()) >= 0;

            return searchVal
          }
          console.log(searchVal)

        } else if(this.searchCategory.value == "publisher") {
          var searchVal = val.publisher.toUpperCase().indexOf(this.bookSearch.toUpperCase()) >= 0;
          return searchVal
        }
      }).slice(start, end);
    },
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