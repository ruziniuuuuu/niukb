#include <iostream>
#include "cat.h"
using namespace std;

void func_take_cat(Cat cat)
{
    cat.set_name("good cat");
    cat.print_object();
}

void func_take_cat_const(const Cat cat)
{
    // cat.set_name("good cat"); // 报错
    cat.print_object();
}

void func_take_cat_pointer(Cat *cat)
{
    cat->set_name("good cat");
    cat->print_object();
}

void func_take_cat_pointer_const(const Cat *cat)
{
    // cat->set_name("good cat"); // 报错
    cat->print_object();
}

void func_take_cat_ref(Cat cat)
{
    cat.set_name("good cat");
    cat.print_object();
}

void func_take_cat_ref_const(const Cat cat)
{
    // cat.set_name("good cat"); // 报错
    cat.print_object();
}

int main(int argc, char *argv[])
{
    Cat cat1("oo", 3);
    func_take_cat(cat1);
    func_take_cat_const(cat1);
    Cat *cat_point{&cat1};
    func_take_cat_pointer(cat_point);
    func_take_cat_pointer_const(cat_point);
    Cat &cat_ref{cat1};
    func_take_cat_ref(cat_ref);
    func_take_cat_ref_const(cat_ref);

    cout << "----- yz ------" << endl;
    return 0;
}