'''处理学生成绩
面向过程的处理方式'''
# student_1={'name':'Mike','score':98}
# student_2={'name':'Jone','score':88}
'''定义一个函数实现学生成绩的打印'''
# def print_score(std):
#     print("%s:%s"%(std['name'],std['score']))
'''调用函数'''
# print_score(student_1)
# print_score(student_2)
'''面向对象的处理方式'''
# class Student:
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#     def print_score(self):
#         print("%s:%s"%(self.name,self.score))
# stu_1=Student('Mike',98)
# stu_2=Student('Lucy',86)
# stu_1.print_score()
# stu_2.print_score()

'''面向对象编程
1.什么是面向对象编程(面向过程编程)
类(class):客观事物抽象的模板
实例(instance):根据类创建出来的具体对象
类的创建:
class 首字母为大写的类名
      类属性(赋值语句，定义“是怎样的”)
      类方法(def 方法名(self):)
            方法具体执行过程，定义“能做什么”
调用类: 类的实例化  实例名=类名()
实例名.属性
实例名.方法()
2.类的两个关键点
(1).特殊参数self:所有实例的替身，会接收实例化过程中传入的数据，当实例对象创建后，实例会代替self运行
self代表表的实例本身，方便数据的流转；
1>只要在类中用def语句创建语法时，就必须把第一个参数位置留给self，并在调用方法时忽略它(不需要给self传参)
2>当在类的方法内部想要调用类属性或其他方法时，就要采用self.属性名或self.方法名的格式
(2).初始化方法
语法格式:def__init__(self):
作用:当每个实例对象创建时，该方法内部的代码无须调用就会自动运行。
除了设置固定常量，初始化方法同样可以接受其他参数，让传入的数据能够作为属性再类的方法之间流转'''


'''创建一个电脑类'''
# class Computer:
#     screen=True
#     def start(self):
#         print('电脑正在开机中……')
# zhangsan_computer=Computer()
# print(zhangsan_computer.screen)
# zhangsan_computer.start()

'''创建一个动物类'''
# class Animal(object):
#     food=True
#     def eat(self):
#         print('狗会吃骨头')
# lisi_animal=Animal()
# print(lisi_animal.food)
# lisi_animal.eat()

'''特殊参数self'''
'''定义一个chinese类'''
# class Chinese:
#     name='张三'
#     def say(self,someone):
#         print(someone+'是中国人')
# person=Chinese()
# print(person.name)
# person.say('张三')

'''怎样实现再方法内部进行类属性的调用？？'''
# class Chinese:
#     name='张三'
#     def say(self):
#         print(self.name+'是中国人')
# person=Chinese()
# print(person.name)
# person.say()

'''初始化方法'''
# class Chinese:
#     def __init__(self):
#         self.mouth=1
#         self.eye=2
#     def body(self):
#         print('我有%s张嘴巴'%self.mouth)
#         print('我有%s只眼睛'%self.eye)
# person=Chinese()
# person.body()

'''定义一个类，不使用初始化方法，完成某人出生低和居住地的输出'''
# class Chinese:
#     def born(self,name,birth):
#         print(name+'出生在'+birth)
#     def live(self,name,region):
#         print(name+'居住在'+region)
#     def work(self,name,place):
#         print(name+'工作地在'+place)
# person=Chinese()
# person.born('steve','湖北')
# person.live('steve','山西')
# person.work('steve','陕西')

'''定义一个类，使用初始化方法，完成某人出生地和居住地的输出'''
# class Chinese:
#     def __init__(self,name,birth,region):
#         self.na=name
#         self.bi=birth
#         self.re=region
#     def born(self):
#         print(self.na+'出生在'+self.bi)
#     def live(self):
#         print(self.na+'居住在'+self.re)
#     def work(self):
#         print(self.na+'工作在'+self.re)
# person=Chinese("张三",'湖北','陕西')
# person.born()
# person.live()

'''包含初始化方法，要求最后打印：自动显示“你在哪里出生？”用户传入参数，完成回答“我出生在**”'''
# class Chinese:
#     def __init__(self,hometown):
#         self.ht=hometown
#         print('你出生在哪里？')
#     def born(self):
#         print('我出生在%s'%self.ht)
# zhangsan=Chinese('西安')
# zhangsan.born()

# class Example:
#     pass
# example=Example()
# print(dir(example))