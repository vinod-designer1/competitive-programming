n = input()
adj = []
prnt = [-1]*n
vist = [False]*n
for i in range(n):
	adj.append([])

for i in range(n-1):
	xy = map(int, raw_input().strip().split())
	adj[xy[0]-1].append(xy[1]-1)
	adj[xy[1]-1].append(xy[0]-1)

def dfs(st):
	global vist
	global adj
	global prnt
	
	vist[st] = True
	for vr in adj[st]:
		if not vist[vr]:
			prnt[vr] = st
			dfs(vr)

