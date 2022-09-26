#include<stdio.h>
#include<stdlib.h>
/*顺序表的类型定义*/
#define MAXLEN 100
//使用typedef定义新类型名，语法typedef 原类型名 新类型名;
typedef int DataType;
/*typedef 原类型名 新类型名;*/
typedef struct 
{
    DataType data[MAXLEN];//存放线性表的数组
    int Length;//length是顺序表的长度
}SeqList;
SeqList L;

/*1.顺序表的初始化*/
void InitList( SeqList *L)
{
    L ->Length = 0;
}
/*2.顺序表的建立*/
void CreateList(SeqList *L,int n)
{
    int i;
    printf("请输入%d个整数:",n);
    for ( i = 0; i < n; i++)
    {
        scanf("%d",&L->data[i]);
    }
    L->Length = i;
}
/*3.查找操作*/
int GetElem(SeqList *L,int i,DataType *x)//按位置查找
{
    if (i<1||i>L->Length)
    {
        return 0;
    }
    else
    {
        *x = L->data[i-1];
        return 1;
    }  
}
int Locate(SeqList *L,DataType x)//按值查找
{
    int i;
    /*while (i<L->Length && L->data[i] != x)
    {
        i++;
    }*/
    for(i=0;L->data[i] != x;i++){};
    if (i>=L->Length)
    {
        return 0;
    }
    else
    {
        return i+1;
    }  
}
/*4.插入操作*/
int InsElem(SeqList *L,int i,DataType x)
{
    int j;
    if (L->Length>=MAXLEN)
    {
        printf("顺序表已满！");
        return -1;
    }
    if (i<1 || i>L->Length+1)
    {
        printf("插入位置出错！");
        return 0;
    }
    if (i == L->Length+1)
    {
        L->data[i-1] = x;
        L->Length++;
        return 1;
    } 
    for ( j = L->Length-1; j >= i-1; j--)
    {
        L->data[j+1] = L->data[j];
    }    
		L->data[i-1] = x;
        L->Length++;
        return 1;
    
}
/*5.删除操作*/
int DelElem(SeqList *L,int i,DataType *x)
{
    int j;
    if (L->Length == 0)
    {
        printf("顺序表为空！");
        return 0;
    }
    if (i<1 || i>L->Length)
    {
        printf("不存在第i个元素");
        return 0;
    }
    *x = L->data[i-1];
    for ( j = i; j < L->Length; j++)
    {
        L->data[j-1] = L->data[j];
    }
    L->Length--;
    return 1;
}
/*6.输出表中元素操作*/
void DispList(SeqList *L)
{
    int i;
    for ( i = 0; i < L->Length; i++)
    {
        printf("%5d ",L->data[i]);
    }  
}
/*7.显示菜单函数*/
void Menu()
{
    printf("            顺序表的各种操作            \n");
    printf("=======================================\n");
    printf("|         1--建立顺序表               ||\n");
    printf("|         2--插入元素                 ||\n");
    printf("|         3--删除元素                  ||\n");
    printf("|         4--按位置查找元素           ||\n");
    printf("|         5--按元素值查找其在表中的位置||\n");
    printf("|         6--求顺序表的长度           ||\n");
    printf("|         0--返回                    ||\n");
    printf("=======================================\n");
    printf("请输入你要选择的菜单号：");
}
/*主函数*/
int main()
{
    SeqList L;
    DataType x;
    int n,i,loc;
    char ch1,ch2,a;
    ch1 = 'y';
    while (ch1 == 'y'|| ch1 == 'Y')
    {
        Menu();
        scanf("%c",&ch2);
        getchar();
        switch (ch2)
        {
        case '1':
            InitList(&L);
            printf("请输入建立线性表的个数：");
            scanf("%d",&n);
            CreateList(&L,n);
            printf("建立的线性表为：");
            DispList(&L);
            break;
        case '2':
            printf("请输入你要插入的位置：");
            scanf("%d",&i);
            printf("请输入你要插入的元素值：");
            scanf("%d",&x);
            if (InsElem(&L,i,x))
            {
                printf("已成功在第%d的位置上插入%d,插入后的线性表为：\n",i,x);
                DispList(&L);
            }
            else
            {
                printf("输入插入的参数错误！");
            }
            break;
        case '3':
            printf("请输入要删除元素的位置：");
            scanf("%d",&i);
            if (DelElem(&L,i,&x))
            {
                printf("已成功在第%d的位置上删除%d，删除后的线性表为：\n",i,x);
                DispList(&L);
            }
            else
            {
                printf("输入删除的参数错误！");
            }
            break;
        case '4':
            printf("请输入要查看表中元素的位置（从1开始）：");
            scanf("%d",&i);
            if (GetElem(&L,i,&x))
            {
                printf("当前线性表第%d个元素的值为：%d",i,x);
            }
            else
            {
                printf("输入的位置错误！");
            }
            break;
            
        case '5':
            printf("请输入要查找的元素值为：");
            scanf("%d",&x);
            loc = Locate(&L,x);
            if (loc)
            {
                printf("查找元素值为%d的位置为：%d",x,loc);
            }
            else
            {
                printf("此表中无此元素！");
            }
            break;
        case '6':
            printf("当前线性表的长度为:%d",L.Length);
            break;
        case '0':
            ch1 = 'n';
            break;
        default:
            printf("输入有误，请输入0~6进行选择。");
            break;
        }
        if (ch2 != '0')
        {
            printf("\n按回车键继续，按任意键返回主菜单！\n");
            a = getchar();
            if (a != '\xA')
            {
                getchar();
                ch1 = 'n';
            }
            
        }
        
    } 
}
