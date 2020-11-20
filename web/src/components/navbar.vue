<template>
  <el-menu
      :default-active="this.$route.path"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      router
      background-color="slateblue"
      text-color="#fff"
      active-text-color="#0084ff"
      >
      <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name" @click="navAdmin">
            <template slot="title">
              <span> {{ item.navItem }}</span>
            </template>
      </el-menu-item>
      <el-menu-item @click="logout" >
        <span> 退出</span>
      </el-menu-item>
  </el-menu>
</template>
<script>
export default {
  name: 'navbar',
   data() {
    return {
      activeIndex:'home',
        navList:[
             {name:'home', navItem:'主页'},
             {name:'problemList',navItem:'题目列表'},
             {name:'situation',navItem:'状态'},
             {name:'help',navItem:'帮助'},
             {name:'login',navItem:'登录'},
             {name:'register',navItem:'注册'},
        ]
    }
  },
  mounted(){
  this.navAdmin()
  },
  methods: {
     handleSelect(key, keyPath) {
        this.$router.push('/'+key);
     },
      logout(){//退出登陆
     this.$confirm('是否继续退出?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
            window.localStorage.clear()
            this.$router.push('/login');
            this.$message({
            type: 'success',
            message: '已退出'
          });
        }).catch(() => {
          this.$router.go(-1);
          this.$message({
            type: 'info',
            message: '已取消'
          });

        });


    },
     navAdmin(){
        var  storage = window.localStorage;
        var isAdmin= storage.getItem('isAdmin');
        // console.log(isAdmin)
        if(isAdmin==='1')
        {this.navList=[
             {name:'home', navItem:'主页'},
             {name:'problemList',navItem:'题目列表'},
             {name:'problemAdd',navItem:'编辑题目'},
             {name:'problemPlus',navItem: '新建题目'},
             {name:'help',navItem:'帮助'},
             {name:'login',navItem:'登录'},
             {name:'register',navItem:'注册'}]}
             else{
       this.navList=[
             {name:'home', navItem:'主页'},
             {name:'problemList',navItem:'题目列表'},
             {name:'situation',navItem:'状态'},
             {name:'help',navItem:'帮助'},
             {name:'login',navItem:'登录'},
             {name:'register',navItem:'注册'},
        ]
     }}
     
  },

}
</script>
<style>
.el-menu-demo{
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>
