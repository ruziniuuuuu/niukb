#include "stack"
#include "string"
#include "iostream"
using namespace std;

string func(string a, string b) {

    int len_a = a.size();
    int len_b = b.size();

    stack<int> stk_a;
    stack<int> stk_b;

    // push
    for (int i = 0; i < len_a; i++) {
        stk_a.push(int(a[i] - '0'));
    }
    for (int i = 0; i < len_b; i++) {
        stk_b.push(int(b[i] - '0'));
    }

    // enum
    int c = 0;
    int add = 0;
    stack<int> res;
    string str_res;

    while (!stk_a.empty() && !stk_b.empty()) {
        int add_1 = 0;
        int add_2 = 0;

        if (stk_a.empty()) {
            add_2 = stk_b.top(); stk_b.pop();
        } else
        if (stk_b.empty()) {
            add_1 = stk_a.top(); stk_a.pop();
        } else {
            add_1 = stk_a.top(); stk_a.pop();
            add_2 = stk_b.top(); stk_b.pop();
        }

        add = add_1 + add_2 + c;

        if (add >= 10) c = 1;
        else c = 0;

        res.push(add % 10);
    }

    if (c == 1) {
        res.push(c);
    }

    while (res.top() == 0) {
        res.pop();
    }

    while (!res.empty()) {
        str_res.push_back(res.top());
        res.pop();
    }

    return str_res;
}


int main() {
    string a = "12345";
    string b = "54321";
    cout << func(a, b) << endl;
}