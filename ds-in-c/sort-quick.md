# 快速排序(quick sort)

快速排序是广泛使用的排序算法，它在平均情况下进行`n log n`比较，用于排序`n`个元素的数组。快速排序算法遵循分而治之的方法。 此算法以下列方式处理该数组。

1. 将数组的第一个索引设置为`left`和`loc`变量。 将数组的最后一个索引设置为`right`变量。 即`left = 0`，`loc = 0`，`en d = n?1`，其中`n`是数组的长度。
2. 从数组的右边开始，从右到开扫描整个数组，将数组的每个元素与`loc`指向的元素进行比较。确保`a[loc]`小于`a[right]`。
   - 如果是这种情况，则继续进行比较，直到右边等于`loc`。
   - 如果`a[loc] > a[right]`，则交换这两个值。 然后转到第3步。
   - 设置，`loc = right`
3. 从左边指向的元素开始，并将每个元素与变量`loc`指向的元素进行比较。 确保`a[loc]> a [left]`。
   - 如果满足上面情况，则继续比较，直到`loc`等于`left`。
   - `a[loc] < a[right]`，然后交换两个值并转到第2步。
   - 设置`loc = left`。

**复杂性**

| 复杂度     | 最好情况                            | 平均情况   | 最坏情况 |
| ---------- | ----------------------------------- | ---------- | -------- |
| 时间复杂度 | O(n)用于3路分区或O(n log n)简单分区 | O(n log n) | O(n^2)   |
| 空间复杂度 | -                                   | -          | O(log n) |

**算法**

```
PARTITION (ARR, BEG, END, LOC)

第1步 : [INITIALIZE] SET LEFT = BEG, RIGHT = END, LOC = BEG, FLAG =
第2步 : 当FLAG != 1 时，重复第3步到第6步，
第3步 : 当 ARR[LOC] <=ARR[RIGHT]时，循环
        AND LOC != RIGHT
        SET RIGHT = RIGHT - 1
        [结束循环]
第4步 : IF LOC = RIGHT
        SET FLAG = 1
        ELSE IF ARR[LOC] > ARR[RIGHT]
        ARR[LOC] 与 ARR[RIGHT] 交换
        SET LOC = RIGHT
        [结束IF]
第5步 : IF FLAG = 0
        当 ARR[LOC] >= ARR[LEFT] AND LOC != LEFT 时，循环
        SET LEFT = LEFT + 1
        [结束循环]
第6步 : IF LOC = LEFT
        SET FLAG = 1
        ELSE IF ARR[LOC] < ARR[LEFT]
        ARR[LOC] 与 ARR[LEFT] 交换
        SET LOC = LEFT
        [IF结束]
        [IF结束]
第7步 : [循环结束]
第8步 : 结束
```

**算法2**

```
QUICK_SORT (ARR, BEG, END)

第1步 : IF (BEG < END)
        CALL PARTITION (ARR, BEG, END, LOC)
        CALL QUICKSORT(ARR, BEG, LOC - 1)
        CALL QUICKSORT(ARR, LOC + 1, END)
    [IF结束]
第2步 : 结束
```

## 使用C语言实现快速排序算法

文件名:sort-quick.c

```c
#include <stdio.h>  
int partition(int a[], int beg, int end);  
void quickSort(int a[], int beg, int end);  
void main()  
{  
    int i;  
    int arr[10]={90,23,101,45,65,23,67,89,34,23};  
    quickSort(arr, 0, 9);  
    printf("The sorted array is: \n");  
    for(i=0;i<10;i++)  
    printf(" %d\t", arr[i]);  
}  
int partition(int a[], int beg, int end)  
{  

    int left, right, temp, loc, flag;     
    loc = left = beg;  
    right = end;  
    flag = 0;  
    while(flag != 1)  
    {  
        while((a[loc] <= a[right]) && (loc!=right))  
        right--;  
        if(loc==right)  
        flag =1;  
        else if(a[loc]>a[right])  
        {  
            temp = a[loc];  
            a[loc] = a[right];  
            a[right] = temp;  
            loc = right;  
        }  
        if(flag!=1)  
        {  
            while((a[loc] >= a[left]) && (loc!=left))  
            left++;  
            if(loc==left)  
            flag =1;  
            else if(a[loc] <a[left])  
            {  
                temp = a[loc];  
                a[loc] = a[left];  
                a[left] = temp;  
                loc = left;  
            }  
        }  
    }  
    return loc;  
}  
void quickSort(int a[], int beg, int end)  
{  

    int loc;  
    if(beg<end)  
    {  
        loc = partition(a, beg, end);  
        quickSort(a, beg, loc-1);  
        quickSort(a, loc+1, end);  
    }  
}
```

```bash
gcc /share/lesson/data-structure/sort-quick.c && ./a.out
```

康康