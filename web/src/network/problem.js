import {request} from './request'

export function getProblemMultiData(){
    return request({
        url: '/getDataList/'
    })
}

