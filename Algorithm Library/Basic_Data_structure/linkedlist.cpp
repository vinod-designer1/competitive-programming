#include "linkedlist.h"
#include <iostream>

using namespace std;

template<class T> Node<T>::Node()
{
	next = NULL;
	data = -1;
}

template<class T> Node<T>::Node(T v)
{
	data = v;
	next = NULL;
}

template class Node<int>;
template class Node<string>;