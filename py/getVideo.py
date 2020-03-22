#coding=utf-8
import requests
from lxml import etree
import os

class Spider(object):
    def __init__(self):
        # 反反爬虫措施，加请求头部信息
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Referer": "https://7v39.com/s/qunjiaopapa/"
        }
        self.href="https://7v39.com/s/qunjiaopapa/"
        # 目录不存在创建，makedirs可以创建多级目录
        if not os.path.exists("video"):
             os.makedirs("video")
    def start_request(self):
        response = requests.get(self.href, headers=self.headers)
        totalpage=int(etree.HTML(response.content.decode()).xpath("//ul[@class='pagination']/li[last()-2]/a/text()")[0])
        for i in range(1,int(totalpage)):
            print("***************%s******************"%(i))
            if i==1:
                item_response=requests.get(self.href,headers=self.headers)
            else:
                item_response=requests.get(self.href+"index_"+str(i)+".html",headers=self.headers)
                
            self.list_data(item_response)
    def list_data(self,html):
        page_list=etree.HTML(html.content.decode()).xpath("//ul[@class='masonry']/li/@data-href")
        for href in page_list:
            try :
                item_response=requests.get("https://7v39.com"+href,headers=self.headers)
                video_src=etree.HTML(item_response.content.decode()).xpath("//a[@class='meihua_btn']/@href")[0]
                video_name=etree.HTML(item_response.content.decode()).xpath("//h1[@class='article-title']/a/text()")[0]
                if not os.path.exists("video/"+video_name+".mp4"):
                    self.down_video(video_src,video_name)
            except:
                print("出错了")
    def down_video(self,video_src,video_name):
        response = requests.get(video_src, headers=self.headers)
        # 3. 存储视频
        if response.status_code==200:
            print(video_name)
            print(video_src)
            try:
                with open("./video/"+video_name+".mp4", "wb") as f:
                    f.write(response.content)
                    f.flush()
            except:
                print("==========保存出错！==========")
        else:
            print("保存链接有误！")
 
 
spider = Spider()
spider.start_request()