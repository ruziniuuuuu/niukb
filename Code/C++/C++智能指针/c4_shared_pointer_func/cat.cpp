#include "cat.h"

Cat::Cat(std::string name) : name(name) {
    std::cout << "Cat " << name << " is created" << std::endl;
}

Cat::~Cat() {
    std::cout << "Cat " << name << " is destroyed" << std::endl;
}
