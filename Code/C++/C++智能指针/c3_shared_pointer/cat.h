#ifndef CAT_H
#define CAT_H
#include <string>
#include <iostream>

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

    private:
        std::string name{"Mimi"};
};

#endif