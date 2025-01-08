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
    // 值类型
    const Cat cat("cat1", 2);
    // 值不可变可以传入可变参数函数
    func_take_cat(cat);
    func_take_cat_const(cat);

    // 指针类型
    const Cat *cat_point{&cat};
    // 指针类型不可以传入可变参数
    // func_take_cat_pointer(cat_point); // 报错
    func_take_cat_pointer_const(cat_point);
    // 引用类型
    const Cat &cat_ref{cat};
    cout << "----- yz ------" << endl;
    return 0;
}