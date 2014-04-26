#http://en.wikipedia.org/wiki/Threaded_binary_tree
#http://web.cs.wpi.edu/~cs2102/b10/Lectures/infinite-trees.html
class Node():
	def __init__(self, val=0, parent=None, left=None, right=None):
		self.val = val
		self.parent = parent
		self.left = left
		self.right = right

	def assign_left(self, left=None):
		self.left = left

	def assign_right(self, right=None):
		self.right = right

	def assign_parent(self, parent=None):
		self.parent = parent

	def assign_val(self, val=0):
		self.val = val

class BinaryTree():
	def __init__(self, ar):
		pass

	def visit(self, node):
		print node.val

	def parent(node):
	    if node is node.tree.root:
	        return None
	    else:
	        x = node
	        y = node
	        while True:
	            if is_thread(y.right):
	                p = y.right
	                if p is None or p.left is not node:
	                    p = x
	                    while not is_thread(p.left):
	                        p = p.left
	                    p = p.left
	                return p
	            elif is_thread(x.left):
	                p = x.left
	                if p is None or p.right is not node:
	                    p = y
	                    while not is_thread(p.right):
	                        p = p.right
	                    p = p.right
	                return p
	            x = x.left
	            y = y.right