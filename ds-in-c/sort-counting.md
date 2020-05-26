# 计数排序(counting sort)

它是一种基于键的分类技术，即根据小整数的键收集对象。 计数排序计算对象的出现次数并存储其键值。 通过添加先前的键元素并分配给对象来形成新数组。

#### 1. 复杂性

- **时间复杂度** ：`O(n + k)`是最坏的情况，其中`n`是元素的数量，`k`是输入的范围。
- **空间复杂度** ：`O(k)`- `k`是输入范围。

| 复杂度     | 最好情况 | 平均情况 | 最坏情况 |
| ---------- | -------- | -------- | -------- |
| 时间复杂度 | Ω(n+k)   | θ(n+k)   | O(n+k)   |
| 空间复杂度 | -        | -        | O(k)     |

#### 2. 计数排序的限制

- 范围不大于对象数时有效。
- 它不是基于比较的复杂度。
- 它也被用作不同算法的子算法。
- 它使用部分散列技术来计算出现次数。
- 它也用于负输入。

**算法**

```
第1步，开始
第2步，存储输入数组。
第3步，按对象出现次数计算键值。
第4步，通过添加以前的键元素并分配给对象来更新数组
第5步，通过将对象替换为新数组并使用`key = key-1`进行排序
第6步，停止
```

使用C语言实现上面排序算法

文件名:sort-counting.c

```c
#include <stdio.h>  
void counting_sort(int A[], int k, int n)  
{  
    int i, j;  
    int B[15], C[100];  
    for (i = 0; i <= k; i++)  
        C[i] = 0;  
    for (j = 1; j <= n; j++)  
        C[A[j]] = C[A[j]] + 1;  
    for (i = 1; i <= k; i++)  
        C[i] = C[i] + C[i-1];  
    for (j = n; j >= 1; j--)  
    {  
        B[C[A[j]]] = A[j];  
        C[A[j]] = C[A[j]] - 1;  
    }  
    printf("The Sorted array is : ");  
    for (i = 1; i <= n; i++)  
        printf("%d ", B[i]);  
}  
/*  End of counting_sort()  */  

/*  The main() begins  */  
int main()  
{  
    int n, k = 0, A[15], i;  
    printf("Enter the number of input : ");  
    scanf("%d", &n);  
    printf("Enter the elements to be sorted :\n");  
    for (i = 1; i <= n; i++)  
    {  
        scanf("%d", &A[i]);  
        if (A[i] > k) {  
            k = A[i];  
        }  
    }  
    counting_sort(A, k, n);  
    printf("\n");  
    return 0;  
}
```

```bash
gcc /share/lesson/data-structure/sort-counting.c && ./a.out
```

康康