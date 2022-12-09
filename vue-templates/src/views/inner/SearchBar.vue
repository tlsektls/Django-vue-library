<template>
  <div class="search d-block">
    <div class="btn-group">
      <div class="dropdown">
        <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
          도서명
        </a>

      <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
        <a class="dropdown-item" href="#">전체</a>
        <a class="dropdown-item" href="#">도서명</a>
        <a class="dropdown-item" href="#">저자</a>
        <a class="dropdown-item" href="#">출판사</a>
        </ul>
      </div>
    </div>
    <input type="search" >
    <button type="submit"><i class="xi-search"></i></button>
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    data () {
    },
    methods : {
    }
  }
</script>

<style scoped>

</style>

