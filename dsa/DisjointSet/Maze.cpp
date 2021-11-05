// Name: ANDREW HANSBURY
// Assignment Number: 4
// Assignment: Disjoint Set
// File Name: Maze.cpp
// Date last modified: November 4, 2021
// Honor statement: I have neither given nor received any unauthorized help on this assignment.

#include <iostream>
#include "Maze.h"
#include <time.h>
#include <utility>

// Creates a Maze object with the given number of rows and columns
// This is a minimal functional constructor; you will need to
// augment the constructor initalizer list and add code to the
// body.
Maze::Maze(int rows, int columns) : rows(rows), columns(columns),
                                    set(rows * columns), rooms(std::vector<std::vector<int>>(rows, std::vector<int>(columns, ALL_WALLS)))
{
    // Add your code (and add to constructor initalizer list as
    // needed.

    // set.Split()
}

// Returns the room information at the given row, column location, encoded
// as bit patterns specifies above (LEFT_WALL, RIGHT_WALL, etc.)
int Maze::operator()(int row, int column) const
{
    // Replace with your code
    return rooms[row][column];
}

// Randomly generates a maze
void Maze::build_maze()
{
    // Add your code

    set.Split();

    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            rooms[i][j] = ALL_WALLS;

    std::cout << "running build_maze()" << std::endl;

    rooms[0][0] = ~LEFT_WALL;
    rooms[rows - 1][columns - 1] = ~RIGHT_WALL;

    while (set.Cardinality() > 1)
    {

        // selectign random start points
        int i = rows * columns + rand();

        int col = i % columns;

        int room_row = rand() % rows;

        int removal = NO_WALLS, adjacent = NO_WALLS;

        int adjacent_col = col, adjacent_row = room_row;
        // randomize rooms
        // srand(time(NULL));

        if (rand() % 2 == 0)
        {
            if (adjacent_row != 0)
            {

                removal = BOTTOM_WALL, adjacent = TOP_WALL;
                adjacent_row--;
            }

            else if (adjacent_row != rows - 1)
            {

                removal = TOP_WALL, adjacent = BOTTOM_WALL;
                adjacent_row++;
            }

            else
            {

                removal = TOP_WALL, adjacent = BOTTOM_WALL;
                adjacent_row++;
            }
        }

        else
        {
            if (adjacent_col != 0)
            {

                adjacent_col--;
                removal = LEFT_WALL, adjacent = RIGHT_WALL;
            }

            else if ((adjacent_col != columns - 1))
            {

                adjacent_col++;
                removal = RIGHT_WALL, adjacent = LEFT_WALL;
            }

            else
            {
                adjacent_col++;
                removal = RIGHT_WALL, adjacent = LEFT_WALL;
            }
        }

        int curr_room = room_row * columns + col;
        int adjacent_room = adjacent_row * columns + adjacent_col;

        // check for equivalence class
        if (set.Find(curr_room) != set.Find(adjacent_room))
        {
            set.Union((curr_room), (adjacent_room));

            rooms[room_row][col] &= ~removal;
            rooms[adjacent_row][adjacent_col] &= ~adjacent;
        }
    }

    std::cout << "Finished!" << std::endl;
}
