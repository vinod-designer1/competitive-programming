#include "binary_tree.hpp"
#include <iostream>

using namespace std;

template<class T> struct BinaryTree<T>::Node {
	T data;
	Node *left;
	Node *right;
};

template<class T> BinaryTree<T>::BinaryTree()
{
	root = NULL;
}

template<class T> void BinaryTree<T>::add_node(T v)
{
	if (root == NULL)
	{
		root = new Node;
		root->data = v;
		root->left = NULL;
		root->right = NULL;
	} else {
		current_node = root;
		Node *new_node = new Node;
		new_node->data = v;
		new_node->left = NULL;
		new_node->right = NULL;

		while (1 == 1)
		{
			if (current_node->data >= v)
			{
				if (current_node->left == NULL)
				{
					current_node->left = new_node;
					break;
				}

				current_node = current_node->left;
			} else {
				if (current_node->right == NULL)
				{
					current_node->right = new_node;
					break;
				}

				current_node = current_node->right;
			}
		}
	}
}

template<class T> void BinaryTree<T>::delete_node(T v)
{
	current_node = root;
	Node *prev_node = NULL;
	while (current_node != NULL)
	{
		prev_node = current_node;
		if (current_node->data > v)
		{
			current_node = current_node->left;
		} else if (current_node->data < v) {
			current_node = current_node->right;
		} else {
			break;
		}
	}

	//@TODO implementation to delete node
}

// template<class T> Node* BinaryTree<T>::search_node(T v)
// {
// 	current_node = root;
// 	while (current_node != NULL)
// 	{
// 		if (current_node->data > v)
// 		{
// 			current_node = current_node->left;
// 		} else if (current_node->data < v) {
// 			current_node = current_node->right;
// 		} else {
// 			break;
// 		}
// 	}

// 	return current_node;
// }

template<class T> bool BinaryTree<T>::empty()
{
	if (root == NULL) return true;
	return false;
}

template<class T> BinaryTree<T>::~BinaryTree()
{

}

template<class T> void BinaryTree<T>::preorder(Node *visit)
{
	if (visit != NULL)
	{
		cout << visit->data << " ";
	    preorder(visit->left);
	    preorder(visit->right);
	}
}


template<class T> void BinaryTree<T>::inorder(Node *visit)
{
	if (visit != NULL)
	{
		inorder(visit->left);
	    cout << visit->data << " ";
	    inorder(visit->right);
	}
}

template<class T> void BinaryTree<T>::postorder(Node *visit)
{
	if (visit != NULL)
	{
		postorder(visit->left);
	    postorder(visit->right);
	    cout << visit->data << " ";
	}
}

template<class T> void BinaryTree<T>::mirror(Node *visit)
{
	if (visit != NULL)
	{
		mirror(visit->right);
	    cout << visit->data << " ";
	    mirror(visit->left);
	}
}


template class BinaryTree<int>;