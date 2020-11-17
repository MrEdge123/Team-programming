<template>
<!-- 学生的题目列表界面，还没有实现搜索功能-->
<el-card class="box-card">
  <div>
    <div class="search">
      <el-row :gutter="50">
        <el-col :span="8">
          <el-input placeholder="请输入题目编号">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="8">
          <el-input placeholder="请输入题目标题">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
      </el-row>
        </div>
      <div>
      <el-table
      :data="problemList"
      style="width: 100%"
      @row-click="detileTrans">
      <el-table-column
        prop="problemId"
        label="题目编号"
        width="300">
      </el-table-column>
      <el-table-column
        prop="problemTitle"
        label="题目标题">
      </el-table-column>
    </el-table>
      </div>
  </div>
</el-card>

</template>

<script>
import axios from 'axios'
// axios.defaults.withCredentials = true
import {getProblemListMultiData} from '../../network/problem'
export default {
  created(){
    // var username = localStorage.getItem('username');
    // var password = localStorage.getItem('password');
    this.init()
  },
  data() {
    return {
      inputId: '',
      inputTitle:'',
      problemList:[], //列表
    };
  },
  mounted() {
    // this.init();
  },
  methods: {
    init(){
          axios({url:'http://8.129.147.77/getproblemlist/',//post这里写请求网址
          method:'get', //然后method改成get
          headers:{'Content-Type':"application/json;charset=UTF-8"},
          withCredentials : true
          }).then(res=>{
              this.problemList = res.data.data;
              console.log(res);
            })
    },
    detileTrans(row) {
        this.$router.push("/problemDetail/" + row.problemId); //跳转页面
    },
    addProblem(){
      this.$router.push("/problemAdd");
    }

  },
};
</script>

<style>
template{
  background-color: #ccc;
}
.box-card{
  margin: 30px;
}

</style>
