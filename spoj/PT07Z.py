#http://www.spoj.com/problems/PT07Z/
'''
from Queue import *

class Graph():
	def __init__(self, v, directed = True):
		self.V = v
		self.E = 0
		self.adjL = []
		self.adjM = []
		self.incV = [0] * v
		self.outV = [0] * v

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

		self.path_length = [0] * v

	def add_edge(self, x, y):
		self.adjL[x].append(y)
		self.adjM[x][y] = 1
		self.E += 1
		self.outV[x] += 1
		self.incV[y] += 1

		if not self.directed:
			self.adjL[y].append(x)
			self.adjM[y][x] = 1
			self.E += 1

	def Longest_Path(self, st):
		self.dfsS.append(st)

		if len(self.dfsS) > 0:
			cvr = self.dfsS.pop()

			if self.dfs_colorV[cvr] != 'B':
				for i in self.adjL[cvr]:
					if self.dfs_colorV[i] == 'W':
						cl = 1+self.path_length[cvr]
						if self.path_length[i] < cl:
							self.path_length[i] = cl
						self.dfs_parentV[i] = cvr
						self.dfs_colorV[i] = 'G'
						self.Longest_Path(i)


				self.bfs_colorV[cvr] = 'B'


	def add_child(self, v):
		st = v

		while st != -1:
			self.bfs_children[st] += 1
			st = self.bfs_parentV[st]

	def topological_sort(self):
		pass

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

v = input()
grph = Graph(v, False)
#ar = [[1,2],[2,3]]
i = 0
while i < v:
	xy = [int(x) for x in raw_input().strip().split(' ')]
	grph.add_edge((xy[0]-1),(xy[1]-1))

grph.Longest_Path(0)

print max(grph.path_length)


#http://www.spoj.com/problems/PT07Z/

from Queue import *

class Graph():
	def __init__(self, v, directed = True):
		self.V = v
		self.E = 0
		self.adjL = []
		self.adjM = []
		self.incV = [0] * v
		self.outV = [0] * v

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

		self.path_length = [0] * self.V

	def dfs_init(self):
		#self.dfsS = []
		self.dfs_colorV = ['W'] * self.V
		#self.dfs_parentV = [-1] * self.V

		#self.path_length = [0] * self.V


	def add_edge(self, x, y):
		self.adjL[x].append(y)
		self.adjM[x][y] = 1
		self.E += 1
		self.outV[x] += 1
		self.incV[y] += 1

		if not self.directed:
			self.adjL[y].append(x)
			self.adjM[y][x] = 1
			self.E += 1

	def Longest_Path(self, st, ds):
		if self.dfs_colorV[st] == 'W':
			self.dfs_colorV[st] = 'G'
			self.path_length[st] = ds
			for i in self.adjL[st]:
				if self.dfs_colorV[i] == 'W':
					cl = 1+self.path_length[st]
					#self.dfs_parentV[i] = st
					self.Longest_Path(i, cl)

v = input()
grph = Graph(v, False)
#ar = [[1,2],[2,3]]
i = 0
while i < (v-1):
	xy = [int(x) for x in raw_input().strip().split(' ')]
	grph.add_edge((xy[0]-1),(xy[1]-1))
	i += 1

grph.dfs_init()
grph.Longest_Path(0, 0)

i = 0
node = 0
while i < v:
	if(grph.path_length[i]>grph.path_length[node]):
		node=i
	i += 1

grph.dfs_init()
grph.Longest_Path(node, 0)

print max(grph.path_length)

2DFS
1 for finding an end and 1 for findig fathest from that end
'''

def func(node):
    global M
    if (len(node)==0):
        return 0
    else:
        s=[func(nodes[n]) for n in node]
        s.sort()
        m1=s[-1]+1
        m2=0
        if len(s)>1:
            m2=s[-2]+1
        M=max(M,m1+m2)
        return m1

t=input()
nodes={}
for node in range(1,t+1):
    nodes[node]=[]
for i in range(t-1):
    s=raw_input().split()
    a,b=int(s[0]),int(s[1])
    nodes[a].append(b)

M=0
func(nodes[1])
print M
