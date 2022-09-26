#include  <stdio.h>
#include  <malloc.h>
typedef int elemtype;
typedef struct node
{
	elemtype data;
	struct node* next;
}linklist;


linklist* InitList(linklist* L)
{
	L=(linklist* )malloc(sizeof(linklist));
	L->next=NULL;
	return(L);
}


linklist * Creatlist(int n)
{
	int x,i;
	linklist  *L,*r,*p;
	L=InitList(L);
	r=L;
	for(i=1;i<=n;i++)
	{
		printf("input value:\n");
		scanf("%d",&x);
		p=(linklist*)malloc(sizeof(linklist));
		p->data=x;
		p->next=NULL;
		r->next=p;
		r=r->next;
	}
	return(L);
}

/*
int  InsItem(linklist* L,elemtype item,int i)
{       //给单链表L的第i个结点前插入元素item
	int j;
	linklist *p,*t;
	p=L;
	j=1;
	t=(linklist*)malloc(sizeof(linklist));
	t->data=item;
	if(L->next==NULL)  //空表，插入的位置为0，则插入到空表末尾
	{
		if(i==0)
		{
			L->next=t;
			t->next=NULL;
			return(1);
		}
		else return (0);
	}
	while((p->next!=NULL)&&(j<i))
	{
		p=p->next;
		j++;
	}
	if(p==NULL)
	{
		printf("The node%d is not exist\n",i);  //i的位置不合理
		return(0);
	}
	else
	{
    	t->next=p->next;
		p->next=t;
		return(1);
	}
}   */

int InsItem(linklist* L,elemtype item,elemtype k)
{            //在L的单链表中元素值为K的前面插入结点item
	linklist *q,*p,*t;
	t=(linklist*)malloc(sizeof(linklist));
	t->data=item;
	if(L->next==NULL)
	{
		printf("The linklist is empty\n");
		return(0);
	}
	else
	{
		q=L;
		p=L->next;
		while(p!=NULL)
			if(p->data!=k)
			{
				q=p;
				p=p->next;
			}
			else
				break;
	}
	if(p==NULL)
	{
		printf("The node%d is not exist\n",k);return(0);
	}
	else
	{
		q->next=t;
		t->next=p;
		return(1);
	}
}
/*
int  DelItem(linklist* L,int i)
{
	int j;
	linklist *p,*q;
	p=L;
	j=1;
	if(L->next==NULL)
	{
		printf("The linklist is empty.\n");
		return(0);
	}
	while((p->next!=NULL)&&(j<i))
	{
		p=p->next;
		j=j+1;
	}
	if(p==NULL)
	{
		printf("The node %d is not exist\n",i);
		return(0);
	}
	else
	{
		q=p->next;
		p->next=p->next->next;
		free(q);
		return(1);
	}
}  */
int DelItem(linklist* L,elemtype item)
{
	 	linklist *p,*q;
	if(L->next==NULL)
	{
		printf("The linklist is empty\n");
		return(0);
	}
	else
	{
		q=L;
		p=L->next;
		while(p!=NULL)
			if(p->data!=item)
			{
				q=p;
				p=p->next;
			}
			else
				break;
	}
	if(p==NULL)
	{
		printf("The node %d is not exist\n",item);
		return(0);
	}
	else
	{
		q->next=p->next;
		free(p);return(1);
	}
}


void  main()
{  linklist  *L,*p;
  L=InitList(L);   //调用初始化
  L=Creatlist(10);
  //测试第二个插入函数
  if( InsItem(L,200,40)==0)   return ;
   else for(p=L->next;;p=p->next)
   {   printf("%5d",p->data);  if(p->next==NULL) break;}
 
if(DelItem(L,30)==0)  return  ;
  else   for(p=L->next;;p=p->next)
   {   printf("%5d",p->data);  if(p->next==NULL) return ;}
     
  /*  测试第一个插入函数
  if(InsItem(L,200,4)==0)   return ;
   else for(p=L->next;;p=p->next)
   {   printf("%5d",p->data);  if(p->next==NULL) return ;}
  */
}