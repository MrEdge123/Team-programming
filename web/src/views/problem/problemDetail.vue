<template>
<div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" ><div class="grid-content bg-purple-light">
      <h1>{{id}}：题目标题</h1>
      <h5> 时间限制: 1 秒 <span></span>空间限制: 512 MB</h5>
      </div></el-col>
</el-row>
<div style="margin: 60px 0;"></div>

<div><h3>题目描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
       <h4>这道题目非常简单！<br>你只需要计算a+b就可以了！！！</h4>
      </div></el-col>
</el-row>
<div><h3>输入描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
     <h4>输入两个整数a,b 1 = a = 100, 1 = b = 100</h4>
      </div></el-col>
</el-row>
<div><h3>输出描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h4>输出一行：输出a+b的值</h4>
      </div></el-col>
</el-row>
<div><h3>例子描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h4>输入</h4><h4>输出</h4><h4>说明</h4>
      </div></el-col>
</el-row>
<div style="margin: 60px 0;"></div>
<div>
<el-row>
  <el-col :span="3" ><div class="grid-content bg-purple-light"><h3>输入代码</h3></div></el-col>
</el-row>
  <div>
    <div></div>
    <el-input
    type="textarea"
    :autosize="{ minRows: 20, maxRows: 40}"
    placeholder="请输入内容"
    v-model="code">
  </el-input>
  </div>
</div>
<el-button >提交代码</el-button>
</div>

</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  created(){
  //  init(this.$route.params.problemId)
  },
data(){
    return{
       id:'',
       code: '',
       problemDetail:[],
    }
},
  mounted() {
    this.init();
  },
methods:{
    init(){
        const id= this.$route.params.problemId
          axios({url:'http://8.129.147.77/getDetails',//post这里写请求网址
          method:'get', //然后method改成get
          headers:{'Content-Type':"application/json;charset=UTF-8"},
          params:{id},
          withCredentials : true
          }).then(res=>{
              this.problemDetail = res.data.data;
              console.log(this.problemDetail)
            })
    },
     submitCode(){
            const code=this.code
            axios({url:'http://8.129.147.77/login/',//post这里写请求网址
            method:'post', //然后method改成get
            headers:{'Content-Type':'application/x-www-form-urlencoded'},
            data:Qs.stringify(code)
              }).then((res) => {
              console.log(res);
              if(res.data.code == '200'){
                // var ses = window.localStorage;
                // var id = JSON.stringify(data.username);
                // var pass = JSON.stringify(data.password)
                // ses.setItem("username",id);
                // ses.setItem("password",pass);
                this.$router.push({path:'/problemList',query:{code:200,msg:'登录成功'}});
              }else{
                alert('用户名或密码错误。');
              }
          })
     }
}
}
</script>

<style>

  .el-row {
  margin-bottom: 20px;
  }
  .el-row > last-child {
    margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 20px 0;
    background-color: #f9fafc;
  }
</style>