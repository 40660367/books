# Lua 面向对象编程

面向对象编程(OOP)是现代编程中使用最多的编程技术之一。 有许多支持OOP的编程语言包括

- C++
- Java
- Objective-C
- Smalltalk
- C#
- Ruby

## 面向对象的特点

- **类** - 类是用于创建对象的可扩展模板，为状态(成员变量)和行为实现提供初始值。
- **对象** - 它是类的一个实例，并为自己分配了单独的内存。
- **继承** - 这是一个概念，通过该概念，一个类的变量和函数由另一个类继承。
- **封装** - 这是在类中组合数据和函数的过程。借助函数可以在类的外部访问数据。 它也被称为数据抽象。

## Lua面向对象

可使用Lua的表和第一类函数在Lua中实现面向对象。 通过将函数和相关数据放入表中，形成对象。可使用元表实现继承，为父对象中不存在的函数(方法)和字段提供查找机制。

Lua中的表具有状态和标识等对象的特征，与其值无关。 具有相同值的两个对象(表)是不同的对象，而对象在不同的时间可以具有不同的值，但它始终是相同的对象。 与对象一样，表的生命周期与谁创建它们或创建位置无关。

## 真实世界的例子

面向对象的概念广泛使用，但需要清楚地理解面向对象以获得适当和最大的好处。
考虑一个简单的数学例子。 我们经常遇到处理不同形状的情况，如圆形，矩形和方形。

形状可以具有共同的属性`area`。 因此，使用公共属性区域从基础对象形状扩展其他形状。 每个形状都可以有自己的属性，像矩形这样的函数可以具有属性`length`，`width`，`area`作为属性，`printArea`和`calculateArea`作为它的函数。

## 创建一个简单的类

下面显示了具有三个属性`length`，`width`和`area`的矩形的简单类实现。 它还有一个`printArea`函数来打印计算区域面积。

```lua
-- Meta class
Rectangle = {area = 0, length = 0, breadth = 0}

-- Derived class method new

function Rectangle:new (o,length,breadth)
   o = o or {}
   setmetatable(o, self)
   self.__index = self
   self.length = length or 0
   self.breadth = breadth or 0
   self.area = length*breadth;
   return o
end

-- Derived class method printArea

function Rectangle:printArea ()
   print("The area of Rectangle is ",self.area)
end
```

**创建一个对象**
创建对象是为类实例分配内存的过程。 每个对象都有自己的内存并共享公共类数据。

```lua
r = Rectangle:new(nil,10,20)
```

**访问属性**
可以使用点(`.`)运算符访问类中的属性，如下所示 - 

```lua
print(r.length)
```

**访问成员函数**

使用带有对象的冒号(`:`)运算符访问成员函数，如下所示 - 

```lua
r = Rectangle:new(nil,10,20)
r:printArea()
```

分配内存并设置初始值。可以将初始化过程与其他面向对象语言中的构造函数进行比较。 它只是一个能够设置如上所示的值的函数。

**完整的例子**
下面来看一下在Lua中使用面向对象的完整示例。

文件名:oob1.lua

```lua
-- Meta class
Shape = {area = 0}

-- Base class method new

function Shape:new (o,side)
   o = o or {}
   setmetatable(o, self)
   self.__index = self
   side = side or 0
   self.area = side*side;
   return o
end

-- Base class method printArea

function Shape:printArea ()
   print("The area is ",self.area)
end

-- Creating an object
myshape = Shape:new(nil,10)

myshape:printArea()
```

```bash
lua /share/lesson/lua/oob1.lua
```

康康

## Lua继承

继承是将简单的基础对象(如形状)扩展为矩形，正方形等的过程。 它经常在现实世界中用于共享和扩展基本属性和功能。

下面来看一个简单的类扩展。有一个如下所示的类，

```lua
-- 元类
Shape = {area = 0}

-- 基类方法
function Shape:new (o,side)
   o = o or {}
   setmetatable(o, self)
   self.__index = self
   side = side or 0
   self.area = side*side;
   return o
end

-- 基类方法 - printArea

function Shape:printArea ()
   print("The area is ",self.area)
end
```

可以将形状扩展为方形类，如下所示。

```lua
Square = Shape:new()

-- Derived class method new

function Square:new (o,side)
   o = o or Shape:new(o,side)
   setmetatable(o, self)
   self.__index = self
   return o
end
```

**覆盖基类函数**

可以覆盖基类函数而不是在基类中使用函数，派生类可以有自己的实现，如下所示 - 

```lua
-- Derived class method printArea

function Square:printArea ()
   print("The area of square is ",self.area)
end
```

**继承完整示例**
在另一个`new`方法的帮助下，使用`metatables`，扩展Lua中的简单类实现，如上所示。 基类的所有成员变量和函数都保留在派生类中。

文件名:oob2.lua

```lua
-- Meta class
Shape = {area = 0}

-- Base class method new

function Shape:new (o,side)
   o = o or {}
   setmetatable(o, self)
   self.__index = self
   side = side or 0
   self.area = side*side;
   return o
end

-- Base class method printArea

function Shape:printArea ()
   print("The area is ",self.area)
end

-- Creating an object
myshape = Shape:new(nil,10)
myshape:printArea()

Square = Shape:new()

-- Derived class method new

function Square:new (o,side)
   o = o or Shape:new(o,side)
   setmetatable(o, self)
   self.__index = self
   return o
end

-- Derived class method printArea

function Square:printArea ()
   print("The area of square is ",self.area)
end

-- Creating an object
mysquare = Square:new(nil,10)
mysquare:printArea()

Rectangle = Shape:new()

-- Derived class method new

function Rectangle:new (o,length,breadth)
   o = o or Shape:new(o)
   setmetatable(o, self)
   self.__index = self
   self.area = length * breadth
   return o
end

-- Derived class method printArea

function Rectangle:printArea ()
    print("The area of Rectangle is ",self.area)
end

-- Creating an object

myrectangle = Rectangle:new(nil,10,20)
myrectangle:printArea()
```

```bash
lua /share/lesson/lua/oob2.lua
```

康康

在上面的例子中，创建了两个派生类 - 基类`Square`和`Rectangle`。并在派生类中覆盖基类的函数。 在此示例中，派生类会覆盖函数`printArea`。