# coding=utf-8
import requests
from lxml import etree
import os
import sys
import you_get
from fake_useragent import UserAgent
import re
from multiprocessing import Pool
import time


class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        self.href = "https://7v39.com"
        # 目录不存在创建，makedirs可以创建多级目录
        # if not os.path.exists("video"):
        #      os.makedirs("video")

    def get_channel(self):
        # 获取类目
        response = etree.HTML(requests.get(self.href, headers=self.headers).content.decode(
        )).xpath("//ul[@class='tags-list']/li/*")
        for channel_item in response:
            if channel_item.text:
                self.start_request(
                    channel_item.attrib["href"], "video/"+channel_item.text+"/")

    def start_request(self, href, path):
        # 获取列表分页
        response = requests.get(self.href+href, headers=self.headers)
        totalpage = int(etree.HTML(response.content.decode()).xpath(
            "//ul[@class='pagination']/li[last()-2]/a/text()")[0])
        for i in range(1, int(totalpage)):
            if i == 1:
                item_response = requests.get(
                    self.href+href, headers=self.headers)
            else:
                item_response = requests.get(
                    self.href+href+"/index_"+str(i)+".html", headers=self.headers)

            self.list_data(item_response, path)

    def list_data(self, html, path):
        # 内容详情页操作
        page_list = etree.HTML(html.content.decode()).xpath(
            "//ul[@class='masonry']/li/@data-href")
        for href in page_list:
            if len(href) > 2:
                try:
                    item_response = requests.get(
                        self.href+href, headers=self.headers)
                    video_src = etree.HTML(item_response.content.decode()).xpath(
                        "//a[@class='meihua_btn']/@href")[0]
                    video_name = etree.HTML(item_response.content.decode()).xpath(
                        "//h1[@class='article-title']/a/text()")[0]
                    if not os.path.exists(path+video_name+".mp4"):
                        self.blob_download(
                            self.href+href, path, video_name+".mp4")
                        # self.down_video(video_src,path+video_name+".mp4")
                        # self.you_get_download(self.href+href,path,video_name+".mp4")
                except:
                    print("出错了")

    def down_video(self, video_src, video_name):
        # 常规存储方式
        # print(str(UserAgent().random))
        response = requests.get(video_src, headers={
            'referer': 'https://7v39.com/',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }, timeout=10)
        if response.status_code == 200:
            print(video_name)
            try:
                with open(video_name, "wb") as f:
                    f.write(response.content)
                    f.flush()
            except:
                print("==========保存出错！==========")
        else:
            print("video status 404 ！！！！", video_src)

    def you_get_download(self, url, path, video_name):
        # you-get下载方式 太慢
        if not os.path.exists(path):
            os.makedirs(path)
        print(url)
        sys.argv = ['you-get', '-o', path, '-O', video_name, url]
        you_get.main()

    def blob_download(self, url, path, video_name):
        def is_ts(val):
            return "ts" in val

        def ts_download(ts_item):
            print(ts_item)
            try:
                res_video = requests.get(
                    base_url+"720kb/hls/"+ts_item, self.headers, timeout=10)
                if res_video.status_code == 200:
                    print(path+video_name[0:-4])
                    if not os.path.exists(path+video_name[0:-4]):
                        os.makedirs(path+video_name[0:-4])
                    with open(path+video_name[0:-4]+"/"+ts_item, "wb") as f:
                        f.write(res_video.content)
            except:
                print("download ts fail")

        response = requests.get(url, headers=self.headers,
                                timeout=10).content.decode()
        rIndex = response.find("m3u8")
        lIndex = response.find("vHLSurl")
        findStr = response[lIndex:rIndex+5]
        # target_url = re.compile('"(.*)"').search(findStr).group()
        target_url = self.txt_wrap_by('"', '"', findStr)
        # ts_urls only two type so we don't get
        # res_blob = requests.get(target_url, headers=self.headers,
        #                         timeout=10).content.decode().splitlines()
        # get m3u8 file url
        # ts_urls=str(res_blob[len(res_blob)-1])
        base_url = target_url[0:len(target_url)-10]
        # download ts file and conact all file
        res_ts = requests.get(base_url+"720kb/hls/index.m3u8",
                              headers=self.headers, timeout=10).content.decode().splitlines()
        res_ts = list(filter(is_ts, res_ts))
        # 创建进程池，执行10个任务
        pool = Pool(10)
        for i in res_ts:
            # ts_download(i)
            pool.apply_async(ts_download, (i,))  # 执行任务
        pool.close()
        pool.join()
        # 调用合并
        print("调用合并")
        time.sleep(5)
        # return
        # os.popen("copy /b mp4\\*.ts mp4\\new.mp4")
        # print('ok！处理完成')

    # def ts_download(self, ts_item):

    def txt_wrap_by(self, start_str, end, html):
        start = html.find(start_str)
        if start >= 0:
            start += len(start_str)
            end = html.find(end, start)
            if end >= 0:
                return html[start:end].strip()


spider = Spider()
spider.get_channel()
