<template>
  <div class="detail-body">
    <nav-header></nav-header>
    <div>
       <h1>这里是题目详情页面</h1>
       <span>时间限制：1s</span>
       {{this.data.id}} 
    </div>
    <nav-footer></nav-footer>
  </div>
</template>

<script>
import NavHeader from '../components/Header'
import NavFooter from '../components/Footer'
export default {
  name: 'detail',
  data(){
    return{
      problemList:[],//列表
      id: this.$route.params.id
    }
  },
  mounted(){
    this.init();
  },  
  props: {},
  components:{
    NavHeader,
    NavFooter,
  },
 methods:{
    init(){
      this.axios.get("/mock/problem.json").then((response)=>{
       let res=response;
       this.problemList=res.data.data;
       window.console.log(this.problemList)
      })
    }
 }
}
</script>

<style scoped>
.detail-body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
