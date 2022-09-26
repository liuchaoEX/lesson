import math
key=2
# 采集函数
def caiji():
    choice=input('请选择计算类型：1-人力计算 2-工时计算')
    if choice=='1':
        size=float(input('请输入项目大小：'))
        number=None
        time=eval(input('请输入工时数量：'))
        return size,number,time
        # 人力计算所需的数据
    elif choice=='2':
        size=float(input('请输入项目大小：'))
        time=None
        number=eval(input('请输入人的数量：'))
        return size,time,number
# 计算函数 
def work(a):
    size=a[0]
    number=a[1]
    time=a[2]
    if number==None and time!=None:
        number=math.ceil(size*80/time)
        print('项目大小为%.1f个标准项目,需要工时数量为%.1f个,则需要人的数量为%d个'%(size,time,number))
    elif number!=None and time==None:
        time=size*80/number
        print('项目大小为%.1f个标准项目,使用%d个人完成,则需要工时数量为%.1f个'%(size,number,time))
# 重复计算的函数
def again():
    global key
    cx=input('是否继续？继续请按‘y’，结束请按任意键')
    if cx!='y':
        key=0
# 主函数
def main():
    while key==2:
      print('欢迎使用')
      a=caiji()
      work(a)
      again()
    print('感谢使用')
main()
