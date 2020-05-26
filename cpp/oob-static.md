# C++ static关键字

在C++中，`static`是属于类而不是实例的关键字或修饰符。 因此，不需要实例来访问静态成员。 在C++中，`static`可以是字段，方法，构造函数，类，属性，操作符和事件。

**C++ static关键字的优点**

**内存效率：** 现在我们不需要创建实例来访问静态成员，因此它节省了内存。 此外，它属于一种类型，所以每次创建实例时不会再去获取内存。

## C++静态字段

使用`static`关键字声明字段称为静态字段。它不像每次创建对象时都要获取内存的实例字段，在内存中只创建一个静态字段的副本。它被共享给所有的对象。

它用于引用所有对象的公共属性，如：`Account`类中的利率(`rateOfInterest`)，`Employee`类中的公司名称(`companyName`)等。

## C++静态字段示例

下面来看看看C++中静态(`static`)字段的简单示例。

文件名:oob-static1.cpp

```cpp
#include <iostream>  
using namespace std;  
class Account {  
   public:  
       int accno; //data member (also instance variable)      
       string name; //data member(also instance variable)  
       static float rateOfInterest;   
       Account(int accno, string name)   
        {    
            this->accno = accno;    
            this->name = name;    
        }    
       void display()    
        {    
            cout<<accno<<" "<<name<< " "<<rateOfInterest<<endl;
        }    
};  
float Account::rateOfInterest=6.5;  
int main(void) {  
    Account a1 =Account(201, "Sanjay"); //creating an object of Employee   
    Account a2=Account(202, "Calf"); //creating an object of Employee  
    a1.display();    
    a2.display();    
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-static1.cpp && ./a.out
```

康康

## C++静态字段示例：统计对象数量

下面来看看看C++中`static`关键字的另一个例子，统计创建对象的数量。

文件名:oob-static2.cpp

```cpp
#include <iostream>  
using namespace std;  
class Account {  
   public:  
       int accno; //data member (also instance variable)      
       string name;   
       static int count;     
       Account(int accno, string name)   
        {    
            this->accno = accno;    
            this->name = name;    
            count++;  
        }    
       void display()    
        {    
            cout<<accno<<" "<<name<<endl;   
        }    
};  
int Account::count=0;  
int main(void) {  
    Account a1 =Account(201, "Sanjay"); //creating an object of Account  
    Account a2=Account(202, "Calf");   
    Account a3=Account(203, "Ranjana");  
    a1.display();    
    a2.display();    
    a3.display();    
    cout<<"Total Objects are: "<<Account::count;  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-static2.cpp && ./a.out
```

康康