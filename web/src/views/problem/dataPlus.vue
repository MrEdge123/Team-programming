 <template>
  <div class="login">
    <div class="login-input">
      <el-form >
        <el-form-item label="输入数据">
          <!-- <el-input v-model="inputData"></el-input> -->
            <el-col :span="24" ><div >
            <el-input
            type="textarea"
            :autosize="{ minRows: 2}"
            placeholder="请输入内容"
            v-model="inputData">
            </el-input>
            </div></el-col>
        </el-form-item>
        <el-form-item label="输出数据" >
          <!-- <el-input v-model="outputData" ></el-input> -->
            <el-col :span="24" ><div >
            <el-input
            type="textarea"
            :autosize="{ minRows: 2}"
            placeholder="请输入内容"
            v-model="outputData">
            </el-input>
            </div></el-col>
        </el-form-item>
        <!-- `checked` 为 true 或 false -->
        <el-form-item label="作为例子展示">
          <el-switch v-model="isExample" @change="inputToDisabled()"></el-switch>
        </el-form-item>
        <el-form-item label="例子说明" >
          <!-- <el-input v-model="outputData" ></el-input> -->
            <el-col :span="24" ><div >
            <el-input
            type="textarea"
            :autosize="{ minRows: 2}"
            placeholder="请输入内容"
            v-model="explanation"
            :disabled="disabled">
            </el-input>
            </div></el-col>
        </el-form-item>
        <el-button  @click="addPro()">添加</el-button>
        <el-button  @click="addCancle()" >取消</el-button>
      </el-form>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import Qs from 'qs'
export default {
data(){
    return{
        id: this.$route.params.problemId,
        inputData:'',
        outputData:'',
        isExample:false,
        explanation:'',
        disabled:true
    }
},
methods:{
  inputToDisabled(){//是否添加例子说明
        if(this.isExample){
          this.disabled=false;}
          else{
          this.disabled=true;
        }
      },
    addPro(){
      if(!this.isExample){this.explanation=null}
      // console.log(this.explanation)
        this.$confirm('请确保添加, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {//加post请求
      let data={//在data里面用键值对的形式写要写的参数
        // problemId:this.id,
        number:this.number,
        inputData:this.inputData,
        outputData:this.outputData,
        isExample:this.isExample,
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
.login{
  display: flex;
  justify-content: center;
  margin-top: 80px;
}
.login-input{
  width: 400px;
}
</style>
