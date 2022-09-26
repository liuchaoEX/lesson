# s='China is a beautiful country'
# print(s.split())
# jieba分词
# ss='中国是一个美丽的国家'
# print(ss.split())
# 第三方库的安装
# 阿里云： https://mirrors.aliyun.com/pypi/simple/
# 豆瓣：http://pypi.douban.com/simple/
# 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
# pip install +库名
# pip install -i 国内源地址 库名
# 导入库
# import jieba
# from *** import ***
# print(jieba.lcut(ss))
# 分词模式
    # 精确模式
    # 全模式
    # 搜索引擎模式
# 主要方法
    # cut(s)精确模式，返回可迭代的数据类型
    # cut(s,cut_all=True)全模式，输出s中所有可能的单词
    # cut_for_search(s)搜索引擎模式
    # luct(s)精确模式，返回列表类型
    # lcut(s,cut_all=True)全模式，返回列表类型
    # lcut_for_search(s)搜索引擎模式，返回列表类型
    # add_word(w)向分词词典中增加新词w
# s='中华人民共和国是一个美丽而伟大的国家'
# print(jieba.lcut_for_search(s))
# jieba.add_word('华大夫')
# print(jieba.lcut('华大夫正在行医治病'))

# 词频统计
# 英文词频统计:读取文件、大小写转换(统一)、去除特殊符号、词频统计

# def findText():
#     txt=open('D:\\Code\\Python\\my_file.txt').read()
#     txt=txt.lower()
#     for c in '~.,"!@#$%^&*()_-+={}[]\<>?':
#         txt=txt.replace(c,' ')
#     return txt
# ss=findText()
# words=ss.split()    
# # print(words)
# # 创建空字典，用于存放统计的词及次数
# counts={}
# for word in words:
#     counts[word]=counts.get(word,0)+1
# items=list(counts.items())
# # print(items)
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(10):
#     word,count=items[i]
#     print('{}:{}'.format(word,count))
# 中文词频统计
import jieba
exclude={'他们','一个','知道','不料','决定','立刻','泉水'}
txt=open('D:\\Code\\Python\\txt\\西游记之女儿国奇遇.txt').read()
words=jieba.lcut(txt)
# print(words)
counts={}
for word in words:
    if len(word)==1:
        continue
    # else:
    #     counts[word]=counts.get(word,0)+1
    elif word=='唐僧' or word=='师傅':
        rword='唐三藏'
    elif word=='大师兄' or word=='孙行者' or word=='猴哥' or word=='孙悟空':
        rword='悟空'
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in exclude:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print('{}:{}'.format(word,count))