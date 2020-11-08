<template>
  <div class="body">
    <div class="left">
      <img src="../assets/logo.png" width="50px"/>
      <span style="color:white;margin-left:15px;" @click="checkClickhome">主页</span>
      <span style="color:white;margin-left:15px;" @click="checkClickhome">题目列表</span>
      <span style="color:white;margin-left:15px;">状态</span>
      <span style="color:white;margin-left:15px;">帮助</span>
      <span style="color:white;margin-left:15px;">退出登录</span>
    </div>
    <div class="right">
    <span style="color:white;margin-right:10px;">用户</span>
    <a href="https://www.baidu.com">
      <img src="../assets/me.png" class="img"/>
    </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'v-header',
  props: {
    msg: String
  },
  methods: {
    checkClickhome(){
        this.$router.push({
          path:'/'//跳转主页面
        })   
    }
  }

}
</script>

<style scoped>
  .body{
    width:100%;
    height:70px; 
    background-color:#333;
    display:flex;
    justify-content:space-between;
    align-items:center;
  }
  .img{
    width:50px;
    height:50px;
    display:inline-block;
    border-radius:50%;
  }
  .left,.right{
    display:flex;
    align-items:center;
    margin:auto 20px;
  }
</style>
