<template>
<!-- 老师的问题添加界面 已完成 -->
<el-card>
  <el-row :gutter="20">
    <el-col :span="4"><h3>题目标题</h3></el-col>
    <el-col :span="16"><div class="grid-content bg-purple">
        <el-input
        type="textarea"
        autosize
        placeholder="请输入题目标题"
        v-model="problemTitle">
      </el-input>
    </div></el-col>
  </el-row>
  <el-row :gutter="20">
      <el-col :span="4"><div class="grid-content bg-purple">
          <span style="center">时间限制：</span>
          </div>
      </el-col>
      <el-col :span="6"><div class="grid-content bg-purple">
      <el-form>
          <el-form-item class="petname">
          <el-input v-model="memoryLimit" placeholder="">
          <template slot="append">ms</template>
          </el-input> </el-form-item>
          </el-form></div>
      </el-col>
      <el-col :span="4"><div class="grid-content bg-purple">
          <span style="center">空间限制：</span>
          </div>
      </el-col>
      <el-col :span="6"><div class="grid-content bg-purple">
        <el-form>
        <el-form-item class="petname">
        <el-input v-model="timeLimit" placeholder="">
        <template slot="append">MB</template>
        </el-input> </el-form-item></el-form></div >
      </el-col>
  </el-row>
  <div><h3>题目描述：</h3></div>
  <el-row type="flex" class="row-bg">
    <el-col :span="20" ><div class="grid-content bg-purple-light">
          <el-input
          type="textarea"
          :autosize="{ minRows: 1}"
          v-model="problemDescription">
          </el-input>
        </div></el-col>
  </el-row>
  <div><h3>输入描述：</h3></div>
  <el-row type="flex" class="row-bg">
    <el-col :span="20" ><div class="grid-content bg-purple-light">
          <el-input
          type="textarea"
          :autosize="{ minRows: 1}"
          v-model="inputDescription">
          </el-input>
        </div></el-col>
  </el-row>
  <div><h3>输出描述：</h3></div>
  <el-row type="flex" class="row-bg">
    <el-col :span="20" ><div class="grid-content bg-purple-light">
          <el-input
          type="textarea"
          :autosize="{ minRows: 1}"
          v-model="outputDescription">
          </el-input>
        </div></el-col>
  </el-row>
  <el-row>
      <el-col :span="6"  ><el-button  @click="addPro()">新建题目</el-button></el-col>
      <el-col :span="6"><el-button  @click="addCancle()" >取消</el-button></el-col>
  </el-row>
</el-card>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
data(){
    return{
        // id: this.$route.params.problemId,
        problemTitle:'',
        memoryLimit:'',
        timeLimit:'',
        problemDescription:'',
        inputDescription:'',
        outputDescription:'',
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
          let data={//在data里面用键值对的形式写要写的参数
          problemTitle:this.problemTitle,
          memoryLimit:this.memoryLimit,
          timeLimit:this.timeLimit,
          problemDescription:this.problemDescription,
          inputDescription:this.inputDescription,
          outputDescription:this.outputDescription,
        }
        axios({url:'http://8.129.147.77/addQuestions/',//post这里写请求网址
        method:'post', //然后method改成get
      //  headers:{'Content-Type':"application/json;charset=UTF-8"},
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        data:Qs.stringify(data)
          }).then((res) => {
          console.log(res)
          if(res.data.code == '200'){
            this.$message({
            type: 'success',
            message: '添加成功!'
          });
          }else{
            alert('出现错误。');
          }
      })
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

<style scoped>
.el-card{
  margin: 15px;
  display: flex;
  flex-direction: column;
}
  .el-row {
    display: flex;
    align-items: center;
  }
  .el-col {
    border-radius: 4px;
    text-align: center;
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
