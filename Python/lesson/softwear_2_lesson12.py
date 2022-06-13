# 文件基础
# 编码
# encode()
# print('软件技术'.encode('UTF-8'))
# print('软件技术'.encode('GBK'))

# 解码
# decode()
# print(b'\xc8\xed\xbc\xfe\xbc\xbc\xca\xf5'.decode('GBK'))

# 文件读写
# 读取
# myfile=open(filename[,mode])
# 相对路径:
# 地址(路径)：相对路径、绝对路径(文件位置+名称.后缀名)

# 打开模式
# r （读模式，默认模式，可省略）
# w （写模式，若文件已存在，则清空原有内容）
# a （写模式，若文件已存在，会进行内容的追加，在末尾的位置）
# b （二进制模式，可与其他模式混合使用）
# t （文本模式，默认，可省略）
# + （读、写模式，与其他模式混用）

# myfile=open('D:\Code\Python\txt\ceshi.txt','r')
# print(myfile)
# 文件的关闭
# 文件名.close()
# myfile.close()
# with语句
# with open('filename'[,mode]) as f:
#     执行语句
# with open('D:\Code\Python\txt\ceshi.txt')as f:
#     content=f.read()
#     print(content)

# 文件对象常用方法
# close()写入并关闭
# flush()写入不关闭
# read([size])读取size个字符/字节，如size省略则读取全部
# readline()从文本文件中读取一行内容作为返回结果
# readlines()从文本文件中的每一行文本作为一个字符串存入列表中，返回列表结果
# seek()把文件指针移动到新的字节位置，为0时表示从头开始
# tell()返回文件指针的当前位置
# weite(s)将s的内容写入文件
# weitelies(s)把字符串列表写入文本文件，不添加换行符

# 向文本文件写入内容
# s='文本文件的读取方法\n文本文件的写入方法\n'
# f=open('D:\Code\Python\txt\ceshi.txt','w')
# f.write(s)
# f.close()

# with open('D:\Code\Python\ceshi.txt','w',encoding='utf-8')as f:
#     f.write(s)

# 读取文本文件中的内容
# f=open('D:\python.txt','r')
# print(f.read(10))
# print(f.tell()) 
# f.seek(0)
# print(f.tell())
# print(f.read())
# f.close()
# 采用csv格式对数据文件进行操作
# with open('D:\\test.csv','r',encoding='UTF-8',newline='')as f:
#     for line in f:
#         line=line.replace('\n','')
#         lst=line.split(',')
#         lns=''
#         for s in lst:
#             lns+='{}\t'.format(s)
#         print(lns)
# lst=['深圳','101.5','126.6','104.3']
# with open ('D:\\test.csv','a+',encoding='utf-8')as f:
#     f.write(','.join(lst)+'\n')

# f=open('D:\Code\Python\my_file.txt',encoding='utf-8')
# print(f.read())
# f.close()



f1=open('D:\\Code\\Python\\txt\\scores.txt','r',encoding='UTF-8')
content=f1.readlines()
f1.close()
# print(file_lines)

for i in content:
    data=i.split()
    sum=0
    for zf in data[1:]:
        sum=sum+int(zf)
    result=data[0]+str(sum)
    print(result)
    