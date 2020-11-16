<template>
<el-menu
    :default-active="this.$route.path"
     class="el-menu-demo"
     mode="horizontal"
     @select="handleSelect"
     router
     background-color="#fff"
     text-color="#333"
     active-text-color="#0084ff"
     >
     <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
          <template slot="title">
             <span> {{ item.navItem }}</span>
          </template>
     </el-menu-item>
</el-menu>
</template>

<script>


export default {
  name: 'navbar',
   data() {
    return {
        navList:[
             {name:'../views/index/home.vue', navItem:'主页'},
             {name:'../views/problem/problemList.vue',navItem:'题目列表'},
             {name:'../views/problem/situation.vue',navItem:'状态'},
             {name:'../views/user/help.vue',navItem:'帮助'},
             {name:'../views/index/login.vue',navItem:'登录'},
             {name:'../views/index/register.vue',navItem:'注册'},
        ]

    }
  },
  methods: {
    handleSelect(key, keyPath) {
        console.log(key, keyPath);

      }
  }
}
</script>

<style>
/* *{
  padding: 0;
  margin: 0;
}

.navbar-list{
  height: 40px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: slateblue;
}

.navbar a{
  color: white;
  text-decoration: none;
  font-size: 20px;
} */
</style>
