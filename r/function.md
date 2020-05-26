# R语言 函数(function)

函数是一组组合在一起以执行特定任务的语句。 R语言具有大量内置函数，用户可以创建自己的函数。

在R语言中，函数是一个对象，因此R语言解释器能够将控制传递给函数，以及函数完成动作所需的参数。

该函数依次执行其任务并将控制返回到解释器以及可以存储在其他对象中的任何结果。

## 函数定义

使用关键字函数创建R语言的函数。 R语言的函数定义的基本语法如下

```
function_name <- function(arg_1, arg_2, ...) {
   Function body 
}
```

## 函数的组成

函数的不同部分 -
- **函数名称** -这是函数的实际名称。 它作为具有此名称的对象存储在R环境中。
- **参数** -参数是一个占位符。 当函数被调用时，你传递一个值到参数。 参数是可选的; 也就是说，一个函数可能不包含参数。 参数也可以有默认值。
- **函数体** -函数体包含定义函数的功能的语句集合。
- **返回值** -函数的返回值是要评估的函数体中的最后一个表达式。

R语言有许多内置函数，可以在程序中直接调用而无需先定义它们。我们还可以创建和使用我们自己的函数，称为用户定义的函数。

#### 练习：内置功能

内置函数的简单示例是**seq()**，**mean()**，**max()**，**sum(x)**和**paste(...)**等。它们由用户编写的程序直接调用。 您可以参考最广泛使用的R函数。
```R
# Create a sequence of numbers from 32 to 44.
print(seq(32,44))

# Find mean of numbers from 25 to 82.
print(mean(25:82))

# Find sum of numbers frm 41 to 68.
print(sum(41:68))
```

#### 练习： 用户定义的函数

我们可以在R语言中创建用户定义的函数。它们特定于用户想要的，一旦创建，它们就可以像内置函数一样使用。 下面是一个创建和使用函数的例子。

```R
# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}	
```
#### 练习： 调用函数
```R
# Create a function to print squares of numbers in sequence.
new.function <- function(a) {
   for(i in 1:a) {
      b <- i^2
      print(b)
   }
}

# Call the function new.function supplying 6 as an argument.
new.function(6)
```

#### 练习： 调用没有参数的函数

```R
# Create a function without an argument.
new.function <- function() {
   for(i in 1:5) {
      print(i^2)
   }
}	

# Call the function without supplying an argument.
new.function()
```

#### 练习：使用参数值调用函数（按位置和名称）

函数调用的参数可以按照函数中定义的顺序提供，也可以以不同的顺序提供，但分配给参数的名称。

```R
# Create a function with arguments.
new.function <- function(a,b,c) {
   result <- a * b + c
   print(result)
}

# Call the function by position of arguments.
new.function(5,3,11)

# Call the function by names of the arguments.
new.function(a = 11, b = 5, c = 3)
```

#### 练习： 使用默认参数调用函数

我们可以在函数定义中定义参数的值，并调用函数而不提供任何参数以获取默认结果。 但是我们也可以通过提供参数的新值来获得非默认结果来调用这样的函数。

```R
# Create a function with arguments.
new.function <- function(a = 3, b = 6) {
   result <- a * b
   print(result)
}

# Call the function without giving any argument.
new.function()

# Call the function with giving new values of the argument.
new.function(9,5)
```

#### 练习：功能的延迟计算

对函数的参数进行延迟评估，这意味着它们只有在函数体需要时才进行评估。

```R
# Create a function with arguments.
new.function <- function(a, b) {
   print(a^2)
   print(a)
   print(b)
}

# Evaluate the function without supplying one of the arguments.
new.function(6)
```
