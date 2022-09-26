#include  <stdio.h>
#include  <malloc.h>
#define MAXSIZE   50
typedef int elemtype;
typedef struct
{
elemtype data[MAXSIZE];    //顺序表中所能容纳的最大数据元素个数
int len;
}Sequenlist;

Sequenlist * InitList(Sequenlist * L)
{
L=(Sequenlist *)malloc(sizeof(Sequenlist));
L-> len =0;
return (L);
}
int InsItem(Sequenlist * L,int i,elemtype item)
{   //在顺序表的i个位置插入元素item,插入成功返回1否则返回0
int j;
if ((* L).len>=MAXSIZE)
{
printf("The list is overflow.\n");  //线性表为满
return 0;
}
else if ((i<1) || (i>(*L).len+ 1))    //位置不合理返回0
{
printf ("Position is not correct.\n");
return 0;
}
else
{
for (j=(*L).len-1;j>=i-1;j--)
(*L).data [j+ 1]=(*L).data [j];  //元素后移
(*L).data [i- 1]=item;
(*L).len++;
return 1;
}
}
int DelItem(Sequenlist* L,int i)
{              //顺序表L中，删除第i个元素，成功返回1否则返回0
int j;
if ((*L).len==0)
{
printf ("List is empty\n");
return 0;
}
else if ((i<1) || (i>(*L).len))
{
printf("Delete item fail\n");
return 0;
}
else 
{
for(j=i;j<=L->len-1;j++)
(*L).data[j-1]=(*L).data[j];
(*L).len--;
return 1;
}
}
int LocItem(Sequenlist* L,elemtype item)
{
int j,i;
j=(*L).len;
if(j==0)
{
printf("The Sequenlist is empty");
return 0;
}
for(i=0;i<j;i++)
if ((*L).data[i]==item)
return(i+1);
printf("The item is not in this Sequenlist");
return 0;
}


void main()
{
	Sequenlist  *L;  int  i;
	L= InitList(L);
  for(i=0;i<10;i++)
	  if(InsItem(L,i+1,(i+1)*10)==0)  return;
	   else  printf("\n位置=%d,元素=%d",i+1,(i+1)*10);

if(DelItem(L,2)==0)  return;
  for(i=0;i<L->len;i++)
	   printf("\n位置=%d,元素=%d",i+1,L->data[i]); 
 
}