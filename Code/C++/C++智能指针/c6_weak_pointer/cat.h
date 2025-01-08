#ifndef CAT_H
#define CAT_H
#include <string>
#include <iostream>
#include <memory>

class Cat {
public:
    Cat(std::string name);
    Cat() = default;
    ~Cat();
    void cat_info() const{
        std::cout << "Cat info name: " << name << std::endl;
    }
    std::string get_name() const{
        return name;
    }
    void set_cat_name(const std::string& name){
        this->name = name;
    }
    void set_friend(std::shared_ptr<Cat> c){
        m_friend = c;
    }

private:
    std::string name{"Mimi"};
    // std::shared_ptr<Cat> m_friend;
    std::weak_ptr<Cat> m_friend;
};

#endif