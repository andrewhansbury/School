//Name: ANDREW HANSBURY
//Assignment Number: 3
//Assignment: Binary Tree
//File Name: tree_extra.hpp
//Date last modified: October 19, 2021
//Honor statement: I have neither given nor received any unauthorized help on this assignment.

// Draws the binary tree rooted at t.
// Parameter link is a symbol to print in front of the node to
// which t points indicating the direction of the branch leading
// to the node.
// Parameter depth is proportional to depth of the node to which p
// points.

template <typename T>
static void draw(TreeNode<T> *t, char link, int depth)
{
    /*************************************************
     * Replace following statement with your code
     *************************************************/

    //pre {36, 100, 11, 3, 10, 5, 2, 8}, // preorder
    //in {11, 100, 10, 3, 5, 36, 8, 2};// inorder
    ++depth;
    if (t)
    {

        draw(t->right, '/', depth);

        for (int i = 0; i < depth; i++)
        {

            std::cout << "   ";
        }
        std::cout << link << '[' << t->data << ']' << std::endl;

        draw(t->left, '\\', depth);
    }

    //std::cout << "TODO: Implement draw function\n";
}

// Frees up the space held by the nodes in a binary tree
// rooted at t.
template <typename T>
void dispose(TreeNode<T> *t)
{

    dispose(t->left);
    dispose(t->right);

    delete t;

    /**********************************
     * Add your code here
     **********************************/
}

// Builds a binary tree from preorder and inorder traversals.
// Parameter pre_begin is an iterator to the beginning of the
// preorder traveral sequence.
// Parameter pre_end is an iterator to the end of the preorder
// traveral sequence.
// Parameter in_begin is an iterator to the beginning of the
// inorder traveral sequence.
// Parameter in_end is an iterator to the end of the inorder
// traveral sequence.
// Returns a pointer to the root of the newly created binary tree.
template <typename T>
static TreeNode<T> *build_tree(typename std::vector<T>::const_iterator pre_begin,
                               typename std::vector<T>::const_iterator pre_end,
                               typename std::vector<T>::const_iterator in_begin,
                               typename std::vector<T>::const_iterator in_end)
{
    /*************************************************
     * Replace following statement with your code
     *************************************************/

    int count = 0;
    int pos;
    for (auto t = in_begin; t != in_end; ++t)
    {
        if (*t == *pre_begin)
        {
            //std::cout << count;
            pos = count;
            break;
        }
        count++;
    }

    int size = pre_end - pre_begin;
    if (size < 1)
    {
        return nullptr;
    }

    size = in_end - in_begin;
    if (size < 1)
    {
        return nullptr;
    }

    TreeNode<T> *left = build_tree<T>(pre_begin + 1, pre_begin + pos + 1, in_begin, in_begin + pos);
    TreeNode<T> *right = build_tree<T>(pre_begin + pos + 1, pre_end, in_begin + pos + 1, in_end);

    TreeNode<T> *tree = new TreeNode<T>(*pre_begin, left,
                                        right);

    return tree;
}
