from Queue import *

class Graph():
	def __init__(self, v, directed = True):
		self.V = v
		self.E = 0
		self.adjL = []
		self.adjM = []

		for i in range(v):
			self.adjL.append([])
			self.adjM.append([])
			for j in range(v):
				self.adjM[i].append(0)


		self.directed = directed

		self.bfsQ = Queue()
		self.bfs_colorV = ['W'] * self.V
		self.bfs_parentV = [-1] * self.V
		self.bfs_children = [0] * self.V

		self.dfsS = []
		self.dfs_colorV = ['W'] * self.V
		self.dfs_parentV = [-1] * self.V

	def add_edge(self, x, y):
		self.adjL[x].append(y)
		self.adjM[x][y] = 1
		self.E += 1

		if not self.directed:
			self.adjL[y].append(x)
			self.adjM[y][x] = 1
			self.E += 1

	def add_child(self, v):
		st = v

		while st != -1:
			self.bfs_children[st] += 1
			st = self.bfs_parentV[st]

	def bfs(self, st):

		self.bfsQ.put(st)

		while not self.bfsQ.empty():
			cvr = self.bfsQ.get()
			if self.bfs_colorV[cvr] != 'B':
				for i in self.adjL[cvr]:
					if self.bfs_colorV[i] == 'W':
						self.bfsQ.put(i)
						self.bfs_parentV[i] = cvr
						self.bfs_colorV[i] = 'G'
						self.add_child(cvr)
				self.bfs_colorV[cvr] = 'B'

	def dfs(self, st):

		self.dfsS.append(st)

		if not self.dfsS:
			cvr = self.dfsS.pop()

			if self.dfs_colorV[cvr] != 'B':
				for i in self.adjL[cvr]:
					if self.dfs_colorV[i] == 'W':
						self.dfs_parentV[i] = cvr
						self.dfs_colorV[i] = 'G'
						self.dfs(i)


				self.bfs_colorV[cvr] = 'B'
