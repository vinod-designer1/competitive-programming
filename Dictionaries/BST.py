class Tree(object):
	"""docstring for Tree"""
	def __init__(self, item, parent):
		super(Tree, self).__init__()
		self.item   = item
		self.parent = parent
		self.left   = None
		self.right  = None

	def setParentNode(self, parent):
		self.parent = parent

	def setLeftNode(self, left):
		self.left = left

	def setRightNode(self, right):
		self.right = right

class BST(object):
	"""docstring for BST"""
	def __init__(self):
		super(BST, self).__init__()
		self.start = None

	def insertNode(self, tree, item, parent = None, leaf = 'main'):
		if not tree:
			tree = Tree(item, parent)

			if leaf == 'left':
				parent.left = tree
			elif leaf == 'right':
				parent.right = tree

			if not self.start:
				#print 'start'
				self.start = tree

			return;
		
		if item < tree.item:
			#print 'left'
			self.insertNode(tree.left, item, tree, 'left')
		else:
			#print 'right'
			self.insertNode(tree.right, item, tree, 'right')

	def traverseTree(self, tree):
		if tree:
			self.traverseTree(tree.left)
			self.processItem(tree.item)
			self.traverseTree(tree.right)

	def processItem(self, item):
		print item

	def findMinimum(self, tree):
		if not tree:
			return None

		min = tree

		while min.left:
			min = min.left

		return min

	def findMax(self, tree):
		if not tree:
			return None

		max = tree

		while max.right:
			max = max.right

		return max

	def searchTree(self, tree, item):
		if not tree:
			return None

		if tree.item == item:
			return tree

		if item < tree.item:
			return searchTree(tree.left, item)
		else:
			return searchTree(tree.right, item)

bst = BST()
bst.insertNode(None, 4)
bst.insertNode(bst.start, 8)
bst.insertNode(bst.start, 6)
bst.insertNode(bst.start, 3)
bst.insertNode(bst.start, 5)
bst.insertNode(bst.start, 2)

bst.traverseTree(bst.start)






						