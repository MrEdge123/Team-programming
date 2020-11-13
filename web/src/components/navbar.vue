<template>
  <div class="container">
    <div class="navbar-list">
      <el-menu>
        <el-menu-item>主页</el-menu-item>
        <el-menu-item>题目列表</el-menu-item>
        <el-menu-item>状态</el-menu-item>
        <el-menu-item>帮助</el-menu-item>
        <el-menu-item>登录</el-menu-item>
        <el-menu-item>注册</el-menu-item>
      </el-menu>
    </div>
  </div>
</template>

<script>


export default {
//   name: 'navbar',
//   components: {

//   }
}
</script>

<style>
*{
  padding: 0;
  margin: 0;
}

.navbar-list{
  height: 40px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: slateblue;
}

.navbar a{
  color: white;
  text-decoration: none;
  font-size: 20px;
}
</style>
