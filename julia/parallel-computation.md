# Julia 并行计算

## 并行计算

Julia 提供了一个基于消息传递的多处理器环境，能够同时在多处理器上使用独立的内存空间运行程序。

Julia 的消息传递与 MPI [1] 等环境不同。Julia 中的通信是“单边”的，即程序员只需要管理双处理器运算中的一个处理器即可。

Julia 中的并行编程基于两个原语：*remote references* 和 *remote calls* 。remote reference 对象，用于从任意的处理器，查阅指定处理器上存储的对象。 remote call 请求，用于一个处理器对另一个（也有可能是同一个）处理器调用某个函数处理某些参数。 remote call 返回 remote reference 对象。 remote call 是立即返回的；调用它的处理器继续执行下一步操作，而 remote call 继续在某处执行。可以对 remote reference 调用 `wait` ，以等待 remote call 执行完毕，然后通过 `fetch` 获取结果的完整值。使用 `put` 可将值存储到 remote reference 。

通过 `julia -p n` 启动，可以在本地机器上提供 `n` 个处理器。一般 `n` 等于机器上 CPU 内核个数：

```julia
./julia -p 2
```
```julia
r = remotecall(2, rand, 2, 2)
RemoteRef(2,1,5)

fetch(r)

s = @spawnat 2 1 .+ fetch(r)

fetch(s)
```

`remote_call` 的第一个参数是要进行这个运算的处理器索引值。Julia 中大部分并行编程不查询特定的处理器或可用处理器的个数，但可认为 `remote_call` 是个为精细控制所提供的低级接口。第二个参数是要调用的函数，剩下的参数是该函数的参数。此例中，我们先让处理器 2 构造一个 2x2 的随机矩阵，然后我们在结果上加 1 。两个计算的结果保存在两个 remote reference 中，即 `r` 和 `s` 。 `@spawnat` 宏在由第一个参数指明的处理器上，计算第二个参数中的表达式。

`remote_call_fetch` 函数可以立即获取要在远端计算的值。它等价于 `fetch(remote_call(...))` ，但比之更高效：

```julia
remotecall_fetch(2, getindex, r, 1, 1)
```

`getindex(r,1,1)` :ref:`等价于 <man-array-indexing>` `r[1,1]` ，因此，这个调用获取 remote reference 对象 `r` 的第一个元素。

`remote_call` 语法不太方便。 `@spawn` 宏简化了这件事儿，它对表达式而非函数进行操作，并自动选取在哪儿进行计算：

```julia
r = @spawn rand(2,2)

s = @spawn 1 .+ fetch(r)

fetch(s)
```

注意，此处用 `1 .+ fetch(r)` 而不是 `1 .+ r` 。这是因为我们不知道代码在何处运行，而 `fetch` 会将需要的 `r` 移到做加法的处理器上。此例中， `@spawn` 很聪明，它知道在有 `r` 对象的处理器上进行计算，因而 `fetch` 将不做任何操作。

（ `@spawn` 不是内置函数，而是 Julia 定义的 :ref:`宏 <man-macros>` ）

所有执行程序代码的处理器上，都必须能获得程序代码。例如，输入：

```julia
function rand2(dims...)
         return 2*rand(dims...)
       end

rand2(2,2)

@spawn rand2(2,2)

@spawn rand2(2,2)

exception on 2: in anonymous: rand2 not defined 
```

进程 1 知道 `rand2` 函数，但进程 2 不知道。 `require` 函数自动在当前所有可用的处理器上载入源文件，使所有的处理器都能运行代码：

```julia
require("myfile")
```

在集群中，文件（及递归载入的任何文件）的内容会被发送到整个网络。可以使用 `@everywhere` 宏在所有处理器上执行命令：

```julia
@everywhere id = myid()

remotecall_fetch(2, ()->id)

@everywhere include("defs.jl")
```

文件也可以在多个进程启动时预加载,并且一个驱动脚本可以用于驱动计算：

