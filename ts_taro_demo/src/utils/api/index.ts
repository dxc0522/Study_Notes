import { get, post } from './requst'

export const test = (params?: object): any => get("index/getBanners", params);