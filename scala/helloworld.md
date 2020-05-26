# Scala 运行Scala的第一个程序

Scala提供了两种编程方式

### 交互式编程

Scala 提供了交互式编程模式。我们可以在命令行中输入程序并立即查看效果。

Scala 交互式编程模式可以通过命令 Scala 来启用：

```bash
scala
```

当有紫色的`scala >`出现时，即表示已经在Scala环境中了，这时就可以与Scala进行交互了，看看有什么返回？

```lua
println("Hello World!")
```

### 脚本式编程

我们可以将 Scala 程序代码保持到一个以 scala 结尾的文件，并执行，该模式称为脚本式编程。

我们将如下代码存储在名为HelloWorld.scala的脚本文件中：

```bash
cd ~ 
#创建Scala脚本文件，并指定了该脚本的解释器为/usr/bin/scala

cat > HelloWorld.scala << EOF
object HelloWorl {
   /* 这是我的第一个 Scala 程序
    * 以下程序将输出'Hello World!' 
    */
   def main(args: Array[String]) {
      println("Hello, World! Again!") // 输出 Hello, World! Again!
   }
}
EOF
```

我们使用`scalac`命令编译它：

```bash
cd ~ 
scalac HelloWorld.scala && ls
```

也可以使用我们可以看到目录下生成了 HelloWorld2.class 文件，该文件可以在Java Virtual Machine (JVM)上运行。

```bash
scala HelloWorld
```

我们也可以直接使用`scala`命令对scala脚本进行编译和执行。

```bash
cd ~ 
scala HelloWorld.scala
```
