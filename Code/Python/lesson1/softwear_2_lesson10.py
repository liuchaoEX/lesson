'''User'''
# class Robot:
#     def __init__(self,name,speak,desire):
#         self.na=name
#         self.sp=speak
#         self.de=desire
#         print('我的名字是什么？')
#     def fullname(self):
#         print('你的名字是%s'%self.na)
#         print('你的的名字是什么？')
#     def hello(self):
#         print('我的名字是%s'%self.sp)
#         print('我的愿望是什么？')
#     def gift(self):
#         for i in range(3):
#             print('我的愿望是%s'%self.de)
# zhangsan=Robot("Steve","mike",'学会python')
# zhangsan.fullname()
# zhangsan.hello()
# zhangsan.gift()

'''Tc'''
# class Robot:
#     def __init__(self):
#         self.name=input('帮我取个名字吧！')
#         self.you=input('请问你叫什么名字？')
#         print('你好%s,我叫%s,很高兴遇见你！'%(self.you,self.name))
#     def wish(self):
#         wi=input('请说出你的愿望：')
#         print(self.you+'的愿望是：')
#         for i in range(3):
#             print(wi)
# robot=Robot()
# robot.wish()

# “伪私有”属性和方法:以双下划线为名称前缀的
# class test:
#     data=100
#     __data2=200
#     def add(a,b):
#         return a+b
#     def __sub(a,b):
#         return a-b

# print(test.data)
# print(test._test__sub(2,3))
# print(test._test__data2)

# 静态方法 @staticmethod
# class test:
#     @staticmethod
#     def add(a,b):
#         return a+b
# 通过类对象调用静态方法 
# print(test.add(2,3))

# 创建实例对象调用静态方法
# x=test()
# print(x.add(3,5))

# __slots__
# @property


# 类的继承和定制
'''
class Chinese:
    eye='black'
    def eat(self):
        print('吃饭用筷子')
# 简单继承 class 子类名(父类名):
class Shanxi(Chinese):
    def eat(self):
        print('我们爱吃biangbiang面')
zhangsan=Chinese()
# print(zhangsan.eye)
# zhangsan.eat()
chenzhongshi=Shanxi()
# print(chenzhongshi.eye)
# chenzhongshi.eat()


# isinstance()验证类与实例之间关系的函数
# 子类实例与父类的关系
print(isinstance('1',int))
print(isinstance(chenzhongshi,Chinese))
# 父类实例和子类的关系
print(isinstance(zhangsan,Shanxi))
# 类创建的实例与根类的关系
print(isinstance(zhangsan,object))
print(isinstance(chenzhongshi,object))
# class Super_class:
#     data=100
#     __data2=200
#     def showinfo(self):
#         print('超类showinfo()方法中的输出信息')
#     def __showinfo(self):
#         print('超类__showinfo()方法中的输出信息')

# class Sub_class(Super_class):
    # pass
# 获得超类的属性和方法
print(dir(Super_class))
# Supper=dir(Sub_class)
# 获得子类的属性和方法
print(dir(Sub_class))
# Sub=dir(Sub_class)
print(Supper==Sub)
# 访问继承的属性
print(Sub_class.data)
print(Sub_class._Super_class__data2)
# 创建子类的实例对象
# x=Sub_class()

# 调用继承的方法
x.showinfo()
# x._Super_class__showinfo()
'''
# 多层继承
# class A(B):
#     pass
# class C(A):
#     pass
# class Earthman:
#     eye_number=2
# class Chinese(Earthman):
#     eye_color='black'
# class Shanxi(Chinese):
#     pass
# czs=Shanxi()
# print(czs.eye_number)
# print(czs.eye_color)
# 多重继承,优先继承靠近子类的父类的属性和方法
# class A(B,C,D):

# class Hei:
#     born_city='Heilongjiang'
#     wearing='thick'
#     def diet(self):
#         print('我们爱吃酸菜')
# class Yue:
#     settle_city='Guangdong'
#     wearing='thin'
#     def diet(self):
#         print('我们吃的清淡')

# class Yuehei(Yue,Hei):
#     pass

# xiaoming=Yuehei()
# print(xiaoming.born_city)
# print(xiaoming.wearing)
# xiaoming.diet()


# class C0:
#     name='C0'
# class C2(C0):
#     num=2
# class C1:
#     num=1
# class C3:
#     name='C3'
# class C4(C1,C2,C3):
#     pass
# Steve=C4()
# print(Steve.name)
# print(Steve.num)

# 类的定制

# 新增代码
# class Chinese:
#     eye='black'
#     def eat(self):
#         print('用筷子')
# class Shanxi(Chinese):
#     native_place="XI'AN"
#     def diet(self):
#         print('我们会讲陕西话')

# czs=Shanxi()
# czs.eat()
# czs.diet()

# 重写代码
# class Chinese:
#     def land_area(self,area):
#         print('我们居住的地方，陆地面积是%d万平方公里左右'%area)
# class Shanxi(Chinese):
#     def land_area(self, area):
#         print('我们居住的地方，陆地面积是%d万平方公里左右'%int(area*0.031))
# class Henan(Chinese):
#     pass
# class Hunan(Chinese):
#     pass

# zs=Chinese()
# czs=Shanxi()
# zs.land_area(960)
# czs.land_area(960)

# 子类直接继承父类的方法：父类，方法名(参数)
# class Chinese:
#     def land_area(self,area):
#         print('我们居住的地方，陆地面积是%d万平方公里左右'%area)
# class Shanxi(Chinese):
#     def land_area(self, area,rate=0.031):
#         Chinese.land_area(self,area*rate)
# class Henan(Chinese):
#     pass
# class Hunan(Chinese):
#     pass

# zs=Chinese()
# czs=Shanxi()
# zs.land_area(960)
# czs.land_area(960)

class Chinese:
    def __init__(self,greet='你好',place='中国'):
        self.greet=greet
        self.place=place
    def greeting(self):
        print('%s!欢迎来到%s'%(self.greet,self.place))



# 在父类的基础上定义一个Guangdong子类，完成：“雷猴，欢迎来到广东”的问候
class Guangdong(Chinese):
    def __init__(self,greet='雷猴',place='广东'):
        Chinese.__init__(self,greet,place)
# zs=Chinese()
# zs.greeting()
yewen=Guangdong()
yewen.greeting()