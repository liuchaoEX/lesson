# 复合数据类型\数据结构
# 基础数据类型：str int float
# 数据结构：序列(字符串、列表、元组) 映射(字典) 集合
# 列表 list ：内置数据类型，有顺序
# 创建：
# []
list_1=[1,2.0,'3',[4,5,6],True,'我们']
# print(list_1)
# list()
list_2=list(('2',3.7,56,'python',(4,5,6)))
# print(list_2)
# print(type(list_2))
# 列表的提取和切片:
# 索引位置进行提取 列表名[索引位置]
# 切片 列表名[开始索引:结束索引:步长]
a='python'
b=list(a)
# print(b)
# 提取b中的t元素，怎样操作？
# print(b[2])
# 提取b列表中的thon，怎样操作？
# print(b[2:])
# 生成一个0-99的数字列表，然后提取任意
L=list(range(100))
# print(L)
# 提取前5个
# 提取后5个数
# 提取1-10的奇数
# 每隔5个数取一个
# 复制序列
# 逆序
# 列表中常用的操作方法
# 增 ：append extend insert
week=['星期一','星期二','星期三','星期四','星期五','星期五']
# week_1=['星期五','星期一','星期二','星期三','星期四','星期五']
# print(week==week_1)
# append:每次增一加个元素，在列表的末尾
# week.append('星期六')
# extend:合并列表,顺序与语法中相同
# other=['星期六','星期日']
# week.extend(other)
# insert:在指定的位置<索引位置>增加一个元素
# week.insert(0,'星期日')

# 删 :del pop remove
# del 列表名[索引位置]
# del week[2]
# pop 列表名.pop(索引位置)
# week.pop(-4)
# remove 列表名.remove('元素名称')
# week.remove('星期六')

# 改 ：赋值语句 列表名[索引位置]='新元素名'
# week[0]='Monday'
# print(week)

# 查 index():返回查询元素首次出现的索引位置 in
# print(week.index('星期五'))
# week[week.index('星期五')]='Friday'
# print(week)
# print('星期日' in week)
# len count sort sorted reverse
# print(len(week))
# 在列表[110,‘dog’,‘cat’,120,‘apple’]中关于动物的字符串之间插入一个空列表，并删除关于水果的字符串
#同时查找出列表中的数值并在列表中增大10倍。 
# mylist_1=[110,'dog','cat',120,'apple']
# mylist_1.insert(2,[])
# del mylist_1[-1]
# mylist_1.pop(-1)
# mylist_1.remove('apple')
# mylist_1[mylist_1.index(110)]*=10
# mylist_1[mylist_1.index(120)]*=10
# print(mylist_1)

# 元组 ：不可变序列
# 创建：() tuple()
# tuple_1=(0,1.2,'3',(4,5,6),True)
# print(tuple_1)
# print(type(tuple_1))
# tuple()
my_tuple=tuple([0,1.2,'3',(4,5,6),True])
# print(my_tuple)
# print(type(my_tuple))
# 元组的常用操作:只能查询，无法实现增删改
# 提取单个元素
# print(my_tuple[1])
# 切片
# print(my_tuple[1:3])


# 字典:存在对应关系 键值对 key:value 无序，键不可以重复
# 创建
# {}
my_dict_1={'张丰毅':[95,78],'张三':89,'张三丰':90,'张一一':98}
# print(my_dict_1)
# dict()
# my_dict_2=dict([['张一一',98],('张三',89),('张三丰',90),('张丰毅',[95,78])])
# print(my_dict_2)
# print(my_dict_2==my_dict_1)
# 字典的常用操作
# 增 
# 键访问赋值  字典名[键名]=值 
my_dict_1['张三山']=99
# update 合并字典 字典名.updata(字典名_1)
other_1={'赵敏':89,'周芷若':91}
my_dict_1.update(other_1)

# 删 del pop clear
# DD=my_dict_1.copy()
# del del 字典名[键]
# del DD['张丰毅']
# print(my_dict_1)
# pop 字典名.pop(键)
# S=DD.pop('张丰毅')
# print(S)

# clear 清空字典元素
# DD.clear()

# 改 赋值语句
# DD['张丰毅']=93
# print(DD)

# 查 keys values items
# print('赵敏' in my_dict_1)
# 获取所有键
# all_keys=my_dict_1.keys()
# print('赵敏' in all_keys)
# print(all_keys)

# score={'Math':96,'English':86,'Chinese':95.5,'Biology':86,'Physics':None}
# score['历史']=88
# # del score['Physics']
# score.pop('Physics')
# # round(a,b)
# score['Chinese']=round(score['Chinese'])
# print('数学成绩',score['Math'])
# print(score)
# my_dict_3={'Math':96,'English':86,'Chinese':95.5,'Biology':86,'Physics':None}
# my_dict_3['history']=88
# DD=my_dict_3.copy()
# my_dict_3.pop('Physics')
# # DD=my_dict_3
# # DD.pop('Physics')
# print(my_dict_3)
# print(DD)

# 字典和列表的异同
# 不同：数据读取方式不同，列表有顺序，要用偏移量来定位，字典无序，通过唯一的键来取值
# 相同点：通过赋值语句完成元素的修改；支持任意嵌套
# 相互嵌套如何提取
# 字典、列表相关嵌套
score={'Mary':63,'Lucy':{'s1':98,'s2':97,'s3':65,'s4':42},'Linda':59,'Lily':17}
# print(score['Lucy']['s4']) 