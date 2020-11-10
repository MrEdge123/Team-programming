<template>
<div>
    <div class="search">
      <el-row :gutter="20">
        <el-col :span="4"><div class="grid-content bg-purple">
              <span style="center">题目编号：</span>
              </div>
        </el-col>
        <el-col :span="6"><div class="grid-content bg-purple">
            <el-form>
              <el-form-item class="petname">
                <el-input v-model="inputId" placeholder="输入题目编号"></el-input> </el-form-item>
                </el-form></div>
        </el-col>
        <el-col :span="4"><div class="grid-content bg-purple">
              <span style="center">题目标题：</span>
              </div>
        </el-col>
        <el-col :span="6"
          ><div class="grid-content bg-purple">
            <el-form>
              <el-form-item class="petname">
                <el-input v-model="inputTitle" placeholder="输入题目标题"></el-input> </el-form-item
            ></el-form></div
        ></el-col>
        <el-col :span="2"><div class="grid-content bg-purple">
            <el-button >搜索</el-button>
            <!-- 没有实现搜索的功能-->
          </div></el-col>
      </el-row>
        </div>
      <div>
      <el-table
      :data="problemList"
      style="width: 100%"
      @row-click="detileTrans">
      <el-table-column
        prop="problemId" 
        label="题目编号"
        width="300">
      </el-table-column>
      <el-table-column
        prop="problemTitle"
        label="题目标题">

      </el-table-column>
    </el-table>
      </div>  
</div>

</template>

<script>
export default {
  name: "problem",
  data() {
    return {
      inputId: '',
      inputTitle:'',
      problemList: [
         {
            "problemId": "10001",
            "problemName": "浪险1",
            "problemPrice": 99,
            "problemNum": 2,
            "problemImage": "1.jpg",
            "problemTitle":"题目标题",
            "checked": false
        },
        {
            "problemId": "10002",
            "problemName": "浪险2",
            "problemPrice": 199,
            "problemNum": 2,
            "problemImage": "2.jpg",
            "problemTitle":"题目标题",
            "checked": false
        },
        {
            "problemId": "10003",
            "problemName": "浪险3",
            "problemPrice": 999,
            "problemNum": 2,
            "problemImage": "3.jpg",
            "problemTitle":"题目标题",
            "checked": true
        }
      ], //列表
    };
  },
  mounted() {
    // this.init();
  },
  computed: {
    checkedCount() {
      return this.problemList.some((item) => {
        return item.checked;
      });
    },
  },
  filters: {},
  methods: {
    // init() {
    //   this.axios.get("/mock/problem.json").then((response) => {
    //     let res = response;
    //     this.problemList = res.data.data;
    //     window.console.log(this.problemList);
    //   });
    // },
    detileTrans(row) {
      if (this.checkedCount) {
        this.$router.push("/problemDetail/" + row.problemId); //跳转页面
      }
    },
  },
};
</script>

<style>
.search {
  margin: 10px 0px;
  padding:0px 10px;
  display: flex;
}
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
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>