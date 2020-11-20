import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import axios from 'axios'
import './assets/css/common.css'
// import tool from './assets/js/tool'


// Vue.prototype.tool = tool;
Vue.use(ElementUI)
Vue.config.productionTip = false
axios.defaults.withCredentials = true;  //跨域访问需要访问发送cookie时
Vue.prototype.$axios = axios;


// Vue.http.options.emulateJSON = true;
// Vue.http.options.xhr = { withCredentials: true};


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

router.beforeEach((to, from , next) => {
  if (to.path === "/login") {next();}
  else { // 判断该路由是否需要登录权限
  if (to.meta.isLogin && !localStorage.getItem("username")) { // 判断当前的token是否存在
  next({
  path: "/login",
  query: {redirect: to.fullPath} // 将跳转的路由path作为参数，登录成功后跳转到该路由
  });
  }else{
  next();
  }
  }
  });