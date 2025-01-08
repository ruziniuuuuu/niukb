#include <iostream>
#include <memory>
#include "cat.h"
using namespace std;

int main(int argc, char *argv[])
{
    std::shared_ptr<Cat> s_p_c1 = std::make_shared<Cat>("C1");
    std::weak_ptr<Cat> w_p_c1(s_p_c1);

    // use_count()
    // 返回与此shared_ptr共享对象的所有者数量
    cout << "s_p_c1 use count: " << s_p_c1.use_count() << endl; // 1
    cout << "w_p_c1 use count: " << w_p_c1.use_count() << endl; // 1

    // lock()可以将weak_ptr转换为shared_ptr
    std::shared_ptr<Cat> s_p_c2 = w_p_c1.lock();
    cout << "s_p_c1 use count: " << s_p_c1.use_count() << endl; // 2
    cout << "w_p_c1 use count: " << w_p_c1.use_count() << endl; // 2
    cout << "s_p_c2 use count: " << s_p_c2.use_count() << endl; // 2

    // 循环依赖问题
    std::shared_ptr<Cat> c3 = std::make_shared<Cat>("C3");
    std::shared_ptr<Cat> c4 = std::make_shared<Cat>("C4");
    c3->set_friend(c4);
    c4->set_friend(c3);
    // 此时C3和C4互相引用，导致引用计数无法为0，内存泄漏
    // C3和C4无法析构
    // 解决方法：使用weak_ptr替换shared_ptr

    cout << "----- done -----" << endl;
    return 0;
}