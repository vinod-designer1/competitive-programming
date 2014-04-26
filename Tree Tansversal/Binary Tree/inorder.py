#http://en.wikipedia.org/wiki/Tree_traversal
#In-order (symmetric)
#    Traverse the left subtree.
#    Visit root.
#    Traverse the right subtree.
#In-order traversal is very commonly used on binary search trees 
#because it returns values from the underlying set in order, 
#according to the comparator that set up the binary search tree (hence the name).


#########################
#Depth First Order
#########################

#recursive
def inorder_recursive(bt, node):
	if node == None:
		return 
	inorder_recursive(node.left)
	bt.visit(node)
	inorder_recursive(node.right)

#iterative
def inorder_iterative(bt, node):
	stk = []
	while stk or node != None:
		if node != None:
			stk.push(node)
			node = node.left
		else:
			node = stk.pop()
			bt.visit(node)
			node = node.right

'''
Morris-InOrder ( root )
current = root
while current != NULL do
    if LEFT(current) == NULL then
       print current
       current=RIGHT(current)
    else do
       // set pre to left child of current
       pre=LEFT(current)
       // find rightmost child of the left child of current
       while (RIGHT(pre) != NULL  and RIGHT(pre) != current) do
           pre=RIGHT(pre)
        //if thus is null, link it to current and set current's left as current
        if RIGHT(pre) == NULL then
           RIGHT(pre)=current
           current=LEFT(current)
        // else unlink it, print current and set right child of current as current
        else do
           RIGHT(pre)=NULL
           print current
           current=RIGHT(current)
'''

