#include "circle.h"

// 初始化类属性
int Circle::number = 0;

// Setter and Getter
double Circle::get_radius()
{
    return radius;
}

double Circle::set_radius(double radius)
{
    return PI * radius * radius;
}

double Circle::area()
{
    return PI * radius * radius;
}
void Circle::print_object()
{
    std::cout << "Object address: " << this << std::endl;
    std::cout << "radius: " << this->get_radius() << std::endl;
}

// 链式调用，返回指针
// object->a()->b()
Circle *Circle::set_radius_point(double radius)
{
    std::cout << "set point: " << radius << std::endl;
    this->radius = radius;
    return this;
}
Circle *Circle::print_radius_point()
{
    std::cout << "print point: " << this->radius << std::endl;
    return this;
}
Circle &Circle::set_radius_ref(double radius)
{
    std::cout << "set point" << std::endl;
    this->radius = radius;
    return *this;
}
Circle &Circle::print_radius_ref(double radius)
{
    std::cout << "print: " << this->get_radius() << std::endl;
    return *this;
}