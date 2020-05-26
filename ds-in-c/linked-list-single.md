# 单链表

单链表是有序元素集的集合。元素的数量可以根据程序的需要而变化。 单链表中的节点由两部分组成：数据部分和链接部分。 节点的数据部分存储将由节点表示的实际信息，而节点的链接部分存储其直接后继的地址。

单向链或单链表可以仅在一个方向上遍历。也就是说每个节点只包含下一个节点的指针，因此不能反向遍历链表。

考虑一个例子，学生在三个科目的成绩存储在如图所示的链表中 -

![img](./images/linked-list-single.png)

在上图中，箭头表示链接。每个节点的数据部分包含学生在不同科目成绩。链表中的最后一个节点由空指针标识，该空指针存在于最后一个节点的地址部分中。可在链表的数据部分中包含所需的数据元素。

**复杂度**

时间复杂度 - 

| 操作 | 平均复杂度 | 最坏复杂度 |
| ---- | ---------- | ---------- |
| 访问 | θ(n)       | θ(n)       |
| 搜索 | θ(n)       | θ(n)       |
| 插入 | θ(1)       | θ(1)       |
| 删除 | θ(1)       | θ(1)       |

## 单链表上的操作

可以在单链表上执行各种操作。下面给出了所有这些操作列表。

#### 节点创建

```c
struct node   
{  
    int data;   
    struct node *next;  
};  
struct node *head, *ptr;   
ptr = (struct node *)malloc(sizeof(struct node *));
```

#### 插入

在不同位置执行插入节点到单个链表。根据插入的新节点的位置，插入分为以下类别。

| 编号 | 操作                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [插入到链表开头](./linked-list-single-insertion-at-head.html) | 它涉及在链表的前面插入任何元素。只需要进行一些链接调整，以使新节点成为链表的头部。 |
| 2    | [插入到链表末尾](./linked-list-single-insertion-at-tail.html) | 它涉及插入链表的最后一个位置。 新节点可以作为列表中的唯一节点插入，也可以作为最后一个插入。在每个场景中实现不同的逻辑。 |
| 3    | [在指定节点之后插入](./linked-list-single-insertion-after-specified-node.html) | 它涉及在链表的指定节点之后插入。需要跳过所需数量的节点才能到达指定节点，之后插入新节点。 |

#### 删除和遍历

在不同位置执行从单链表中删除节点。根据要删除的节点的位置，操作分为以下类别。

| 编号 | 操作                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [删除链表开头节点](./linked-list-single-deletion-at-head.html) | 它涉及从链表的开头节点删除。这是所有操作中最简单的操作。它只需要在节点指针中进行一些调整。 |
| 2    | [删除链表末尾节点](./linked-list-single-deletion-at-tail.html) | 它涉及删除列表的最后一个节点。链表可以为空或完整。针对不同场景实现不同的逻辑。 |
| 3    | [删除指定节点之后节点](./linked-list-single-deletion-after-specified-node.html) | 它涉及删除链表中指定节点之后的节点。需要跳过所需数量的节点才能到达节点，之后的节点将被删除。这需要遍历链表。 |
| 4    | [遍历](./linked-list-single-traversing.html)                 | 在遍历中，简单地访问链表的每个节点至少一次，以便对其执行某些特定操作，例如，打印列表中存在的每个节点的数据部分。 |
| 5    | [搜索](./linked-list-single-searching.html)                  | 在搜索中，将链表的每个元素与给定元素匹配。 如果在任何位置找到该元素，则返回该元素的位置，否则返回`null`。。 |

## C语言实现的示例代码

菜单驱动程序，用于实现单链表上的所有操作(使用C语言实现)

文件名:linked-list-single.c

