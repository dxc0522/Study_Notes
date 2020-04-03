import requests
from lxml import etree
import os
import time
from fake_useragent import UserAgent
from string import Template
from multiprocessing import Pool
import random
import urllib3
ua = UserAgent()

requests.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5
requests.session().keep_alive = False


def use_proxy_requst(url, Referer=""):
    proxyIp = random.choice(http_ip_arr)
    print("访问：%s 代理IP：%s" % (url, proxyIp))
    try:
        response = requests.get(
            url, headers={
                # 'Connection': 'close',
                "User-Agent": ua.random,
                # "Referer": Referer
            }, proxies={
                'http': proxyIp,
                # 'https': proxyIp,
            }, verify=False)
        return response
    except BaseException as e:
        print(e)


class Spider(object):
    def __init__(self):
        if not os.path.exists("img"):
            # 目录不存在创建，makedirs可以创建多级目录
            os.makedirs("img")

    def start_request(self):
        # *1. 获取整体网页的数据 requests
        for i in range(0, 500):
            print("==========正在抓取%s页==========" % i)
            pageUrl = "https://www.mzitu.com/xinggan/page/" + str(i) + "/"
            response = use_proxy_requst(
                pageUrl, "https://www.mzitu.com/xinggan/")
            html = etree.HTML(response.content.decode())
            time.sleep(3)
            self.xpath_data(html, pageUrl)

    def xpath_data(self, html, pageUrl):
        # *2. 抽取想要的数据 标题 图片 xpath
        alt_list = html.xpath('//ul[@id="pins"]/li/a/img/@alt')
        hrefs_list = html.xpath('//ul[@id="pins"]/li/a/@href')
        for href, alt in zip(hrefs_list, alt_list):
            if not os.path.exists("img/"+alt):
                os.makedirs("img/"+alt)
            item_responset = use_proxy_requst(href, pageUrl)
            time.sleep(3)
            item_totalpage = int(etree.HTML(item_responset.content.decode()).xpath(
                "//div[@class='pagenavi']/a[last()-1]/span/text()")[0])
            # print(alt+"共"+item_totalpage)
            print('%s共%s张' % (alt, item_totalpage))
            p = Pool(10)
            for i in range(1, item_totalpage):
                if not os.path.exists("img/"+alt+str(i)+".jpg"):
                    # self.down_img(alt, href+"/"+str(i), alt+str(i))
                    p.apply_async(
                        self.down_img, (alt, href+"/"+str(i), alt+str(i), pageUrl))
            p.close()
            p.join()

    def down_img(self, alt, href, item_name, pageUrl):
        # *下载图片
        try:
            item_responset = use_proxy_requst(href, pageUrl)
            item_src = etree.HTML(item_responset.content.decode()).xpath(
                "//div[@class='main-image']/p/a/img/@src")
            response = requests.get(item_src[0], headers={
                "User-Agent": ua.random,
                "Referer": pageUrl
            }, proxies={
                'http': proxyIp,
                'https': proxyIp,
            })
            print("正在抓取图片：" + item_name)
            # 3. 存储数据 jpg with open
            with open("./img/"+alt+"/"+item_name+".jpg", "wb") as f:
                f.write(response.content)
        except:
            print("==========文件名有误！==========")


if __name__ == "__main__":
    http_ip_arr = []
    with open('ip_proxies_valid.txt', 'r') as f:
        for ip in f.readlines():
            if ip != None:
                # 从文件中读取行数据时，会带换行符，使用strip函数去掉 换行符后存入列表
                http_ip_arr.append(ip.strip("\n"))
    f.close()
    spider = Spider()
    spider.start_request()
