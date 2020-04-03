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
from proxy_requst import use_proxy_requst
import ffmpeg


class Spider(object):
    def __init__(self):
        self.href = "https://7v39.com"
        # 目录不存在创建，makedirs可以创建多级目录
        # if not os.path.exists("video"):
        #      os.makedirs("video")

    def get_channel(self):
        # * 获取类目
        response = etree.HTML(use_proxy_requst(self.href).content.decode(
        )).xpath("//ul[@class='tags-list']/li/*")
        for channel_item in response:
            if channel_item.text:
                self.start_request(
                    channel_item.attrib["href"], "video/"+channel_item.text+"/")

    def start_request(self, href, path):
        # *获取列表分页
        totalpage = int(etree.HTML(use_proxy_requst(self.href+href).content.decode()).xpath(
            "//ul[@class='pagination']/li[last()-2]/a/text()")[0])
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(1, int(totalpage)):
            if i == 1:
                item_response = use_proxy_requst(self.href+href)
            else:
                item_response = use_proxy_requst(
                    self.href+href+"/index_"+str(i)+".html")

            self.list_data(item_response, path)

    def list_data(self, html, path):
        # *内容详情页操作
        page_list = etree.HTML(html.content.decode()).xpath(
            "//ul[@class='masonry']/li/@data-href")
        path = path.replace(" ", "")
        pool = Pool(moreThread)
        for href in page_list:
            if len(href) > 2:
                item_response = use_proxy_requst(self.href+href)
                video_src = etree.HTML(item_response.content.decode()).xpath(
                    "//a[@class='meihua_btn']/@href")[0]
                video_name = etree.HTML(item_response.content.decode()).xpath(
                    "//h1[@class='article-title']/a/text()")[0].replace(" ", "")
                if not os.path.exists(path+video_name+".mp4"):
                    # todo 直接下载可用
                    # self.down_video(video_src, path+video_name+".mp4")
                    pool.apply_async(
                        self.down_video, (video_src, path+video_name))
        pool.close()
        pool.join()

    def down_video(self, video_src, url, path, video_name):
        # *常规存储方式
        response = use_proxy_requst(video_src)
        if response.status_code == 200:
            print(video_name+"完成")
            try:
                with open(video_name+".mp4", "wb") as f:
                    f.write(response.content)
                    f.flush()
            except:
                print("==========保存出错！==========")
        else:
            print("正常下载出错！")
            # todo m3u8破解下载
            self.blob_download(
                url, path, video_name)

    def you_get_download(self, url, path, video_name):
        # *you-get下载方式 太慢
        try:
            sys.argv = ['you-get', '-o', path, '-O', video_name+".mp4", url]
            you_get.main()
        except:
            print("you-get 下载失败")

    def blob_download(self, url, path, video_name):
        def is_ts(val):
            return "ts" in val

        def ts_download(ts_item):
            try:
                if not os.path.exists(path+video_name+"/"+ts_item):
                    res_video = use_proxy_requst(base_url+"720kb/hls/"+ts_item)
                    if res_video.status_code == 200:
                        if not os.path.exists(path+video_name):
                            os.makedirs(path+video_name)
                        with open(path+video_name+"/"+ts_item, "wb") as f:
                            f.write(res_video.content)
            except:
                print("download ts fail")

        response = use_proxy_requst(url).content.decode()
        rIndex = response.find("m3u8")
        lIndex = response.find("vHLSurl")
        findStr = response[lIndex:rIndex+5]
        target_url = self.txt_wrap_by('"', '"', findStr)
        #  ts_urls only two type so we don't get
        # res_blob = requests.get(target_url, headers=self.headers,
        #                         timeout=10).content.decode().splitlines()
        # * get m3u8 file url
        base_url = target_url[0:len(target_url)-10]
        # * 判断是否存在ffmpeg
        b = 1
        if not isHasffmpeg:
            # download ts file and conact all file
            res_ts = use_proxy_requst(
                base_url+"720kb/hls/index.m3u8").content.decode().splitlines()
            res_ts = list(filter(is_ts, res_ts))
            # 创建进程池，执行10个任务
            # Thread = Pool(moreThread)
            for i in res_ts:
                ts_download(i)
            # Thread.apply_async(ts_download, (i))  # 执行任务
            # Thread.close()
            # Thread.join()
            # 调用合并
            print("调用合并")
            try:
                b = os.system("copy /b %s/*.ts %s.mp4",
                              (path+video_name, path+video_name))
            except:
                print("调用合并失败")
            else:
                os.system("rmdir /s/q %s", (path+video_name))

        else:
            b = os.system("ffmpeg -i %s -acodec copy -vcodec copy -absf aac_adtstoasc %s.mp4" %
                          (base_url+"720kb/hls/index.m3u8", path+video_name))
            # b = os.system("ffmpeg -i %s -c copy  %s.mp4" %
            #               (base_url+"720kb/hls/index.m3u8", path+video_name))

        if b == 0:
            print(video_name[0:-4]+'下载完成')
        else:
            print('m3u8')
            if isHasyou_get:
                # todo you_get下载方式
                self.you_get_download(url, path, video_name)

    def txt_wrap_by(self, start_str, end, html):
        start = html.find(start_str)
        if start >= 0:
            start += len(start_str)
            end = html.find(end, start)
            if end >= 0:
                return html[start:end].strip()


if __name__ == "__main__":
    moreThread = 10  # ! 线程数
    isHasffmpeg = True  # ! 是否安装ffmpeg
    isHasyou_get = True  # ! 是否安装you-get
    spider = Spider()
    spider.get_channel()
