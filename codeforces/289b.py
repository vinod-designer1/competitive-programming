n,m,d = map(int, raw_input().split())

ar = []
isV = True
for i in range(n):
	s = map(int, raw_input().split())
	for j in s:
		ar.append(j)
ar.sort()
md = (n*m)//2
cM = ar[0]%d
mvs = abs(ar[0]-ar[md])
for i in range(1, (n*m)):
	if ar[i]%d != cM:
		isV=False
		break
	else:
		mvs += abs(ar[i]-ar[md])

if isV:
	print mvs/d
else:
	print -1