# urllib库：内置HTTP请求库，无需单独安装
# 常用模块 ：request error parse robotpaeser
# 模块中的常用函数
# urlopen()
# 调用urllib库中的request模块
# 方法一：
# import urllib.request
# res_1=urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# 方法二：
# from urllib.request import urlopen 
# res_2=urlopen('url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None')

#输出网页https://docs.python.org/3/library/urllib.html源代码
# from urllib.request import urlopen 
# res_2=urlopen('https://docs.python.org/3/library/urllib.html')
# print(res_2.read().decode('utf-8'))

#扩展：输出指定长度的网页源代码（300个字符）？读取一行？逐行读取？？？
# readline() readlines()

# getcode()获取网页状态码，200正常，404异常
# status也可判断响应状态码，200正常，404异常
# from urllib.request import urlopen 
# res_2=urlopen('https://docs.python.org/3/library/urllib.html')
# print(res_2.getcode())
# print(res_2.status)

# 使用异常处理机制 try…except，当出现HTTPerror时，直接在终端返回404
import urllib.error
from urllib.request import urlopen 
try:
    url2=urlopen('https://docs.python.org/3/library/nourllib.html')
except urllib.error.HTTPError as e:
    if e.code==404:
        print(404)