import {request} from './request'
import Qs from 'qs'

export function getRegisterMultidata(data){
    return request({
        url: '/register/',
        method: 'post',
        data
    })
}

export function getLoginMultidata(datas){
    return request({
        url: '/login/',
        method: 'post',
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        data:Qs.stringify(datas)
         //  method:'post', //然后method改成get
                    //  headers:{'Content-Type':'application/x-www-form-urlencoded'},
                    //  data:Qs.stringify(data)
    })
}

