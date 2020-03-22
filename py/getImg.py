import requests
from lxml import etree
import os
 
class Spider(object):
    def __init__(self):
        # 反反爬虫措施，加请求头部信息
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/xinggan/"
        }
        if not os.path.exists("img"):
        # 目录不存在创建，makedirs可以创建多级目录
             os.makedirs("img")
    def start_request(self):
        # 1. 获取整体网页的数据 requests
        for i in range(0, 500):
            print("==========正在抓取%s页==========" % i)
            response = requests.get("https://www.mzitu.com/page/"+ str(i) + "/", headers=self.headers)
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)
 
    def xpath_data(self, html):
        # 2. 抽取想要的数据 标题 图片 xpath
        alt_list = html.xpath('//ul[@id="pins"]/li/a/img/@alt')
        hrefs_list = html.xpath('//ul[@id="pins"]/li/a/@href')
        for href,alt in zip(hrefs_list,alt_list):
            if not os.path.exists("img/"+alt):
                os.makedirs("img/"+alt)
            item_responset=requests.get(href,headers=self.headers)
            item_totalpage=int(etree.HTML(item_responset.content.decode()).xpath("//div[@class='pagenavi']/a[last()-1]/span/text()")[0])
            print(item_totalpage)
            for i in range(1,item_totalpage):
                if not os.path.exists("img/"+alt+str(i)+".jpg"):
                    self.down_img(alt,href+"/"+str(i),alt+str(i))
    def down_img(self,alt,href,item_name):
        try:
            item_responset=requests.get(href,headers=self.headers)
            item_src=etree.HTML(item_responset.content.decode()).xpath("//div[@class='main-image']/p/a/img/@src")
            response = requests.get(item_src[0], headers=self.headers)
            print("正在抓取图片：" + item_name)
            # 3. 存储数据 jpg with open
            with open("./img/"+alt+"/"+item_name+".jpg", "wb") as f:
                f.write(response.content)
        except:
            print("==========文件名有误！==========")
 
 
spider = Spider()
spider.start_request()