# Scala 匿名函数

Scala提供了一个相对轻量级的语法来定义匿名函数。源代码中的匿名函数称为函数文字，在运行时，函数文字被实例化为称为函数值的对象。

Scala支持一级函数，函数可以用函数文字语法表达，即`(x：Int)=> x + 1`，该函数可以由一个叫作函数值的对象来表示。

尝试以下表达式，它为整数创建一个后继函数 -

```scala
var inc = (x:Int) => x+1
```

变量`inc`现在是一种可以像函数那样使用的函数 -

```scala
var x = inc(7)-1
```

还可以如下定义具有多个参数的函数：

```scala
var mul = (x: Int, y: Int) => x*y
```

变量`mul`现在是可以像函数那样使用的函数 -

```scala
println(mul(3, 4))
```

也可以定义不带参数的函数，如下所示：

```scala
var userDir = () => { System.getProperty("user.dir") }
```

变量`userDir`现在是可以像函数那样使用的函数 -

```scala
println( userDir )
```