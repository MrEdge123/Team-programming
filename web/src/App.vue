<template>
  <div id="#app" class="container">
    <navBar></navBar>
	  <router-view />
  </div>
</template>

<script>
import navBar from './components/navbar'

export default {
  name: 'app',
  components: {
    navBar
  },
  method:{
  }
}
</script>
<style>
</style>
