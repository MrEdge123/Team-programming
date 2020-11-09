<template>
<div>
  <!-- <el-row>
  <el-col :span="24"><div class="grid-content bg-purple-dark">
    <h1 style="center">{{id}}：题目标题</h1>
    </div></el-col>
</el-row> -->
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="8"><div class="grid-content bg-purple-light">
      <h1>{{id}}：题目标题</h1>
      </div></el-col>
</el-row>
<div style="margin: 60px 0;"></div>

<div><h3>题目描述：</h3></div>
<el-row>
  <el-col :span="24" ><div class="grid-content bg-purple-dark"><h1>{{id}}：题目标题</h1></div></el-col>
</el-row>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h1>{{id}}：题目标题</h1>
      </div></el-col>
</el-row>
<div><h3>输入描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h1>{{id}}：题目标题</h1>
      </div></el-col>
</el-row>
<div><h3>输出描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h1>{{id}}：题目标题</h1>
      </div></el-col>
</el-row>
<div><h3>例子描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" :offset="1"><div class="grid-content bg-purple-light">
      <h1>{{id}}：题目标题</h1>
      </div></el-col>
</el-row>
<div style="margin: 60px 0;"></div>
<div>
<el-row>
  <el-col :span="3" ><div class="grid-content bg-purple-light"><h3>输入代码</h3></div></el-col>
</el-row>
<el-input
  type="textarea"
  :autosize="{ minRows: 20, maxRows: 40}"
  placeholder="请输入内容"
  v-model="textarea">
</el-input>
</div>
</div>

</template>

<script>
export default {
data(){
    return{
       id: this.$route.params.problemId,
       textarea: '',
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