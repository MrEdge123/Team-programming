import axios from 'axios'
import Vue from 'vue'
import store from '@/store'
import ElementUI from 'element-ui'
import {ACCESS_TOKEN} from '@store/mutation-types'

// 创建axios实例
const instance = axios.create({
        baseURL: 'http://8.129.147.77:80',
        timeout: 5000
})

// 错误拦截回调函数
const err = err => {
    if(error.response){
        let data = error.response.data;
        const taken = Vue.ls.get(ACCESS_TOKEN);  //获取保存的taken
        switch(err.response.status){
            case 403:
                ElementUI.err({message: '消息提示', description: '拒绝访问', duration: 4})
                break
            case 500:
                if(token && data.message == 'Token失效，请重新登录'){
                    ElementUI.err({
                        title: '登录已过期',
                        content: '很抱歉，登录已过期，请重新登录',
                        okText: '重新登录',
                        mask: false,
                        onOk: () => {
                            store.dispatch('Logout').then(() => {
                                Vue.ls.remove(ACCESS_TOKEN)
                                window.location.reload();
                            })
                        }
                    })
                }
                break
            case 404:
                ElementUI.err({message:'系统提示', description: '很抱歉未找到资源。', duration: 4})
                break
            case 401:
                ElementUI.err({message: '系统提示', description: '未授权，请重新登录。', duration: 4})
                if(token){
                    store.dispatch('Logout').then(() => {
                        setTimeout(() => {
                            window.location.reload()
                        }, 1500)
                    })
                }
                break
            default: 
                ElementUI.err({
                    message: '系统系统',
                    description: '连接超时。',
                    duration: 4
                })
                break
        }
    }
    return Promise.reject(error)
}

instance.interceptors.request.use(
    config => {
        const token = Vue.ls.get(ACCESS_TOKEN)
        if(token){
            config.headers['X-Access-Token'] = token
        }
        if(config.method == 'get'){
            config.params = {
                _t: Date.parse(new Date()) / 1000,
                ...config.params
            }
        }
        return config
    },
    error => {
        return Promise.reject(error)
    }
)

instance.interceptors.response.use(response => {
    return response.data
}, err)

export { instance as axios }