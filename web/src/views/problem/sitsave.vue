<template>
  <el-card>
    <!-- 顶部搜索区域 -->
    <div class="search">
      <el-row :gutter="50">
        <el-col :span="5">
          <el-input placeholder="请输入用户名" v-model="search">
            <el-button slot="append" icon="el-icon-search" @click="searchBtn()"></el-button>
          </el-input>
        </el-col>
        <el-col :span="5">
          <el-input placeholder="请输入题目编号">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
        <el-col :span="5">
          <el-input placeholder="请输入运行结果">
            <el-button slot="append" icon="el-icon-search"></el-button>
          </el-input>
        </el-col>
      </el-row>
    </div>

     <!-- 题目提交状态 -->
      <el-table :data="tableData" border stripe>
        <el-table-column type="index" label="序号"></el-table-column>
        <el-table-column label="用户名" prop="userName"></el-table-column>
        <el-table-column label="题目编号" prop="problemId"></el-table-column>
        <el-table-column label="运行结果" prop="judgeResult"></el-table-column>
        <el-table-column label="消耗内存" prop="usedMemory"></el-table-column>
        <el-table-column label="运行时间" prop="usedTime"></el-table-column>
        <el-table-column label="使用语言" prop="language"></el-table-column>
        <el-table-column label="提交时间" prop="submitTime"></el-table-column>
      </el-table>
  </el-card>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  created(){
    this.init()
  },
  data() {
      return {
        tableData:[],
        search: '',
        searchData: ''
      }
    },
    methods: {
      init(){
          axios({url:'http://8.129.147.77/getState/',//post这里写请求网址
          method:'get', //然后method改成get
          headers:{'Content-Type':"application/json;charset=UTF-8"},
          withCredentials : true
          }).then((res)=>{
              this.statue = res.data.data;
              // console.log(res.data.data);
              this.tableData = res.data.data;
            })
      },
      resetDateFilter() {
        this.$refs.filterTable.clearFilter('date');
      },
      clearFilter() {
        this.$refs.filterTable.clearFilter();
      },
      formatter(row, column) {
        return row.address;
      },
      filterTag(value, row) {//页面内
        return row.tag === value;
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },

      // 搜索功能
      searchBtn(){
        var search = this.search;
        var userName = [];
        this.tableData.map((item) => {
          userName += item.userName + ','
        })
        // console.log(userName);
        if(search){
          this.searchData = this.tableData.filter((res) =>{
            console.log(res);
            return Object.keys(res).some((key) => {
              // console.log(key);
              return String(res[key]).toLowerCase().indexOf(search) > -1
            })
          })
        }
      }
    }
  }
</script>

<style>
.el-card{
  padding: 0 20px;
}
</style>
