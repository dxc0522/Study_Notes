import sys
import time
import requests
import multiprocessing
from multiprocessing import Pool
from fake_useragent import UserAgent
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url_str = 'https://www.baidu.com'
ua = UserAgent()


def open_url(proxy_ip):
    headers = {
        "user-agent": ua.random,
    }
    try:
        if bool(proxy_ip):
            requests.get(url=url_str, headers=headers,
                         proxies={
                             'http': proxy_ip,
                         }).content
        else:
            requests.get(url=url_str, headers=headers).content
        print("有效")
    except:
        print(proxy_ip, "无效")
        pass


if __name__ == "__main__":
    http_ip_arr = []
    with open('ip_proxies_valid.txt', 'r') as f:
        for ip in f.readlines():
            if ip != None:
                # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
                http_ip_arr.append(ip.strip("\n"))
    f.close()
    time.sleep(1)
    print("开始验证!")
    # 这里只做简单演示请求,单次延时访问,并发可以使用asyncio,aiohttp
    p = Pool(15)
    for item_proxy in http_ip_arr:
        p.apply_async(open_url, (item_proxy,))
        # open_url(item_proxy)
    p.close()
    p.join()
    sys.exit(0)
    print("执行结束")
