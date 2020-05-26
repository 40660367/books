# 双向链表 搜索特定节点

只需要遍历链表就可以搜索链表中的特定元素。执行以下操作以搜索特定操作。

- 将头指针复制到临时指针变量

  ```
  ptr
  ```

  中。

  ```c
  ptr = head;
  ```

- 声明一个局部变量

  ```
  i
  ```

  并将其赋值为

  ```
  0
  ```

  。

  ```c
  i=0;
  ```

- 遍历链表，直到指针`ptr`变为`null`。继续将指针移动到下一个并将`i`增加`1`。

- 将链表中的每个元素与要搜索的数据项进行比较。

- 如果数据项与某一节点值匹配，则从函数返回该值的位置`i`，否则将返回`NULL`。

**算法**

```
第1步：IF HEAD == NULL
   提示 “UNDERFLOW”
  转到第8步
  [IF结束]

第2步：设置PTR = HEAD
第3步：设置i = 0
第4步：重复第5步到第7步，同时PTR != NULL
第5步：IF PTR→data = item
返回 i 的值
[结束]

第6步：i = i + 1
第7步：PTR = PTR→NEXT
第8步：退出
```

## C语言实现的示例代码

文件名:linked-list-double-searching.c

```c
#include<stdio.h>  
#include<stdlib.h>  
void create(int);
void search();
struct node
{
    int data;
    struct node *next;
    struct node *prev;
};
struct node *head;
void main()
{
    int choice, item, loc;
    do
    {
        printf("1.Create\\n2.Search\\n3.Exit\\n4.Enter your choice?");
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
    if (ptr == NULL)
    {
        printf("OVERFLOW");
    }
    else
    {
        if (head == NULL)
        {
            ptr->next = NULL;
            ptr->prev = NULL;
            ptr->data = item;
            head = ptr;
        }
        else
        {
            ptr->data = item;printf("Press 0 to insert more ?\\n");
            ptr->prev = NULL;
            ptr->next = head;
            head->prev = ptr;
            head = ptr;
        }
        printf("Node Inserted\\n");
    }

}
void search()
{
    struct node *ptr;
    int item, i = 0, flag;
    ptr = head;
    if (ptr == NULL)
    {
        printf("Empty List\\n");
    }
    else
    {
        printf("Enter item which you want to search?\\n");
        scanf("%d", &item);
        while (ptr != NULL)
        {
            if (ptr->data == item)
            {
                printf("item found at location %d ", i + 1);
                flag = 0;
                break;
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
            printf("Item not found\\n");
        }
    }

}
```

```bash
gcc /share/lesson/data-structure/linked-list-double-searching.c && ./a.out
```

康康