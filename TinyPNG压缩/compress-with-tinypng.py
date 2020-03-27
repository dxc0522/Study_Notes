# -*- coding: utf-8 -*-

"""脚本功能说明：使用 tinypng api，一键批量压缩指定文件(夹)所有文件"""

import os
import sys
import tinify

tinify.key = "N2x6drKv3F2Cf7cms125YFL1DF779WQ7" # AppKey

def get_file_dir(file):
    """获取文件目录通用函数"""
    fullpath = os.path.abspath(os.path.realpath(file))
    return os.path.dirname(fullpath)

def check_suffix(file_path):
    """检查指定文件的后缀是否符合要求"""
    file_path_lower = file_path.lower()
    return (file_path_lower.endswith('.png')
            or file_path_lower.endswith('.jpg')
            or file_path_lower.endswith('.jpeg'))
def check_size(file_path):
	old_size = os.path.getsize(file_path)/1024
	return old_size>100

def compress_by_tinypng(input_file):
    """使用 tinypng 进行压缩，中文前面的 u 是为了兼容 py2.7"""
    if not check_suffix(input_file):
        print(u'只支持png\\jpg\\jepg格式文件：' + input_file)
        return
    # if not check_size(input_file):
    # 	print(u'只压缩大于100kb图片')
    # 	return

    file_name = os.path.basename(input_file)
    output_path = get_file_dir(input_file)
    output_file = os.path.join(output_path, file_name)
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    try:
        
        old_size = os.path.getsize(input_file)/1024
        print(u'压缩前文件大小：%d kb' % old_size)

        source = tinify.from_file(input_file)
        source.to_file(output_file)
        print(u'文件压缩成功：' + input_file)

        new_size = os.path.getsize(output_file)/1024
        print(u'文件保存地址：%s' % output_file)
        print(u'压缩后文件大小：%d kb' % new_size)
        print(u'压缩比： %d%%' % ((old_size - new_size) * 100 / old_size))
    except tinify.errors.AccountError:
        print(u'Key 使用量已超，请更新 Key，并使用命令[Usage] %s [filepath] [key]运行'
              % os.path.basename(sys.argv[0]))

def check_path(input_path):
    """如果输入的是文件则直接压缩，如果是文件夹则先遍历"""
    if os.path.isfile(input_path):
        compress_by_tinypng(input_path)
    elif os.path.isdir(input_path):
        dirlist = os.walk(input_path)
        for root, dirs, files in dirlist:
            for filename in files:
                compress_by_tinypng(os.path.join(root, filename))
    else:
        print(u'目标文件(夹)不存在，请确认后重试。')

if __name__ == '__main__':
    len_param = len(sys.argv)
    if len_param != 2 and len_param != 3:
        print('[Usage] %s [filepath]' % os.path.basename(sys.argv[0]))
    elif len_param == 3:
        tinify.key = sys.argv[2]
        check_path(sys.argv[1])
    else:
        check_path(sys.argv[1])