<template>
<!-- 数据编辑和显示列表 未测试 -->
<div>
  <br>
  <el-row  type="flex" justify="end">
    <el-col :span="3">
    <el-button icon="el-icon-circle-plus" 
    @click.native.prevent="plusData()">添加数据</el-button></el-col>
  </el-row>
  <el-table
    :data="dataList"
    style="width: 100%" >
    <el-table-column
      fixed
      prop="problemId"
      label="数据编号"
      width="150">
    </el-table-column>
    <el-table-column
      prop="name"
      label="是否为例子"
      width="100">
    </el-table-column> 
    <el-table-column
      fixed="right"
      label="编辑数据"
      width="80">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-edit" circle
        @click.native.prevent="editData(scope.$index, dataList )" size="small"></el-button>
      </template>
    </el-table-column>   
    <el-table-column
      fixed="right"
      label="删除题目"
      width="80">
      <template slot-scope="scope">
        <el-button type="danger" icon="el-icon-delete" circle
        @click.native.prevent="deleteRow(scope.$index, dataList)" size="small"></el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
  export default {
  created(){
    this.init()
  },
    methods: {
    init(){
        let data ={
          problemId:this.$route.params.problemId
          }
          console.log(this.$route.params.problemId)
            axios({url:'http://8.129.147.77/showTestData/ ',//post这里写请求网址
            method:'post', //然后method改成get
            headers:{'Content-Type':'application/x-www-form-urlencoded'},
            data:Qs.stringify(data)
              }).then((res) => {
              console.log(res);
              if(res.data.code == '200'){
                console.log('成功')
              }
          })
    }, 
      deleteRow(index, rows) {
        rows.splice(index, 1);
        //返回post请求
      },
      editData(index,rows){
        this.$router.push("/dataPlus/" + rows[index].problemId); //跳转页面
      },
      plusData(){
        this.$router.push("/dataPlus/"+ '005'); //跳转页面
      }
    },
    data() {
      return {
        dataList: []
      }
    }
  }
</script>
<style>

</style>