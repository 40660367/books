# Java 访问修饰符

Java提供了许多访问修饰符来设置类，变量，方法和构造函数的访问级别。 四个访问级别是 - 

- 无关键字(不指定修饰符) - 对包可见，不需要修饰符。
- `private` - 仅对类内部可见。
- `public` - 公开，对外部可见。
- `protected` - 对包和所有子类可见。

## 默认访问修饰符 - 无关键字

默认访问修饰是指没有为类，字段，方法等显式声明访问修饰符。
声明没有任何访问控制修饰符的变量或方法可用于同一包中的任何其他类。 接口中的字段隐式为`public static final`，接口中的方法默认为`public`。

**示例**

可以在没有任何修饰符的情况下声明变量和方法，如以下示例所示 - 

```java
class Order{
    String version = "1.0.1";

    boolean processOrder() {
       return true;
    }
}
```

## 私有访问修饰符 - private

声明为`private`的方法，变量和构造函数只能在声明的类本身中访问。专用访问修饰符是限制性最强的访问级别。类和接口不能声明为：`private`。
如果类中存在公共`getter`方法，则可以在类中将变量声明为`private`。使用`private`修饰符是对象封装自身并隐藏来自外部世界的数据的主要方式。

**示例**
以下类使用`private`访问控制

```java
public class Logger {
   private String format;

   public String getFormat() {
      return this.format;
   }

   public void setFormat(String format) {
      this.format = format;
   }
}
```

这里，`Logger`类的`format`变量是`private`，因此其他类无法直接检索或设置它的值。

因此，为了使这个变量对外界可用，`Logger`类中定义了两个公共方法：`getFormat()`用于返回`format`的值，`setFormat(String)`用于设置它的值。

## 公共访问修饰符 - public

可以从任何其他类访问使用`public`声明的类，方法，构造函数，接口等。 因此，可以从属于Java任何类访问在公共类中声明的字段，方法，块。

但是，如果尝试访问的公共类位于不同的包中，则仍需要导入公共类。 由于类继承，类的所有公共方法和变量都由其子类继承。

**示例**

以下方法使用`public`访问控制 - 

```java
public static void main(String[] arguments) {
   // ...
}
```

应用程序的`main()`方法必须声明为`public`。否则Java解释器无法调用它来运行该类。

## 受保护的访问修饰符 - protected

在超类中声明受保护的变量，方法和构造函数只能由其他包中的子类或受保护成员类的包中的任何类访问。
受保护的访问修饰符不能应用于类和接口。 方法，字段可以声明为`protected`，但是接口中的方法和字段不能声明为`protected`。受保护的访问使子类有机会使用辅助方法或变量，同时防止非相关类尝试使用它。

**示例**
以下父类使用`protected`访问控制，以允许它的子类覆盖`openSpeaker()`方法 - 

```java
class AudioPlayer {
   protected boolean openSpeaker(Speaker sp) {
      // 实现详细代码...
   }
}

class StreamingAudioPlayer {
   boolean openSpeaker(Speaker sp) {
      // 实现详细代码...
   }
}
```

在这里，如果将`openSpeaker()`方法定义为`private`，那么它将无法从`AudioPlayer`以外的任何其他类访问。 如果将类定义为`public`，那么它将被所有外部世界类访问。 但这里的目的是仅将此方法暴露给它的子类，所以只使用`protected`修饰符。

**访问控制和继承**

强制执行以下继承方法规则 - 

- 在超类中声明为`public`的方法也必须在所有子类中都是`public`。
- 在超类中声明为`protected`的方法必须在子类中也要声明为：`protected`或`public`; 不能声明为：`private`。
- 声明为`private`的方法根本不能被继承，因此没有规则。