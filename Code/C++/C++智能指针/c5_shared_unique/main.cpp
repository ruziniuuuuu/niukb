#include <iostream>
#include <memory>
#include "cat.h"
using namespace std;

std::unique_ptr<Cat> get_unique_ptr()
{
    std::unique_ptr<Cat> c_p = make_unique<Cat>("Local Cat");
    return c_p;
}

int main(int argc, char *argv[])
{
    std::unique_ptr<Cat> c_p_1 = make_unique<Cat>("dd");
    std::shared_ptr<Cat> c_p_2 = std::move(c_p_1);

    cout << "c_p_2 use count: " << c_p_2.use_count() << endl; // 1

    // func
    // 将unique_ptr转换为shared_ptr
    std::shared_ptr<Cat> c_p_3 = get_unique_ptr();
    if (c_p_3)
    {
        // 可以进行转换
        c_p_3->cat_info();
        cout << "c_p_3 use count: " << c_p_3.use_count() << endl;
    }

    cout << "----- done -----" << endl;
    return 0;
}