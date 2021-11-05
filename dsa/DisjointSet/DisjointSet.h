#ifndef DISJOINT_SET_
#define DISJOINT_SET_

#include <vector>

// Maintains a disjoint set of equivalence classes
class DisjointSet {
    std::vector<int> set;     // The disjoint set data strucure
	int number_of_sets;       // The number of equivalence classes
  public:
	// Construct size sets, each in its own equivalent class
	DisjointSet(int size);

	// Find the equivalence class of n.
	// Uses path compression to reduce the search path
	// of all the elements on the path from n to its
	// representative element.
    int Find(int i);

	// Merge the two equivalence classes s1 and s2.
	// No optimization performed during the union.
	int Union(int s1, int s2);

	// Number of equivalence classes (sets)
	int Cardinality() const;

    // Makes a set in its own equivalence class
    void Make_Set(int i);

	// Unmerge all elements into separate sets.
    // Each element will be a singleton in its 
    // own equivalence class.
	void Split();
};

#endif