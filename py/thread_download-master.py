import sys
from ThreadDownload import *





def main():
    try:   
        Link = "https://dxc12345.gitee.io/dd_blog/media/4keep.mp4"
        file_path = 'new.mp4'
        thread_number = 10
        thread_number = int(thread_number)
        dl = Download(Link, file_path, thread_number)
        dl.download()
        print('\n开始下载!')
        show_process(dl)
        print('\r' + '下载中···（已下载' + '100%)', end='', flush=True)
        print('\n下载完成!')
    except Exception:
            print('Parameter Setting Error')
            sys.exit(1)

if __name__=='__main__':
        main()