<template>
  <div class="login">
    <div class="login-input">
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="ruleForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass">
          <el-input v-model="ruleForm.pass" type="password"></el-input>
        </el-form-item>
        <el-button @click="submitForm('ruleForm')">登录</el-button>
        <el-button>忘记密码</el-button>
      </el-form>
    </div>
  </div>
</template>

<script>
import {getLoginMultidata} from '../../network/user'

export default {
  data(){
    var checkname = (rule, value, callback) => {
      if(!value){
          return callback(new Error('用户名不能为空'));
      }else{
          callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if(value === ''){
        return callback(new Error('请输入密码'))
      }else {
        callback();
      }
    }
    return{
      ruleForm: {
        username: '',
        pass: ''
      },
      rules: {
        username: [
          {validator: checkname, trigger: 'blur'}
        ],
        pass: [
          {validator: validatePass, trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
        submitForm(formname){
            this.$refs[formname].validate((valid) => {
                if(valid){
                    console.log(this.ruleForm);
                    getLoginMultidata({
                        username: this.ruleForm.username,
                        password: this.ruleForm.pass,
                    }).then((res) => {
                      if(res['code']== 200){
                        localStorage.clear()            //清除
                        localStorage.setItem('info',1)  //保存
                        localStorage['flag'] = 1

                        sessionStorage.clear()
                        sessionStorage.setItem('username',JSON.stringify(res.username)) //转换为JSON数据
                        sessionStorage.setItem['token'] = JSON.stringify(res.token)

                        this.$message({
                          type: 'success',
                          message: '登录成功'
                        });
                        console.log(res);
                        this.$router.push('/problemList');
                      }
                    })
                }else{
                    alert('err');
                    return false;
                }
            });
        }
  }
}
</script>

<style>
.login{
  display: flex;
  justify-content: center;
  margin-top: 80px;
}
.login-input{
  width: 400px;
}
</style>
