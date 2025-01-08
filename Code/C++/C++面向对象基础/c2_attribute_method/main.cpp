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
    Circle(double param_radius)
    {
        number++;
        radius = param_radius;
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

private:
    double radius{0};
};

// 初始化类属性
int Circle::number = 0;

int main(int argc, char *argv[])
{
    // 栈上的对象
    Circle circle(2);
    cout << Circle::number << endl;
    cout << "area: "<< circle.area() << endl;

    // 堆上的对象，需要自己删除
    Circle *pCircle = new Circle(3);
    cout << Circle::number << endl;
    cout << "area: "<< pCircle->area() << endl;
    delete pCircle;
    pCircle = nullptr;
    
    cout << "----- yz ------" << endl;
    return 0;
}