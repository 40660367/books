# Java switch语句

`switch`语句用于测试变量与值列表的相等性。 每个值称为一个`case`，并且针对每种情况检查对应的变量值。

**语法**
增强`for`循环的语法是

```java
switch(expression) {
   case value :
      // 执行语句块
      break; // 可选

   case value :
      // 执行语句块
      break; // 可选

   // 可以拥有任意数量的 case 语句。
   default : // 可选
      // 执行语句块
}
```

以下是适用于`switch`语句的规则 - 

- `switch`语句中使用的变量只能是整数，可转换为整数(如：`byte`，`short`，`char`)，字符串和枚举类型。
- 可以在`switch`中包含任意数量的`case`语句。每个`case`后跟要与之比较的值和冒号。
- `case`的值必须与`switch`中的变量具有相同的数据类型，并且必须是常量或文字。
- 当`switch`的变量等于`case`中的值时，该`case`之后的语句将一直执行，直到达到`break`语句。
- 当达到`break`语句时`switch`终止，控制流跳转到`switch`语句块后面的下一行代码。
- 不是每个`case`都需要包含`break`语句。 如果没有指定`break`语句，则控制流将落到后续`case`中，直到达到`break`语句。
- `switch`语句可以有一个可选的`default`，它必须出现在`switch`语句的末尾。 当没有任何`case`匹配时，执行`default`中的代码块。`default`中不需要`break`语句。

![Switch语句流程图](./images/switch.jpg)

**示例1**

文件名:SwitchExample1.java

```java
public class SwitchExample1 {
    public static void main(String[] args) {
        // 为switch表达式声明一个变量
        int number = 20;
        // Switch表达式
        switch (number) {
        // Case语句
        case 10:
            System.out.println("10");
            break;
        case 20:
            System.out.println("20");
            break;
        case 30:
            System.out.println("30");
            break;
        // Default case statement
        default:
            System.out.println("Not in 10, 20 or 30");
        }
    }
}
```

```shell
cd ~/java && javac SwitchExample1.java
java SwitchExample1
```

康康

**示例2**

文件名:SwitchExample2.java

```java
public class SwitchExample2 {
    public static void main(String args[]) {
        // char grade = args[0].charAt(0);
        char grade = 'B';

        switch (grade) {
        case 'A':
            System.out.println("相当优秀!");
            break;
        case 'B':
        case 'C':
            System.out.println("一般优秀");
            break;
        case 'D':
            System.out.println("还不错");
        case 'F':
            System.out.println("好像不太行");
            break;
        default:
            System.out.println("无效级别");
        }
        System.out.println("您的级别是：" + grade);
    }
}
```

```shell
cd ~/java && javac SwitchExample2.java
java SwitchExample2
```

康康