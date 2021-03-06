# Vim 编辑

Vim提供了许多命令，使编辑功能非常强大。 在本章中，将讨论以下主题内容 -

- 插入
- 附加
- 打开新行
- 替换
- 更改
- 更换
- 加入

## 先进入Vim环境
```bash
vim
```

### 在光标前插入文本

`I`切换到插入模式

**在行的开头插入文本**

假设位于行的中间，并且希望在当前行的开头插入文本，然后执行以下步骤 -

- `Esc`切换到命令模式

- `I`激活插入模式

此操作将光标移动到当前行的开头并在插入模式下切换Vim。

**在光标后附加文本**

要在光标后附加文本，请执行以下步骤:

切换到命令模式并将光标移动到适当的位置

- `a`切换到插入模式，此操作将光标移动一个位置并在插入模式下切换Vim。

###  在行尾添加文本

假设位于行的中间，并且希望在当前行的末尾附加文本，然后执行以下步骤 -

- `Esc`切换到命令模式

- `A`切换到插入模式

  此操作将光标移动到行尾并在插入模式下切换Vim

### 打开光标下方的新行

假设光标处于中间位置，并且想在当前行下面打开新行，然后执行以下步骤 -

- `Esc`切换到命令模式

- `O`切换到插入模式，此操作将在当前行上方插入空行并在插入模式下切换Vim。

**打开光标上方的新行**

假设光标处于行中间，并且想在当前行上方打开新行，然后执行以下步骤 -

- `Esc`切换到命令模式

- `o`切换到插入模式

### 替换文字

假设想要替换单个字符然后执行以下步骤 -

- `Esc`切换到命令模式

- 将光标移动到适当的位置
- `s`切换到插入模式

此操作将删除光标下的字符并在插入模式下切换Vim要替换整行使用

此操作将删除整行并在插入模式下切换Vim。

### 改变文字

假设要更改当前行中的文本，然后执行以下步骤 -

- `Esc`切换到命令模式
- `cc`这类似于使用S的替代动作
- 要从当前光标位置更改文本，请执行以下命令`C`

此操作将删除当前光标位置后的文本，并在插入模式下切换Vim。

### 替换文字

要替换单个字符，请执行以下步骤

- `Esc`切换到命令模式

- 将光标移动到适当的位置
- 执行以下命令`r`

- 输入要替换的字符。
  请注意，此命令不会在插入模式下切换Vim

要替换整行执行`R`

###  加入文字

要连接两行，请执行以下步骤 

- `Esc`切换到命令模式
- 将光标移动到适当的行
- 执行以下命令`J`