# Jupyter Latex

## 环境配置

[环境安装](./setup.html)

## 如何使用

LaTeX实现的原理类似于HTML，Notebook中的Markdown格式解释器中内置Latex渲染器，可以将由\$与\$包裹的内容进行渲染并产生最终效果。

## 语法及公式

上下标
```markdown
$$x_1^2 , x_{n}^{1}$$
```
$$
x_1^2 , x_{n}^{1}
$$

```markdown
$$ y = x_i^{a_1^2} $$
```
$$
y = x_i^{a_1^2}
$$

公式中插入文本`\mbox{}`：

```markdown
$$ y = x^2 \; \mbox{(二次函数)} $$
```
$$
y = x^2 \; \mbox{(二次函数)} 
$$

bigcap:
```markdown
$$
\bigcap_{i=1}^{n} \bigcup_{i=1}^n  \binom{5}{3}
$$
```

$$
\bigcap_{i=1}^{n} \bigcup_{i=1}^n  \binom{5}{3}
$$


量词:
```markdown
$$\forall$$全称量词,表示任意的
$$\exists$$存在量词,表示存在/至少一个   
```
$\forall$全称量词,表示任意的，$\exists$存在量词,表示存在/至少一个   

偏导符号， 正比符号，无穷符号及极限

```markdown
$\partial$ 偏导符号
$\propto$ 正比符号，
$\mathop{\lim}_{n \to \infty }f(x)$无穷符号及极限
```
$\partial$ 偏导符号
$\propto$ 正比符号，
$\mathop{\lim}_{n \to \infty }f(x)$无穷符号及极限

公式中插入空格`\,  \;  \quad  \qquad`间隔依次变宽：

```markdown
$$ ab $$ $$ a\,b $$ $$ a\;b $$ $$ a\quad b $$ $$ a\qquad b $$
```
$$ ab $$ $$ a\,b $$ $$ a\;b $$ $$ a\quad b $$ $$ a\qquad b $$


字母上方横线`\overline{}, \bar{}`：
```markdown
$$ \overline{xyz} \mbox{ 或 } \bar{x} $$
```
$$
\overline{xyz} \mbox{ 或 } \bar{x} 
$$

字母下方横线`\underline{}`：

```markdown
$$ \underline{ABC} $$
```
$$
\underline{ABC}
$$

字母上方波浪线`\tilde{}, \widetilde{}`：
```markdown
$$ \tilde{A} \mbox{ 或 } \widetilde{ABC} $$
```
$$
\tilde{A} \mbox{ 或 } \widetilde{ABC}
$$

字母上方尖号^`\hat{}, \widehat{}`：
```markdown
$$ \hat{A} \mbox{ 或 } \widehat{ABC} $$
```
$$
\hat{A} \mbox{ 或 } \widehat{ABC}
$$

字母上方箭头`\vec{}, \overleftarrow{}, \overrightarrow{}`：
```markdown
$$ \vec{ab} \mbox{ 或 } \overleftarrow{ab} \mbox{ 或 } \overrightarrow{ab} $$
```
$$
\vec{ab} \mbox{ 或 } \overleftarrow{ab} \mbox{ 或 } \overrightarrow{ab}
$$

字母上方花括号`\overbrace{}`，或下方花括号`\underbrace{}`：
```markdown
$$ \overbrace{1+2+3} \mbox{ 或 } \underbrace{1+2+3} $$
```
$$
\overbrace{1+2+3} \mbox{ 或 } \underbrace{1+2+3}
$$

字母上方点号`\dot{}, \ddot{}`：
```markdown
$$ \dot{a} \mbox{ 或 } \ddot{a} $$
```
$$
\dot{a} \mbox{ 或 } \ddot{a}
$$

省略号`\dots, \cdots`
```markdown
$$ 1,2,\dots  \qquad  1,2,\cdots $$  
```
$$
1,2,\dots  \qquad  1,2,\cdots
$$

积分`\int_{}^{}`：

```markdown
$$ \int_{-\infty}^{+\infty} f(x) \mathrm{d}x $$
```
$$
\int_{-\infty}^{+\infty} f(x) \mathrm{d}x
$$

双重积分`\iint`：

```markdown
$$ \iint_{-\infty}^{+\infty} f(x,y) \mathrm{d}x \mathrm{d}y $$
```
$$
\iint_{-\infty}^{+\infty} f(x,y) \mathrm{d}x \mathrm{d}y
$$


