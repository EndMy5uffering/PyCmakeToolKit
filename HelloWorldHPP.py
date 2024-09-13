TXT = """#ifndef HELLOWORLD_HPP
#define HELLOWORLD_HPP

#include <string>
#include <iostream>

class HelloWorld
{
private:
    std::string m_text;

public:
    HelloWorld(std::string text);
    ~HelloWorld();

    void Print();
};

#endif // HELLOWORLD_HPP
"""