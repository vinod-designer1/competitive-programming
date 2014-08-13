n = input()
ar = map(int, raw_input().split())
arS = sorted(ar)

for i in range(1,n):
	ar[i] += ar[i-1]
	arS[i] += arS[i-1]

m = input()
for i in range(m):
	t,l,r = map(int, raw_input().split())

	if t == 1:
		if (l-1) > 0:
			print ar[r-1]-ar[l-2]
		else:
			print ar[r-1]
	elif t == 2:
		if (l-1) > 0:
			print arS[r-1]-arS[l-2]
		else:
			print arS[r-1]