// #include  <stdio.h>
// #define  Maxsize   50
// typedef int ElemType;
// typedef struct SqStack
// {
//     ElemType elem[Maxsize];
//     int top;
// }SqStack;
// /*��ʼ��ջ��*/
// void   Init_SqStack(SqStack *s)
// {
// s->top=-1;  //��ʼ��  ָ�����->��Ա ���� (*ָ�����).��Ա
// }
// /*��ջ��*/
// void   Push(SqStack *s,ElemType  x)
// {
// if(s->top<Maxsize-1)
//   {
//    s->top++; //s->top=s->top+1; ջ������
//    s->elem[s->top]=x;    //ѹջ
//   }
// else 
// printf("ջ����������ջ\n");
// }
// /*��ջ*/
// ElemType  Pop(SqStack *s)
// {
// ElemType  x;
//  if(s->top!=-1)
//   {
//   x= s->elem[s->top];  //����Ҫ��ջ��Ԫ��
//  s->top--; //s->top=s->top-1; ջ������
//  return x;
//   }
// else 
// printf("ջ�գ����ܳ�ջ\n");  return 0;
// }
// /*��ջ��Ԫ��*/
// void   Get_top(SqStack *s, ElemType  *x)
// {
// if(s->top!=-1)
//   {
//   *x= s->elem[s->top];  //����Ҫ��ջ��Ԫ��
//  }
// }
// main()
// {SqStack S;
// int  i;  ElemType  x;
// Init_SqStack(&S);
// for(i=0;i<5;i++)
//  Push(&S,(i+1)*10);
// Get_top(&S,&x);
// printf("ջ��Ԫ��=%d",x);
// x=Pop(&S);
// printf("��ջԪ��=%d",x);
// Get_top(&S,&x);
// printf("ջ��Ԫ��=%d",x);
// }

/*ջ��ʽ�ṹ*/
// #include<stdio.h>
// #include<malloc.h>
// typedef int ElemType;
// typedef struct node
// {
//     ElemType data;
//     struct node* next;   
// }Structnode,* LinkStack;
// /*��ջ*/
// void Push(Structnode *s, ElemType e)
// {
//     Structnode *p;
//     p=(Structnode*)malloc(sizeof(Structnode));
//     p->data=e;
//     p->next=s;
//     s=p;
// }
// /*��ջ*/
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
//     if(Get_Top(s,&x)==0) printf("ջ�գ���ջ��Ԫ��\n");
//     else printf("ջ��Ԫ��=%d",x);
//     if(Pop(s,&x)==0) printf("ջ�գ���Ԫ�ؿɳ�\n");
//     else printf("ջ��Ԫ��=%d",x);
//     if(Get_Top(s,&x)==0) printf("ջ�գ���ջ��Ԫ��\n");
//     else printf("ջ��Ԫ��=%d",x);
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
/*��ջ*/
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
if(Get_Top(s,&x)==0)   printf("ջ�գ���ջ��Ԫ��\n");
else  printf("ջ��Ԫ��=%d",x);
if(Pop(s,&x)==0)  printf("ջ�գ���Ԫ�ؿɳ�\n");
 else  printf("ջ��Ԫ��=%d",x);
if(Get_Top(s,&x)==0)   printf("ջ�գ���ջ��Ԫ��\n");
else  printf("ջ��Ԫ��=%d",x);
}
