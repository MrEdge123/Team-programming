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
             {name:'home', navItem:'主页'},
             {name:'problemList',navItem:'题目列表'},
             {name:'situation',navItem:'状态'},
             {name:'help',navItem:'帮助'},
             {name:'login',navItem:'登录'},
             {name:'register',navItem:'注册'},
        ]

    }
  },
  methods: {
     handleSelect(key, keyPath) {
        console.log(key, keyPath);
     }
  },

}
</script>

<style>

</style>
