# R语言 变量(variable)
变量为我们提供了我们的程序可以操作的命名存储。 R语言中的变量可以存储原子向量，原子向量组或许多Robject的组合。 有效的变量名称由字母，数字和点或下划线字符组成。 变量名以字母或不以数字后跟的点开头。

|变量名|合法性|	原因|
|:--|:--|:--|
|`var_name2.`	|有效	|有字母，数字，点和下划线|
|`VAR_NAME％`	|无效	|有字符'％'。只有点(.)和下划线允许的。|
|`2var_name`	|无效	|以数字开头|
|`.var_name`,`var.name`|	有效|	可以用一个点(.)，但启动点(.)，不应该后跟一个数字。|
|`.2var_name`	|无效	|起始点后面是数字使其无效。|
|`_var_name`	|无效	|开头_这是无效的|

## 变量赋值
可以使用向左，向右和等于运算符来为变量分配值。 可以使用`print()`或`cat()`函数打印变量的值。 `cat()`函数将多个项目组合成连续打印输出。
```R
# Assignment using equal operator.
var.1 = c(0,1,2,3)           

# Assignment using leftward operator.
var.2 <- c("learn","R")   

# Assignment using rightward operator.   
c(TRUE,1) -> var.3           

print(var.1)
```

注 :向量`c`（TRUE，1）具有逻辑和数值类的混合。 因此，逻辑类强制转换为数字类，使TRUE为1。


## 变量的数据类型
在R语言中，变量本身没有声明任何数据类型，而是获取分配给它的R - 对象的数据类型。 所以R称为动态类型语言，这意味着我们可以在程序中使用同一个变量时，一次又一次地更改变量的数据类型。
```R
var_x <- "Hello"
cat("The class of var_x is ",class(var_x),"")

var_x <- 34.5
cat("  Now the class of var_x is ",class(var_x),"")

var_x <- 27L
cat("   Next the class of var_x becomes ",class(var_x),"")
```
## 查找变量
要知道工作空间中当前可用的所有变量，我们使用`ls()`函数。 `ls()`函数也可以使用模式来匹配变量名。注意:`ls()`取决于在您的环境中声明的变量。
```R
ls()
```

## 删除变量
可以使用`rm()`函数删除变量。 下面我们删除变量`var.3`。 打印时，抛出变量错误的值。
```R
rm(var.3)
print(var.3)
```
