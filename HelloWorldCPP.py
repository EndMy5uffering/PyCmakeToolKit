TXT = '''#include "HelloWorld.hpp"

HelloWorld::HelloWorld(std::string text) 
:
m_text{text}
{
}

HelloWorld::~HelloWorld() 
{
}

void HelloWorld::Print() 
{
    std::cout << "From Hello World: " << m_text << "\\n";
}

'''