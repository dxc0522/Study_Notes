
import Taro from "@tarojs/taro";

const baseUrl = "https://nzteexhimp.koyooo.com/api/";

export const baseOptions = (params: any, method: "GET" | "OPTIONS" | "HEAD" | "POST" | "PUT" | "DELETE" | "TRACE" | "CONNECT" | undefined = "GET"): object => {
    let { url, data } = params;
    let contentType = "application/x-www-form-urlencoded";
    contentType = params.contentType || contentType;
    const option = {
        isShowLoading: false,
        loadingText: "正在加载",
        url: baseUrl + url,
        data: data,
        method: method,
        header: { "content-type": contentType, },
        success(res: any) {
            return res.data;
        },
        fail(e: any) {
            return e;
        }
    };
    return Taro.request(option);
}
export const get = (url: string, data: object = {}): any => {
    return baseOptions({ url, data });
}
export const post = (url: string, data: object, contentType: string): any => {
    return baseOptions({ url, data, contentType }, "POST");
}
