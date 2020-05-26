# 合并排序(sort merge)

合并排序是遵循分而治之的方法。 考虑一下，假设有`n`个元素的数组`A`。该算法分`3`个步骤处理元素。

1. 如果`A`包含`0`或`1`个元素，则它已经被排序，否则，将`A`分成两个具有相同数量元素的子数组。
2. 使用合并排序递归地对两个子数组进行排序。
3. 组合子数组以形成单个最终排序数组，维护数组的顺序。

合并排序背后的主要思想是，短列表需要较少的时间进行排序。

**复杂度**

| 复杂度     | 最好情况   | 平均情况   | 最坏情况   |
| ---------- | ---------- | ---------- | ---------- |
| 时间复杂度 | O(n log n) | O(n log n) | O(n log n) |
| 空间复杂度 | -          | -          | O(n)       |

**示例：**
考虑以下`7`个元素的数组，使用合并排序对数组进行排序。

```
A = {10, 5, 2, 23, 45, 21, 7}
```

**算法**

```
第1步 : [INITIALIZE] SET I = BEG, J = MID + 1, INDEX = 0
第2步 : 当(I <= MID) AND (J<=END)时，循环执行
    IF ARR[I] < ARR[J]
        SET TEMP[INDEX] = ARR[I]
        SET I = I + 1
    ELSE
        SET TEMP[INDEX] = ARR[J]
        SET J = J + 1
    [IF结束]
    SET INDEX = INDEX + 1
    [结束循环]
第3步 : [复制右子数组的其余元素(如果有的话)]
    IF I > MID
    当 while J <= END时，循环
        SET TEMP[INDEX] = ARR[J]
        SET INDEX = INDEX + 1, SET J = J + 1
        [结束循环]
        [复制右子数组的其余元素(如果有的话)]
    ELSE
        当 while I <= MID 时，循环
        SET TEMP[INDEX] = ARR[I]
        SET INDEX = INDEX + 1, SET I = I + 1
    [循环结束]
    [IF结束]
第4步 : [将TEMP的内容复制回ARR] SET K = 0
第5步 : 当 while K < INDEX 时，循环
    SET ARR[K] = TEMP[K]
    SET K = K + 1
[结束循环]
第6步 : 退出

MERGE_SORT(ARR，BEG，END)

第1步：IF BEG <END
    SET MID =(BEG + END)/ 2
    CALL MERGE_SORT(ARR，BEG，MID)
    CALL MERGE_SORT(ARR，MID + 1，END)
    MERGE(ARR，BEG，MID，END)
    [结束]
第2步：结束
```

## 使用C语言实现合并排序算法

文件名:sort-merge.c

```c
#include<stdio.h>  
void mergeSort(int[],int,int);  
void merge(int[],int,int,int);  
void main ()  
{  
    int a[10]= {10, 9, 7, 101, 23, 44, 12, 78, 34, 23};  
    int i;  
    mergeSort(a,0,9);  
    printf("printing the sorted elements");  
    for(i=0;i<10;i++)  
    {  
        printf("\n%d\n",a[i]);  
    }  

}  
void mergeSort(int a[], int beg, int end)  
{  
    int mid;  
    if(beg<end)  
    {  
        mid = (beg+end)/2;  
        mergeSort(a,beg,mid);  
        mergeSort(a,mid+1,end);  
        merge(a,beg,mid,end);  
    }  
}  
void merge(int a[], int beg, int mid, int end)  
{  
    int i=beg,j=mid+1,k,index = beg;  
    int temp[10];  
    while(i<=mid && j<=end)  
    {  
        if(a[i]<a[j])  
        {  
            temp[index] = a[i];  
            i = i+1;  
        }  
        else   
        {  
            temp[index] = a[j];  
            j = j+1;   
        }  
        index++;  
    }  
    if(i>mid)  
    {  
        while(j<=end)  
        {  
            temp[index] = a[j];  
            index++;  
            j++;  
        }  
    }  
    else   
    {  
        while(i<=mid)  
        {  
            temp[index] = a[i];  
            index++;  
            i++;  
        }  
    }  
    k = beg;  
    while(k<index)  
    {  
        a[k]=temp[k];  
        k++;  
    }  
}
```

```bash
gcc /share/lesson/data-structure/sort-merge.c && ./a.out
```

康康