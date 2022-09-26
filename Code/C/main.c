// #include  <stdio.h>
// #define  Maxsize   50
// typedef int ElemType;
// typedef struct SqStack
// {
//     ElemType elem[Maxsize];
//     int top;
// }SqStack;
// /*初始化栈：*/
// void   Init_SqStack(SqStack *s)
// {
// s->top=-1;  //初始化  指针变量->成员 或者 (*指针变量).成员
// }
// /*进栈：*/
// void   Push(SqStack *s,ElemType  x)
// {
// if(s->top<Maxsize-1)
//   {
//    s->top++; //s->top=s->top+1; 栈顶上移
//    s->elem[s->top]=x;    //压栈
//   }
// else 
// printf("栈满，不能入栈\n");
// }
// /*出栈*/
// ElemType  Pop(SqStack *s)
// {
// ElemType  x;
//  if(s->top!=-1)
//   {
//   x= s->elem[s->top];  //读出要出栈的元素
//  s->top--; //s->top=s->top-1; 栈顶下移
//  return x;
//   }
// else 
// printf("栈空，不能出栈\n");  return 0;
// }
// /*读栈顶元素*/
// void   Get_top(SqStack *s, ElemType  *x)
// {
// if(s->top!=-1)
//   {
//   *x= s->elem[s->top];  //读出要出栈的元素
//  }
// }
// main()
// {SqStack S;
// int  i;  ElemType  x;
// Init_SqStack(&S);
// for(i=0;i<5;i++)
//  Push(&S,(i+1)*10);
// Get_top(&S,&x);
// printf("栈顶元素=%d",x);
// x=Pop(&S);
// printf("出栈元素=%d",x);
// Get_top(&S,&x);
// printf("栈顶元素=%d",x);
// }

/*栈链式结构*/
// #include<stdio.h>
// #include<malloc.h>
// typedef int ElemType;
// typedef struct node
// {
//     ElemType data;
//     struct node* next;   
// }Structnode,* LinkStack;
// /*进栈*/
// void Push(Structnode *s, ElemType e)
// {
//     Structnode *p;
//     p=(Structnode*)malloc(sizeof(Structnode));
//     p->data=e;
//     p->next=s;
//     s=p;
// }
// /*出栈*/
// int Pop(Structnode *s, ElemType *e)
// {
//     Structnode *p;
//     if(s==NULL)
//       return 0;
//     p=s;
//     *e=p->data;
//     s=p->next;
//     free(p);
//     return 1;
// }
// int Get_Top(Structnode*s, ElemType *e)
// {
//     if(s==NULL)
//      return 0;
//     *e= s->data;
//     return 1;
// }
// main()
// {
//     Structnode *s;
//     int i;ElemType x;
//     s=NULL;
//     for(i=0;i<5;i++)
//     Push(s,(i+1)*10);
//     if(Get_Top(s,&x)==0) printf("栈空，无栈顶元素\n");
//     else printf("栈顶元素=%d",x);
//     if(Pop(s,&x)==0) printf("栈空，无元素可出\n");
//     else printf("栈顶元素=%d",x);
//     if(Get_Top(s,&x)==0) printf("栈空，无栈顶元素\n");
//     else printf("栈顶元素=%d",x);
// }


#include  <stdio.h>
#include  <malloc.h>
typedef  int  ElemType;
typedef  struct  node
   {
ElemType  data;    
struct  node *next;
 }Structnode,*LinkStack; 
void   Push(Structnode *s,ElemType  e)
{
Structnode *p;
p=(Structnode *)malloc(sizeof(Structnode));
p->data=e; p->next=s;
s=p;
}
/*出栈*/
int Pop(Structnode *s,ElemType  *e)
{
Structnode  * p;
if(s==NULL)  return  0;
p=s;
*e=p->data;
s=p->next;
free(p);
return  1;
}
int  Get_Top(Structnode  *s,ElemType *e)
{if(s==NULL)  return  0;
*e=s->data;
return 1;
}  

int  main()                                        
{ Structnode  *s;
int  i; ElemType   x;
s=NULL;
for(i=0;i<5;i++)
Push(s,(i+1)*10);
if(Get_Top(s,&x)==0)   printf("栈空，无栈顶元素\n");
else  printf("栈顶元素=%d",x);
if(Pop(s,&x)==0)  printf("栈空，无元素可出\n");
 else  printf("栈顶元素=%d",x);
if(Get_Top(s,&x)==0)   printf("栈空，无栈顶元素\n");
else  printf("栈顶元素=%d",x);
}
