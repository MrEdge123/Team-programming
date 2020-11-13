import axios from 'axios'
// import Vue from 'vue'
// import store from '../store'
// import ElementUI from 'element-ui'
// import {ACCESS_TOKEN} from '../store/mutation-types'

// 创建axios实例
export function request(config){
        const instance = axios.create({
            baseURL: 'http://8.129.147.77:80',
            timeout: 5000
        })

        // axios的拦截器
        // 请求拦截的作用
        instance.interceptors.request.use(config => {
            return config
        }, err => {
            console.log(err);
        })

        //响应拦截
        instance.interceptors.response.use(res =>{
            return res.data
        }, err =>{
            console.log(err);
        })

        // 发送真正的网络请求
        return instance(config)

    }

