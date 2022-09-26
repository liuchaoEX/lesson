# Python 基础语法
# print()语句
# print(123,'网络爬虫','34+12')
# '+'


# def math_1(x,y):
#     z=3*x+y
#     return z
#     print (z)

# print(math_1(3,5))
# math_1(6,9)

# def cs(a,b):
#     a=5
#     b=6
#     c=a+b
# def cs_1(b,d):
#     d=7
#     e=d+b
# print(cs)
# print(cs_1)

# a = input('请输入数字:')
# if a == '1':
#     print('星期一')
# elif a == '2':
#     print('星期二')
# elif a == '3':
#     print('星期三')
# elif a == '4':
#     print('星期四')
# elif a == '5':
#     print('星期五')
# elif a == '6':
#     print('星期六')
# elif a == '7':
#     print('星期日')
# else:
#     print('数字无效')


# a = int(input("请输入一个1-7的数字:"))
# b = ["星期1","星期2","星期3","星期4","星期5","星期6","星期天"]
# print(b[a-1]) 


# num = '1234567'
# week = '一二三四五六七'
# a = input("请输入任意数字1~7中的一个：")
# if a in num:
#   b = week[num.index(a)]
#   print("星期{}".format(b)) 

# import random
# md=['张惠妹','周杰伦','孙燕姿','蔡依林']
# dianming=random.choice(md)
# print(dianming)

# b=random.random()
# print()
# import random
# a =random.randint(1,1000)
# num=0
# while True:
#     try:
#         b=eval(input('请输入一个整数（1到1000）：'))
#     except:
#         print("输入有误")
#         continue
#     num=num+1
#     if  int(b)<=0:
#         print("输入有误")
#         break
#     elif type(b)!=type(123):
#         print("输入有误")
#         break
#     elif b>a:
#          print('猜大了')
#     elif  b<a:
#         print('猜小了')   
#     else:
#         print('猜对了')
#         break
# print("本轮的猜测次数是：",num) 

# import random
# a=random.randint(1,10)
# for i in range(1,4):
#     m=eval(input('请输入一个整数：'))
#     if m==a:
#         print('恭喜，猜对了，一共猜了{}次'.format(i))
#         break
#     elif m<a:
#         print('猜小了')
#     else:
#         print('猜大了')
# else:
#     print('游戏结束！')
# print('系统生成随机数为%d' %a)
'''随机生成密码'''
import random
txt='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_1=list(txt)
for i in range(10):
    a=''
    for i in range(8):
        a=random.choice(list_1)+a
    print(a)



# ss_1='abcdefghijklmnopqrstuvwxyz'
# ss_2=ss_1.upper()
# ss_3='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ss_3.lower()
# print(ss_2)