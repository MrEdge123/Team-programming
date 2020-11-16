import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import axios from 'axios'
import tool from './assets/js/tool'


Vue.prototype.tool = tool;
Vue.use(ElementUI)
Vue.config.productionTip = false

axios.defaults.withCredentials=true

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
