<template>
<div>
  <br>
  <el-row  type="flex" justify="end">
    <el-col :span="3">
    <el-button icon="el-icon-circle-plus" 
    @click.native.prevent="plusProblem()">新建题目</el-button></el-col>
  </el-row>
  <el-table
    :data="problemList"
    style="width: 100%" >
    <el-table-column
      fixed
      prop="problemId"
      label="题目编号"
      width="150">
    </el-table-column>
    <el-table-column
      prop="problemTitle"
      label="题目标题"
      width="300">
    </el-table-column> 
    <el-table-column
      fixed="right"
      label="编辑题目"
      width="80">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-edit" circle
         @click.native.prevent="editProblem(scope.$index, problemList)" size="small"></el-button>
      </template>
    </el-table-column>
    <el-table-column
      fixed="right"
      label="编辑数据"
      width="80">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-edit" circle
        @click.native.prevent="editData(scope.$index, problemList )" size="small"></el-button>
      </template>
    </el-table-column>   
    <el-table-column
      fixed="right"
      label="删除题目"
      width="80">
      <template slot-scope="scope">
        <el-button type="danger" icon="el-icon-delete" circle
        @click.native.prevent="deleteRow(scope.$index, problemList)" size="small"></el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>

<script>
import axios from 'axios'
axios.defaults.withCredentials = true
  export default {
    created(){
    this.init()
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
      deleteRow(index, rows) {
        rows.splice(index, 1);
      },
      editProblem(index,rows){
      this.$router.push("/problemEdit/" + rows[index].problemId); //跳转页面
      },
      editData(index,rows){
        this.$router.push("/dataEdit/" + rows[index].problemId); //跳转页面
      },
      plusProblem(){
        this.$router.push("/problemPlus" ); //跳转页面
      }
    },
    data() {
      return {
        problemList: [],
      }
    }
  }
</script>
<style>

</style>