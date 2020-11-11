<template>
  <div id="#app" class="container">
    <div class="link-list">
      <router-link to="/home">主页</router-link>
      <router-link to="/problemList">题目列表</router-link>
      <router-link to="/situation">状态</router-link>
      <router-link to="/help">帮助</router-link>
      <router-link to="/signIn">登录</router-link>
      <router-link to="/login">注册</router-link>
    </div>
    <router-view/>
    <!-- <router-link to="/foot">页脚</router-link> -->
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
   
  }
}
</script>

<style>
*{
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
}
</style>
