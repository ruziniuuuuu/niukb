#include <iostream>
#include "cat.h"
using namespace std;

int main(int argc, char *argv[])
{
    // const object
    // 值
    const Cat cat1("moon", 3);
    // const object只能调用const method
    cout << cat1.get_name() << endl;
    cat1.print_object();
    // 指针
    const Cat* cat_point{&cat1};
    cout << cat_point->get_name() << endl;
    cat_point->print_object();

    // 引用
    const Cat &cat_ref{cat1};
    cout << cat_ref.get_name() << endl;
    cat_ref.print_object();
    cout << "----- yz ------" << endl;
    return 0;
}