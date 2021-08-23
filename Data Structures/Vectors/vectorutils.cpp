#include <iostream>
#include <vector>
#include "vectorutils.h"
//#include <limits.h>

using namespace std;

int maximum(const std::vector<int> &v)
{
    int max_int = v[0];

    for (int num : v)
    {
        if (num > max_int)
        {
            max_int = num;
        }
    }

    return max_int;
}

int find(const std::vector<int> &v, int seek)
{
    for (int i = 0; i < v.size(); i++)
    {

        if (v[i] == seek)
        {
            return i;
        }
    }
    return -1;
}

int count(const std::vector<int> &v, int seek)
{
    int counter = 0;
    for (int i = 0; i < v.size(); i++)
    {

        if (v[i] == seek)
        {
            counter++;
        }
    }
    return counter;
}

bool equivalent(const std::vector<int> &v1, const std::vector<int> &v2)
{
}

int main()
{
    std::vector<int> v{3, 2, 1, 2, 2, 2, 4, 4};
    //cout << maximum(v) << endl;

    //cout << find(v, 2) << endl;

    cout << count(v, 5) << endl;

    return 0;
}