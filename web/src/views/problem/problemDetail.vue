<template>
<!-- 具体题目描述 -->
  <div class="container">
      <!-- 标题 -->
    <el-row class="row-title">
      <el-row><h1>{{id}}. {{problemDetail.problemTitle}}</h1></el-row>
      <el-row type="flex">
        <el-col><span>时间限制：</span>{{problemDetail.timeLimit}} 秒</el-col>
        <el-col><span>空间限制：</span>{{problemDetail.memoryLimit}} MB</el-col>
      </el-row>
    </el-row>
        <!-- 内容 -->
    <el-row class="detail-content" type="flex">
        <!-- 题目描述 -->
      <el-col class="left-content">
        <el-row>
          <h3>题目描述</h3>
          <el-card>{{problemDetail.problemDescription}}</el-card>
        </el-row>
        <el-row>
          <h4>输入描述</h4>
          <el-card>{{problemDetail.inputDescription}}</el-card>
        </el-row>
        <el-row>
          <h4>输出描述</h4>
          <el-card>{{problemDetail.outputDescription}}</el-card>
        </el-row>
        <el-row>
          <h4>示例</h4>
          <el-card>
            <el-table
                ref="filterTable"
                :data="problemDetail.examples">
              <el-table-column
                  prop="explanation"
                  label="例子">
              </el-table-column>
              <el-table-column
                  prop="inputData"
                  label="输入数据">
              </el-table-column>
              <el-table-column
                  prop="outputData"
                  label="输出数据">
              </el-table-column>
            </el-table>
          </el-card>
        </el-row>
      </el-col>

        <!-- 代码提交 -->
      <el-col class="right-content">
        <el-row type="flex" justify="space-between">
          <el-autocomplete
              v-model="language"
              placeholder="请选择语言"
              :fetch-suggestions="querySearch"
              @select="handleSelect">
          </el-autocomplete>
          <el-button type="primary" @click="submitCode()">提交代码</el-button>
        </el-row>
        <el-cow>
          <el-input
              type="textarea"
              v-model="code"
              :autosize="{ minRows: 10}">
          </el-input>
        </el-cow>
      </el-col>
    </el-row>
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
          data:JSON.stringify(data),
            }).then((res) => {
            console.log(res);
            if(res.data.code == '200'){
              this.$router.push('/situation');//跳转到状态
            }else{
              alert('代码有误，请检查。');
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

<style scoped>
.container{
  width: 100%;
  display: flex;
  flex-direction: column;
}
.row-title{
  width: 100%;
  text-align: center;
  color: 	#708090;
}
.left-content{
  margin: 0 10px;
}
.right-content{
  display: flex;
  flex-direction: column;
  margin: 0 10px;
}
span{
  font-size: 18px;
  font-weight: bold;
}
h3{color:	#4682B4}
h4{color: 	#4682B4}
.el-card{color: #778899}
</style>
