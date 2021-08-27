#include <iostream>
#include <vector>
#include "vectorutils.h"
#include <unordered_map>
#include <string>
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

template <typename K, typename V>
void print_map(std::unordered_map<K, V> const &m)
{
    for (auto const &pair : m)
    {
        std::cout << "{" << pair.first << ": " << pair.second << "}\n";
    }
}

bool equivalent(const std::vector<int> &v1, const std::vector<int> &v2)
{
    unordered_map<int, int> v1_frequencies;
    unordered_map<int, int> v2_frequencies;

    for (int num : v1)
    {
        if (v1_frequencies.find(num) == v1_frequencies.end())
        {
            v1_frequencies[num] = 1;
        }
        else
        {
            v1_frequencies[num]++;
        }
    }

    for (int num : v2)
    {
        if (v2_frequencies.find(num) == v2_frequencies.end())
        {
            v2_frequencies[num] = 1;
        }
        else
        {
            v2_frequencies[num]++;
        }
    }

    if (v1_frequencies == v2_frequencies)
    {
        return true;
    }

    return false;
}

void sort(std::vector<int> &v)
{
    int n = v.size();

    if (n == 0)
    {
        return;
    }

    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (v[j] > v[j + 1])
            {
                int temp = v[j];
                v[j] = v[j + 1];
                v[j + 1] = temp;
            }
        }
    }
}

bool remove_first(std::vector<int> &v, int del)
{
    return true;

}

void printArray(std::vector<int> v)
{
    for (int num : v)
    {
        cout << to_string(num) + " ";
    }
    cout << endl;
}

int main()
{
    std::vector<int> list{1, 5, 3, 10, 3, 7, 5, 2};
    std::vector<int> list2{5, 1, 3, 10, 3, 7, 5, 2};
    std::vector<int> l1{};
    std::vector<int> l2{};
    //cout << equivalent(l1, l2);

    printArray(list2);
    sort(list2);
    printArray(list2);
}
