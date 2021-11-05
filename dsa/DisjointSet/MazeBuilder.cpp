#include <iostream>
#include <vector>
#include <GL/sgl.hpp>
#include "Maze.h"


// Graphical window for presenting a maze object
class MazeWindow : public sgl::Window {
	Maze maze;                   // The maze object to present
	static const int SIZE = 20;  // Size of each room in window units

  public:
	// Constructs a random rows x columns maze.
	MazeWindow(int rows, int columns) :
		Window("Maze", 100, 100, SIZE*(columns + 2), SIZE*(rows + 2),
		       0, SIZE*(columns + 2), 0, SIZE*(rows + 2)), maze(rows, columns) {
        repaint();
	}

	// Renders the maze image in the window
	void paint() override {
		int rows = maze.rows, columns = maze.columns;
        sgl::set_line_width(2);
        sgl::set_color(sgl::BLACK);
		for (int r = 0; r < rows; r++) {
			for (int c = 0; c < columns; c++) {
                int room = maze(r, c);
				if (room & TOP_WALL)       // Draw top wall?
					sgl::draw_line(SIZE * c + SIZE, SIZE * (r + 1) + SIZE,
					               SIZE * (c + 1) + SIZE, SIZE * (r + 1) + SIZE);
				if (room & BOTTOM_WALL)   // Draw bottom wall?
					sgl::draw_line(SIZE * c + SIZE, SIZE * r + SIZE,
					               SIZE * (c + 1) + SIZE, SIZE * r + SIZE);
				if (room & LEFT_WALL)   // Draw left wall?
					sgl::draw_line(SIZE * c + SIZE, SIZE * r + SIZE,
					               SIZE * c + SIZE, SIZE * (r + 1) + SIZE);
				if (room & RIGHT_WALL) // Draw right wall?
					sgl::draw_line(SIZE * (c + 1) + SIZE, SIZE * r + SIZE,
					               SIZE * (c + 1) + SIZE, SIZE * (r + 1) + SIZE);
			}
		}
	}

	void key_pressed(int key, double x, double y) override {
		switch (key) {
			case 'n':
			case 'N':    // Generate new maze
				maze.build_maze();  
				break;
		}
        // Defer further processing to base class
		Window::key_pressed(key, x, y);   
		repaint();
	}
};


// Create and run the maze program
int main() {
    sgl::run<MazeWindow>(30, 50);
}