```c
#include<stdio.h>  
#include<stdlib.h>  
struct node
{
    int data;
    struct node *next;
};
struct node *head;

void beginsert();
void lastinsert();
void randominsert();
void begin_delete();
void last_delete();
void random_delete();
void display();
void search();

void main()
{
    int choice = 0;
    while (choice != 9)
    {
        printf("\n\n********* 主菜单 *********\n");
        printf("从以下菜单列表中选择一个选项操作 ...\n");
        printf("===============================================\n");
        printf("1.插入到开头\n");
        printf("2.插入到结尾\n");
        printf("3.插入任何随机位置\n");
        printf("4.从头部删除\n");
        printf("5.从尾部删除\n");
        printf("6.删除指定位置后的节点\n");
        printf("7.搜索元素\n");
        printf("8.显示链表中的数据\n");
        printf("9.退出\n\n"); 
        printf("===============================================\n");
        printf("请输入您的选择：");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            beginsert();
            break;
        case 2:
            lastinsert();
            break;
        case 3:
            randominsert();
            break;
        case 4:
            begin_delete();
            break;
        case 5:
            last_delete();
            break;
        case 6:
            random_delete();
            break;
        case 7:
            search();
            break;
        case 8:
            display();
            break;
        case 9:
            exit(0);
            break;
        default:
            printf("请输入有效的选项...");
        }
    }
}
void beginsert()
{
    struct node *ptr;
    int item;
    ptr = (struct node *) malloc(sizeof(struct node *));
    if (ptr == NULL)
    {
        printf("内存不够！\n");
    }
    else
    {
        printf("请输入一个整数值：");
        scanf("%d", &item);
        ptr->data = item;
        ptr->next = head;
        head = ptr;
        printf("节点已经成功插入\n");
    }

}
void lastinsert()
{
    struct node *ptr, *temp;
    int item;
    ptr = (struct node*)malloc(sizeof(struct node));
    if (ptr == NULL)
    {
        printf("内存不够！\n");
    }
    else
    {
        printf("请输入一个整数值：");
        scanf("%d", &item);
        ptr->data = item;
        if (head == NULL)
        {
            ptr->next = NULL;
            head = ptr;
            printf("节点已经成功插入\n");
        }
        else
        {
            temp = head;
            while (temp->next != NULL)
            {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->next = NULL;
            printf("节点已经成功插入\n");

        }
    }
}
void randominsert()
{
    int i, loc, item;
    struct node *ptr, *temp;
    ptr = (struct node *) malloc(sizeof(struct node));
    if (ptr == NULL)
    {
        printf("内存不够！\n");
    }
    else
    {
        printf("请输入一个整数值：");
        scanf("%d", &item);
        ptr->data = item;
        printf("输入要插入的位置：");
        scanf("%d", &loc);
        temp = head;
        for (i = 0;i < loc;i++)
        {
            temp = temp->next;
            if (temp == NULL)
            {
                printf("此处不能插入节点\n");
                return;
            }

        }
        ptr->next = temp->next;
        temp->next = ptr;
        printf("节点已经成功插入\n");
    }
}
void begin_delete()
{
    struct node *ptr;
    if (head == NULL)
    {
        printf("链表为空，没有什么可以删除！\n");
    }
    else
    {
        ptr = head;
        head = ptr->next;
        free(ptr);
        printf("已经删除头部节点 ...\n");
    }
}
void last_delete()
{
    struct node *ptr, *ptr1;
    if (head == NULL)
    {
        printf("链表为空，没有什么可以删除！\n");
    }
    else if (head->next == NULL)
    {
        head = NULL;
        free(head);
        printf("唯一的节点已经被删除了...\n");
    }

    else
    {
        ptr = head;
        while (ptr->next != NULL)
        {
            ptr1 = ptr;
            ptr = ptr->next;
        }
        ptr1->next = NULL;
        free(ptr);
        printf("已删除最后一个节点...\n");
    }
}
void random_delete()
{
    struct node *ptr, *ptr1;
    int loc, i;
    printf("输入要在此节点之后执行删除的节点的位置：");
    scanf("%d", &loc);
    ptr = head;
    for (i = 0;i < loc;i++)
    {
        ptr1 = ptr;
        ptr = ptr->next;

        if (ptr == NULL)
        {
            printf("不能删除\n");
            return;
        }
    }
    ptr1->next = ptr->next;
    free(ptr);
    printf("\n第 %d 个节点已经被删除了", loc + 1);
}
void search()
{
    struct node *ptr;
    int item, i = 0, flag;
    ptr = head;
    if (ptr == NULL)
    {
        printf("链表为空！\n");
    }
    else
    {
        printf("请输入要搜索的项目：");
        scanf("%d", &item);
        while (ptr != NULL)
        {
            if (ptr->data == item)
            {
                printf("在 %d 位置找到数据项\n", i + 1);
                flag = 0;
            }
            else
            {
                flag = 1;
            }
            i++;
            ptr = ptr->next;
        }
        if (flag == 1)
        {
            printf("数据项未找到\n");
        }
    }

}

/**
 * 显示链表中的数据 
 */
void display()
{
    struct node *ptr;
    ptr = head;
    if (ptr == NULL)
    {
        printf("链表为空，没有数据可以显示。");
    }
    else
    {
        printf("链表中的数据值如下所示：\n");
        printf("--------------------------------------------------\n");
        while (ptr != NULL)
        {
            printf("\n%d", ptr->data);
            ptr = ptr->next;
        }
    }
    printf("\n\n\n");

}
```

```bash
gcc /share/lesson/data-structure/linked-list-single.c && ./a.out
```

康康