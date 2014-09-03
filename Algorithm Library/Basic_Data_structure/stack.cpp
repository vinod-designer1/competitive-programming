#include "stack.h"
#include <iostream>

using namespace std;

template<class T> Stack<T>::Stack()
{
	max_size = 10;
	in_stack = 0;
	head = new Node<T>();
}

template<class T> Stack<T>::Stack(int s)
{
	max_size = s;
	in_stack = 0;
	head = new Node<T>();
}

template<class T> void Stack<T>::push(T v)
{
	if (in_stack == max_size) throw Overflow();
	Node<T> *new_node = new Node<T>(v);
	new_node->next = head->next;
	head->next = new_node;

	in_stack += 1;
}

template<class T> void Stack<T>::pop()
{
	if (in_stack == 0) throw Underflow();
	Node<T> *top_node = head->next;
	head->next = top_node->next;
	delete top_node;

	in_stack -= 1;
}

template<class T> T Stack<T>::top()
{
	if (in_stack == 0) throw Underflow();
	Node<T> *top_node = head->next;
	return top_node->data;
}

template<class T> bool Stack<T>::empty()
{
	if (in_stack == 0) return true;
	return false;
}

template<class T> Stack<T>::~Stack()
{
	
}

template class Stack<int>;
template class Stack<string>;