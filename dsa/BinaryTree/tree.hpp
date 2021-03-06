//  tree.hpp

#include <vector>

// Represents a node in a binary tree.
template <typename T>
struct TreeNode
{
    T data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(const T &d, TreeNode *lf, TreeNode *rt) : data(d), left(lf), right(rt) {}
};

#include "tree_extra.hpp"

// Draws the binary tree rooted at t.  Invokes the services of the
// overloaded version to do the real work.
template <typename T>
void draw(TreeNode<T> *t)
{
    draw(t, '-', 0);
}

// Builds a binary tree from preorder and inorder traversals.
// Invokes the services of the overloaded version that
// accepts iterators to the vectors.
// Parameter preorder is a vector storing the preorder traversal sequence.
// Parameter inorder is a vector storing the inorder traversal sequence.
// Returns a pointer to the root of the newly created binary tree.
template <typename T>
TreeNode<T> *build_tree(const std::vector<T> &preorder,
                        const std::vector<T> &inorder)
{
    return build_tree<T>(begin(preorder), end(preorder),
                         begin(inorder), end(inorder));
}
