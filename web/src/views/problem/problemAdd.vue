<template>
<div>
  <br>
  <el-row  type="flex" justify="end">
    <el-col :span="3">
    <el-button icon="el-icon-circle-plus" 
    @click.native.prevent="plusProblem()">新建题目</el-button></el-col>
  </el-row>
  <el-table
    :data="tableData"
    style="width: 100%" >
    <el-table-column
      fixed
      prop="problemId"
      label="题目编号"
      width="150">
    </el-table-column>
    <el-table-column
      prop="name"
      label="题目标题"
      width="300">
    </el-table-column> 
    <el-table-column
      fixed="right"
      label="编辑题目"
      width="80">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-edit" circle
         @click.native.prevent="editProblem(scope.$index, tableData)" size="small"></el-button>
      </template>
    </el-table-column>
    <el-table-column
      fixed="right"
      label="编辑数据"
      width="80">
      <template slot-scope="scope">
        <el-button type="primary" icon="el-icon-edit" circle
        @click.native.prevent="editData(scope.$index, tableData )" size="small"></el-button>
      </template>
    </el-table-column>   
    <el-table-column
      fixed="right"
      label="删除题目"
      width="80">
      <template slot-scope="scope">
        <el-button type="danger" icon="el-icon-delete" circle
        @click.native.prevent="deleteRow(scope.$index, tableData)" size="small"></el-button>
      </template>
    </el-table-column>
  </el-table>
</div>
</template>

<script>
  export default {
    methods: {
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
        tableData: [{
          date: '10001',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200331
        }, {
          date: '2016-05-02',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200332
        }, {
          date: '2016-05-04',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200333
        }, {
          date: '2016-05-01',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200335
        }, {
          date: '2016-05-08',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200353
        }, {
          date: '2016-05-06',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200633
        }, {
          date: '2016-05-07',
          name: '题目标题',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          problemId: 200393
        }]
      }
    }
  }
</script>
<style>

</style>