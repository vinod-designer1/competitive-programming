def getVerticalSlit(s, hd, ar):
	if ar[hd]!= None:
		ar[hd].append(s.data)
	else:
		ar[hd] = []
		ar[hd] = [s.data]
	getVerticalSlit(s.left, hd-1, ar)
	getVerticalSlit(s.right, hd+1, ar)

def binaryTree_print_vertical(s):
	h = 0
	ar = {}
	getVerticalSlit(s, hd, ar)

def level_order_transversal(s):
	pass

def inorder_transversal(s):
	if s == None:
		return 0
	inorder_transversal(s.left)

	print s.data

	inorder_transversal(s.right)


def preorder_transversal(s):
	if s == None:
		return 0

	print s.data

	inorder_transversal(s.left)

	inorder_transversal(s.right)

def postorder_transversal(s):
	if s == None:
		return 0

	inorder_transversal(s.left)

	inorder_transversal(s.right)

	print s.data