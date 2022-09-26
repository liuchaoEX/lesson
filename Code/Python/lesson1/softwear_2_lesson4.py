# 循环结构
# for ：遍历循环，循环次数可以提前确定
# for <循环变量> in <遍历结构>:
#     <循环体>
# range():快速构造一个数字序列
# range(a,b,c) len
    # a='python'
    # print(len(a))
    # for i in range(0,6,2):
    #     print(i)
# for循环无法改变序列元素
    # L=[1,2,3]
    # for a in L:
    #     a+=1
    # print(L)
# for循环搭配range、len实现序列的更改
    # for i in range(len(L)):
    #     L[i]+=1
    # print(L)

# 输入一个小于1000的整数n，计算1+2+3+……+n的值
# n=eval(input('请输入一个小于1000的整数：'))
# s=0
# for i in range (1,n+1):
#     s+=i
# print(s)

# eval()
# print(eval('1+1'))
# a='[1,2,3,4,5]'
# print(eval(a))
# ff=eval(input('请输入浮点数：'))
# print(ff)
# print(type(ff))


# while
# while <条件表达式>:
#     <循环体>
# 输入一个小于1000的整数n，计算1+2+3+……+n的值
# s=0
# i=1
# n=eval(input('请输入一个小于1000的整数：'))
# while (i<=n):   
#     s+=i
#     i+=1
# print(s)
# count=0
# while count<5:
#     print(count,'is less than 5')
#     count+=1

# else:
#     print(count,'is not less than 5')

# 四种语句
# break：终止循环
# s=0
# while True:
#     s+=1
#     if s==6:
#         break
#     print(s)

# for i in range(0,10):
#     print(i)
#     if i==1:
#         break

# continue:跳出本次循环
# for i in range(0,5):
#     if i==1:
#         continue
#     print(i)

# s=3
# while s>0:
#     s-=1
#     if s==1:
#         continue
#     print(s)

# pass:空语句，保持程序结构完整性，占位

# if 5>3:
#     pass
# else:
#     pass

# for i in range(0,3):
#     if i==1:
#         pass
#         print('这是一个pass块')
#     print(i)

'''
猜数字游戏
要求系统随机生成一个1-100的数字，
有3次机会，
猜对输出“恭喜，猜对了，一共猜了x次”；
如果三次都没猜对，输出“游戏结束”
每次都会根据用户输入的值和随机数进行比较，并告知“猜大了”、“猜小了”
'''
# 随机生成
# 标准函数：random
# import random
# a=random.randint(1,100)
# 三次机会
# for i in range(1,4):
#     print('现在是第{}次机会'.format(i))
# 输出 print()
# 输入 input()
# 比较 比较运算符> < >= <= !=
# 如果 条件分支语句(if elif else)
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
#     print('系统生成随机数为%d' %a)

# i = 1
# import random
# SuiJiShu = int(random.randint(1, 10))
# while i <= 3:
#     i += 1
#     GuessNum = int(input('请输入猜测： '))
#     if GuessNum == SuiJiShu:
#         print('恭喜！！猜测正确')
#         print('系统生成随机数为%d' %SuiJiShu)
#         exit()
#     elif GuessNum > SuiJiShu:
#         print('大了')
#     else:
#         print('小了')
# print('系统生成随机数为%d' %SuiJiShu) 

# 求1-100的素数
import math
# x=1
# while x<100:
#     n=2
#     while n<x-1:
#         if x%n==0:
#             break
#         n+=1
#     else:
#         print(x,end='\\')
#     x+=1
# else:
#     print('over')

# for i in range(2,101):
#     n=int(math.sqrt(i))+1
#     for j in range(2,n):
#         if i%j==0:
#             break
#     else:
#         print(i,end=',')



# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}x{i}={i*j}\t', end='')
#     print() 

# print('hello',end='!')
# print('python')
# print('1x1=1')
# print('2x1=2  2x2=4')
# print('3x1=3  3x2=6  3x3=9')
# for i in range(1,10):
#     for j in range (1,i+1):
#         print('%d x %d = %d'%(j,i,i*j),end=' ')
#     print('')

# for i in range(1,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(j,i,i*j),end=' ')
#         if i ==j:
#             print('')
#             break

# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print('%d x %d = %d'%(j,i,i*j),end=' ')
#         j+=1
#     print('')
#     i+=1

# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print('{}*{}={}'.format(j,i,j*i),end = '\t')
#         j += 1
#     print()
#     i += 1 