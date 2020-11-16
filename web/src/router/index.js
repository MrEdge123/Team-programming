import VueRouter from 'vue-router'
import Vue from 'vue'
import axios from 'axios'
import home from '../views/index/home.vue'
import problemList from '../views/problem/problemList.vue'
import problemDetail from '../views/problem/problemDetail.vue'
import problemAdd from '../views/problem/problemAdd.vue'
import problemEdit from '../views/problem/problemEdit.vue'
import dataEdit from '../views/problem/dataEdit.vue'
import dataPlus from '../views/problem/dataPlus.vue'
import problemPlus from '../views/problem/problemPlus.vue'
import situation from '../views/problem/situation.vue'
import help from '../views/user/help.vue'
import register from '../views/index/register.vue'
import login from '../views/index/login.vue'
import foot from '../components/foot.vue'

Vue.use(VueRouter)
axios.defaults.withCredentials=true;
Vue.prototype.$axios = axios;

const routes = [
    {
        path: '/',//默认路径
        redirect:'/home'//重定向
    },
    {
        path: '/home',
        component: home,
    },
    {
        path: '/problemList',
        name: 'problemList',
        meta:{
        requireAuth: true},
        component: problemList,
    },
    {
        path: '/problemDetail/:problemId',
        component:problemDetail
    },
    {
        path: '/problemAdd',//--
        component:problemAdd
    },
    {
        path: '/problemEdit/:problemId',//--/:problemId
        component:problemEdit
    },
    {
        path: '/dataEdit/:problemId',
        component:dataEdit
    },
    {
        path: '/dataPlus/:problemId',
        component:dataPlus
    },
    {
        path: '/problemPlus',//--/:problemId
        component:problemPlus
    },
    {
        path: '/situation',
        component: situation
    },
        {
        path: '/help',
        component: help
    },
    {
        path: '/register',
        component: register,
        meta: {
          isLogin: false
        }
    },
    {
        path: '/login',
        name: 'login',
        component: login,
        meta: {
          isLogin: false
        }
    },
    {
        path: '/foot',
        component: foot
    }
]

const router = new VueRouter({
    routes
})

router.beforeEach((to, from, next) => {
    const lastname = sessionStorage.getItem("Name")
    console.log(lastname)
    console.log(JSON.parse(lastname))
    if (to.name === 'login') {
        const islogin = localStorage.getItem('login')
        console.log(islogin)
        if (islogin){
            router.replace('/problemList')
        }
    }
    next()
})
export default router
