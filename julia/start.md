# Julia 开始

## 开始

Julia 的安装，不管是使用编译好的程序，还是自己从源代码编译，都很简单。按照 这儿 的说明下载并安装即可。

使用交互式会话（也记为 repl），是学习 Julia 最简单的方法：`julia`


```julia
1 + 2
```

输入 `^D` — `ctrl` 键加 `d` 键，或者输入 `quit()` ，可以退出交互式会话。交互式模式下， `julia` 会显示一个横幅，并提示用户来输入。一旦用户输入了完整的表达式，例如 `1 + 2` ，然后按回车，交互式会话就对表达式求值并返回这个值。如果输入的表达式末尾有分号，就不会显示它的值了。变量 `ans` 的值就是上一次计算的表达式的值，无论上一次是否被显示。变量 `ans` 仅适用于交互式会话，不适用于以其它方式运行的 Julia 代码。

如果想运行写在源文件 file.jl 中的代码，可以输入命令 `include("file.jl")` 。

要在非交互式模式下运行代码，你可以把它当做 Julia 命令行的第一个参数：

```julia
julia script.jl arg1 arg2...
```

如这个例子所示，julia 后面跟着的命令行参数，被认为是程序 script.jl 的命令行参数。这些参数使用全局变量 ARGS 来传递。使用 -e 选项，也可以在命令行设置 ARGS 参数。可如下操作，来打印传递的参数：

```julia
julia -e 'for x in ARGS; println(x); end' foo bar
```

也可以把代码放在一个脚本中，然后运行：

```julia
echo 'for x in ARGS; println(x); end' > script.jl
julia script.jl foo bar
```

Julia 可以用 `-p` 或 `--machinefile` 选项来开启并行模式。 `-p n` 会发起额外的 n 个工作进程，而 `--machinefile file` 会为文件 file 的每一行发起一个工作进程。 file 定义的机器，必须要能经由无密码的 ssh 访问，且每个机器上的 Julia 安装的位置应完全相同，每个机器的定义为 `[user@]host[:port] [bind_addr]` 。 `user` 默认为当前的用户，`port` 默认为标准 ssh 端口。可选择的，万一是多网主机，`bind_addr` 可被用来精确指定接口。

如果你想让 Julia 在启动时运行一些代码，可以将代码放入 `~/.juliarc.jl` ：

```julia
echo 'println("Greetings! 你好! 안녕하세요?")' > ~/.juliarc.jl
julia
```

运行 Julia 有各种可选项：

## 资源

除了本手册，还有一些其它的资源：

