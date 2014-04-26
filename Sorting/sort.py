class Sort(object):
	"""docstring for Sort"""
	def __init__(self, items):
		super(Sort, self).__init__()
		self.items = items
		self.itemsLen = len(self.items)

	def insertionSort(self):
		for i in range(1, self.itemsLen):
			j = i
			while j > 0 and (self.items[j] < self.items[j-1]):
				self.swap(j, j-1)
				j = j-1

	def quickSort(self, start, end):
		if (end - start) > 0:
			pivot = self.partition(start, end)
			self.quickSort(start, pivot-1)
			self.quickSort(pivot+1, end)


	def partition(self, start, pivot):
		firstHigh = start

		for i in range(start, pivot):
			if self.items[i] < self.items[pivot]:
				self.swap(i, firstHigh)
				firstHigh += 1

		self.swap(pivot, firstHigh)

		return firstHigh

	def swap(self, fromIn, to):
		temp = self.items[fromIn]
		self.items[fromIn] = self.items[to]
		self.items[to] = temp

	def printItems(self):
		print self.items

items = [4, 2, 5, 12, 9, 1, 3, 11, 7 , 6]

sort = Sort(items)

sort.quickSort(0, len(items)-1)
sort.printItems()

#print " ".join(map(str,ar))
#m = input()
#ar = [int(i) for i in raw_input().strip().split()]