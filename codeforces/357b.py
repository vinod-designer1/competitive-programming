n, m = map(int, raw_input().split())
ar = [0]*(n)
for i in range(m):
	r = map(int, raw_input().split())
	cl = [False]*4
	rm = []
	clLf = []

	for el in r:
		if ar[el-1] != 0:
			cl[ar[el-1]] = True
		else:
			rm.append(el-1)

	for j in range(1,4):
		if not cl[j]:
			clLf.append(j)

	for p in range(len(rm)):
		ar[rm[p]] = clLf[p]

print ' '.join(map(str, ar))