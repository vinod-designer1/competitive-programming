#http://en.wikipedia.org/wiki/Tree_traversal
#Pre-order
#    Visit the root.
#    Traverse the left subtree.
#    Traverse the right subtree.
#Pre-order traversal while duplicating nodes and values can 
#make a complete duplicate of a binary tree. It can also be used to 
#make a prefix expression (Polish notation) from expression trees:
#traverse the expression tree pre-orderly.

#########################
#Depth First Order
#########################

#recursive
def preorder_recursive(bt, node):
	if node == None:
		return 

	bt.visit(node)
	preorder_recursive(node.left)
	preorder_recursive(node.right)

#iterative
def preorder_iterative(bt, node):
	stk = []
	top = node
	while top != None:
		bt.visit(node)
		if node.right != None:
			stk.push(node.right)
		if node.left != None:
			stk.push(node.left)

		top = stk.pop()


