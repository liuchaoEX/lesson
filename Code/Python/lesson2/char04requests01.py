# reqquests库 第三方库
# pip install 库名
# pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple/
import requests
# url='http://www.cqepc.cn/'
# res=requests.get(url)
# print(res)
# res=requests.get("http://www.cqepc.cn/")
# print(res.text)

# import urllib.request
# url='http://www.baidu.com/'
# resp=urllib.request.urlopen(url)
# print(resp.getcode())
# print(resp.read())
# 获取该网址前800个字，在终端显示即可
# url_1='http://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md'
# res=requests.get(url_1)
# print(res.status_code)
# print(res.text[:800])
# url='https://www.sogou.com/web?query=刘德华'
# dic={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'}
# res=requests.get(url,headers=dic)
# print(res.text)

url='https://www.baidu.com/'
dict_1={"pwd":"cat"}
res=requests.post(url,data=dict_1)
# print(res.text)
print(res.json())
