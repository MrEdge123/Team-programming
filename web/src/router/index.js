import VueRouter from 'vue-router'
import Vue from 'vue'
import home from '../views/index/home.vue'
import problemList from '../views/problem/problemList.vue'
import situation from '../views/problem/situation.vue'
import help from '../views/user/help.vue'
import signIn from '../views/index/signIn.vue'
import login from '../views/index/login.vue'
import foot from '../components/foot.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/home',
        component: home
    },
    {
        path: '/problemList',
        component: problemList
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