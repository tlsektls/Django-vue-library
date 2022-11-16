<template>
  <div class="posts">
    <Navbar></Navbar> 
      <div class="album py-5 bg-light">
        <h3>BOOKS</h3>
        <!--<div>{{APIData}}</div>-->
        <div class="container">
            <div class="row">
              <h3>Books</h3>
              <ul v-for="book in APIData" :key="book.id" class="col-md-4">
                <li>
                  <a :href="book">{{ book.title }}</a> ({{book.author}})
                  <span>{{ book.language }}</span> / 
                  <span>{{ book.genre[0].name }}</span>

                  <!--<p>{{ book.image }}</p>-->
                  <!--<p>{{ book.image.url }}</p>-->
                  <img :src="'http://127.0.0.1:8000' + book.image" :alt="book.title + '-image'" style="width:100px;">
                </li>
              </ul>

              <h3>BookInstance</h3>
              <ul v-for="bookInstance in DIData" :key="bookInstance.id" class="col-md-4">
                <li>{{ bookInstance }}</li>
              </ul>
            </div>


          </div>
      </div>
  </div>
</template>

<script>
  import { getAPI } from '../axios-api'
  import Navbar from '../components/Navbar'
  export default {
    name: 'Books',
    data () {
      return {
          APIData: [],
          DIData: [],
        }
    },
    components: {
      Navbar
    },
    created () {
        getAPI.get('/catalog/',)
          .then(response => {
            console.log(response)
            console.log('Post API has recieved data')
            this.APIData = response.data
            //console.log(response.data)
          })
          .catch(err => {
            console.log(err)
          });

        getAPI.get('/bookInstance/',)
          .then(response => {
            console.log(response)
            console.log('Post API has recieved data')
            this.DIData = response.data
            //console.log(response.data)
          })
          .catch(err => {
            console.log(err)
          })
    }
  }
</script>

<style scoped>

</style>

