import VueRouter from 'vue-router'
import Vue from 'vue'
import home from '../views/index/home.vue'
import problemList from '../views/problem/problemList.vue'
import problemDetail from '../views/problem/problemDetail.vue'
import problemAdd from '../views/problem/problemAdd.vue'
import problemEdit from '../views/problem/problemEdit.vue'
import dataEdit from '../views/problem/dataEdit.vue'
import situation from '../views/problem/situation.vue'
import help from '../views/user/help.vue'
import signIn from '../views/index/signIn.vue'
import login from '../views/index/login.vue'
import foot from '../components/foot.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',//默认路径
        redirect:'/home'//重定向
      },
    {
        path: '/home',
        component: home
    },
    {
        path: '/problemList',
        component: problemList
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
        path: '/situation',
        component: situation
    },
        {
        path: '/help',
        component: help
    },
    {
        path: '/signIn',
        component: signIn
    },
    {
        path: '/login',
        component: login
    },    
    {
        path: '/foot',
        component: foot
    }
]

const router = new VueRouter({
    routes
})

export default router