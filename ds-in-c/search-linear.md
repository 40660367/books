# 线性搜索 			

搜索是在列表中查找某个特定元素的过程。 如果元素存在于列表中，则该过程称为成功，并且该过程返回该元素的位置，否则搜索将被称为不成功。

有两种流行的搜索方法被广泛用于在列表中搜索某些项目。 但是，算法的选择取决于列表的排列。

- 线性搜索
- 二进制搜索

## 线性搜索

线性搜索是最简单的搜索算法，通常称为顺序搜索。 在这种类型的搜索中，只是完全遍历列表，并将列表中的每个元素与要找到其位置的项匹配。如果找到匹配，则返回项目的位置，否则算法返回`NULL`。
线性搜索主要用于搜索未排序项目的无序列表。 线性搜索算法如下。

```
LINEAR_SEARCH(A，N，VAL)
第1步：[INITIALIZE] SET POS = -1
第2步：[INITIALIZE] SET I = 1
第3步：当I <= N 时重复第4步
第4步：如果 A [I] = VAL
    SET POS = I
    打印POS
    转到第6步
    [IF结束]
    SET I = I + 1
    [循环结束]
第5步：IF POS = -1
    打印“值不在数组中”
    [IF结束]
第6步：退出
```

**算法的复杂性**

| 复杂度 | 最好情况 | 平均情况 | 最坏情况 |
| ------ | -------- | -------- | -------- |
| 时间   | O(1)     | O(n)     | O(n)     |
| 空间   | —        | —        | O(1)     |

## C语言实现代码

文件名:search-linear.c

```c
#include<stdio.h>   
void main ()  
{  
    int a[10] = {10, 23, 40, 1, 2, 0, 14, 13, 50, 9};  
    int item, i,flag;  
    printf("Enter Item which is to be searched\n");  
    scanf("%d",&item);  
    for (i = 0; i< 10; i++)  
    {  
        if(a[i] == item)   
        {  
            flag = i+1;  
            break;  
        }   
        else   
        flag = 0;  
    }   
    if(flag != 0)  
    {  
        printf("Item found at location %d\n",flag);  
    }  
    else  
    {  
        printf("Item not found\n");   
    }  
}
```

```bash
gcc /share/lesson/data-structure/search-linear.c && ./a.out
```

康康