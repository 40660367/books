# Julia 多维数组

## 多维数组

数组是一个存在多维网格中的对象集合。通常，数组包含的对象的类型为 `Any` 。对大多数计算而言，数组对象一般更具体为 `Float64` 或 `Int32` 。

因为性能的原因，Julia 不希望把程序写成向量化的形式。

在 Julia 中，通过引用将参数传递给函数。Julia 的库函数不会修改传递给它的输入。用户写代码时，如果要想做类似的功能，要注意先把输入复制一份儿。

## 数组

### 基础函数

| 函数          | 说明                                                         |
| :------------ | :----------------------------------------------------------- |
| `eltype(A)`   | A 中元素的类型                                               |
| `length(A)`   | A 中元素的个数                                               |
| `ndims(A)`    | A 有几个维度                                                 |
| `nnz(A)`      | A 中非零元素的个数                                           |
| `size(A)`     | 返回一个元素为 A 的维度的多元组                              |
| `size(A,n)`   | A 在某个维度上的长度                                         |
| `stride(A,k)` | 在维度 k 上，邻接元素（在内存中）的线性索引距离              |
| `strides(A)`  | 返回多元组，其元素为在每个维度上，邻接元素（在内存中）的线性索引距离 |

### 构造和初始化

下列函数中调用的 `dims...` 参数，既可以是维度的单多元组，也可以是维度作为可变参数时的一组值。

| 函数                                                         | 说明                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| `Array(type, dims...)`                                       | 未初始化的稠密数组                                           |
| `cell(dims...)`                                              | 未初始化的元胞数组（异构数组）                               |
| `zeros(type, dims...)` |指定类型的全 0 数组. 如果未指明 `type`, 默认为 `Float64` |                                                              |
| `zeros(A)` |全 0 数组, 元素类型和大小同 `A`.                 |                                                              |
| `ones(type, dims...)` |指定类型的全 1 数组. 如果未指明 `type`, 默认为 `Float64` |                                                              |
| `ones(A)` |全 1 数组, 元素类型和大小同 `A`.                  |                                                              |
| `trues(dims...)` | 全 `true` 的 `Bool` 数组                  |                                                              |
| `falses(dims...)` | 全 `false` 的 `Bool` 数组                |                                                              |
| `reshape(A, dims...)`                                        | 将数组中的数据按照指定维度排列                               |
| `copy(A)` | 复制 `A`                                         |                                                              |
| `deepcopy(A)` | 复制 `A` ，并递归复制其元素                  |                                                              |
| `similar(A, element_type, dims...)`                          | 属性与输入数组（稠密、稀疏等）相同的未初始化数组，但指明了元素类型和维度。 |
|                                                              | 第二、三参数可省略，省略时默认为 `A` 的元素类型和维度        |
| `reinterpret(type, A)`                                       | 二进制数据与输入数组相同的数组，但指明了元素类型             |
| `rand(dims)` | 在 [0,1) 上独立均匀同分布的 `Float64` 类型的随机数组 |                                                              |
| `randn(dims)` | `Float64` 类型的独立正态同分布的随机数组，均值为 0 ，标准差为 1 |                                                              |
| `eye(n)` | `n` x `n` 单位矩阵                                |                                                              |
| `eye(m, n)` | `m` x `n` 单位矩阵                             |                                                              |
| `linspace(start, stop, n)`| 从 `start` 至 `stop` 的由 `n` 个元素构成的线性向量 |                                                              |
| `fill!(A, x)` | 用值 `x` 填充数组 `A`                        |                                                              |
| `fill(x, dims)` | 创建指定规模的数组, 并使用 `x` 填充        |                                                              |

### 连接

使用下列函数，可在任意维度连接数组：

| 函数                                            | 描述 |
| :---------------------------------------------- | :--- |
| `cat(k, A...)` | 在 `k` 维度上连接输入 n-d 数组 |      |
| `vcat(A...)` | `cat(1, A...)` 的简写            |      |
| `hcat(A...)` |`cat(2, A...)` 的简写             |      |

