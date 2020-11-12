<template>
<div>
<div style="margin: 10px 0;"></div>
<el-row :gutter="20">
  <el-col :span="4"><div class="grid-content bg-purple"><h3>题目标题</h3></div></el-col>
  <el-col :span="16"><div class="grid-content bg-purple">
      <el-input
      type="textarea"
      autosize
      placeholder="请输入内容"
      v-model="textarea">
    </el-input>
  </div></el-col>
</el-row>
<el-row :gutter="20">
    <el-col :span="2"><div class="grid-content bg-purple">
        <span style="center">时间限制：</span>
        </div>
    </el-col>
    <el-col :span="4"><div class="grid-content bg-purple">
    <el-form>
        <el-form-item class="petname">
        <el-input v-model="inputId" placeholder="输入题目编号"></el-input> </el-form-item>
        </el-form></div>
    </el-col>
    <el-col :span="2"><div class="grid-content bg-purple">
        <span style="center">空间限制：</span>
        </div>
    </el-col>
    <el-col :span="4"><div class="grid-content bg-purple">
       <el-form>
       <el-form-item class="petname">
       <el-input v-model="inputTitle" placeholder="输入题目标题">
       </el-input> </el-form-item></el-form></div >
    </el-col>
</el-row>
<div><h3>题目描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" ><div class="grid-content bg-purple-light">
        <el-input
        type="textarea"
        :autosize="{ minRows: 1}"
        placeholder="请输入内容"
        v-model="dePro">
        </el-input>
      </div></el-col>
</el-row>
<div><h3>输入描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" ><div class="grid-content bg-purple-light">
        <el-input
        type="textarea"
        :autosize="{ minRows: 1}"
        placeholder="请输入内容"
        v-model="dein">
        </el-input>
      </div></el-col>
</el-row>
<div><h3>输出描述：</h3></div>
<el-row type="flex" class="row-bg">
  <el-col :span="20" ><div class="grid-content bg-purple-light">
        <el-input
        type="textarea"
        :autosize="{ minRows: 1}"
        placeholder="请输入内容"
        v-model="deout">
        </el-input>
      </div></el-col>
</el-row>
<el-row>
    <el-button></el-button>
</el-row>
</div>
</template>

<script>
export default {
data(){
    return{
        id: this.$route.params.problemId,
        textarea:'',
        dePro:'',
        dein:'',
        deout:'',
    }
}
}
</script>

<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
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