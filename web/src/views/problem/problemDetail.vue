<template>
<!-- -->
<div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" ><div class="grid-content bg-purple-light">
      <h1>{{id}}：{{problemDetail.problemTitle}}</h1>
      <h5> 时间限制: {{problemDetail.timeLimit}} 秒 <span></span>空间限制: {{problemDetail.memoryLimit}} MB</h5>
      </div></el-col>
</el-row>
<div style="margin: 60px 0;"></div>

<div><h3>题目描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
       <h4>{{problemDetail.problemDescription}}</h4>
      </div></el-col>
</el-row>
<div><h3>输入描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
     <h4>{{problemDetail.inputDescription}}</h4>
      </div></el-col>
</el-row>
<div><h3>输出描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h4>{{problemDetail.outputDescription}}</h4>
      </div></el-col>
</el-row>
<div><h3>例子描述：</h3></div>
<el-row type="flex" class="row-bg">
 <el-table
    ref="filterTable"
    :data="problemDetail.examples"
    style="width: 100%">
    <el-table-column
      prop="explanation"
      label="例子"
      width="180">
    </el-table-column>
    <el-table-column
      prop="inputData"
      label="输入数据"
      width="180">
    </el-table-column>
    <el-table-column
      prop="outputData"
      label="输出结果"
      width="180">
    </el-table-column>

  </el-table>
</el-row>
<div style="margin: 60px 0;"></div>
<div>
<el-row>
  <el-col :span="3" ><div class="grid-content bg-purple-light"><h3>输入代码</h3></div></el-col>
</el-row>
<el-row>
  <el-col :span="3"><div class="grid-content bg-purple-light">
    <div class="sub-title"><h3>选择语言</h3></div></div>
    </el-col>
    <el-col :span="6">
    <el-autocomplete
      class="inline-input"
      v-model="language"
      :fetch-suggestions="querySearch"
      placeholder="请输入内容"
      @select="handleSelect"
    ></el-autocomplete>

  </el-col>
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
<el-button @click="submitCode()" >提交代码</el-button>
</div>

</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  created(){
   this.init(this.$route.params.problemId)
  },
data(){
    return{
       id:this.$route.params.problemId,
       code: '',
       problemDetail:[],
       restaurants: [],
      language: '',
    }
},
  mounted() {
    //  this.id = this.$router.params.problemId;
    // this.init(this.id);
    this.restaurants = this.loadAll();
  },
methods:{
    init(id){
          // this.id = this.$route.params.problemId;
          console.log(id)
          axios({url:'http://8.129.147.77/getDetails/',//post这里写请求网址
          method:'get', //然后method改成get
          headers:{'Content-Type':"application/json;charset=UTF-8"},
          params:{problemId:id},
          withCredentials : true
          }).then(res=>{
              this.problemDetail = res.data.data;
              console.log(res);
            })
    },
     submitCode(){
          var  storage = window.localStorage;
          var username = storage.getItem('username');
          let data ={
            // userName:username,
            problemId:this.id,
            code:this.code,
            language:this.language,
            }
          console.log(data)
          axios({url:'http://8.129.147.77/submitCode/ ',//post这里写请求网址
          method:'post', //然后method改成get
          headers:{'Content-Type':'application/x-www-form-urlencoded'},
          data:Qs.stringify(data)
            }).then((res) => {
            console.log(res);
            if(res.data.code == '200'){
              this.$router.push('/situation');//跳转到状态
            }else{
              alert('用户名或密码错误。');
            }
          })
     },
     querySearch(queryString, cb) {
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
        // 调用 callback 返回建议列表的数据
        cb(results);
      },
      createFilter(queryString) {
        return (restaurant) => {
          return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadAll() {
        return [
          { "value": "C", "address": "1" },
          { "value": "C++", "address": "2" },
         { "value": "Python3", "address": "3" },
        ];
      },
       handleSelect(item) {
         console.log(this.language);
        console.log(item);
      }
    },

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
