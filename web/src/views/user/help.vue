<template class="help">
    <div class="help-btns">
      <el-button @click="router">修改个人信息</el-button>
      <el-button @click="logout">退出登录</el-button>
      <el-button @click="adminLogin">管理员登录</el-button>
    </div>
</template>

<script>
export default {
  methods: {
    logout(){
    window.localStorage.clear()
     this.$router.push('/login');
    },
    adminLogin(){
      // this.$router.push('/adminLogin');
    }
  }
}
</script>

<style>

.help-btns button{
  margin: 80px;
  width: 200px;
}
</style>
