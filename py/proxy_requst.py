import requests
import random
from fake_useragent import UserAgent

ua = UserAgent()
http_ip_arr = []
with open('ip_proxies_valid.txt', 'r') as f:
    for ip in f.readlines():
        if ip != None:
            # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
            http_ip_arr.append(ip.strip("\n"))
f.close()


def use_proxy_requst(url, Referer=""):
    proxyIp = random.choice(http_ip_arr)
    # print("访问：%s 代理IP：%s" % (url, proxyIp))
    try:
        response = requests.get(
            url, headers={
                'Connection': 'close',
                "User-Agent": ua.random,
                "Referer": Referer
            }, proxies={
                'http': proxyIp,
                # 'https': proxyIp,
            })
        # }, verify=False)
        return response
    except BaseException as e:
        print(e)
