# 单链表  遍历

遍历是在单链表中执行的最常见操作。 遍历表示访问链表的每个节点一次，以便对其执行某些操作。这将通过使用以下语句来完成。

```c
ptr = head;   
while (ptr!=NULL)  
{  
    ptr = ptr -> next;  
}
```

**算法**

```
第1步：设置PTR = HEAD
第2步：如果PTR = NULL
    提示“空链表”
    转到第7步
   结束条件

第4步：重复第5步和第6步直到PTR！= NULL
第5步：打印PTR→DATA
第6步：PTR = PTR→NEXT
[循环结束]

第7步：退出
```

## C语言实现的示例代码

文件名:linked-list-single-traversing.c

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
        printf("1.Append List\n");
        printf("2.Traverse\n");
        printf("3.Exit\n");
        printf("4.Enter your choice ? ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter the item\n");
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
            printf("\nPlease enter valid choice\n");
        }

    } while (choice != 3);
}
void create(int item)
{
    struct node *ptr = (struct node *)malloc(sizeof(struct node *));
    if (ptr == NULL)
    {
        printf("\nOVERFLOW\n");
    }
    else
    {
        ptr->data = item;
        ptr->next = head;
        head = ptr;
        printf("\nNode inserted\n");
    }

}
void traverse()
{
    struct node *ptr;
    ptr = head;
    if (ptr == NULL)
    {
        printf("Empty list..");
    }
    else
    {
        printf("printing values . . . . .\n");
        while (ptr != NULL)
        {
            printf("\n%d", ptr->data);
            ptr = ptr->next;
        }
    }
}
```

```bash
gcc /share/lesson/data-structure/linked-list-single-traversing.c && ./a.out
```

康康