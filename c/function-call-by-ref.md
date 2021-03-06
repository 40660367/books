# C语言 传址方式调用函数

通过引用传递方式，形参为指向实参地址的指针，当对形参的指向操作时，就相当于对实参本身进行的操作。

传递指针可以让多个函数访问指针所引用的对象，而不用把对象声明为全局可访问。

```c
/* 函数定义 */
void swap(int *x, int *y)
{
   int temp;
   temp = *x;    /* 保存地址 x 的值 */
   *x = *y;      /* 把 y 赋值给 x */
   *y = temp;    /* 把 temp 赋值给 y */
  
   return;
}
```

如需了解 C 中指针的更多细节，请访问 [C语言 指针](./pointer.html) 章节。

现在，让我们通过引用传值来调用函数 **swap()**：

## 实例

文件名:function-callbyref.c

```c
#include <stdio.h>
 
/* 函数声明 */
void swap(int *x, int *y)
{
   int temp;
   temp = *x;    /* 保存地址 x 的值 */
   *x = *y;      /* 把 y 赋值给 x */
   *y = temp;    /* 把 temp 赋值给 y */
  
   return;
}

int main ()
{
   /* 局部变量定义 */
   int a = 100;
   int b = 200;
 
   printf("交换前，a 的值： %d\n", a );
   printf("交换前，b 的值： %d\n", b );
 
   /* 调用函数来交换值
    * &a 表示指向 a 的指针，即变量 a 的地址
    * &b 表示指向 b 的指针，即变量 b 的地址
   */
   swap(&a, &b);
 
   printf("交换后，a 的值： %d\n", a );
   printf("交换后，b 的值： %d\n", b );
 
   return 0;
}
```

```bash
gcc /share/lesson/c/function-callbyref.c && ./a.out
```

康康

上面的实例表明了，与传值调用不同，引用调用在函数内改变了 a 和 b 的值，实际上也改变了函数外 a 和 b 的值。