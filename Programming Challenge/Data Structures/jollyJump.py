ar = map(int, raw_input().strip().split())
n = ar[0]
ar = ar[1:]
np = [0]*(n-1)
yn = False
for i in range(n-1):
	p = abs(ar[i+1] - ar[i])
	if np[p] == 1:
		yn = True
		break
	else:
		np[p] = 1

if yn:
	print "Not jolly"
else:
	print "Jolly"
