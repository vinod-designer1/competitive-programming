#https://www.hackerrank.com/challenges/the-quickest-way-up
'''
8
11,5
8,80 32,76 40,92 12,78 22,68 42,94 44,58 52,74 26,98 2,60 24,88
81,53 71,47 73,11 63,29 75,27
6,3
24,72 30,56 20,46 14,96 26,84 4,40
95,19 55,27 47,29
5,12
26,90 44,92 34,80 46,94 18,82
75,11 95,31 67,3 77,41 81,19 73,17 65,37 83,51 79,35 91,13 89,23 59,9
10,11
2,86 34,58 30,92 10,82 16,62 28,52 12,96 26,90 18,98 4,46
43,5 53,23 67,21 55,27 71,37 57,35 45,39 69,7 81,29 49,25 79,31
9,11
2,52 28,76 50,98 16,78 46,64 24,92 6,54 26,68 40,86
99,39 91,47 87,49 95,27 53,31 59,5 73,7 63,43 51,15 75,29 89,19
14,4
10,58 22,64 4,82 24,72 32,96 20,86 48,94 38,84 16,60 56,68 50,62 26,88 44,80 12,70
93,9 85,35 59,57 91,41
11,11
48,68 12,98 54,88 30,62 22,96 20,80 8,84 52,78 34,66 2,72 46,64
93,3 85,47 67,43 91,27 59,45 73,25 57,11 63,23 83,37 75,29 79,19
13,9
4,96 12,94 36,88 10,72 28,56 6,76 14,70 18,52 38,92 26,68 30,82 8,48 24,98
91,7 63,9 65,11 97,15 49,25 73,17 89,27 59,39 53,3
'''

'''
6
4
6
3
6
4
3
2
'''

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
		self.bfs_distance = [-1] * self.V

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

		self.bfs_distance[st] = 0

		while not self.bfsQ.empty():
			cvr = self.bfsQ.get()
			if self.bfs_colorV[cvr] != 'B':
				for i in self.adjL[cvr]:
					if self.bfs_colorV[i] == 'W':
						self.bfsQ.put(i)
						if self.bfs_distance[i] == -1:
								self.bfs_distance[i] = self.bfs_distance[cvr] + 1
						self.bfs_parentV[i] = cvr
						self.bfs_colorV[i] = 'G'
						self.add_child(cvr)
				self.bfs_colorV[cvr] = 'B'

def initBoard(grph):
	for i  in range(100):
		for j in range(1,7):
			if i+j <= 99:
				graph.add_edge(i, i+j)

t = input()
#t = 3
#l = ['4,96 12,94 36,88 10,72 28,56 6,76 14,70 18,52 38,92 26,68 30,82 8,48 24,98', '32,62 44,66 22,58 34,60 2,90', '8,52 6,80 26,42 2,72']
#s = ['91,7 63,9 65,11 97,15 49,25 73,17 89,27 59,39 53,3', '85,7 63,31 87,13 75,11 89,33 57,5 71,15 55,25', '51,19 39,11 37,29 81,3 59,5 79,23 53,7 43,33 77,21']

for i in range(t):
	graph = Graph(100)
	initBoard(graph)
	ls = [int(i) for i in raw_input().strip().split(' ')]


	for xy in l[i].strip().split(' '):
		xy = [int(y) for y in xy.strip().split(',')]
		graph.add_edge(xy[0], xy[1])

	for xy in s[i].strip().split(' '):
		xy = [int(y) for y in xy.strip().split(',')]
		graph.add_edge(xy[0], xy[1])

	graph.bfs(0)

	ary = [99]

	st = 99

	cnt = 1

	while graph.bfs_parentV[st] != 0:
		st = graph.bfs_parentV[st]
		ary.append(st)
		cnt += 1

	rolls = 0

	print len(ary) - 1

	


	











