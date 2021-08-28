//  File simplevectortestfile.cpp

#include <iostream>
#include "vectorutils.h"
#include "vectorutils.cpp"

//  This code performs *extremely* simple
//  tests.  This is only the first steps to any
//  testing you may want to perform.  You must ensure
//  that your vectorstuff.cpp file compiles cleanly
//  with this file.  If the compiler generates errors
//  when using your code and this code together, your
//  code has no chance passing my more extensive test
//  suite.
//
//  Since this is only a very test simple suite, you should
//  create more interesting tests in an attempt to reveal
//  the logic errors that may be lurking in your
//  functions.

// Conveniently print the contents of a vector.
template <typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &vec)
{
    os << '{';
    if (!vec.empty())
    {
        auto iter = vec.begin();
        auto end = vec.end();
        os << *iter++;
        while (iter != end)
            os << ", " << *iter++;
    }
    os << '}';
    return os;
}

int main()
{
    //  Make a small vector of integers
    std::vector<int> list{1, 5, 3, 10, 3, 7, 5, 2};

    //  Some variables to ensure the function return types
    //  are properly assignable.
    int i;
    bool b;

    i = maximum(list);
    std::cout << "The largest in " << list << " is " << i << '\n';
    std::cout << "---------------------------------\n";

    i = find(list, 10);
    std::cout << "10 is at index " << i << " in " << list << '\n';
    std::cout << "---------------------------------\n";

    i = count(list, 3);
    std::cout << "3 occurs " << i << " times in " << list << '\n';
    std::cout << "---------------------------------\n";

    b = equivalent(list, list);
    if (b)
        std::cout << list << " is equivalent to " << list << '\n';
    std::cout << "---------------------------------\n";

    sort(list);
    std::cout << list << " sorted" << '\n';
    std::cout << "---------------------------------\n";

    list = {1, 5, 3, 10, 3, 7, 5, 2};
    std::cout << "Before: " << list << '\n';
    b = remove_first(list, 3);
    std::cout << "After removing the first 3: " << list << '\n';
    std::cout << "---------------------------------\n";
}
