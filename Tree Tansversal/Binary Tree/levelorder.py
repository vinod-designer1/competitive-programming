#http://en.wikipedia.org/wiki/Tree_traversal
from Queue import *

def levelorder(bt, root):
	q = queue()
	q.enqueue(root)
	while not q.empty:
		node = q.dequeue()
		bt.visit(node)

		if node.left != None:
			q.enqueue(node.left)

		if node.right != None:
			q.enqueue(node.right)