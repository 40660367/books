# Scala 访问修辞符(modifier)

Scala中的包，类或对象的成员可以使用私有(`private`)和受保护(`protected`)的访问修饰符进行标注，如果不使用这两个关键字的其中一个，那么访问将被视为公开(`public`)的。

这些修饰符限制了对某些代码区域的成员访问。要使用访问修饰符，请将其关键字包含在包，类或对象的成员的定义中。

## 私有成员

私有(`private`)成员只能在包含成员定义的类或对象内部可见。

以下是示例代码段解释私有(`private`)成员 - 

文件名:access-modifier-private.scala

```scala
class Outer {
   class Inner {
      private def f() { println("f") }

      class InnerMost {
         f() // OK
      }
   }
   (new Inner).f() // Error: f is not accessible
}
```

在Scala，访问`(new Inner). f()`是非法的，因为`f`在`Inner`类中声明为`private`，并且访问不在`Inner`类内。 相比之下，第一次在`“InnerMost”`类中访问`f()`是可以的，因为该访问包含在`Inner`类的主体中。在Java中也允许这样的两个访问，因为它允许外部类访问其内部类的私有成员。

```bash
scala /share/lesson/scala/access-modifier-private.scala
```

康康

## 受保护的成员

受保护(`protected`)成员只能从定义成员的类的子类访问。以下是说明受保护(`protected`)成员的示例代码片段 -

文件名:access-modifier-protected.scala

```scala
class Super {
    protected def f() { println("f") }
}

class Sub extends Super {
    f()
}

class Other {
    (new Super).f() // Error: f is not accessible
}
```

在`Sub`类中访问`f`是可行的，因为`f`被声明为在`Super`类中被保护，`Sub`类是`Super`的子类。 相反，不允许访问`Other`类中的`f()`方法，因为`Other`类不会从`Super`类继承。在Java中，后者的访问将仍然允许，因为`Other`类与`Sub`类在同一个包中。

```bash
scala /share/lesson/scala/access-modifier-protected.scala
```

康康

## 公有成员

不同于私有和受保护的成员，不需要为公有成员使用`Public`关键字指定。没有明确使用修饰符则自动归为公共成员。 这些成员可以从任何地方访问。

以下是解释公共成员的示例代码片段 -

文件名:access-modifier-public.scala

```scala
class Outer {
   class Inner {
      def f() { println("f") }

      class InnerMost {
         f() // OK
      }
   }
   (new Inner).f() // OK because now f() is public
}
```

```bash
scala /share/lesson/scala/access-modifier-public.scala
```

康康

## 保护作用域

Scala中的访问修饰符可以通过限定符进行扩充。

形式为`private [X]`或`protected [X]`的修饰符表示为访问是私有或受保护的“最多”到*X*，其中*X*指定一些封闭的包，类或单例对象。

文件名:access-modifier-mixed.scala

```scala
class Executive {
 private[professional] var workDetails = null
 private[society] var friends = null
 private[this] var secrets = null

 def help(another : Executive) {
    println(another.workDetails)
    println(another.secrets) //ERROR
 }
}
```

```bash
scala /share/lesson/scala/access-modifier-mixed.scala
```

康康

**注意** - 以下几点来自上面的例子总结 - 

- 变量：`workDetails`在封闭包`professional`中的任何类中可访问。
- 封闭包：`friends`的任何类都可以被`society`包中任何类访问。
- 变量：`secrets`只能在实例方法的隐式对象(`this`)中访问。