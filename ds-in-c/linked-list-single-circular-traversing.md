# 循环单向链表 遍历

遍历循环单链表可以通过循环完成。 将临时指针变量`temp`初始化为`head`指针并运行`while`循环，直到`temp`的`next`指针变为`head`。 算法和实现该算法的c函数描述如下。

**算法**

```
第1步：设置PTR = HEAD
第2步：如果PTR = NULL
        提示 内存溢出
        转到第8步
    [IF结束]

第4步：重复第5步和第6步直到 PTR→NEXT！= HEAD
第5步：打印PTR→DATA
第6步：PTR = PTR→NEXT
[循环结束]

第7步：打印PTR->DATA
第8步：退出
```

## C语言实现的示例代码

文件名:linked-list-single-circular-traversing.c

```c
#include<stdio.h>  
#include<stdlib.h>  
void create(int);
void traverse();
struct node
{
    int data;
    struct node *next;
};
struct node *head;
void main()
{
    int choice, item;
    do
    {
        printf("1.Append List\\n2.Traverse\\n3.Exit\\n4.Enter your choice?");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the item\\n");
            scanf("%d", &item);
            create(item);
            break;
        case 2:
            traverse();
            break;
        case 3:
            exit(0);
            break;
        default:
            printf("Please enter valid choice\\n");
        }

    } while (choice != 3);
}
void create(int item)
{

    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    struct node *temp;
    if (ptr == NULL)
    {
        printf("OVERFLOW\\n");
    }
    else
    {
        ptr->data = item;
        if (head == NULL)
        {
            head = ptr;
            ptr->next = head;
        }
        else
        {
            temp = head;
            while (temp->next != head)
                temp = temp->next;
            ptr->next = head;
            temp->next = ptr;
            head = ptr;
        }
        printf("Node Inserted\\n");
    }

}
void traverse()
{
    struct node *ptr;
    ptr = head;
    if (head == NULL)
    {
        printf("nothing to print");
    }
    else
    {
        printf("printing values ... \\n");

        while (ptr->next != head)
        {

            printf("%d\\n", ptr->data);
            ptr = ptr->next;
        }
        printf("%d\\n", ptr->data);
    }

}
```

```bash
gcc /share/lesson/data-structure/linked-list-single-circular-traversing.c && ./a.out
```

康康