传递给这些函数的标量值被视为一元阵列。

级联功能非常常用，所以为它们设计了特殊的语法：

| 表示                       | 调用 |
| :------------------------- | :--- |
| `[A B C ...]` |`hcat`      |      |
| `[A, B, C, ...]` |`vcat`   |      |
| `[A B; C D; ...]` |`hvcat` |      |

`hvcat` 可以实现一维上的（使用分号间隔）或二维上的（使用空格间隔）的级联。

### Comprehensions

Comprehensions 用于构造数组。它的语法类似于数学中的集合标记法：

```
    A = [ F(x,y,...) for x=rx, y=ry, ... ]
```

`F(x,y,...)` 根据变量 `x`, `y` 等来求值。这些变量的值可以是任何迭代对象，但大多数情况下，都使用类似于 `1:n` 或 `2:(n-1)` 的范围对象，或显式指明为类似 `[1.2, 3.4, 5.7]` 的数组。它的结果是 N 维稠密数组。

下例计算在维度 1 上，当前元素及左右邻居元素的加权平均数：

```julia
const x = rand(8)

[ 0.25*x[i-1] + 0.5*x[i] + 0.25*x[i+1] for i=2:length(x)-1 ]
```

> 注解： 上例中，`x` 被声明为常量，因为对于非常量的全局变量，Julia 的类型推断不怎么样。

可在 comprehension 之前显式指明它的类型。如要避免在前例中声明 `x` 为常量，但仍要确保结果类型为 `Float64`，应这样写：

```julia
Float64[ 0.25*x[i-1] + 0.5*x[i] + 0.25*x[i+1] for i=2:length(x)-1 ]
```

使用花括号来替代方括号，可以将它简写为 `Any` 类型的数组：

```julia
{ i/2 for i = 1:3 }
```

### 索引

索引 n 维数组 A 的通用语法为：

```julia
X = A[I_1, I_2, ..., I_n]
```

其中 I_k 可以是：

1. 标量
2. 满足 `:`, `a:b`, 或 `a:b:c` 格式的 `Range` 对象
3. 任意整数向量，包括空向量 `[]`
4. 布尔值向量

结果 X 的维度通常为 `(length(I_1), length(I_2), ..., length(I_n))` ，且 X 的索引 `(i_1, i_2, ..., i_n)` 处的值为 `A[I_1[i_1], I_2[i_2], ..., I_n[i_n]]` 。缀在后面的标量索引的维度信息被舍弃。如，`A[I, 1]` 的维度为 `(length(I),)`。布尔值向量先由 `find` 函数进行转换。由布尔值向量索引的维度长度，是向量中 `true` 值的个数。

索引语法与调用 `getindex` 等价：

```julia
X = getindex(A, I_1, I_2, ..., I_n)
```

例如：

```julia
x = reshape(1:16, 4, 4)

x[2:3, 2:end-1]
```

`n:n-1` 形式的空范围有时用来表示相互索引位置在 `n-1` 和 `n`之间。例如，在 `searchsorted` 函数使用本习惯指出插入点的值不在排序后的数组中：

```julia
a = [1,2,5,6,7];

searchsorted(a, 3)
```

### 赋值

给 n 维数组 A 赋值的通用语法为：`A[I_1, I_2, ..., I_n] = X`

其中 I_k 可能是：

1. 标量
2. 满足 `:`, `a:b`, 或 `a:b:c` 格式的 `Range` 对象
3. 任意整数向量，包括空向量 `[]`
4. 布尔值向量

如果 `X` 是一个数组，它的维度应为 `(length(I_1), length(I_2), ..., length(I_n))` ，且 `A` 在 `i_1, i_2, ..., i_n` 处的值被覆写为 `X[I_1[i_1], I_2[i_2], ..., I_n[i_n]]` 。如果 `X` 不是数组，它的值被写进所有 `A` 被引用的地方。

