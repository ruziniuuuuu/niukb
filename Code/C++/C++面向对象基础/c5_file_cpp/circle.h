#ifndef CIRCLE_H
#define CIRCLE_H
#include <iostream>
#include "constants.h"

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
        std::cout << "constructor default" << std::endl;
    }
    Circle(double radius)
    {
        number++;
        this->radius = radius;
        std::cout << "constructor" << std::endl;
    }
    ~Circle()
    {
        // 实例减少1
        number--;
        std::cout << "destructor" << std::endl;
        std::cout << number << std::endl;
    }

    // Setter and Getter
    double get_radius();

    double set_radius(double radius);

    double area();

    void print_object();

    // 链式调用，返回指针
    // object->a()->b()
    Circle *set_radius_point(double radius);
    Circle *print_radius_point();
    Circle &set_radius_ref(double radius);
    Circle &print_radius_ref(double radius);

private:
    double radius{0};
};

#endif