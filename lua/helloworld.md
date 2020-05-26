# Lua 运行Lua的第一个程序

Lua提供了两种编程方式

### 交互式编程

Lua 提供了交互式编程模式。我们可以在命令行中输入程序并立即查看效果。

Lua 交互式编程模式可以通过命令 lua 来启用：

```bash
lua
```

有`>`即表示已经在Lua环境中了，这时就可以输入以下命令，看看有什么返回？

```lua
print("Hello World！")
```

### 脚本式编程

我们可以将 Lua 程序代码保持到一个以 lua 结尾的文件，并执行，该模式称为脚本式编程，如我们将如下代码存储在名为 hello.lua 的脚本文件中：

```bash
cd ~ 
echo 'print("Hello World！")' > helloworld.lua
```

使用 lua 名执行以上脚本，输出结果为：

```bash
cd ~ 
lua helloworld.lua
```

我们也可以将代码修改为如下形式来执行脚本（在开头添加：#!/usr/bin/lua）：

```bash
cd ~
#创建lua脚本文件，并指定了该脚本的解释器为/usr/bin/lua
cat > helloworld2.lua << EOF
#!/usr/bin/lua
print("Hello World Again！")
EOF

#我们为脚本添加可执行权限
chmod +x helloworld2.lua

#执行这个脚本
./helloworld2.lua
```