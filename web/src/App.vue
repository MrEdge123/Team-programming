<template>
  <div id="#app" class="container">
    <!-- <div class="link-list">
      <router-link to="/home">主页</router-link>
      <router-link to="/problemList">题目列表</router-link>
      <router-link to="/situation">状态</router-link>
      <router-link to="/help">帮助</router-link>
      <router-link to="/login">登录</router-link>
      <router-link to="/register">注册</router-link>
    </div> -->
    <navBar></navBar>
    <!-- <el-main class="detailed-content"> -->
	    <router-view />
     <!-- </el-main> -->
  </div>
</template>

<script>
import navBar from './components/navBar'

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
/* *{
  padding: 0;
  margin: 0;
}

.link-list{
  height: 40px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: slateblue;
}

.link-list a{
  color: white;
  text-decoration: none;
  font-size: 20px;
} */
</style>
