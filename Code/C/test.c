// #include <stdio.h>

// #include <stdlib.h>

// int main()

// {

//     printf("Hello World!\n");

//     printf("你好世界！\n");

//     system("pause");    // 防止运行后自动退出，需头文件stdlib.h

//     return 0;

// }

#include <stdio.h>
 
int age(n)
int n;
{
    int c;
    if(n==1) c=10;
    else c=age(n-1)+2;
    return(c);
}
int main()
{
    printf("%d\n",age(5));
}