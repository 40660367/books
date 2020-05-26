# C++ 继承(inheritance)

在C++中，继承是一个对象自动获取其父对象的所有属性和行为的过程。 在示例方式中，您可以重用，扩展或修改在其他类中定义的属性和行为。

在C++中，继承另一个类的成员的类称为派生类，其成员被继承的类称为基类。 派生类是基类的子类。

## C++继承的优点

代码可重用性：现在可以重用父类的成员。 因此，不需要再次定义那些跟父类成员。 因此在类中需要较少的代码，提高了代码的重用。

文件名:oob-inheritance1.cpp

```cpp
#include <iostream>  
using namespace std;  
class Account {  
   public:  
   float salary = 60000;   
};

class Programmer: public Account {  
   public:  
   float bonus = 5000;    
};

int main(void) {  
     Programmer p1;  
     cout<<"Salary: "<<p1.salary<<endl;    
     cout<<"Bonus: "<<p1.bonus<<endl;    
    return 0;  
}
```

在上面的例子中，`Employee`是基类，而`Programmer`类是派生类。

```bash
g++ /share/lesson/cpp/oob-inheritance1.cpp && ./a.out
```

康康

## C++单级继承示例：继承方法

下面来看看看在继承方法的C++继承的另一个例子。

文件名:oob-inheritance2.cpp

```cpp
#include <iostream>  
using namespace std;  
 class Animal {  
   public:  
 void eat() {   
    cout<<"Eating..."<<endl;   
 }    
   };  
   class Dog: public Animal    
   {    
       public:  
     void bark(){  
    cout<<"Barking...";   
     }    
   };   
int main(void) {  
    Dog d1;  
    d1.eat();  
    d1.bark();  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-inheritance2.cpp && ./a.out
```

康康

## C++多级继承示例

当一个类继承一个被另一个类继承的类时，它被称为C++中的多级继承。 继承是传递的，所以最后的派生类获取所有其基类的所有成员。

下面来看看看在C++中多级继承的例子。

文件名:oob-inheritance3.cpp

```cpp
#include <iostream>
using namespace std;
class Animal
{
public:
  void eat()
  {
    cout << "Eating..." << endl;
  }
};
class Dog : public Animal
{
public:
  void bark()
  {
    cout << "Barking..." << endl;
  }
};
class BabyDog : public Dog
{
public:
  void weep()
  {
    cout << "Weeping...";
  }
};
int main(void)
{
  BabyDog d1;
  d1.eat();
  d1.bark();
  d1.weep();
  return 0;
}
```

```bash
g++ /share/lesson/cpp/oob-inheritance3.cpp && ./a.out
```

康康