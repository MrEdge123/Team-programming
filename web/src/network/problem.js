import {request} from './request'

export function getProblemListMultiData(){
    return request({
        URL: '/getproblemlist/',
        method: 'get'
    })
}

export function testPost() {
    const data = {}
    return request({
        method: 'post',
        URL: '',
        datatype:'json',data
    })
}
