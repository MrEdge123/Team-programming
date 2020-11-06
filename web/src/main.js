import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui'
import './assets/css/common.css'

Vue.use(ElementUI);

new Vue({
  el: '#app',
  render: h => h(App)
});


createApp(App).use(store).use(router).mount('#app')
