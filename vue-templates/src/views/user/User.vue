<template>
  <div class="user">
    <Header></Header>

		<div>유저만 들어오는 페이지</div>

    <Footer></Footer>
	</div>
</template>

<script>
  import { getAPI } from '@/axios-api'
  import Header from '@/components/Header'
  import Footer from '@/components/Footer'

  export default {
    name: 'user',
    data () {
      return {
      }
    },
		components: {
      Header, 
      Footer,
    },
	}
</script>