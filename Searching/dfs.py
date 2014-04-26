def DFS(adjList, st, V, E):
	parentV = []
	distV = []
	colorV = []
	nextV = []
	processed = []

	for i in range(V):
		parentV.append(-1)
		distV.append(0)
		colorV.append(False)
		processed.append(False)

	nextV.append(st)

	time = 0

	while nextV:
		crv = nextV.pop()
		colorV[crv] = True
		distV[crv] = time

		#process vertex before
			
		for i in adjList[crv]:
			if not colorV[i]:
				nextV.append(i)
				parentV[i] = crv
			#process edge 
		time += 1
		processed[crv] = True
		#process vertex later





