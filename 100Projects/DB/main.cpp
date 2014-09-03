#include <iostream>
#include <cstdio>
#include <string>

using namespace std;
#define MAX 1000000

class Node
{
public:
	string key;
	string value;
	Node *left;
	Node *right;
	Node(string key, string value);
	~Node();
};

Node::Node(string key, string value)
{
	Node::key = key;
    Node::value = value;
	left = NULL;
	right = NULL; 
}

Node::~Node()
{

}

class Tree
{
public:
	Node *root;
	Tree(string key, string value);
	Tree();
	void addNode(string key, string value);
	Node* findNode(string key);
};

Tree::Tree()
{

}

Tree::Tree(string key, string value)
{
	root = new Node(key, value);
}

void Tree::addNode(string key, string value)
{
	Node *temp = new Node(key, value);
	Node *curr = root;

	if (root  == NULL)
	{
		root = temp;
	}

	while (curr != NULL)
	{
		int cmp = key.compare(curr->key);
		if (cmp < 0) {
			if (curr->left == NULL)
			{
				curr->left = temp;
				break;
			}
			curr = curr->left;
		} else {
			if (curr->right == NULL)
			{
				curr->right = temp;
				break;
			}
			curr = curr->right;
		}
	}
}

Node* Tree::findNode(string key)
{
	Node *curr = root;

	while (curr != NULL)
	{
		int cmp = key.compare(curr->key);
		if (cmp < 0)
		{
			curr = curr->left; 
		} else if (cmp > 0) {
			curr = curr->right;
		} else {
			break;
		}
	}

	return curr;
}

void testNode()
{
	// creating node
	Node *s = new Node("Test", "Data");
	// checking if values stored
	assert(*s->key == "Test");
	assert(*s->value == "Data");
	assert(*s->left == NULL);
	assert(*s->right == NULL);
}

void assert(bool )
{

}

void testTree()
{
	//creating Tree
	Tree db;
	// inserting Node
	db.addNode("Test1", "Data1");
	assert(db->root->key == "Test");
	assert(db->root->value == "Data");
	assert(db->root->left == NULL);
	assert(db->root->right == NULL);

	db.addNode("Error", "Wrong!");
	assert(db->root->left->key == "Error");
	assert(db->root->left->value == "Wrong!");

	db.addNode("Stone", "Water");
	db.addNode("Force", "Newton");
	db.addNode("Undo", "Doit!");
	db.addNode("Dull", "not at all");

	Node *fn = db.findNode("Force");
	assert(fn->value == "Newton");

	fn = db.findNode("Dull");
	assert(fn->value == "not at all");
}

int main()
{
	int i = 0, j;
	testNode();
	testTree();
	return 0;
}