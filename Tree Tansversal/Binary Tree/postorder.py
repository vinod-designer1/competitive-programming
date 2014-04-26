#http://en.wikipedia.org/wiki/Tree_traversal
#Post-order
#    Traverse the left subtree.
#    Traverse the right subtree.
#   Visit the root.
#Post-order traversal while deleting or freeing nodes 
#and values can delete or free an entire binary tree. 
#It can also generate a postfix representation of a binary tree.

#########################
#Depth First Order
#########################

#recursive
def postorder_recursive(bt, node):
	if node == None:
		return 
	inorder_recursive(node.left)
	inorder_recursive(node.right)
	bt.visit(node)

#iterative
def postorder_iterative(bt, node):
	stk = []
	lastnodevisited = None
	while stk or node != None:
		if node != None:
			stk.push(node)
			node = node.left
		else:
			peeknode = stk.peek()
			if peeknode.right != None and peeknode.right != lastnodevisited:
				#/* if right child exists AND traversing node from left child, move right *
				node = peeknode.right
			else:
				stk.pop() 
				bt.visit(peeknode)
				lastnodevisited = peeknode