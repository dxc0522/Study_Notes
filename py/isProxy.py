#! /usr/bin/env python
# -*- coding: utf-8 -*-
from futures.thread import ThreadPoolExecutor
import requests
import os
from bs4 import BeautifulSoup


class ProxyValidation(object):
    def __init__(self):
        self.session = requests.session()
        self.proxies = None
        self.timeout = 5
        self.time_interval = 2
        self.headers = {
            'content-type': 'charset=utf8',  # 解决response乱码
            "Accept": "text/html,application/xhtml+xml,"
                      "application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "Keep-Alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/55.0.2883.87 Safari/537.36",
        }
        path = os.path.join(os.getcwd(), "IP_OK.txt")
        path = os.path.abspath(path)
        self.file = open(path, "a+", encoding="utf-8")

    def get_status(self, url, proxies=None):
        """
        获取状态
        :param proxies:
        :param url: 访问地址
        :return: 返回response或False
        """
        response = self.session.get(
            url=url,
            headers=self.headers,
            proxies=proxies,
            timeout=self.timeout,
            # verify=False,
            # allow_redirects=False
        )
        if response.status_code == 200:
            return response
        else:
            print("ERROR: 网络连接失败！", url)
            return False

    @staticmethod
    def read_text():
        path = os.path.join(os.getcwd(), "IP.txt")
        path = os.path.abspath(path)
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines

    @staticmethod
    def parse_html(response):
        html = response.text
        soup = BeautifulSoup(html, "html5lib")
        results = soup.select("#result p")
        # print(results)
        ip_query = results[0].find("code").text
        ip_location = results[1].find("code").text
        geo_ip = results[2].text if len(results) >= 3 else None
        network_mode = results[3].text if len(results) >= 4 else None

        # print(ip_query, ip_location, geo_ip, network_mode)
        return ip_query, ip_location, geo_ip, network_mode

    def local_ip(self):
        """
        获取本机IP地址
        :return: ip
        """
        url = 'https://ip.cn/index.php?ip='
        response = self.get_status(url)
        if response:
            ip_query, ip_location, geo_ip, network_mode = self.parse_html(response)
            return ip_query
        else:
            return None

    def location(self, ip_port):
        """
        获取 ip:port 地址位置
        :param ip_port:
        :param ip_port: ip:port
        :return:
        """
        url = 'https://ip.cn/index.php?ip=' + ip_port
        response = self.get_status(url)
        if response:
            ip_query, ip_location, geo_ip, network_mode = self.parse_html(response)
            return ip_query, ip_location, geo_ip, network_mode
        else:
            print("获取所在地理位置失败！IP:PORT %s" % ip_port)
            return None, None, None, None

    def https_protocol(self, ip_port):
        """
        https protocol 验证
        :param ip_port:
        :return:
        """
        protocol = "https"
        url = 'https://ip.cn/index.php?ip='
        proxies = {
            'https': 'https://' + ip_port,
        }

        try:
            response = self.get_status(url, proxies)
            if response:
                return response, protocol
            else:
                return None, protocol
        except requests.exceptions.ProxyError:
            return None, protocol
        except requests.exceptions.ConnectTimeout:
            return None, protocol
        except requests.exceptions.SSLError:
            return None, protocol

    def http_protocol(self, ip_port):
        """
        http protocol 验证
        :param ip_port:
        :return:
        """
        protocol = "http"
        url = 'https://ip.cn/index.php?ip='
        proxies = {
            'http': 'http://' + ip_port,
        }

        try:
            response = self.get_status(url, proxies)
            if response:
                return response, protocol
            else:
                return None, protocol
        except requests.exceptions.ProxyError:
            return None, protocol
        except requests.exceptions.ConnectTimeout:
            return None, protocol
        except requests.exceptions.SSLError:
            return None, protocol

    def validation(self, ip_port, local_ip):
        # 获取 ip:port 地址位置, 可以在代理之后直接获取
        # ip_query, ip_location, geo_ip, network_mode = self.location(ip_port)
        # print(ip_query, ip_location, geo_ip, network_mode)

        https_response, https_protocol = self.https_protocol(ip_port)
        https = "https://" + ip_port
        if https_response:
            ip_query, ip_location, geo_ip, network_mode = self.parse_html(https_response)
            # print(ip_query, ip_location, geo_ip, network_mode)
            if ip_query != local_ip:
                print("验证成功! https: %s location: %s" % (https, ip_location))
                self.file.write(https + "," + ip_location + "\n")
            else:
                print("验证失败！https: %s" % https)
        else:
            print("验证失败！https: %s" % https)

        http_response, http_protocol = self.http_protocol(ip_port)
        http = "http://" + ip_port
        if http_response:
            ip_query, ip_location, geo_ip, network_mode = self.parse_html(http_response)
            # print(ip_query, ip_location, geo_ip, network_mode)
            if ip_query != local_ip:
                print("验证成功! http: %s location: %s" % (http, ip_location))
                self.file.write(http + "," + ip_location + "\n")
            else:
                print("验证失败！http: %s" % http)
        else:
            print("验证失败！http: %s" % http)

    def start_validation(self, local_ip):
        """
        启用线程池，进行抓数据
        :param local_ip:
        :return:
        """
        pool = ThreadPoolExecutor(4)  # 设置线程池大小，默认等于cpu核数
        lines = self.read_text()
        for line in lines:
            ip_port = line.strip()
            pool.submit(self.validation, ip_port, local_ip)  # 异步提交（只是提交需要运行的线程不等待）

        # 作用1：关闭进程池入口不能再提交了   作用2：相当于jion 等待进程池全部运行完毕
        pool.shutdown(wait=True)

    def main(self):
        local_ip = self.local_ip()  # 获取本机IP地址
        print("本机IP: %s" % local_ip)

        self.start_validation(local_ip)  # 文本验证

        self.file.close()


if __name__ == '__main__':
    proxy_val = ProxyValidation()
    proxy_val.main()