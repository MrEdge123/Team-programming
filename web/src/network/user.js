import {request} from './request'

export function getRegisterMultidata(){
    return request({
        url: '/register/',
        method: 'post',
        params: []
    })
}

export function getLoginMultidata(){
    return request({
        url: '/login/',
        method: 'post',
        params: []
    })
}