用于索引的布尔值向量与 `getindex` 中一样（先由 `find` 函数进行转换）。

索引赋值语法等价于调用 `setindex!` ：`setindex!(A, X, I_1, I_2, ..., I_n)`

例如：

```julia
x = reshape(1:9, 3, 3)

x[1:2, 2:3] = -1

x
```

### 向量化的运算符和函数

数组支持下列运算符。逐元素进行的运算，应使用带“点”（逐元素）版本的二元运算符。

1. 一元： `-`, `+`, `!`
2. 二元： `+`, `-`, `*`, `.*`, `/`, `./`, `\`, `.\`, `^`, `.^`, `div`, `mod`
3. 比较： `.==`, `.!=`, `.<`, `.<=`, `.>`, `.>=`
4. 一元布尔值或位运算： `~`
5. 二元布尔值或位运算： `&`, `|`, `$`

一些没有“点”（逐元素）操作运算符当一个参数是一个标量时会被使用。这些运算符有 `*`, `/`, `\` 和按位运算符。

请注意，像 `==` 操作这样的比较运算是操作在整个阵列上的，它会给出一个布尔返回值。逐位的比较使用点操作符。

下列内置的函数也都是向量化的, 即函数是逐元素版本的：

abs abs2 angle cbrt
airy airyai airyaiprime airybi airybiprime airyprime
acos acosh asin asinh atan atan2 atanh
acsc acsch asec asech acot acoth
cos  cospi cosh  sin  sinpi sinh  tan  tanh  sinc  cosc
csc  csch  sec  sech  cot  coth
acosd asind atand asecd acscd acotd
cosd  sind  tand  secd  cscd  cotd
besselh besseli besselj besselj0 besselj1 besselk bessely bessely0 bessely1
exp  erf  erfc  erfinv erfcinv exp2  expm1
beta dawson digamma erfcx erfi
exponent eta zeta gamma
hankelh1 hankelh2
 ceil  floor  round  trunc
iceil ifloor iround itrunc
isfinite isinf isnan
lbeta lfact lgamma
log log10 log1p log2
copysign max min significand
sqrt hypot



注意 `min` `max` 和 `minimum` `maximum` 之间的区别，前者是对多个数组操作，找出各数组对应的的元素中的最大最小，后者是作用在一个数组上找出该数组的最大最小值。

Julia 提供了 `@vectorize_1arg` 和 `@vectorize_2arg` 两个宏，分别用来向量化任意的单参数或两个参数的函数。每个宏都接收两个参数，即函数参数的类型和函数名。例如：

```julia
square(x) = x^2

@vectorize_1arg Number square

methods(square)
    square(x) at none:1

square([1 2 4; 5 6 7])
```

### Broadcasting

有时要对不同维度的数组进行逐元素的二元运算，如将向量加到矩阵的每一列。低效的方法是，把向量复制成同维度的矩阵：

```julia
a = rand(2,1); A = rand(2,3);

repmat(a,1,3)+A
```

维度很大时，效率会很低。Julia 提供 `broadcast` 函数，它将数组参数的维度进行扩展，使其匹配另一个数组的对应维度，且不需要额外内存，最后再逐元素调用指定的二元函数：

```julia
broadcast(+, a, A)

b = rand(1,2)

