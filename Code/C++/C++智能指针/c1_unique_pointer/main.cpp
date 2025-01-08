#include <iostream>
#include <memory>
#include "cat.h"
using namespace std;

int main(int argc, char *argv[])
{
    // stack
    // Cat c1("OK");
    // c1.cat_info();
    // {
    //     Cat c1("OK");
    //     c1.cat_info();
    // }

    // heap
    // raw pointer
    // Cat *c_p1 = new Cat("yy");
    // int *i_p1 = new int(200);
    // c_p1->cat_info();
    // {
    //     Cat *c_p1 = new Cat("yy_scope");
    //     int *i_p1 = new int(100);
    //     c_p1->cat_info();
    //     delete c_p1;
    //     delete i_p1;
    // }
    // delete c_p1;

    // unique_pointer的三种创建方式
    Cat *c_p2 = new Cat("yz");
    std::unique_ptr<Cat> u_c_p2{c_p2};

    // c_p2还能用吗
    // 建议销毁，否则如下
    // c_p2->cat_info();
    // u_c_p2->cat_info();
    // c_p2->set_cat_name("ok");
    // u_c_p2->cat_info(); // c_p2和u_c_p2指向同一个对象，所以u_c_p2的cat_name也被改变了

    // delete c_p2;   // 释放c_p2，会导致u_c_p2指向的对象被释放，所以u_c_p2不能再使用
    c_p2 = nullptr;
    u_c_p2->cat_info();

    // 第二种new
    std::unique_ptr<Cat> u_c_p3 {new Cat("dd")};
    std::unique_ptr<int> u_i_p3 {new int(100)};
    u_c_p3->cat_info();
    u_c_p3->set_cat_name("oo");
    u_c_p3->cat_info();
    cout << *u_i_p3 << endl;
    cout << "int address: " << u_i_p3.get() << endl;
    cout << "cat address: " << u_c_p3.get() << endl;
    
    cout << endl;

    // 推荐创建方式 第三种 std::make_unique
    std::unique_ptr<Cat> u_c_p4 = make_unique<Cat>();
    std::unique_ptr<int> u_i_p4 = make_unique<int>(200);
    u_c_p4->cat_info();
    u_c_p4->set_cat_name("oo");
    u_c_p4->cat_info();
    cout << *u_i_p4 << endl;
    cout << "int address: " << u_i_p4.get() << endl;
    cout << "cat address: " << u_c_p4.get() << endl;
    // get和常量类型
    

    cout << "----- done -----" << endl;
    return 0;
}