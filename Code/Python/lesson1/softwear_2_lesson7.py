# 函数
# y=3x=5
# 自定义函数、调用函数
# 自定义函数语法格式:
# def 函数名(形式参数):
#     函数执行体语句序列
#     return[表达式]
# 定义一个函数，传入一个字符串作为参数，并将该字符串打印输出


# def print_str(str1):
#     print(str1)
#     return

# 定义一个函数，传入两个整数参数，并将两数相加的结果打印输出
# def print_sum(a,b):
#     c=a+b
#     print(c)
#     return c

# 函数的调用
# 常规调用
# 函数名(实际参数)
# print_str('我是print_str函数打印的信息')
# print_sum(1949,70)
    
# 函数的别名
# Ps=print_str
# Ps('我是print_str函数的别名调用的！')


# 函数没有reture语句
# 不返回值的函数称为过程
# 定义一个过程，传入一个字符串参数，在该字符串两端加上*并输出






# 函数有多个return语句
# def whatisit(num):
#     if num>0:
#         return '正数'
#     if num<0:
#         return '负数'
#     if num==0:
#         return '零'
# str=whatisit(100)
# print(str)
# str=whatisit(-100)
# print(str)
# str=whatisit(0)
# print(str)



# 定义一个累加函数add，带有两个参数
# def add(x,y):
#     z=x+y
#     print (z)
# add(3,7)



# 函数的参数类型
# 可变与不可变类型
# 传递可变类型实例
# def test_list(list1):
#     list1.append([10,20,30])
#     print('函数内部的值：',list1)
#     return

# list1=[1,2,3]
# test_list(list1)
# print('函数外部的值：',list1)

# 参数传递方式
# 位置参数
# def menu(zhushi,xiaocai):
#     print('一份主食：',zhushi)
#     print('一份小菜：',xiaocai)
#     # return zhushi,xiaocai
# menu('牛肉面','凉拌三丝')
# menu('话梅花生','蛋炒饭')


# print(list(range(10,2,0)))


# 关键字参数
# def menu(zhushi,xiaocai):
#     print('一份主食：',zhushi)
#     print('一份小菜：',xiaocai)
#     return zhushi,xiaocai
# menu('牛肉面','凉拌三丝')
# menu(xaiocai='话梅花生',zhushi='蛋炒饭')

# 默认参数
# def menu(zhushi,xiaocai,tianpin='绿豆沙'):
#     print('一份主食：',zhushi)
#     print('一份小菜：',xiaocai)
#     print('一份甜品：',tianpin)
#     # return zhushi,xiaocai,tianpin
# menu('牛肉面','凉拌三丝')
# menu('话梅花生','蛋炒饭','大麦茶')

# 不定长参数:只占用用一个参数，以*开头的参数名
# arg=[0,10,2]
# L=list(range(*arg))
# print(L)
# print('python',123,'78+9','变成课程')

# def user(username,age,**kwargs):
#     print('username:',username,'age:',age,'other:',kwargs)
# user('jone',27,city='guangzhou',job='Data Analyst')

# 定义函数的参数中包含有默认参数nationality
# def reg_user(name,sex,age,nationality='中国'):
#     print(f'{name}({nationality},{sex},{age})')
# reg_user('小丽','女',18)
# reg_user('小强','男',18,'印度')


# 定义一个可以传入不定数量参数的函数
# def add_int(*args):
#     result=0
#     for x in args:
#         result += x
#     print(result)
#     return result
# add_int(1,2,3,4,5)
# add_int(10,15,20)


# 变量的作用域
# 局部变量
# totle=0# 全局变量
# def mul(a1,a2):
#     global totle
#     totle=a1*a2 #局部变量
#     print('函数内部局部变量totle值是：',totle)
#     return totle
# mul(5,4)
# print('函数外部全局变量totle值是：',totle)

# global可以将局部变量声明为全局变量

# 红包游戏
# 给定红包的总金额和红包发放数量，模拟一个抢红包的游戏
# 红包总金额totle 红包发放数量num
# 限定红包最低金额为1元，且为整数金额，则每个红包能够抢到的金额范围[1,totle-以抢金额-剩余红包数*1]
import random
def fahongbao(totle,num):
    # 记录每个红包的金额
    eachone=''
    # 记录已发红包，初始为0
    already=0
    # 为num-1人随机分配金额
    for i in range(1,num):
        # 至少给剩下的人每人留1元钱
        hb=(random.uniform(0.01,(totle-already)-(num-i)*0.01),2)
        # 每个红包金额转成字符串并积累保存
        eachone=eachone+str(round((totle-already),2))
        # 已发红包累计金额
        already=already+hb
    #将剩余所有的金额发给最后一个人 
    eachone=eachone+str(totle-already)
    return eachone
# 修改最低金额为0.01元，且可以是非整数，上述代码如何修改

totle=20
num=5
for i in range(10):
    eachone=fahongbao(totle,num)
    print(eachone)

# random.randint(a,b)生成