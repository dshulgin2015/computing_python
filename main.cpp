#include <iostream>


bool accept()
{
std::cout << "Do you want to proceed (y or n)?\n";
char answer = 0;
std::cin >> answer;
// write question
// read answer
if (answer == 'y') return true;
return false;
};


int main()
{
bool a = true;
std::cout << a << std::endl;
std::cout << accept();
}