broadcast(+, a, b)
```

逐元素的运算符，如 `.+` 和 `.*` 将会在必要时进行 broadcasting 。还提供了 `broadcast!` 函数，可以明确指明目的，而 `broadcast_getindex` 和 `broadcast_setindex!` 函数可以在索引前对索引值做 broadcast。

### 实现

Julia 的基础数组类型是抽象类型 `AbstractArray{T,N}`，其中维度为 `N`，元素类型为 `T`。`AbstractVector` 和 `AbstractMatrix` 分别是它 1 维和 2 维的别名。

`AbstractArray` 类型包含任何形似数组的类型， 而且它的实现和通常的数组会很不一样。例如，任何具体的 `AbstractArray{T，N}` 至少要有 `size(A)` (返回 `Int` 多元组)，`getindex(A,i)` 和 `getindex(A,i1,...,iN)` (返回 `T` 类型的一个元素), 可变的数组要能 `setindex！`。 这些操作都要求在近乎常数的时间复杂度或 O(1) 复杂度，否则某些数组函数就会特别慢。具体的类型也要提供类似于 `similar(A,T=eltype(A),dims=size(A))` 的方法用来分配一个拷贝。

`DenseArray` 是一个抽象的 `AbstractArray` 类型的亚型，它应该包括在内存的常规偏移上的所有数组，因此可以被传递到外部在此内存布局上的 C 和 Fortran 函数。
亚型应该提供一个方法 `stride(A,k)`，使之返回“跨越”的维度 `k`：向给出的维度 `k` 加 `1` 应该使 `getindex(A,i)` 中的 `i` 增加 `stride(A,k)`。如果提供了一个指针转换方法 `convert(Ptr{T},A)`，那么内存布局应该以相同的方式对应于这些扩展。

`Array{T,N}` 类型是 `DenseArray` 的特殊实例，它的元素以列序为主序存储（详见[代码性能优化](http://julia-cn.readthedocs.org/zh_CN/latest/manual/performance-tips/#man-performance-tips)）。`Vector` 和 `Matrix` 是分别是它 1 维和 2 维的别名。

`SubArray` 是 `AbstractArray` 的特殊实例，它通过引用而不是复制来进行索引。使用 `sub` 函数来构造 `SubArray`，它的调用方式与 `getindex` 相同（使用数组和一组索引参数）。`sub` 的结果与 `getindex` 的结果类似，但它的数据仍留在原地。`sub` 在 `SubArray` 对象中保存输入的索引向量，这个向量将被用来间接索引原数组。

`StridedVector` 和 `StridedMatrix` 是为了方便而定义的别名。通过给他们传递 `Array` 或 `SubArray` 对象，可以使 Julia 大范围调用 BLAS 和 LAPACK 函数，提高内存申请和复制的效率。

下面的例子计算大数组中的一个小块的 QR 分解，无需构造临时变量，直接调用合适的 LAPACK 函数。

```julia
a = rand(10,10)

b = sub(a, 2:2:8,2:2:4)

(q,r) = qr(b);

q

r
```

## 稀疏矩阵

[稀疏矩阵](http://zh.wikipedia.org/zh-cn/稀疏矩阵)是其元素大部分为 0 的矩阵。

### 列压缩（CSC）存储

Julia 中，稀疏矩阵使用 [列压缩（CSC）格式](http://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_column_.28CSC_or_CCS.29)。Julia 稀疏矩阵的类型为 `SparseMatrixCSC{Tv,Ti}` ，其中 `Tv` 是非零元素的类型， `Ti` 是整数类型，存储列指针和行索引：

```julia
type SparseMatrixCSC{Tv,Ti<:Integer} <: AbstractSparseMatrix{Tv,Ti}
    m::Int                  # Number of rows
    n::Int                  # Number of columns
    colptr::Vector{Ti}      # Column i is in colptr[i]:(colptr[i+1]-1)
    rowval::Vector{Ti}      # Row values of nonzeros
    nzval::Vector{Tv}       # Nonzero values
end
```

列压缩存储便于按列简单快速地存取稀疏矩阵的元素，但按行存取则较慢。把非零值插入 CSC 结构等运算，都比较慢，这是因为稀疏矩阵中，在所插入元素后面的元素，都要逐一移位。

如果你从其他地方获得的数据是 CSC 格式储存的，想用 Julia 来读取，应确保它的序号从 1 开始索引。每一列中的行索引值应该是排好序的。如果你的 `SparseMatrixCSC` 对象包含未排序的行索引值，对它们进行排序的最快的方法是转置两次。

有时，在 `SparseMatrixCSC` 中存储一些零值，后面的运算比较方便。 `Base` 中允许这种行为（但是不保证在操作中会一直保留这些零值）。这些被存储的零被许多函数认为是非零值。`nnz` 函数返回稀疏数据结构中存储的元素数目，包括被存储的零。要想得到准确的非零元素的数目，请使用 `countnz` 函数，它挨个检查每个元素的值（因此它的时间复杂度不再是常数，而是与元素数目成正比）。

## 构造稀疏矩阵

稠密矩阵有 `zeros` 和 `eye` 函数，稀疏矩阵对应的函数，在函数名前加 `sp` 前缀即可：

```julia
spzeros(3,5)

