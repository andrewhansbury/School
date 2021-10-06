//  name: annalisse chang, rebecca zaldivar, andrei modiga
//  assignment number: 2
//  assignment: c++ linked list
//  file name: llist.cpp
//  date last modified: oct 4, 2021
//  honor statement: i have neither given nor received any unauthorized help on this assignment

#include "llist.h"
#include <string>

LinkedList::LinkedList() : head(), tail(), len(0){};

LinkedList::Node::Node(const string &item) : data(item), next(new Node("")), prev(new Node("")) {}

LinkedList::Iterator::Iterator(Node *p) : ptr(p) {}

string &LinkedList::Iterator::operator*()
{

    return this->ptr->data;
}

LinkedList::Iterator &LinkedList::Iterator::operator++()
{
    ptr = ptr->next;
    return *this;
}

LinkedList::Iterator LinkedList::Iterator::operator++(int)
{

    Iterator Iter1 = *this;
    ++(*this);
    return Iter1;
}

LinkedList::Iterator &LinkedList::Iterator::operator--()
{
    ptr = ptr->prev;
    return *this;
}

LinkedList::Iterator LinkedList::Iterator::operator--(int)
{
    Iterator Iter1 = *this;
    --(*this);
    return Iter1;
}

bool LinkedList::Iterator::operator==(const Iterator &other)
{
    return other.ptr == this->ptr;
}

bool LinkedList::Iterator::operator!=(const Iterator &other)
{
    return other.ptr != this->ptr;
}

LinkedList::Iterator LinkedList::begin() const
{

    return Iterator(head->next);
}

LinkedList::Iterator LinkedList::end() const
{

    return Iterator(tail);
}

int LinkedList::length() const
{
    return len;
}

void LinkedList::insert(const Iterator &iter, const string &item)
{
    Node *new_node = new Node(item);
    new_node->next = iter.ptr;
    new_node->prev = iter.ptr->prev;
    iter.ptr->prev = new_node;
    iter.ptr->prev->next = new_node;
    len++;
}

LinkedList::LinkedList(const LinkedList &other) : head(new Node("")), tail(new Node("")), len(0)
{
    Iterator iter1 = other.begin();

    while (iter1 != other.end())
    {
        insert(this->end(), iter1.ptr->data);
        iter1++;
    }
}

//deallocation funtion

//assignment operator (iterator func)
//remove
//find (iterator func)
//clear func
//operator==
//operator!=
