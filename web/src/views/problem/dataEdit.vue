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
      prop="number"
      label="数据编号"
      width="150">
    </el-table-column>
    <el-table-column
      prop="isExample"
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
      label="删除数据"
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
          // console.log(this.$route.params.problemId)
            axios({url:'http://8.129.147.77/showTestData/ ',//数据请求有问题
            method:'post', //然后method改成get
            headers:{'Content-Type':'application/x-www-form-urlencoded'},
            data:Qs.stringify(data),
              }).then((res) => {
              if(res.data.code == '200'){
                this.dataList=res.data.data
                // console.log('成功')
                console.log(this.dataList)
              }
          })
    }, 
deleteRow(index, rows) {
        this.$confirm('请确保删除, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
        let data={//在data里面用键值对的形式写要写的参数
        problemId:this.id,
        number: rows[index].number,//数据的号码
        isExample:rows[index].isExample
                }
        console.log(data)
          axios({url:'http://8.129.147.77/deleteTestData/',// 好像没有界面
          method:'post', //然后method改成get
        //  headers:{'Content-Type':"application/json;charset=UTF-8"},
          headers:{'Content-Type':'application/x-www-form-urlencoded'},
          data:JSON.stringify(data)
            }).then((res) => {
            // console.log(res)
            if(res.data.code == '200'){
              rows.splice(index, 1);
              this.$message({
              type: 'success',
              message: '删除成功!'
            });
            }else{
              alert('出现错误');
            }
        })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消'
          });
        });
     },
      editData(index,rows){
        this.$router.push("/dataPlus/"+this.id+"/"+rows[index].number); //跳转页面如果传入题目序号
      },
      plusData(){
        this.$router.push("/dataPlus/"+this.id+"/new"); //跳转页面如果传入题目序号
      }
    },
    data() {
      return {
        id:this.$route.params.problemId,
        dataList: []
      }
    }
  }
</script>
<style>

</style>