# C++ 对象和类(object and class)			

由于C++是一种面向对象的语言，程序可使用C++中的对象和类来设计。

## C++对象

在C++中，对象是一个真实世界的实体，例如：椅子，汽车，笔，手机，笔记本电脑等。换句话说，对象是一个具有状态和行为的实体。 这里，状态意味着数据，而行为意味着功能。
对象是一个运行时实体，它在运行时创建。

对象是类的一个实例。 类的所有成员都可以通过对象访问。下面来看看一个使用`s1`作为引用变量创建`Student`类对象的示例。

```cpp
Student s1;  //creating an object of Student
```

在此示例中，`Student`是类型，`s1`是引用`Student`类的实例的引用变量。

## C++类

在C++中，对象是一组相似的类。 它是一个模板，用于从中创建对象。 它可以有字段，方法，构造函数等。

下面来看看一个只有三个字段的C++类的例子。

```cpp
class Student    
 {    
     public:  
         int id;  //field or data member     
         float salary; //field or data member  
         String name;//field or data member    
 }
```

## C++对象和类示例

下面来看看一个有两个字段的类的例子：`id`和`name`。 它创建类的实例，初始化对象并打印对象值。

文件名:oob-oc1.cpp

```cpp
#include <iostream>  
using namespace std;  
class Student {  
   public:  
      int id;//data member (also instance variable)      
      string name;//data member(also instance variable)      
};  
int main() {  
    Student s1; //creating an object of Student   
    s1.id = 201;    
    s1.name = "Joker Wang";   
    cout<<s1.id<<endl;  
    cout<<s1.name<<endl;  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-oc1.cpp && ./a.out
```

康康

**C++类示例：通过方法初始化和显示数据**

下面来看看看另一个C++类的例子，我们通过方法初始化并显示对象。

文件名:oob-oc2.cpp

```cpp
#include <iostream>  
using namespace std;  
class Student {  
   public:  
       int id;//data member (also instance variable)      
       string name;//data member(also instance variable)      
       void insert(int i, string n)    
        {    
            id = i;    
            name = n;    
        }    
       void display()    
        {    
            cout<<id<<"  "<<name<<endl;    
        }    
};  
int main(void) {  
    Student s1; //creating an object of Student   
    Student s2; //creating an object of Student  
    s1.insert(201, "Wei");    
    s2.insert(202, "Hema");    
    s1.display();    
    s2.display();  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-oc2.cpp && ./a.out
```

康康

**C++类示例：存储和显示员工信息**

下面来看看看另一个C++类的例子，使用方法存储和显示员工的信息。

文件名:oob-oc3.cpp

```cpp
#include <iostream>  
using namespace std;  
class Employee {  
   public:  
       int id;//data member (also instance variable)      
       string name;//data member(also instance variable)  
       float salary;  
       void insert(int i, string n, float s)    
        {    
            id = i;    
            name = n;    
            salary = s;  
        }    
       void display()    
        {    
            cout<<id<<"  "<<name<<"  "<<salary<<endl;    
        }    
};  
int main(void) {  
    Employee e1; //creating an object of Employee   
    Employee e2; //creating an object of Employee  
    e1.insert(201, "Wei",99000);    
    e2.insert(202, "Hema", 29000);    
    e1.display();    
    e2.display();    
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-oc3.cpp && ./a.out
```

康康