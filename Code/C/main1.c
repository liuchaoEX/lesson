#include <stdio.h>
void main(){
    printf("Hello World!\n");
}
// // #include <stdio.h>
// // void main(){
// //     printf("Hello World!\n");
// // }
// #include  <stdio.h>
// #include  <malloc.h>
// typedef int elemtype;
// typedef struct node
// {
// elemtype data;
// struct node *next;
// }linklist;

// linklist* Initlist(linklist*L)
// {
// L=(linklist*)malloc(sizeof(linklist));
// L-> next=NULL;
// return(L);
// }


// linklist*Creatlist(int n)
// {
// int x,i;
// linklist *L,*r,*p;
// L=Initlist(L);
// r=L;
// for(i=1;i<=n;i++)
// {
// printf("input value:\n");
// scanf("%d",&x);
// p=(linklist*)malloc(sizeof(linklist));
// p->data=x;
// p->next=NULL;
// r->next=p;
// r=r->next;
// }
// return(L);
// }


// int InsItem(linklist*L,elemtype item,int i)
// {
// int j;
// linklist*p,*t;
// p=L;
// j=1;
// t=(linklist*)malloc(sizeof(linklist));
// t->data=item;
// if(L->next==NULL)
// {
// if(i==0)
// {
// L->next=t;
// t->next=NULL;
// return(1);
// }
// else return(0);
// }
// while((p->next!=NULL)&&(j<i))
// {
// p=p->next;
// j++;
// }
// if(p==NULL)
// {
// printf("The node%d is ont exist\n",i);
// return (0);
// }
// else
// {
// t->next=p->next;
// p->next=t;
// return (1);
// }
// }
// /*
// int InsItem(linklist *L, elemtype item,  elemtype k)    //????
// {              //????L?????????item, ???????? K????????item
// linklist *q,*p,*t;
// t=(linklist*)malloc(sizeof(linklist));
// t->data=item;
// if(L->next ==NULL)
// {
// printf("The linklist is empty\n");
// return(0);
// }
// else
// {
// q=L;
// p=L->next;
// while(p!=NULL)
// if(p->data!=k)
// {
// q=p;
// p=p->next;
// }
// else   break;
// }
// if(p==NULL)
// {
// printf("The node %d is not exit\n",k); return(0);
// }
// else
// {
// q->next=t;
// t->next=p;
// return(1);
// }
// }
// */

// int DelItem(linklist*L,int i)
// {
// int j;
// linklist *p,*q;
// p=L;
// j=1;
// if(L->next==NULL)
// {
// printf("The linklist is empty.\n");
// return(0);
// }
// while((p->next!=NULL)&&(j<i))
// {
// p=p->next;
// j=j+1;
// }
// if(p==NULL)
// {
// printf("The node%d is not exist\n",i);
// return(0);
// }
// else
// {
// q=p->next;
// p->next=p->next->next;
// free(q);
// return(1);
// }
//}
// /*
// int DelItem(linklist*L,elemtype item)
// {
// linklist*q,*p,*t;
// if(L->next==NULL)
// {
// printf("The linklist is empty\n")
// return(0);
// }
// else
// {
// q=L;
// p=L->next;
// while(p!=NULL)
// if(p->data!=item)
// {
// q=p;
// p=p->next;
// }
// else
// break;
// }
// if(p==NULL)
// {
// printf("The node %d is not exist\n",k);
// return(0);
// }
// else
// {
// q->next=p->next;
// free(p);return(1);
// }
// }
// */
// void main()
// { linklist  *L,*p;
// L=Initlist(L);
// L=Creatlist(10);
// p=L;
// do
// {   p=p->next;
// 	printf("%d\n",p->data);
// }while(p->next!=NULL);

// }
