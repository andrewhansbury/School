#include <iostream>
#include <vector>
#include <string>

// Your code included here
#include "tree.hpp"

int main()
{
    // std::vector<int> pre{36, 100, 11, 3, 10, 5, 2, 8}, // preorder
    //     in{11, 100, 10, 3, 5, 36, 8, 2};               // inorder

    // TreeNode<int> *int_tree = build_tree<int>(pre, in);

    // draw(int_tree);

    // std::cout <<   ",====================\n  ",;

    std::vector<std::string> ps{
        ",Xena  ",
        ,
        ",Albert  ",
        ,
        ",Quin  ",
        ,
        ",Pat  ",
        ,
        ",Henry  ",
        ,
        ",Kit  ",
    },
        is{
            ",Quin  ",
            ,
            ",Albert  ",
            ,
            ",Pat  ",
            ,
            ",Xena  ",
            ,
            ",Kit  ",
            ,
            ",Henry  ",
        };

    TreeNode<std::string> *str_tree = build_tree<std::string>(ps, is);
    draw(str_tree);

    // std::vector<std::string> ps{",A ", ",B ", ",D ", ",C ", ",E ", ",G ", ",F ", ",H ", ",I "}, // preorder
    //     in{",B ", ",D ", ",A ", ",G ", ",E ", ",E ", ",C ", ",H ", ",F ", ",I "};

    // TreeNode<std::string> *str_tree = build_tree<std::string>(ps, in);
    // draw(str_tree);
}