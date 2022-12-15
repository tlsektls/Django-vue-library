<template>
  <div class="">
    <table>
      <tr v-for="news in newsData" :key="news">
        <td><router-link :to="{ name:'NewsInner', params:{id:news.id}}">{{ news.news_title }}</router-link></td>
        <td>{{ news.news_date }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import { getAPI } from '@/axios-api'

export default {
  name: 'News-list',
  data () {
    return {
      newsData:[]
    }
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
  computed: {
    newsData () {
      const end = 5;
			return this.newsData.slice(0, 5);
    }
    //boardSearch(val){},
  }
}
</script>
