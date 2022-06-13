# # print("Hello World!")

# 根据给定的半径，求取周长 、面积
# import math
# PI=3.14
# r = int(input("请输入圆的半径："))
# print("圆的半径：",2*PI*r)
# print("圆的面积：",PI*r*r)

# 根据给定的周长，求取半径、面积
# import math
# PI=3.14
# C = int(input("请输入圆的周长："))
# print("圆的半径：",C/(2*PI))
# print("圆的面积：",PI*(C/(2*PI)*C/(2*PI)))

# 根据给定的面积，求周长、半径
# import math
# PI=3.14
# S = int(input("请输入圆的面积："))
# print("圆的半径：",math.sqrt(S/PI))
# print("圆的周长：",2*PI*(math.sqrt(S/PI)))

# 天龙八部
# while True:
#     a1=input('第一问：地方是？')
#     if a1!='冰窟':
#         continue
#     print('答对了，现在第二问')
#     a2=input('第二问：名字是？')
#     if a2!='梦姑':
#         continue
#     print('答对了，现在第三问')
#     a3=input('第三问：相貌？')
#     if a3=='不知道':
#         break
#     print('你就是驸马')
# # 西游记
# for i in range(5):
#     print('供养一对童男童女')
#     if i==4:
#         break
#     print('唐僧师徒到来')
#     print('孙悟空制服了鲤鱼精，百姓再也不用受苦了')

# # 字典和列表的异同
# # 不同：数据读取方式不同，列表有顺序，要用偏移量来定位，字典无序，通过唯一的健来取值
# # 相同点：通过赋值语句完成元素的修改：支持任意嵌套
# # 相互嵌套如何提取
# # 字典、列表相关嵌套
# # score={'Mary':63,'Lucy':{'s1':98,'s2':97,'s3':65,'s4':42},'Linda':59,'Lily':17}
# # # print(score[5]['Lucy'][1])
# # print(score['Lucy']['s4']) 
# while True:
#     dict_1 = {'汉堡类':'香辣鸡腿堡，劲爆鸡腿堡，新奥尔良烤鸡腿堡，半鸡半虾堡'}
#     dict_2 = {'小食类':'薯条，黄鸡鸡块，土豆泥'}
#     dict_3 = {'饮料类':'可口可乐，九珍果汁，经典咖啡'}
#     LC=input('查看汉堡类请输入1，查看小吃类请输入2，查看饮料类请输入3，若不查看请输入0\n')
#     if LC=='1':
#         print(dict_1)
#         continue
#     elif LC=='2':
#         print(dict_2)
#         continue
#     elif LC=='3':
#         print(dict_3)
#         continue
#     else:
#         print('不需要')
#         break