<template class="help">
    <div class="help-container">
      <div class="help-btns">
        <el-button @click="router">修改个人信息</el-button>
        <el-button @click="logout">退出登录</el-button>
        <el-button @click="adminLogin">管理员登录</el-button>
      </div>
      <div class="help-content" id="content">
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm">
          <el-form-item label="用户名" prop="username" id="username">
            <el-input v-model="ruleForm.username"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pass" id="password">
            <el-input v-model="ruleForm.pass" type="password"></el-input>
          </el-form-item>
          <el-button @click="submitForm('ruleForm')">登录</el-button>
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
  // mounted(){
  //   this.getCookie();
  // },
  methods: {
        submitForm(formname){
            this.$refs[formname].validate((valid) => {
                if(valid){
                    console.log(this.ruleForm);
                    let data={//在data里面用键值对的形式写要写的参数
                        username: this.ruleForm.username,
                        password: this.ruleForm.pass,
                        isAdmin: 1
                     }
                     axios({url:'http://8.129.147.77/login/',//post这里写请求网址
                     method:'post', //然后method改成get
                    //  headers:{'Content-Type':"application/json;charset=UTF-8"},
                     headers:{'Content-Type':'application/x-www-form-urlencoded'},
                     data:Qs.stringify(data)
                        }).then((res) => {
                        console.log(res);
                        if(res.data.code == '200'){
                          var ses = window.localStorage;
                          var id = JSON.stringify(data.username);
                          var pass = JSON.stringify(data.password)
                          ses.setItem("username",id);
                          ses.setItem("password",pass);
                          this.$router.push('/problemAdd');
                        }else{
                          this.$message.error('用户名或密码错误。');
                        }
                    })
                }else{
                    alert('err');
                    return false;
                }
            });
        },

        // 退出登录
        logout(){
            window.localStorage.clear()
            this.$router.push('/login');
            },

        // 管理员登录
        adminLogin(){
              // var adminStyle = document.getElementsByClassName('help-content');
              // adminStyle.style.display = 'block';
              document.getElementById('content').style.display = 'flex';
        }
  },

}
</script>

<style>

.help-btns button{
  margin: 80px;
  width: 200px;
}
.help-content{
  display: none;
  justify-content: center;
}
</style>
//

