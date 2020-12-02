<template class="help">
    <div class="help-container">
      <div class="help-btns">
        <el-button>修改个人信息</el-button>
      </div>
      <el-form :model="infoForm" :rules="rules" ref="infoForm">
        <el-form-item label="用户名" prop="username">
          <el-input type="text" v-model="infoForm.username" ref="username"></el-input>
        </el-form-item>
        <el-form-item label="昵称" prop="nickname">
          <el-input type="text" v-model="infoForm.nickname" ref="nickname"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input type="text" v-model="infoForm.email" ref="email"></el-input>
        </el-form-item>
      </el-form>
      <el-button @click="submitForm('infoForm')">修改</el-button>
      <!-- <Code></Code> -->
    </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
// import Code from '../../components/Code'

export default {
  components: {
    // Code
  },
  data() {
    var checkname = (rule,value,callback) => {
      if(!value){
        return callback(new Error('用户名不能为空'));
      } else {
        callback();
      }
    };
    var checkEmail = (rule,value,callback) => {
      var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
      if(!value){
        return callback(new Error('邮箱不能为空'));
      }
      setTimeout(() => {
        if(!reg.test(value)){
          callback(new Error('请输入正确的邮箱。'));
        } else {
          callback();
        }
      },1000);
    };
    return {
        infoForm: {
          username: '',
          nickname: '',
          email: '',
      },
      rules: {
        username: [
          {validator: checkname, trigger: 'blur'}
        ],
        email: [
          {validator: checkEmail, trigger: 'blur'}
        ]
      }
    }
  },

  methods: {
    submitForm(formname){
      this.$refs[formname].validate((valid) => {
        if(valid){
          console.log(this.infoForm);
          let data = {
            username: this.infoForm.username,
            nickname: this.infoForm.nickname,
            email: this.infoForm.email
          }
          axios({url: 'http://8.129.147.77/modify/',
            method: 'post',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            data: Qs.stringify(data)
            }).then((res) => {
              console.log(res.data);
              // if(res.data.code === 200){
                // this.infoForm = res.data.data;
                console.log(res.data);
                window.localStorage.setItem('username',JSON.stringify(this.infoForm.username));
                this.$router.go(0);
              // }
            }).catch((error) => {
              console.log(error);
            })
        }
      })
    }
  }

}
</script>

<style scoped>
.help-container{
  margin: 80px;
}
.el-form{
  display: flex;
  flex-direction: column;
}
.el-form-item{
  width: 250px;
}
</style>


