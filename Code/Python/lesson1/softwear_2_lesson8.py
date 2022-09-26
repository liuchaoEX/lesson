# 项目实操二——工作量计算器小程序
# 项目大小、人数、工时
# 已知信息：1个标准项目(size：浮点数)，一个人(number：整数)，80个工时(time：浮点数)
# 演示：1.5大小项目，2个人，需要多少工时；0.5大小项目，20个工时，需要多少人？
# 核心公式：
# number=size*80/time
# time=size*80/number
# 请根据核心公式完成工时、人数函数的定义及调用
# 计算工时
# 1.0版本
# import math
# def work_time(size,number):
#     time=size*80/number
#     print('项目大小为%.1f个标准项目,使用%d个人完成,则需要工时数量为%.1f个'%(size,number,time))
# # work_time(1.5,2)
# # 计算人数
# def work_time(size,time):
#     number=math.ceil(size*80/time)
#     print('项目大小为%.1f个标准项目,需要工时数量为%.1f个,则需要人的数量为%d个'%(size,time,number))
# work_time(0.5,20)
# 1.0 人数未能取整，并将两个函数合二为一，定义一个函数完成工时/人力的计算
# 版本2.0定义一个函数
# def work(size=1,number=None,time=None):
#     if number==None and time!=None:
#         number=math.ceil(size*80/time)
#         print('项目大小为%.1f个标准项目,需要工时数量为%.1f个,则需要人的数量为%d个'%(size,time,number))
#     elif number!=None and time==None:
#         time=size*80/number
#         print('项目大小为%.1f个标准项目,使用%d个人完成,则需要工时数量为%.1f个'%(size,number,time))
# work(size=1.5,time=30)
# 限定选择类型，完成对应的计算
import math
# def work(types,size,other):
#     if types==1:
#         number=math.ceil(size*80/other)
#         print('项目大小为%.1f个标准项目,需要工时数量为%.1f个,则需要人的数量为%d个'%(size,other,number))
#     elif types==2:
#         time=size*80/other
#         print('项目大小为%.1f个标准项目,使用%d个人完成,则需要工时数量为%.1f个'%(size,other,time))
# work(1,7.7,20)
# work(2,5.4,5)

#3.0版本，交互式：采集、计算、返回结果
# 定义一个采集函数
key=2
def caiji():
    choice=input('请选择计算类型：1-人力计算 2-工时计算')
    if choice=='1':
        size=float(input('请输入项目大小：'))
        number=None
        time=eval(input('请输入工时数量：'))
        return size,number,time
        # 采集的人力计算所需的数据
    elif choice=='2':
        size=float(input('请输入项目大小：'))
        time=None
        number=eval(input('请输入人的数量：'))
        return size,time,number
# 定义计算函数 
def work(a):
    size=a[0]
    number=a[1]
    time=a[2]
# 如何将caiji()的数据作为work的参数来使用？
    if number==None and time!=None:
        number=math.ceil(size*80/time)
        print('项目大小为%.1f个标准项目,需要工时数量为%.1f个,则需要人的数量为%d个'%(size,time,number))
    elif number!=None and time==None:
        time=size*80/number
        print('项目大小为%.1f个标准项目,使用%d个人完成,则需要工时数量为%.1f个'%(size,number,time))
# 添加一个重复计算的函数
def again():
    global key
    cx=input('是否继续？继续请按‘y’，结束请按任意键')
    if cx!='y':
        key=0
# 定义一个主函数
def main():
    while key==2:
      print('欢迎使用!')
      a=caiji()
      work(a)
      again()
    print('感谢使用!')
main()
