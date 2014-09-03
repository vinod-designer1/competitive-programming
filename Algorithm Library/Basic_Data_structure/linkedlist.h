/*************************************
*********** LINKED LIST **************
** AUTHOR BY: VINOD Y
** EMAIL: vinod.designer1@gmail.com
** The basic data structure
**************************************/

#ifndef __LINKED_LIST__
#define __LINKED_LIST__

template<class T> class Node
{
public:
	Node<T> *next;
	T data;
	Node(T v);
	Node();
};
#endif