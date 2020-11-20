<template>
  <div class="login">
    <div class="login-input">
      <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm">
        <el-form-item label="用户名" prop="username" id="username">
          <el-input v-model="ruleForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="pass" id="password">
          <el-input v-model="ruleForm.pass" type="password"></el-input>
        </el-form-item>
        <el-form-item>
        <!-- `checked` 为 true 或 false -->
        <el-checkbox v-model="checked">老师 / 管理员</el-checkbox>
        </el-form-item>
        <el-button @click="submitForm('ruleForm')">登录</el-button>
        <el-button @click="forgetPassword()">忘记密码</el-button>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'

export default {
  name:'login',
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
      checked: false,
      ruleForm: {
        username: '',
        pass: '',
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
  // mounted(){
  //   this.getCookie();
  // },
  methods: {
        submitForm(formname){
            this.$refs[formname].validate((valid) => {
                if(valid){
                  var isadmin=0
                  if(this.checked){isadmin=1}
                    // console.log(isadmin);
                    let data={//在data里面用键值对的形式写要写的参数
                        username: this.ruleForm.username,
                        password: this.ruleForm.pass,
                        isAdmin: isadmin
                     }
                     axios({url:'http://8.129.147.77/login/',//post这里写请求网址
                     method:'post', //然后method改成get
                    //  headers:{'Content-Type':"application/json;charset=UTF-8"},
                     headers:{'Content-Type':'application/x-www-form-urlencoded'},
                     data:Qs.stringify(data)
                        }).then((res) => {
                        console.log(res);
                        if(res.data.code == '200'){
                          if(!isadmin){this.$router.push('/home');}
                          else{this.$router.push('/problemAdd');}
                          var ses = window.localStorage;
                          var id = JSON.stringify(data.username);
                          var pass = JSON.stringify(data.password);
                          var isadmin = JSON.stringify(data.isAdmin)
                          ses.setItem("username",id);
                          ses.setItem("password",pass);
                          ses.setItem("isAdmin",isadmin);
                        }else{
                          this.$message.error('用户名或密码错误。');
                        }
                    })
                }else{
                    alert('err');
                    return false;
                }
            });
        }
  },
    // 忘记密码
  forgetPassword(){
    this.$router.push('/forgetPass');
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
