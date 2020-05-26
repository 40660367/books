# C++ this关键字

在C++编程中，`this`是一个引用类的当前实例的关键字。 `this`关键字在C++中可以有`3`个主要用途。

1. 用于将当前对象作为参数传递给另一个方法。
2. 用来引用当前类的实例变量。
3. 用来声明索引器。

## C++ this指针的例子

下面来看看看`this`关键字在C++中的例子，它指的是当前类的字段。

文件名:oob-this.cpp

```cpp
#include <iostream>  
using namespace std;  
class Employee {  
   public:  
       int id; //data member (also instance variable)      
       string name; //data member(also instance variable)  
       float salary;  
       Employee(int id, string name, float salary)    
        {    
             this->id = id;    
            this->name = name;    
            this->salary = salary;   
        }    
       void display()    
        {    	
            cout<<id<<"  "<<name<<"  "<<salary<<endl;    
        }    
};  
int main(void) {  
    Employee e1 =Employee(101, "Hema", 890000); //creating an object of Employee   
    Employee e2=Employee(102, "Calf", 59000); //creating an object of Employee  
    e1.display();    
    e2.display();    
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-this.cpp && ./a.out
```

康康