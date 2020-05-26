# 希尔排序(shell sort)

希尔(Shell)排序是插入排序的概括，它通过比较由几个位置的间隙分隔的元素来克服插入排序的缺点。 通常，希尔(Shell)排序执行以下步骤。

- 第1步：以扁平形式排列元素，并使用插入排序对列进行排序。
- 第2步：重复第1步; 每次使用较少数量的较长列，最终只需要对一列数据进行排序。

#### 复杂性

| 复杂性     | 最好情况    | 平均情况      | 最坏情况      |
| ---------- | ----------- | ------------- | ------------- |
| 时间复杂性 | Ω(n log(n)) | θ(n log(n)^2) | O(n log(n)^2) |
| 空间复杂性 | -           | -             | O(1)          |

**算法**

```
Shell_Sort(Arr, n)


第1步 : SET FLAG = 1, GAP_SIZE = N
第2步 : 当 FLAG = 1 OR GAP_SIZE > 1 时，循环第3步到第6步。
第3步 :SET FLAG = 0
第4步 :SET GAP_SIZE = (GAP_SIZE + 1) / 2
第5步 :当 I = 0 到 I < (N -GAP_SIZE) 时，循环第6步。
第6步 :IF Arr[I + GAP_SIZE] > Arr[I]
        SWAP Arr[I + GAP_SIZE], Arr[I]
        SET FLAG = 0
第7步 : 循环
```

## 使用C语言实现希尔排序

文件名:sort-shell.c

```c
#include <stdio.h>  
void shellsort(int arr[], int num)    
{    
    int i, j, k, tmp;    
    for (i = num / 2; i > 0; i = i / 2)    
    {    
        for (j = i; j < num; j++)    
        {    
            for(k = j - i; k >= 0; k = k - i)    
            {    
                if (arr[k+i] >= arr[k])    
                break;    
                else    
                {    
                    tmp = arr[k];    
                    arr[k] = arr[k+i];    
                    arr[k+i] = tmp;    
                }    
            }    
        }    
    }    
}    
int main()    
{    
    int arr[30];    
    int k,  num;    
    printf("Enter total no. of elements : ");    
    scanf("%d", &num);    
    printf("Enter %d numbers: ", num);    

    for (k =  0 ; k < num; k++)    
    {    
        scanf("%d", &arr[k]);    
    }    
    shellsort(arr, num);    
    printf("Sorted array is: ");    
    for (k = 0; k < num; k++)    
        printf("%d ", arr[k]);    
    return 0;    
}
```

```bash
gcc /share/lesson/data-structure/sort-shell.c && ./a.out
```

康康