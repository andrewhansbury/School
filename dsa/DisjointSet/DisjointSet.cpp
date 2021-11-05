#include "DisjointSet.h"

// Construct size sets, each in its own equivalent class
DisjointSet::DisjointSet(int size)  {
	// Add your code (and add a constructor initializer list as // needed
}

// Find the equivalence class of n.
// Uses path compression to reduce the search path
// of all the elements on the path from n to its
// representative element.
int DisjointSet::Find(int i) {
    // Replace with your code
    return -1;
}

// Merge the two equivalence classes s1 and s2.
// No optimization performed during the union.
int DisjointSet::Union(int s1, int s2) {
    // Replace with your code
    return -1;
}

// Number of equivalence classes (sets)
int DisjointSet::Cardinality() const {
    // Replace with your code
    return 0;
}

// Makes a set in its own equivalence class
void DisjointSet::Make_Set(int i) {
    // Add your code
}

// Unmerge all elements into separate sets.
// Each element will be a singleton in its 
// own equivalence class.
void DisjointSet::Split() {
    // Add your code
}
