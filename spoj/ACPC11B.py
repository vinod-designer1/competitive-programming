def closetMountains(mt1, mt2, mt1H, mt2H):
	minD = 10**9
	for i in range(mt1H):
		for j in range(mt2H):
			dif = abs(mt2[j] - mt1[i])
			if minD > dif:
				minD = dif
	return minD
t = input()
for i in range(t):
	mt1 = map(int, raw_input().split())
	mt1H = mt1[0]
	mt1 = mt1[1:]
	mt2 = map(int, raw_input().split())
	mt2H = mt2[0]
	mt2 = mt2[1:]
	print closetMountains(mt1, mt2, mt1H, mt2H)