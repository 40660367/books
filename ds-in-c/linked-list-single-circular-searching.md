# 循环单向链表 搜索

在循环单链表中搜索需要遍历链表。要在链表中搜索的数据项与链表的每个节点数据匹配一次，如果找到匹配，则返回该数据项的位置，否则返回`-1`。

该算法在C语言中的实现给出如下。

**算法**

```
第1步：设置PTR = HEAD
第2步：设置I = 0
第3步：如果PTR = NULL
    提示 内存溢出
    转到第8步
    [IF结束]

第4步：如果IF HEAD → DATA = ITEM
    写入i + 1返回[结束]
第5步：重复第5步到第7步直到PTR-> next！= head
第6步：如果ptr→data = item
    执行 i + 1
        返回
    [IF结束]
第7步：I = I + 1
第8步：PTR = PTR→NEXT
[循环结束]

第9步：退出
```

## C语言实现的示例代码

文件名:linked-list-single-circular-searching.c

```c
#include<stdio.h>  
#include<stdlib.h>  
void create(int);
void search();
struct node
{
    int data;
    struct node *next;
};
struct node *head;
void main()
{
    int choice, item, loc;
    do
    {
        printf("\\n1.Create\\n2.Search\\n3.Exit\\n4.Enter your choice?");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the item\\n");
            scanf("%d", &item);
            create(item);
            break;
        case 2:
            search();
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
            {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->next = head;
        }
        printf("Node Inserted\\n");
    }

}
void search()
{
    struct node *ptr;
    int item, i = 0, flag = 1;
    ptr = head;
    if (ptr == NULL)
    {
        printf("Empty List\\n");
    }
    else
    {
        printf("Enter item which you want to search?\\n");
        scanf("%d", &item);
        if (head->data == item)
        {
            printf("item found at location %d", i + 1);
            flag = 0;
            return;
        }
        else
        {
            while (ptr->next != head)
            {
                if (ptr->data == item)
                {
                    printf("item found at location %d ", i + 1);
                    flag = 0;
                    return;
                }
                else
                {
                    flag = 1;
                }
                i++;
                ptr = ptr->next;
            }
        }
        if (flag != 0)
        {
            printf("Item not found\\n");
            return;
        }
    }

}
```

```bash
gcc /share/lesson/data-structure/linked-list-single-circular-searching.c && ./a.out
```

康康