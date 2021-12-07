//  Name: Andrew Hansbury
//  Assignment number: 6
//  Assignment: Edit Distance
//  File name: hansbury-1.cpp
//  Date last modified: December 6, 2021
//  Honor statement: I have neither given nor received any unauthorized help on this assignment.

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

int smallest(int x, int y, int z)
{
    return std::min(std::min(x, y), z);
}

void print_matrix(std::vector<std::vector<int>> matrix, std::string word_1, std::string word_2)
{
    // Printing top word horizontally
    std ::cout << "      ";
    for (int i = 0; i < word_1.length(); i++)
    {
        std::cout << word_1[i] << "  ";
    }
    std::cout << std::endl;

    for (int i = 0; i < matrix.size(); i++)
    {
        // Printing 2nd word vertically
        std::string word_2_copy = " " + word_2;
        std::cout << word_2_copy[i] << " ";

        // Printing matrix
        for (int j = 0; j < matrix[i].size(); j++)
        {
            std::cout << std::setfill(' ') << std::setw(2) << matrix[i][j] << " ";

            // std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int edit_distance(std::string word1, std::string word2)
{
    int distance = 0;

    const int length_1 = word1.length() + 1;
    const int length_2 = word2.length() + 1;

    // Initializes 2D vector based on words' sizes with default value of 0's
    std::vector<int> v(length_1, 0);
    std::vector<std::vector<int>> matrix(length_2, v);

    // Set first collumn
    for (int i = 1; i < matrix.size(); i++)
        matrix[i][0] = i;
    for (int i = 1; i < matrix[0].size(); i++)
        matrix[0][i] = i;

    // Inserting correct values in Matrix
    for (int i = 1; i < matrix.size(); i++)
    {
        for (int j = 1; j < matrix[0].size(); j++)
        {
            if (word1[i - 1] == word2[j - 1])
                matrix[i][j] = matrix[i - 1][j - 1];
            else if (word1[i - 1] != word2[j - 1])
            {
                int left_num = matrix[i][j - 1];
                int diagonal_left_num = matrix[i - 1][j - 1];
                int above_num = matrix[i - 1][j];
                int minimum = smallest(left_num, diagonal_left_num, above_num);

                matrix[i][j] = minimum + 1;
            }
        }
    }

    print_matrix(matrix, word1, word2);

    // Edit distance should be the bottom right element in the Matrix
    distance = matrix[matrix.size() - 1][matrix[0].size() - 1];
    return distance;
}

int main()
{
    std::string word_1 = " ";
    std::string word_2 = " ";

    while (true)
    {
        getline(std::cin, word_1);
        if (word_1 == "")
            break;

        getline(std::cin, word_2);
        if (word_2 == "")
            break;

        std::cout << edit_distance(word_2, word_1) << std::endl;
    }
}
