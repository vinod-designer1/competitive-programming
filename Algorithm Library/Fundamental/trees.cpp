#include <cstdio>

using namespace std;

struct leaf
{
  int value;
  leaf *left;
  leaf *right;
};

struct LL
{
  leaf *root;
  LL *next;
  LL *prev;
};

void add_BT(leaf *root, int value)
{
	// Time Complexity
	//   O(height_of_tree)
	// Space Complexity
	//   O(1)
	leaf *iter = root;
	leaf *t = new leaf;
	t->value = value;

	while (1==1)
	{
		if (iter->value < value)
		{
			if (iter->right == NULL)
			{
				iter->right = t;
				break;
			} else {
				iter = iter->right;
			}

		} else {
			if (iter->left == NULL)
			{
				iter->left = t;
				break;
			} else {
				iter = iter->left;
			}
		}
	}
}

leaf * search_BT(leaf *root, int value)
{
	// Time Complexity
	//   O(height_of_tree)
	// Space Complexity
	//   O(1)
	leaf *iter = root;

	while (1==1)
	{
		if (iter->value == value)
		{
			return iter;
		} else {
			if (iter->value > value)
				iter = iter->left;
			else
				iter = iter->right;
		}
	}
}

void preorder_transversal(leaf *root)
{
	// root then visit left then visit right
	if (root != NULL) 
	{
		printf(" %d ", root->value);
		preorder_transversal(root->left);
		preorder_transversal(root->right);
	}
}

void inorder_transversal(leaf *root)
{
	// left then visit root then visit right
	if (root != NULL) 
	{
		inorder_transversal(root->left);
		printf(" %d ", root->value);
		inorder_transversal(root->right);
	}
}

void postorder_transversal(leaf *root)
{
	// left then visit right then visit root
	if (root != NULL)
	{
		postorder_transversal(root->left);
		postorder_transversal(root->right);
		printf(" %d ", root->value);
	}
}


int main()
{
	leaf *BT = new leaf;
	BT->value = 12;
	add_BT(BT, 14);
	add_BT(BT, 6);
	add_BT(BT, 13);
	add_BT(BT, 7);
	sprial_transversal(BT);
	// leaf *v = search_BT(BT, 7);
	// printf("%d\n", v->value);
	// preorder_transversal(BT);
	// printf("\n");
	// postorder_transversal(BT);
	// printf("\n");
	// inorder_transversal(BT);
	// printf("\n");
}