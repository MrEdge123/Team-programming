<template>
  <div id="login" class="login-input">
      <el-form>
          <el-form-item class="username">
              <el-input placeholder="用户名"></el-input>
          </el-form-item>
          <el-form-item class="petname">
              <el-input placeholder="昵称"></el-input>
          </el-form-item>
          <el-form-item class="password">
              <el-input placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item class="confirm">
              <el-input placeholder="确认密码"></el-input>
          </el-form-item>
          <el-form-item class="email">
              <el-input placeholder="邮箱"></el-input>
          </el-form-item>
          <el-button>登录</el-button>
      </el-form>
  </div>
</template>

<script>
export default {
    data(){
        
    }
}
</script>

<style> 
.login-input{
    width: 400px;
}


</style>