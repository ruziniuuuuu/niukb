#include <iostream>
#include <memory>
#include "cat.h"
using namespace std;

void cat_by_value(std::shared_ptr<Cat> c)
{
    cout << c->get_name() << endl;
    c->set_cat_name("mm");
    cout << "use count: " << c.use_count() << endl;
}

void cat_by_ref(std::shared_ptr<Cat> &c)
{
    cout << c->get_name() << endl;
    c->set_cat_name("nn");
    c.reset(new Cat());
    cout << "use count: " << c.use_count() << endl;
}

// void cat_by_ref(const std::shared_ptr<Cat> &c)
// {
//     cout << c->get_name() << endl;
//     c->set_cat_name("nn");
//     // c.reset(new Cat());
//     cout << "use count: " << c.use_count() << endl;
// }

// 一般不这么用
std::shared_ptr<Cat> get_shared_ptr()
{
    std::shared_ptr<Cat> c_p = make_shared<Cat>("Local Cat");
    return c_p;
}

int main(int argc, char *argv[])
{
    std::shared_ptr<Cat> c1 = make_shared<Cat>();
    c1->cat_info();
    cat_by_value(c1);
    c1->cat_info();
    cout << "use count: " << c1.use_count() << endl;

    cat_by_ref(c1);
    c1->cat_info();
    cout << "use count: " << c1.use_count() << endl;

    std::shared_ptr<Cat> c_p = get_shared_ptr();
    c_p->cat_info();

    // 链式
    get_shared_ptr()->cat_info();

    cout << "----- done -----" << endl;
    return 0;
}