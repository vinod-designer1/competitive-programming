VE =  map(int, raw_input().strip().split(' '))
V = VE[0]
E = VE[1]

if E != V-1:
	print 'NO'
else:
	if V == 1:
		print 'YES'
	else:
		adj = []
		vistd = [False]*V
		prnt = [-1]*V
		dfk = []

		for i in range(V):
			adj.append([])

		i = 0
		while i < E:
			xy = map(int, raw_input().strip().split(' '))
			x = xy[0]
			y = xy[1]
			adj[x-1].append(y-1)
			adj[y-1].append(x-1)
			i += 1

		def DFS(st):
			global adj
			global vistd
			global prnt
			global dfk

			dfk.append(st)

			while dfk:
				crP = dfk.pop()
				if not vistd[crP]:
					vistd[crP] = True
					for el in adj[crP]:
						if not vistd[el]:
							prnt[el] = crP
							DFS(el)
		DFS(0)

		tree = True
		for tr in vistd:
			if not tr:
				tree = False
				break
		if tree:
			print 'YES'
		else:
			print 'NO'
