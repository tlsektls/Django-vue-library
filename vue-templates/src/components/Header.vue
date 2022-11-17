<template>
  <div class="header nav-bar">
    <nav class="navbar navbar-expand-lg">
      <div class="container">

        <a class="navbar-brand" href="#">
        <img src="@/assets/images/logo.png" width="" height="27" class="d-inline-block align-top" alt="" loading="lazy">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
            <router-link :to = "{ name:'index' }" exact>Posts</router-link>
            </li>
          </ul>
        </div>

      </div>
    </nav>
  </div>
</template>

<script>
  export default {
    name: 'Header',
  }
</script>

<style lang="scss">
@import "@/assets/scss/header.scss";
</style>