from urllib.request import urlopen
url='http://www.cqepc.cn'
resp=urlopen(url)
print(resp.getcode())
with open('D:\I.html','wb')as f:
    f.write(resp.read())
    print("已经打印源代码完成")