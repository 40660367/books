# Shell 函数(function)

函数允许您对分解成更小的，逻辑子部分，然后可以被要求执行各项任务时，它需要一个脚本的整体功能。

使用函数来执行重复性的任务，是一个很好的方式来创建代码的重用。代码重用是现代面向对象编程的原则的重要组成部分。

Shell函数是类似于其他编程语言中的子程序，过程和函数。

## 	创建函数：

声明一个函数，只需使用以下语法：

```shell
function_name () { 
   list of commands
}
```

函数名 function_name，这就是你将使用它从其他地方在你的脚本调用。函数名必须遵循括号内，后括号内的命令的列表。

### 	例如：

以下是使用函数简单的例子：

文件名:function.sh

```shell
#!/bin/sh

# Define your function here
Hello () {
   echo "Hello World"
}

# Invoke your function
Hello
```

当你想执行上面的脚本，它会产生以下结果：

```bash
bash /share/lesson/shell/function.sh
```

## 	参数传递给函数：

你可以定义一个函数，它接受参数，而调用这些函数。将这些参数代表$1，$2，依此类推。

以下是一个例子，我们传递两个参数Zara和Ali ，然后我们捕获和打印这些参数函数。

文件名:function-parm.sh

```shell
#!/bin/sh

# Define your function here
Hello () {
   echo "Hello World $1 $2"
}

# Invoke your function
Hello Lucy Liu
```

这将产生以下结果：

```bash
bash /share/lesson/shell/function-parm.sh
```

## 	从函数的返回值：

如果你执行一个exit命令从一个函数内部，其效果不仅是终止执行的功能，而且Shell 程序中调用该函数。

如果你不是想，只是终止执行该函数，再有就是退出来的一个定义的函数。

根据实际情况，你可以从你的函数返回任何值，使用返回的命令，其语法如下：

```shell
return code
```

这里的代码可以是任何你选择这里，但很明显，你应该选择你的脚本作为一个整体的背景下是有意义的或有用的东西。

### 	例子：

下面的函数返回一个值：

文件名:function-return.sh

```shell
#!/bin/sh

# Define your function here
Hello () {
   echo "Hello World $1 $2"
   return 10
}

# Invoke your function
Hello Lucy Liu

# Capture value returnd by last command
ret=$?

echo "Return value is $ret"
```

```bash
bash /share/lesson/shell/function-return.sh
```

## 	嵌套函数：

函数更有趣的功能之一是，他们可以调用本身以及调用其他函数。被称为递归函数调用自身的函数。

经过简单的例子演示了一个嵌套的两个函数：

文件名:function-loop.sh

```shell
#!/bin/sh

# Calling one function from another
number_one () {
   echo "This is the first function speaking..."
   number_two
}

number_two () {
   echo "This is now the second function speaking..."
}

# Calling function one.
number_one
```

这将产生以下结果：

```bash
bash /share/lesson/shell/function-loop.sh
```

## 	从文件中导入函数：

```bash
. /share/lesson/shell/function-loop.sh
```

这样做的效果造成在function-loop.sh内定义的函数，被导入到当前环境。

我们进行调用以及证明：

```bash
number_one && number_two
```

要删除从 shell 函数的定义，可以使用unset命令

```bash
unset number_two && number_two
```

