a=float(input("第一条边的长度："))
b=float(input("第二条边的长度："))
c=float(input("第三条边的长度："))
n=(a+b>c)+(b+c>a)+(a+c>b)
if n==3:
    print("三角形的三边边长：",a,b,c)
    print("是一个符合条件的三角形！")
else:
    print("输入有误，输入的三边不能构成三角形！")