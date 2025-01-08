#include <iostream>
#include "constants.h"
#include "circle.h"
using namespace std;

int main(int argc, char *argv[])
{
    // 堆上
    Circle *c = new Circle(3);
    c->print_object();
    c->print_radius_point()->set_radius_point(4)->print_radius_point();
    cout << "get set:" << endl;
    cout << "get radius: " << c->get_radius() << endl;

    // 栈上 gdb
    Circle c1(3);
    c1.print_object();
    c1.print_radius_point()->set_radius_point(4)->print_radius_point();
    cout << "get set:" << endl;
    cout << "get radius: " << c1.get_radius() << endl;
    
    cout << "----- yz ------" << endl;
    return 0;
}