#include <iostream>
#include <memory>
#include "cat.h"
using namespace std;

void do_with_cat_pass_value(std::unique_ptr<Cat> c)
{
    c->cat_info();
}

void do_with_cat_pass_ref(const std::unique_ptr<Cat> &c)
{
    c->set_cat_name("hh");
    c->cat_info();
    // c.reset(); // 释放资源
}

// 链式
std::unique_ptr<Cat> get_unique_ptr()
{
    std::unique_ptr<Cat> p_dog = make_unique<Cat>("Local Cat");
    cout << "unique address: " << p_dog.get() << endl;
    cout << "unique address: " << &p_dog << endl;
    return p_dog;
}

int main(int argc, char *argv[])
{
    // 1 pass by value
    std::unique_ptr<Cat> c1 = make_unique<Cat>("ff");
    // do_with_cat_pass_value(c1); // 所有权有问题，会报错
    do_with_cat_pass_value(std::move(c1)); // 通过std::move转移所有权
    // c1->cat_info(); // c1已经没有所有权了
    do_with_cat_pass_value(make_unique<Cat>("gg")); // 临时对象，所有权转移给函数

    // 2 pass by reference
    std::unique_ptr<Cat> c2 = make_unique<Cat>("ii");
    c2->cat_info();
    do_with_cat_pass_ref(c2);
    // c2->cat_info(); // c2已经没有所有权了

    // 链式
    get_unique_ptr()->cat_info();

    cout << "----- done -----" << endl;
    return 0;
}