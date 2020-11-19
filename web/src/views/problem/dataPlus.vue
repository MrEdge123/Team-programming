<template>
<!-- 数据添加，测试，输入框太少 -->
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
import axios from 'axios'
import Qs from 'qs'
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
        }).then(() => {//加post请求
let data={//在data里面用键值对的形式写要写的参数
        number:this.number,
        inputData:this.dein,
        outputData:this.deout,
        isExample:this.isExample,
        problemDescription:this.problemDescription,
        explanation:this.explanation,
                }
          axios({url:'http://8.129.147.77/addTestData/',//post这里写请求网址
          method:'post', //然后method改成get
        //  headers:{'Content-Type':"application/json;charset=UTF-8"},
          headers:{'Content-Type':'application/x-www-form-urlencoded'},
          data:Qs.stringify(data)
            }).then((res) => {
            console.log(res)
            if(res.data.code == '200'){
              rows.splice(index, 1);
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

<style>