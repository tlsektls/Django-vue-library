<template>
  <div class="news">
    <ol>
      <li v-for="news in NewsData" :key="news.id">
        <!--<a :href="news.id">{{ news.news_title }}</a>-->
        <!--<router-link v-bind:to="`/NewsBoard/News/${news.id}`">{{ news.news_title }}</router-link>-->
        <router-link :to="{ name: 'News', params: { title: news.news_title, id: news.id } }" :data-title="news.news_title">
          {{ news.news_title }}
        </router-link>
      </li>
    </ol>
  </div>
</template>

<script>
  import { getAPI } from '../../axios-api'
  export default {
    name: 'News',
    data () {
      return {
        NewsData: [],
      }
    },
    created () {
      getAPI.get('/newsboard/',)
        .then(response => {
          console.log(response)
          console.log('newsboard API has recieved data')
          this.NewsData = response.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
</script>