speye(3,5)
```

`sparse` 函数是比较常用的构造稀疏矩阵的方法。它输入行索引 `I` ，列索引向量 `J` ，以及非零值向量 `V` 。 `sparse(I,J,V)` 构造一个满足 `S[I[k], J[k]] = V[k]` 的稀疏矩阵：

```julia
I = [1, 4, 3, 5]; J = [4, 7, 18, 9]; V = [1, 2, -5, 3];

S = sparse(I,J,V)
```

与 `sparse` 相反的函数为 `findn` ，它返回构造稀疏矩阵时的输入：

```julia
findn(S)

findnz(S)
```

另一个构造稀疏矩阵的方法是，使用 `sparse` 函数将稠密矩阵转换为稀疏矩阵：

```julia
sparse(eye(5))
```

可以使用 `dense` 或 `full` 函数做逆操作。 `issparse` 函数可用来检查矩阵是否稀疏：

```julia
issparse(speye(5))
```

### 稀疏矩阵运算

稠密矩阵的算术运算也可以用在稀疏矩阵上。对稀疏矩阵进行赋值运算，是比较费资源的。大多数情况下，建议使用 `findnz` 函数把稀疏矩阵转换为 `(I,J,V)` 格式，在非零数或者稠密向量 `(I,J,V)` 的结构上做运算，最后再重构回稀疏矩阵。

### 稠密矩阵和稀疏矩阵函数对应关系

接下来的表格列出了内置的稀疏矩阵的函数, 及其对应的稠密矩阵的函数。通常，稀疏矩阵的函数，要么返回与输入稀疏矩阵 `S` 同样的稀疏度，要么返回 `d` 稠密度，例如矩阵的每个元素是非零的概率为 `d` 。

详见可以标准库文档的 [*stdlib-sparse*](http://julia-cn.readthedocs.org/zh_CN/latest/stdlib/sparse/#stdlib-sparse) 章节。

| 稀疏矩阵          | 稠密矩阵      | 说明                                                         |
| :---------------- | :------------ | :----------------------------------------------------------- |
| spzeros(m,n)      | zeros(m,n)    | 构造 m x n 的全 0 矩阵 (spzeros(m,n) 是空矩阵)               |
| spones(S)         | ones(m,n)     | 构造的全 1 矩阵 与稠密版本的不同， spones 的稀疏 度与 S 相同 |
| speye(n)          | eye(n)        | 构造 m x n 的单位矩阵                                        |
| full(S)           | sparse(A)     | 转换为稀疏矩阵和稠密矩阵                                     |
| sprand(m,n,d)     | rand(m,n)     | 构造 m-by-n 的随机矩阵（稠密度为 d ） 独立同分布的非零元素在 [0, 1] 内均匀分布 |
| sprandn(m,n,d)    | randn(m,n)    | 构造 m-by-n 的随机矩阵（稠密度为 d ） 独立同分布的非零元素满足标准正 态（高斯）分布 |
| sprandn(m,n,d,X)  | randn(m,n,X)  | 构造 m-by-n 的随机矩阵（稠密度为 d ） 独立同分布的非零元素满足 X 分 布。（需要 Distributions 扩展包） |
| sprandbool(m,n,d) | randbool(m,n) | 构造 m-by-n 的随机矩阵（稠密度为 d ） ，非零 Bool`元素的概率为 *d* (`randbool 中 d =0.5 ) |

