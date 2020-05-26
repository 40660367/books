# C++ 聚合(aggregation)

在C++中，聚合是一个进程，一个类将另一个类定义为实体引用(一个类作为另一个类的成员)。 这是另一种重用类的方法。 它是一种表示**HAS-A**关系的关联形式。

## C++聚合示例

下面来看看一个聚合的例子，其中`Employee`类有`Address`类的引用作为数据成员。 这样，它可以重用`Address`类的成员。

文件名:oob-agg.cpp

```cpp
#include <iostream>  
using namespace std;  
class Address {  
    public:  
   string addressLine, city, state;    
     Address(string addressLine, string city, string state)    
    {    
        this->addressLine = addressLine;    
        this->city = city;    
        this->state = state;    
    }    
};  
class Employee    
    {    
        private:  
        Address* address;  //Employee HAS-A Address   
        public:  
        int id;    
        string name;    
        Employee(int id, string name, Address* address)    
       {    
           this->id = id;    
           this->name = name;    
           this->address = address;    
       }    
     void display()    
       {    
           cout<<id <<" "<<name<< " "<<     
             address->addressLine<< " "<< address->city<< " "<<address->state<<endl;    
       }    
   };   
int main(void) {  
    Address a1= Address("Renmin Road-15","Haikou","UP");    
    Employee e1 = Employee(101,"Beijing",&a1);    
            e1.display();   
   return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-agg.cpp && ./a.out
```

康康