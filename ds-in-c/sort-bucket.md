# 桶排序(bucket sort)

存储桶排序也称为*bin* 排序。它的工作原理是将元素分配到也称为存储桶的数组中。 桶使用不同的排序算法单独排序。

**桶排序的复杂性**

| 算法     | 复杂性 |
| -------- | ------ |
| 空间     | O(1)   |
| 最坏情况 | O(n^2) |
| 最好情况 | Ω(n+k) |
| 平均情况 | θ(n+k) |

**算法**

```
第1步，开始
第2步，设置一个最初为空的“桶”(`buckets`)数组。
第3步，分散：遍历原始数组，将每个对象放入其存储桶中。
第4步，对每个非空桶进行排序。
第5步，收集：按顺序访问存储桶并将所有元素放回原始数组中。
第6步，停止
```

## 使用C语言实现桶排序算法如下 

文件名:sort-bucket.c

```c
#include <stdio.h>  
void Bucket_Sort(int array[], int n)  
{    
    int i, j;    
    int count[n];   
    for (i = 0; i < n; i++)  
        count[i] = 0;  

    for (i = 0; i < n; i++)  
        (count[array[i]])++;  

    for (i = 0, j = 0; i < n; i++)    
        for(; count[i] > 0; (count[i])--)  
            array[j++] = i;  
}     
/* End of Bucket_Sort() */  

/* The main() begins */  
int main()  
{  
    int array[100], i, num;   

    printf("Enter the size of array : ");     
    scanf("%d", &num);     
    printf("Enter the %d elements to be sorted:\n",num);   
    for (i = 0; i < num; i++)  
        scanf("%d", &array[i]);   
    printf("The array of elements before sorting : \n");  
    for (i = 0; i < num; i++)  
        printf("%d ", array[i]);    
    printf("The array of elements after sorting : \n");   
    Bucket_Sort(array, num);   
    for (i = 0; i < num; i++)  
        printf("%d ", array[i]);     
    printf("\n");       
    return 0;  
}
```

```bash
gcc /share/lesson/data-structure/sort-bucket.c && ./a.out
```

康康