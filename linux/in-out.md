# Linux 输入输出，重定向,管道符

在Linux系统中，有4个特殊的符号，`<`, `>`, `|`, `-`，在我们处理输入和输出时存在重要但具有迷惑性的作用。

## Linux输入与输出
Linux终端用1表示标准输出，2表示标准错误。

默认Linux的命令的结果都是输出到标准输出，错误信息 (比如命令未找到或文件格式识别错误等) 输出到标准错误，而标准输出和标准错误默认都会显示到屏幕上。

`>`表示重定向标准输出，`> filename`就是把标准输出存储到文件filename里面。标准错误还是会显示在屏幕上。

`<`标准输入，后面可以跟可以产生输出的命令，一般用于1个程序需要多个输入的时候。

`2 >&1` 表示把标准错误重定向到标准输出。

`-` (短横线)：表示标准输入，一般用于1个程序需要多个输入的时候。

## 练习：
下面我们通过创建一个脚本stdout_error.sh来练习
```bash
cd ~
cat > stdout_error.sh  << END
echo "I am std output"
unexisted_command
END
# unexisted_command是随便写的一个理论上不存在的命令, 理论上会报错的。
```

```bash
#使用bash运行这个脚本
# 标准输出和标准错误默认都会显示到屏幕上
bash stdout_error.sh 
```

```bash
# >把结果输入到了文件；标准错误还显示在屏幕上
bash stdout_error.sh > stdout_error.stdout
```

```bash
# >把结果输入到了文件; 2>把标准错误输入到了另一个文件
bash stdout_error.sh >stdout_error.stdout 2>stdout_error.stderr
cat stdout_error.stderr
```

```bash
# 标准输出和标准错误写入同一个文件
bash stdout_error.sh >stdout_error.stdout 2>&1
cat stdout_error.stdout
```

## 管道符和标准输入的使用

`|`管道符，表示把前一个命令的输出作为后一个命令的输入，前面也有一些展示例子。用于数据在不同的命令之间传输，用途是减少硬盘存取损耗。

### 练习：管道符的使用
```bash
# 第一个命令的输出作为第二个的输入
# tr: 是用于替换字符的，把空格替换为换行，文字就从一行变为了一列
cat stdout_error.sh | tr ' ' '\n'
echo "1 2 3 A B C" | tr ' ' '\n'
```

### 练习：
```bash
# cat命令之前也用过，输出一段文字
# diff是比较2个文件的差异的，需要2个参数
# - (短横线)表示上一个命令的输出，传递给diff
# < 表示其后的命令的输出，也重定向给diff
cat << END | diff - <(echo "1 2 3" | tr ' ' '\n')
2
3
4
END
```

### 练习：
```bash
# 如果不使用管道和重定向标准输入，程序是这么写的
# 先把第一部分存储为1个文件
cat << END > firstfile
2
3
4
END
cat firstfile 

# 再把第二部分存储为1个文件
echo "1 2 3" | tr ' ' '\n' >secondfile

# 然后比较
diff firstfile secondfile 
```

## 练习：
```bash
echo  "actg aaaaa cccccg" | tr ' ' '\n' | wc -l
```

## 练习：
```bash
# sed =：先输出行号，再输出每行的内容
echo  "a b c" | tr ' ' '\n' | sed =  
```
## 练习：
```bash
# sed = 同时输出行号
# N: 表示读入下一行；sed命令每次只读一行，加上N之后就是缓存了第2行，所有的操作都针对第一行；
# s: 替换；把换行符替换为\t
echo  "a b c" | tr ' ' '\n' | sed = | sed 'N;s/\n/\t/' 
```

## 练习：
```bash
# 后面这个命令不太好解释
# sed = 同时输出行号
# N: 表示读入下一行；sed命令每次只读一行，加上N之后就是缓存了第2行，所有的操作都针对第一行；
# s: 替换；把读取的奇数行行首加一个'>'（偶数行相当于被隐藏了）
echo  "a b c" | tr ' ' '\n' | sed = | sed 'N;s/^/>/' 
```

## 练习：把多条序列转成FATSA格式
```bash
# sed = 同时输出行号
# N: 表示读入下一行；sed命令每次只读一行，加上N之后就是缓存了第2行，所有的操作都针对第一行；
# s: 替换；把读取的奇数行行首加一个'>'（偶数行相当于被隐藏了）
# 于是FASTA格式序列就出来了
echo  "actg aaaaa cccccg" | tr ' ' '\n' | sed = | sed 'N;s/^/>/' 
```

