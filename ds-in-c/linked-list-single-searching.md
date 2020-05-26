# 单链表 搜索

执行搜索以便在链表中找到指定元素的位置。 搜索链表中的任何元素都需要遍历列表，并将列表的每个元素与指定的元素进行比较。 如果元素与任何链表中的元素匹配，则从函数返回元素的位置。

**算法**

```
第1步：设置PTR = HEAD
第2步：设置I = 0
第3步：如果PTR = NULL
   提示“空列表，没有什么可以搜索”
   转到第8步
   结束IF条件

第4步：重复第5步到第7步直到PTR！= NULL
第5步：如果ptr→data = item
   写入 i + 1
  结束IF条件

第6步：I = I + 1
第7步：PTR = PTR→NEXT
[循环结束]

第8步：退出
```

## C语言实现的示例代码

文件名:linked-list-single-searching.c

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
        printf("1.Create\n");
        printf("2.Search\n");
        printf("3.Exit\n");
        printf("4.Enter your choice ? ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the item\n");
            scanf("%d", &item);
            create(item);
            break;
        case 2:
            search();
        case 3:
            exit(0);
            break;
        default:
            printf("Please enter valid choice\n");
        }

    } while (choice != 3);
}
void create(int item)
{
    struct node *ptr = (struct node *)malloc(sizeof(struct node *));
    if (ptr == NULL)
    {
        printf("OVERFLOW\n");
    }
    else
    {
        ptr->data = item;
        ptr->next = head;
        head = ptr;
        printf("Node inserted\n");
    }

}
void search()
{
    struct node *ptr;
    int item, i = 0, flag;
    ptr = head;
    if (ptr == NULL)
    {
        printf("Empty List\n");
    }
    else
    {
        printf("Enter item which you want to search?\n");
        scanf("%d", &item);
        while (ptr != NULL)
        {
            if (ptr->data == item)
            {
                printf("item found at location %d ", i + 1);
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
            printf("Item not found\n");
        }
    }

}
```

```bash
gcc /share/lesson/data-structure/linked-list-single-searching.c && ./a.out
```

康康