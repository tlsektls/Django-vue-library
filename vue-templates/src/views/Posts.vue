<template>
  <div class="posts">
    <Navbar></Navbar> 
      <div class="album py-5 bg-light">
        <h3>BOOKS</h3>
        <!--<div>{{APIData}}</div>-->
        <div class="container">
            <div class="row">
              <ul v-for="book in APIData" :key="book.id" class="col-md-4">
                <li>
                  <a href="{{ book.get_absolute_url }}">{{ book.title }}</a> ({{book.author}})
                </li>
              </ul>
            </div>


            <!--<h2>book</h2>
              {% if book_list %}
              <ul>
                {% for book in book_list %}
                  <li>
                    <a href="{{ book.get_absolute_url }}">{{ book.title }}</a> ({{book.author}})
                  </li>
                {% endfor %}
              </ul>
            {% else %}-->

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
          APIData: []
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
          })
    }
  }
</script>

<style scoped>

</style>

