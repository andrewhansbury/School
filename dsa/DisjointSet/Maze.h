#ifndef MAZE_H_
#define MAZE_H_

#include <iostream>
#include <vector>
#include "DisjointSet.h"

// Masking bit patterns stored in the two-dimensional array representing the 
// walls of each maze room
const int NO_WALLS    = 0;                          // 0000
const int LEFT_WALL   = 1;                          // 0001
const int RIGHT_WALL  = 2;                          // 0010
const int TOP_WALL    = 4;                          // 0100
const int BOTTOM_WALL = 8;                          // 1000
const int ALL_WALLS   = LEFT_WALL | RIGHT_WALL
                         | TOP_WALL | BOTTOM_WALL;  // 1111


class Maze {
public:
	const int rows;     // Number of rows in the maze
	const int columns;  // Number of columns in the maze
private:
    std::vector<std::vector<int>> rooms; 

	DisjointSet set;    // Keeps track of the "equivalence" of the rooms (rooms
	                    // connected by a path)
public:
    // Creates a Maze object with the given number of rows and columns
	Maze(int rows, int columns);

    // Returns the room information at the given row, column location, encoded
    // as bit patterns specifies above (LEFT_WALL, RIGHT_WALL, etc.)
	int operator()(int a, int b) const;

    //  Randomly generates a maze
    void build_maze();
};

#endif
