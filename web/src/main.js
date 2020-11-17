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
axios.defaults.withCredentials=true;  //跨域访问需要访问发送cookie时
Vue.prototype.$axios = axios;

// Vue.prototype.$http = axios;
// axios.defaults.baseURL = "http://8.129.147.77:80"

// Vue.http.options.emulateJSON = true;
// Vue.http.options.xhr = { withCredentials: true};


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

