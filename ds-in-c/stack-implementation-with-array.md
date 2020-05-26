# 堆栈 数组实现堆栈

在数组实现中，通过使用数组形成堆栈。 关于堆栈的所有操作都是使用数组执行的。 下面来看看如何使用数组数据结构在堆栈上实现每个操作。

#### 1. 在堆栈中添加元素(推送操作)

将元素添加到堆栈顶部称为推送操作。推送操作包括以下两个步骤。
增加变量`top`，使其现在可以引用到下一个内存位置。
在顶部位置添加元素，这个操作称为在堆栈顶部添加新元素。
当尝试将一个元素插入一个完全填充的堆栈时，堆栈溢出，因此，`main()`函数必须始终避免堆栈溢出条件。

**算法**

```
开始   
    if top = n 那么堆栈满   
    top = top + 1  
    stack (top) : = item;  
结束
```

时间复杂度为：`o(1)`

C语言中推送算法的实现 - 

```c
void push (int val,int n) //n is size of the stack   
{  
    if (top == n ){
        printf("Overflow\n");   
    }else   
    {  
        top = top + 1;   
        stack[top] = val;   
    }   
}
```

#### 2. 从堆栈中删除元素(弹出操作)

从堆栈顶部删除元素称为弹出操作。 每当从堆栈中删除一个项目时，变量`top`的值将增加`1`。 堆栈的最顶层元素存储在另一个变量中，然后顶部递减`1`。该操作返回作为结果存储在另一个变量中的已删除值。

当尝试从已经空的堆栈中删除元素时，会发生下溢情况。

**算法**

```
开始
    if top = 0 那么堆栈为空;   
    item := stack(top);  
    top = top ? 1;  
结束
```

时间复杂度为：`o(1)`

**使用C语言实现弹出算法**

```c
int pop ()  
{   
    if(top == -1)   
    {  
        printf("Underflow");  
        return 0;  
    }  
    else  
    {  
        return stack[top -- ];   
    }    
}
```

#### 3. 访问堆栈的每个元素(Peek操作)

Peek操作涉及返回堆栈顶部存在的元素但不删除它。如果尝试返回已经空堆栈中的顶部元素，则可能发生下溢情况。

**算法：**

```
开始
    if top = -1 那么堆栈   
    item = stack[top]   
    return item  
结束
```

时间复杂度为：`o(1)`

**用C语言实现Peek算法**

```c
int peek()  
{  
    if (top == -1)   
    {  
        printf("Underflow");  
        return 0;   
    }  
    else  
    {  
        return stack [top];  
    }  
}
```

## C语言实现的示例代码

文件名:stack-implementation-with-array.c

```c
#include <stdio.h>   
int stack[100], i, j, choice = 0, n, top = -1;
void push();
void pop();
void show();
void main()
{

    printf("Enter the number of elements in the stack ");
    scanf("%d", &n);
    printf("*********Stack operations using array*********");
    printf("----------------------------------------------\n");
    while (choice != 4)
    {
        printf("Chose one from the below options...\n");
        printf("1.Push\n2.Pop\n3.Show\n4.Exit");
        printf("Enter your choice \n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
        {
            push();
            break;
        }
        case 2:
        {
            pop();
            break;
        }
        case 3:
        {
            show();
            break;
        }
        case 4:
        {
            printf("Exiting....");
            break;
        }
        default:
        {
            printf("Please Enter valid choice ");
        }
        };
    }
}

void push()
{
    int val;
    if (top == n)
        printf("Overflow");
    else
    {
        printf("Enter the value?");
        scanf("%d", &val);
        top = top + 1;
        stack[top] = val;
    }
}

void pop()
{
    if (top == -1)
        printf("Underflow");
    else
        top = top - 1;
}
void show()
{
    for (i = top;i >= 0;i--)
    {
        printf("%d\n", stack[i]);
    }
    if (top == -1)
    {
        printf("Stack is empty");
    }
}
```

```bash
gcc /share/lesson/data-structure/stack-implementation-with-array.c && ./a.out
```

康康