# 基数排序(radix sort)

基数(Radix)排序处理元素的方式与姓名按字母顺序排序的方式相同。在这种情况下有`26`个基数，因为英语中有`26`个字母。 在第一遍中，姓名根据名字的第一个字母的升序进行分组。

在第二遍中，名称根据第二个字母的升序进行分组。 同样的过程一直持续到我们找到已排序的名称列表。 存储桶用于存储每次传递中生成的名称。 传递次数取决于具有最大字母的名称的长度。

在整数的情况下，基数排序根据数字对数字进行排序。 比较从`LSB`到`MSB`的数字之间进行。 通过次数取决于具有最多位数的数字的长度。

#### 复杂性

| 复杂       | 最好情况 | 平均情况 | 最坏情况 |
| ---------- | -------- | -------- | -------- |
| 时间复杂性 | Ω(n+k)   | θ(nk)    | O(nk)    |
| 空间复杂性 | -        | -        | O(n+k)   |

#### 示例

考虑下面给出的长度为`6`的数组。 使用基数(Radix)排序对数组进行排序。

```
A = {10, 2, 901, 803, 1024}
```

第1步 : 根据`0`位置的数字对列表进行排序。

```
10, 901, 2, 803, 1024
```

第2步 : 根据`10`位的数字对列表进行排序。

```
02, 10, 901, 803, 1024
```

第3步 : 根据`100`位的数字对列表进行排序。

```
02, 10, 1024, 803, 901
```

第4步 : 根据`1000`位的数字对列表进行排序。

```
02, 10, 803, 901, 1024
```

因此，在第4步中生成的列表是从基数排序序列的排序列表。

#### 算法

```
第1步 : 在ARR中找到最大的数字作为LARGE
第2步 : [INITIALIZE] SET NOP = LARGE 中的位数
第3步 : SET PASS =0
第4步 : 当 PASS <= NOP-1时， 重复第5步
第5步 : SET I = 0 并初始化存储桶
第6步 : 当 I<A的长度时， 重复第5步至第7步
第7步 : SET DIGIT = A [I]中第PASS位的数字
第8步 : 将A[I]添加到编号为 DIGIT 的存储桶中
第9步 : 增量DIGIT桶数
        [结束循环]
第10步 : 收集桶中的数字
        [结束循环]
第11步 : 结束
```

## 使用C语言来实现基数排序

文件名:sort-radix.c

```c
#include <stdio.h>  
int largest(int a[]);  
void radix_sort(int a[]);  
void main()  
{  
    int i;  
    int a[10]={90,23,101,45,65,23,67,89,34,23};       
    radix_sort(a);    
    printf("The sorted array is: \n");  
    for(i=0;i<10;i++)  
        printf(" %d\t", a[i]);  
}  

int largest(int a[])  
{     
    int larger=a[0], i;   
    for(i=1;i<10;i++)  
    {  
        if(a[i]>larger)  
        larger = a[i];  
    }  
    return larger;  
}  
void radix_sort(int a[])  
{  
    int bucket[10][10], bucket_count[10];  
    int i, j, k, remainder, NOP=0, divisor=1, larger, pass;  
    larger = largest(a);  
    while(larger>0)  
    {  
        NOP++;  
        larger/=10;  
    }  
    for(pass=0;pass<NOP;pass++) // Initialize the buckets  
    {  
        for(i=0;i<10;i++)  
        bucket_count[i]=0;  
        for(i=0;i<10;i++)  
        {  
            // sort the numbers according to the digit at passth place            
            remainder = (a[i]/divisor)%10;  
            bucket[remainder][bucket_count[remainder]] = a[i];  
            bucket_count[remainder] += 1;  
        }  
        // collect the numbers after PASS pass  
        i=0;  
        for(k=0;k<10;k++)  
        {  
            for(j=0;j<bucket_count[k];j++)  
            {  
                a[i] = bucket[k][j];  
                i++;  
            }  
        }  
        divisor *= 10;  

    }  
}
```

```bash
gcc /share/lesson/data-structure/sort-radix.c && ./a.out
```

康康