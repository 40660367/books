# R语言 语法(syntax)
我们将开始学习R语言编程，首先编写一个“你好，世界！ 的程序。 根据需要，您可以在R语言命令提示符处编程，也可以使用R语言脚本文件编写程序。 让我们逐个体验不同之处。

## 命令提示符
如果你已经配置好R语言环境，那么你只需要按一下的命令便可轻易开启命令提示符`R`，这将启动R语言解释器，在交互环境下，你会得到一个提示`>`。在那里你可以开始输入你的程序，具体如下：
```R
myString <- "Hello, World!"
print(myString)
```
在这里，第一个语句先定义一个字符串变量`myString`，并将“Hello，World！”赋值其中，第二句则使用`print()`语句将变量`myString`的内容进行打印。

## 脚本文件
通常，您将通过在脚本文件中编写程序来执行编程，然后在命令提示符下使用R解释器（称为Rscript）来执行这些脚本。 所以让我们开始在一个命名为test.R的文本文件中编写下面的代码
```
# My first program in R Programming
myString <- "Hello, World!"
print(myString)
```
将上述代码保存在test.R文件中，并在Linux命令提示符下执行，如下所示。 即使您使用的是Windows或其他系统，语法也将保持不变。
```
Rscript test.R
```
当我们运行上面的程序，它产生以下结果。`[1] "Hello, World!"`
## 注释
注释能帮助您解释R语言程序中的脚本，它们在实际执行程序时会被解释器忽略。 单个注释使用＃在语句的开头写入，如下所示
`# My first program in R Programming`
R语言不支持多行注释，但你可以使用一个小技巧，如下
```R
if(FALSE) {
   "This is a demo for multi-line comments and it should be put inside either a single
      OR double quote"
}

myString <- "Hello, World!"
print(myString)
```
虽然上面的注释将由R解释器执行，但它们不会干扰您的实际程序。 但是你必须为内容加上单引号或双引号。