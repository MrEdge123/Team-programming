import {request} from './request'

export function getRegisterMultidata(){
    return request({
        url: '/register/'
    })
}

export function getLoginMultidata(){
    return request({
        url: '/login/'
    })
}

