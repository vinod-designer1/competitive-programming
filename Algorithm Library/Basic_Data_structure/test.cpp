#include <iostream>
#include <cstdio>
#include "binary_tree.hpp"

using namespace std;

int main()
{
	BinaryTree<int> bt;
	bt.add_node(12);
	bt.add_node(10);
	bt.add_node(9);
	bt.add_node(11);
	bt.add_node(15);
	bt.add_node(13);
	bt.add_node(14);
	bt.add_node(8);
	bt.add_node(16);
	bt.preorder(bt.root);
	cout << endl;
	bt.inorder(bt.root);
	cout << endl;
	bt.postorder(bt.root);
	cout << endl;
	bt.mirror(bt.root);
	cout << endl;
	return 0;
}