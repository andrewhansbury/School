//  Name: Andrew Hansbury
//  Assignment number: 1
//  Assignment: Vectors
//  File name: vectorutils.cpp
//  Date last modified: September 1, 2021
//  Honor statement: I have neither given nor received any unauthorized help on this assignment. 
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


bool equivalent(const std::vector<int> &v1, const std::vector<int> &v2)
{
    for (int i =0; i < v1.size(); i++){
        if (find(v2, v1[i]) == -1){
            return false;

        }
        if (count(v1, v1[i]) != count(v2, v1[i])){
            return false;
        } 
    }
    return true;
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
    
    for (int i = 0; i <v.size(); i++){
        if (v[i] == del){
            
            int j = i;
        
            while (j < v.size()-1){
                v[j] = v[j+1];
                j++;
            }
            v.resize(v.size()-1);
            return true;
        }
    }
    
    return false;

}

void printArray(std::vector<int> v)
{
    cout << "{";
    for (int num : v)
    {
        cout << to_string(num) + ", ";
    }
    cout << "}" << endl;
}
