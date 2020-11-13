<template>
<div>
<div style="margin: 10px 0;" class="container"></div>
<el-row ><el-col :span="10" ><div><h3>输入数据：</h3></div></el-col>  
<el-col :span="4"> </el-col>
<el-col :span="10" ><div><h3>输出数据：</h3></div></el-col>  </el-row>  
<el-row type="flex" class="row-bg">
    <el-col :span="10" ><div >
    <el-input
    type="textarea"
    :autosize="{ minRows: 2}"
    placeholder="请输入内容"
    v-model="dein">
    </el-input>
    </div></el-col>
<el-col :span="2"> </el-col>
  <el-col :span="10" ><div>
        <el-input
        type="textarea"
        :autosize="{ minRows: 2}"
        placeholder="请输入内容"
        v-model="deout">
        </el-input>
      </div></el-col>
</el-row>
<el-row>
    <el-col :span="6"  ><el-button  @click="addPro()">添加数据</el-button></el-col>
    <el-col :span="6"><el-button  @click="addCancle()" >取消</el-button></el-col>
</el-row>
</div>
</template>

<script>
export default {
data(){
    return{
        id: this.$route.params.problemId,
        dein:'',
        deout:'',
    }
},
methods:{
    addPro(){
        this.$confirm('请确保添加, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
          this.$message({
            type: 'success',
            message: '添加成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消'
          });
        });
      },
      addCancle(){
          this.$router.go(-1);
          this.$message({
            type: 'info',
            message: '已取消'
          });
        }
}
}
</script>

<style>