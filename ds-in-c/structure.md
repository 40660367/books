# 结构体(structure)			

结构是一种复合数据类型，它定义了一组变量列表，这些变量将放在一个内存块中的一个名称下。 它允许通过使用指向结构的一个指针来访问不同的变量。

语法如下:

```c
struct structure_name   
{  
    data_type member1;  
    data_type member2;  
    ...  
    ...
    data_type memeber;  
};
```

**结构体优点**

- 可以保存不同数据类型的变量。
- 可以创建包含不同类型属性的对象。
- 允许跨程序重用数据布局。
- 用于实现其他数据结构，如链表，堆栈，队列，树，图等。

**示例程序**

文件名:structure-sample.c

```c
#include<stdio.h>  
#include<conio.h>  
void main( )  
{  
struct employee  
{  
    int id ;  
    float salary ;  
    int mobile ;  
};
// 定义结构体变量
    struct employee e1,e2,e3 ;  
    clrscr();  
    printf ("\nEnter ids, salary & mobile no. of 3 employee\n"  
    scanf ("%d %f %d", &e1.id, &e1.salary, &e1.mobile);  
    scanf ("%d%f %d", &e2.id, &e2.salary, &e2.mobile);  
    scanf ("%d %f %d", &e3.id, &e3.salary, &e3.mobile);  
    printf ("\n Entered Result ");  
    printf ("\n%d %f %d", e1.id, e1.salary, e1.mobile);  
    printf ("\n%d%f %d", e2.id, e2.salary, e2.mobile);  
    printf ("\n%d %f %d", e3.id, e3.salary, e3.mobile);  
    getch();  
}
```

```bash
gcc /share/lesson/data-structure/structure-sample.c -Wformat=0
./a.out
```

康康