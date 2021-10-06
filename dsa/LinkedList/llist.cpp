#include "llist.h"

//Name: JAEHYUN PARK, ANDREW HANSBURY
//Assignment Number: 2
//Assignment: Linked List
//File Name: llist.cpp
//Date last modified: October 4, 2021
//Honor statement: I have neither given nor received any unauthorized help on this assignment.


LinkedList::Node::Node(const string& item) : data(item), next(nullptr), prev(nullptr) {}	// Constructor

LinkedList::Iterator::Iterator(LinkedList::Node* p) : ptr(p) {}		//Iterator constructor


#pragma region Iterator methods
string& LinkedList::Iterator::operator*()      // Evaluates to the current object
{
	return ptr->data;
}
LinkedList::Iterator& LinkedList::Iterator::operator++()   // Preincrement the position - increment BEFORE using.
{
	Iterator thisIter = ptr;		///do it like this, or just straight up do ptr = ptr->next????
	thisIter.ptr = ptr->next;	
	ptr = ptr->next;
	return thisIter;
}
LinkedList::Iterator LinkedList::Iterator::operator++(int) // Postincrement the position - increment AFTER using value.
{
	Iterator tempPTR = ptr;
	ptr = ptr->next;
	return tempPTR;
}
LinkedList::Iterator& LinkedList::Iterator::operator--()   // Predecrement the position
{
	Iterator thisIter = ptr;
	thisIter.ptr = ptr->prev;
	ptr = ptr->prev;
	return thisIter;
}
LinkedList::Iterator LinkedList::Iterator::operator--(int) // Postdecrement the position
{
	Iterator tempIter = ptr;
	ptr = ptr->prev;
	return tempIter;
}
// Determines if another iterator pointers to the same
// element in the list
bool LinkedList::Iterator::operator==(const Iterator& other)
{
	if (other.ptr == ptr)
		return true;
	return false;
}
// Determines if another iterator pointers to a different
// element in the list
bool LinkedList::Iterator::operator!=(const Iterator& other)
{
	if (other.ptr != ptr)
		return true;
	return false;
}
#pragma endregion 


LinkedList::LinkedList() : head(new LinkedList::Node ("*HEAD*")), tail(new LinkedList::Node ("*TAIL*")) //default constructor
{
	head->next = tail;
	tail->prev = head;

}

LinkedList::LinkedList(const LinkedList& other) : head(new LinkedList::Node("*HEAD*")), tail(new LinkedList::Node("*TAIL*")) //Copy Constructor
{
	head->next = tail;
	tail->prev = head;
	Iterator otherIter = other.begin();					//set other ptr to first elem
	while (otherIter != other.end())
	{
		insert(end(), *otherIter);		//insert into list2 the item in other's node
		otherIter++;		//increment other ptr?


		//otherIter++; //post
		//++otherIter; //preinc
	}
	//return list2; //... do i return anything for copy constructor?
}

LinkedList::~LinkedList() //destructor - is this right? delete elems, and delete head/tail?
{


	clear();
	Iterator thisIter = begin();
	delete thisIter.ptr->prev;
	delete thisIter.ptr;
}

LinkedList& LinkedList::operator=(const LinkedList& other) //Assignment Operator	//Make list 2 point to list 1? or copy/make new?
{
	// body would call like this?
	// Linkedlist newList;
	// newList = existingList;

	clear();
	Iterator thisIter = begin();		//do I create a new linkedlist, or is it assuming there's already an empty linkedlist to assign to?
	Iterator otherIter = other.begin();

	while (otherIter != other.end())
	{
		insert(end(), *otherIter);
		++otherIter;
	}

	return *this;	//how to refer to this LinkedList itself?
}


LinkedList::Iterator LinkedList::begin() const //Begin method - first elem, not head
{
	Iterator tempiter(head);	//new iterator that points to head
	tempiter.ptr = tempiter.ptr->next;
	return tempiter;		
}

LinkedList::Iterator LinkedList::end() const //End method
{
	Iterator tempiter(tail);
	return tempiter;
}


// Inserts an item into the list before
	// the position indicated by the iterator.
	// To append an item to the back of list lst, use
	//      lst.insert(lst.end(), item);
	// To prepend an item to the front of list lst, use
	//      lst.insert(lst.begin(), item);
	// The insertion does not change the iterator's position. 
void LinkedList::insert(const LinkedList::Iterator& iter, const string& item) //Insert method
{
	Node* newnode = new Node(item);		//proper way - only the pointer to the new node is deleted after function, node itself is a-ok
	//Node newnode(item); - this node would be deleted after ending this function
	//if (iter.ptr == begin().ptr->prev)		//if iter is head
	//{
	//
	//	newnode->next = iter.ptr->next;		//how to properly refer to ptr?
	//	newnode->prev = iter.ptr;
	//	iter.ptr->next->prev = newnode;
	//	iter.ptr->next = newnode;
	//	len++;
	//}
	/*else
	{*/
	newnode->next = iter.ptr;
	newnode->prev = iter.ptr->prev;
	iter.ptr->prev->next = newnode;
	iter.ptr->prev = newnode;
	len++;
	//}
}



// Removes the element at the position indicated by the iterator.
// After the removal the iterator will point to the element after 
// the removed element.
void LinkedList::remove(LinkedList::Iterator& iter) //Remove method
{
	LinkedList::Iterator tempiter = iter.ptr->next;

	iter.ptr->prev->next = iter.ptr->next;
	iter.ptr->next->prev = iter.ptr->prev;
	delete iter.ptr;
	iter.ptr = tempiter.ptr;
	len--;
}


// Returns an iterator to the first occurrence of the element
   // seek.  Returns the list's end iterator if seek is not present 
   // in the list.
LinkedList::Iterator LinkedList::find(const string& seek) const //Find method
{
	Iterator tempPTR = begin();								//how to properly call Iterator methods?
	while (tempPTR != end())
	{
		if (tempPTR.ptr->data == seek)
			return tempPTR;
		tempPTR = tempPTR.ptr->next;
	}
	
	return tempPTR;
}

// Returns the number of elements in the linked list.
int LinkedList::length() const //Length method
{
	return len;
}

// Removes all the elements in the linked list.
void LinkedList::clear() //Clear method
{
	Iterator thisIter = begin();
	while (thisIter.ptr != end().ptr)
	{
		remove(thisIter);		//removes current ptr node AND increments ptr
	}
}

// Returns true if other contains the same elements,
	// in the same order; otherwise, returns false.
bool LinkedList::operator==(const LinkedList& other) const	//Equality operator
{
	Iterator thisIter = begin();
	Iterator otherIter = other.begin();
	if (length() != other.length())
		return false;
	while (thisIter != end()) //maybe try thisIter.ptr != end().ptr?
	{
		if (thisIter.ptr->data != otherIter.ptr->data)
			return false;
		otherIter++;
		thisIter++;
	}
	return true;

}

bool LinkedList::operator!=(const LinkedList& other) const		//Inequality operator
{
	Iterator thisIter = begin();
	Iterator otherIter = other.begin();
	if (length() != other.length())
		return true;
	while (thisIter != end()) //maybe try thisIter.ptr != end().ptr?
	{
		if (thisIter.ptr->data != otherIter.ptr->data)
			return true;
		otherIter++;
		thisIter++;
	}
	return false;
}



