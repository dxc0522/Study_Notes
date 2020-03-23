import telnetlib
import requests
from lxml import etree
import os
from fake_useragent import UserAgent


class get_proxy_ip:
    def __init__(self):
        self.url = ["https://www.kuaidaili.com/free/inha/",
                    "https://www.xicidaili.com/nn/"]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }

    def start_request(self):
        for item in self.url:
            for index in range(1, 100):
                response = etree.HTML(requests.get(item+str(index), headers = self.headers).content.decode()).xpath("//tbody/tr")
                for html_item in response:
                    try:
                        item_ip = html_item.xpath(".//td[@data-title='IP']/text()")
                        item_port = html_item.xpath(".//td[@data-title='PORT']/text()")
                    except IOError:
                        item_ip = html_item.xpath(".//td[0]/text()")
                        item_port = html_item.xpath(".//td[1]/text()")
                    
                        
                    self.test_ip(item_ip[0], item_port[0])

    def test_ip(self, ip, port):
        try:
            telnetlib.Telnet(ip, port, timeout=2)
            f=open('有效ip.txt','r',encoding='utf-8').read()
            if ip not in f:
                print("代理ip有效！",ip)
                with open('有效ip.txt','a') as file_handle:   # .txt可以不自己新建,代码会自动新建
                    file_handle.write(ip+" "+port)     # 写入
                    file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
            else :
                print("已存在！")
        except:
            print("ip无效！")


get_proxy_ip().start_request()