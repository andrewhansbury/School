// listmain.cpp

#include <iostream>
#include <algorithm>   // For std::for_each
#include "llist.h"   

int main() {
    std::cout << "Starting program\n";
    // Make an empty list
    LinkedList my_list;
    // Insert some elements
    my_list.insert(my_list.end(), "Fred");
    my_list.insert(my_list.end(), "Wilma");
    my_list.insert(my_list.end(), "Betty");
    my_list.insert(my_list.end(), "Dino");
    my_list.insert(my_list.end(), "Barney");
    // Print the list with a loop
    std::cout << "Print the list with a for loop: \n";
    for (string elem : my_list) {
        std::cout << elem << ' ';
    }
    std::cout << '\n';
    // Print the list with a standard algorithm!
    std::cout << "Print the list with std::for_each: \n";
    std::for_each(my_list.begin(), my_list.end(),
        [](const string& s) { std::cout << s << ' '; });
    std::cout << '\n';
    // Remove Dino
    std::cout << "Remove Dino: \n";
    auto p = my_list.find("Dino");
    my_list.remove(p);
    // Print the list with a standard algorithm!
    std::for_each(my_list.begin(), my_list.end(),
        [](const string& s) { std::cout << s << ' '; });
    std::cout << '\n';

    // Print the list backwards
    std::cout << "Print backwards: \n";
    p = my_list.end();
    while (p-- != my_list.begin()) {
        std::cout << *p << ' ';
    }
    std::cout << '\n';

    LinkedList empty;
    // Print the empty list backwards
    std::cout << "Print empty backwards: \n";
    std::cout << '[';
    p = empty.end();
    while (p-- != empty.begin()) {
        std::cout << *p << ' ';
    }
    std::cout << "]\n";

    std::cout << "*** Add lots more test code to convince yourself that ";
    std::cout << "your code is correct. ***\n";







    std::cout << "Print the list, then print after clear():\n";
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    my_list.clear();
    for (string elem : my_list) {
        std::cout << elem << " ";
    }

    std::cout << "\n";
    std::cout << "\n";


    my_list.insert(my_list.end(), "ONE");
    my_list.insert(my_list.end(), "THREE");
    my_list.insert(my_list.end(), "TWO");
    
    empty.insert(empty.end(), "ONE");
    empty.insert(empty.end(), "TWO");
    empty.insert(empty.end(), "THREE");
    

    std::cout << "my_list == empty (shold be 0):\n";
    bool response = my_list == empty;
    std::cout << response;
    std::cout << "\n";

    std::cout << "my_list != empty (should be 1): \n";
    response = my_list != empty;
    std::cout << response;
    std::cout << "\n";

    std::cout << "my_List == empty (should be 0):\n";
    my_list.insert(my_list.end(), "FOUR");
    response = my_list == empty;
    std::cout << response;
    std::cout << "\n";

    std::cout << "my_list != empty (should be 1):\n";
    response = my_list != empty;
    std::cout << response;
    std::cout << "\n";





    std::cout << "\n";
    std::cout << "\n";

    
    my_list.insert(my_list.begin(), "apple");
    my_list.insert(my_list.begin(), "bread");
    my_list.insert(my_list.begin(), "carrot");
    std::cout << "Initialize List 1:\n";
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    LinkedList list2;
    list2.insert(list2.end(), "zero");
    list2.insert(list2.end(), "one");
    list2.insert(list2.end(), "two");
    list2.insert(list2.end(), "three");
    std::cout << "Initialize List 2:\n";
    for (string elem : list2) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    std::cout << "test assignment list2= list1; Print list 1\n";
    list2 = my_list;
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    std::cout << "Print list 2 (should have same item as list1 now):\n";
    for (string elem : list2) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    my_list.insert(my_list.end(), "--LIST 2 SHOULD NOT HAVE THIS--");
    std::cout << "Print list 1:\n";
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    std::cout << "Print list 2 (should not have newly inserted item in list 1):\n";
    for (string elem : list2) {
        std::cout << elem << " ";
    }

    std::cout << "\n";
    std::cout << "\n";

    //Current lists: my_list, list2, empty
    LinkedList copiedlist(my_list);
    std::cout << "Print list1:\n";
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    std::cout << "Print COPIED LIST\n";
    for (string elem : copiedlist) {
        std::cout << elem << " ";
    }
    std::cout << "\n";

    my_list.insert(my_list.end(), "--copylist should not have this--");
    std::cout << "added something to list 1:\n";
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    std::cout << "Print COPIED LIST after assigning something new to list 1:\n";
    for (string elem : copiedlist) {
        std::cout << elem << " ";
    }

    std::cout << "\n";
    std::cout << "\n";
    std::cout << "\n";

    auto a = my_list.begin();
    std::cout << *a++;
    std::cout << "\n";
    std::cout << *++a;


    std::cout << "\n";
    std::cout << "\n";


    std::cout << "Just checking\n";
    for (string elem : my_list) {
        std::cout << elem << " ";
    }
    std::cout << "\n";
    std::cout << *my_list.find("TWOO");







    std::cout << "\n";
    std::cout << "Program finished\n";
}
