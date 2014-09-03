/*************************************
*********** LINKED LIST **************
** AUTHOR BY: VINOD Y
** EMAIL: vinod.designer1@gmail.com
** The basic tree structure
**************************************/

#ifndef __BINARY_TREE__
#define __BINARY_TREE__
template <class T>
class BinaryTree
{
private:
	struct Node;
	Node *current_node;
public:
	Node *root;
	BinaryTree();
	~BinaryTree();
	void add_node(T v);
	void delete_node(T v);
	//Node *search_node(T v);
	bool empty();
	int height() const;
	int size() const;
	void clear();
	void preorder(Node *visit);
	void inorder(Node *visit);
	void postorder(Node *visit);
	void mirror(Node *visit);
};
#endif