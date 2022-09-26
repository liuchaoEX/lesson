'''
# 导入urlopen函数
from urllib.request import urlopen
url='http://www.baidu.com'
resp=urlopen(url)
# print(resp.status)
# print(resp.getcode())
# print(resp.read().decode('utf8'))
# 保存在本地
with open('D:/mybaidu.html','wb')as f:
    f.write(resp.read())
print('The End')
'''

'''
将远程数据下载到木地urlretrieve0
impor turllib.request
url1ib.request.urlretrieve(url,filename=.None，reporthook=None，data=None)
函数返回一个二元组〈filename指定的本地文件，用来存储url的网络资源，headersi,k%用urlopen后返回的对象再调用info()方
法后的返回值〈主要用于远程对象〉）
filenname：木地路径，未设定则生成临时文件
reporthook：回调函数（可以显小当前前的下载进度）
data：指post到服务器的数据
以抓取百度首页为例
'''

'''
from urllib import request
def fun(blocknum,blocksize,totlesize):
    percent=blocknum*blocksize/totlesize
    if percent>1.0:
        percent=1.0
    percent*=100
    print('Download:%.2f%%'%(percent))
url='http://www.baidu.com'
path='D:\mybaidu.html'
request.urlretrieve(url,path,fun)
'''

# URL的编码和解码
# JSON：三种格式
# l.简单形式：JS中的基础数据类型
# 2．对象形式：JS中的对象
'''
{
"name":"Li",
"age":18,
"hobby":["听音乐"]
"}
'''


'''
from unittest import result
from urllib import parse,request
url='http://www.baidu.com'
dict_data={'wd':'百度翻译'}
'''
# unlencode 转化字典
# url_data=parse.urlencode(dict_data)
# print(url_data)
# str_1='你好爬虫！'
# quote 对字符串进行编码
# ru_1=parse.quote(str_1)
# print(ru_1)

# unquote 对url进行解码
# re_2=parse.unquote(ru_1)
# print(re_2)
# parse.unquote()

'''urllib.parse  解析url  urlsplit'''

# from urllib import parse
# url='http://www.youdao.com/s?username=spider'
# result=parse.urlparse(url)
# print(result)

import urllib.request
import urllib.parse
url='http://www.runoob.com/?s='
keyword='Python教程'
key_code=urllib.request.quote(keyword)
url_all=url+key_code
hea={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
}
requ=urllib.request.Request(url,headers=hea)
resp=urllib.request.urlopen(requ)
# print(resp.read())
fp=open('D:\mybaidu.html','wb')
fp.write(resp)
fp.close()
print('over')