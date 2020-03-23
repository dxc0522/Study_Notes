#coding=utf-8
import requests
from lxml import etree
import os
import sys
import you_get
from fake_useragent import UserAgent

class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        self.href="https://7v39.com"
    def get_channel(self):
        # 获取类目
        response = etree.HTML(requests.get(self.href, headers=self.headers).content.decode()).xpath("//ul[@class='tags-list']/li/*")
        for channel_item in response :
             if channel_item.text:
                self.start_request(channel_item.attrib["href"],"video/"+channel_item.text+"/")
    def start_request(self,href,path):
        # 获取列表分页
        response = requests.get(self.href+href, headers=self.headers)
        totalpage=int(etree.HTML(response.content.decode()).xpath("//ul[@class='pagination']/li[last()-2]/a/text()")[0])
        for i in range(1,int(totalpage)):
            if i==1:
                item_response=requests.get(self.href+href,headers=self.headers)
            else:
                item_response=requests.get(self.href+href+"/index_"+str(i)+".html",headers=self.headers)
                
            self.list_data(item_response,path)
    def list_data(self,html,path):
        # 内容详情页操作
        page_list=etree.HTML(html.content.decode()).xpath("//ul[@class='masonry']/li/@data-href")
        for href in page_list:
            if len(href)>2:
                try :
                    item_response=requests.get(self.href+href,headers=self.headers)
                    video_src=etree.HTML(item_response.content.decode()).xpath("//a[@class='meihua_btn']/@href")[0]
                    video_name=etree.HTML(item_response.content.decode()).xpath("//h1[@class='article-title']/a/text()")[0]
                    if not os.path.exists(path+video_name+".mp4"):
                        self.down_video(video_src,path+video_name+".mp4")
                        # self.you_get_download(self.href+href,path,video_name+".mp4")
                except:
                    print("出错了")
    def down_video(self,video_src,video_name):
        # 常规存储方式
        # print(str(UserAgent().random))
        response = requests.get(video_src, headers={
            'referer': 'https://7v39.com/',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        },timeout=10)
        if response.status_code==200:
            print(video_name)
            try:
                with open(video_name, "wb") as f:
                    f.write(response.content)
                    f.flush()
            except:
                print("==========保存出错！==========")
        else:
            print("video status 404 ！！！！",video_src)
    def you_get_download(self,url, path,video_name):
        # you-get下载方式
        if not os.path.exists(path):
            os.makedirs(path)
        print(url)
        sys.argv = ['you-get', '-o', path,'-O',video_name, url]
        you_get.main()
 
spider = Spider()
spider.get_channel()