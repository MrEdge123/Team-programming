import axios from 'axios'


// 创建axios实例
export function request(config){
        const instance = axios.create({
            baseURL: 'http://8.129.147.77:80',
            timeout: 5000,
        })
        // axios的拦截器
        // 请求拦截的作用
        instance.interceptors.request.use(config => {
            const token = sessionStorage.getItem("token"); //获取存储在本地的token，如果需要token就在这里带上
            console.log(token)
        config.data = JSON.stringify(config.data);  // 这里我们也可以在过滤下 请求参数数据
        config.headers = {    // 设置请求头   常用语post请求 
             "Content-Type": "application/json"               
         };
         if (token) {
              config.headers.Authorization = "Token " + token; //存在的话 就携带 token
        }
        return config;   //  然后把配置返回
        }, err => {
            console.log(err);
        })

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

