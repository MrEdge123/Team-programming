<template>
<div>
    <div class="search">
      <el-row :gutter="20">
        <el-col :span="4"><div class="grid-content bg-purple">
              <span style="center">题目编号：</span>
              </div>
        </el-col>
        <el-col :span="6"><div class="grid-content bg-purple">
            <el-form>
              <el-form-item class="petname">
                <el-input v-model="inputId" placeholder="输入题目编号"></el-input> </el-form-item>
                </el-form></div>
        </el-col>
        <el-col :span="4"><div class="grid-content bg-purple">
              <span style="center">题目标题：</span>
              </div>
        </el-col>
        <el-col :span="6"
          ><div class="grid-content bg-purple">
            <el-form>
              <el-form-item class="petname">
                <el-input v-model="inputTitle" placeholder="输入题目标题"></el-input> </el-form-item
            ></el-form></div
        ></el-col>
        <el-col :span="2"><div class="grid-content bg-purple">
            <el-button type="primary" icon="el-icon-search" @click="addProblem()">搜索</el-button>
            <!-- <el-button >搜索</el-button> -->
            <!-- 没有实现搜索的功能-->
          </div></el-col>
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

</template>

<script>
import axios from 'axios'
axios.defaults.withCredentials = true
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
          axios({url:'http://8.129.147.77/getproblemlist',//post这里写请求网址
          method:'get', //然后method改成get
          headers:{'Content-Type':"application/json;charset=UTF-8"},
          withCredentials : true
          }).then(res=>{
              this.problemList = res.data.data;
              console.log(this.problemList)
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
.search {
  margin: 10px 0px;
  padding:0px 10px;
  display: flex;
}
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
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
