# C语言 逻辑判断嵌套switch语句

您可以把一个 **switch** 作为一个外部 **switch** 的语句序列的一部分，即可以在一个 **switch** 语句内使用另一个 **switch** 语句。即使内部和外部 switch 的 case 常量包含共同的值，也没有矛盾。

## 语法

C 语言中 **嵌套 switch** 语句的语法：

```c
switch(ch1) {
   case 'A': 
      printf("这个 A 是外部 switch 的一部分" );
      switch(ch2) {
         case 'A':
            printf("这个 A 是内部 switch 的一部分" );
            break;
         case 'B': /* 内部 B case 代码 */
      }
      break;
   case 'B': /* 外部 B case 代码 */
}
```

## 实例

文件名:logic-switchnested.c

```c
#include <stdio.h>
 
int main ()
{
   /* 局部变量定义 */
   int a = 100;
   int b = 200;
 
   switch(a) {
      case 100: 
         printf("这是外部 switch 的一部分\n");
         switch(b) {
            case 200:
               printf("这是内部 switch 的一部分\n");
         }
   }
   printf("a 的准确值是 %d\n", a );
   printf("b 的准确值是 %d\n", b );
 
   return 0;
}
```

```bash
gcc /share/lesson/c/logic-switchnested.c && ./a.out
```

康康