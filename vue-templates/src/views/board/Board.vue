<template>
  <div class="NoticeBoard">
    <Header></Header> 
		
        <h3>inner</h3>
				
        <div class="container">

					<h1> id: {{ this.$route.params.id }}  </h1>

					<h3>{{ this.$route.params }}</h3>
					<p>{{ this.$route.params.news_title }}</p>


      	</div>

    <Footer></Footer>
  </div>
</template>

<script>
  import Header from '../../components/Header'
  import Footer from '../../components/Footer'
  export default {
    name: 'Board',
    data () {
    },
    components: {
      Header,
      Footer
    },
    methods : {
    }
  }
</script>

<style scoped>

</style>

