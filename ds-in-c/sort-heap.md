# 堆排序(heap sort)

堆排序通过使用给定数组的元素创建最小堆或最大堆来处理元素。 最小堆或最大堆表示数组的顺序，其中根元素表示数组的最小或最大元素。 在每个步骤中，堆的根元素被删除并存储到已排序的数组中，堆将再次堆积。

堆排序基本上递归地执行两个主要操作。

- 使用数组`ARR`的元素构建堆`H`。
- 重复删除阶段`1`中形成的堆的根元素。

**复杂度**

| 复杂性     | 最好情况     | 平均情况     | 最坏情况     |
| ---------- | ------------ | ------------ | ------------ |
| 时间复杂性 | Ω(n log (n)) | θ(n log (n)) | O(n log (n)) |
| 空间复杂性 | -            | -            | O(1)         |

**算法**

```
HEAP_SORT(ARR, N)

第1步 : [构建堆 H]
    重复 i=0 到 N-1
    CALL INSERT_HEAP(ARR, N, ARR[i])
    [结束循环]
第2步 : 反复删除根元素
    当 N > 0 时，重复执行
    CALL Delete_Heap(ARR,N,VAL)
    SET N = N+1 
    [结束循环]
第3步: 结束
```

## 使用C语言实现堆排序算法

文件名:sort-heap.c

```c
#include<stdio.h>  
int temp;  

void heapify(int arr[], int size, int i)  
{  
    int largest = i;    
    int left = 2*i + 1;    
    int right = 2*i + 2;    

    if (left < size && arr[left] >arr[largest])  
        largest = left;  

    if (right < size && arr[right] > arr[largest])  
        largest = right;  

    if (largest != i)  
    {  
        temp = arr[i];  
        arr[i]= arr[largest];   
        arr[largest] = temp;  
        heapify(arr, size, largest);  
    }  
}  

void heapSort(int arr[], int size)  
{  
    int i;  
    for (i = size / 2 - 1; i >= 0; i--)  
    heapify(arr, size, i);  
    for (i=size-1; i>=0; i--)  
    {  
        temp = arr[0];  
        arr[0]= arr[i];   
        arr[i] = temp;  
        heapify(arr, i, 0);  
    }  
}  

void main()  
{  
    int arr[] = {1, 10, 2, 3, 4, 1, 2, 100,23, 2};  
    int i;  
    int size = sizeof(arr)/sizeof(arr[0]);  

    heapSort(arr, size);  

    printf("printing sorted elements\n");  
    for (i=0; i<size; ++i)  
        printf("%d\n",arr[i]);  
}
```

```bash
gcc /share/lesson/data-structure/sort-heap.c && ./a.out
```

康康