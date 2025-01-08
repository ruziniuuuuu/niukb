#include <iostream>
using namespace std;

const double PI(3.1415926);

class Circle
{
public:
    static int number;
    // constructor
    Circle()
    {
        // 实例增加1
        number++;
        radius = 1.0;
        cout << "constructor default" << endl;
    }
    Circle(double radius)
    {
        number++;
        this->radius = radius;
        cout << "constructor" << endl;
    }
    ~Circle()
    {
        // 实例减少1
        number--;
        cout << "destructor" << endl;
        cout << number << endl;
    }
    double area()
    {
        return PI * radius * radius;
    }
    void print_object()
    {
        cout << "Object address: " << this << endl;
        cout << "radius: " << this->radius << endl;
    }

    // 链式调用，返回指针
    // object->a()->b()
    Circle *set_radius_point(double radius)
    {
        cout << "set point: " << radius << endl;
        this->radius = radius;
        return this;
    }
    Circle *print_radius_point()
    {
        cout << "print point: " << this->radius << endl;
        return this;
    }
    Circle &set_radius_ref(double radius)
    {
        cout << "set point" << endl;
        this->radius = radius;
        return *this;
    }
    Circle &print_radius_ref(double radius)
    {
        cout << "print: " << this->radius << endl;
        return *this;
    }

private:
    double radius{0};
};

// 初始化类属性
int Circle::number = 0;

int main(int argc, char *argv[])
{
    // 堆上
    Circle *c = new Circle(3);
    c->print_object();
    c->print_radius_point()->set_radius_point(4)->print_radius_point();

    // 栈上 gdb
    Circle c1(3);
    c1.print_object();
    c1.print_radius_point()->set_radius_point(4)->print_radius_point();
    
    cout << "----- yz ------" << endl;
    return 0;
}