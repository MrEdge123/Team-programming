import {axios} from './request'

export function getRegisterMultidata(){
    return axios({
        url: '/register/',
        method: 'post',
        params: []
    })
}

export function getLoginMultidata(){
    return axios({
        url: '/login/'
    })
}

