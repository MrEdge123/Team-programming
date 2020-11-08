<template>
  <div class="problem-body">
    <nav-header></nav-header>
    <div class="search">
   <form>
     <!-- action="/login/" method="post" -->
    <!-- <div class="pro-num"></div> -->
    题目编号：<input type="text" name="FirstName" value="输入编号"> 
    <!-- <div class="pro-message"></div>  -->
    标题：<input type="text" name="LastName" value="题目标题">
    <!-- 页面转换-->
   </form>
    </div> 
  <div class="main">
    <div class="pro-title">
        <div class="pro-num">题目序号</div>
        <div class="pro-message">题目描述</div>
    </div>
    <ul class="pro-list">
      <li class="pro" v-for="item in problemList" :key="item.productId"  @click="checkTitle(item.productId)">
        <div class="pro-num">
            <div style="margin:0px 5px;">{{item.productId}}</div>
        </div>
        <div class="pro-message">
          <div @click="checkTitle(item.productId)">{{item.problemTitle}}</div>
          </div>
      </li>
    </ul>
  </div>
  <nav-footer></nav-footer>
  </div>      
</template>

<script>
import NavHeader from '../components/Header'
import NavFooter from '../components/Footer'
// import Modal from '../components/Modal'
export default {
  name: 'problem',
  data(){
    return{
      modalConfirm:false,//弹框显示属性
      problemList:[],//列表
      delItem:'',//要删除的一项
    }
  },
  components:{
    NavHeader,
    NavFooter,
    // Modal
  },
  mounted(){
    this.init();
  },
  computed:{
    checkAllFlag(){
      return this.problemList.every((item)=>{
        return item.checked;
      });
    },
    checkedCount(){
      return this.problemList.some((item)=>{
        return item.checked;
      })
    },
    totalPrice(){
      let money=0;
      this.problemList.forEach((val)=>{
        if(val.checked){
          money+=val.productNum*val.productPrice;
        }
      })
      return money
    }
  },
  filters:{
    // currency:(value)=>{
    //   if(!value){
    //     return 0.00;
    //   } 
    //   return '¥'+(value*1).toFixed(2)+'元'
    // }
  },
  methods:{
    init(){
      this.axios.get("/mock/problem.json").then((response)=>{
       let res=response;
       this.problemList=res.data.data;
       window.console.log(this.problemList)
      })
    },
    checkTitle(){
       if(this.checkedCount){
        this.$router.push({
          // path:'/problemdetail/${productId}',//跳转页面
          name:'detail',
          params:{
             id:'productId'}
            //  msgKey: this.msg}
          /*query: {  
            key: 'key',   
            msgKey: this.msg  
            }*/

        })
       }
    }
    // closeModal(){
    //   this.modalConfirm=false;
    // },
    // delproblem(){
    //   let delItem=this.delItem;
    //   this.problemList.forEach((val,index)=>{
    //     if(delItem.productId==val.productId){
    //       this.problemList.splice(index,1);
    //       this.modalConfirm=false;
    //     }
    //   })
    // },
    // toggleCheckAll(){
    //   let flag=!this.checkAllFlag;
    //   this.problemList.forEach((item)=>{
    //     item.checked=flag;
    //   })
    // },
    // checkOut(){
    //   if(this.checkedCount){
    //     this.$router.push({
    //       path:'/address'
    //     })
    //   }
    // }
  }
}
</script>

<style scoped>
.problem-body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.search {
  height: 20px;
  line-height: 0px;
  margin: 10px 0px;
  /* background-color: rgb(252, 252, 252); */
  padding: 0px 0px;
  display: flex;
  color: rgb(14, 13, 13);
}
.main {
  width: 100%;
  background-color: #eee;
  padding: 5px 0px;
  flex: 1;
}
.pro-title {
  height: 30px;
  line-height: 30px;
  margin: 0px 0px;
  background-color: #333;
  display: flex;
  color: white;
}
/* .pro-title > div:nth-child(1) {
  flex: 3;
}
.pro-title > div:nth-child(2) {
  flex: 2;
}
.pro-title > div:nth-child(n + 3) {
  flex: 1;
} */
.pro-list {
  margin: 0;
  padding: 0;
}
.pro {
  display: flex;
  background-color: white;
  margin: 0px 0px 0px;
  height: 90px;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid #ddd;
}
.pro-message {
  flex: 3;
  display: flex;
  align-items: center;
}
.pro-message > img:nth-child(1) {
  margin-left: 20px;
  cursor: pointer;
}
.pro-message > img:nth-child(2) {
  margin-left: 20px;
  cursor: pointer;
}
.pro-message > img:nth-child(3) {
  margin-left: 10px;
}
.pro-message > div {
  margin-left: 10px;
}
.pro-price {
  flex: 2;
}
.pro-num {
  flex: 1;
  display: flex;
  align-items: left;
  justify-content:left;
}
.pro-price-total {
  flex: 1;
}
.pro-delete {
  flex: 1;
}
.pro-pay {
  display: flex;
  background-color: white;
  margin: 10px 5px;
}
.pro-bottom-left {
  display: flex;
  flex: 1;
  justify-content: space-between;
  padding: 10px 20px;
}
.pro-bottom-right {
  width: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ddd;
}
.pro-all,
.pro-total {
  display: flex;
}
.pro-all img {
  margin-right: 10px;
  cursor: pointer;
}
.ablePay {
  background-color: crimson;
  color: white;
  cursor: pointer;
}
</style>
