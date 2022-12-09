<template>
  <div class="NoticeBoard">
    <Header></Header> 
		
      <div class="content"><div class="container author">        
				<h3>{{this.authorData.name}}</h3>

        <div class="author-life">
          <span>{{this.authorData.date_of_birth}}</span>
          <span v-if="authorData.date_of_birth != Null"> ~ </span>
          <span>{{this.authorData.date_of_death}}</span>
        </div>
				<div class="author-intro">{{this.authorData.intro}}</div>
	

        <div class="author-book">
          <div v-for="book in bookData" :key="book" >
            <img :src="'http://127.0.0.1:8000'+book.image">
            {{book.title}}
            <!--<router-link :to="{ name:'book', params:{id:book.id}}">{{book.title}}</router-link>-->
          </div>
        </div>

      </div></div>

    <Footer></Footer>
  </div>
</template>

<script>
  import { getAPI } from '@/axios-api'
  import { useRoute } from 'vue-router'
  import Header from '@/components/Header'
  import Footer from '@/components/Footer'
  export default {
    name: 'Author',
    data () {
      return {
        authorData: [],
        bookData: [],
      }
    },
    components: {
      Header,
      Footer,
    },
    methods : {
    },
    mounted() {
      console.log(this.$route)
    },
    created () {
      const route = useRoute();
      const id = route.params.id;

      getAPI.get(`/author/${id}/`)
        .then(response => {
          console.log('Author API has recieved data')
          this.authorData = response.data

          getAPI.get(`/bookSuggest/?author=${this.authorData.name}`)
            .then(response => {
              console.log('suggest-book API has recieved data')
              this.bookData = response.data
            })
            .catch(err => {console.log(err)})
        })
        .catch(err => {
          console.log(err)
        })

      
    },
  }
</script>

<style scoped>

</style>

book = Book.objects.filter(title="asd")
auth = Book.objects.filter(auth__name="test")