`julia -p <n> -L file1.jl -L file2.jl driver.jl`

每个进程都有一个关联的标识符。这个过程提供的 Julia 提示总是有一个 id 值为 1 ,就如上面例子中 julia 进程会运行驱动脚本一样。这个被默认用作平行操作的进程被称为 `workers`。当只有一个进程的时候，进程 1 就被当做一个 worker。否则，worker 就是指除了进程 1 之外的所有进程。

Julia 内置有对于两种集群的支持：

- 如上文所示,一个本地集群指定使用 `—p` 选项。
- 一个集群生成机器使用 `--machinefile` 选项。它使用一个无密码的 `ssh` 登来在指定的机器上启动 julia 工作进程(以相同的路径作为当前主机)。

函数 `addprocs`,`rmprocs`,`workers`,当然还有其他的在一个集群中可用的以可编程的方式进行添加,删除和查询的函数。

其他类型的集群可以通过编写自己的自定义 ClusterManager。请参阅 ClusterManagers 部分。

## 数据移动

并行计算中，消息传递和数据移动是最大的开销。减少这两者的数量，对性能至关重要。

`fetch` 是显式的数据移动操作，它直接要求将对象移动到当前机器。 `@spawn` （及相关宏）也进行数据移动，但不是显式的，因而被称为隐式数据移动操作。对比如下两种构造随机矩阵并计算其平方的方法： :

```julia
# method 1
A = rand(1000,1000)
Bref = @spawn A^2
...
fetch(Bref)

# method 2
Bref = @spawn rand(1000,1000)^2
...
fetch(Bref)
```

方法 1 中，本地构造了一个随机矩阵，然后将其传递给做平方计算的处理器。方法 2 中，在同一处理器构造随机矩阵并进行平方计算。因此，方法 2 比方法 1 移动的数据少得多。

## 并行映射和循环

大部分并行计算不需要移动数据。最常见的是蒙特卡罗仿真。下例使用 `@spawn` 在两个处理器上仿真投硬币。先在 `count_heads.jl` 中写如下函数：

```julia
function count_heads(n)
    c::Int = 0
    for i=1:n
        c += randbool()
    end
    c
end
```

在两台机器上做仿真，最后将结果加起来：

```julia
require("count_heads")

a = @spawn count_heads(100000000)
b = @spawn count_heads(100000000)
fetch(a)+fetch(b)
```

在多处理器上独立地进行迭代运算，然后用一些函数把它们的结果综合起来。综合的过程称为 *约简* 。

上例中，我们显式调用了两个 `@spawn` 语句，它将并行计算限制在两个处理器上。要在任意个数的处理器上运行，应使用 *并行 for 循环* ，它在 Julia 中应写为：

```julia
nheads = @parallel (+) for i=1:200000000
  int(randbool())
end
```

这个构造实现了给多处理器分配迭代的模式，并且使用特定约简来综合结果（此例中为 `(+)` ）。

注意，尽管并行 for 循环看起来和一组 for 循环差不多，但它们的行为有很大区别。第一，循环不是按顺序进行的。第二，写进变量或数组的值不是全局可见的，因为迭代运行在不同的处理器上。并行循环内使用的所有变量都会被复制、广播到每个处理器。

下列代码并不会按照预想运行：

```julia
a = zeros(100000)
@parallel for i=1:100000
  a[i] = i
end
```

如果不需要，可以省略约简运算符。但此代码不会初始化 `a` 的所有元素，因为每个处理器上都只有独立的一份儿。应避免类似的并行 for 循环。但是我们可以使用分布式数组来规避这种情形，后面我们会讲。

如果“外部”变量是只读的，就可以在并行循环中使用它：

```julia
a = randn(1000)
@parallel (+) for i=1:100000
  f(a[randi(end)])
end
```

有时我们不需要约简，仅希望将函数应用到某个范围的整数（或某个集合的元素）上。这时可以使用 *并行映射* `pmap` 函数。下例中并行计算几个大随机矩阵的奇异值：

