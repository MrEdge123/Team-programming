import {request} from './request'

export function getProblemListMultiData(){
    return request({
      url: 'getproblemlist',
      method: 'post',
      params: []
    })
}

