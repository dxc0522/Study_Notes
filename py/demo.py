import requests
import os
import time
from multiprocessing import Pool

def run(i):
    url = 'https://cn1.chinapellets.com/hls/20190406/ae64c4b38a00fb989546672c7d75c660/1554536039/film_0%04d.ts'%i
    print("开始下载："+url)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
    r = requests.get(url, headers = headers)
    # print(r.content)
    with open('./mp4/{}'.format(url[-10:]),'wb') as f:
        f.write(r.content)

def merge(t,cmd):
    time.sleep(t)
    res=os.popen(cmd)
    print(res.read())



# if __name__ == '__main__':
#     # 创建进程池，执行10个任务
#     pool = Pool(10)
#     for i in range(2790):
#         pool.apply_async(run, (i,)) #执行任务
#     pool.close()
#     pool.join()
#     #调用合并
#     merge(5,"copy /b mp4\\*.ts mp4\\new.mp4")
#     print('ok！处理完成')

path = "./video/国产自拍/萝莉主播臭弟弟你要乖乖就给你看鲍鲍"
# os.popen("copy /b "+path+"\\*.ts mp4\\"+path+".mp4")
os.popen("copy "+path+"/*.ts "+path+".mp4")