```julia
M = {rand(1000,1000) for i=1:10}
pmap(svd, M)
```

被调用的函数需处理大量工作时使用 `pmap` ，反之，则使用 `@parallel for` 。

## 与远程引用同步

### 调度

Julia 的平行编程平台使用[任务（也成为协程）](http://julia-cn.readthedocs.org/zh_CN/latest/manual/control-flow/#man-tasks) ,其可在多个计算中切换。每当代码执行一个通信操作，例如 `fetch` 或者 `wait`，当前任务便暂停同时调度器会选择另一个任务运行。在事件等待完成后，任务会重新启动。

对于很多问题，没必要直接考虑任务。然而，由于提供了动态调度，可以同时等待多个事件。在动态调度中，一个程序决定计算什么和在哪计算，这是基于其他工作何时完成的。这是被不可预知的或不可平衡的工作荷载所需要的，只有当他们结束当前任务我们才能分配更多的工作进程。

作为一个例子,考虑计算不同大小的矩阵的奇异值:

```julia
M = {rand(800,800), rand(600,600), rand(800,800), rand(600,600)}
pmap(svd, M)
```

如果一个进程要处理 800 x 800 矩阵和另一个 600 x 600 矩阵,我们不会得到很多的可伸缩性。解决方案是让本地的任务在他们完成当前的任务时去“喂”每个进程中的工作。`pmap` 的实现过程中可以看到这个:

```julia
function pmap(f, lst)
    np = nprocs()  # determine the number of processes available
    n = length(lst)
    results = cell(n)
    i = 1
    # function to produce the next work item from the queue.
    # in this case it's just an index.
    nextidx() = (idx=i; i+=1; idx)
    @sync begin
        for p=1:np
            if p != myid() || np == 1 
                @async begin
                    while true
                        idx = nextidx()
                        if idx > n
                            break
                        end
                        results[idx] = remotecall_fetch(p, f, lst[idx])
                    end
                end
            end
        end
    end
    results
end
```

只有在本地运行任务的过程中，`@async` 才与 `@spawn` 类似。我们使用它来为每个流程创建一个“供给”的任务。每个任务选择下一个需要被计算的指数,然后等待它的进程完成,接着一直重复到用完指数。注意,“供给”任务只有当主要任务到达 `@sync` 块结束时才开始执行,此时它放弃控制并等待所有的本地任务在从函数返回之前完成。供给任务可以通过 `nextidx()` 共享状态,因为它们都在相同的进程上运行。这个过程不需要锁定,因为线程是实时进行调度的而不是一成不变。这意味着内容的切换只发生在定义好的时候:在这种情况下,当 `remotecall_fetch` 会被调用。

## 分布式数组

并行计算综合使用多个机器上的内存资源，因而可以使用在一个机器上不能实现的大数组。这时，可使用分布式数组，每个处理器仅对它所拥有的那部分数组进行操作。

分布式数组（或 *全局对象* ）逻辑上是个单数组，但它分为很多块儿，每个处理器上保存一块儿。但对整个数组的运算与在本地数组的运算是一样的，并行计算是隐藏的。

分布式数组是用 `DArray` 类型来实现的。 `DArray` 的元素类型和维度与 `Array` 一样。 `DArray` 的数据的分布，是这样实现的：它把索引空间在每个维度都分成一些小块。

一些常用分布式数组可以使用 `d` 开头的函数来构造：

`dzeros(100,100,10),dones(100,100,10),drand(100,100,10),drandn(100,100,10),dfill(x, 100,100,10)`

最后一个例子中，数组的元素由值 `x` 来初始化。这些函数自动选取某个分布。如果要指明使用哪个进程，如何分布数据，应这样写：

```julia
dzeros((100,100), [1:4], [1,4])
```

第二个参数指定了数组应该在处理器 1 到 4 中创建。划分含有很多进程的数据时,人们经常看到性能收益递减。把 `DArrays` 放在一个进程的子集中，该进程允许多个 `DArray` 同时计算,并且每个进程拥有更高比例的通信工作。

第三个参数指定了一个分布;数组第 n 个元素指定了应该分成多少个块。在本例中,第一个维度不会分割,而第二个维度将分为四块。因此每个局部块的大小为 `(100，25)`。注意,分布式数组必须与进程数量相符。

`distribute(a::Array)` 可用来将本地数组转换为分布式数组。

`localpart(a::DArray)` 可用来获取 `DArray` 本地存储的部分。

`localindexes(a::DArray)` 返回本地进程所存储的维度索引值范围多元组。

`convert(Array, a::DArray)` 将所有数据综合到本地进程上。

使用索引值范围来索引 `DArray` （方括号）时，会创建 `SubArray` 对象，但不复制数据。

## 构造分布式数组

`DArray` 的构造函数是 `darray` ，它的声明如下：`DArray(init, dims[, procs, dist])`

`init` 函数的参数，是索引值范围多元组。这个函数在本地声名一块分布式数组，并用指定索引值来进行初始化。 `dims` 是整个分布式数组的维度。 `procs` 是可选的，指明一个存有要使用的进程 ID 的向量 。 `dist` 是一个整数向量，指明分布式数组在每个维度应该被分成几块。

最后俩参数是可选的，忽略的时候使用默认值。

下例演示如果将本地数组 `fill` 的构造函数更改为分布式数组的构造函数：

```
dfill(v, args...) = DArray(I->fill(v, map(length,I)), args...)
```

此例中 `init` 函数仅对它构造的本地块的维度调用 `fill` 。

## 分布式数组运算

在这个时候,分布式数组没有太多的功能。主要功能是通过数组索引来允许进行通信，这对许多问题来说都很方便。作为一个例子,考虑实现“生活”细胞自动机,每个单元网格中的细胞根据其邻近的细胞进行更新。每个进程需要其本地块中直接相邻的细胞才能计算一个迭代的结果。下面的代码可以实现这个功能:

```julia
function life_step(d::DArray)
    DArray(size(d),procs(d)) do I
        top   = mod(first(I[1])-2,size(d,1))+1
        bot   = mod( last(I[1])  ,size(d,1))+1
        left  = mod(first(I[2])-2,size(d,2))+1
        right = mod( last(I[2])  ,size(d,2))+1

        old = Array(Bool, length(I[1])+2, length(I[2])+2)
        old[1      , 1      ] = d[top , left]   # left side
        old[2:end-1, 1      ] = d[I[1], left]
        old[end    , 1      ] = d[bot , left]
        old[1      , 2:end-1] = d[top , I[2]]
        old[2:end-1, 2:end-1] = d[I[1], I[2]]   # middle
        old[end    , 2:end-1] = d[bot , I[2]]
        old[1      , end    ] = d[top , right]  # right side
        old[2:end-1, end    ] = d[I[1], right]
        old[end    , end    ] = d[bot , right]

        life_rule(old)
    end
end
```

可以看到,我们使用一系列的索引表达式来获取一个本地数组中的数组 `old`。注意,`do` 块语法方便 `init` 函数传递给 `DArray` 构造函数。接下来,连续函数 `life_rule` 被调用以提供数据的更新规则，产生所需的 `DArray` 块。 `life_rule` 与 `DArray-specific` 没有关系,但为了完整性，我们在此仍将它列出:

```julia
function life_rule(old)
    m, n = size(old)
    new = similar(old, m-2, n-2)
    for j = 2:n-1
        for i = 2:m-1
            nc = +(old[i-1,j-1], old[i-1,j], old[i-1,j+1],
                   old[i  ,j-1],             old[i  ,j+1],
                   old[i+1,j-1], old[i+1,j], old[i+1,j+1])
            new[i-1,j-1] = (nc == 3 || nc == 2 && old[i,j])
        end
    end
    new
end
```

## 共享数组 (用于试验, 仅在 unix 上)

共享阵列使用在许多进程中共享内存来映射相同数组的系统。虽然与 `DArray` 有一些相似之处,但是 `SharedArray` 的行为是完全不同的。在一个 `DArray` 中,每个进程只能本地访问一块数据,并且两个进程共享同一块;相比之下,在 `SharedArray` 中，每个“参与”的进程能够访问整个数组。当你想要在同一台机器上大量数据共同访问两个或两个以上的进程时， `SharedArray` 是一个不错的选择。

`SharedArray` 索引(分配和访问值)与常规数组一样工作,并且是非常高效的,因为其底层内存可用于本地进程。因此,大多数算法自然地在 `SharedArrays` 上运行,即使在单进程模式中。当某个算法必须在一个 `Array` 输入的情况下,可以从 `SharedArray` 检索底层数组通过调用 `sdata(S)` 取回。对于其他 `AbstractArray` 类型, `sdata` 返回对象本身,所以在任何数组类型下使用 `sdata` 都是很安全的。

共享数字构造函数数的形式:

```
SharedArray(T::Type, dims::NTuple; init=false, pids=Int[])
```

创建一个被 `pids` 进程指定的，bitstype 为 `T` 并且大小为 `dims` 的共享数组。与分布式阵列不同,共享数组只能用于这些参与人员指定的以 `pid` 命名的参数(如果在同一个主机上，创建过程也同样如此)。

如果一个签名为 `initfn(S::SharedArray)` 的 `init` 函数被指定,它会被所有参与人员调用。你可以控制它，每个工人可以在数组的不同部分运行 `init` 函数,因此进行并行的初始化。

这里有一个简单的例子:

```julia
addprocs(3)

S = SharedArray(Int, (3,4), init = S -> S[localindexes(S)] = myid())

S[3,2] = 7

S
```

`localindexes` 提供不相交的一维索引的范围,它有时方便进程之间的任务交流。当然,你可以按你希望的方式来划分工作:

```julia
S = SharedArray(Int, (3,4), init = S -> S[myid()-1:nworkers():length(S)] = myid())
```

因为所有进程都可以访问底层数据,你必须小心不要设置冲突。例如:

```julia
@sync begin
  for p in workers()
      @async begin
          remotecall_wait(p, fill!, S, p)
      end
  end
end
```

这有可能导致未定义的行为:因为每个进程有他自己的 `pid` 来充满整个数组,无论最后执行的是哪一个进程（任何特定元素 `S`）都将保留他的 `pid`。

## ClusterManagers

Julia 工作进程也可以在任意机器中产生,让 Julia 的自然并行功能非常透明地在集群环境中运行。`ClusterManager` 接口提供了一种方法来指定启动和管理工作进程的手段。例如, `ssh` 集群也使用 `ClusterManager` 来实现:

```julia
immutable SSHManager <: ClusterManager
    launch::Function
    manage::Function
    machines::AbstractVector

    SSHManager(; machines=[]) = new(launch_ssh_workers, manage_ssh_workers, machines)
end

function launch_ssh_workers(cman::SSHManager, np::Integer, config::Dict)
    ...
end

function manage_ssh_workers(id::Integer, config::Dict, op::Symbol)
    ...
end
```

`launch_ssh_workers` 负责实例化新的 Julia 进程并且 `manage_ssh_workers` 提供了一种方法来管理这些进程,例如发送中断信号。在运行时可以使用 `addprocs` 添加新进程:

```
addprocs(5, cman=LocalManager())
```

来指定添加一批进程并且 `ClusterManager` 用于启动这些进程。

脚注

[1]:在这边文中, MPI 是指 MPI-1 标准。从 MPI-2 开始,MPI 标准委员会引入了一系列新的通信机制,统称为远程内存访问 (RMA) 。添加 RMA MPI 标准的动机是改善单方面的沟通模式。最新的 MPI 标准的更多信息,参见 <http://www.mpi-forum.org/docs>。


