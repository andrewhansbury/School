#include <iostream>
#include "Maze.h"


// Creates a Maze object with the given number of rows and columns
// This is a minimal functional constructor; you will need to 
// augment the constructor initalizer list and add code to the
// body.
Maze::Maze(int rows, int columns) : rows(rows), columns(columns),
	                                set(rows*columns) {
    // Add your code (and add to constructor initalizer list as
    // needed.
}


// Returns the room information at the given row, column location, encoded
// as bit patterns specifies above (LEFT_WALL, RIGHT_WALL, etc.)
int Maze::operator()(int row, int column) const {
    // Replace with your code
	return ALL_WALLS;
}


// Randomly generates a maze
void Maze::build_maze() {
    // Add your code
}
