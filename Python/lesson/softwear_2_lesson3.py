# print(123,'123','hao',3.14)
# NianLing=int(input('age:'))
# print(type(NianLing))
"""
a='3'
print(type(a))
b=int(a)
print(type(b))

print('今天\'是\'新的一周')
print('Let\'s go!')
print("Let's go")
import keyword
print(keyword.iskeyword('is'))"""
from re import T


Char='abcdefg'
# 提取单个 
# print(Char[5])
# print(Char[-2])
# 提取多个 
# 切片 str[开始索引位置:结束索引位置:步长]
# print(Char[::2])
# 创建一个0-99的数序列，任意取其中一段
L=list(range(100))
# print(L)
# 取前5个数
# print(L[:5])
# 取后5个数
# print(L[95:100])
# print(L[-5:]) 
# 取1-10的奇数
# print(L[1:11:2])
# 每隔5个取一个数
# print(L[0:100:5])
# print(L[::5])
# 复制序列
# print(L[::])
# print(L[:])
# 逆序
# print(L[::-1]) 
# 拼接
a='python'
# b='hello'
# print(b+a)
# 最终结果pythoy
# a[-1]='y'
# b=a[:-1]+'y'
# print(b)
# 运算符
pai=3.14
# 根据给定的半径，求取周长、面积
# r=float(input('请输入圆形的半径：'))
# C=2*pai*r
# S=pai*r**2
# print('半径为：'+str(r)+'周长为:'+str(C)+'面积为:'+str(S))
# print('半径为：%s，周长为：%s，面积为：%s'%(r,C,S))
# 格式化字符串：%s （字符串类型）%d（整数类型）%f（浮点数类型）
# print('半径为：{}，周长为：{}，面积为：{}'.format(r,C,S))
# 根据给定的面积，求取周长和半径
# S=float(input('请输入圆形的面积：'))
# r=round((S/pai)**0.5,1)
# C=2*pai*r
# print('面积为：{},半径为：{}，周长为：{}，'.format(S,r,C))

# 程序控制结构
# 条件语句与条件嵌套
# 程序基本结构：顺序结构（自上而下执行语句）、分支结构和循环结构
# 50min  21.7km 
# s=21.7*1000
# t=50
# v=s/t
# print(v)
# 分支结构
# 单分支、二分支、多分支、嵌套
# rain=True
# if rain:
#     print('记得带伞')
# 会员消费9.5折，非会员不打折，根据用户类型和消费金额，输出最后应付金额
# jine=float(input('请输入消费金额：'))
# huiyuan=input('请输入会员类型：1：会员，其他：非会员')
# if huiyuan=='1':
#     jine*=0.95
# print('用户应付款：{}'.format(jine))

# 二分支
# if 条件:
#     代码块1
# else:
#     代码块2
# 分数，60及分以上及格，否则不及格
# score=int(input('请输入分数：'))
# if score>=60:
#     print('及格')
#     if score>=85:
#         print('优秀')
#     else:
#         print('良好')
# else:
#     print('不及格')
#     if score>=40:
#         print('还能挽救一下')
#     else:
#         print('哎……')

# 复仇者联盟，蜘蛛侠，高中生，历史成绩60分以上为及格，否则不及格，40以下：学渣，
# 40-60，挽救一下，85以上，发放奖学金，60-85，表现还不错。history=26
# score=26
# if score>=60:
#     print('及格')
#     if score>=85:
#         print('发放奖学金')
#     else:
#         print('表现还不错')   
# else:
#     print('不及格')
#     if score<=40:
#         print('学渣')
#     else:
#         print('挽救一下')


score = int(input("请输入分数："))

if score>=60:
    print('及格')
    if score>=85:
        print('表现还不错')
        print('100亿万奖学金')
else:

    print('不及格')
    if score<=40:
        prin('学渣')
    else:
        print('挽救一下')












# 会员消费9.5折，非会员9.9，根据用户类型和消费金额，输出最后应付金额
# money=float(input('请输入消费金额：'))
# flag=input('请输入会员类型：1：会员，2：非会员')
# if flag=='1':
#     money*=0.95
# if flag=='2':
#     money*=0.99
# print('用户应付款：',format(money)) 

#coding:utf-8
# jine=float(input('请输入消费金额:'))
# huiyuan=input('请输入会员类型：1：会员，其他：非会员')
# if  huiyuan=='1':
#     jine*=0.95
# else:
#     jine*=0.99
# print('用户应付款:{}'.format(jine)) 

# 多分支结构
# if 条件:
#     代码块1
# elif 条件:
#     代码块2
# elif 条件:
#     代码块3
# elif 条件:
#     代码块4
# ……
# else:
#     代码块n
# 90以上为A，80以上为B，70以上为C，60以上为D，其余为E
# score=int(input('请输入分数：'))
# if score>=90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else:
#     print('E')

# 金卡会员消费9折，普通会员9.5，，非会员9.9折，根据用户类型和消费金额，输出最后应付金额
#coding:utf-8
# jine=float(input('请输入消费金额:'))
# huiyuan=input('请输入会员类型：1：普通会员，2：非会员,3:金卡会员')
# if  huiyuan=='1':
#     jine*=0.95
# elif huiyuan=='2':
#     jine*=0.99
# else:
#     jine*=0.9
# print('用户应付款:{}'.format(jine))  