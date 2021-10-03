//  Name: Andrew Hansbury
//  Assignment number: 2 (?)
//  Assignment: Linked Lists
//  File name: llist.cpp
//  Date last modified: September 27, 2021
//  Honor statement: I have neither given nor received any unauthorized help on this assignment.
#include <iostream>
#include <string>
#include "llist.h"

LinkedList::Node::Node(const string &item) : data{item} {};

LinkedList::LinkedList() : head{&LinkedList::Node("*HEAD*")}, tail{&LinkedList::Node("*TAIL*")}
{
    head->next = tail;
    tail->prev = head;
    head->prev = nullptr;
    tail->next = nullptr;
};

int main()
{
    LinkedList list1;
    //std::cout << list1.head->data;
    std::cout << "hi";
}
