import VueRouter from 'vue-router'
import Vue from 'vue'
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

const routes = [
    {
        path: '/',//默认路径
        redirect:'/home'//重定向
      },
    {
        path: '/home',
        component: home,
        meta: {
          isLogin: false
        }
    },
    {
        path: '/problemList',
<<<<<<< HEAD
        component: problemList,
        meta: {
          isLogin: true
        }
=======
        name: 'problemList',
        component: problemList,
        // meta: {
        //     isLogin: true
        //   }
>>>>>>> 5d7b6180947e89fd55df5199357d65695428d077
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

// router.beforeEach((to, from, next) => {
//     const isLogin = sessionStorage.getItem('isLogin'); //获取本地存储的登陆信息
//     console.log(isLogin)
//     if (to.name == 'login') { //判断是否进入的login页
//       if (isLogin == "true") {  //判断是否登陆
//         next({ name: 'problemList'});  //已登录，跳转首页（a页面） name: 'problemList'
//       } else {
//         next();  //没登录，继续进入login页
//       }
//     } else { //如果进入的非login页
//       if (isLogin == "true") {   //同样判断是否登陆
//         next();  //已登录，正常进入
//       } else {
//         next({ name: 'login'});  //没登录，跳转到login页
//       }
//     }
//   });
export default router
