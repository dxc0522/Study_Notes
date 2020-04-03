import requests
from lxml import etree
import time
from multiprocessing import Pool
import multiprocessing
import sys
from fake_useragent import UserAgent

ua = UserAgent()

get_proxy_arr = [
    {
        'name': "kuaidaili",
        'url': "https://www.kuaidaili.com/free/inha/"
    },
    {
        'name': "xicidaili",
        'url': "https://www.xicidaili.com/nn/"
    },
]
headers = {
    "user-agent": ua.random,
}
ip_list = []

# *爬取网址


def input_urls():
    for item in get_proxy_arr:
        print("正在爬取", item['url'])
        try:
            for i in range(1, 3):
                get_single(item, str(i))
                print('爬取第'+str(i)+'页\r', end="")
                time.sleep(3)
        except:
            print("异常退出")

# *摘录代理IP


def get_single(item, index):  # 爬出单页上的所有代理ip
    r = requests.get(item['url'] + index, headers=headers)
    if r.status_code == 503:
        print('由于爬取次数过多,你的Ip已经被封')
        sys.exit(0)
    content = etree.HTML(r.text)
    if item['name'] == "kuaidaili":
        ip = content.xpath(".//td[@data-title='IP']/text()")
        duankou = content.xpath(".//td[@data-title='PORT']/text()")
    elif item['name'] == "xicidaili":
        ip = content.xpath('//table[@id="ip_list"]/tr/td[2]/text()')
        duankou = content.xpath('//table[@id="ip_list"]/tr/td[3]/text()')
    for i in range(0, len(ip)):
        ip_list.append(ip[i]+":"+duankou[i])

# *验证代理ip


def verify_ips(ip, ip_valid_list):
    poxie = "http://"+ip
    proxies = {
        'http': poxie,
        'https': poxie
    }
    try:
        requests.get('https://www.baidu.com', headers=headers,
                     proxies=proxies, timeout=3)
        ip_valid_list.append(ip)
        print(ip, "有效")
    except:
        pass
        # print("IP失效")



if __name__ == "__main__":
    print(
        """
        程序结束后会在当前文件夹生成一个ip_proxies_valid.txt文件，
        防止ip被封,控制爬取频率
        """
    )
    mlist = multiprocessing.Manager()
    ip_valid_list = mlist.list()
    input_urls()
    print("总共爬取到"+str(len(ip_list))+"个ip,接下来准备验证ip有效性")
    print("验证倒计时3s")
    time.sleep(1)
    print("验证倒计时2s")
    time.sleep(1)
    print("验证倒计时1s")
    time.sleep(1)
    print("开始验证!")
    p = Pool(20)
    for ip in ip_list:
        p.apply_async(verify_ips, (ip, ip_valid_list))  # 多进程验证
    p.close()
    p.join()
    f = open('ip_proxies_valid.txt', 'a')
    for ip in ip_valid_list:  # 写入txt文件
        f.write(ip)
        if ip != ip_valid_list[-1]:
            f.write('\n')
    f.close()
    print("完成")
