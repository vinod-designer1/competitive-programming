#28382
f = open('cttree.txt')
n = int(raw_input().strip())
nval = map(int, raw_input().strip().split())
s = sum(nval)
adj = []
prnt = [-1] * n
visit = [False] * n
valF = [0] * n

for i in range(n):
	adj.append([])

for i in range(n-1):
	xy = map(int, raw_input().strip().split())
	adj[xy[0]-1].append(xy[1]-1)
	adj[xy[1]-1].append(xy[0]-1)

def dfsOld(st):
	global adj
	global prnt
	global nval
	global valF

	if visit[st]:
		return 0

	visit[st] = True

	if len(adj[st]) == 1:
		valF[st] = nval[st]
	else:
		c = nval[st]
		for el in adj[st]:
			prnt[el] = st
			c += dfsOld(el)
		valF[st] = c
	return valF[st]


def dfs(st):
	global adj
	global prnt
	global nval
	global valF

	stk = [st]

	while stk:
		cr = stk.pop()
		if not visit[cr]:
			visit[cr] = True
			if len(adj[cr]) == 1:
				valF[cr] += nval[cr]
			else:
				valF[cr] += nval[cr]
				for el in adj[cr]:
					if not visit[el]:
						prnt[el] =  cr
						stk.append(el)
					else:
						if prnt[el] != -1:
							valF[prnt[el]] += valF[el]
			if prnt[cr] != -1:
				valF[prnt[cr]] += valF[cr]
			
	# if visit[st]:
	# 	return 0

	# visit[st] = True

	# if len(adj[st]) == 1:
	# 	valF[st] = nval[st]
	# else:
	# 	c = nval[st]
	# 	for el in adj[st]:
	# 		prnt[el] = st
	# 		c += dfs(el)
	# 	valF[st] = c
	# return valF[st]

root = 0
for i in range(n):
	if len(adj[i]) > 1:
		root = i
		break

dfs(root)
print valF

minV = s

for val in valF:
	otv = s-val
	if abs(otv - val) < minV:
		minV = abs(otv - val)

print minV