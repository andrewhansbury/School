// Name: ANDREW HANSBURY
// Assignment Number: 4
// Assignment: Disjoint Set
// File Name: Maze.cpp
// Date last modified: November 4, 2021
// Honor statement: I have neither given nor received any unauthorized help on this assignment.

#include "DisjointSet.h"
#include <numeric>

// Construct size sets, each in its own equivalent class
DisjointSet::DisjointSet(int size) : number_of_sets(size), set(size)
{
    // Add your code (and add a constructor initializer list as // needed
    for (int i = 0; i < size; i++)
    {
        set[i] = i;
    }
}

// Find the equivalence class of n.
// Uses path compression to reduce the search path
// of all the elements on the path from n to its
// representative element.
int DisjointSet::Find(int i)
{
    // Replace with your code

    if (set[i] == i)
        return i;
    else
        return Find(set[i]);
}

// Merge the two equivalence classes s1 and s2.
// No optimization performed during the union.
int DisjointSet::Union(int s1, int s2)
{
    // Replace with your code
    int set1 = Find(s1);
    int set2 = Find(s2);
    set[set1] = set2;

    return 1;
}

// Number of equivalence classes (sets)
int DisjointSet::Cardinality() const
{
    // Replace with your code
    int count = 0;
    for (int i = 0; i < set.size(); i++)
    {
        if (set[i] == i)
        {
            count++;
        }
    }
    return count;
}

// Makes a set in its own equivalence class
void DisjointSet::Make_Set(int i)
{
    // Add your code
}

// Unmerge all elements into separate sets.
// Each element will be a singleton in its
// own equivalence class.
void DisjointSet::Split()
{
    // Add your code
    iota(set.begin(), set.end(), 0);
}