行内积分limits模式:`\int\limits_{}^{}`：

```markdown
$$\int\limits_{-\infty}^{+\infty} f(x) \mathrm{d}x$$
```
$$
\int\limits_{-\infty}^{+\infty} f(x) \mathrm{d}x
$$


行内积分display模式:`\displaystyle \int_{}^{}`

```markdown
$$\displaystyle \int_{-\infty}^{+\infty} f(x) \mathrm{d}x$$
```
$$
\displaystyle \int_{-\infty}^{+\infty} f(x) \mathrm{d}x
$$


圆圈积分`\oint`：

```markdown
$$ \oint_{-\infty}^{+\infty} $$
```
$$
\oint_{-\infty}^{+\infty} 
$$


求和`\sum_{}^{}`：

```markdown
$$ \sum_{i=1}^{n} i^2 $$
```
$$
\sum_{i=1}^{n} i^2 
$$

行内求和：

```markdown
$$\sum_{i=1}^{n} i^2$$
```
$$
\sum_{i=1}^{n} i^2
$$

行内求和limits模式`\sum\limits_{}^{}`：
```markdown
$\sum\limits_{i=1}^{n} i^2$
```
$$
\sum\limits_{i=1}^{n} i^2
$$


行内求和display模式
```markdown
$$\displaystyle \sum_{i=1}^{n} i^2$$
```
$$
\displaystyle \sum_{i=1}^{n} i^2
$$


求乘积`\prod_{}^{}`：

```markdown
$$ \prod_{i=1}^{n} a_i $$
```
$$
\prod_{i=1}^{n} a_i
$$

分数`\frac{up}{down}`：

```markdown
$$ x_1,x_2 = \frac{b^2 \pm 4ac}{2a} $$
```
$$
x_1,x_2 = \frac{b^2 \pm 4ac}{2a}
$$

根号`\sqrt`：

```markdown
$$ r = \sqrt{x^2+y^2} $$
```
$$
r = \sqrt{x^2+y^2} 
$$
多次根号`\sqrt[n]`：

```markdown
$$ x^{2/3} = \sqrt[3]{x^2} $$
```
$$
x^{2/3} = \sqrt[3]{x^2}
$$

矩阵：
```markdown
$$
A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}
$$
```
$$
A_{m,n} =
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n}
 \end{pmatrix}
$$

公式编号及引用：
使用`\tag`指令指定公式的具体编号，并使用`\label`指令埋下锚点。如

```markdown
$$ y=ax+b \tag{1.1}\label{eq:test} $$
```
$$
y=ax+b \tag{1.1}\label{eq:test}
$$

引用编号：使用`\eqref`指令引用前面埋下的锚点，`\eqref{eq:test}`将显示为：

```markdown
$$ \eqref{eq:test} $$
```
$$
\eqref{eq:test}
$$

方程组

左侧花括号

>  注意：在 markdown 环境下，某些特殊字符，如'\', '\*'等，会首先被 markdown 语法转义，然后再被 Latex 转义。
> 因此有时候 '\{'需要写作'\\{'，'*'需要写作'\*'，'\\'需要写作'\\\\'等，视不同的解释环境而定

```markdown
$$
\begin{equation}
\left\\{
\begin{aligned}
2x + y &= 1 \\\\
2x + 2y &= 2
\end{aligned}
\right.
\end{equation} 
$$
```

