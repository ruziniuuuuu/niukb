#include <iostream>
using namespace std;

class Vector2
{
public:
    // 构造函数
    Vector2(int x, int y): x(x), y(y)
    {
        cout << "Vector2 constructor" << endl;
    }
    virtual ~Vector2() { cout << "virtual" << endl; }
    virtual void print() const
    {
        cout << "(" << x << ", " << y << ")" << endl;
    }
protected:
// private:
    int x;
    int y;
};

class Vector3 : public Vector2
{
public:
    Vector3(int x, int y, int z): Vector2(x, y), z(z)
    {
        cout << "Vector3 constructor" << endl;
    }
    void print() const
    {
        cout << "(" << x << ", " << y << ", "<< z << ")" << endl;
    }
private:
    int z;
};

int main(int argc, char *argv[])
{
    // 在栈上创建
    Vector2 ex(1, 3);
    Vector3 ex3(2, 3, 4);
    ex3.print();

    // 在堆上创建
    Vector2 *demo2d = new Vector2(1, 2);
    delete demo2d;

    Vector3 *demo3d = new Vector3(1, 2, 3);
    demo3d->print();
    delete demo3d;
    cout << "----- yz ------" << endl;
    return 0;
}