# 图书管理小程序
# 书籍类

'''class Book:
    # 将书籍作者、书名、推荐语、书籍状态，默认未借出，初始值0，展示所有书籍
    def __init__(self,name,author,comment,state=0):
        self.n=name
        self.a=author
        self.c=comment
        self.s=state
    # 定义一个显示所有书籍信息的方法
    def show_info(self):
        if self.s==0:
            zt='未接出'
        else:
            zt='已借出'
        return '名称：《%s》 作者：%s 推荐语：%s \n状态：%s'%(self.n,self.a,self.c,zt)
book=Book('红楼梦','曹雪芹','金陵四大家族的兴衰史')
print(book.show_info())'''

# 特殊用法： __str__(self):使用print打印实例对象时，会直接打印出这个方法中return的数据。
class Book:
    # 将书籍作者、书名、推荐语、书籍状态，默认未借出，初始值0，展示所有书籍
    def __init__(self,name,author,comment,state=0):
        self.n=name
        self.a=author
        self.c=comment
        self.s=state
    # 定义一个显示所有书籍信息的方法
    def __str__(self):
        if self.s==1:
            zt='未借出'
        elif self.s==0:
            zt='已借出'
        return '名称：《%s》 作者：%s 推荐语：%s \n状态：%s'%(self.n,self.a,self.c,zt)
book=Book('红楼梦','曹雪芹','金陵四大家族的兴衰史')
print(book)
# 书籍管理类
class BookManager:
    books=[]
    def menu(self):
        print('欢迎使用！')
        while True:
            print('1.查询 \n2.添加 \n3.借阅 \n4.归还 \n5.退出')
            choice=int (input('请输入数字：'))
            if choice==1:
                self.show_all_book()
            if choice==2:
                self.add_book()
            if choice==3:
                self.lend_book()
            if choice==4:
                self.return_book()
            if choice==5:
                print('感谢使用！')
                break
    # 查询所有书籍的方法
    def show_all_book(self):
        print('书籍信息如下：')
        for book in self.books:
            # if self.books!=None:
            print(book)
            print('')
        # else:
        #      print('系统暂时无书\n')
    # 添加书籍
    def add_book(self):
        new_name=input('书名：')
        new_author=input('作者名：')
        new_comment=input('推荐语：')
        new_book=Book(new_name,new_author,new_comment)
        self.books.append(new_book)
        print('书籍录入成功！\n')
    # 检查书籍的方法
    def check_book(self,name):
        for book in self.books:
            if book.n==name:
                return book
        else:
            return None
    # 借阅书籍
    def lend_book(self):
        name=input('请输入书籍的名称：')
        res=self.check_book(name)
        if res!=None:
            if res.s==0:
                print('来晚一步，此书已经被借走')
            else:
                res.s=0
                print('借阅成功')
                
    # 归还书籍
    def return_book(self):
        name=input('请输入要归还的书籍名称：')
        res=self.check_book(name)
        if res!=None:
            if res.s==0:
               res.s=1
               print('书籍《%s》归还成功'%name)
               print(res)
            else:
                print('书籍《%s》未借出'%name)
        else:
            print('书籍《%s》不存在'%name)
bm=BookManager()
bm.menu()
