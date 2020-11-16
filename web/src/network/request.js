import axios from 'axios'


// 创建axios实例
export function request(config){
        const instance = axios.create({
            baseURL: 'http://8.129.147.77:80',
            timeout: 5000,
            // headers:{'Content-Type':'application/x-www-form-urlencoded'},
            withCredentials: true,
        })
        // axios的拦截器
        // 请求拦截的作用
        instance.interceptors.request.use(config => {
        if (config.method === 'get') {
          //  给data赋值以绕过if判断
          config.data = true 
        }
      
        config.headers['Content-Type'] = 'application/json'
        return config
      }, err => Promise.reject(err))

        //响应拦截
    instance.interceptors.response.use(
        res => {
            return res.data
        }, err =>{
            console.log(err);
        })

        // 发送真正的网络请求
        return instance(config)

    }

