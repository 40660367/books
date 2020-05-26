# Java 修饰符类型

修饰符是一种添加到定义以更改其含义的关键字。Java语言有各种各样的修饰符，包括以下两种 - 

- [Java访问修饰符](./access-modifiers.html) - 例如：`private`,`protected`,`public`等。
- [Java非访问修饰符](./nonaccess_modifiers.html) - 例如：`static`,`final`等。

<iframe src="//player.bilibili.com/player.html?aid=48057758&bvid=BV1bb411p7D3&cid=84187051&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" height="400" width="100%" allowfullscreen="true"> </iframe>
要使用修饰符，请在类，方法或变量的定义中包含修饰符关键字。 修饰符位于语句之前，如下例所示

```java
public class className {
   // ...
}

private boolean myFlag;
static final double weeks = 9.5;
protected static final int BOXWIDTH = 42;

public static void main(String[] arguments) {
   // body of method
}
```

## 访问控制修饰符

Java提供了许多访问修饰符来设置类，变量，方法和构造函数的访问级别。 四个访问级别是 - 

- 对包可见(`default`)，不需要修饰符。
- 仅对类可见(`prive`)。
- 对所有可见(`public`)。
- 对包和所有子类可见(`protected`)。

## 非访问修饰符

Java提供了许多非访问修饰符来实现许多其他功能。

- 用于创建类方法和变量的`static`修饰符。
- 用于完成类，方法和变量的实现的`final`修饰符。
- 用于创建抽象类和方法的`abstract`修饰符。
- `synchronized`和`volatile`修饰符，用于线程。
