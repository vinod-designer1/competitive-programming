n = input()
ar = [True] * n
lap = []
for i in range(n):
	lap.append(map(int, raw_input().split()))

for i in range(n):
	for j in range(i+1, n):
		if lap[i][0] < lap[j][0] and lap[i][1] < lap[j][1] and lap[i][2] < lap[j][2]:
			ar[i] = False
		elif lap[i][0] > lap[j][0] and lap[i][1] > lap[j][1] and lap[i][2] > lap[j][2]:
			ar[j] = False
minc = 2000
minI = -1
for i in range(n):
	if ar[i]:
		if minc > lap[i][3]:
			minc = lap[i][3]
			minI = i
print (minI+1)