$$
\begin{equation}
\left\\{
\begin{aligned}
2x + y &= 1 \\\\
2x + 2y &= 2
\end{aligned}
\right.
\end{equation}
$$

**注**：如果各个方程需要在某个字符处对齐（如等号对齐），只需在所有要对齐的字符前加上 `&` 符号。如果不需要公式编号，只需在宏包名称后加上 `*` 号。

```markdown
$$
f(x) =
\begin{cases}
x^2 \qquad & a \gt 0 \\
e^x \qquad & a \le 0
\end{cases}
$$
```
$$
f(x) =
\begin{cases}
x^2 \qquad & a \gt 0 \\
e^x \qquad & a \le 0
\end{cases}
$$


```markdown
$$
f(x) = \begin{cases}
x^2 \qquad & a \gt 0 \\\\
e^x \qquad & a \le 0
\end{cases}
$$
```
$$
f(x) = \begin{cases}
x^2 \qquad & a \gt 0 \\\\
e^x \qquad & a \le 0
\end{cases}
$$

```markdown
$$
\begin{aligned}
a &= 1 \\\\
bcd &= 2
\end{aligned}
$$
```
$$
\begin{aligned}
a &= 1 \\\\
bcd &= 2
\end{aligned}
$$

```markdown
$$y=x^2$$

$$e^{i\pi} + 1 = 0$$

$$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$$

$$\frac{n!}{k!(n-k)!} = {n \choose k}$$
```
$$
y=x^2
$$
$$
e^{i\pi} + 1 = 0
$$
$$
e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i
$$
$$
\frac{n!}{k!(n-k)!} = {n \choose k}
$$

## 希腊字母   

|希腊字母小写/大写|LaTeX形式|希腊字母小写/大写|LaTeX形式|
|:---|:---|:---|:---|
|α A|\alpha  $\alpha$	|μ N| \mu $\mu$ |
|β B|\beta  $\beta$|ξ Ξ|\xi \Xi $\xi \Xi$|
|γ Γ	|\gamma \Gamma  $\gamma   \Gamma$	|o O|o O $$|
|δ Δ	|\delta \ Delta $\delta \Delta$	|π Π| \pi \Pi $\pi \Pi$ |
|ε E	|\epsilon \varepsilon  $\epsilon \varepsilon$	|ϱ P	|\rho \varrho $\rho \varrho$|
|ζ Z	|\zeta $\zeta$	|σ Σ| \sigma \Sigma $\sigma \Sigma$ |
|η H	|\eta $\eta$	|τ T	|\tau $\tau$|
|θ ϑ Θ	|\theta \vartheta \Theta $\theta \vartheta \Theta$|	υ Υ| \upsilon \Upsilon $\upsilon \Upsilon$ |
|ι I	|\iota $\iota$	|ϕ φ Φ| \phi \varphi \Phi $\phi \varphi \Phi$ |
|κ K	|\kappa $\kappa$	|χ X	|\chi $\chi$|
|λ Λ	|\lambda \Lambda $\lambda \Lambda$	|ψ Ψ|	\psi \Psi $\psi \Psi$|

## 常用特殊字符

| Name         | Display        | Name         | Display        | Name     | Display    | Name      | Display     |
| ---------- | :------------: | ---------- | :------------: | ------ | :--------: | ------- | :---------: |
| `\times`     | $$\times$$       | `\div`       | $$\div$$         | `\pm`    | $$\pm$$      | `\mp`     | $$\mp$$       |
| `\otimes`    | $$\otimes$$      | `\ominus`    | $$\ominus$$      | `\oplus` | $$\oplus$$   | `\odot`   | $$\odot$$     |
| `\oslash`    | $$\oslash$$      | `\triangleq` | $$\triangleq$$   | `\ne`    | $$\ne$$      | `\equiv`  | $$\equiv$$    |
| `\lt`        | $$\lt$$          | `\gt`        | $$\gt$$          | `\le`    | $$\le$$      | `\ge`     | $$\ge$$       |
| `\cup`       | $$\cup$$         | `\cap`       | $$\cap$$         | `\Cup`   | $$\Cup$$     | `\Cap`    | $$\Cap$$      |
| `\bigcup`    | $$\bigcup$$      | `\bigcap`    | $$\bigcap$$      | `\ast`   | $$\ast$$     | `\star`   | $$\star$$     |
| `\bigotimes` | $$\bigotimes$$   | `\bigoplus`  | $$\bigoplus$$    | `\circ`  | $$\circ$$    | `\bullet` | $$\bullet$$   |
| `\bigcirc`   | $$\bigcirc$$     | `\amalg`     | $$\amalg$$       | `\to`    | $$\to$$      | `\infty`  | $$\infty$$    |
| `\vee`       | $$\vee$$         | `\wedge`     | $$\wedge$$       | `\lhd`   | $$\lhd$$     | `\rhd`    | $$\rhd$$      |
| `\bigvee`    | $$\bigvee$$      | `\bigwedge`  | $$\bigwedge$$    | `\unlhd` | $$\unlhd$$   | `\unrhd`  | $$\unrhd$$    |
| `\sqcap`     | $$\sqcap$$       | `\sqcup`     | $$\sqcup$$       | `\prec`  | $$\prec$$    | `\succ`   | $$\succ$$     |
| `\subset`    | $$\subset$$      | `\supset`    | $$\supset$$      | `\sim`   | $$\sim$$     | `\approx` | $$\approx$$   |
| `\subseteq`  | $$\subseteq$$    | `\supseteq`  | $$\supseteq$$    | `\cong`  | $$\cong$$    | `\doteq`  | $$\doteq$$    |
| `\setminus`  | $$\setminus$$    | `\mid`       | $$\mid$$         | `\ll`    | $$\ll$$      | `\gg`     | $$\gg$$       |
| `\parallel`  | $$\parallel$$    | `\Join`      | $$\Join$$        | `\in`    | $$\in$$      | `\notin`  | $$\notin$$    |
| `\propto`    | $$\propto$$      | `\neg`       | $$\neg$$         | `\ldots` | $$\ldots$$   | `\cdots`  | $$\cdots$$    |
| `\forall`    | $$\forall$$      | `\exists`    | $$\exists$$      | `\vdots` | $$\vdots$$   | `\ddots`  | $$\ddots$$    |
| `\aleph`     | $$\aleph$$       | `\nabla`     | $$\nabla$$       | `\imath` | $$\imath$$   | `\jmath`  | $$\jmath$$    |
| `\ell`       | $$\ell$$         | `\partial`   | $$\partial$$     | `\int`   | $$\int$$     | `\oint`   | $$\oint$$     |
| `\uplus`     | $$\uplus$$       | `\biguplus`  | $$\biguplus$$    |          |            |           |             |

## 其他图形

| Name                 |        Display         | Name                  |         Display         |
| -------------------| :--------------------: | --------------------| :---------------------: |
| `\triangleleft`      |   $$\triangleleft$$    | `\triangleright`      |   $$\triangleright$$    |
| `\bigtriangleup`     |   $$\bigtriangleup$$   | `\bigtriangledown`    |  $$\bigtriangledown$$   |
| `\uparrow`           |      $$\uparrow$$      | `\downarrow`          |     $$\downarrow$$      |
| `\leftarrow`         |     $$\leftarrow$$     | `\rightarrow`         |     $$\rightarrow$$     |
| `\Leftarrow`         |     $$\Leftarrow$$     | `\Rightarrow`         |     $$\Rightarrow$$     |
| `\longleftarrow`     |   $$\longleftarrow$$   | `\longrightarrow`     |   $$\longrightarrow$$   |
| `\Longleftarrow`     |   $$\Longleftarrow$$   | `\Longrightarrow`     |   $$\Longrightarrow$$   |
| `\leftrightarrow`    |  $$\leftrightarrow$$   | `\longleftrightarrow` | $$\longleftrightarrow$$ |
| `\Leftrightarrow`    |  $$\Leftrightarrow$$   | `\Longleftrightarrow` | $$\Longleftrightarrow$$ |
| `\leftharpoonup`     |   $$\leftharpoonup$$   | `\rightharpoonup`     |   $$\rightharpoonup$$   |
| `\leftharpoondown`   |  $$\leftharpoondown$$  | `\rightharpoondown`   |  $$\rightharpoondown$$  |
| `\rightleftharpoons` | $$\rightleftharpoons$$ | `\S`                  |         $$\S$$          |
| `\nwarrow`           |      $$\nwarrow$$      | `\nearrow`            |      $$\nearrow$$       |
| `\swarrow`           |      $$\swarrow$$      | `\searrow`            |      $$\searrow$$       |
| `\triangle`          |     $$\triangle$$      | `\box`                |        $$\Box$$         |
| `\diamond`           |      $$\diamond$$      | `\diamondsuit`        |    $$\diamondsuit$$     |
| `\heartsuit`         |     $$\heartsuit$$     | `\clubsuit`           |      $$\clubsuit$$      |
| `\spadesuit`         |     $$\spadesuit$$     |                       |                         |

## 不同的数字字母字体

### mathbb:
$$
\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}
$$
$$
\mathbb{abcdefghijklmnopqrstuvwxyz}
$$

### mathscr:
$$
\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}
$$

$$
\mathscr{abcdefghijklmnopqrstuvwxyz}
$$
### mathcal:
$$
\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}
$$

$$
\mathcal{abcdefghijklmnopqrstuvwxyz}
$$
### mathbf:
$$
\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}
$$
$$
\mathbf{abcdefghijklmnopqrstuvwxyz}
$$

默认倾斜：$$x_{z}$$

取消默认倾斜：$$\rm x_{z}$$
