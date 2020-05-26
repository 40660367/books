# 梳排序(comb sort)

梳排序是冒泡排序的推进形式。冒泡排序会比较所有相邻值，而梳排序会删除列表末尾附近的所有小值。

影响梳排序的因素有：

- 通过使用大于`1`的间隙来改进冒泡排序。
- 差距从大值开始，收缩至因子`1.3`。
- 差距缩小直到值达到`1`。

**复杂性**

| 算法         | 复杂性                  |
| ------------ | ----------------------- |
| 最坏情况     | O(n^2)                  |
| 最好情况     | θ(n log n)              |
| 平均情况     | Ω(n2/2p)其中p是增量数。 |
| 最坏空间情况 | O(1)                    |

**算法**

```
第1步，开始
第2步，如果间隙值 == 1，则计算间隙值，然后转到第5步，否则转到第3步
第3步，迭代数据集并将每个项目与间隙项目进行比较，然后转到第4步。
第4步，如果需要，请交换元素转到第2步。
第5步，打印已排序的组数。
第6步，停止
```

## 使用C语言实现桶排序算法

文件名:sort-comb.c

```c
#include <stdio.h>  
#include <stdlib.h>  
 int newgap(int gap)  
{  
    gap = (gap * 10) / 13;  
    if (gap == 9 || gap == 10)  
        gap = 11;  
    if (gap < 1)  
        gap = 1;  
    return gap;  
}  

void combsort(int a[], int aSize)  
{  
    int gap = aSize;  
    int temp, i;  
    for (;;)  
    {  
        gap = newgap(gap);  
        int swapped = 0;  
        for (i = 0; i < aSize - gap; i++)   
        {  
            int j = i + gap;  
            if (a[i] > a[j])  
            {  
                temp = a[i];  
                a[i] = a[j];  
                a[j] = temp;  
                swapped  =  1;  
            }  
        }  
        if (gap  ==  1 && !swapped)  
            break;  
    }  
}  
int main ()  
{  
    int n, i;  
    int *a;  
    printf("Please insert the number of elements to be sorted: ");  
    scanf("%d", &n);       // The total number of elements  
    a  =  (int *)calloc(n, sizeof(int));  
    for (i = 0;i< n;i++)  
    {  
        printf("Input element %d :", i);  
        scanf("%d", &a[i]); // Adding the elements to the array  
    }  
    printf("unsorted list");       // Displaying the unsorted array  
    for(i = 0;i < n;i++)  
    {  
         printf("%d", a[i]);  
    }  
    combsort(a, n);  
    printf("Sorted list:\n"); // Display the sorted array  
    for(i = 0;i < n;i++)  
    {  
        printf("%d ", (a[i]));  
    }  
    return 0;  
}
```

```bash
gcc /share/lesson/data-structure/sort-comb.c && ./a.out
```

康康