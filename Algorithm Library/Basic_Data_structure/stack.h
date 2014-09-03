/*************************************
*********** Stack **************
** AUTHOR BY: VINOD Y
** EMAIL: vinod.designer1@gmail.com
** The basic data structure which depends on linked list
**************************************/

#include "linkedlist.h"

#ifndef __STACK__
#define __STACK__

template<class T> class Stack 
{
private:
	Node<T> *head;
	int max_size;
	int in_stack;
public:
	Stack();
	Stack(int s);
	~Stack();
	class Underflow {};
	class Overflow {};
	void push(T v);
	void pop();
	bool empty();
	T top();
};
#endif